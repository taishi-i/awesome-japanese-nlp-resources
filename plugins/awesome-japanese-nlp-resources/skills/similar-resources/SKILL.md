---
description: Given a Japanese NLP GitHub repo (URL / owner/repo / tool name), find repositories that do the same or related processing. Mines the bundled dataset for content-similar items, then expands via web research, then merges and re-ranks.
when_to_use: "Use when the user names a SPECIFIC repository or tool and wants ones like it — alternatives, equivalents, or related tools. Trigger phrases include 'mecabに似たツール', 'fugashiの代替', 'ginzaと同じことができるライブラリ', '〜の類似リポジトリ', '〜の代わり', 'alternatives to fugashi', 'repos like manga-ocr', 'tools similar to oseti', 'what else is like sudachi'. For a topic/keyword search use the search skill; to find repos NOT yet in the list use find-new-resources."
argument-hint: [github-url | owner/repo | tool-name]
allowed-tools: Bash WebSearch WebFetch
---

Find repositories similar to: "$ARGUMENTS" — first from the bundled awesome-japanese-nlp-resources dataset, then from the web.

## Instructions

### Preamble — Establish the current date

Before anything else, run this once and remember the values — every step that mentions a year refers to them:

```bash
echo "YEAR_NOW=$(date +%Y)"
echo "YEAR_PREV=$(($(date +%Y) - 1))"
```

Substitute these wherever this skill writes `${YEAR_NOW}` or `${YEAR_PREV}`. **Do not hardcode years.**

### Step 0 — Validate input

This skill needs a seed repository or tool. If `$ARGUMENTS` is empty or blank, **stop immediately** and output:

```
Usage: /awesome-japanese-nlp-resources:similar-resources <github-url | owner/repo | tool-name>

Examples:
  /awesome-japanese-nlp-resources:similar-resources mecab
  /awesome-japanese-nlp-resources:similar-resources fugashi
  /awesome-japanese-nlp-resources:similar-resources https://github.com/polm/cutlet
  /awesome-japanese-nlp-resources:similar-resources WorksApplications/Sudachi
  /awesome-japanese-nlp-resources:similar-resources manga-ocr

Pass the repository (URL, owner/repo, or a tool name) you want similar resources for.

---

使い方: /awesome-japanese-nlp-resources:similar-resources <github-url | owner/repo | tool-name>

例:
  /awesome-japanese-nlp-resources:similar-resources mecab
  /awesome-japanese-nlp-resources:similar-resources 形態素解析 nagisa
  /awesome-japanese-nlp-resources:similar-resources https://github.com/polm/cutlet
  /awesome-japanese-nlp-resources:similar-resources WorksApplications/Sudachi
  /awesome-japanese-nlp-resources:similar-resources manga-ocr

類似リソースを探したいリポジトリ（URL / owner/repo / ツール名）を引数に指定してください。
```

Do **not** proceed if `$ARGUMENTS` is empty.

### Step 1 — Normalize the seed

The seed is: "$ARGUMENTS". It may be a full GitHub URL (`https://github.com/owner/repo`), an `owner/repo` pair, or a bare tool name (e.g. `mecab`). The Step 3 script handles all three forms.

If `$ARGUMENTS` is wrapped in a natural-language phrase (e.g. `mecabに似たツール`, `alternatives to fugashi`, `形態素解析 nagisa`), first **extract the core identifier** (the URL, `owner/repo`, or tool name) and pass only that to the Step 3 script as `SEED`. Keep the full `$ARGUMENTS` for the language-detection rule in Step 8.

### Step 2 — Locate the data files

The data ships with the plugin. Resolve paths via `${CLAUDE_PLUGIN_ROOT}` (Claude Code substitutes this inline), falling back to a scoped search only if the install is unusual:

```bash
RESOURCES_PATH="${CLAUDE_PLUGIN_ROOT}/data/resources.json"
[ -f "$RESOURCES_PATH" ] || RESOURCES_PATH="$(find "${HOME}/.claude/plugins" -type f -name resources.json 2>/dev/null | grep "awesome-japanese-nlp-resources/" | head -1)"
echo "RESOURCES_PATH=$RESOURCES_PATH"
```

