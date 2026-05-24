---
description: Search all Japanese NLP resources (libraries, models, datasets, tutorials, dictionaries, Hugging Face). Accepts keywords or natural language questions in any language.
when_to_use: "Use whenever the user asks which Japanese NLP resource to use, or wants to find one: tokenizers / morphological analyzers, BERT or LLM models, embeddings, NER, text classification, datasets / corpora, dictionaries, tutorials, or Hugging Face models. Trigger phrases include '日本語の形態素解析ライブラリ', 'おすすめの日本語tokenizer', '日本語BERTモデル', '日本語の感情分析データセット', '日本語LLM 一覧', 'which Japanese embedding model', 'Japanese NER library'."
argument-hint: [query]
allowed-tools: Bash
---

Search the awesome-japanese-nlp-resources database for: "$ARGUMENTS"

## Instructions

### Step 0 — Validate input

If `$ARGUMENTS` is empty or blank, **stop immediately** and output:

```
Usage: /awesome-japanese-nlp-resources:search <query>

Examples:
  /awesome-japanese-nlp-resources:search morphological analysis
  /awesome-japanese-nlp-resources:search BERT
  /awesome-japanese-nlp-resources:search named entity recognition
  /awesome-japanese-nlp-resources:search text classification dataset
  /awesome-japanese-nlp-resources:search sentence embedding

Please pass the keyword(s) you want to search for as the argument.

---

使い方: /awesome-japanese-nlp-resources:search <query>

クエリ例:
  /awesome-japanese-nlp-resources:search 形態素解析
  /awesome-japanese-nlp-resources:search BERT
  /awesome-japanese-nlp-resources:search 固有表現認識
  /awesome-japanese-nlp-resources:search テキスト分類 データセット
  /awesome-japanese-nlp-resources:search 文埋め込み

検索したいキーワードを引数に指定してください。
```

Do **not** proceed to Step 1 if `$ARGUMENTS` is empty.

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
| OCR / 光学文字認識 | `ocr`, `optical character`, `recogni` | `manga-ocr`, `donut`, `tesseract` |
| RAG / 検索拡張生成 | `retriev`, `rag`, `embed` | `ruri`, `glucose`, `faiss` |
| ファインチューニング / fine-tuning | `fine-tun`, `finetun`, `lora`, `peft` | `lora`, `peft`, `qlora` |
| ベンチマーク・評価 / benchmark | `benchmark`, `evaluat`, `jglue` | `llm-jp-eval`, `jglue`, `nejumi` |

3. **Aim for 4–6 keywords.** Fewer miss items; more than 6 inflates low-quality partial matches.
4. **If none of the above domains fit**, translate the query intent literally to English stems.

### Step 2 — Locate the data file

The data file ships with the plugin. Resolve its path via `${CLAUDE_PLUGIN_ROOT}` (Claude Code substitutes this inline in skill content), falling back to a scoped search only if the install is unusual:

```bash
RESOURCES_PATH="${CLAUDE_PLUGIN_ROOT}/data/resources.json"
[ -f "$RESOURCES_PATH" ] || RESOURCES_PATH="$(find "${HOME}/.claude/plugins" -type f -name resources.json 2>/dev/null | grep "awesome-japanese-nlp-resources/" | head -1)"
echo "RESOURCES_PATH=$RESOURCES_PATH"
```

Use the resulting absolute `RESOURCES_PATH` wherever Step 3 opens the data file.

### Step 3 — Search and score via Bash

**Do NOT use the Read tool** — the file exceeds the Read tool's size limit and would consume ~64K tokens unnecessarily. Instead, run the scoring in a single Bash call using Python.

Each item in the JSON array has:
- `u`: GitHub or Hugging Face URL
- `n`: repository/model name
- `d`: description (English for most items; some Japanese-only items have Japanese descriptions)
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

with open("RESOURCES_PATH") as f:    # absolute path from Step 2
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
seen = {item['n'] for _, _, item in results}

