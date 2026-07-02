---
description: Given a Japanese NLP GitHub repo or Hugging Face model/dataset (URL / owner/repo / tool name), find repositories or models/datasets that do the same or related processing. Mines the bundled dataset for content-similar items, then expands via web research across both GitHub and Hugging Face, then merges and re-ranks.
when_to_use: "Use when the user names a SPECIFIC repository, model, or tool and wants ones like it — alternatives, equivalents, or related tools. Trigger phrases include 'mecabに似たツール', 'fugashiの代替', 'ginzaと同じことができるライブラリ', '〜の類似リポジトリ', '〜の代わり', 'alternatives to fugashi', 'repos like manga-ocr', 'tools similar to oseti', 'what else is like sudachi', 'models like rinna/japanese-gpt-neox-small'. For a topic/keyword search use the search skill; to find repos NOT yet in the list use find-new-resources."
argument-hint: [github-url | huggingface-url | owner/repo | tool-name]
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

This skill needs a seed repository, model, or tool. If `$ARGUMENTS` is empty or blank, **stop immediately** and output:

```
Usage: /awesome-japanese-nlp-resources:similar-resources <github-url | huggingface-url | owner/repo | tool-name>

Examples:
  /awesome-japanese-nlp-resources:similar-resources mecab
  /awesome-japanese-nlp-resources:similar-resources fugashi
  /awesome-japanese-nlp-resources:similar-resources https://github.com/polm/cutlet
  /awesome-japanese-nlp-resources:similar-resources WorksApplications/Sudachi
  /awesome-japanese-nlp-resources:similar-resources manga-ocr
  /awesome-japanese-nlp-resources:similar-resources https://huggingface.co/cl-nagoya/ruri-large

Pass the repository/model (URL, owner/repo, or a tool/model name) you want similar resources for.

---

使い方: /awesome-japanese-nlp-resources:similar-resources <github-url | huggingface-url | owner/repo | tool-name>

例:
  /awesome-japanese-nlp-resources:similar-resources mecab
  /awesome-japanese-nlp-resources:similar-resources 形態素解析 nagisa
  /awesome-japanese-nlp-resources:similar-resources https://github.com/polm/cutlet
  /awesome-japanese-nlp-resources:similar-resources WorksApplications/Sudachi
  /awesome-japanese-nlp-resources:similar-resources manga-ocr
  /awesome-japanese-nlp-resources:similar-resources https://huggingface.co/cl-nagoya/ruri-large

類似リソースを探したいリポジトリ/モデル（URL / owner/repo / ツール名・モデル名）を引数に指定してください。
```

Do **not** proceed if `$ARGUMENTS` is empty.

### Step 1 — Normalize the seed

The seed is: "$ARGUMENTS". It takes one of three shapes:

**(a) A direct identifier** — a full GitHub URL (`https://github.com/owner/repo`), a full Hugging Face URL (`https://huggingface.co/owner/name` or `https://huggingface.co/datasets/owner/name`), an `owner/repo` pair, or a bare tool/model name (e.g. `mecab`). Pass it straight through as `SEED`; the Step 3 script handles all these forms.

**(b) A natural-language phrase wrapping an identifier** (e.g. `mecabに似たツール`, `alternatives to fugashi`, `形態素解析 nagisa`) — first **extract the core identifier** (the URL, `owner/repo`, or tool/model name) and pass only that as `SEED`.