Use the resulting absolute `RESOURCES_PATH` in Steps 3 and 7. (`resources.json` is the only data file this skill needs — the in-list check in Step 7 reads it directly.)

### Step 3 — Locate the seed and score similarity (inline Python)

**Do NOT use the Read tool** on `resources.json` — it exceeds the read limit. Run the following in a single Bash call, substituting `RESOURCES_PATH` (from Step 2) and `SEED` (the raw `$ARGUMENTS` value).

How it works: each item has a category `c` and comma-separated semantic labels `s` (e.g. `"Syntactic Text Processing, Text Segmentation, Tagging, Morphology"`). The script builds a fingerprint of the seed and scores every other item by **same category**, **shared semantic labels**, and **shared description tokens**. Shared labels/tokens are **IDF-weighted** so that rare, discriminative labels (e.g. `Sentiment Analysis`) count far more than ubiquitous ones (e.g. `Dictionary`).

```python
python3 << 'EOF'
import json, re, math

RESOURCES_PATH = "RESOURCES_PATH"   # from Step 2
SEED_RAW       = "SEED"             # the raw $ARGUMENTS value

with open(RESOURCES_PATH) as f:
    data = json.load(f)
N = len(data)

STOP = {
    "the","and","for","with","that","this","from","into","your","you","are","was",
    "japanese","nlp","python","library","tool","tools","text","based","using","use",
    "used","language","data","model","models","repository","repo","support","simple",
    "fast","easy","also","can","via","etc","https","http","github","com","www","org",
    "not","but","all","any","other","such","more","most","than","its","each","which",
}

def norm_url(u): return (u or "").lower().rstrip("/")
def subs_of(it): return set(t.strip().lower() for t in (it.get("s") or "").split(",") if t.strip())
def family(c):   return (c or "").split("(")[0].strip().lower()
def toks(text):
    return set(w for w in re.findall(r"[a-z0-9]+", (text or "").lower())
               if len(w) >= 4 and w not in STOP)

# ---- locate the seed (url -> owner/repo slug -> exact name -> loose) ----
seed = SEED_RAW.strip().lower().rstrip("/")
m = re.search(r"github\.com/([^/#?]+/[^/#?]+)", seed)
slug = m.group(1) if m else (seed if seed.count("/") == 1 else None)
basename = seed.split("/")[-1]

def find_matches():
    exact = [x for x in data if norm_url(x["u"]) == seed]
    if exact: return exact, "exact URL"
    if slug:
        sm = [x for x in data if norm_url(x["u"]).endswith("/" + slug)]
        if sm: return sm, "owner/repo"
        # an explicit owner/repo we don't have: treat as not-found and let Step 4
        # characterize it from the web. Do NOT fall back to a same-named repo from
        # a different owner.
        return [], None
    nm = [x for x in data if x["n"].lower() == basename]
    if nm: return nm, "name"
    loose = [x for x in data if basename and (basename in x["n"].lower() or ("/" + basename) in norm_url(x["u"]))]
    if loose: return loose, "loose substring"
    return [], None

matches, how = find_matches()
matches.sort(key=lambda x: -(max(x.get("ns") or 0, x.get("nd") or 0)))
seed_item = matches[0] if matches else None

if not seed_item:
    print("SEED_NOT_FOUND")
    # surface near-name candidates to help disambiguate / confirm
    near = [x for x in data if basename and basename[:4] and basename[:4] in x["n"].lower()]
    near.sort(key=lambda x: -(max(x.get("ns") or 0, x.get("nd") or 0)))
    for x in near[:8]:
        print(f"  near? {x['n']} | {x['c']} | {x['u']}")
    raise SystemExit

print(f"SEED_FOUND via {how}: {seed_item['n']}")
print(f"  url={seed_item['u']}")
print(f"  c={seed_item['c']}")
print(f"  s={seed_item.get('s','')}")
print(f"  d={seed_item.get('d','')[:200]}")
if len(matches) > 1:
    print(f"  NOTE: {len(matches)} entries matched '{seed}' — chose the most popular. Others:")
    for x in matches[1:6]:
        print(f"    - {x['n']} ({x['u']})")
print()

# ---- IDF tables ----
from collections import Counter
sub_df, tok_df = Counter(), Counter()
for x in data:
    for s in subs_of(x): sub_df[s] += 1
    for t in toks((x.get("d") or "") + " " + x["n"] + " " + (x.get("s") or "")): tok_df[t] += 1
SUB_FLOOR, TOK_FLOOR = 1.5, 1.5     # zero out ubiquitous labels/tokens
def idf_sub(l): return max(0.0, math.log(N / sub_df.get(l, 1)) - SUB_FLOOR)
def idf_tok(t): return max(0.0, math.log(N / tok_df.get(t, 1)) - TOK_FLOOR)

SUB_W, TOK_W, THRESHOLD = 3.0, 1.5, 8.0

seed_cat  = seed_item["c"]; seed_fam = family(seed_cat)
seed_subs = subs_of(seed_item)
seed_tok  = toks((seed_item.get("d") or "") + " " + seed_item["n"] + " " + (seed_item.get("s") or ""))
# exclude the seed itself plus only its EXACT-name twins (e.g. two repos both
# named "mecab") — not unrelated repos that merely share a substring (e.g. the
# many "...Swallow..." models a loose search for "swallow" returns).
seed_name = seed_item["n"].lower()
seed_urls = {norm_url(seed_item["u"])} | {norm_url(x["u"]) for x in matches if x["n"].lower() == seed_name}

results = []
for x in data:
    if norm_url(x["u"]) in seed_urls:
        continue
    score = 0.0
    if x["c"] == seed_cat:            score += 10
    elif family(x["c"]) == seed_fam:  score += 5
    sh_subs = seed_subs & subs_of(x)
    score += SUB_W * sum(idf_sub(l) for l in sh_subs)
    sh_tok = seed_tok & toks((x.get("d") or "") + " " + x["n"] + " " + (x.get("s") or ""))
    score += TOK_W * sum(idf_tok(t) for t in sh_tok)
    if score < THRESHOLD:
        continue
    pop = max(x.get("ns") or 0, x.get("nd") or 0)
    results.append((score + 0.5 * pop, score, sorted(sh_subs), sorted(sh_tok), x))

results.sort(key=lambda r: -r[0])
print(f"=== LOCAL SIMILAR ({len(results)} candidates; showing top 15) ===")
for combined, sc, sh_subs, sh_tok, x in results[:15]:
    st = x.get("st", 0) or 0; dl = x.get("dl", 0) or 0
    print(f"score={combined:.1f}")
    print(f"  n={x['n']}")
    print(f"  u={x['u']}")
    print(f"  c={x['c']}")
    print(f"  st={st} dl={dl}")
    print(f"  shared_labels={', '.join(sh_subs) if sh_subs else '-'}")
    print(f"  shared_terms={', '.join(sh_tok[:6]) if sh_tok else '-'}")
    print(f"  d={x.get('d','')[:120]}")
    print()
EOF
```