# Supplemental pass: surface high-popularity items from matching categories
# that may have been missed because their descriptions are in Japanese.
# Keys are stems to match against user keywords; values are category prefixes
# (prefix match covers "HuggingFace Model (Text Generation)" etc.).
CATEGORY_KEYWORDS = {
    "tutorial": "Tutorial", "introduc": "Tutorial", "learn": "Tutorial",
    "morpholog": "Python library", "segment": "Python library",
    "mecab": "Python library", "janome": "Python library", "sudachi": "Python library",
    "spacy": "Python library", "ginza": "Python library",
    "corpus": "Corpus", "dataset": "Corpus",
    "bert": "HuggingFace Model", "gpt": "HuggingFace Model",
    "llm": "HuggingFace Model", "llama": "HuggingFace Model",
    "pretrain": "HuggingFace Model", "embed": "HuggingFace Model",
    "model": "Pretrained model",
}
supplement_cats = set()
for kw in keywords:
    for ck, cat in CATEGORY_KEYWORDS.items():
        if ck in kw.lower():
            supplement_cats.add(cat)

if supplement_cats:
    def cat_match(c):
        return any(c == cat or c.startswith(cat + " ") for cat in supplement_cats)
    extras = [
        item for item in data
        if cat_match(item.get("c", ""))
        and (item.get("st", 0) or item.get("dl", 0))
        and item["n"] not in seen
    ]
    extras.sort(key=lambda x: -max(x.get("ns") or 0, x.get("nd") or 0))
    for item in extras[:5]:
        ns = item.get("ns") or 0
        nd = item.get("nd") or 0
        sc = item.get("sc") or 0
        # base 8 = category-match credit (same as the text_score threshold)
        combined = 8 + max(ns, nd) * 2.5 + min(5, sc * 5 / 21)
        results.append((combined, 0, item))
        seen.add(item["n"])

results.sort(key=lambda x: -x[0])
for combined, text_score, item in results[:20]:
    st = item.get("st", 0) or 0
    dl = item.get("dl", 0) or 0
    flag = " [supplemental]" if text_score == 0 else ""
    print(f"score={combined:.1f} text={text_score} st={st} dl={dl}{flag}")
    print(f"  n={item['n']}")
    print(f"  u={item['u']}")
    print(f"  c={item['c']}")
    print(f"  s={item.get('s','')}")
    print(f"  d={item.get('d','')[:120]}")
    print()
EOF
```

This returns up to 20 candidates. Items marked `[supplemental]` were added by the category-based pass to recover high-star resources whose descriptions are in Japanese. In Step 4, evaluate supplemental items on semantic fit before including them in the final list.

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

**Language detection rule (apply before writing any output):**
- `$ARGUMENTS` contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English** (default)

Apply the detected language to all headings and prose.

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

### Step 6 — Output use-case selection guide table

After the search results list, append a guide table that helps the user pick the right resource for their specific situation.

**Match the section heading and table language to the query language** — translate the heading and column headers into the query language (e.g. Japanese query → Japanese heading and headers).

```
## Use-case Selection Guide

| Use case | Recommended | Popularity | Why |
|---|---|---|---|
| ... | [name](url) | ⭐N or 📥N | short reason |
```

**Rules:**
- List **3–6 distinct use cases** derived from the top 10 results. Each row should represent a meaningfully different scenario (e.g., "fine-tune an LLM" vs "evaluate an LLM"), not just a restatement of the search query.
- For each row, select the **single best resource** from the top 10 results.
- **Popularity column**: use `⭐{st}` for GitHub stars, `📥{dl}` for HuggingFace downloads. If both are 0, omit.
- **Why**: write a 10–15 word reason in the query language explaining why this resource is the best fit for that use case. Do not copy the description verbatim. Focus on the practical benefit.
- If two use cases would map to the same resource, merge them into one row or drop the weaker one.
- If there are fewer than 3 meaningfully distinct use cases in the results, output as many rows as make sense (minimum 1).
