---
name: compare
description: "Compare several Japanese NLP libraries, models, or datasets for a keyword (a specific tool name, or a function/task like '形態素解析') across a handful of criteria chosen for that comparison, rendered as a ○/△/✕ table. Use when the user wants a side-by-side comparison of multiple Japanese NLP tools/libraries/datasets, not just the single best one. Trigger phrases include 'X と Y と Z を比較して', '形態素解析ライブラリを比較', 'MeCab と Sudachi どっちがいい', 'どのツールを使うべき', 'compare japanese tokenizers', 'mecab vs sudachi vs janome', 'which embedding model should I use', '日本語NERライブラリの比較表', 'pros and cons of japanese OCR tools'. For a single ranked list use search; for alternatives to one specific tool (or contribution candidates) without a multi-axis table, use discover."
argument-hint: [tool-name | topic]
allowed-tools: Bash WebSearch WebFetch
---

Compare Japanese NLP resources for the user's query across a few criteria, as a table.

## Claude Code and Codex

This skill is shared by the Claude Code and Codex versions of the plugin. The steps are the same in both tools; only these details differ:

- **Query** — Claude Code: the arguments of `/awesome-japanese-nlp-resources:compare`, appended at the end of this skill as `ARGUMENTS: …`. Codex: the user's message that invoked `$awesome-japanese-nlp-resources:compare`, minus that `$…` mention. If the skill was picked automatically rather than invoked by name, use the user's request as the query.
- **Plugin root** — Claude Code: `${CLAUDE_PLUGIN_ROOT}`. Codex: the directory two levels above this `SKILL.md` (use its absolute path).
- **Shell** — run the commands below with Claude Code's `Bash` tool or Codex's shell tool. Copy each Python script in full and run it as written, changing only its placeholders (`RESOURCES_PATH`, `SEED`, the keyword list) — don't shorten it, drop passes, or alter its scores and thresholds.
- **Web** — Claude Code: `WebSearch` to search and `WebFetch` to read a page. Codex: the built-in web search tool (search, then open the page). Do not use the `gh` CLI, `curl`, or other network commands from the shell.
- **Commands** — write any command you show the user in the current tool's form: `/awesome-japanese-nlp-resources:<skill>` in Claude Code, `$awesome-japanese-nlp-resources:<skill>` in Codex.

Candidates come from the bundled data (Step 3), topped up from the web only as Step 4 describes. If the data file can't be read (for example, shell commands are blocked or fail to start), say so and link https://github.com/taishi-i/awesome-japanese-nlp-resources instead of building the comparison from memory alone.

## Instructions

### Step 0 — Validate input

If the query is empty or blank, **stop immediately** and output (in Codex, write the commands with `$` instead of `/`):

```
Usage: /awesome-japanese-nlp-resources:compare <tool-name | topic>

Examples:
  /awesome-japanese-nlp-resources:compare mecab
  /awesome-japanese-nlp-resources:compare 形態素解析
  /awesome-japanese-nlp-resources:compare japanese sentence embedding models
  /awesome-japanese-nlp-resources:compare OCR

Pass a tool name (to compare it against its closest alternatives) or a topic/function (to compare the leading options for that task).

---

使い方: /awesome-japanese-nlp-resources:compare <ツール名 | トピック>

例:
  /awesome-japanese-nlp-resources:compare mecab
  /awesome-japanese-nlp-resources:compare 形態素解析
  /awesome-japanese-nlp-resources:compare 日本語 文埋め込み モデル
  /awesome-japanese-nlp-resources:compare OCR

比較したいツール名(その代替と比較)、またはトピック/機能名(その分野の主要な選択肢を比較)を引数に指定してください。
```

Do **not** proceed if the query is empty. Unlike `discover`, this skill has no empty-argument default — a comparison needs something to compare.

### Step 1 — Classify the input: seed mode or topic mode

**Seed mode** — names ONE specific existing tool/library/model (a full GitHub/Hugging Face URL, `owner/repo`, or a bare tool name, e.g. `mecab`, `fugashi`). Pass it through as `SEED` and proceed to Step 3 in seed mode — the comparison set will be the seed plus its closest peers.

**Topic mode** — a descriptive/functional phrase with no single specific name (e.g. `形態素解析`, `japanese sentence embedding models`, `OCR`). Proceed to Step 3 in topic mode — the comparison set will be the leading local matches for the topic.

### Step 2 — Locate the data file

