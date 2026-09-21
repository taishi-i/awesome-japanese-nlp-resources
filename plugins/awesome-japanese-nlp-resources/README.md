# awesome-japanese-nlp-resources

Search, discover, and track 1,350+ Japanese NLP resources directly from [Claude Code](https://claude.ai/code) or [Codex](https://developers.openai.com/codex).

This plugin ships four skills that work together across all categories of [awesome-japanese-nlp-resources](https://github.com/taishi-i/awesome-japanese-nlp-resources): libraries, pretrained models, datasets, tutorials, dictionaries, and Hugging Face resources. It also covers [multilingual libraries, models, and datasets that also support Japanese](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/multilingual.md), such as language detectors, speech and OCR models, and search engines with Japanese analyzers.

Claude Code and Codex share the same skills (`skills/*/SKILL.md`) and the same bundled data (`data/`). Each tool reads its own manifest: `.claude-plugin/plugin.json` for Claude Code and `.codex-plugin/plugin.json` for Codex.

## Install

### Claude Code

**Inside Claude Code:**
```shell
/plugin marketplace add taishi-i/awesome-japanese-nlp-resources
/plugin install awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

**Via CLI:**
```bash
claude plugin marketplace add taishi-i/awesome-japanese-nlp-resources
claude plugin install awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

**From a local clone:**
```bash
git clone https://github.com/taishi-i/awesome-japanese-nlp-resources
cd awesome-japanese-nlp-resources
claude plugin marketplace add ./.claude-plugin/marketplace.json
claude plugin install awesome-japanese-nlp-resources
```

### Codex

```bash
codex plugin marketplace add taishi-i/awesome-japanese-nlp-resources
codex plugin add awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

Start a new Codex session afterwards so the skills are loaded. Once the marketplace is added, the plugin can also be installed from `/plugins` inside Codex.

**From a local clone:**
```bash
git clone https://github.com/taishi-i/awesome-japanese-nlp-resources
cd awesome-japanese-nlp-resources
codex plugin marketplace add .
codex plugin add awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

The skills run small Python 3 scripts over the bundled data, so Codex needs to be able to run shell commands; read-only access is enough. `discover`, `compare`, and `research` also use Codex's built-in web search.

## Update

To get the latest data, run:

**Claude Code:**
```shell
/plugin update awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

Or via CLI:
```bash
claude plugin update awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

**Codex:**
```bash
codex plugin marketplace upgrade awesome-japanese-nlp-resources
codex plugin add awesome-japanese-nlp-resources@awesome-japanese-nlp-resources
```

## Skills

This plugin ships four skills. The commands below use the Claude Code form; in Codex, mention the same skills with `$` instead of `/` (e.g. `$awesome-japanese-nlp-resources:search <query>`). Both tools can also pick the matching skill on their own when you simply ask a question:

| Command | Purpose |
|---|---|
| `/awesome-japanese-nlp-resources:search <query>` | Search the bundled 1,350+ resource dataset |
| `/awesome-japanese-nlp-resources:discover <tool-or-topic>` | Given a tool, find alternatives (listed and unlisted); given a topic, find contribution candidates not yet in the list |
| `/awesome-japanese-nlp-resources:compare <tool-or-topic>` | Compare several libraries/models/datasets across a few criteria as a ○/△/✕ table |
| `/awesome-japanese-nlp-resources:research <topic>` | Survey the dataset + latest web research for a combined trend + challenges report |

---

### `search` — query the bundled dataset

Searches the bundled dataset by keyword or natural language query. Accepts any language — queries are internally translated to English stems for matching, then results are presented in the query language.

After the results list, outputs a **use-case selection guide table** that maps common scenarios (fine-tuning, evaluation, building an app, etc.) to the single best resource for each.

```shell
/awesome-japanese-nlp-resources:search <query>
```

Examples:

```shell
/awesome-japanese-nlp-resources:search tokenizer
/awesome-japanese-nlp-resources:search BERT
/awesome-japanese-nlp-resources:search named entity recognition
/awesome-japanese-nlp-resources:search 形態素解析
/awesome-japanese-nlp-resources:search text classification dataset
/awesome-japanese-nlp-resources:search sentence embedding huggingface
```

---

### `discover` — find alternatives, or find what's missing

Takes **either** a specific repository/model/tool (GitHub URL, Hugging Face URL, `owner/repo`, or a bare tool/model name) **or** a topic, and reports both **what's already in the list** and **what's not yet listed**.

- **Given a tool** (`mecab`, `https://github.com/polm/cutlet`, ...): mines the bundled dataset for content-similar entries — scoring every candidate by shared category, shared semantic labels (IDF-weighted so rare labels like *Sentiment Analysis* outweigh ubiquitous ones), and shared description terms — then uses web search (Claude Code's `WebSearch` + `WebFetch`, or Codex's built-in web search) across **both GitHub and Hugging Face** to surface alternatives that aren't cataloged yet.
- **Given a topic** (`形態素解析`, `japanese LLM fine-tuning`, ...): searches the dataset by keyword, then runs the same web discovery pipeline to propose new candidates for that topic.

Either way, low-quality web candidates (fewer than 3 stars/likes **and** inactive for over 2 years, archived, or an unmaintained fork) are automatically filtered out, and the "not yet in the list" bullets are contribution-ready — GitHub lines match the existing `README.md` style, Hugging Face lines match `docs/huggingface.md`, both paste-ready for a PR.

Calling with no argument runs a **general search for the latest Japanese NLP resources** from the past year or so.

```shell
/awesome-japanese-nlp-resources:discover <github-url | huggingface-url | owner/repo | tool-name | topic>
/awesome-japanese-nlp-resources:discover          # general latest-resources scan
```

Examples:

```shell
/awesome-japanese-nlp-resources:discover mecab
/awesome-japanese-nlp-resources:discover fugashi
/awesome-japanese-nlp-resources:discover https://github.com/polm/cutlet
/awesome-japanese-nlp-resources:discover https://huggingface.co/cl-nagoya/ruri-large
/awesome-japanese-nlp-resources:discover 形態素解析
/awesome-japanese-nlp-resources:discover japanese LLM fine-tuning
/awesome-japanese-nlp-resources:discover RAG 日本語
```

---

### `compare` — side-by-side ○/△/✕ comparison

Takes **either** a specific tool (compared against its closest peers) **or** a topic (compared across its leading options), picks **3–6 comparable candidates**, then the agent (Claude or Codex) chooses **3–5 criteria** relevant to that specific comparison (not a fixed checklist) and rates every candidate on each as ○ (clearly supports / strong), △ (partial or unverified), or ✕ (does not support / weak). Ratings are grounded in the dataset plus a fetch of each candidate's page where a rating would otherwise be a guess.

Output is a single table plus notes justifying any non-obvious △/✕ rating and a short recommendation.

```shell
/awesome-japanese-nlp-resources:compare <github-url | huggingface-url | owner/repo | tool-name | topic>
```

Examples:

```shell
/awesome-japanese-nlp-resources:compare mecab
/awesome-japanese-nlp-resources:compare 形態素解析
/awesome-japanese-nlp-resources:compare japanese sentence embedding models
/awesome-japanese-nlp-resources:compare OCR
```

---

### `research` — trend + challenge report for a topic

Combines the bundled dataset (current state) with live web search (latest releases, papers, model launches, known limitations, ongoing efforts) and produces a scannable report with sections: Overview / Current resources / Latest trends / Known challenges / Current efforts / Still unsolved / References.

Calling with no argument produces a **general overview of the current Japanese NLP landscape** across all sub-fields.

```shell
/awesome-japanese-nlp-resources:research <topic>
/awesome-japanese-nlp-resources:research             # general landscape overview
```

Examples:

```shell
/awesome-japanese-nlp-resources:research 日本語LLM
/awesome-japanese-nlp-resources:research japanese embedding models
/awesome-japanese-nlp-resources:research RAG 日本語
/awesome-japanese-nlp-resources:research speech synthesis japanese
```

---

## Output language

All four skills detect the query language and respond in kind:

| Query | Output language |
|---|---|
| Contains Japanese characters (hiragana / katakana / kanji) | Japanese |
| English or empty | English (default) |

Resource descriptions in `discover`'s "not yet in the list" bullet lines are always in English regardless of output language, matching the contribution style of the awesome list.

Queries in other languages (Chinese, Korean, etc.) fall back to English output today; broader multilingual support is a future direction.

## Ranking

`search` results are ranked by a combined score:

1. **Text relevance** — keyword matches in name, description, subcategory, category, and aliases
2. **Popularity** — GitHub stars (normalized) for libraries/models; Hugging Face downloads (normalized) for HF resources
3. **Quality signal** — pre-computed activity score reflecting stars, downloads, and commit history
4. **Agent re-ranking** — the final top candidates are re-ordered by Claude's or Codex's semantic judgment (category fit, specificity, recency)

`discover` ranks differently depending on mode: given a tool, it scores each candidate by **content similarity to the seed** (shared category, IDF-weighted shared labels, shared description terms); given a topic, it scores by the same keyword matching as `search`. Either way, the agent (Claude or Codex) re-ranks the merged local + web set by functional closeness before presenting it.

`compare` doesn't rank at all — it selects 3–6 candidates the same way `discover` does, then rates each one independently against criteria the agent chooses for that comparison (○/△/✕), grounded in the dataset and, where needed, a fetch of the candidate's own page.

## Data coverage

All data is bundled in the plugin at `data/resources.json` and sourced from the upstream awesome-japanese-nlp-resources dataset.

<!-- BEGIN AUTO-COUNTS — regenerated by build_data.py; do not edit by hand -->
| Category | Source | Count |
|----------|--------|-------|
| Python library | GitHub | 346 |
| Corpus / Dataset | GitHub | 223 |
| Hugging Face models | Hugging Face | 174 |
| Hugging Face datasets | Hugging Face | 137 |
| JavaScript / Rust / C++ / Go / Java | GitHub | 131 |
| Dictionary and IME | GitHub | 88 |
| Pretrained model / ChatGPT | GitHub | 68 |
| Tutorials / Research summaries | GitHub | 42 |
| **Total** | | **1,209** |
<!-- END AUTO-COUNTS -->

## License

CC0-1.0 — Public Domain
