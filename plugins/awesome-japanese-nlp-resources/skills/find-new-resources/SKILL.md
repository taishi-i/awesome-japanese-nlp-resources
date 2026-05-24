---
description: Find Japanese NLP GitHub repositories that are NOT yet in awesome-japanese-nlp-resources. Suggests candidates to add for a given topic using WebSearch + WebFetch, then outputs contribution-ready markdown.
when_to_use: "Use only when the user explicitly wants to discover Japanese NLP GitHub repositories NOT yet in awesome-japanese-nlp-resources, or to prepare a contribution. Trigger phrases include 'リストに無い新しい日本語NLP', 'awesome-japanese-nlpに追加できそうな', '最近公開された日本語NLPツール', 'find unlisted Japanese NLP repos', 'contribute a new resource'. For searching what already exists, use the search skill instead."
argument-hint: [topic]
allowed-tools: Bash WebSearch WebFetch
---

Find new Japanese NLP GitHub repositories for topic: "$ARGUMENTS" that are not already in the awesome-japanese-nlp-resources list.

## Instructions

### Preamble — Establish the current date

Before doing anything else, run this once and remember the values — every step that mentions a year refers to them:

```bash
echo "YEAR_NOW=$(date +%Y)"
echo "YEAR_PREV=$(($(date +%Y) - 1))"
```

Substitute these everywhere this skill writes `${YEAR_NOW}` or `${YEAR_PREV}` below. **Do not hardcode years** — the skill must always reflect the current year.

### Step 0 — Handle empty input

If `$ARGUMENTS` is empty or blank, treat it as a **general search for the latest Japanese NLP resources**. Use the following default settings for the rest of the steps:

