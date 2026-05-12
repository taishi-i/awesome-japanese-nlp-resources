# awesome-japanese-nlp-search

Search, discover, and track 1,200+ Japanese NLP resources directly from [Claude Code](https://claude.ai/code).

This plugin ships three skills that work together across all categories of [awesome-japanese-nlp-resources](https://github.com/taishi-i/awesome-japanese-nlp-resources): libraries, pretrained models, datasets, tutorials, dictionaries, and Hugging Face resources.

## Install

**Inside Claude Code:**
```shell
/plugin marketplace add taishi-i/awesome-japanese-nlp-resources
/plugin install awesome-japanese-nlp-search@awesome-japanese-nlp-search
```

**Via CLI:**
```bash
claude plugin marketplace add taishi-i/awesome-japanese-nlp-resources
claude plugin install awesome-japanese-nlp-search@awesome-japanese-nlp-search
```

**From a local clone:**
```bash
git clone https://github.com/taishi-i/awesome-japanese-nlp-resources
cd awesome-japanese-nlp-resources
claude plugin marketplace add ./.claude-plugin/marketplace.json
claude plugin install awesome-japanese-nlp-search
```

## Update

To get the latest data, run:

```shell
/plugin update awesome-japanese-nlp-search@awesome-japanese-nlp-search
```

Or via CLI:
```bash
claude plugin update awesome-japanese-nlp-search@awesome-japanese-nlp-search
```

## Skills

This plugin ships three skills:

| Command | Purpose |
|---|---|
| `/awesome-japanese-nlp-search:search <query>` | Search the bundled 1,200+ resource dataset |
| `/awesome-japanese-nlp-search:find-new-resources <topic>` | Discover GitHub repos NOT yet in the list — contribution helper |
| `/awesome-japanese-nlp-search:research-trends <topic>` | Survey the dataset + latest web research for a digestible trend report |

---

### `search` — query the bundled dataset

Searches the bundled dataset by keyword or natural language query. Accepts any language — queries are internally translated to English stems for matching, then results are presented in the query language.

After the results list, outputs a **use-case selection guide table** that maps common scenarios (fine-tuning, evaluation, building an app, etc.) to the single best resource for each.

```shell
/awesome-japanese-nlp-search:search <query>
```

Examples:

```shell
/awesome-japanese-nlp-search:search tokenizer
/awesome-japanese-nlp-search:search BERT
/awesome-japanese-nlp-search:search named entity recognition
/awesome-japanese-nlp-search:search 形態素解析
/awesome-japanese-nlp-search:search text classification dataset
/awesome-japanese-nlp-search:search sentence embedding huggingface
```

---

### `find-new-resources` — propose additions to the list

Discovers GitHub repositories related to a topic that are **not** yet in `awesome-japanese-nlp-resources`. Uses WebSearch to surface candidates and WebFetch to verify each repo (stars, last-updated date, archived/fork status, Japanese NLP coverage). Low-quality repos (fewer than 3 stars **and** inactive for over 2 years) are automatically filtered out.

Output is contribution-ready markdown — bullet lines match the existing README style and can be pasted directly into a PR.

Calling with no argument runs a **general search for the latest Japanese NLP resources** added in 2025–2026.

```shell
/awesome-japanese-nlp-search:find-new-resources <topic>
/awesome-japanese-nlp-search:find-new-resources          # general latest-resources scan
```

Examples:

```shell
/awesome-japanese-nlp-search:find-new-resources 形態素解析
/awesome-japanese-nlp-search:find-new-resources japanese LLM fine-tuning
/awesome-japanese-nlp-search:find-new-resources RAG 日本語
/awesome-japanese-nlp-search:find-new-resources speech recognition
```

---

### `research-trends` — trend report for a topic

Combines the bundled dataset (current state) with live WebSearch (latest releases, papers, model launches) and produces a short scannable report (~600 words) with sections: Overview / Current resources / Latest trends / Key takeaways / References.

Calling with no argument produces a **general overview of current Japanese NLP trends** across all sub-fields.

```shell
/awesome-japanese-nlp-search:research-trends <topic>
/awesome-japanese-nlp-search:research-trends             # general trend overview
```

Examples:

```shell
/awesome-japanese-nlp-search:research-trends 日本語LLM
/awesome-japanese-nlp-search:research-trends japanese embedding models
/awesome-japanese-nlp-search:research-trends RAG 日本語
/awesome-japanese-nlp-search:research-trends speech synthesis japanese
```

---

## Output language

All three skills detect the query language and respond in kind:

| Query | Output language |
|---|---|
| Contains Japanese characters (hiragana / katakana / kanji) | Japanese |
| English or empty | English (default) |

Resource descriptions in `find-new-resources` bullet lines are always in English regardless of output language, matching the contribution style of the awesome list.

## Ranking

`search` results are ranked by a combined score:

1. **Text relevance** — keyword matches in name, description, subcategory, and category
2. **Popularity** — GitHub stars (normalized) for libraries/models; Hugging Face downloads (normalized) for HF resources
3. **Quality signal** — pre-computed activity score reflecting stars, downloads, and commit history
4. **Claude re-ranking** — the final top-15 are re-ordered by Claude's semantic judgment (category fit, specificity, recency)

## Data coverage

All data is bundled in the plugin and sourced from `awesome-japanese-nlp-resources-search.json`.

| Category | Source | Count |
|----------|--------|-------|
| Python library | GitHub | 334 |
| Corpus / Dataset | GitHub | 208 |
| Hugging Face models | Hugging Face | 208 |
| Hugging Face datasets | Hugging Face | 156 |
| Dictionary and IME | GitHub | 83 |
| Pretrained model / ChatGPT | GitHub | 69 |
| JavaScript / Rust / C++ / Go / Java | GitHub | 116 |
| Tutorials / Research summaries | GitHub | 38 |
| **Total** | | **1,212** |

## License

CC0-1.0 — Public Domain