```bash
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT}"  # Codex: replace with the plugin root, two levels above this SKILL.md
RESOURCES_PATH="$PLUGIN_ROOT/data/resources.json"
[ -f "$RESOURCES_PATH" ] || RESOURCES_PATH="$(find "${CODEX_HOME:-$HOME/.codex}/plugins" "${HOME}/.claude/plugins" -type f -name resources.json 2>/dev/null | grep "awesome-japanese-nlp-resources/" | head -1)"
echo "RESOURCES_PATH=$RESOURCES_PATH"
```

Write the resulting absolute path into the Step 3 script — shell variables may not persist between commands.

The plugin also ships `data/multilingual_resources.json` (same item format) listing multilingual libraries, models, and datasets (GitHub repositories) that also support Japanese, from `docs/multilingual.md`. The scripts below load it automatically when it exists; its items have categories like `Multilingual (Speech recognition)`.

### Step 3 — Find comparison candidates (inline Python)

**Do not read `resources.json` directly** (no Read tool, `cat`, or `head`). Run one of the two scripts below, substituting `RESOURCES_PATH` (Step 2) and, for seed mode, `SEED` (from Step 1).

**Seed mode** — locate the seed and score peers by shared category, shared semantic labels, and shared description tokens (IDF-weighted):

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
    raise SystemExit

print(f"SEED_FOUND via {how}: {seed_item['n']}")
print(f"  url={seed_item['u']}  c={seed_item['c']}")
print(f"  d={seed_item.get('d','')[:200]}")
print()

sub_df, tok_df = Counter(), Counter()
for x in data:
    for s in subs_of(x): sub_df[s] += 1
    for t in toks((x.get("d") or "") + " " + x["n"] + " " + " ".join(x.get("s") or [])): tok_df[t] += 1
def idf_sub(l): return max(0.0, math.log(N / sub_df.get(l, 1)) - 1.5)
def idf_tok(t): return max(0.0, math.log(N / tok_df.get(t, 1)) - 1.5)

seed_cat  = seed_item["c"]; seed_fam = family(seed_cat)
seed_subs = subs_of(seed_item)
seed_tok  = toks((seed_item.get("d") or "") + " " + seed_item["n"] + " " + " ".join(seed_item.get("s") or []))
seed_name = seed_item["n"].lower()
seed_urls = {norm_url(seed_item["u"])} | {norm_url(x["u"]) for x in matches if x["n"].lower() == seed_name}

results = []
for x in data:
    if x.get("status") == "not_found" or norm_url(x["u"]) in seed_urls:
        continue
    score = 0.0
    if x["c"] == seed_cat:            score += 10
    elif family(x["c"]) == seed_fam:  score += 5
    sh_subs = seed_subs & subs_of(x)
    score += 3.0 * sum(idf_sub(l) for l in sh_subs)
    sh_tok = seed_tok & toks((x.get("d") or "") + " " + x["n"] + " " + " ".join(x.get("s") or []))
    score += 1.5 * sum(idf_tok(t) for t in sh_tok)
    if score < 8.0:
        continue
    pop = max(x.get("ns") or 0, x.get("nd") or 0)
    results.append((score + 0.5 * pop, x))

results.sort(key=lambda r: -r[0])
print(f"=== CANDIDATES ({len(results)} peers found; seed + top 6 shown) ===")
print(f"[seed] n={seed_item['n']}  u={seed_item['u']}  c={seed_item['c']}  d={seed_item.get('d','')[:150]}")
for score, x in results[:6]:
    print(f"score={score:.1f}  n={x['n']}  u={x['u']}  c={x['c']}  d={x.get('d','')[:150]}")
EOF
```

**Topic mode** — score by keyword match (3–5 stems from Step 1, same conventions as `search`):

```python
python3 << 'EOF'
import json, os

with open("RESOURCES_PATH") as f:    # from Step 2
    data = json.load(f)
multilingual_path = os.path.join(os.path.dirname("RESOURCES_PATH"), "multilingual_resources.json")
if os.path.exists(multilingual_path):
    with open(multilingual_path) as f:
        data += json.load(f)

keywords = ["keyword1", "keyword2", "keyword3"]  # short stems, from Step 1

results = []
for item in data:
    if item.get("status") == "not_found":
        continue
    n = item.get("n", "").lower(); d = item.get("d", "").lower()
    s = " ".join(item.get("s") or []).lower(); c = item.get("c", "").lower()
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
    ns = item.get("ns") or 0; nd = item.get("nd") or 0
    results.append((text_score + max(ns, nd) * 2.5, item))

results.sort(key=lambda x: -x[0])
print(f"=== CANDIDATES ({len(results)} matches; top 6 shown) ===")
for combined, item in results[:6]:
    print(f"score={combined:.1f}  n={item['n']}  u={item['u']}  c={item['c']}  d={item.get('d','')[:150]}")
