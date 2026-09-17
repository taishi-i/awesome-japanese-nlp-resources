---
description: Given a Japanese NLP GitHub repo/model/dataset (URL / owner/repo / tool name) OR a topic, find what's already in awesome-japanese-nlp-resources and discover related resources NOT yet listed (contribution candidates). Mines the bundled dataset, then expands via web research across GitHub and Hugging Face.
when_to_use: "Use when the user names a SPECIFIC repository, model, or tool and wants alternatives/equivalents, OR wants to discover Japanese NLP resources for a topic that are NOT yet in the list, OR wants to prepare a contribution. Trigger phrases include 'mecabに似たツール', 'fugashiの代替', 'alternatives to fugashi', 'repos like manga-ocr', 'what else is like sudachi', 'リストに無い新しい日本語NLP', 'awesome-japanese-nlpに追加できそうな', '最近公開された日本語NLPツール', 'find unlisted Japanese NLP repos', 'new Japanese models on Hugging Face', 'contribute a new resource'. For a simple lookup of what already exists, use the search skill instead."
argument-hint: [github-url | huggingface-url | owner/repo | tool-name | topic]
allowed-tools: Bash WebSearch WebFetch
---

Discover Japanese NLP resources related to: "$ARGUMENTS" — both what's already in awesome-japanese-nlp-resources and what's not yet listed.

## Instructions

### Preamble — Establish the current date

Before anything else, run this once and remember the values — every step that mentions a year refers to them:

```bash
echo "YEAR_NOW=$(date +%Y)"
echo "YEAR_PREV=$(($(date +%Y) - 1))"
```

Substitute these wherever this skill writes `${YEAR_NOW}` or `${YEAR_PREV}`. **Do not hardcode years.**

### Step 0 — Handle empty input

If `$ARGUMENTS` is empty or blank, treat it as a **topic-mode** request for a general search for the latest Japanese NLP resources. Use these defaults for the rest of the steps:

- **Topic label**: "Latest Japanese NLP Resources" (use "最新の日本語NLPリソース" only when the user's query was written in Japanese)
- **Keywords for Step 3 (topic mode)**: `llm`, `bert`, `embed`, `speech`, `morpholog` — short stems for local substring matching (a phrase like `japanese language processing` almost never occurs verbatim in a description and would silently match nothing; see Step 3's substring-matching note)
- **WebSearch queries for Step 6**: focus on recency — add `${YEAR_PREV} ${YEAR_NOW}` to every query, and include:
  - `japanese NLP new library github ${YEAR_NOW}`
  - `日本語 NLP 新しい ライブラリ github ${YEAR_NOW}`
  - `japanese NLP new model huggingface ${YEAR_NOW}`
  - `huggingface japanese nlp ${YEAR_PREV} ${YEAR_NOW} new`
- **Output heading**: "Latest Japanese NLP Resources" instead of `Discover: "$ARGUMENTS"`

Then skip Step 1 (mode is topic mode) and continue from Step 2.

### Step 1 — Classify the input: seed mode or topic mode

`$ARGUMENTS` is: "$ARGUMENTS"

**Seed mode** — `$ARGUMENTS` names ONE specific existing repository, model, or tool:

(a) **A direct identifier** — a full GitHub URL (`https://github.com/owner/repo`), a full Hugging Face URL (`https://huggingface.co/owner/name` or `https://huggingface.co/datasets/owner/name`), an `owner/repo` pair, or a bare tool/model name (e.g. `mecab`). Pass it straight through as `SEED`.

(b) **A natural-language phrase wrapping an identifier** (e.g. `mecabに似たツール`, `alternatives to fugashi`) — extract the core identifier (the URL, `owner/repo`, or tool/model name) and pass only that as `SEED`.

If (a) or (b) applies, proceed to Step 2 in **seed mode**.

**Topic mode** — `$ARGUMENTS` is a descriptive/topical phrase with **no single specific name** in it (e.g. `日本語の要約データセット`, `japanese sentiment analysis dataset`, `形態素解析`). There is no identifier to extract and no reason to force one — proceed to Step 2 in **topic mode** directly. Do not invent a seed; topic mode already covers this case via keyword search plus web discovery.

Keep the full `$ARGUMENTS` for the language-detection rule in Step 9.

### Step 2 — Locate the data files

The data ships with the plugin. Resolve paths via `${CLAUDE_PLUGIN_ROOT}` (Claude Code substitutes this inline), falling back to a scoped search only if the install is unusual:

```bash
RESOURCES_PATH="${CLAUDE_PLUGIN_ROOT}/data/resources.json"
[ -f "$RESOURCES_PATH" ] || RESOURCES_PATH="$(find "${HOME}/.claude/plugins" -type f -name resources.json 2>/dev/null | grep "awesome-japanese-nlp-resources/" | head -1)"
echo "RESOURCES_PATH=$RESOURCES_PATH"
```

The plugin also ships `data/multilingual_resources.json` (same item format) listing multilingual GitHub repositories that provide concrete Japanese features, from `docs/multilingual.md`. The scripts below load it automatically when it exists; its items have categories like `Multilingual (Speech recognition)`.

**Topic mode only** — also build the existing-URL set used to filter web candidates in Step 6. The plugin's `resources.json` may lag behind the repo's `README.md`, so prefer the pre-built `data/existing_urls.txt` (emitted by `build_data.py`) when present:

```bash
EXISTING_URLS_FILE=$(mktemp -t awesome_ja_nlp_urls.XXXXXX)
```

```python
python3 << 'EOF'
import json, re, os

RESOURCES_PATH = "RESOURCES_PATH"          # from above
OUTPUT_PATH    = "EXISTING_URLS_FILE"      # from the mktemp above

data_dir = os.path.dirname(os.path.abspath(RESOURCES_PATH))
prebuilt = os.path.join(data_dir, "existing_urls.txt")

urls = set()
source = ""

if os.path.exists(prebuilt):
    with open(prebuilt) as f:
        urls = {line.strip().lower() for line in f if line.strip()}
    source = f"pre-built {prebuilt}"

if not urls:
    with open(RESOURCES_PATH) as f:
        data = json.load(f)
    for item in data:
        u = (item.get("u") or "").lower().rstrip("/")
        if not u:
            continue
        urls.add(u)
        if "github.com/" in u:
            parts = u.split("github.com/", 1)[1].split("/")
            if len(parts) >= 2:
                urls.add(f"https://github.com/{parts[0]}/{parts[1]}".lower())
        elif "huggingface.co/" in u:
            tail = u.split("huggingface.co/", 1)[1]
            is_dataset = tail.startswith("datasets/")
            parts = tail[len("datasets/"):].split("/") if is_dataset else tail.split("/")
            if len(parts) >= 2:
                prefix = "datasets/" if is_dataset else ""
                urls.add(f"https://huggingface.co/{prefix}{parts[0]}/{parts[1]}".lower())
    count_json = len(urls)
    try:
        p = os.path.abspath(data_dir)
        scan_files = []
        for _ in range(6):
            p = os.path.dirname(p)
            readme = os.path.join(p, "README.md")
            if os.path.exists(readme):
                scan_files.append(readme)
            if os.path.exists(os.path.join(p, "awesome-japanese-nlp-resources.json")):
                hf_doc = os.path.join(p, "docs", "huggingface.md")
                if os.path.exists(hf_doc):
                    scan_files.append(hf_doc)
                break
        url_pattern = re.compile(
            r"https://(?:github\.com|huggingface\.co)/(?:datasets/)?[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"
        )
        for scan_file in scan_files:
            before = len(urls)
            with open(scan_file) as f:
                content = f.read()
            for url in url_pattern.findall(content):
                urls.add(url.lower().rstrip("/"))
            if len(urls) > before:
                print(f"Supplemented {len(urls)-before} URLs from {scan_file}")
    except Exception as e:
        print(f"README.md/docs scan skipped ({e}), using resources.json only")
    source = f"derived ({count_json} from JSON, {len(urls)-count_json} from doc walk)"

multilingual_path = os.path.join(data_dir, "multilingual_resources.json")
if os.path.exists(multilingual_path):
    with open(multilingual_path) as f:
        urls.update((item.get("u") or "").lower().rstrip("/") for item in json.load(f))

with open(OUTPUT_PATH, "w") as f:
    f.write("\n".join(sorted(urls)))
print(f"Loaded {len(urls)} existing URLs from {source} → {OUTPUT_PATH}")
EOF
```

Remember to clean up the temp file at the end (`rm -f "$EXISTING_URLS_FILE"`).

### Step 3 — Local matching

**Seed mode**: locate the seed and score every other item by shared category, shared semantic labels, and shared description tokens (IDF-weighted so rare, discriminative labels count more than ubiquitous ones). Substitute `RESOURCES_PATH` (Step 2) and `SEED` (from Step 1):

```python
python3 << 'EOF'
import json, re, math, os
from collections import Counter

RESOURCES_PATH = "RESOURCES_PATH"   # from Step 2
SEED_RAW       = "SEED"             # from Step 1

with open(RESOURCES_PATH) as f:
    data = json.load(f)
multilingual_path = os.path.join(os.path.dirname(RESOURCES_PATH), "multilingual_resources.json")
if os.path.exists(multilingual_path):
    with open(multilingual_path) as f:
        data += json.load(f)
N = len(data)

STOP = {
    "the","and","for","with","that","this","from","into","your","you","are","was",
    "japanese","nlp","python","library","tool","tools","text","based","using","use",
    "used","language","data","model","models","repository","repo","support","simple",
    "fast","easy","also","can","via","etc","https","http","github","com","www","org",
    "not","but","all","any","other","such","more","most","than","its","each","which",
}

def norm_url(u): return (u or "").lower().rstrip("/")
def subs_of(it): return set(t.strip().lower() for t in (it.get("s") or []))
def family(c):   return (c or "").split("(")[0].strip().lower()
def toks(text):
    return set(w for w in re.findall(r"[a-z0-9]+", (text or "").lower())
               if len(w) >= 4 and w not in STOP)

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

sub_df, tok_df = Counter(), Counter()
for x in data:
    for s in subs_of(x): sub_df[s] += 1
    for t in toks((x.get("d") or "") + " " + x["n"] + " " + " ".join(x.get("s") or [])): tok_df[t] += 1
SUB_FLOOR, TOK_FLOOR = 1.5, 1.5
def idf_sub(l): return max(0.0, math.log(N / sub_df.get(l, 1)) - SUB_FLOOR)
def idf_tok(t): return max(0.0, math.log(N / tok_df.get(t, 1)) - TOK_FLOOR)

SUB_W, TOK_W, THRESHOLD = 3.0, 1.5, 8.0

seed_cat  = seed_item["c"]; seed_fam = family(seed_cat)
seed_subs = subs_of(seed_item)
seed_tok  = toks((seed_item.get("d") or "") + " " + seed_item["n"] + " " + " ".join(seed_item.get("s") or []))
seed_name = seed_item["n"].lower()
seed_urls = {norm_url(seed_item["u"])} | {norm_url(x["u"]) for x in matches if x["n"].lower() == seed_name}

results = []
for x in data:
    if x.get("status") == "not_found":
        continue
    if norm_url(x["u"]) in seed_urls:
        continue
    score = 0.0
    if x["c"] == seed_cat:            score += 10
    elif family(x["c"]) == seed_fam:  score += 5
    sh_subs = seed_subs & subs_of(x)
    score += SUB_W * sum(idf_sub(l) for l in sh_subs)
    sh_tok = seed_tok & toks((x.get("d") or "") + " " + x["n"] + " " + " ".join(x.get("s") or []))
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

**Topic mode**: translate the topic to 3–5 English keywords (same stem + tool-name conventions as the `search` skill — see its domain table if unsure), then score by keyword match instead of seed fingerprint:

```python
python3 << 'EOF'
import json, os

with open("RESOURCES_PATH") as f:    # from Step 2
    data = json.load(f)
multilingual_path = os.path.join(os.path.dirname("RESOURCES_PATH"), "multilingual_resources.json")
if os.path.exists(multilingual_path):
    with open(multilingual_path) as f:
        data += json.load(f)

keywords = ["keyword1", "keyword2", "keyword3"]  # from Step 1 (topic mode)

results = []
for item in data:
    if item.get("status") == "not_found":
        continue
    n = item.get("n", "").lower()
    d = item.get("d", "").lower()
    s = " ".join(item.get("s") or []).lower()
    c = item.get("c", "").lower()
    al = " ".join(item.get("al") or []).lower()

    text_score = 0
    for kw in keywords:
        kw = kw.lower()
        if n == kw:       text_score += 20
        elif kw in n:     text_score += 10
        if kw in d:       text_score += 5
        if kw in s:       text_score += 3
        if kw in c:       text_score += 2
        if kw in al:      text_score += 10

    if text_score < 8:
        continue
    ns = item.get("ns") or 0
    nd = item.get("nd") or 0
    results.append((text_score + max(ns, nd) * 2.5, item))

results.sort(key=lambda x: -x[0])
print(f"=== LOCAL MATCHES ({len(results)} candidates; showing top 15) ===")
for combined, item in results[:15]:
    st = item.get("st", 0) or 0; dl = item.get("dl", 0) or 0
    print(f"score={combined:.1f} st={st} dl={dl}")
    print(f"  n={item['n']}")
    print(f"  u={item['u']}")
    print(f"  c={item['c']}")
    print(f"  s={item.get('s','')}")
    print(f"  d={item.get('d','')[:120]}")
    print()
EOF
```

This prints the resolved seed (seed mode) or keyword matches (topic mode), plus up to 15 local candidates. Use the shared labels/terms (seed mode) or matched keywords (topic mode) to justify the "Why" column later.

### Step 4 — Seed mode only: if the seed is not in the dataset

If Step 3 printed `SEED_NOT_FOUND`:

1. If the seed looks like a GitHub URL or `owner/repo`, `WebFetch` it:
   ```
   WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: name, one-line description, primary language, the NLP task it performs, star count, and whether it targets Japanese. If a field is unavailable, set it to null."
   ```
   If it looks like a Hugging Face URL, `WebFetch` it instead:
   ```
   WebFetch url="https://huggingface.co/<owner>/<name>" prompt="Extract as JSON: name, one-line description / model card summary, pipeline or task tag, whether it is a model or a dataset, downloads count, likes count, and whether it targets Japanese. If a field is unavailable, set it to null."
   ```
   If it's a bare name with no domain hint, run one WebSearch (`<name> japanese nlp`) to identify what it does and where it lives.
2. From the seed's inferred task, derive 4–6 English stem keywords and re-run the Step 3 topic-mode script in keyword mode to recover the closest local items. Treat its top ~10 as the "local matches" set.
3. Continue to Step 5. In the final output, note that the seed itself is **not yet in the list**.

If the seed cannot be found locally or resolved on the web, this is the **only** case where you stop and report back: state what you tried, and suggest `/awesome-japanese-nlp-resources:search "$ARGUMENTS"`.

### Step 5 — Derive web-search queries

**Seed mode** — using the seed's task and category, build 6–8 queries mixing GitHub and Hugging Face, English and Japanese:

GitHub-oriented: `<seed-name> alternative github`, `<seed-name> vs`, `japanese <task> library github`, `日本語 <task> ライブラリ github`, `<seed-name> 類似 ツール`
Hugging Face-oriented: `<seed-name> alternative huggingface`, `japanese <task> huggingface`, `huggingface japanese <task>`

**Topic mode** — reuse the same keywords derived in Step 3 (the `search` skill's domain-table conventions), build 6–9 queries. Unlike Step 3's local substring matching, these are search-engine queries, so natural multi-word phrasing (e.g. `japanese sentence embedding`) works fine here even where it wouldn't as a literal substring:

GitHub-oriented: `<keyword> japanese site:github.com`, `japanese <keyword> ${YEAR_NOW} site:github.com`, `<topic> 日本語 github`, `awesome japanese <keyword>`
Hugging Face-oriented (always include at least 2–3): `<keyword> japanese site:huggingface.co`, `huggingface japanese <keyword> ${YEAR_NOW}`, `<topic> 日本語 huggingface`

Both modes: add `${YEAR_NOW}` recency variants when the topic is fast-moving (LLMs, embeddings, speech).

### Step 6 — Web research

Use **WebSearch + WebFetch only — do not use the `gh` CLI in this project.**

Run the queries from Step 5 (6–9 of them). From each result, extract every URL matching:
- `https://github.com/<owner>/<repo>` (ignore deeper paths like `/issues`, `/pull/`, `/blob/`, `/tree/`)
- `https://huggingface.co/<owner>/<name>` for models, `https://huggingface.co/datasets/<owner>/<name>` for datasets (ignore deeper paths)

Collect them, lowercased, trailing slashes stripped, tagged by kind (`github` / `hf_model` / `hf_dataset`), de-duplicated by `owner/repo` (or `owner/name`) **within each kind**, and drop the seed itself (seed mode).

**Keep only resources NOT already in the dataset** — this section reports unlisted items only; anything already catalogued belongs in the "Already in the list" table from Step 3.

**Seed mode**: check candidates directly against `resources.json` (substituting `RESOURCES_PATH` from Step 2):
```bash
grep -iqE "github\.com/<owner>/<repo>[\"/]" "$RESOURCES_PATH" "$(dirname "$RESOURCES_PATH")/multilingual_resources.json" 2>/dev/null && echo "in list — drop" || echo "unlisted — keep"
```

**Topic mode**: check candidates against `$EXISTING_URLS_FILE` (the temp file from Step 2) instead — it also covers items that only exist in the live README, not yet synced to `resources.json`:
```bash
grep -iqxF "https://github.com/<owner>/<repo>" "$EXISTING_URLS_FILE" && echo "in list — drop" || echo "unlisted — keep"
```

Cap the survivors at 10–15 total (seed mode: 5, spread across both kinds), prioritizing candidates that appear in multiple result sets and keeping a mix of both platforms.

### Step 7 — Enrich survivors via WebFetch

For each surviving candidate, `WebFetch` the page (up to 5 calls in parallel — single message, multiple tool calls):

For `github` candidates:
```
WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: name, one-line description, primary language, star count, last-updated date (YYYY-MM), whether archived, whether a fork, and what NLP task it performs. Note if it targets Japanese."
```

For `hf_model` / `hf_dataset` candidates:
```
WebFetch url="https://huggingface.co/<owner>/<name>" prompt="Extract as JSON: name, one-line description / model card summary, pipeline or task tag, whether model or dataset, downloads count, likes count, last-updated date (YYYY-MM), and what NLP task it performs. Note if it targets Japanese."
```

Drop any candidate that: is archived (GitHub); is an inactive/throwaway fork (keep only if independently maintained and published — e.g. on PyPI/crates.io/npm — with a distinct improvement); clearly does not perform the same/related task; is not Japanese-NLP-related (unless a widely-known direct equivalent); or (topic mode, general-search default) has `stars < 3` / `likes < 3` AND is >24 months stale. Keep stars/downloads/likes and last-updated for the survivors.

### Step 8 — Categorize the unlisted candidates

Group survivors under awesome-japanese-nlp-resources section headings, contribution-ready:

**Hugging Face candidates** go to "Hugging Face model" or "Hugging Face dataset", inferred from the WebFetch result (`hf_model`/`hf_dataset` kind, or whether the URL contains `/datasets/`).

**GitHub candidates** are grouped by primary language and description:

| Heading | Cues |
|---|---|
| Python library / C++ / Rust crate / JavaScript / Go / Java | primary language |
| Pretrained model | "model", "weights", "fine-tuned", links to HuggingFace |
| ChatGPT / LLM application | LLM app, RAG, agent |
| Dictionary and IME | dictionary, lexicon, IME |
| Corpus | corpus, dataset, annotation |
| Tutorial | tutorial, course, lecture, "学習", "入門" |
| Research summary | survey, paper list, "サーベイ" |

### Step 9 — Format the output

**Language detection rule (apply before writing any output):**
- `$ARGUMENTS` is empty → **English**
- `$ARGUMENTS` contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English**

Apply the detected language to all headings and prose. Repository/model descriptions stay in **English** (the awesome list standard).

**English output template:**

```
## Discover: "$ARGUMENTS"

**Seed:** [<seed-name>](<seed-url>) — <category> — <one-line what it does>    ← seed mode only
*(Similarity from the bundled dataset + web research across GitHub and Hugging Face)*

### Already in awesome-japanese-nlp-resources

| # | Repository | Category | Popularity | Why |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N / 📥N | shares <task/labels> (seed mode) or matched <keywords> (topic mode) |

*(Omit this table, with a one-line note, if Step 3 found nothing.)*

### Not yet in the list — candidates

Found **N** resources not yet in awesome-japanese-nlp-resources (**G** GitHub, **H** Hugging Face).

#### Python library
* [repo-name](https://github.com/owner/repo) - One-line English description. (⭐ 123, last updated: YYYY-MM)

#### Hugging Face model
* [model-name](https://huggingface.co/owner/name) - 📥 {downloads} / ⭐ {likes} / One-line English description.

*(Only the section headings that actually have candidates. Omit the whole block, with a one-line note, if Step 6/7 found nothing unlisted.)*

### Recommendation

- **Closest alternative** (seed mode) or **Highlight** (topic mode): [name](url) — one-line reason.
- **Next step:** `/awesome-japanese-nlp-resources:search <query>` for the full catalog, or `/awesome-japanese-nlp-resources:research <topic>` for a trend/challenge report.

Sources:
- [Title 1](https://...)
```

**Japanese output template (when the query is in Japanese):** mirror the structure with `## "$ARGUMENTS" の発見結果`, `### awesome-japanese-nlp-resources 内の既存リソース`, `### 未収録の候補`, `### おすすめ`, and per-bullet suffixes `(⭐ N, 最終更新: YYYY-MM)`.

**Rules:**
- "Already in the list" table: 3–8 rows (seed mode) or up to 10 (topic mode); ⭐ for GitHub stars, 📥 for HF downloads, omit if both 0.
- "Not yet in the list": every row **must** be confirmed absent from the dataset in Step 6 — never show a catalogued repo here. Bullet format matches the repo's own contribution style exactly (paste-ready for a PR): GitHub `* [name](url) - description. (⭐ N, last updated: YYYY-MM)`; Hugging Face `* [name](url) - 📥 {downloads} / ⭐ {likes} / description.` (abbreviate with `k`/`M`, e.g. `📥 367k`).
- Descriptions ≤ 100 characters, always in **English**, even if the source card/README is Japanese.
- `Sources:` is **mandatory** (WebSearch requirement) — list the result URLs actually used.
- If nothing survives Step 6/7 in topic mode, or the seed already has no siblings in seed mode, say so plainly rather than padding.

### Step 10 — Edge cases

- **Seed not in the dataset** (seed mode): handled in Step 4 — say so in the output; the seed itself may be worth adding.
- **Seed found but few/no local siblings**: keep the first table small and lean on the web results.
- **Ambiguous seed** (Step 3 reported multiple matches): state which entry was treated as the seed and list alternatives so the user can re-run with a precise URL.
- **No unlisted web results**: omit the "Not yet in the list" section, note it explicitly — this itself signals the list already covers the area well.
- **Descriptive phrase that could resolve to seed OR topic mode**: prefer topic mode unless a specific, recognizable tool/product name is clearly present — topic mode's keyword search plus web discovery already covers broad requests well, and forcing a fake seed narrows the results unnecessarily.