This prints the resolved seed and up to 15 local candidates, each with the **shared semantic labels** and **shared terms** that justify the match (use these to write the "Why similar" column later).

### Step 4 — If the seed is not in the dataset

If Step 3 printed `SEED_NOT_FOUND`:

1. If the seed looks like a GitHub repo (URL or `owner/repo`), `WebFetch` it to characterize it:
   ```
   WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: name, one-line description, primary language, the NLP task it performs (e.g. tokenization, OCR, sentiment, translation), star count, and whether it targets Japanese. If a field is unavailable, set it to null."
   ```
   If the seed is a bare tool name, run one WebSearch (`<name> japanese nlp github`) to identify what it does.
2. From the seed's inferred **task** + **category**, derive 4–6 English stem keywords (use the same stem + tool-name conventions as the search skill: `morpholog`, `embed`, `classif`, `translat`, `recogni`, `ocr`, `sentiment`, plus tool names like `mecab`, `sudachi`, `bert`, `whisper`).
3. Re-run the Step 3 script logic in keyword mode to recover the closest **local** items — replace the seed-fingerprint scoring with the keyword scorer from the `search` skill (match keywords against `n`/`d`/`s`/`c`). Treat its top ~10 as the "local similar" set.
4. Continue to Step 5. In the final output, note that the seed itself is **not yet in the list** (a candidate for `find-new-resources`).

