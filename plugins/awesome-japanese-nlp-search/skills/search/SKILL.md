---
description: Search all Japanese NLP resources (libraries, models, datasets, tutorials, dictionaries, Hugging Face). Accepts keywords or natural language questions in any language.
---

Search the awesome-japanese-nlp-resources database for: "$ARGUMENTS"

## Instructions

### Step 1 — Interpret the query

The user's query is: "$ARGUMENTS"

The data descriptions are in **English**, so always convert the query intent to English keywords before searching.

**Keyword rules — read before choosing keywords:**
1. **Use stems, not full words.** Substring match is used, so `morpholog` catches "morphology", "morphological", "morphological analyzer". Other examples: `embed` → embedding/embeddings, `classif` → classification/classifier, `translat` → translation/translate, `generat` → generation/generative, `segment` → segmentation/segmenter, `recogni` → recognition/recognizer, `extract` → extraction/extractor, `retriev` → retrieval/retrieve.
2. **Add domain-specific tool names.** When the query maps to a known NLP domain, include the well-known tool names present in the database:

| Domain (Japanese query hint) | Stem keywords | Tool names to add |
|---|---|---|
| 形態素解析 / morphological analysis | `morpholog`, `segment` | `mecab`, `janome`, `sudachi`, `kytea`, `kuromoji`, `jumanpp`, `nagisa` |
| 固有表現認識 / NER | `named entit`, `NER`, `recogni` | `ginza`, `spacy`, `knp` |
| 係り受け解析 / dependency parsing | `depend`, `parse`, `syntax` | `cabocha`, `knp`, `ginza`, `spacy` |
| 文章分類 / text classification | `classif`, `sentiment`, `categor` | `bert`, `fasttext` |
| 感情分析 / sentiment analysis | `sentiment`, `emotion`, `opinion` | `oseti`, `wrime` |
| 埋め込み / word vectors / embeddings | `embed`, `vector`, `represent` | `word2vec`, `fasttext`, `bert`, `sbert` |
| 事前学習モデル / pretrained model | `pretrain`, `language model`, `bert`, `gpt` | `bert`, `gpt`, `llama`, `rinna`, `elyza`, `calm`, `swallow` |
| テキスト生成 / text generation | `generat`, `language model` | `gpt`, `llm`, `llama`, `rinna`, `elyza` |
| 機械翻訳 / machine translation | `translat`, `machine translation` | `opus`, `marian`, `fairseq` |
| 音声認識 / speech recognition | `speech`, `recogni`, `audio`, `asr` | `whisper`, `julius`, `espnet` |
| 音声合成 / text-to-speech | `speech`, `synthesis`, `tts` | `voicevox`, `espnet` |
| 質問応答 / QA | `question`, `answer`, `qa` | `bert`, `t5` |
| 要約 / summarization | `summari`, `abstract` | `bart`, `t5`, `pegasus` |
| 辞書・IME / dictionary | `dict`, `lexicon`, `ime` | `mecab`, `sudachi`, `mozc` |
| コーパス・データセット / corpus | `corpus`, `dataset`, `annot` | *(rely on stems)* |
| チュートリアル / learning | `tutorial`, `introduc`, `learn` | *(rely on stems)* |

3. **Aim for 4–6 keywords.** Fewer miss items; more than 6 inflates low-quality partial matches.
4. **If none of the above domains fit**, translate the query intent literally to English stems.

### Step 2 — Locate the data file

Run:
```
find "${HOME}/.claude/plugins" "${PWD}" -type f -name "resources.json" -path "*awesome-japanese-nlp-search*" 2>/dev/null | head -1
```

If empty, try:
```
find "${PWD}" -type f -name "resources.json" -path "*/data/*" 2>/dev/null | head -1
```

### Step 3 — Search and score via Bash

**Do NOT use the Read tool** — the file exceeds the Read tool's size limit and would consume ~64K tokens unnecessarily. Instead, run the scoring in a single Bash call using Python.

Each item in the JSON array has:
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

Run the following, substituting `KEYWORDS` with your English keywords list from Step 1:

```python
python3 << 'EOF'
import json

with open("PATH_FROM_STEP2") as f:
    data = json.load(f)

keywords = ["keyword1", "keyword2", "keyword3"]  # from Step 1

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

    if text_score == 0:
        continue

    ns = item.get("ns") or 0
    nd = item.get("nd") or 0
    sc = item.get("sc") or 0
    pop = (ns if ns else nd) * 0.8
    qual = min(5, sc * 5 / 21)
    combined = text_score + pop + qual

    results.append((combined, text_score, item))

results.sort(key=lambda x: -x[0])
for combined, text_score, item in results[:20]:
    st = item.get("st", 0) or 0
    dl = item.get("dl", 0) or 0
    print(f"score={combined:.1f} text={text_score} st={st} dl={dl}")
    print(f"  n={item['n']}")
    print(f"  u={item['u']}")
    print(f"  c={item['c']}")
    print(f"  s={item.get('s','')}")
    print(f"  d={item.get('d','')[:120]}")
    print()
EOF
```

This returns up to 20 candidates with their scores. Only matched items are output, keeping token usage minimal (~1K tokens vs ~64K for reading the full file).

### Step 4 — Re-rank with your judgment

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

Do not mechanically follow the combined score from Step 3 — use it as a starting point, then move items up or down based on the criteria above.

### Step 5 — Format the output

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
