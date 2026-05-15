---
description: Investigate current challenges, limitations, and proposed solutions in Japanese NLP for a topic. Surveys the existing awesome-japanese-nlp-resources dataset to see what already exists, then web-researches known problems and ongoing efforts to produce a digestible issue report.
---

Research current challenges in Japanese NLP for topic: "$ARGUMENTS" by combining the bundled dataset with the latest web information.

## Instructions

### Step 0 — Handle empty input

If `$ARGUMENTS` is empty or blank, treat it as a request for a **general overview of current Japanese NLP challenges**. Use the following defaults for the rest of the steps:

- **Topic label** for output headings: "Japanese NLP Current Challenges" (use "日本語NLP 現状の課題" only when the user's query was written in Japanese)
- **Keywords for Step 1** (local dataset survey): `japanese nlp`, `llm`, `evaluat`, `benchmark`, `embed`, `speech`, `morpholog`
  — These broad keywords give a cross-category snapshot for inferring coverage gaps
- **WebSearch queries for Step 5**: cover challenge-language across multiple sub-fields:
  - `japanese NLP challenges 2026 overview`
  - `日本語 NLP 課題 2026`
  - `japanese LLM limitations evaluation 2026`
  - `日本語 自然言語処理 問題点 未解決 2026`
  - `japanese NLP benchmark error analysis 2026`
- **Report title**: `## 🔍 Japanese NLP Issue Report (as of May 2026)` instead of `## 🔍 Issue Report for "$ARGUMENTS"` (use `## 🔍 日本語NLP 現状の課題レポート (2026年5月時点)` only when output language is Japanese)
- **Section 1 (Overview)**: write a broad 3–4 sentence overview covering the most pressing challenges across active sub-fields (LLM evaluation, low-resource domains, embedding quality, speech, benchmarks)

Then continue normally from Step 1 using the above defaults.

### Step 1 — Interpret the topic

The user's topic is: "$ARGUMENTS"

Generate **two keyword sets**:

1. **English stem keywords (4–6)** for searching the local dataset (descriptions are mostly English). Use stems like `morpholog`, `embed`, `classif`, `translat`, `generat`, `recogni`, etc. Add well-known Japanese-specific tool/model names where applicable: `mecab`, `sudachi`, `ginza`, `bert`, `gpt`, `llama`, `swallow`, `elyza`, `rinna`, `calm`, `ruri`, `whisper`, `voicevox`, `manga-ocr`, `jglue`, `llm-jp-eval`, etc.

2. **Web search phrases (3–5)** mixing English and Japanese, **explicitly biased to challenge language**:
   - English-side: `challenges`, `limitations`, `problems`, `bottleneck`, `unsolved`, `failure modes`, `error analysis`
   - Japanese-side: `課題`, `問題点`, `限界`, `未解決`, `誤り分析`

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

# Print top 10 for the issue-report snapshot
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
- **Top 10** items currently in the dataset for the topic — these define *what coverage already exists*
- **Category distribution** showing which resource types dominate (and by inference, which are missing)
- Popularity stats — low popularity on a top match can itself indicate an underinvested area

### Step 4 — Identify challenge angles to investigate

Before searching the web, decide what to look for. Based on the survey in Step 3, ask:

- **Coverage gaps**: which sub-problems within "$ARGUMENTS" are *not* well-represented in the existing resources?
- **Known limitations of top items**: small dataset size, narrow domain, dated baselines, evaluation issues, restrictive license — what would a practitioner complain about?
- **Famous open difficulties** in this domain (e.g., honorific generation, code-switching, ambiguity, domain transfer, low-resource dialects)
- **Inferred gaps**: if recent items are absent, the field may have stagnated or shifted elsewhere — worth checking on the web

Use these angles to shape Step 5's queries.

### Step 5 — Web research

Use **WebSearch + WebFetch only — do not use the `gh` CLI in this project.**

Run **4–6 WebSearch queries**, biased toward challenge-language. Always include the year **2026** or **2025** to bias toward recency. Mix English and Japanese:

- `Japanese NLP <topic-en> challenges 2026`
- `Japanese NLP <topic-en> limitations`
- `日本語 <topic> 課題 2026`
- `日本語 <topic> 問題点 未解決`
- `arxiv japanese <topic-en> 2025 2026 challenges`
- Optional: `<topic-en> japanese benchmark error analysis`, `<topic-en> japanese low-resource`

When a specific high-value URL surfaces (e.g. arXiv abstract describing a failure mode, an evaluation paper, a position paper, a benchmark leaderboard with error analysis), use **WebFetch** to extract details:

```
WebFetch url="https://..." prompt="Extract: publication date, problem statement (what challenge or limitation does this describe), proposed solution if any, dataset/model used, and a 1-sentence summary of the result. Note if it cites Japanese-specific issues."
```

Limit WebFetch to **at most 3 calls** to keep latency in check.

### Step 6 — Cross-reference and synthesize

Sort the findings from Step 5 into three buckets:

1. **Known challenges** — 3–6 concrete, dated items with URLs. Each should be a *specific* problem ("evaluation suites still over-rely on machine-translated GLUE-style tasks", not "evaluation is hard").
2. **Current efforts / proposed solutions** — 2–4 ongoing projects, papers, or releases attempting to address the challenges in bucket 1. Each needs a URL. If no public efforts surfaced, say so explicitly.
3. **Open gaps** — items in bucket 1 that bucket 2 does NOT cover. These become Section 5's "Still unsolved" line.

Also note any **mismatch with the dataset survey**: web items not in the existing list are candidates for `/awesome-japanese-nlp-resources:find-new-resources`.

### Step 7 — Format the issue report

**Language detection rule (apply before writing any output):**
- `$ARGUMENTS` is empty → **English**
- `$ARGUMENTS` contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English**

Apply the detected language to all headings and prose.

**English output template (default):**

```
## 🔍 Issue Report for "$ARGUMENTS" (as of May 2026)

### 1. Overview
2–3 sentences. "The main challenges in X are A, B, and C. Recent work tackled D; E remains open."

### 2. Current Resources (awesome-japanese-nlp-resources)

Top 5 resources covering this topic:

| # | Resource | Category | Popularity | Coverage note |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N or 📥N | what aspect it handles / its known limitation |
| 2 | ... | ... | ... | ... |

What's covered well: <comma-separated list of well-served aspects>
What's weak / missing: <comma-separated list of gap aspects>

### 3. Known Challenges (from the web)

- **<date or year-month>** — <specific challenge>. <URL>
- **2026-03** — Evaluation benchmarks still over-rely on translated GLUE tasks, missing Japanese-specific phenomena (honorifics, particles). https://arxiv.org/...
- ... (3–6 items)

### 4. Current Efforts & Proposed Solutions

- **<approach / paper / project>** — <what it solves, status>. <URL>
- ... (2–4 items)

If no public efforts surfaced, write: "No widely-cited public efforts directly addressing the above challenges surfaced in this scan."

### 5. Key Takeaways

- **Most pressing issue**: <one-line summary of the top challenge from Section 3>
- **Promising direction**: <one-line, cite a Section-4 item by name>
- **Still unsolved**: <one-line, item from Section 3 not covered by Section 4>
- **Next step**: run `/awesome-japanese-nlp-resources:find-new-resources "$ARGUMENTS"` to discover repos that may address these issues

### 6. References
(See the Sources section below)

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Japanese output template (when query is in Japanese):**

```
## 🔍 "$ARGUMENTS" の課題レポート (2026年5月時点)

### 1. 概要
2–3 文の要約。「主要な課題は X, Y, Z。最近 D は進展、E は未解決」のように端的に。

### 2. 既存リソースの現状 (awesome-japanese-nlp-resources)

このトピックを扱う代表的なリソース top 5:

| # | リソース | カテゴリ | 人気度 | カバー範囲メモ |
|---|---|---|---|---|
| 1 | [name](url) | category | ⭐N or 📥N | 何を扱っているか / 既知の限界 |
| 2 | ... | ... | ... | ... |

カバーできている領域: <カバー良好な側面のコンマ区切り>
未対応 / 弱い領域: <ギャップとなっている側面のコンマ区切り>

### 3. 既知の課題 (Web より)

- **<日付 or 年月>** — <具体的な課題>。<URL>
- **2026-03** — 評価ベンチマークが翻訳版 GLUE 系に偏り、敬語・助詞など日本語固有現象を捉えきれていない。 https://arxiv.org/...
- ... (3–6 項目)

### 4. 現状の取り組み / 提案されている解決策

- **<アプローチ / 論文 / プロジェクト>** — <何を解決しようとしているか、進捗>。<URL>
- ... (2–4 項目)

公開された取り組みが見つからない場合は「上記課題に直接取り組んでいる広く引用された公開プロジェクトは今回の調査では発見できませんでした。」と明記。

### 5. 注目ポイント

- **最重要課題**: <Section 3 で最重要な課題を1行で>
- **有望な方向性**: <Section 4 から1件、名前付きで1行>
- **未解決の点**: <Section 3 にあって Section 4 で扱われていない課題を1行で>
- **次の一手**: `/awesome-japanese-nlp-resources:find-new-resources "$ARGUMENTS"` で課題に対応するリポジトリ候補を探索

### 6. 参考リンク
(下の Sources セクションを参照)

Sources:
- [Title 1](https://...)
- [Title 2](https://...)
```

**Rules:**
- Keep total length under ~700 words. The report should be **scannable**, not exhaustive.
- Each line in Section 3 must include a **date** (or year-month) and a **URL**. No undated speculation.
- Section 4 must cite at least 2 efforts with URLs, OR explicitly state none were found.
- Section 5 must include all four sub-bullets in order.
- The `Sources:` block at the very end is **mandatory** — WebSearch results require it.

### Step 8 — Edge cases

- **No existing results** (Step 3 returns empty): In Section 2, write "既存リストにこのトピックの直接的なリソースは見つかりませんでした。" (Japanese) or "No direct resources found in the existing list for this topic." (English). Then make Sections 3–5 the focus.
- **No challenges surface from the web**: Note in Section 3 that little challenge discussion was found — the field may be mature or under-discussed. Suggest a broader / adjacent query.
- **Topic is too broad** (e.g. just "NLP"): Add a line in Section 5 suggesting a narrower sub-topic to re-query.