**(c) A purely descriptive/topic phrase with no specific name in it** (e.g. `クエリを含む日本語NLPデータセット`, `日本語の要約データセット`, `japanese sentiment analysis dataset`) — there is no identifier to extract. **Do not stop and ask the user to name a specific resource.** Instead, infer a concrete seed yourself:
   1. Use your own knowledge of well-known Japanese NLP resources to name the single most representative, canonical resource matching the description (e.g. a widely-cited dataset or the most popular tool for that task).
   2. If you're not confident which one is canonical, run one WebSearch to identify it — e.g. `<topic keywords, translated to English> japanese nlp dataset github` or `<topic keywords> japanese huggingface dataset`.
   3. Use that resource's name/URL as `SEED` and continue to Step 3 as normal — it will either resolve locally or fall through to Step 4's web characterization.
   4. In the final output (Step 8), add one line near the top noting which resource you inferred as the seed and why (e.g. "Interpreted as: JSQuAD, the standard Japanese QA dataset"), so the user can redirect you with a more precise seed if it wasn't what they meant. Proceed autonomously — never block on a clarifying question for this skill.

Keep the full `$ARGUMENTS` for the language-detection rule in Step 8.

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
gh_m = re.search(r"github\.com/([^/#?]+/[^/#?]+)", seed)
hf_m = re.search(r"huggingface\.co/(?:datasets/)?([^/#?]+/[^/#?]+)", seed)
slug = (gh_m or hf_m).group(1) if (gh_m or hf_m) else (seed if seed.count("/") == 1 else None)
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

1. If the seed looks like a GitHub URL or `owner/repo`, `WebFetch` it to characterize it:
   ```
   WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: name, one-line description, primary language, the NLP task it performs (e.g. tokenization, OCR, sentiment, translation), star count, and whether it targets Japanese. If a field is unavailable, set it to null."
   ```
   If the seed looks like a Hugging Face URL (contains `huggingface.co`, optionally with a `datasets/` prefix), `WebFetch` it instead:
   ```
   WebFetch url="https://huggingface.co/<owner>/<name>" prompt="Extract as JSON: name, one-line description / model card summary, pipeline or task tag, whether it is a model or a dataset, downloads count, likes count, and whether it targets Japanese. If a field is unavailable, set it to null."
   ```
   If the seed is a bare tool/model name with no domain hint, run one WebSearch (`<name> japanese nlp`) — do not bias it to a single site — to identify what it does and whether it lives on GitHub or Hugging Face.
2. From the seed's inferred **task** + **category**, derive 4–6 English stem keywords (use the same stem + tool-name conventions as the search skill: `morpholog`, `embed`, `classif`, `translat`, `recogni`, `ocr`, `sentiment`, plus tool names like `mecab`, `sudachi`, `bert`, `whisper`).
3. Re-run the Step 3 script logic in keyword mode to recover the closest **local** items — replace the seed-fingerprint scoring with the keyword scorer from the `search` skill (match keywords against `n`/`d`/`s`/`c`). Treat its top ~10 as the "local similar" set.
4. Continue to Step 5. In the final output, note that the seed itself is **not yet in the list** (a candidate for `find-new-resources`).

If the seed (including any seed you inferred in Step 1(c)) is neither found locally nor resolvable on the web, this is the **only** case where you stop and report back instead of guessing further: state which seed you inferred/tried and that it couldn't be verified, and suggest `/awesome-japanese-nlp-resources:search "$ARGUMENTS"`.

### Step 5 — Derive web-search angles

Using the seed's **task** (what it does) and **category**, build 6–8 web queries to find more similar repos **and Hugging Face models/datasets**. **Bias toward Japanese NLP** (the list's scope). Mix English and Japanese, and mix both platforms — always include at least 2 Hugging Face-oriented queries, even when the seed itself is a GitHub repo, since the closest alternative to a tool can be a model or dataset:

GitHub-oriented:
- `<seed-name> alternative github` / `<seed-name> vs`
- `japanese <task> library github` (e.g. `japanese tokenizer library github`)
- `日本語 <task> ライブラリ github`
- `<seed-name> 類似 ツール` / `<seed-name> 代替`

Hugging Face-oriented:
- `<seed-name> alternative huggingface`
- `japanese <task> huggingface` (e.g. `japanese sentence embedding huggingface`)
- `huggingface japanese <task>`