EOF
```

### Step 4 — Select the comparison set

From Step 3's output, pick **3–6 candidates** for the table:
- **Seed mode**: the seed itself plus its 2–5 closest peers (drop peers that don't actually do a comparable job, even if they scored).
- **Topic mode**: the top 3–6 matches, preferring ones that are genuinely distinct approaches rather than near-duplicates (e.g. don't list `mecab` and 3 thin wrappers around `mecab` as if they were independent options — pick the one or two that matter, plus other real alternatives).

**If fewer than 3 solid local candidates exist**, run 2–3 web searches (`<topic-en> japanese library`, `japanese <topic-en> alternatives`, `<topic-en> japanese huggingface`) to find 1–3 more well-known options. You don't need to filter these against the dataset the way `discover` does — the goal here is just enough real, comparable candidates for a meaningful table, not a completeness audit.

If, even after this, fewer than 2 comparable resources exist, stop and say so — a 1-row table isn't a comparison. Suggest running the `search` skill with the same query instead.

### Step 5 — Choose comparison axes

Pick **3–5 axes** that a practitioner would actually use to decide between *these specific candidates* — do not reuse a generic checklist. Good axes:
- **Actually differ** across the candidates (an axis where every row is the same is not useful — drop it).
- Are **concrete and checkable**, not vague ("license" or "supports custom dictionaries", not "good" or "quality").
- Are relevant to the domain. Examples of the *kind* of axis to look for (not a fixed list — invent axes suited to the actual topic):
  - Libraries/tools: speed, ease of installation/setup, customization (e.g. custom dictionaries, fine-tuning support), language/platform coverage, license permissiveness, active maintenance
  - Models: parameter count / resource requirements, context length, license permissiveness, Japanese-specific tuning vs. multilingual, benchmark performance if known
  - Datasets: size, license/commercial-use permissiveness, annotation quality/type, domain coverage, whether it's still actively updated

### Step 6 — Rate each candidate

For each candidate × axis, decide:
- **○** — clearly supports / strong on this axis
- **△** — partial support, average, or a notable caveat
- **✕** — does not support / weak on this axis

Ground every rating in evidence:
- Start from the dataset's `d`/`d_ja`/`s`/`st`/`lc` fields as a first signal.
- **Fetch each candidate's page** (repo README or model card) whenever a rating would otherwise be a guess — required for any claim about license, specific feature support, or benchmark numbers you are not already confident about from well-established knowledge. Cap at 6 page fetches (one per candidate), issued in parallel where possible. In Claude Code, call `WebFetch` as below; in Codex, open the page with the web search tool and extract the same fields:
  ```
  WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: license, key features relevant to <the chosen axes>, install/setup complexity, and any explicit limitations mentioned. If a field is unavailable, set it to null."
  ```
- For extremely well-known tools/axes where you have high confidence without fetching (e.g. "MeCab is written in C++ and is fast" is common knowledge), it's fine to skip the fetch — but say so is not required per-cell; just don't invent a rating you aren't reasonably confident in. When genuinely uncertain, rate **△** rather than guessing ○ or ✕.

### Step 7 — Format the output

**Language detection rule:**
- The query contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English** (default)

```
## Comparison: "<query>"

| Resource | <Axis 1> | <Axis 2> | <Axis 3> | <Axis 4> |
|---|---|---|---|---|
| [name](url) | ○ | △ | ○ | ✕ |
| [name](url) | ○ | ○ | △ | ○ |

○ = clearly supports / strong · △ = partial or unverified · ✕ = does not support / weak

**Notes:**
- [name]: one-line justification for any △ or ✕ rating that isn't self-evident.
- [name]: ...

**Recommendation:**
- If <priority A> matters most: [name](url) — why.
- If <priority B> matters most: [name](url) — why.

Sources (if you searched the web or fetched pages):
- [Title](https://...)
```

**Japanese output template:** mirror the structure with `## 比較: "<query>"`, `**注記:**`, `**おすすめ:**`, keeping the ○/△/✕ symbols and legend as-is (they're already language-neutral).

**Rules:**
- 3–6 rows, 3–5 columns — this is meant to be scannable at a glance, not exhaustive. If you have more good candidates than fit, keep the most relevant/popular ones and mention in a closing line that others exist (pointing to the `search` or `discover` skill, written in the current tool's command form).
- Every non-obvious △/✕ needs a one-line reason in **Notes** — a bare symbol with no justification is not trustworthy.
- Don't pad the table with an axis just to hit a target column count; 3 solid axes beat 5 where two are filler.
- If you searched the web or fetched pages, `Sources:` is mandatory.