If the seed is neither found locally nor resolvable on the web, tell the user the seed could not be identified and suggest `/awesome-japanese-nlp-resources:search "$ARGUMENTS"`, then stop.

### Step 5 — Derive web-search angles

Using the seed's **task** (what it does) and **category**, build 4–6 web queries to find more similar repos. **Bias toward Japanese NLP** (the list's scope). Mix English and Japanese; vary phrasing:

- `<seed-name> alternative github` / `<seed-name> vs`
- `japanese <task> library github` (e.g. `japanese tokenizer library github`)
- `日本語 <task> ライブラリ github`
- `<seed-name> 類似 ツール` / `<seed-name> 代替`
- `awesome japanese <task>`
- Optional recency: `japanese <task> github ${YEAR_NOW}`

`<task>` examples by seed: tokenizer/morphological analyzer → `morphological analysis / tokenizer`; OCR → `ocr / manga ocr`; sentiment → `sentiment analysis`; embeddings → `sentence embedding`; LLM → `llm / language model`.

### Step 6 — Web research

Use **WebSearch + WebFetch only — do not use the `gh` CLI in this project.**

Run **4–6 WebSearch queries** from Step 5. From each result, extract every `https://github.com/<owner>/<repo>` URL (ignore deeper paths like `/issues`, `/pull/`, `/blob/`, `/tree/`). Collect them, lowercased, trailing slashes stripped, de-duplicated by `owner/repo`, and drop the seed itself.