Optional:
- `awesome japanese <task>`
- Recency: `japanese <task> github ${YEAR_NOW}` / `huggingface japanese <task> ${YEAR_NOW}`

`<task>` examples by seed: tokenizer/morphological analyzer → `morphological analysis / tokenizer`; OCR → `ocr / manga ocr`; sentiment → `sentiment analysis`; embeddings → `sentence embedding`; LLM → `llm / language model`.

### Step 6 — Web research

Use **WebSearch + WebFetch only — do not use the `gh` CLI in this project.**

Run **6–8 WebSearch queries** from Step 5. From each result, extract every URL matching:
- `https://github.com/<owner>/<repo>` (ignore deeper paths like `/issues`, `/pull/`, `/blob/`, `/tree/`)
- `https://huggingface.co/<owner>/<name>` for models, `https://huggingface.co/datasets/<owner>/<name>` for datasets (ignore deeper paths like `/tree/`, `/blob/`, `/discussions/`, `/commits/`)

Collect them, lowercased, trailing slashes stripped, tagged with kind (`github` / `hf_model` / `hf_dataset`), de-duplicated by `owner/repo` (or `owner/name`) **within each kind**, and drop the seed itself.

**Keep only resources NOT already in the dataset.** The web section reports **unlisted** items only — anything already catalogued is covered by the "Closest matches" table from Step 3. Drop any candidate whose path is already in `resources.json` (substituting `RESOURCES_PATH` from Step 2 — the `["/]` anchor matches the closing quote or a sub-path in the JSON URL, so `foo/bar` won't match `foo/bar-baz`):

```bash
# github candidate
grep -iqE "github\.com/<owner>/<repo>[\"/]" "$RESOURCES_PATH" && echo "in list — drop" || echo "unlisted — keep"
# hf_model candidate
grep -iqE "huggingface\.co/<owner>/<name>[\"/]" "$RESOURCES_PATH" && echo "in list — drop" || echo "unlisted — keep"
# hf_dataset candidate
grep -iqE "huggingface\.co/datasets/<owner>/<name>[\"/]" "$RESOURCES_PATH" && echo "in list — drop" || echo "unlisted — keep"
```

For the most promising **remaining (unlisted)** candidates (cap at **5, spread across both kinds**), `WebFetch` the page in parallel (single message, multiple calls) to confirm it exists and is relevant.

For `github` candidates:
```
WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: name, one-line description, primary language, star count, last-updated date (YYYY-MM), whether archived, whether a fork, and what NLP task it performs. Note if it targets Japanese."
```

For `hf_model` / `hf_dataset` candidates:
```
WebFetch url="https://huggingface.co/<owner>/<name>" prompt="Extract as JSON: name, one-line description / model card summary, pipeline or task tag, whether it is a model or a dataset, downloads count, likes count, last-updated date (YYYY-MM), and what NLP task it performs. Note if it targets Japanese."
```

Drop any candidate that: is archived (GitHub); is an inactive or throwaway fork (GitHub only — keep a fork **only** if it is independently maintained and published — e.g. on PyPI/crates.io/npm — and offers a distinct improvement, like a maintained successor); clearly does **not** perform the same/related task as the seed; or is not Japanese-NLP-related (unless it is a widely-known direct equivalent worth noting). Keep stars/last-updated (GitHub) or downloads+likes/last-updated (Hugging Face) for the survivors.

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
*(Similarity from the bundled dataset + web research across GitHub and Hugging Face)*
*(Only if the seed was inferred per Step 1(c): "Interpreted "$ARGUMENTS" as: <seed-name> — <one-line reason>. Pass a more specific name/URL to target a different resource.")*

### Closest matches in awesome-japanese-nlp-resources

| # | Repository | Category | Popularity | Why similar |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N / 📥N | shares <task/labels>; <distinguishing note> |
| 2 | ... | ... | ... | ... |

### More from the web (not yet in the list)

| # | Repository | Popularity | Why similar |
|---|---|---|---|
| 1 | [name](url) | ⭐N or 📥N/❤️N (updated YYYY-MM) | <reason> |
| 2 | ... | ... | ... |

### Recommendation

- **Closest alternative:** [name](url) — <one-line why it is the best drop-in match>.
- **If you instead want <variant need>:** [name](url) — <why>.
- **Next step:** run `/awesome-japanese-nlp-resources:search <task>` for the full catalog, or `/awesome-japanese-nlp-resources:find-new-resources <task>` to surface more unlisted repos and models.

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Japanese output template (when the query is in Japanese):**

```
## <seed-name> に類似するリポジトリ

**起点:** [<seed-name>](<seed-url>) — <category> — <何をするツールか一言>
*(バンドル済みデータセット + GitHub / Hugging Face を対象にした Web 調査による類似度)*
*(Step 1(c) でシードを推測した場合のみ: 「"$ARGUMENTS" を <seed-name> と解釈しました — <一言理由>。別のリソースを対象にしたい場合は、より具体的な名前/URLを指定してください。」)*

### awesome-japanese-nlp-resources 内の近いリソース

| # | リポジトリ | カテゴリ | 人気度 | 類似する理由 |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N / 📥N | <共通するタスク/ラベル>; <違い> |
| 2 | ... | ... | ... | ... |

### Web で見つかった未収録リポジトリ

| # | リポジトリ | 人気度 | 類似する理由 |
|---|---|---|---|
| 1 | [name](url) | ⭐N or 📥N/❤️N (更新 YYYY-MM) | <理由> |
| 2 | ... | ... | ... |

### おすすめ

- **最も近い代替:** [name](url) — <最良の乗り換え先である理由を一言>。
- **<別の要件> なら:** [name](url) — <理由>。
- **次の一手:** `/awesome-japanese-nlp-resources:search <task>` で全件、`/awesome-japanese-nlp-resources:find-new-resources <task>` で未収録リポジトリ・モデルをさらに探索。

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Rules:**
- **Closest matches table:** 3–8 rows from the local dataset (fewer if few siblings exist). Use ⭐ for GitHub stars, 📥 for Hugging Face downloads; omit if both are 0.
- **"More from the web" table:** 2–7 rows, **every one not yet in the list** (in-list hits were already dropped in Step 6 — never show a catalogued repo here), mixing GitHub and Hugging Face results rather than favoring one platform. Use ⭐N for GitHub stars, 📥N/❤️N for Hugging Face downloads/likes. If the web surfaced nothing unlisted, omit this table and note "No unlisted similar repositories surfaced on the web."
- **Why similar:** 8–15 words grounded in the `shared_labels` / `shared_terms` and the actual task — not a restatement of the description.
- The **Recommendation** block must name a single closest alternative. The `Sources:` block is **mandatory** (WebSearch requirement) — list the result URLs you actually used.

### Step 9 — Edge cases

- **Seed not in the dataset:** handled in Step 4 — say so, and end with the `find-new-resources` pointer (the seed may be worth adding).
- **Seed found but few/no local siblings:** keep the (possibly empty) first table small and lean on the web table. Note that the dataset has little coverage for this niche.
- **Ambiguous seed** (Step 3 reported multiple matches): state which entry you treated as the seed and list the alternatives so the user can re-run with a precise URL.
- **Descriptive/topic argument with no literal name** (e.g. `クエリを含む日本語NLPデータセット`): handled in Step 1(c) — infer the single most representative concrete resource yourself (own knowledge, or one WebSearch if unsure) and proceed with the full pipeline. **Never stop to ask the user to pick one** — state the inferred seed near the top of the output instead, so they can correct it in a follow-up if needed.
- **No unlisted web results** (the web only surfaced repos already in the list, or nothing): omit the web table, note it explicitly, and present the local matches only — that itself signals the list already covers this niche well.
