# awesome-japanese-nlp-search

Search 1,200+ Japanese NLP resources directly from [Claude Code](https://claude.ai/code).

This plugin provides a single skill that searches across all categories of [awesome-japanese-nlp-resources](https://github.com/taishi-i/awesome-japanese-nlp-resources): libraries, pretrained models, datasets, tutorials, dictionaries, and Hugging Face resources.

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

## Usage

```shell
/awesome-japanese-nlp-search:search <query>
```

### Examples

```shell
/awesome-japanese-nlp-search:search tokenizer
/awesome-japanese-nlp-search:search BERT
/awesome-japanese-nlp-search:search named entity recognition
/awesome-japanese-nlp-search:search morphology python
/awesome-japanese-nlp-search:search text classification dataset
/awesome-japanese-nlp-search:search sentence embedding huggingface
```

## Ranking

Search results are ranked by a combined score:

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
