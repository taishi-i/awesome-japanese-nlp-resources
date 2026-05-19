---
description: Analyze current trends in Japanese NLP for a topic. Surveys the existing awesome-japanese-nlp-resources dataset and augments it with up-to-the-minute web research to produce a digestible trend report.
---

Research Japanese NLP trends for topic: "$ARGUMENTS" by combining the bundled dataset with the latest web information.

## Instructions

### Preamble — Establish the current date

Before doing anything else, run this once and remember the values — every subsequent step that mentions a year, month, or report date refers to them:

```bash
echo "YEAR_NOW=$(date +%Y)"
echo "YEAR_PREV=$(($(date +%Y) - 1))"
echo "REPORT_DATE_EN=$(date '+%B %Y')"
echo "REPORT_DATE_JP=$(date '+%Y年%-m月')"
```

Substitute these values everywhere this skill writes `${YEAR_NOW}`, `${YEAR_PREV}`, `${REPORT_DATE_EN}`, or `${REPORT_DATE_JP}` below. **Do not hardcode dates** — the skill must always reflect the current month.

### Step 0 — Handle empty input

If `$ARGUMENTS` is empty or blank, treat it as a request for a **general overview of current Japanese NLP trends**. Use the following defaults for the rest of the steps:

- **Topic label** for output headings: "Japanese NLP Overall Trends" (use "日本語NLP 全体トレンド" only when the user's query was written in Japanese)
- **Keywords for Step 1** (local dataset survey): `japanese nlp`, `llm`, `bert`, `embed`, `speech`, `morpholog`, `translat`
  — These broad keywords give a cross-category snapshot of the most popular resources
- **WebSearch queries for Step 5**: cover multiple active sub-fields rather than one topic:
  - `japanese NLP trends ${YEAR_NOW} overview`
  - `日本語 NLP 最新動向 ${YEAR_NOW}`
  - `japanese LLM embedding benchmark ${YEAR_NOW} github`
  - `日本語 自然言語処理 注目 モデル ${YEAR_NOW}`
  - `huggingface japanese models trending ${YEAR_NOW}`
- **Report title**: `## 📊 Japanese NLP Trend Report (as of ${REPORT_DATE_EN})` instead of `## 📊 Trend Report for "$ARGUMENTS"` (use `## 📊 日本語NLP 全体トレンドレポート (${REPORT_DATE_JP}時点)` only when output language is Japanese)
- **Section 1 (Overview)**: write a broad 3–4 sentence overview covering the major active sub-fields (LLMs, embeddings/RAG, speech, morphological analysis, benchmarks)

Then continue normally from Step 1 using the above defaults.

### Step 1 — Interpret the topic

The user's topic is: "$ARGUMENTS"

Generate **two keyword sets**:

1. **English stem keywords (4–6)** for searching the local dataset (descriptions are mostly English). Use stems like `morpholog`, `embed`, `classif`, `translat`, `generat`, `recogni`, etc. Add well-known Japanese-specific tool/model names where applicable: `mecab`, `sudachi`, `ginza`, `bert`, `gpt`, `llama`, `swallow`, `elyza`, `rinna`, `calm`, `ruri`, `whisper`, `voicevox`, `manga-ocr`, `jglue`, `llm-jp-eval`, etc.

2. **Web search phrases (3–5)** mixing English and Japanese for the latest information.

### Step 2 — Locate the data file

```bash
find "${HOME}/.claude/plugins" "${PWD}" -type f -name "resources.json" 2>/dev/null | grep "awesome-japanese-nlp" | head -1
```

If empty:
```bash
find "${HOME}/.claude/plugins" -type f -name "resources.json" 2>/dev/null | grep "awesome-japanese-nlp" | head -1
```

Save as `RESOURCES_PATH`.

### Step 3 — Survey existing resources (inline scoring)

**Do NOT use the Read tool** on `resources.json` — it exceeds the read limit. Run this Python block in Bash, substituting `RESOURCES_PATH` and your English stem keywords:

```python
python3 << 'EOF'
import json
from collections import Counter

with open("RESOURCES_PATH") as f:
    data = json.load(f)

keywords = ["keyword1", "keyword2", "keyword3"]  # English stems from Step 1

results = []
for item in data:
    n = item.get("n", "").lower()
    d = item.get("d", "").lower()
    s = item.get("s", "").lower()
    c = item.get("c", "").lower()

    text_score = 0
    for kw in keywords:
        kw = kw.lower()
        if n == kw:       text_score += 20
        elif kw in n:     text_score += 10
        if kw in d:       text_score += 5
        if kw in s:       text_score += 3
        if kw in c:       text_score += 2

    if text_score < 8:
        continue

    ns = item.get("ns") or 0
    nd = item.get("nd") or 0
    sc = item.get("sc") or 0
    pop = (ns if ns else nd) * 2.5
    qual = min(5, sc * 5 / 21)
    combined = text_score + pop + qual

    results.append((combined, text_score, item))

results.sort(key=lambda x: -x[0])

# Print top 10 for the trend snapshot
print("=== TOP MATCHES ===")
for combined, ts, item in results[:10]:
    st = item.get("st", 0) or 0
    dl = item.get("dl", 0) or 0
    print(f"score={combined:.1f} | {item.get('c','')} | ⭐{st} 📥{dl}")
    print(f"  n={item['n']}")
    print(f"  u={item['u']}")
    print(f"  d={item.get('d','')[:120]}")
    print()

# Print category distribution of full result set
print("=== CATEGORY DISTRIBUTION ===")
cats = Counter(item.get("c", "") for _, _, item in results)
for cat, count in cats.most_common(8):
    print(f"  {count:3d}  {cat}")
EOF
```

This gives you:
- **Top 10** items currently in the dataset for the topic
- **Category distribution** showing which resource types dominate
- Popularity stats (stars / downloads) to gauge maturity

### Step 4 — Identify trend angles to investigate

Before searching the web, decide what to look for. Based on the survey in Step 3, ask:

- What's the dominant **architecture** in the top matches (BERT vs. GPT vs. T5 vs. LLaMA)?
- What's the dominant **resource type** (libraries vs. models vs. corpora)?
- Are the top items **recent (within the last 2 years)** or **older (>3 years ago)**?
- Is there an apparent **gap** (e.g., no recent multimodal models, no public benchmarks)?

Use these angles to shape Step 5's queries.

### Step 5 — Web research

Use **WebSearch + WebFetch only — do not use the `gh` CLI in this project.**

Run **4–6 WebSearch queries**. Always include `${YEAR_NOW}` (and optionally `${YEAR_PREV}`) to bias toward recency. Mix English and Japanese:

- `Japanese NLP <topic-en> ${YEAR_NOW}`
- `日本語 <topic> 最新 モデル ${YEAR_NOW}`
- `arxiv japanese <topic-en> ${YEAR_PREV} ${YEAR_NOW}`
- `huggingface japanese <topic-en> new release`
- `<topic-en> github trending japanese ${YEAR_NOW}`
- Optional domain-specific: `<topic-en> jp benchmark ${YEAR_NOW}`, `日本語 <topic> 評価`

When a specific high-value URL surfaces (e.g. an arXiv abstract, a HuggingFace model card, a blog post announcing a release), use **WebFetch** to extract details:

```
WebFetch url="https://..." prompt="Extract: release date, model/library name, key contribution, GitHub/HuggingFace URL if any, parameter count or dataset size if applicable."
```

Limit WebFetch to **at most 3 calls** to keep latency in check.

### Step 6 — Cross-reference and synthesize

Combine signals:

1. **Web items already in the dataset** — confirm the survey's top items remain relevant; note if anything new dethrones them.
2. **Web items NOT in the dataset** — these are candidates the user could also surface via `/awesome-japanese-nlp-resources:find-new-resources "$ARGUMENTS"`; mention this in section 4 of the output.
3. **Directional signals** — write 2–4 specific observations about *where the field is heading*. Examples:
   - "Parameter-count growth: 1B → 7B → 70B for Japanese LLMs since 2024"
   - "Shift from encoder-only (BERT) to decoder-only (LLaMA-derived) base models"
   - "Embedding models specialized for RAG dominate 2025–2026 releases (Ruri-v3, GLuCoSE)"
   - "Multimodal Japanese models (image+text) are emerging but still rare"
4. **Gaps** — what's missing from the existing list that the web shows exists?

### Step 7 — Format the trend report

**Language detection rule (apply before writing any output):**
- `$ARGUMENTS` is empty → **English**
- `$ARGUMENTS` contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English**

Apply the detected language to all headings and prose.

**English output template (default):**

```
## 📊 Trend Report for "$ARGUMENTS" (as of ${REPORT_DATE_EN})

### 1. Overview
2–3 sentence summary. "The current focus is X, the latest trend is Y, and the highlight is Z."

### 2. Current Resources (awesome-japanese-nlp-resources)

Top 5 resources:

| # | Resource | Category | Popularity | Summary |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N or 📥N | 10–15 word summary |
| 2 | ... | ... | ... | ... |

Category distribution: <Python library: 45, HuggingFace Model: 30, ...>

Maturity comment: 1–2 sentences. Assessment of "mature / growing / sparse."

### 3. Latest Trends (from the web)

- **<date or year-month>** — <finding>. <URL>
- **YYYY-MM** — `XYZ-LLM-7B` released, achieves SOTA on Japanese JGLUE, N downloads on HuggingFace. https://huggingface.co/...
- ... (3–6 items)

### 4. Key Takeaways

- **Direction**: <directional signal 1 and 2>
- **Gaps**: important resources not yet in the list
  - <name> (https://...) — short reason
  - ... (if any)
- **Next step**: run `/awesome-japanese-nlp-resources:find-new-resources "$ARGUMENTS"` to get the full candidate list

### 5. References
(See the Sources section below)

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Japanese output template (when query is in Japanese):**

```
## 📊 "$ARGUMENTS" トレンドレポート (${REPORT_DATE_JP}時点)

### 1. 概要
2–3 文の要約。「現状の中心は X、最新の動向は Y、注目は Z」のように端的に。

### 2. 既存リソースの現状 (awesome-japanese-nlp-resources)

代表的なリソース top 5:

| # | リソース | カテゴリ | 人気度 | 一言 |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N or 📥N | 10–15 字の要約 |
| 2 | ... | ... | ... | ... |

カテゴリ分布: <Python library: 45, HuggingFace Model: 30, ...>

成熟度コメント: 1–2 文。「成熟・拡大期・空白期」の判定。

### 3. 最新トレンド (Web より)

- **<日付 or 年月>** — <発見事項>。<関連 URL>
- **YYYY-MM** — `XYZ-LLM-7B` 公開、日本語 JGLUE で SOTA、HuggingFace で N DL。 https://huggingface.co/...
- ... (3–6 項目)

### 4. 注目ポイント

- **方向性**: <directional signal 1 と 2>
- **ギャップ**: 既存リストに未収録の重要リソース
  - <name> (https://...) — 短い理由
  - ... (もしあれば)
- **次の一手**: `/awesome-japanese-nlp-resources:find-new-resources "$ARGUMENTS"` を実行すると候補一覧を取得できる

### 5. 参考リンク
(下の Sources セクションを参照)

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Rules:**
- Keep total length under ~600 words. The report should be **scannable**, not exhaustive.
- Each line in section 3 must include a **date** (or year-month) and a **URL**. No undated rumors.
- Section 4 must include at least one *directional signal* and at least one *gap* (or explicitly note "no obvious gaps").
- The `Sources:` block at the very end is **mandatory** — WebSearch results require it.

### Step 8 — Edge cases

- **No existing results** (Step 3 returns empty): Skip section 2's table; in section 2 write "既存リストにこのトピックの直接的なリソースは見つかりませんでした。" Then make section 3 + 4 the focus.
- **No recent web results**: Note in section 3 that the field is quiet — that's itself a signal.
- **Topic is too broad** (e.g. just "NLP"): Suggest in section 4 a narrower sub-topic to re-query.
