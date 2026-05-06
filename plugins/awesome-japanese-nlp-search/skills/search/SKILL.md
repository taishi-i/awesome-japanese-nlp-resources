---
description: Search all Japanese NLP resources (libraries, models, datasets, tutorials, dictionaries, Hugging Face). Accepts keywords or natural language questions in any language.
---

Search the awesome-japanese-nlp-resources database for: "$ARGUMENTS"

## Instructions

### Step 1 — Interpret the query

The user's query is: "$ARGUMENTS"

The data descriptions are in **English**, so always convert the query intent to English keywords before searching.

Examples:
| User query (any language) | English keywords to search |
|---------------------------|---------------------------|
| 日本語のNLPを勉強するためのリソース | tutorial, introduction, learning, NLP |
| トークナイザーを探しています | tokenizer, morphology, segmentation |
| 형태소 분석 (Korean) | morphology, tokenizer, segmentation |
| BERTの日本語モデルが欲しい | BERT, japanese, pretrained, transformer |
| what are good NER datasets? | named entity, NER, dataset, corpus |
| mots japonais en vecteurs (French) | word2vec, embedding, word vectors |

### Step 2 — Locate the data file

Run:
```
find "${HOME}/.claude/plugins" "${PWD}" -type f -name "resources.json" -path "*awesome-japanese-nlp-search*" 2>/dev/null | head -1
```

If empty, try:
```
find "${PWD}" -type f -name "resources.json" -path "*/data/*" 2>/dev/null | head -1
```

### Step 3 — Read the file

Use the Read tool on the returned path.

The file is a JSON array of ~1,212 items. Each item has:
- `u`: GitHub or Hugging Face URL
- `n`: repository/model name
- `d`: English description
- `c`: category (e.g. `Python library`, `HuggingFace Model (Text Generation)`, `Corpus`, `Tutorial`, ...)
- `s`: subcategory / semantic labels (comma-separated)
- `st`: GitHub star count (GitHub items only; absent or 0 otherwise)
- `ns`: normalized star score 0–10 (log-scaled, GitHub items only)
- `dl`: Hugging Face download count (HF items only; absent or 0 otherwise)
- `nd`: normalized download score 0–10 (log-scaled, HF items only)
- `sc`: pre-computed quality score (higher = more popular/active)

### Step 4 — Score candidates

Using the English keywords from Step 1, compute a **combined score** for each item:

**Text match score** (case-insensitive, per keyword):
- Name (`n`) exact keyword match: +20 pts
- Name (`n`) contains keyword: +10 pts
- Description (`d`) contains keyword: +5 pts
- Subcategory (`s`) contains keyword: +3 pts
- Category (`c`) contains keyword: +2 pts

**Popularity bonus** (added once per item, not per keyword):
- GitHub items: `ns * 1.5` (e.g. ns=8 → +12 pts)
- HF items: `nd * 1.5` (e.g. nd=9 → +13.5 pts)

**Quality bonus**: `min(5, sc * 5 / 21)`

**Combined score = text_match + popularity_bonus + quality_bonus**

Exclude items with text_match = 0 (zero keyword hits).

Collect the top **20** candidates sorted by combined score descending.

### Step 5 — Re-rank with your judgment

You now have up to 20 candidates. Apply your semantic judgment to produce the final ordered list of up to **10** results.

Re-rank by evaluating each candidate on:
1. **Semantic centrality** — how directly does this resource address the query's core intent? A BERT model is more central to "BERT fine-tuning" than a generic transformer library.
2. **Popularity as a proxy for quality** — high stars/downloads generally signal battle-tested, well-documented tools. Prefer them when candidates are otherwise equivalent.
3. **Category fit** — match the resource type to the implied need:
   - "how to learn / 勉強" → prefer `Tutorial`, `Research summary`
   - "I need a model" → prefer `Pretrained model`, `HuggingFace Model`
   - "find a dataset / コーパス" → prefer `Corpus`, `HuggingFace Dataset`
   - "build an app / ライブラリ" → prefer `Python library`, language-specific libs
4. **Specificity** — a resource specialized for the exact task beats a general one.
5. **Recency signal** — when `sc` is significantly higher among otherwise-similar items, it usually reflects more recent activity; prefer those.

Do not mechanically follow the combined score from Step 4 — use it as a starting point, then move items up or down based on the criteria above.

### Step 6 — Format the output

Present the final re-ranked results:

```
## Search results for "$ARGUMENTS"

*(Searched for: keyword1, keyword2, ...)*

Found N result(s).

### 1. [repository-name](url)
**Category:** category > subcategory
**Popularity:** ⭐ {st} stars  (or  📥 {dl} downloads for HF)
Description text here.

### 2. ...
```

If no results, suggest alternate keywords and link to:
https://github.com/taishi-i/awesome-japanese-nlp-resources