- **Topic label** for output headings: "Latest Japanese NLP Resources" (use "最新の日本語NLPリソース" only when the user's query was written in Japanese)
- **Keywords for Step 1**: `japanese nlp`, `日本語 nlp`, `japanese language processing`, `japanese machine learning`
- **WebSearch queries for Step 4**: focus on recency — add `${YEAR_PREV} ${YEAR_NOW}` to every query, and include:
  - `japanese NLP new library github ${YEAR_NOW}`
  - `日本語 NLP 新しい ライブラリ github ${YEAR_NOW}`
  - `awesome japanese nlp ${YEAR_PREV} ${YEAR_NOW} new`
  - `japanese natural language processing tool released ${YEAR_PREV} ${YEAR_NOW}`
- **Output heading**: "New Japanese NLP Resource Candidates" instead of `New candidates for "$ARGUMENTS"` (use "最近追加された日本語NLPリソース候補" only when the output language is Japanese)

Then continue normally from Step 1 using the above defaults.

### Step 1 — Interpret the topic

The user's topic is: "$ARGUMENTS"

Translate the topic intent to English keywords for search. **Aim for 3–5 keywords/phrases.** Use the same stem + tool-name conventions as the `search` skill:

| Domain (Japanese hint) | English keywords / search phrases |
|---|---|
| 形態素解析 / morphological analysis | `japanese morphological analyzer`, `japanese tokenizer`, `mecab`, `sudachi`, `janome` |
| 固有表現認識 / NER | `japanese named entity recognition`, `japanese NER`, `ginza` |
| 係り受け解析 / dependency parsing | `japanese dependency parser`, `cabocha`, `knp` |
| 文章分類 / text classification | `japanese text classification`, `japanese sentiment` |
| 埋め込み / embeddings | `japanese sentence embedding`, `japanese embedding model`, `ruri`, `sbert` |
| 事前学習モデル / pretrained model | `japanese pretrained model`, `japanese LLM`, `japanese BERT`, `japanese GPT` |
| LLM / 大規模言語モデル | `japanese llm`, `japanese language model`, `llama japanese`, `swallow`, `elyza` |
| テキスト生成 / generation | `japanese text generation`, `japanese chatbot` |
| 機械翻訳 / translation | `japanese machine translation`, `english japanese translation` |
| 音声認識 / speech | `japanese speech recognition`, `japanese asr`, `whisper japanese` |
| 音声合成 / TTS | `japanese text to speech`, `japanese tts`, `voicevox` |
| 質問応答 / QA | `japanese question answering`, `japanese qa dataset` |
| 要約 / summarization | `japanese summarization`, `japanese abstractive summarization` |
| 辞書 / dictionary・IME | `japanese dictionary`, `japanese ime`, `mozc` |
| コーパス / corpus | `japanese corpus`, `japanese dataset`, `japanese annotated` |
| OCR | `japanese ocr`, `manga ocr` |
| RAG | `japanese rag`, `japanese retrieval`, `japanese reranker` |
| ファインチューニング | `japanese fine-tuning`, `japanese lora`, `japanese instruction tuning` |
| ベンチマーク / 評価 | `japanese benchmark`, `japanese evaluation`, `jglue`, `llm-jp-eval` |

If none fits, translate the topic literally to English and add `japanese` / `日本語` modifiers.

### Step 2 — Locate the existing data file

The data file ships with the plugin. Resolve its path via `${CLAUDE_PLUGIN_ROOT}` (Claude Code substitutes this inline in skill content), falling back to a scoped search only if the install is unusual:

```bash
RESOURCES_PATH="${CLAUDE_PLUGIN_ROOT}/data/resources.json"
[ -f "$RESOURCES_PATH" ] || RESOURCES_PATH="$(find "${HOME}/.claude/plugins" -type f -name resources.json 2>/dev/null | grep "awesome-japanese-nlp-resources/" | head -1)"
echo "RESOURCES_PATH=$RESOURCES_PATH"
```

Use the resulting absolute `RESOURCES_PATH` below.

### Step 3 — Build the existing-URL set

The plugin's `resources.json` may lag behind the repo's `README.md` — some entries exist only in the README. To avoid false "new resource" reports, prefer the pre-built `data/existing_urls.txt` (emitted by `build_data.py`) when present and fall back to a live README scan otherwise.

Create a temporary file for the merged URL set (so concurrent runs don't clobber each other):

```bash
EXISTING_URLS_FILE=$(mktemp -t awesome_ja_nlp_urls.XXXXXX)
```

Then run the following Python block (substituting `RESOURCES_PATH` and `EXISTING_URLS_FILE`):

```python
python3 << 'EOF'
import json, re, os

RESOURCES_PATH = "RESOURCES_PATH"          # from Step 2
OUTPUT_PATH    = "EXISTING_URLS_FILE"      # from the mktemp above

data_dir = os.path.dirname(os.path.abspath(RESOURCES_PATH))
prebuilt = os.path.join(data_dir, "existing_urls.txt")

urls = set()
source = ""

# Fast path: use pre-built existing_urls.txt if present
if os.path.exists(prebuilt):
    with open(prebuilt) as f:
        urls = {line.strip().lower() for line in f if line.strip()}
    source = f"pre-built {prebuilt}"

# Fallback: derive from resources.json + walk to repo-root README.md
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

    count_json = len(urls)
    try:
        p = os.path.abspath(data_dir)
        readme_files = []
        for _ in range(6):
            p = os.path.dirname(p)
            readme = os.path.join(p, "README.md")
            if os.path.exists(readme):
                readme_files.append(readme)
            if os.path.exists(os.path.join(p, "awesome-japanese-nlp-resources.json")):
                break  # reached repo root
        for readme in readme_files:
            before = len(urls)
            with open(readme) as f:
                content = f.read()
            for url in re.findall(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", content):
                urls.add(url.lower().rstrip("/"))
            if len(urls) > before:
                print(f"Supplemented {len(urls)-before} URLs from {readme}")
    except Exception as e:
        print(f"README.md scan skipped ({e}), using resources.json only")
    source = f"derived ({count_json} from JSON, {len(urls)-count_json} from README walk)"

with open(OUTPUT_PATH, "w") as f:
    f.write("\n".join(sorted(urls)))
print(f"Loaded {len(urls)} existing URLs from {source} → {OUTPUT_PATH}")
EOF
```

Remember to clean up the temp file when the skill finishes (`rm -f "$EXISTING_URLS_FILE"`).

### Step 4 — Discover candidates via WebSearch

Run **4–6 WebSearch queries** to find candidate GitHub repos. Mix English and Japanese; vary phrasing to widen coverage. **Do not use the `gh` CLI in this project — rely on WebSearch + WebFetch only.**

- `<english-keyword> japanese site:github.com`
- `japanese <english-keyword> ${YEAR_NOW} site:github.com`
- `<topic> 日本語 github` (Japanese-side phrasing)
- `awesome japanese <english-keyword>`
- `<japanese-tool-name> github` (when a topic maps to known tool names like `mecab`, `sudachi`, `voicevox`)
- Optional: `<english-keyword> japanese language model ${YEAR_PREV}` for LLM-flavored topics

From each result, extract every URL matching `https://github.com/<owner>/<repo>` (ignore deeper paths like `/issues`, `/pull/`, `/blob/`, `/tree/`). Capture them into a candidate set, lowercased and with trailing slashes stripped.

### Step 5 — Filter against the existing dataset

Drop any candidate URL whose lowercased form (or its `https://github.com/owner/repo` prefix) is in `$EXISTING_URLS_FILE` (the temp file from Step 3). Deduplicate by `owner/repo` pair.

After filtering, you should have at most a few dozen unique candidates. If more than 20, prioritize those that appear in multiple WebSearch result sets (signal of relevance) and those with English keyword matches in the search-result title/snippet.

### Step 6 — Enrich top candidates via WebFetch

For each surviving candidate (cap at **10–15**), call `WebFetch` on the repo URL to confirm it exists and extract the essentials:

```
WebFetch url="https://github.com/<owner>/<repo>" prompt="Extract as JSON: name, one-line description, primary language, star count, last-updated date (in YYYY-MM format), whether the repo is archived, whether it is a fork, and whether the README / description mentions Japanese/日本語 NLP. If any field is unavailable, set it to null."
```

To keep latency manageable, **issue up to 5 WebFetch calls in parallel** (single message, multiple tool calls). If a candidate's page 404s or redirects unexpectedly, drop it.

From the WebFetch results, drop any candidate where:
- `archived: true` or `fork: true`
- The description / README does not mention Japanese / 日本語 / NLP
- `stars < 3` AND `last_updated` is more than 24 months ago

Keep the metadata for the survivors — you'll cite stars and last-updated date in the output.

### Step 7 — Categorize

Group the final survivors (target **5–15**) under awesome-japanese-nlp-resources section headings, inferred from `lang` and `description`:

| Heading | Cues |
|---|---|
| Python library | Python primary, library/SDK description |
| C++ | C++ primary, native library |
| Rust crate | Rust primary |
| JavaScript | JavaScript / TypeScript |
| Go | Go primary |
| Java | Java primary |
| Pretrained model | "model", "weights", "fine-tuned", links to HuggingFace |
| ChatGPT / LLM application | LLM app, RAG, agent |
| Dictionary and IME | dictionary, lexicon, IME |
| Corpus | corpus, dataset, annotation |
| Tutorial | tutorial, course, lecture, "学習", "入門" |
| Research summary | survey, paper list, "サーベイ" |

### Step 8 — Output contribution-ready markdown

**Language detection rule (apply before writing any output):**
- `$ARGUMENTS` is empty → **English**
- `$ARGUMENTS` contains Japanese characters (hiragana / katakana / kanji) → **Japanese**
- Otherwise → **English**

Apply the detected language to all headings and prose. Resource descriptions in the bullet lines are always in **English** regardless of output language (the awesome list standard).

**English output template (default):**

```
## New candidates for "$ARGUMENTS"

Found **N** GitHub repositories not yet in awesome-japanese-nlp-resources.

*(Search keywords: keyword1, keyword2, ...)*

### Python library
* [repo-name](https://github.com/owner/repo) - One-line English description. (⭐ 123, last updated: YYYY-MM)
* ...

### Corpus
* ...

---

### Notes

- The `<dominant category>` category is most active in the "$ARGUMENTS" space
- Suggested section in `README.md`: `<section-name>`
- Highlight: <name> (⭐ N) — short reason why it stands out
- Follow-up suggestion: <alternative keywords to try next>
```

**Japanese output template (when query is in Japanese):**

```
## "$ARGUMENTS" に関する追加候補

awesome-japanese-nlp-resources に未収録の GitHub リポジトリ **N 件** を発見しました。

*(検索キーワード: keyword1, keyword2, ...)*

### Python library
* [repo-name](https://github.com/owner/repo) - One-line English description. (⭐ 123, 最終更新: YYYY-MM)
* ...

### Corpus
* ...

---

### 追加の検討メモ

- "$ARGUMENTS" 領域では `<dominant category>` のリポジトリが特に活発
- 推奨追加先: `README.md` の `<section-name>` セクション
- 注目株: <name> (⭐ N) — 短い推薦理由
- フォローアップ提案: <その他のキーワードで再検索すると良い場合の提案>
```

**Rules for the bullet lines:**
- Format `* [name](url) - description` matches the existing README.md contribution style exactly — paste-ready for a PR
- Keep the description ≤ 100 characters and in **English**. If the repo's own README/description is in Japanese, translate it to English for the bullet line (the awesome list keeps resource descriptions in English)
- For English output, append `(⭐ N, last updated: YYYY-MM)`; for Japanese output, append `(⭐ N, 最終更新: YYYY-MM)`
- If `last_updated` is null from WebFetch, write `last updated: unknown` (English) or `最終更新: 不明` (Japanese)
- If no candidates remain after filtering, output:

  English:
  ```
  ## New candidates for "$ARGUMENTS"

  No unlisted repositories found.

  Suggestions:
  - Retry with different keywords: `<suggested keywords>`
  - Check existing similar resources with `/awesome-japanese-nlp-resources:search "$ARGUMENTS"`
  ```

  Japanese:
  ```
  ## "$ARGUMENTS" に関する追加候補

  該当する未収録リポジトリは見つかりませんでした。

  検討事項:
  - 別キーワードで再試行: `<suggested keywords>`
  - 既存リスト内で類似カテゴリを `/awesome-japanese-nlp-resources:search "$ARGUMENTS"` で確認
  ```

### Step 9 — Sources

Append the `Sources:` section required by WebSearch — list the URLs of the WebSearch results you actually used.

Finally, clean up the temp file: `rm -f "$EXISTING_URLS_FILE"`
