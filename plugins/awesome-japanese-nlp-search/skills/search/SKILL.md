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

The file is a JSON array of 1,212 items. Each item has:
- `u`: GitHub or Hugging Face URL
- `n`: repository/model name
- `d`: English description
- `c`: category (e.g. Python library, HuggingFace Model, Corpus, Tutorial, ...)
- `s`: subcategory

### Step 4 — Search and rank

Using the extracted English keywords from Step 1, score each item (case-insensitive):
- Name (`n`) exact keyword match: +20 points per keyword
- Name contains keyword: +10 points per keyword
- Description (`d`) contains keyword: +5 points per keyword
- Subcategory (`s`) contains keyword: +3 points per keyword
- Category (`c`) contains keyword: +2 points per keyword

Exclude items with zero score.

### Step 5 — Format the output

Present up to 15 results, sorted by score descending:

```
## Search results for "$ARGUMENTS"

*(Searched for: keyword1, keyword2, ...)*

Found N result(s).

### 1. [repository-name](url)
**Category:** category > subcategory
Description text here.

### 2. ...
```

If no results, suggest alternate keywords and link to:
https://github.com/taishi-i/awesome-japanese-nlp-resources
