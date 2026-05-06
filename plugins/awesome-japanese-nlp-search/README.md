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

## Data coverage

All data is bundled in the plugin and sourced from this repository.

| Category | Source | Count |
|----------|--------|-------|
| Libraries (Python, C++, Rust, JS, Go, Java) | GitHub | 450 |
| Hugging Face models | huggingface.md | 208 |
| Corpora / Datasets | GitHub | 208 |
| Hugging Face datasets | huggingface.md | 156 |
| Dictionaries / IME | GitHub | 83 |
| Pretrained models | GitHub | 69 |
| Tutorials / Research summaries | GitHub | 38 |
| **Total** | | **1,212** |

## License

CC0-1.0 — Public Domain
