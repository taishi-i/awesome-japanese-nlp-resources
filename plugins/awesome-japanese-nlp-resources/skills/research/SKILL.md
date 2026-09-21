---
name: research
description: "Analyze current trends and challenges in Japanese NLP for a topic. Surveys the existing awesome-japanese-nlp-resources dataset and augments it with up-to-the-minute web research to produce a combined trend + issue report. Use only when the user explicitly wants a trend/landscape report, a challenges/limitations report, or a general research overview of a Japanese NLP topic (this combines the bundled dataset with live web research). Trigger phrases include '日本語LLMの最新トレンド', '〜の動向をまとめて', '最近の日本語NLPの流れ', '日本語LLMの課題', '〜の問題点・限界', '未解決の論点', 'trend report on Japanese embeddings', 'latest Japanese speech models', 'challenges in Japanese NER', 'limitations of Japanese embeddings'. For a simple lookup use the search skill; this one runs web research."
argument-hint: [topic]
allowed-tools: Bash WebSearch WebFetch
---

Research Japanese NLP trends and challenges for the user's topic by combining the bundled dataset with the latest web information.

## Claude Code and Codex

This skill is shared by the Claude Code and Codex versions of the plugin. The steps are the same in both tools; only these details differ:

- **Topic** — Claude Code: the arguments of `/awesome-japanese-nlp-resources:research`, appended at the end of this skill as `ARGUMENTS: …`. Codex: the user's message that invoked `$awesome-japanese-nlp-resources:research`, minus that `$…` mention. If the skill was picked automatically rather than invoked by name, use the user's request as the topic.
- **Plugin root** — Claude Code: `${CLAUDE_PLUGIN_ROOT}`. Codex: the directory two levels above this `SKILL.md` (use its absolute path).
- **Shell** — run the commands below with Claude Code's `Bash` tool or Codex's shell tool. Copy each Python script in full and run it as written, changing only its placeholders (`RESOURCES_PATH`, the keyword list) — don't shorten it, drop passes, or alter its scores and thresholds.
- **Web** — Claude Code: `WebSearch` to search and `WebFetch` to read a page. Codex: the built-in web search tool (search, then open the page). Do not use the `gh` CLI, `curl`, or other network commands from the shell.
- **Commands** — write any command you show the user in the current tool's form: `/awesome-japanese-nlp-resources:<skill>` in Claude Code, `$awesome-japanese-nlp-resources:<skill>` in Codex.

Section 1 of the report ("What's already in awesome-japanese-nlp-resources") must come from the bundled data. If the data file can't be read (for example, shell commands are blocked or fail to start), say so in that section instead of filling it from memory or web search.

## Instructions

### Preamble — Establish the current date

Before anything else, run this once and remember the values — every step that mentions a year or the report date refers to them:

```bash
echo "YEAR_NOW=$(date +%Y)"
echo "YEAR_PREV=$(($(date +%Y) - 1))"
echo "REPORT_DATE_EN=$(LC_ALL=C date '+%B %-d, %Y')"
echo "REPORT_DATE_JP=$(date '+%Y年%-m月%-d日')"
```

Substitute these wherever this skill writes `${YEAR_NOW}`, `${YEAR_PREV}`, `${REPORT_DATE_EN}` or `${REPORT_DATE_JP}`. **Do not hardcode years.**

### Step 0 — Validate input

If the topic is empty or blank, treat it as a request for a **general overview of the current Japanese NLP landscape** (both trends and challenges). Use the following defaults for the rest of the steps:

- **Topic label** for output headings: "Japanese NLP Overall Landscape" (use "日本語NLP 全体動向" only when the user's query was written in Japanese)
- **Keywords for Step 1** (local dataset survey): `llm`, `bert`, `embed`, `speech`, `morpholog`, `translat`, `evaluat`, `benchmark` — short stems, since Step 3 matches by literal substring and a multi-word phrase like `japanese nlp` rarely occurs verbatim in a description
  — This broad set gives a cross-category snapshot of the most popular resources and of coverage gaps
- **Web searches for Step 5**: cover both trend and challenge language across multiple sub-fields:
  - `japanese NLP trends ${YEAR_NOW} overview`
  - `日本語 NLP 最新動向 ${YEAR_NOW}`
  - `japanese LLM embedding benchmark ${YEAR_NOW} github`
  - `japanese NLP challenges ${YEAR_NOW} overview`
  - `日本語 NLP 課題 ${YEAR_NOW}`
  - `japanese LLM limitations evaluation ${YEAR_NOW}`
- **Report title**: `## 🔭 Japanese NLP Research Report (as of ${REPORT_DATE_EN})` instead of `## 🔭 Research Report for "<topic>"` (use `## 🔭 日本語NLP リサーチレポート (${REPORT_DATE_JP}時点)` only when output language is Japanese)
- **Section 1 (Overview)**: write a broad 3–4 sentence overview covering the major active sub-fields (LLMs, embeddings/RAG, speech, morphological analysis, benchmarks) and the most pressing shared challenges

### Step 1 — Interpret the topic

Translate the topic intent to English keywords for the local dataset survey. **Aim for 4–6 keywords**, using the same stem + tool-name conventions as the `search` skill (`morpholog`, `embed`, `classif`, `translat`, `recogni`, plus well-known tool names for the domain).

### Step 2 — Locate the data file

The data file ships with the plugin at `data/resources.json` under the plugin root (see "Claude Code and Codex" above). Resolve its absolute path, falling back to a scoped search only if the install is unusual:

```bash
PLUGIN_ROOT="${CLAUDE_PLUGIN_ROOT}"  # Codex: replace with the plugin root, two levels above this SKILL.md
RESOURCES_PATH="$PLUGIN_ROOT/data/resources.json"
[ -f "$RESOURCES_PATH" ] || RESOURCES_PATH="$(find "${CODEX_HOME:-$HOME/.codex}/plugins" "${HOME}/.claude/plugins" -type f -name resources.json 2>/dev/null | grep "awesome-japanese-nlp-resources/" | head -1)"
echo "RESOURCES_PATH=$RESOURCES_PATH"
```

Use the resulting absolute `RESOURCES_PATH` wherever Step 3 opens the data file — write the path itself into the script, since shell variables may not persist between commands.

The plugin also ships `data/multilingual_resources.json` (same item format) listing multilingual libraries, models, and datasets (GitHub repositories) that also support Japanese, from `docs/multilingual.md`. The scripts below load it automatically when it exists; its items have categories like `Multilingual (Speech recognition)`.

### Step 3 — Survey the existing dataset (inline Python)

**Do not read the data file directly** (no Read tool, `cat`, or `head`) — it is about 660 KB. Run the scoring in a single shell command using Python.

```python
python3 << 'EOF'
import json, os

with open("RESOURCES_PATH") as f:    # absolute path from Step 2
    data = json.load(f)
multilingual_path = os.path.join(os.path.dirname("RESOURCES_PATH"), "multilingual_resources.json")
if os.path.exists(multilingual_path):
    with open(multilingual_path) as f:
        data += json.load(f)

keywords = ["keyword1", "keyword2", "keyword3"]  # from Step 1

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
    sc = item.get("sc") or 0
    pop = (ns if ns else nd) * 2.5
    qual = min(5, sc * 5 / 21)
    combined = text_score + pop + qual

    results.append((combined, item))

results.sort(key=lambda x: -x[0])

# Category distribution across ALL matches (not just the top slice) — used to
# spot which resource types dominate and, by inference, which are thin.
from collections import Counter
cat_counts = Counter(item["c"] for _, item in results)

print(f"=== {len(results)} local matches; top 10 shown ===")
for combined, item in results[:10]:
    st = item.get("st", 0) or 0
    dl = item.get("dl", 0) or 0
    print(f"score={combined:.1f} st={st} dl={dl}")
    print(f"  n={item['n']}")
    print(f"  u={item['u']}")
    print(f"  c={item['c']}")
    print(f"  s={item.get('s','')}")
    print(f"  d={item.get('d','')[:120]}")
    print()

print("=== category distribution (all matches) ===")
for cat, count in cat_counts.most_common(10):
    print(f"  {count:4d}  {cat}")
EOF
```

Substitute `RESOURCES_PATH` with the absolute path from Step 2 and `keywords` with your keywords list from Step 1.

### Step 4 — Identify trend and challenge angles

From the Step 3 survey, note both:

**Trend angles:**
- What's the dominant **architecture** in the top matches (BERT vs. GPT vs. T5 vs. LLaMA)?
- What's the dominant **resource type** (libraries vs. models vs. corpora)?
- Are the top items **recent (within the last 2 years)** or **older (>3 years ago)**?

**Challenge angles:**
- **Coverage gaps**: which sub-problems within the topic are *not* well-represented in the existing resources?
- **Known limitations of top items**: small dataset size, narrow domain, dated baselines, evaluation issues, restrictive license — what would a practitioner complain about?
- **Famous open difficulties** in this domain (e.g. honorific generation, code-switching, ambiguity, domain transfer, low-resource dialects)

Both angles feed the same Step 5 web research — you don't need two separate research passes.

### Step 5 — Web research

Use the web search and page-fetch tools only (see "Claude Code and Codex" above) — do not use the `gh` CLI in this project.

Run **6–10 web searches**, mixing trend-language and challenge-language, English and Japanese. Always include `${YEAR_NOW}` (and optionally `${YEAR_PREV}`) to bias toward recency:

Trend-oriented:
- `Japanese NLP <topic-en> ${YEAR_NOW}`
- `日本語 <topic> 最新 モデル ${YEAR_NOW}`
- `arxiv japanese <topic-en> ${YEAR_PREV} ${YEAR_NOW}`
- `huggingface japanese <topic-en> new release`

Challenge-oriented:
- `Japanese NLP <topic-en> challenges ${YEAR_NOW}`
- `日本語 <topic> 課題 未解決 ${YEAR_NOW}`
- `arxiv japanese <topic-en> ${YEAR_PREV} ${YEAR_NOW} limitations`
- `<topic-en> japanese benchmark error analysis`

When a specific high-value URL surfaces (arXiv abstract, HuggingFace model card, blog post, benchmark leaderboard), fetch it to extract details — in Claude Code with `WebFetch` as below; in Codex, open it with the web search tool and extract the same fields:

```
WebFetch url="https://..." prompt="Extract: publication/release date, name, key contribution or problem statement, proposed solution if any, GitHub/HuggingFace URL if any, and a 1-sentence summary. Note if it cites Japanese-specific issues."
```

### Step 6 — Synthesize findings

Sort the Step 5 findings into:

1. **Web items already in the dataset** — confirm the survey's top items remain relevant; note if anything new dethrones them.
2. **Web items NOT in the dataset** — candidates the user could also surface by running the `discover` skill on the same topic; mention this in the output.
3. **Directional signals (trends)** — 2–4 specific observations about *where the field is heading*, e.g. "Parameter-count growth: 1B → 7B → 70B for Japanese LLMs since 2024", "Shift from encoder-only to decoder-only base models".
4. **Known challenges** — 3–6 concrete, dated items with URLs. Each should be a *specific* problem ("evaluation suites still over-rely on machine-translated GLUE-style tasks", not "evaluation is hard").
5. **Current efforts / proposed solutions** — 2–4 ongoing projects, papers, or releases attempting to address the challenges in bucket 4. Each needs a URL. If none surfaced, say so explicitly.
6. **Open gaps** — items in bucket 4 that bucket 5 does NOT cover, and dataset coverage gaps from Step 4.

### Step 7 — Format the report

**Language detection rule (apply before writing any output):**
- The topic contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English** (default)

Apply the detected language to all headings and prose.

```
## 🔭 Research Report for "<topic>" (as of ${REPORT_DATE_EN})

2–3 sentence summary covering both the current focus/trend and the main open challenge.

### 1. What's already in awesome-japanese-nlp-resources

Top 5 resources:

| # | Resource | Category | Popularity | Summary |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N or 📥N | 10–15 word summary |

Category distribution: <Python library: 45, HuggingFace Model: 30, ...>

### 2. Latest Trends

- 2–4 bullet points of directional signals (bucket 3), each with a source link.

### 3. Known Challenges

| # | Challenge | Notes | Source |
|---|---|---|---|
| 1 | short challenge statement | 1 sentence detail | [source](url) |

### 4. Current Efforts

- 2–4 bullets naming ongoing work that addresses a Step 3 challenge, each with a URL. If none found, state that explicitly.

### 5. Still Unsolved

- Bullet list of open gaps (bucket 6) — combine dataset coverage gaps and challenge gaps not covered by current efforts.

### 6. Not yet in the list

If any notable web finds from bucket 2 exist, list them briefly and point to the `discover` skill (same topic, written in the current tool's command form) for the full discovery workflow. Omit this section if bucket 2 was empty.

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

If the topic was empty, use the Step 0 defaults for the title/overview instead of topic-specific text.

**Rules:**
- Every claim in sections 2–4 needs a source link — this skill's value is grounding trend/challenge claims in fresh web evidence, not restating the dataset.
- Keep section 1's table to the top 5 — this is context, not the point of the report.
- If Step 5 surfaced little (e.g. a very niche topic), say so explicitly rather than padding with generic statements.