**Keep only repositories NOT already in the dataset.** The web section reports **unlisted** repos only — anything already catalogued is covered by the "Closest matches" table from Step 3. Drop any candidate whose `owner/repo` is already in `resources.json` (substituting `RESOURCES_PATH` from Step 2 — the `["/]` anchor matches the closing quote or a sub-path in the JSON URL, so `foo/bar` won't match `foo/bar-baz`):

```bash
grep -iqE "github\.com/<owner>/<repo>[\"/]" "$RESOURCES_PATH" && echo "in list — drop" || echo "unlisted — keep"
```

For the most promising **remaining (unlisted)** candidates (cap at **5**), `WebFetch` the repo page in parallel (single message, multiple calls) to confirm it exists and is relevant:

```
WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: name, one-line description, primary language, star count, last-updated date (YYYY-MM), whether archived, whether a fork, and what NLP task it performs. Note if it targets Japanese."
```

Drop any candidate that: is archived; is an inactive or throwaway fork (keep a fork **only** if it is independently maintained and published — e.g. on PyPI/crates.io/npm — and offers a distinct improvement, like a maintained successor); clearly does **not** perform the same/related task as the seed; or is not Japanese-NLP-related (unless it is a widely-known direct equivalent worth noting). Keep stars + last-updated for the survivors.

### Step 7 — Re-rank

The two result sets are **disjoint**: local candidates (Step 3/4) are all **in the list**, and the web candidates that survived Step 6 are all **unlisted**. So there is no cross-set de-duplication to do — the local matches populate the first table, the web finds populate the second.

**Re-rank within each set by your judgment**, not mechanically by the Step 3 score. Order by:
   - **Functional closeness** — does it do the *same task with the same kind of input/output* as the seed? (A MeCab wrapper is closer to `fugashi` than a generic NLP toolkit.) Use the `shared_labels` / `shared_terms` from Step 3 as evidence.
   - **Category fit** — same category/ecosystem as the seed ranks higher.
   - **Popularity** as a quality proxy (stars / downloads) when otherwise equivalent.
   - **Recency / maintenance** — prefer actively maintained over abandoned, when otherwise equal.

### Step 8 — Format the output

**Language detection rule (apply before writing any output):**
- `$ARGUMENTS` contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English** (default)

Apply the detected language to all headings and prose. Repository descriptions stay in **English** (the awesome list standard).

**English output template (default):**

```
## Repositories similar to <seed-name>

**Seed:** [<seed-name>](<seed-url>) — <category> — <one-line what it does>
*(Similarity from the bundled dataset + web research)*

### Closest matches in awesome-japanese-nlp-resources

| # | Repository | Category | Popularity | Why similar |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N / 📥N | shares <task/labels>; <distinguishing note> |
| 2 | ... | ... | ... | ... |

### More from the web (not yet in the list)

| # | Repository | Popularity | Why similar |
|---|---|---|---|
| 1 | [name](url) | ⭐N (updated YYYY-MM) | <reason> |
| 2 | ... | ... | ... |

### Recommendation

- **Closest alternative:** [name](url) — <one-line why it is the best drop-in match>.
- **If you instead want <variant need>:** [name](url) — <why>.
- **Next step:** run `/awesome-japanese-nlp-resources:search <task>` for the full catalog, or `/awesome-japanese-nlp-resources:find-new-resources <task>` to surface more unlisted repos.

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Japanese output template (when the query is in Japanese):**

```
## <seed-name> に類似するリポジトリ

**起点:** [<seed-name>](<seed-url>) — <category> — <何をするツールか一言>
*(バンドル済みデータセット + Web 調査による類似度)*

### awesome-japanese-nlp-resources 内の近いリソース

| # | リポジトリ | カテゴリ | 人気度 | 類似する理由 |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N / 📥N | <共通するタスク/ラベル>; <違い> |
| 2 | ... | ... | ... | ... |

### Web で見つかった未収録リポジトリ

| # | リポジトリ | 人気度 | 類似する理由 |
|---|---|---|---|
| 1 | [name](url) | ⭐N (更新 YYYY-MM) | <理由> |
| 2 | ... | ... | ... |

### おすすめ

- **最も近い代替:** [name](url) — <最良の乗り換え先である理由を一言>。
- **<別の要件> なら:** [name](url) — <理由>。
- **次の一手:** `/awesome-japanese-nlp-resources:search <task>` で全件、`/awesome-japanese-nlp-resources:find-new-resources <task>` で未収録リポジトリをさらに探索。

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Rules:**
- **Closest matches table:** 3–8 rows from the local dataset (fewer if few siblings exist). Use ⭐ for GitHub stars, 📥 for Hugging Face downloads; omit if both are 0.
- **"More from the web" table:** 2–7 rows, **every one not yet in the list** (in-list hits were already dropped in Step 6 — never show a catalogued repo here). If the web surfaced nothing unlisted, omit this table and note "No unlisted similar repositories surfaced on the web."
- **Why similar:** 8–15 words grounded in the `shared_labels` / `shared_terms` and the actual task — not a restatement of the description.
- The **Recommendation** block must name a single closest alternative. The `Sources:` block is **mandatory** (WebSearch requirement) — list the result URLs you actually used.

### Step 9 — Edge cases

- **Seed not in the dataset:** handled in Step 4 — say so, and end with the `find-new-resources` pointer (the seed may be worth adding).
- **Seed found but few/no local siblings:** keep the (possibly empty) first table small and lean on the web table. Note that the dataset has little coverage for this niche.
- **Ambiguous seed** (Step 3 reported multiple matches): state which entry you treated as the seed and list the alternatives so the user can re-run with a precise URL.
- **No unlisted web results** (the web only surfaced repos already in the list, or nothing): omit the web table, note it explicitly, and present the local matches only — that itself signals the list already covers this niche well.
