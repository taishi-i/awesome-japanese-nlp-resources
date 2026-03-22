# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of resources dedicated to Python libraries, llms, dictionaries, and corpora of NLP for Japanese

- Listed information on [848 GitHub repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md)
- Listed information on [273 Hugging Face repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md) (models and datasets)
- 🎉 We are excited to announce the release of [awesome-japanese-nlp-survey](https://awesome-japanese-nlp-survey.vercel.app/) on March 1, 2026!


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## 🎉 The latest additions

**Corpus**
 * [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) - VLM Evaluation Benchmark for Understanding Software Diagrams (Japanese, English, Korean supported)
 * [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) - Performance evaluation benchmark of Long Context LLM in the Japanese HR domain.

_Updated on Mar 22, 2026_

## Contents
 * [Hugging Face](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md)
   * [Models](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md#models)
   * [Datasets](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md#datasets)
 * [Python library](#python-library)
   * [Morphology analysis](#morphology-analysis)
   * [Parsing](#parsing)
   * [Converter](#converter)
   * [Preprocessor](#preprocessor)
   * [Sentence spliter](#sentence-spliter)
   * [Sentiment analysis](#sentiment-analysis)
   * [Machine translation](#machine-translation)
   * [Named entity recognition](#named-entity-recognition)
   * [OCR](#ocr)
   * [Tool for pretrained models](#tool-for-pretrained-models)
   * [Others](#others)
 * [C++](#c)
   * [Morphology analysis](#morphology-analysis-1)
   * [Parsing](#parsing-1)
   * [Others](#others-1)
 * [Rust crate](#rust-crate)
   * [Morphology analysis](#morphology-analysis-2)
   * [Converter](#converter-1)
   * [Search engine library](#search-engine-library)
   * [Others](#others-2)
 * [JavaScript](#javaScript)
   * [Morphology analysis](#morphology-analysis-3)
   * [Converter](#converter-2)
   * [Others](#others-3)
 * [Go](#go)
   * [Morphology analysis](#morphology-analysis-4)
   * [Others](#others-4)
 * [Java](#java)
   * [Morphology analysis](#morphology-analysis-5)
   * [Others](#others-5)
 * [Pretrained model](#pretrained-model)
   * [Word2Vec](#word2Vec)
   * [Transformer based models](#transformer-based-models)
 * [ChatGPT](#chatgpt)
 * [Dictionary and IME](#dictionary-and-ime)
 * [Corpus](#corpus)
   * [Part-of-speech tagging / Named entity recognition](#part-of-speech-tagging--named-entity-recognition)
   * [Text classification](#text-classification)
   * [Parallel corpus](#parallel-corpus)
   * [Dialog corpus](#dialog-corpus)
   * [Others](#others-3)
 * [Tutorial](#tutorial)
 * [Research summary](#research-summary)
 * [Reference](#reference)
 * [Contributors](#contributors)


## Python library

### Morphology analysis
Libraries that split Japanese text into words or morphemes and assign part-of-speech and base forms

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - SudachiPy 0.6* and above are developed as Sudachi.rs.
 * [Janome](https://github.com/mocobeta/janome) - Japanese morphological analysis engine written in pure Python
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - mecab-python. mecab-python. you can find original version here:http://taku910.github.io/mecab/
 * [mecab](https://github.com/ikegami-yukino/mecab) - This repository is for building Windows 64-bit MeCab binary and improving MeCab Python binding.
 * [fugashi](https://github.com/polm/fugashi) - A Cython MeCab wrapper for fast, pythonic Japanese tokenization and morphological analysis.
 * [nagisa](https://github.com/taishi-i/nagisa) - A Japanese tokenizer based on recurrent neural networks
 * [pyknp](https://github.com/ku-nlp/pyknp) - A Python Module for JUMAN++/KNP
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - Python wrapper for KyTea
 * [konoha](https://github.com/himkt/konoha) - Konoha: Simple wrapper of Japanese Tokenizers
 * [natto-py](https://github.com/buruzaemon/natto-py) - natto-py combines the Python programming language with MeCab, the part-of-speech and morphological analyzer for the Japanese language.
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - Rakuten MA (Python version)
 * [python-vaporetto](https://github.com/daac-tools/python-vaporetto) -  Vaporetto is a fast and lightweight pointwise prediction based tokenizer. This is a Python wrapper for Vaporetto.
 * [dango](https://github.com/mkartawijaya/dango) - An easy to use tokenizer for Japanese text, aimed at language learners and non-linguists
 * [rhoknp](https://github.com/ku-nlp/rhoknp) - Yet another Python binding for Juman++/KNP
 * [python-vibrato](https://github.com/daac-tools/python-vibrato) -  Viterbi-based accelerated tokenizer (Python wrapper)
 * [jagger-python](https://github.com/lighttransport/jagger-python) - Python binding for Jagger(C++ implementation of Pattern-based Japanese Morphological Analyzer)
 * [Mecari](https://github.com/zbller/Mecari) - Mecari (Japanese Morphological Analysis with Graph Neural Networks)


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [SudachiPy](https://github.com/WorksApplications/SudachiPy) | 📥 326k | 📦 62M | ⭐ 429 | 🔴 october 2022|
| 🔗 [Janome](https://github.com/mocobeta/janome) | 📥 84k | 📦 11M | ⭐ 907 | 🟡 october 2025|
| 🔗 [mecab-python3](https://github.com/SamuraiT/mecab-python3) | 📥 164k | 📦 36M | ⭐ 580 | 🟡 november 2025|
| 🔗 [mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python) | 📥 16k | 📦 679k | ⭐ 272 | 🔴 october 2024|
| 🔗 [fugashi](https://github.com/polm/fugashi) | 📥 106k | 📦 14M | ⭐ 516 | 🟡 october 2025|
| 🔗 [nagisa](https://github.com/taishi-i/nagisa) | 📥 40k | 📦 8M | ⭐ 415 | 🟢 february|
| 🔗 [pyknp](https://github.com/ku-nlp/pyknp) | 📥 2k | 📦 3M | ⭐ 92 | 🟢 january|
| 🔗 [Mykytea-python](https://github.com/chezou/Mykytea-python) | 📥 950 | 📦 556k | ⭐ 36 | 🔴 january 2024|
| 🔗 [konoha](https://github.com/himkt/konoha) | 📥 61k | 📦 6M | ⭐ 261 | 🟢 march|
| 🔗 [natto-py](https://github.com/buruzaemon/natto-py) | 📥 341k | 📦 34M | ⭐ 95 | 🔴 november 2023|
| 🔗 [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) | 📥 13 | 📦 27k | ⭐ 23 | 🔴 may 2017|
| 🔗 [python-vaporetto](https://github.com/daac-tools/python-vaporetto) | 📥 285 | 📦 175k | ⭐ 21 | 🟡 june 2025|
| 🔗 [dango](https://github.com/mkartawijaya/dango) | 📥 58 | 📦 26k | ⭐ 25 | 🔴 november 2021|
| 🔗 [rhoknp](https://github.com/ku-nlp/rhoknp) | 📥 18k | 📦 1M | ⭐ 38 | 🟢 january|
| 🔗 [python-vibrato](https://github.com/daac-tools/python-vibrato) | 📥 304 | 📦 117k | ⭐ 43 | 🔴 september 2024|
| 🔗 [jagger-python](https://github.com/lighttransport/jagger-python) | 📥 2k | 📦 298k | ⭐ 13 | 🔴 march 2024|
| 🔗 [Mecari](https://github.com/zbller/Mecari) | - | - | ⭐ 39 | 🟡 september 2025|


### Parsing
Libraries that analyze syntactic and dependency structures of Japanese sentences

 * [ginza](https://github.com/megagonlabs/ginza) - A Japanese NLP Library using spaCy as framework based on Universal Dependencies
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - Camphr - NLP libary for creating pipeline components
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese with BERT models
 * [depccg](https://github.com/masashi-y/depccg) - A* CCG Parser with a Supertag and Dependency Factored Model
 * [bertknp](https://github.com/ku-nlp/bertknp) - A Japanese dependency parser based on BERT
 * [esupar](https://github.com/KoichiYasuoka/esupar) - Tokenizer POS-Tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models for Japanese and other languages
 * [yomikata](https://github.com/passaglia/yomikata) - Heteronym disambiguation library using a fine-tuned BERT model.
 * [jdepp-python](https://github.com/lighttransport/jdepp-python) - Python binding for J.DepP(C++ implementation of Japanese Dependency Parsers)
 * [lightblue](https://github.com/daisukebekki/lightblue) - A CCG parser for Japanese with DTS-representations
 * [natsume-simple](https://github.com/borh-lab/natsume-simple) - natsume-simple is a Japanese dependency relation search system.
 * [jdeppy](https://github.com/matsurih/jdeppy) - Python wrapper for J.DepP, fast Japanese Dependency Parser


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ginza](https://github.com/megagonlabs/ginza) | 📥 14k | 📦 2M | ⭐ 838 | 🔴 march 2024|
| 🔗 [cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python) | 📥 42 | 📦 54k | ⭐ 7 | 🔴 august 2022|
| 🔗 [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) | 📥 485 | 📦 329k | ⭐ 38 | 🟡 december 2025|
| 🔗 [camphr](https://github.com/PKSHATechnology-Research/camphr) | 📥 225 | 📦 269k | ⭐ 337 | 🔴 august 2021|
| 🔗 [SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic) | 📥 249 | 📦 119k | ⭐ 20 | 🔴 repo not found|
| 🔗 [depccg](https://github.com/masashi-y/depccg) | 📥 52 | 📦 46k | ⭐ 98 | 🔴 august 2023|
| 🔗 [bertknp](https://github.com/ku-nlp/bertknp) | - | - | ⭐ 23 | 🔴 october 2021|
| 🔗 [esupar](https://github.com/KoichiYasuoka/esupar) | 📥 472 | 📦 170k | ⭐ 55 | 🟢 february|
| 🔗 [yomikata](https://github.com/passaglia/yomikata) | 📥 40 | 📦 50k | ⭐ 32 | 🔴 october 2023|
| 🔗 [jdepp-python](https://github.com/lighttransport/jdepp-python) | 📥 2k | 📦 283k | ⭐ 4 | 🔴 february 2024|
| 🔗 [lightblue](https://github.com/daisukebekki/lightblue) | - | - | ⭐ 27 | 🟢 last friday|
| 🔗 [natsume-simple](https://github.com/borh-lab/natsume-simple) | - | - | ⭐ 5 | 🔴 february 2025|
| 🔗 [jdeppy](https://github.com/matsurih/jdeppy) | 📥 20 | 📦 11k | ⭐ 3 | 🔴 february 2022|


### Converter
Libraries that convert between character types such as kana, romaji, and full-width/half-width forms

 * [pykakasi](https://github.com/miurahr/pykakasi) - Lightweight converter from Japanese Kana-kanji sentences into Kana-Roman.
 * [cutlet](https://github.com/polm/cutlet) - Japanese to romaji converter in Python
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - Convert English alphabet to Katakana
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - Converts Arabic numerals, or 'western' style numbers, to a Japanese context.
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Mozc for Python: Kana-Kanji converter
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - Japanese text parser that separates Hiragana/Katakana strings into morae (syllables).
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - Script to convert Japanese text into phoneme sequence.
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - A fast character conversion and transliteration library based on the scheme defined for Japan National Tax Agency (国税庁) 's corporate number (法人番号) system.
 * [wiredify](https://github.com/eggplants/wiredify) - Convert japanese kana from ba-bi-bu-be-bo into va-vi-vu-ve-vo
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - Simple Python package (CLI/Python API) for getting japanese readings (yomigana) and accents using MeCab.
 * [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) - Python implementation of NormalizeNumexp for extracting and normalizing quantity expressions and time expressions.
 * [Jusho](https://github.com/nagataaaas/Jusho) - Easy wrapper for the postal code data of Japan
 * [yurenizer](https://github.com/sea-turt1e/yurenizer) - Japanese text normalizer that resolves spelling inconsistencies. （日本語表記揺れ解消ツール
 * [e2k](https://github.com/Patchethium/e2k) - A tool for automatic English to Katakana conversion
 * [alkana.py](https://github.com/zomysan/alkana.py) - A tool to get the katakana reading of an alphabetical string.
 * [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) - Program to convert English strings to Katakana
 * [kanjiconv](https://github.com/sea-turt1e/kanjiconv) - Kanji Converter to Hiragana, Katakana, Roman alphabet.
 * [kanjize](https://github.com/nagataaaas/kanjize) - Kanjize(カンジャイズ): Easy converter between Kanji-Number and Integer


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [pykakasi](https://github.com/miurahr/pykakasi) | 📥 321k | 📦 29M | ⭐ 444 | 🔴 july 2022|
| 🔗 [cutlet](https://github.com/polm/cutlet) | 📥 18k | 📦 1M | ⭐ 373 | 🟡 june 2025|
| 🔗 [alphabet2kana](https://github.com/shihono/alphabet2kana) | 📥 234 | 📦 58k | ⭐ 14 | 🟢 february|
| 🔗 [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) | - | - | ⭐ 50 | 🔴 november 2020|
| 🔗 [mozcpy](https://github.com/ikegami-yukino/mozcpy) | 📥 173 | 📦 13k | ⭐ 47 | 🔴 february 2025|
| 🔗 [jamorasep](https://github.com/tachi-hi/jamorasep) | 📥 82 | 📦 9k | ⭐ 11 | 🟢 february|
| 🔗 [text2phoneme](https://github.com/korguchi/text2phoneme) | - | - | ⭐ 13 | 🔴 may 2023|
| 🔗 [jntajis-python](https://github.com/opencollector/jntajis-python) | 📥 2k | 📦 115k | ⭐ 21 | 🟢 march|
| 🔗 [wiredify](https://github.com/eggplants/wiredify) | 📥 32 | 📦 6k | ⭐ 3 | 🟡 december 2025|
| 🔗 [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) | 📥 28 | 📦 4k | ⭐ 7 | 🟢 february|
| 🔗 [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) | 📥 16 | 📦 14k | ⭐ 8 | 🔴 april 2024|
| 🔗 [Jusho](https://github.com/nagataaaas/Jusho) | 📥 145 | 📦 55k | ⭐ 11 | 🔴 june 2024|
| 🔗 [yurenizer](https://github.com/sea-turt1e/yurenizer) | 📥 96 | 📦 18k | ⭐ 4 | 🔴 march 2025|
| 🔗 [e2k](https://github.com/Patchethium/e2k) | 📥 193 | 📦 25k | ⭐ 16 | 🟡 november 2025|
| 🔗 [alkana.py](https://github.com/zomysan/alkana.py) | - | - | ⭐ 34 | 🔴 october 2021|
| 🔗 [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) | - | - | ⭐ 4 | 🟢 february|
| 🔗 [kanjiconv](https://github.com/sea-turt1e/kanjiconv) | 📥 95 | 📦 12k | ⭐ 17 | 🟡 october 2025|
| 🔗 [kanjize](https://github.com/nagataaaas/kanjize) | 📥 17k | 📦 1M | ⭐ 68 | 🟡 june 2025|


### Preprocessor
Libraries that normalize and clean text before analysis

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - Japanese text normalizer for mecab-neologd
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - A Python-based tool for converting Japanese characters between Hiragana, Katakana, Hankaku, and Zenkaku.
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - A quick converter for Japanese half-width and full-width characters.
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - A powerful text cleaner for Japanese web texts
 * [HojiChar](https://github.com/HojiChar/HojiChar) - A text preprocessing tool that configures and manages multiple preprocessing steps.
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho is a Python module that facilitates bidirectional conversion between half-width katakana and full-width katakana in Japanese.
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - Yet Another Fast Japanese String Converter
 * [kairyou](https://github.com/bikatr7/kairyou) - Quickly preprocesses Japanese text using NLP/NER from SpaCy for Japanese translation or other NLP tasks.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [neologdn](https://github.com/ikegami-yukino/neologdn) | 📥 7k | 📦 1M | ⭐ 287 | 🟡 december 2025|
| 🔗 [jaconv](https://github.com/ikegami-yukino/jaconv) | 📥 556k | 📦 63M | ⭐ 342 | 🟢 february|
| 🔗 [mojimoji](https://github.com/studio-ousia/mojimoji) | 📥 59k | 📦 11M | ⭐ 152 | 🔴 january 2024|
| 🔗 [text-cleaning](https://github.com/ku-nlp/text-cleaning) | - | - | ⭐ 12 | 🔴 november 2022|
| 🔗 [HojiChar](https://github.com/HojiChar/HojiChar) | 📥 24k | 📦 873k | ⭐ 124 | 🟡 november 2025|
| 🔗 [utsuho](https://github.com/juno-rmks/utsuho) | 📥 333 | 📦 19k | ⭐ 4 | 🟢 yesterday|
| 🔗 [python-habachen](https://github.com/Hizuru3/python-habachen) | 📥 9k | 📦 2M | ⭐ 6 | 🟡 october 2025|
| 🔗 [kairyou](https://github.com/bikatr7/kairyou) | 📥 111 | 📦 31k | ⭐ 6 | 🟡 june 2025|


### Sentence spliter
Libraries that automatically detect sentence boundaries and split text

 * [Bunkai](https://github.com/megagonlabs/bunkai) - Sentence boundary disambiguation tool for Japanese texts (日本語文境界判定器)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - Japanese Sentence Breaker
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - Yet another sentence-level tokenizer for the Japanese text
 * [budoux](https://github.com/google/budoux) - Standalone. Small. Language-neutral. BudouX is the successor to Budou, the machine learning powered line break organizer tool.
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - japanese sentence segmentation library for python
 * [hasami](https://github.com/mkartawijaya/hasami) - A tool to perform sentence segmentation on Japanese text
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - Japanese Text Segmenter for Python written in Rust
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - Comparison of Japanese Sentence Segmentation Tools
 * [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) - Japanese sentence splitting(日本語文境界判定器), 40–250× faster via a Rust-accelerated Python library with near-perfect API compatibility with megagonlabs/bunkai.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bunkai](https://github.com/megagonlabs/bunkai) | 📥 442 | 📦 108k | ⭐ 199 | 🔴 august 2023|
| 🔗 [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) | 📥 15 | 📦 5k | ⭐ 14 | 🔴 february 2021|
| 🔗 [sengiri](https://github.com/ikegami-yukino/sengiri) | 📥 58 | 📦 136k | ⭐ 24 | 🟡 november 2025|
| 🔗 [budoux](https://github.com/google/budoux) | 📥 9k | 📦 430k | ⭐ 1.6k | 🟢 last thursday|
| 🔗 [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) | 📥 2k | 📦 189k | ⭐ 74 | 🔴 april 2023|
| 🔗 [hasami](https://github.com/mkartawijaya/hasami) | 📥 128 | 📦 39k | ⭐ 6 | 🔴 february 2021|
| 🔗 [kuzukiri](https://github.com/alinear-corp/kuzukiri) | 📥 113 | 📦 27k | ⭐ 6 | 🟡 june 2025|
| 🔗 [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) | - | - | ⭐ 9 | 🔴 february 2023|
| 🔗 [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) | 📥 95 | 📦 4k | ⭐ 71 | 🟡 october 2025|


### Sentiment analysis
Libraries that detect emotions or polarity in text

 * [oseti](https://github.com/ikegami-yukino/oseti) - Dictionary based Sentiment Analysis for Japanese
 * [negapoji](https://github.com/liaoziyang/negapoji) - Japanese document sentiment analysis to determine negative or positive.
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - Emotion analyzer for Japanese text
 * [asari](https://github.com/Hironsan/asari) - Japanese sentiment analyzer implemented in Python.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [oseti](https://github.com/ikegami-yukino/oseti) | 📥 190 | 📦 167k | ⭐ 97 | 🟡 august 2025|
| 🔗 [negapoji](https://github.com/liaoziyang/negapoji) | - | - | ⭐ 151 | 🔴 august 2017|
| 🔗 [pymlask](https://github.com/ikegami-yukino/pymlask) | 📥 23 | 📦 66k | ⭐ 116 | 🔴 july 2024|
| 🔗 [asari](https://github.com/Hironsan/asari) | 📥 109 | 📦 79k | ⭐ 152 | 🔴 october 2022|


### Machine translation
Libraries that automatically translate text between languages

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - An example usage of JParaCrawl pre-trained Neural Machine Translation (NMT) models.
 * [JASS](https://github.com/Mao-KU/JASS) - JASS: Japanese-specific Sequence to Sequence Pre-training for Neural Machine Translation (LREC2020) & Linguistically Driven Multi-Task Pre-Training for Low-Resource Neural Machine Translation (ACM TALLIP)
 * [PheMT](https://github.com/cl-tohoku/PheMT) - A phenomenon-wise evaluation dataset for Japanese-English machine translation robustness. The dataset is based on the MTNT dataset, with additional annotations of four linguistic phenomena; Proper Noun, Abbreviated Noun, Colloquial Expression, and Variant. COLING 2020.
 * [VISA](https://github.com/ku-nlp/VISA) - An ambiguous subtitles dataset for visual scene-aware machine translation
 * [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) - A command-line interface for translation using the plamo-2-translate model with local execution.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) | - | - | ⭐ 105 | 🔴 april 2021|
| 🔗 [JASS](https://github.com/Mao-KU/JASS) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [PheMT](https://github.com/cl-tohoku/PheMT) | - | - | ⭐ 19 | 🔴 february 2021|
| 🔗 [VISA](https://github.com/ku-nlp/VISA) | - | - | ⭐ 14 | 🔴 october 2022|
| 🔗 [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) | - | - | ⭐ 332 | 🟡 october 2025|


### Named entity recognition
Libraries that extract names of people, places, and organizations from text

 * [namaco](https://github.com/chakki-works/namaco) - Character Based Named Entity Recognition.
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia is an Extended Named Entity Dictionary from Wikipedia.
 * [noyaki](https://github.com/ken11/noyaki) - Converts character span label information to tokenized text-based label information.
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - This is a sample code for creating and using a model for named entity recognition task through finetuning of the BERT model.
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - Code for inferring the accuracy of named entity and relation extraction from a case report corpus based on detailed annotation criteria.
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp, A python module for geotagging Japanese texts.
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - Program for fine-tuning Japanese named entity recognition using BERT
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - Examples to finetune encoder-only and encoder-decoder transformers for Japanese language (Hugging Face) Resources
 * [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) - Named entity extraction using BERT fine-tuning


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namaco](https://github.com/chakki-works/namaco) | - | - | ⭐ 40 | 🔴 february 2018|
| 🔗 [entitypedia](https://github.com/chakki-works/entitypedia) | - | - | ⭐ 13 | 🔴 december 2018|
| 🔗 [noyaki](https://github.com/ken11/noyaki) | 📥 178 | 📦 20k | ⭐ 5 | 🔴 august 2022|
| 🔗 [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) | - | - | ⭐ 11 | 🔴 june 2022|
| 🔗 [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) | - | - | ⭐ 1 | 🔴 november 2021|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 82 | 📦 21k | ⭐ 22 | 🟡 october 2025|
| 🔗 [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) | - | - | ⭐ 5 | 🔴 september 2022|
| 🔗 [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) | - | - | ⭐ 16 | 🔴 october 2023|
| 🔗 [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) | - | - | ⭐ 2 | 🔴 june 2024|


### OCR
Libraries that recognize and extract text from images

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - About Optical character recognition for Japanese text, with the main focus being Japanese manga
 * [mokuro](https://github.com/kha-white/mokuro) - Read Japanese manga inside browser with selectable text.
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - Handwritten Japanese OCR demo using touch panel to draw the input text using Intel OpenVINO toolkit
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - Japanese OCR
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - NDLOCR application
 * [donut](https://github.com/clovaai/donut) - Official Implementation of OCR-free Document Understanding Transformer (Donut) and Synthetic Document Generator (SynthDoG), ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - Manga translator - retrieve Japanese manga from URL to translate manga images.
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - OCR system for recognizing modern Japanese magazines
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - Text recognition module for NDLOCR.
 * [Poricom](https://github.com/blueaxis/Poricom) - Optical character recognition in manga images. Manga OCR desktop application
 * [owocr](https://github.com/aurorawright/owocr) - Optical character recognition for Japanese text
 * [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) - Yomitoku is an AI-powered document image analysis package designed specifically for the Japanese language.
 * [findtextcenternet](https://github.com/lithium0003/findtextcenternet) - Japanese OCR with CenterNet
 * [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) - A simple OCR for manga (Japanese traditional and Japanese vertical)
 * [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) - Evaluate the performance of OCR on Japanese text images.
 * [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) - Fine-tune PaddleOCR-VL on the Manga109s dataset for Japanese manga text recognition. The base model struggles with vertical Japanese text reading order in manga. After fine-tuning, the model correctly handles manga-specific text layouts.
 * [MangaOCR](https://github.com/gnurt2041/MangaOCR) - A lightweight OCR model for Japanese text, especially in Manga
 * [meikiocr](https://github.com/rtr46/meikiocr) - high-speed, high-accuracy, local ocr for japanese video games
 * [meikipop](https://github.com/rtr46/meikipop) - universal japanese ocr popup dictionary for windows, linux and macos


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [manga-ocr](https://github.com/kha-white/manga-ocr) | 📥 3k | 📦 258k | ⭐ 2.6k | 🟡 june 2025|
| 🔗 [mokuro](https://github.com/kha-white/mokuro) | 📥 471 | 📦 93k | ⭐ 1.6k | 🟢 february|
| 🔗 [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) | - | - | ⭐ 38 | 🔴 april 2022|
| 🔗 [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) | - | - | ⭐ 245 | 🔴 april 2021|
| 🔗 [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) | - | - | ⭐ 650 | 🟡 september 2025|
| 🔗 [donut](https://github.com/clovaai/donut) | 📥 237 | 📦 198k | ⭐ 6.8k | 🔴 july 2023|
| 🔗 [JMTrans](https://github.com/ttop32/JMTrans) | - | - | ⭐ 90 | 🔴 january 2021|
| 🔗 [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) | - | - | ⭐ 153 | 🔴 july 2023|
| 🔗 [text_recognition](https://github.com/ndl-lab/text_recognition) | - | - | ⭐ 8 | 🔴 july 2023|
| 🔗 [Poricom](https://github.com/blueaxis/Poricom) | - | - | ⭐ 417 | 🔴 june 2023|
| 🔗 [owocr](https://github.com/aurorawright/owocr) | - | - | ⭐ 216 | 🟢 yesterday|
| 🔗 [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) | 📥 855 | 📦 83k | ⭐ 1.4k | 🟢 last tuesday|
| 🔗 [findtextcenternet](https://github.com/lithium0003/findtextcenternet) | - | - | ⭐ 57 | 🟡 august 2025|
| 🔗 [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-fogi-manga) | - | - | ⭐ 7 | 🔴 repo not found|
| 🔗 [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) | - | - | ⭐ 1 | 🔴 march 2024|
| 🔗 [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) | - | - | ⭐ 9 | 🟡 december 2025|
| 🔗 [MangaOCR](https://github.com/gnurt2041/MangaOCR) | - | - | ⭐ 35 | 🔴 may 2024|
| 🔗 [meikiocr](https://github.com/rtr46/meikiocr) | 📥 601 | 📦 20k | ⭐ 64 | 🟢 yesterday|
| 🔗 [meikipop](https://github.com/rtr46/meikipop) | - | - | ⭐ 241 | 🟢 last thursday|


### Tool for pretrained models
Libraries that utilize pretrained models to improve accuracy and efficiency

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE: Japanese General Language Understanding Evaluation
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - Use custom tokenizers in spacy-transformers
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - Conversation generation using T5.
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - To investigate various DNN text classifiers including MLP, CNN, RNN, BERT approaches.
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - Deploying sentiment analysis server with FastAPI and BERT
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - Masked Language Model-based Scoring for Japanese and Vietnamese
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - AllenNLP integration for Shiba: Japanese CANINE model
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - script to evaluate pre-trained Japanese word2vec model on Japanese similarity dataset
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - BERT-based GEC tagging for Japanese
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - 日本語-BPEエンコーダー
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - Japanese-BPEEncoder Version 2
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - Japanese grammar error correction tool
 * [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) - Japanese Stable Diffusion is a Japanese specific latent text-to-image diffusion model capable of generating photo-realistic images given any text input.
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - A BERT model for Nagisa.
 * [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) - Example code for prefix-tuning GPT/GPT-NeoX models and for inference with trained prefixes
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) - 日本語のトークナイザー（分かち書きツール）をTransformersライブラリ用に作成しました。
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP Language Model Evaluation Harness
 * [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) - How do different tokenizers perform on downstream tasks in scriptio continua languages?: A case study in Japanese - ACL SRW 2023
 * [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) - A framework for few-shot evaluation of autoregressive language models.
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classification
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP Language Model Evaluation Harness
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - The repository contains scripts and merge scripts that have been modified to adapt an Alpaca-Lora adapter for LoRA tuning when assuming the use of the "rinna/japanese-gpt-neox..." [gpt-neox] model converted to ggml.
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - This repository was created to evaluate the performance of character role-playing in Japanese LLM.
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - This repository supports YuzuAI's Rakuda leaderboard of Japanese LLMs, which is a Japanese-focused analogue of LMSYS' Vicuna eval.
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - This tool is designed to automatically evaluate large-scale Japanese language models across multiple datasets.
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - This repository contains the code for supervised fine-tuning of LLM-jp models.
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - This is a repository that summarizes the tokenizer related to LLM being developed at the LLM Study Group (LLM-jp).
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - 日本語言模型金融评估工具
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - Japanese Vicuna QA Benchmark
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - Swallow Project Large-Scale Language Model Evaluation Script
 * [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) - Swallow Project Post-learning Large-scale Language Model Evaluation Framework
 * [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) - pretrained doc2vec models on Japanese Wikipedia
 * [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) - A repository of Japanese Phoneme-Level BERT


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 337 | 🔴 march 2025|
| 🔗 [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) | 📥 3k | 📦 183k | ⭐ 16 | 🔴 august 2022|
| 🔗 [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) | - | - | ⭐ 9 | 🔴 january 2020|
| 🔗 [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) | - | - | ⭐ 2 | 🔴 april 2021|
| 🔗 [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) | - | - | ⭐ 5 | 🔴 february 2022|
| 🔗 [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) | 📥 58 | 📦 20k | ⭐ 12 | 🔴 june 2021|
| 🔗 [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) | - | - | ⭐ 12 | 🔴 november 2024|
| 🔗 [gector-ja](https://github.com/jonnyli1125/gector-ja) | - | - | ⭐ 19 | 🔴 june 2021|
| 🔗 [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) | - | - | ⭐ 41 | 🔴 september 2021|
| 🔗 [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) | - | - | ⭐ 41 | 🔴 january 2023|
| 🔗 [transformer-copy](https://github.com/youichiro/transformer-copy) | - | - | ⭐ 29 | 🔴 september 2020|
| 🔗 [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [nagisa_bert](https://github.com/taishi-i/nagisa_bert) | 📥 39 | 📦 57k | ⭐ 5 | 🟢 february|
| 🔗 [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) | - | - | ⭐ 18 | 🟢 march|
| 🔗 [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) | 📥 71 | 📦 28k | ⭐ 5 | 🔴 february 2024|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) | - | - | ⭐ 6 | 🔴 june 2023|
| 🔗 [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) | - | - | ⭐ 1 | 🔴 june 2023|
| 🔗 [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) | - | - | ⭐ 98 | 🔴 july 2023|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) | - | - | ⭐ 18 | 🔴 may 2023|
| 🔗 [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) | - | - | ⭐ 40 | 🔴 november 2023|
| 🔗 [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) | - | - | ⭐ 50 | 🔴 march 2024|
| 🔗 [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | - | - | ⭐ 149 | 🟢 march|
| 🔗 [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) | - | - | ⭐ 62 | 🔴 june 2024|
| 🔗 [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) | - | - | ⭐ 46 | 🟢 last wednesday|
| 🔗 [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | - | - | ⭐ 77 | 🟢 january|
| 🔗 [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | - | - | ⭐ 33 | 🔴 june 2024|
| 🔗 [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) | - | - | ⭐ 24 | 🟡 september 2025|
| 🔗 [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) | - | - | ⭐ 26 | 🟡 october 2025|
| 🔗 [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) | - | - | ⭐ 25 | 🔴 january 2019|
| 🔗 [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) | - | - | ⭐ 22 | 🔴 december 2023|


### Others
General-purpose tools supporting Japanese language processing

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - A tool for dividing the Japanese full name into a family name and a given name.
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - A curated list of resources dedicated to Python libraries of NLP for Japanese
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - Python-based Japanese semantic role labeling system (ASA)
 * [toiro](https://github.com/taishi-i/toiro) - A comparison tool of Japanese tokenizers
 * [ja-timex](https://github.com/yagays/ja-timex) - A rule-based parser for extracting/normalizing time expressions written in natural language.
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - A set of metrics for feature selection from text data
 * [daaja](https://github.com/kajyuuen/daaja) - This repository has implementations of data augmentation for NLP for Japanese.
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - The purpose of this repository is to make prototypes as case study in the context of proof of concept(PoC) and research and development(R&D) that I have written in my website. The main research topics are Auto-Encoders in relation to the representation learning, the statistical machine learning for energy-based models, adversarial generation net…
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - A processor for KyotoCorpus, KWDLC, and AnnotatedFKCCorpus
 * [nlplot](https://github.com/takapy0210/nlplot) - Visualization Module for Natural Language Processing
 * [rake-ja](https://github.com/kanjirz50/rake-ja) - Rapid Automatic Keyword Extraction algorithm for Japanese
 * [jel](https://github.com/izuna385/jel) - Japanese Entity Linker.
 * [MedNER-J](https://github.com/sociocom/MedNER-J) - Latest version of MedEX/J (Japanese disease name extractor)
 * [zunda-python](https://github.com/ikegami-yukino/zunda-python) - Zunda: Japanese Enhanced Modality Analyzer client for Python.
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
 * [showcase](https://github.com/cl-tohoku/showcase) - A PyTorch implementation of the Japanese Predicate-Argument Structure (PAS) analyser presented in the paper of Matsubayashi & Inui (2018) with some improvements.
 * [darts-clone-python](https://github.com/rixwew/darts-clone-python) - Darts-clone python binding
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - Example codes for the Japanese Realistic Textual Entailment Corpus.
 * [desuwa](https://github.com/megagonlabs/desuwa) - Feature annotator to morphemes and phrases based on KNP rule files (pure-Python)
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - Restaurant Search System through Dialogue in Japanese.
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - Samples codes for natural language processing in Japanese
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - Small example scripts for working with Japanese texts in Python
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - Japanese version of DNorm
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - EventGraph is a development platform for high-level NLP applications in Japanese.
 * [ishi](https://github.com/ku-nlp/ishi) - Ishi: A volition classifier for Japanese
 * [python-npylm](https://github.com/musyoku/python-npylm) - Unsupervised morphological analysis using a Bayesian hierarchical language model.
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - Semi-supervised morphological analysis through integration of conditional probability fields and Bayesian hierarchical language models.
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - Part-of-speech tagging without a teacher
 * [negima](https://github.com/cocodrips/negima) - Negima is a Python package to extract phrases in Japanese text by using the part-of-speeches based rules you defined.
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - Extractive summarizer using BertSum as summarization model
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - A parser for Japanese number (Kanji, arabic) in the natural language.
 * [kantan](https://github.com/itayperl/kantan) - Lookup japanese words by radical patterns
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - Obtain a corpus of Japanese dialogue.
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - A summarizer for Japanese articles.
 * [chirptext](https://github.com/letuananh/chirptext) - ChirpText is a collection of text processing tools for Python.
 * [yubin](https://github.com/alvations/yubin) - 日本の住所マンガー
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - Japanese Wikipedia Cleaner
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - A python library to convert Japanese to phoneme.
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - This repository contains codes related to the experiments in "An Experimental Evaluation of Japanese Tokenizers for Sentiment-Based Text Classification"
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - About
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - Generates plain or tokenized text files from the Aozora Bunko
 * [JLM](https://github.com/jiali-ms/JLM) - A fast LSTM Language Model for large vocabulary language like Japanese and Chinese
 * [NTM](https://github.com/m3yrin/NTM) - Testing of Neural Topic Modeling for Japanese articles
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - This is a English-Japanese lexicon for Machine Learning and Deep Learning terminology.
 * [text-generation](https://github.com/discus0434/text-generation) - Easy-to-use scripts to fine-tune GPT-2-JA with your own texts, to generate sentences, and to tweet them automatically.
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - Neural Image Caption (NIC) on chainer, its pretrained models on English and Japanese image caption datasets.
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - The official repository for "UnihanLM: Coarse-to-Fine Chinese-Japanese Language Model Pretraining with the Unihan Database", AACL-IJCNLP 2020
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - Code to perform finetuning of the mBART model.
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - Model xvector on jtubespeech.
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - A tool for creating a custom learning model for TinySegmenter.
 * [Grongish](https://github.com/shogo82148/Grongish) - Script for mutual conversion between Japanese and Gurongi language.
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - A script that enables morphological analysis-like display of Japanese sentences in WordCloud without using Mecab (a morphological analysis engine).
 * [snark](https://github.com/hiraokusky/snark) - DB access library using Japanese WordNet
 * [toEmoji](https://github.com/mkan0141/toEmoji) - Something that converts Japanese sentences into sentences made up of only emojis.
 * [termextract](https://github.com/kanjirz50/termextract) - Practice implementing a specialized terminology extraction algorithm.
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - Scoring is performed using an N-gram language model by KenLM on response candidates from Japanese-Dialog-Transformer, followed by filtering or re-ranking.
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - Mixture of Unigram Model and Infinite Mixture of Unigram Model in Python. (混合ユニグラムモデルと無限混合ユニグラムモデル)
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - 隠れマルコフモデル (Hidden Markov Model, HMM) and 無限隠れマルコフモデル (Infinite Hidden Markov Model, iHMM) in Python.
 * [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) - Ngram language model in Python. (Nグラム言語モデル)
 * [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) - Automatic Speech Recognition with deepspeech2 model in pytorch with support from Zakuro AI.
 * [neural_ime](https://github.com/yohokuno/neural_ime) - Neural IME: Neural Input Method Engine
 * [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) - Can neural networks transliterate Romaji into Japanese correctly?
 * [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) - tokenizer specified for Japanese
 * [AugLy-jp](https://github.com/chck/AugLy-jp) - Data Augmentation for Japanese Text on AugLy
 * [furigana4epub](https://github.com/Mumumu4/furigana4epub) - A Python script for adding furigana to Japanese epub books using Mecab and Unidic.
 * [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) - Japanese verb/adjective inflections tool
 * [jageocoder](https://github.com/t-sagara/jageocoder) - Pure Python Japanese address geocoder
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp, A python module for geotagging Japanese texts.
 * [nksnd](https://github.com/yoriyuki/nksnd) - 新しい仮名漢字変換エンジン
 * [JaMIE](https://github.com/racerandom/JaMIE) - A Japanese Medical Information Extraction Toolkit
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - This is a comparison between fasttext and word2vec, as well as execution and learning scripts.
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - Smallest search engine/PageRank/tf-idf
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - Scraping past logs from 5ch and conducting tracking investigations on words that were popular in the past (e.g. kagutsushi, orz).
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - Tweet downloader for Japanese sentiment analysis dataset on Twitter.
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - Aggregating Japanese words based on Juman++ and ConceptNet5.5
 * [jinf](https://github.com/hkiyomaru/jinf) - A Japanese inflection converter
 * [kwja](https://github.com/ku-nlp/kwja) - A unified language analyzer for Japanese
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - Reproduced package based on Masked Language Model Scoring (ACL2020).
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - [PyTorch] ClipCap for Japanese
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - [PyTorch] Show, Attend and Tell for Japanese
 * [cihai](https://github.com/cihai/cihai) - Python library for CJK (Chinese, Japanese, and Korean) language dictionary
 * [marine](https://github.com/6gsn/marine) - MARINE : Multi-task leaRnIng-based JapaNese accent Estimation
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - Fine-tuning the Whisper ASR model.
 * [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) - A PyTorch Implementation of japanese chatbot using BERT and Transformer's decoder
 * [radicalchar](https://github.com/yamamaya/radicalchar) - Radical character normalization library
 * [akaza](https://github.com/tokuhirom/akaza) - Yet another Japanese IME for IBus/Linux
 * [posuto](https://github.com/polm/posuto) - 日本の郵便番号データ。
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - Tacotron2 implementation of Japanese
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - Hiragana IME for IBus
 * [furiganapad](https://github.com/esrille/furiganapad) - Furigana pad
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - Japanese synonym library
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - Mecab + NEologd + Docker + Python3
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - Japanese Embedding Evaluation
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPT will become a YouTuber.
 * [shuwa](https://github.com/google/shuwa) - Extend GNOME On-Screen Keyboard for Input Methods
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - This repository provides the code for Japanese NLI model, a fine-tuned masked language model.
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - A tool for Japanese-English translation and English-Japanese translation by using FuguMT
 * [fugumt](https://github.com/s-taka/fugumt) - This is a translation environment that uses a machine translation engine released on the Blue Forest Concept website. It is capable of translating input text strings and PDF files through a form.
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - JaSPICE: Automatic Evaluation Metric Using Predicate-Argument Structures for Image Captioning Models
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - Japanese localization
 * [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) - Python wrapper for OpenJTalk
 * [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) - Make learning Japanese easier by adding readings for every kanji in the eBook
 * [N46Whisper](https://github.com/Ayanaminn/N46Whisper) - Whisper based Japanese subtitle generator
 * [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) - This is a simple web interface for Japanese compatible LLM (Large Language Model) such as Rinna-3.6B and OpenCALM.
 * [pdf-translator](https://github.com/discus0434/pdf-translator) - pdf-translator translates English PDF files into Japanese, preserving the original layout.
 * [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) - Haystack + Elasticsearch + wikipedia(ja) を用いた、日本語の質問応答システムのサンプル
 * [mozc-devices](https://github.com/google/mozc-devices) - Automatically exported from code.google.com/p/mozc-morse
 * [natsume](https://github.com/faruzan0820/natsume) - A Japanese text frontend processing toolkit
 * [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) - 日本語TTS（VITS）の学習と音声合成のGradio WebUI
 * [ja-law-parser](https://github.com/takuyaa/ja-law-parser) - A Japanese law parser
 * [dictation-kit](https://github.com/julius-speech/dictation-kit) - 日本語の音声認識キットを使用しているジュリウス
 * [julius4seg](https://github.com/Hiroshiba/julius4seg) - Segmentation support tool using Julius
 * [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) - VOICEVOX is a high-quality text-to-speech software that can be used for free.
 * [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) - LLaVA-JP is a Japanese VLM trained by LLaVA method
 * [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) - Open source RAG with Llama Index for Japanese LLM in low resource settting
 * [bertjsc](https://github.com/er-ri/bertjsc) - Japanese Spelling Error Corrector using BERT(Masked-Language Model). BERTに基づいて日本語校正
 * [llm-leaderboard](https://github.com/wandb/llm-leaderboard) - Project of llm evaluation to Japanese tasks
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - About Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - Modifying LAVIS' BLIP2 Q-former with models pretrained on Japanese datasets.
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - wikipedia 日本語の文を、各種日本語の embeddings や faiss index へと変換するスクリプト等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - Exploring Japanese SimCSE
 * [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) - Sample RAG based on Gradio to answer user questions using Japanese Wikipedia articles
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - Script for automatically evaluating language model responses using GPT-4.
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - Japanese T5 model
 * [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) - A repo for evaluating Japanese LLMs　・　日本語LLMを評価するレポ
 * [jmteb](https://github.com/sbintuitions/jmteb) - The evaluation scripts of JMTEB (Japanese Massive Text Embedding Benchmark)
 * [pydomino](https://github.com/dwangomediavillage/pydomino) - This is a tool for aligning phoneme labels with Japanese language audio.
 * [easynovelassistant](https://github.com/zuntan03/easynovelassistant) - This is a simple novel generation assistant using the lightweight and unregulated Japanese local LLM "LightChatAssistant-TypeB". It generates forever with local privileges, stacking up hit gachas. It also supports reading aloud.
 * [clip-japanese](https://github.com/sonoisa/clip-japanese) - Japanese CLIP model
 * [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) - Japanese rōmaji input schema for Rime IME
 * [deep-question-generation](https://github.com/sonoisa/deep-question-generation) - Quiz automatic generation using deep learning (Japanese T5 model)
 * [magpie-nemotron](https://github.com/aratako/magpie-nemotron) - Code to create a synthetic dialogue dataset using the technique called Magpie and Nemotron-4-340B-Instruct.
 * [qlora_ja](https://github.com/sosuke115/qlora_ja) - Sample code for qlora instruction tuning learning in a Japanese dataset.
 * [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) - Mozc UT Jawiki Dictionary is a dictionary generated from the Japanese Wikipedia for Mozc.
 * [shisa-v2](https://github.com/shisa-ai/shisa-v2) - Japanese / English Bilingual LLM
 * [llm-translator](https://github.com/hpprc/llm-translator) - Mixtral-based Ja-En (En-Ja) Translation model
 * [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) - Code for training a speech recognition model using a Whisper decoder replaced with llm-jp-1.3b-v1.0.
 * [rag-japanese](https://github.com/akimfromparis/rag-japanese) - Open source RAG with Llama Index for Japanese LLM in low resource settting
 * [monaka](https://github.com/komiya-lab/monaka) - A Japanese Parser (including historical Japanese)
 * [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) - A state-of-the-art open-source Japanese <--> English machine translation system based on the latest NMT research.
 * [substring-word-finder](https://github.com/toufu-24/substring-word-finder) - Perform word judgment on consecutive substring.
 * [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) - This project is a benchmarking tool for evaluating and comparing the performance of various Vision Language Models (VLMs). It uses two datasets: LLaVA-Bench-In-the-Wild and Japanese HERON Bench to measure model performance.
 * [text2dataset](https://github.com/llm-jp/text2dataset) - Easily turn large English text datasets into Japanese text datasets using open LLMs.
 * [mecab-web-api](https://github.com/bungoume/mecab-web-api) - Japanese Morphological Analysis Web API using MeCab
 * [mecab_controller](https://github.com/ajatt-tools/mecab_controller) - Mecab wrapper to generate furigana readings.
 * [vits](https://github.com/zassou65535/vits) - Text-to-speech engine and voice changer by VITS
 * [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) - Chatbot application that uses speech recognition, text generation, and speech synthesis for dialogue.
 * [kudasai](https://github.com/bikatr7/kudasai) - Streamlining Japanese-English Translation with Advanced Preprocessing and Integrated Translation Technologies
 * [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) - Tool to visualize the morphological analysis results of MeCab
 * [add-dictionary](https://github.com/massao000/add-dictionary) - An app to add user dictionaries for OpenJTalk using a GUI.
 * [j-moshi](https://github.com/nu-dialogue/j-moshi) - J-Moshi: A Japanese Full-duplex Spoken Dialogue System
 * [jatts](https://github.com/unilight/jatts) - JATTS: Japanese TTS (for research)
 * [tsukasa-speech](https://github.com/respaired/tsukasa-speech) - a Frontier Japanese Speech Generation net
 * [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) - I tried a semantic structure search that absorbs patient expression variations using Elasticsearch, GiNZA, and a patient expression dictionary.
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - Python tool for generating automatic evaluations
 * [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) - Sample trying out Asagi (large-scale Japanese VLM utilizing synthetic datasets) on Colaboratory.
 * [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) - This tool automatically evaluates Japanese multi-modal large language models across multiple datasets.
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - Python tool for generating automatic evaluations
 * [manga109api](https://github.com/manga109/manga109api) - Simple python API to read annotation data of Manga109
 * [fastrtc-jp](https://github.com/route250/fastrtc-jp) - Japanese TTS and STT add-on kit for fastrtc
 * [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) - Speech-to-text tool using Whisper model with Python
 * [pocket-researcher](https://github.com/u-masao/pocket-researcher) - Autonomous investigation agent utilizing LLM. Easily collect information and grasp an overview.
 * [jtransbench](https://github.com/webbigdata-jp/jtransbench) - A tool to easily benchmark Japanese translation skills
 * [easyllasa](https://github.com/zuntan03/easyllasa) - EasyLlasa is a TSTS (TextSpeechToSpeech) that generates Japanese speech from Japanese text and Japanese voice of 5-15 seconds.
 * [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) - Name Kanji Kana Matching Model
 * [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) - Automatically discover and analyze OpenReview papers with Japanese-compatible AI agents.
 * [pitchbench](https://github.com/shewiiii/pitchbench) - Experimental Japanese pitch accent based LLM Benchmark
 * [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) - English to Japanese Transformer from scratch
 * [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) - Inference code of the deep learning model used in the core of VOICEVOX
 * [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) - pyopenjtalk-plus: A Python wrapper for OpenJTalk with additional improvements
 * [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) - Japanese Spelling Correction
 * [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) - Python kaomoji
 * [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) - This repository contains the code for training llm-jp/llm-jp-3-vila-14b, modified from VILA repository.
 * [kanjivg-radical](https://github.com/yagays/kanjivg-radical) - KanjiVG Radical
 * [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) - This project visualizes the Japanese Wordnet (日本語ワードネット) with web application built by Django
 * [piper-plus](https://github.com/ayutaz/piper-plus) - Enhanced Piper TTS with Japanese support, WebAssembly, multi-GPU training, and quality improvements.
 * [Japanera](https://github.com/nagataaaas/Japanera) - Easy Tools for Japanese Era System
 * [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) - Japanese Sentence Summarization with BERT
 * [kyujipy](https://github.com/drturnon/kyujipy) - A Python library to convert Japanese texts from Shinjitai (新字体) to Kyujitai (舊字體) and vice versa
 * [jitenbot](https://github.com/konstantindjairo/jitenbot) - Web crawler for creating personal copies of Japanese dictionaries
 * [ja-icd10](https://github.com/yagays/ja-icd10) - Python package for handling Japanese information of ICD-10 international disease classification
 * [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) - VITS2 using Phoneme-Level Japanese BERT
 * [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) - Machine learning model of NDCPredictor (pre-trained model of fastText that predicts Japanese Decimal Classification from bibliographic information)
 * [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) - pfmt-bench-fin-ja: Preferred Multi-turn Benchmark for Finance in Japanese
 * [marine-plus](https://github.com/tsukumijima/marine-plus) - MARINE : Multi-task leaRnIng-based JapaNese accent Estimation (Also supported Windows)
 * [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) - Compare the speed of various Japanese tokenizers in Python.
 * [yat](https://github.com/yagays/yat) - yat: Yet Another Tokenizer for Japanese NLP
 * [igakuqa119](https://github.com/docto-rin/igakuqa119) - Evaluating LLMs on the 119th Japanese Medical Licensing Examination
 * [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) - Japanese Long-Unit-Word Tokenizer with RemBertTokenizerFast of Transformers
 * [ibus-jig](https://github.com/y-koj/ibus-jig) - ibus-jig: Japanese-language Input-method using GPT-4
 * [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) - A lightweight Python library designed to filter stopwords from Japanese text based on customizable rules.
 * [yasumail](https://github.com/terallite/yasumail) - Synthetic Japanese business email generator for ML training data
 * [himotoki](https://github.com/msr2903/himotoki) - A Python-based Japanese Tokenizer, Dictionary, Morphological Analyzer and Romanization Tool. Based on JMDict for Language Learning.
 * [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) - A toolkit for synthesizing filler-rich, short-utterance Japanese dialogue scripts for speech-based interaction using Large Language Models (LLMs) This project is designed to generate data in two phases: Seed Generation (metadata creation) and Dialogue Generation (script creation).
 * [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) - Evaluating Multimodal Large Language Models on Vertically Written Japanese Text
 * [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) - This code is for filtering "sensitive personal information" that requires special consideration, from the training corpus of a large-scale language model (LLM).
 * [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) - Evaluating Multimodal Large Language Models on Vertically Written Japanese Text
 * [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) - Method for constructing a casual conversation corpus from novel texts


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namedivider-python](https://github.com/rskmoi/namedivider-python) | 📥 413 | 📦 81k | ⭐ 251 | 🟡 november 2025|
| 🔗 [asa-python](https://github.com/ikegami-yukino/asa-python) | 📥 45 | 📦 31k | ⭐ 11 | 🔴 february 2019|
| 🔗 [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) | - | - | ⭐ 22 | 🔴 january 2020|
| 🔗 [toiro](https://github.com/taishi-i/toiro) | 📥 61 | 📦 26k | ⭐ 121 | 🟡 november 2025|
| 🔗 [ja-timex](https://github.com/yagays/ja-timex) | 📥 475 | 📦 91k | ⭐ 140 | 🔴 november 2023|
| 🔗 [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) | - | - | ⭐ 137 | 🔴 march 2019|
| 🔗 [daaja](https://github.com/kajyuuen/daaja) | 📥 38 | 📦 25k | ⭐ 64 | 🔴 february 2023|
| 🔗 [accel-brain-code](https://github.com/accel-brain/accel-brain-code) | 📥 160 | 📦 149k | ⭐ 323 | 🔴 december 2023|
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 337 | 🔴 march 2025|
| 🔗 [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) | 📥 362 | 📦 52k | ⭐ 10 | 🔴 june 2024|
| 🔗 [nlplot](https://github.com/takapy0210/nlplot) | 📥 106 | 📦 109k | ⭐ 238 | 🔴 september 2022|
| 🔗 [rake-ja](https://github.com/kanjirz50/rake-ja) | - | - | ⭐ 21 | 🔴 october 2018|
| 🔗 [jel](https://github.com/izuna385/jel) | 📥 18 | 📦 8k | ⭐ 11 | 🔴 july 2021|
| 🔗 [MedNER-J](https://github.com/sociocom/MedNER-J) | - | - | ⭐ 18 | 🔴 may 2022|
| 🔗 [zunda-python](https://github.com/ikegami-yukino/zunda-python) | 📥 10 | 📦 6k | ⭐ 10 | 🔴 november 2019|
| 🔗 [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [showcase](https://github.com/cl-tohoku/showcase) | 📥 10 | 📦 7k | ⭐ 6 | 🔴 june 2018|
| 🔗 [darts-clone-python](https://github.com/rixwew/darts-clone-python) | 📥 3k | 📦 9M | ⭐ 20 | 🔴 april 2022|
| 🔗 [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [desuwa](https://github.com/megagonlabs/desuwa) | 📥 24 | 📦 10k | ⭐ 6 | 🔴 may 2022|
| 🔗 [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) | - | - | ⭐ 277 | 🔴 may 2016|
| 🔗 [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) | - | - | ⭐ 66 | 🔴 april 2021|
| 🔗 [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) | - | - | ⭐ 26 | 🔴 june 2019|
| 🔗 [DNorm-J](https://github.com/sociocom/DNorm-J) | - | - | ⭐ 9 | 🔴 june 2022|
| 🔗 [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) | 📥 29 | 📦 65k | ⭐ 9 | 🔴 september 2022|
| 🔗 [ishi](https://github.com/ku-nlp/ishi) | 📥 13 | 📦 6k | ⭐ 2 | 🔴 may 2020|
| 🔗 [python-npylm](https://github.com/musyoku/python-npylm) | - | - | ⭐ 34 | 🔴 january 2019|
| 🔗 [python-npycrf](https://github.com/musyoku/python-npycrf) | - | - | ⭐ 11 | 🔴 march 2018|
| 🔗 [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) | - | - | ⭐ 16 | 🔴 october 2017|
| 🔗 [negima](https://github.com/cocodrips/negima) | 📥 22 | 📦 16k | ⭐ 14 | 🔴 august 2018|
| 🔗 [YouyakuMan](https://github.com/neilctwu/YouyakuMan) | - | - | ⭐ 52 | 🔴 september 2020|
| 🔗 [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) | 📥 639 | 📦 2M | ⭐ 21 | 🔴 april 2020|
| 🔗 [kantan](https://github.com/itayperl/kantan) | - | - | ⭐ 8 | 🔴 october 2024|
| 🔗 [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) | - | - | ⭐ 40 | 🔴 september 2017|
| 🔗 [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) | - | - | ⭐ 10 | 🔴 august 2022|
| 🔗 [chirptext](https://github.com/letuananh/chirptext) | 📥 2k | 📦 200k | ⭐ 7 | 🔴 october 2022|
| 🔗 [yubin](https://github.com/alvations/yubin) | 📥 5 | 📦 3k | ⭐ 3 | 🔴 october 2019|
| 🔗 [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) | 📥 52 | 📦 24k | ⭐ 6 | 🔴 february 2021|
| 🔗 [japanese2phoneme](https://github.com/iory/japanese2phoneme) | 📥 18 | 📦 4k | ⭐ 1 | 🔴 february 2022|
| 🔗 [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) | - | - | ⭐ 1 | 🔴 march 2022|
| 🔗 [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) | - | - | ⭐ 11 | 🔴 september 2017|
| 🔗 [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) | - | - | ⭐ 8 | 🟡 june 2025|
| 🔗 [JLM](https://github.com/jiali-ms/JLM) | - | - | ⭐ 111 | 🔴 june 2019|
| 🔗 [NTM](https://github.com/m3yrin/NTM) | - | - | ⭐ 13 | 🔴 july 2019|
| 🔗 [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) | - | - | ⭐ 40 | 🔴 march 2021|
| 🔗 [text-generation](https://github.com/discus0434/text-generation) | - | - | ⭐ 19 | 🟡 august 2025|
| 🔗 [chainer_nic](https://github.com/yuyay/chainer_nic) | - | - | ⭐ 17 | 🔴 december 2018|
| 🔗 [unihan-lm](https://github.com/JetRunner/unihan-lm) | - | - | ⭐ 2 | 🔴 november 2020|
| 🔗 [mbart-finetuning](https://github.com/ken11/mbart-finetuning) | - | - | ⭐ 3 | 🔴 october 2021|
| 🔗 [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) | - | - | ⭐ 47 | 🔴 november 2023|
| 🔗 [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) | - | - | ⭐ 72 | 🔴 september 2022|
| 🔗 [Grongish](https://github.com/shogo82148/Grongish) | - | - | ⭐ 25 | 🟡 december 2025|
| 🔗 [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) | - | - | ⭐ 9 | 🔴 january 2020|
| 🔗 [snark](https://github.com/hiraokusky/snark) | - | - | ⭐ 11 | 🔴 march 2020|
| 🔗 [toEmoji](https://github.com/mkan0141/toEmoji) | - | - | ⭐ 4 | 🔴 april 2018|
| 🔗 [termextract](https://github.com/kanjirz50/termextract) | - | - | ⭐ 18 | 🔴 september 2018|
| 🔗 [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) | - | - | ⭐ 1 | 🔴 july 2022|
| 🔗 [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) | - | - | ⭐ 6 | 🔴 june 2017|
| 🔗 [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) | - | - | ⭐ 5 | 🔴 june 2017|
| 🔗 [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) | - | - | ⭐ 5 | 🔴 december 2017|
| 🔗 [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) | - | - | ⭐ 69 | 🔴 september 2022|
| 🔗 [neural_ime](https://github.com/yohokuno/neural_ime) | - | - | ⭐ 67 | 🔴 december 2016|
| 🔗 [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) | - | - | ⭐ 178 | 🔴 september 2017|
| 🔗 [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) | 📥 141k | 📦 172k | ⭐ repo not found | 🔴 november 2015|
| 🔗 [AugLy-jp](https://github.com/chck/AugLy-jp) | 📥 56 | 📦 30k | ⭐ 7 | 🔴 september 2021|
| 🔗 [furigana4epub](https://github.com/Mumumu4/furigana4epub) | 📥 27 | 📦 12k | ⭐ 29 | 🔴 september 2021|
| 🔗 [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) | 📥 70 | 📦 20k | ⭐ 12 | 🔴 march 2025|
| 🔗 [jageocoder](https://github.com/t-sagara/jageocoder) | 📥 3k | 📦 339k | ⭐ 95 | 🟡 september 2025|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 82 | 📦 21k | ⭐ 22 | 🟡 october 2025|
| 🔗 [nksnd](https://github.com/yoriyuki/nksnd) | - | - | ⭐ 26 | 🔴 may 2018|
| 🔗 [JaMIE](https://github.com/racerandom/JaMIE) | - | - | ⭐ 9 | 🟢 march|
| 🔗 [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) | - | - | ⭐ 48 | 🔴 august 2017|
| 🔗 [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) | - | - | ⭐ 19 | 🔴 july 2019|
| 🔗 [5ch-analysis](https://github.com/GINK03/5ch-analysis) | - | - | ⭐ 75 | 🔴 november 2018|
| 🔗 [tweet_extructor](https://github.com/tatHi/tweet_extructor) | - | - | ⭐ 3 | 🔴 august 2022|
| 🔗 [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) | - | - | ⭐ 2 | 🔴 august 2018|
| 🔗 [jinf](https://github.com/hkiyomaru/jinf) | 📥 325 | 📦 55k | ⭐ 4 | 🔴 december 2022|
| 🔗 [kwja](https://github.com/ku-nlp/kwja) | 📥 275 | 📦 56k | ⭐ 139 | 🟡 august 2025|
| 🔗 [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) | - | - | ⭐ 6 | 🔴 december 2022|
| 🔗 [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) | - | - | ⭐ 12 | 🔴 october 2022|
| 🔗 [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) | - | - | ⭐ 2 | 🔴 october 2022|
| 🔗 [cihai](https://github.com/cihai/cihai) | 📥 360 | 📦 212k | ⭐ 93 | 🟢 yesterday|
| 🔗 [marine](https://github.com/6gsn/marine) | 📥 39 | 📦 15k | ⭐ 36 | 🔴 september 2022|
| 🔗 [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) | - | - | ⭐ 32 | 🔴 december 2022|
| 🔗 [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [radicalchar](https://github.com/yamamaya/radicalchar) | - | - | ⭐ 9 | 🔴 december 2022|
| 🔗 [akaza](https://github.com/tokuhirom/akaza) | - | - | ⭐ 247 | 🟢 today|
| 🔗 [posuto](https://github.com/polm/posuto) | 📥 5k | 📦 684k | ⭐ 226 | 🟢 march|
| 🔗 [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) | - | - | ⭐ 269 | 🔴 september 2022|
| 🔗 [ibus-hiragana](https://github.com/esrille/ibus-hiragana) | - | - | ⭐ 78 | 🟢 today|
| 🔗 [furiganapad](https://github.com/esrille/furiganapad) | - | - | ⭐ 19 | 🟡 april 2025|
| 🔗 [chikkarpy](https://github.com/WorksApplications/chikkarpy) | 📥 265 | 📦 59k | ⭐ 55 | 🔴 february 2022|
| 🔗 [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) | - | - | ⭐ 36 | 🔴 may 2022|
| 🔗 [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) | - | - | ⭐ 184 | 🔴 october 2024|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [shuwa](https://github.com/google/shuwa) | - | - | ⭐ 145 | 🔴 december 2022|
| 🔗 [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) | - | - | ⭐ 6 | 🔴 october 2022|
| 🔗 [tra-fugu](https://github.com/tos-kamiya/tra-fugu) | - | - | ⭐ 6 | 🔴 march 2023|
| 🔗 [fugumt](https://github.com/s-taka/fugumt) | - | - | ⭐ 64 | 🔴 february 2021|
| 🔗 [JaSPICE](https://github.com/keio-smilab23/JaSPICE) | 📥 6 | 📦 2k | ⭐ 9 | 🔴 november 2023|
| 🔗 [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) | - | - | ⭐ 48 | 🔴 april 2023|
| 🔗 [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) | 📥 17k | 📦 1M | ⭐ 245 | 🟡 april 2025|
| 🔗 [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) | 📥 35 | 📦 7k | ⭐ 26 | 🔴 february 2024|
| 🔗 [N46Whisper](https://github.com/Ayanaminn/N46Whisper) | - | - | ⭐ 1.7k | 🔴 february 2025|
| 🔗 [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) | - | - | ⭐ 17 | 🔴 may 2024|
| 🔗 [pdf-translator](https://github.com/discus0434/pdf-translator) | - | - | ⭐ 338 | 🔴 may 2024|
| 🔗 [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) | - | - | ⭐ 1 | 🔴 december 2022|
| 🔗 [mozc-devices](https://github.com/google/mozc-devices) | - | - | ⭐ 2.7k | 🟡 november 2025|
| 🔗 [natsume](https://github.com/faruzan0820/natsume) | 📥 0 | 📦 3k | ⭐ repo not found | 🔴 repo not found|
| 🔗 [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) | - | - | ⭐ 42 | 🔴 january 2024|
| 🔗 [ja-law-parser](https://github.com/takuyaa/ja-law-parser) | - | - | ⭐ 25 | 🔴 january 2024|
| 🔗 [dictation-kit](https://github.com/julius-speech/dictation-kit) | - | - | ⭐ 164 | 🔴 april 2019|
| 🔗 [julius4seg](https://github.com/Hiroshiba/julius4seg) | - | - | ⭐ 7 | 🔴 august 2021|
| 🔗 [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) | - | - | ⭐ 1.6k | 🟢 march|
| 🔗 [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) | - | - | ⭐ 64 | 🔴 june 2024|
| 🔗 [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [bertjsc](https://github.com/er-ri/bertjsc) | - | - | ⭐ 14 | 🔴 august 2024|
| 🔗 [llm-leaderboard](https://github.com/wandb/llm-leaderboard) | - | - | ⭐ 92 | 🟡 september 2025|
| 🔗 [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) | - | - | ⭐ 18 | 🟢 march|
| 🔗 [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) | - | - | ⭐ 11 | 🔴 march 2024|
| 🔗 [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) | - | - | ⭐ 69 | 🔴 october 2023|
| 🔗 [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) | - | - | ⭐ 16 | 🔴 june 2024|
| 🔗 [t5-japanese](https://github.com/sonoisa/t5-japanese) | - | - | ⭐ 118 | 🟡 september 2025|
| 🔗 [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) | - | - | ⭐ 5 | 🔴 april 2024|
| 🔗 [jmteb](https://github.com/sbintuitions/jmteb) | - | - | ⭐ 87 | 🟢 last monday|
| 🔗 [pydomino](https://github.com/dwangomediavillage/pydomino) | - | - | ⭐ 37 | 🟡 august 2025|
| 🔗 [easynovelassistant](https://github.com/zuntan03/easynovelassistant) | - | - | ⭐ 220 | 🔴 july 2024|
| 🔗 [clip-japanese](https://github.com/sonoisa/clip-japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) | - | - | ⭐ 48 | 🟢 last thursday|
| 🔗 [deep-question-generation](https://github.com/sonoisa/deep-question-generation) | - | - | ⭐ 12 | 🔴 march 2023|
| 🔗 [magpie-nemotron](https://github.com/aratako/magpie-nemotron) | - | - | ⭐ 9 | 🔴 july 2024|
| 🔗 [qlora_ja](https://github.com/sosuke115/qlora_ja) | - | - | ⭐ 1 | 🔴 july 2024|
| 🔗 [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) | - | - | ⭐ 28 | 🟢 march|
| 🔗 [shisa-v2](https://github.com/shisa-ai/shisa-v2) | - | - | ⭐ 28 | 🟡 december 2025|
| 🔗 [llm-translator](https://github.com/hpprc/llm-translator) | - | - | ⭐ 20 | 🔴 january 2025|
| 🔗 [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) | - | - | ⭐ 9 | 🔴 september 2024|
| 🔗 [rag-japanese](https://github.com/akimfromparis/rag-japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [monaka](https://github.com/komiya-lab/monaka) | - | - | ⭐ 4 | 🔴 january 2025|
| 🔗 [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) | - | - | ⭐ 3 | 🔴 september 2024|
| 🔗 [substring-word-finder](https://github.com/toufu-24/substring-word-finder) | - | - | ⭐ 4 | 🟡 november 2025|
| 🔗 [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) | - | - | ⭐ 6 | 🔴 december 2024|
| 🔗 [text2dataset](https://github.com/llm-jp/text2dataset) | - | - | ⭐ 27 | 🔴 january 2025|
| 🔗 [mecab-web-api](https://github.com/bungoume/mecab-web-api) | - | - | ⭐ 40 | 🔴 july 2022|
| 🔗 [mecab_controller](https://github.com/ajatt-tools/mecab_controller) | - | - | ⭐ 19 | 🟢 january|
| 🔗 [vits](https://github.com/zassou65535/vits) | - | - | ⭐ 92 | 🔴 february 2023|
| 🔗 [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) | - | - | ⭐ 48 | 🟡 october 2025|
| 🔗 [kudasai](https://github.com/bikatr7/kudasai) | - | - | ⭐ 26 | 🟡 june 2025|
| 🔗 [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) | - | - | ⭐ 2 | 🔴 september 2023|
| 🔗 [add-dictionary](https://github.com/massao000/add-dictionary) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [j-moshi](https://github.com/nu-dialogue/j-moshi) | - | - | ⭐ 302 | 🟡 june 2025|
| 🔗 [jatts](https://github.com/unilight/jatts) | - | - | ⭐ 44 | 🟢 march|
| 🔗 [tsukasa-speech](https://github.com/respaired/tsukasa-speech) | - | - | ⭐ 63 | 🟡 may 2025|
| 🔗 [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) | - | - | ⭐ 2 | 🔴 february 2021|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 39 | 🟡 december 2025|
| 🔗 [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) | - | - | ⭐ 1 | 🔴 march 2025|
| 🔗 [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) | - | - | ⭐ 41 | 🟢 january|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 39 | 🟡 december 2025|
| 🔗 [manga109api](https://github.com/manga109/manga109api) | 📥 163 | 📦 46k | ⭐ 129 | 🔴 march 2022|
| 🔗 [fastrtc-jp](https://github.com/route250/fastrtc-jp) | - | - | ⭐ 5 | 🟡 may 2025|
| 🔗 [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) | - | - | ⭐ 17 | 🟢 january|
| 🔗 [pocket-researcher](https://github.com/u-masao/pocket-researcher) | - | - | ⭐ 10 | 🟡 april 2025|
| 🔗 [jtransbench](https://github.com/webbigdata-jp/jtransbench) | - | - | ⭐ 13 | 🟡 october 2025|
| 🔗 [easyllasa](https://github.com/zuntan03/easyllasa) | - | - | ⭐ 25 | 🟡 september 2025|
| 🔗 [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) | - | - | ⭐ 114 | 🟡 december 2025|
| 🔗 [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) | - | - | ⭐ 13 | 🟡 november 2025|
| 🔗 [pitchbench](https://github.com/shewiiii/pitchbench) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) | - | - | ⭐ 31 | 🟡 december 2025|
| 🔗 [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) | 📥 11k | 📦 422k | ⭐ 56 | 🟢 march|
| 🔗 [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) | 📥 18 | 📦 37k | ⭐ 6 | 🔴 december 2018|
| 🔗 [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) | - | - | ⭐ 10 | 🟡 august 2025|
| 🔗 [kanjivg-radical](https://github.com/yagays/kanjivg-radical) | - | - | ⭐ 106 | 🔴 august 2018|
| 🔗 [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) | - | - | ⭐ 3 | 🔴 november 2022|
| 🔗 [piper-plus](https://github.com/ayutaz/piper-plus) | - | - | ⭐ 85 | 🟢 today|
| 🔗 [Japanera](https://github.com/nagataaaas/Japanera) | 📥 3k | 📦 359k | ⭐ 35 | 🟡 june 2025|
| 🔗 [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) | - | - | ⭐ 49 | 🔴 december 2019|
| 🔗 [kyujipy](https://github.com/drturnon/kyujipy) | 📥 38 | 📦 23k | ⭐ 22 | 🟢 january|
| 🔗 [jitenbot](https://github.com/konstantindjairo/jitenbot) | - | - | ⭐ 4 | 🔴 december 2024|
| 🔗 [ja-icd10](https://github.com/yagays/ja-icd10) | - | - | ⭐ 5 | 🔴 july 2021|
| 🔗 [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) | - | - | ⭐ 14 | 🔴 december 2023|
| 🔗 [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) | - | - | ⭐ 11 | 🔴 august 2021|
| 🔗 [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) | - | - | ⭐ 9 | 🔴 march 2025|
| 🔗 [marine-plus](https://github.com/tsukumijima/marine-plus) | 📥 55 | 📦 12k | ⭐ 8 | 🟢 today|
| 🔗 [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) | - | - | ⭐ 7 | 🔴 february 2022|
| 🔗 [yat](https://github.com/yagays/yat) | - | - | ⭐ 7 | 🔴 june 2018|
| 🔗 [igakuqa119](https://github.com/docto-rin/igakuqa119) | - | - | ⭐ 8 | 🟢 january|
| 🔗 [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) | - | - | ⭐ 6 | 🔴 december 2021|
| 🔗 [ibus-jig](https://github.com/y-koj/ibus-jig) | - | - | ⭐ 4 | 🔴 december 2023|
| 🔗 [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) | 📥 27 | 📦 5k | ⭐ 4 | 🔴 november 2024|
| 🔗 [yasumail](https://github.com/terallite/yasumail) | - | - | ⭐ 2 | 🟢 january|
| 🔗 [himotoki](https://github.com/msr2903/himotoki) | 📥 85 | 📦 4k | ⭐ 3 | 🟢 february|
| 🔗 [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) | - | - | ⭐ 0 | 🟢 january|
| 🔗 [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) | - | - | ⭐ 7 | 🔴 march 2025|
| 🔗 [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) | - | - | ⭐ 0 | 🟢 february|


## C++

### Morphology analysis
High-performance libraries for Japanese morphological analysis

 * [mecab](https://github.com/taku910/mecab) - Yet another Japanese morphological analyzer
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++ (a Morphological Analyzer Toolkit)
 * [kytea](https://github.com/neubig/kytea) - The Kyoto Text Analysis Toolkit for word segmentation and pronunciation estimation, etc.
 * [juman](https://github.com/ku-nlp/juman) - Japanese Morphological Analysis System JUMAN


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab](https://github.com/taku910/mecab) | - | - | ⭐ 1.1k | 🔴 february 2025|
| 🔗 [jumanpp](https://github.com/ku-nlp/jumanpp) | - | - | ⭐ 409 | 🔴 march 2023|
| 🔗 [kytea](https://github.com/neubig/kytea) | - | - | ⭐ 212 | 🔴 april 2020|
| 🔗 [juman](https://github.com/ku-nlp/juman) | - | - | ⭐ 12 | 🔴 december 2021|

### Parsing
Libraries for dependency and syntactic parsing of Japanese sentences

 * [cabocha](https://github.com/taku910/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [knp](https://github.com/ku-nlp/knp) - A Japanese Parser


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [cabocha](https://github.com/taku910/cabocha) | - | - | ⭐ 121 | 🔴 february 2025|
| 🔗 [knp](https://github.com/ku-nlp/knp) | - | - | ⭐ 33 | 🔴 november 2023|

### Others
Other Japanese NLP and text processing libraries

 * [jsc](https://github.com/yohokuno/jsc) - Joint source channel model for Japanese Kana Kanji conversion, Chinese pinyin input and CJE mixed input.
 * [aquaskk](https://github.com/codefirst/aquaskk) - An input method without morphological analysis.
 * [mozc](https://github.com/google/mozc) - Mozc - a Japanese Input Method Editor designed for multi-platform
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch: An (Exact|Prefix|Approximate) String Matching Library
 * [resembla](https://github.com/tuem/resembla) - Resembla: Word-based Japanese similar sentence search library
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ SKK-like Japanese Input Method Editor for Windows
 * [mozuku](https://github.com/t3tra-dev/mozuku) - LSP server that performs analysis and proofreading of Japanese text.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jsc](https://github.com/yohokuno/jsc) | - | - | ⭐ 15 | 🔴 december 2012|
| 🔗 [aquaskk](https://github.com/codefirst/aquaskk) | - | - | ⭐ 368 | 🔴 july 2023|
| 🔗 [mozc](https://github.com/google/mozc) | - | - | ⭐ 2.9k | 🟢 last thursday|
| 🔗 [trimatch](https://github.com/tuem/trimatch) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [resembla](https://github.com/tuem/resembla) | - | - | ⭐ 73 | 🟡 august 2025|
| 🔗 [corvusskk](https://github.com/nathancorvussolis/corvusskk) | - | - | ⭐ 356 | 🟢 last friday|
| 🔗 [mozuku](https://github.com/t3tra-dev/mozuku) | - | - | ⭐ 412 | 🟢 last monday|


## Rust crate

### Morphology analysis
Fast Japanese morphological analysis crates written in Rust

 * [lindera](https://github.com/lindera-morphology/lindera) - A morphological analysis library.
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto: Very Accelerated POintwise pREdicTion based TOkenizer
 * [goya](https://github.com/Leko/goya) - Japanese Morphological Analysis written in Rust
 * [vibrato](https://github.com/daac-tools/vibrato) - vibrato: Viterbi-based accelerated tokenizer
 * [yoin](https://github.com/agatan/yoin) - A Japanese Morphological Analyzer written in pure Rust
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - Safe Rust bindings for mecab a part-of-speech and morphological analyzer library
 * [awabi](https://github.com/nakagami/awabi) - A morphological analyzer using mecab dictionary
 * [kanpyo](https://github.com/togatoga/kanpyo) - Japanese Morphological Analyzer written in Rust


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera](https://github.com/lindera-morphology/lindera) | - | 📦 966k | ⭐ 609 | 🟢 last thursday|
| 🔗 [vaporetto](https://github.com/daac-tools/vaporetto) | - | 📦 190k | ⭐ 254 | 🟢 february|
| 🔗 [goya](https://github.com/Leko/goya) | - | 📦 11k | ⭐ 83 | 🔴 december 2021|
| 🔗 [vibrato](https://github.com/daac-tools/vibrato) | - | 📦 58k | ⭐ 403 | 🟢 february|
| 🔗 [yoin](https://github.com/agatan/yoin) | - | 📦 3k | ⭐ 26 | 🔴 october 2017|
| 🔗 [mecab-rs](https://github.com/tsurai/mecab-rs) | - | 📦 39k | ⭐ 67 | 🔴 september 2023|
| 🔗 [awabi](https://github.com/nakagami/awabi) | - | 📦 24k | ⭐ 10 | 🟡 november 2025|
| 🔗 [kanpyo](https://github.com/togatoga/kanpyo) | - | 📦 2.5k | ⭐ 109 | 🟢 february|


### Converter
Crates for script and character conversion in Japanese text

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - Utility library for checking and converting between Japanese characters - Hiragana, Katakana - and Romaji
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - A Rust library to convert Japanese Half-width-kana[半角ｶﾅ] and Wide-alphanumeric[全角英数] into normal ones
 * [kana](https://github.com/gbrlsnchs/kana) - [Mirror] CLI program for transliterating romaji text to either hiragana or katakana
 * [kanaria](https://github.com/samunohito/kanaria) - This library provides functions such as mutual conversion and discrimination of hiragana, katakana, half-width, and full-width characters.
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - This is a library that splits Japanese addresses into prefecture/city or town/village/neighborhood/other.
 * [yosina](https://github.com/yosina-lib/yosina) - Yosina is a transliteration library deals with the letters and symbols used in Japanese writing.
 * [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) - Rust implementation of a fast converter between Japanese hankaku and zenkaku characters, mojimoji.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) | - | 📦 344k | ⭐ 90 | 🔴 march 2025|
| 🔗 [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) | - | 📦 63k | ⭐ 19 | 🔴 april 2020|
| 🔗 [kana](https://github.com/gbrlsnchs/kana) | - | - | ⭐ 12 | 🔴 january 2023|
| 🔗 [kanaria](https://github.com/samunohito/kanaria) | - | - | ⭐ 21 | 🟢 february|
| 🔗 [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) | - | - | ⭐ 10 | 🟡 november 2025|
| 🔗 [yosina](https://github.com/yosina-lib/yosina) | - | - | ⭐ 23 | 🟢 last thursday|
| 🔗 [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) | - | - | ⭐ 4 | 🔴 november 2022|


### Search engine library
Libraries for Japanese full-text search and indexing

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy.
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - A Tantivy tokenizer using Vibrato.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) | - | 📦 171k | ⭐ 68 | 🟢 january|
| 🔗 [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) | - | 📦 1.5k | ⭐ 3 | 🔴 january 2023|


### Others
Supplementary crates for Japanese text and IME processing

 * [daachorse](https://github.com/daac-tools/daachorse) - A fast implementation of the Aho-Corasick algorithm using the compact double-array data structure in Rust.
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - Finding all pairs of similar documents time- and memory-efficiently
 * [crawdad](https://github.com/daac-tools/crawdad) - Rust library of natural language dictionaries using character-wise double-array tries.
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) -  Comparison code of various tokenizers
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - Here provides benchmark tools to compare the performance of data structures for string matching.
 * [vime](https://github.com/algon-320/vime) - Using Vim as an input method for X11 apps
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - The core of VOICEVOX, a medium-quality text-to-speech software that can be used for free.
 * [akaza](https://github.com/akaza-im/akaza) - Yet another Japanese IME for IBus/Linux
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - A free online, self-hostable, multilang Japanese dictionary.
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - DvorakJP Roman Table for Google Japanese Input
 * [niinii](https://github.com/Netdex/niinii) -  Japanese glossator for assisted reading of text using Ichiran
 * [cskk](https://github.com/naokiri/cskk) - SKK (Simple Kana Kanji conversion) library
 * [japanki](https://github.com/tysonwu/japanki) - Learn Japanese vocabs 🇯🇵 by doing quizzes on CLI!
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - Japanese text preprocessor for Text-to-Speech applications (OpenJTalk rewrite in rust language)
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - Software that scrapes and generates a list of case law data from the court's website (https://www.courts.go.jp/index.html)
 * [jisho](https://github.com/eagleflo/jisho) - Jisho is a CLI tool & Rust library that provides a Japanese-English dictionary.
 * [kanalizer](https://github.com/voicevox/kanalizer) - Library that guesses readings from English words.
 * [koharu](https://github.com/mayocream/koharu) - Automated manga translation tool with LLM, written in Rust.
 * [yomine](https://github.com/mcgrizzz/yomine) - A Japanese vocabulary mining tool designed to help language learners mine new words and expressions.
 * [matsuba](https://github.com/mrpicklepinosaur/matsuba) - lightweight japanese ime written in rust
 * [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) - 日本語辞書 by Rust, support Telegram bot, AWS Lambda and Cloudflare Workers. Support LLM and search RAG.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [daachorse](https://github.com/daac-tools/daachorse) | - | 📦 718k | ⭐ 245 | 🟢 january|
| 🔗 [find-simdoc](https://github.com/legalforce-research/find-simdoc) | - | 📦 29k | ⭐ 62 | 🔴 march 2025|
| 🔗 [crawdad](https://github.com/daac-tools/crawdad) | - | 📦 63k | ⭐ 37 | 🔴 january 2025|
| 🔗 [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) | - | - | ⭐ 4 | 🔴 march 2023|
| 🔗 [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [vime](https://github.com/algon-320/vime) | - | - | ⭐ 230 | 🔴 november 2022|
| 🔗 [voicevox_core](https://github.com/VOICEVOX/voicevox_core) | - | - | ⭐ 1.1k | 🟢 last wednesday|
| 🔗 [akaza](https://github.com/akaza-im/akaza) | - | - | ⭐ 247 | 🟢 today|
| 🔗 [Jotoba](https://github.com/WeDontPanic/Jotoba) | - | - | ⭐ 199 | 🔴 january 2024|
| 🔗 [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) | - | - | ⭐ 55 | 🟢 february|
| 🔗 [niinii](https://github.com/Netdex/niinii) | - | - | ⭐ 15 | 🟢 february|
| 🔗 [cskk](https://github.com/naokiri/cskk) | - | - | ⭐ 80 | 🟢 march|
| 🔗 [japanki](https://github.com/tysonwu/japanki) | - | - | ⭐ 3 | 🔴 october 2023|
| 🔗 [jpreprocess](https://github.com/jpreprocess/jpreprocess) | - | - | ⭐ 52 | 🟢 february|
| 🔗 [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) | - | - | ⭐ 5 | 🔴 february 2025|
| 🔗 [jisho](https://github.com/eagleflo/jisho) | - | - | ⭐ 17 | 🟢 february|
| 🔗 [kanalizer](https://github.com/voicevox/kanalizer) | - | - | ⭐ 26 | 🟢 march|
| 🔗 [koharu](https://github.com/mayocream/koharu) | - | - | ⭐ 844 | 🟢 today|
| 🔗 [yomine](https://github.com/mcgrizzz/yomine) | - | - | ⭐ 50 | 🟢 february|
| 🔗 [matsuba](https://github.com/mrpicklepinosaur/matsuba) | - | - | ⭐ 18 | 🔴 march 2023|
| 🔗 [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) | - | - | ⭐ 70 | 🟢 last thursday|


## JavaScript

### Morphology analysis
Japanese morphological analysis libraries for browser and Node.js

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - JavaScript implementation of Japanese morphological analyzer
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) -  Rakuten MA - morphological analyzer (word segmentor + PoS Tagger) for Chinese and Japanese written purely in JavaScript.
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - Yet another mecab wrapper for nodejs
 * [juman-bin](https://github.com/thammin/juman-bin) - a User-Extensible Morphological Analyzer for Japanese. 日本語形態素解析システム
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - Asynchronous japanese morphological analyser using MeCab.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji.js](https://github.com/takuyaa/kuromoji.js) | 📥 77k/week | 📦 8.3M | ⭐ 970 | 🔴 november 2018|
| 🔗 [rakutenma](https://github.com/rakuten-nlp/rakutenma) | 📥 7/week | 📦 906 | ⭐ 472 | 🔴 january 2015|
| 🔗 [node-mecab-ya](https://github.com/golbin/mecab-ya) | 📥 51/week | 📦 7.2k | ⭐ 110 | 🔴 repo not found|
| 🔗 [juman-bin](https://github.com/thammin/juman-bin) | 📥 0/week | 📦 292 | ⭐ 3 | 🔴 may 2017|
| 🔗 [node-mecab-async](https://github.com/hecomi/node-mecab-async) | 📥 1.3k/week | 📦 rate limited by upstream service | ⭐ 103 | 🔴 october 2017|


### Converter
Libraries for converting Japanese scripts and readings

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - Japanese language library for converting Japanese sentence to Hiragana, Katakana or Romaji with furigana and okurigana modes supported.
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - Kuromoji morphological analyzer for kuroshiro.
 * [hepburn](https://github.com/lovell/hepburn) - Node.js module for converting Japanese Hiragana and Katakana script to, and from, Romaji using Hepburn romanisation
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - Converts Japanese Numerals into number
 * [jslingua](https://github.com/kariminf/jslingua) - Javascript libraries for text processing: Arabic, Japanese, and more.
 * [WanaKana](https://github.com/WaniKani/WanaKana) - A Javascript library that can detect and transliterate between Hiragana, Katakana, and Romaji.
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - Normalize and fix common issues with Romaji-based Japanese names.
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - Utility collections for making Japanese text old-fashioned
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - Open source address normalization library.
 * [jaconv](https://github.com/kazuhikoarase/jaconv) - Japanese text conversion library (javascript)
 * [romaji-conv](https://github.com/koozaki/romaji-conv) - Convert romaji into hiragana
 * [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) - National address data API
 * [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) - Convert text words to emojis
 * [japanese.js](https://github.com/hakatashi/japanese.js) - Util collection for Japanese text processing. Hiraganize, Katakanize, and Romanize.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuroshiro](https://github.com/hexenq/kuroshiro) | 📥 5.2k/week | 📦 406k | ⭐ 960 | 🔴 june 2021|
| 🔗 [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) | 📥 4.9k/week | 📦 382k | ⭐ 67 | 🔴 august 2018|
| 🔗 [hepburn](https://github.com/lovell/hepburn) | 📥 50k/week | 📦 3.3M | ⭐ 137 | 🟡 september 2025|
| 🔗 [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) | 📥 15k/week | 📦 2.2M | ⭐ 59 | 🔴 february 2023|
| 🔗 [jslingua](https://github.com/kariminf/jslingua) | 📥 37/week | 📦 8.1k | ⭐ 53 | 🔴 october 2023|
| 🔗 [WanaKana](https://github.com/WaniKani/WanaKana) | 📥 16k/week | 📦 2.1M | ⭐ 909 | 🟡 september 2025|
| 🔗 [node-romaji-name](https://github.com/jeresig/node-romaji-name) | 📥 86/week | 📦 rate limited by upstream service | ⭐ 41 | 🔴 december 2023|
| 🔗 [kyujitai.js](https://github.com/hakatashi/kyujitai.js) | 📥 7/week | 📦 1.1k | ⭐ 23 | 🔴 august 2020|
| 🔗 [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) | - | - | ⭐ 946 | 🟡 july 2025|
| 🔗 [jaconv](https://github.com/kazuhikoarase/jaconv) | - | - | ⭐ 87 | 🟡 june 2025|
| 🔗 [romaji-conv](https://github.com/koozaki/romaji-conv) | - | - | ⭐ 26 | 🟢 february|
| 🔗 [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) | - | - | ⭐ 71 | 🔴 january 2025|
| 🔗 [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [japanese.js](https://github.com/hakatashi/japanese.js) | - | - | ⭐ 167 | 🔴 august 2020|


### Others
Other libraries for Japanese NLP in JavaScript

 * [bangumi-data](https://github.com/bangumi-data/bangumi-data) - 生データーの日本のアニメについて
 * [yomichan](https://github.com/FooSoft/yomichan) - Japanese pop-up dictionary extension for Chrome and Firefox.
 * [proofreading-tool](https://github.com/gecko655/proofreading-tool) - GUIで動作する文書校正ツール GUI tool for textlinting.
 * [kanjigrid](https://github.com/minosvasilias/kanjigrid) - A web-app displaying the 2200 kanji characters taught in James Heisig's "Remembering the Kanji", 6th edition.
 * [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) - Monorepo for Kanji, Furigana, Japanese DB, and others
 * [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) - A JavaScript library for analyzing polite language (desu-masu style) and plain language (da-aru style) in sentences.
 * [hatsuon](https://github.com/DJTB/hatsuon) - Japanese pitch accent utils
 * [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) - Sentiment Analysis in Japanese. sentiment_ja with JavaScript
 * [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) - mecab-ipadic seed dictionary reader
 * [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) - Well, a different Japanese word everyday.
 * [oskim](https://github.com/esrille/oskim) - Extend GNOME On-Screen Keyboard for Input Methods
 * [tweetMapping](https://github.com/wtnv-lab/tweetMapping) - This is a digital archive of geotagged tweets that were tweeted within 24 hours of the occurrence of the Great East Japan Earthquake.
 * [pitch-accent](https://github.com/shirakaba/pitch-accent) - Predict pitch accent in Japanese
 * [kana2ipa](https://github.com/amanoese/kana2ipa) - Command to convert "hiragana" or "katakana" into International Phonetic Alphabet (IPA) symbols when pronouncing in Japanese.
 * [voicevox](https://github.com/VOICEVOX/voicevox) - Editor for VOICEVOX, a high-quality text-to-speech software that can be used for free.
 * [kamiya-codec](https://github.com/fasiha/kamiya-codec) - Towards a Japanese verb conjugator and deconjugator based on Taeko Kamiya's *The Handbook of Japanese Verbs* and *The Handbook of Japanese Adjectives and Adverbs* opuses.
 * [closewords](https://github.com/otoneko1102/closewords) - A library that searches for the most similar word from a group of words in Japanese (including kanji)
 * [japanese-analyzer](https://github.com/cokice/japanese-analyzer) - Japanese Sentence Analyzer (日本語文章解析器)
 * [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) - Standardize Japanese Furigana
 * [yama](https://github.com/sapjax/yama) - acquire Japanese vocabulary on any website
 * [kaitai](https://github.com/compile10/kaitai) - An application for analyzing Japanese sentence structure using AI. This tool visualizes how words and phrases relate to each other, showing grammatical relationships with interactive diagrams.
 * [tsukeru-furigana-converter](https://github.com/ln2058/tsukeru-furigana-converter) - Browser extension (Chrome/Edge/Firefox) that injects furigana into Japanese webpages on-demand; includes dictionary tooltips, JLPT filtering, and vocab/Anki export.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bangumi-data](https://github.com/bangumi-data/bangumi-data) | 📥 442/week | 📦 58k | ⭐ 596 | 🟢 today|
| 🔗 [yomichan](https://github.com/FooSoft/yomichan) | - | - | ⭐ 1.1k | 🔴 february 2023|
| 🔗 [proofreading-tool](https://github.com/gecko655/proofreading-tool) | - | - | ⭐ 87 | 🟡 october 2025|
| 🔗 [kanjigrid](https://github.com/minosvasilias/kanjigrid) | - | - | ⭐ 44 | 🔴 november 2018|
| 🔗 [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) | - | - | ⭐ 62 | 🔴 january 2023|
| 🔗 [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) | 📥 34k/week | 📦 4.9M | ⭐ 18 | 🔴 january 2025|
| 🔗 [hatsuon](https://github.com/DJTB/hatsuon) | 📥 5/week | 📦 903 | ⭐ 38 | 🔴 march 2022|
| 🔗 [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) | - | - | ⭐ 10 | 🔴 december 2021|
| 🔗 [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) | 📥 65/week | 📦 6k | ⭐ 8 | 🔴 july 2016|
| 🔗 [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) | 📥 1/week | 📦 274 | ⭐ repo not found | 🔴 repo not found|
| 🔗 [oskim](https://github.com/esrille/oskim) | - | - | ⭐ 2 | 🔴 february 2023|
| 🔗 [tweetMapping](https://github.com/wtnv-lab/tweetMapping) | - | - | ⭐ 26 | 🟢 march|
| 🔗 [pitch-accent](https://github.com/shirakaba/pitch-accent) | 📥 rate limited by upstream service | 📦 85 | ⭐ 2 | 🔴 september 2023|
| 🔗 [kana2ipa](https://github.com/amanoese/kana2ipa) | - | - | ⭐ 17 | 🔴 october 2020|
| 🔗 [voicevox](https://github.com/VOICEVOX/voicevox) | - | - | ⭐ 3.1k | 🟢 march|
| 🔗 [kamiya-codec](https://github.com/fasiha/kamiya-codec) | - | - | ⭐ 22 | 🟡 may 2025|
| 🔗 [closewords](https://github.com/otoneko1102/closewords) | - | - | ⭐ 4 | 🟢 march|
| 🔗 [japanese-analyzer](https://github.com/cokice/japanese-analyzer) | - | - | ⭐ 705 | 🟡 december 2025|
| 🔗 [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) | - | - | ⭐ 6 | 🔴 july 2024|
| 🔗 [yama](https://github.com/sapjax/yama) | - | - | ⭐ 8 | 🟢 february|
| 🔗 [kaitai](https://github.com/compile10/kaitai) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [tsukeru-furigana-converter](https://github.com/ln2058/tsukeru-furigana-converter) | - | - | ⭐ 1 | 🟢 march|


## Go

### Morphology analysis
Lightweight Japanese morphological analysis libraries in Go

 * [kagome](https://github.com/ikawaha/kagome) - Self-contained Japanese Morphological Analyzer written in pure Go


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kagome](https://github.com/ikawaha/kagome) | - | - | ⭐ 956 | 🟢 last tuesday|


### Others
Additional Go-based Japanese text processing libraries

 * [ojosama](https://github.com/jiro4989/ojosama) - Converts text into the tone of Lady Salome from the Hundred Celestial Plains.
 * [nihongo](https://github.com/gojp/nihongo) - Japanese Dictionary
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - External dictionary importer for Yomichan.
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - THE IDOLM@STER words dictionary for Japanese IME (by imas-db.jp)
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - Kanji 転写 to hiragana/katakana/romaji, in Go
 * [go-moji](https://github.com/ktnyt/go-moji) - A Go library for Zenkaku/Hankaku conversion
 * [ojichat](https://github.com/greymd/ojichat) - Generate sentences that an uncle would send via LINE or email.
 * [name](https://github.com/kuniwak/name) - 名前検索者


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ojosama](https://github.com/jiro4989/ojosama) | - | - | ⭐ 387 | 🟢 march|
| 🔗 [nihongo](https://github.com/gojp/nihongo) | - | - | ⭐ 83 | 🔴 february 2024|
| 🔗 [yomichan-import](https://github.com/FooSoft/yomichan-import) | - | - | ⭐ 86 | 🔴 february 2023|
| 🔗 [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) | - | - | ⭐ 32 | 🟢 january|
| 🔗 [go-kakasi](https://github.com/sarumaj/go-kakasi) | - | - | ⭐ 6 | 🟡 december 2025|
| 🔗 [go-moji](https://github.com/ktnyt/go-moji) | - | - | ⭐ 20 | 🔴 april 2019|
| 🔗 [ojichat](https://github.com/greymd/ojichat) | - | - | ⭐ 1.3k | 🔴 october 2024|
| 🔗 [name](https://github.com/kuniwak/name) | - | - | ⭐ 11 | 🔴 january 2025|


## Java

### Morphology analysis
Japanese morphological analysis and dictionary management libraries

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji is a self-contained and very easy to use Japanese morphological analyzer designed for search
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - A lexicon for Sudachi
 * [meval](https://github.com/teru-oka-1933/meval) - Morphological analyzer performance evaluation system MevAL


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji](https://github.com/atilika/kuromoji) | - | - | ⭐ 1k | 🔴 september 2019|
| 🔗 [Sudachi](https://github.com/WorksApplications/Sudachi) | - | - | ⭐ 948 | 🔴 november 2024|
| 🔗 [SudachiDict](https://github.com/WorksApplications/SudachiDict) | - | - | ⭐ 283 | 🟢 january|
| 🔗 [meval](https://github.com/teru-oka-1933/meval) | - | - | ⭐ 7 | 🔴 august 2019|


### Others
Java libraries for Japanese NLP and OCR

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - Java library for identifying Japanese characters from images
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - Java library and command-line tool to transliterate Japanese kanji to romaji (Latin alphabet)
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Kanji transliteration to hiragana/katakana/romaji, in Java
 * [Kamite](https://github.com/fauu/Kamite) - A desktop language immersion companion for learners of Japanese
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - Async Japanese Tokenizer Native Plugin for React Native for iOS and Android
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - The Japanese analyzer utilizes the Kuromoji Japanese tokenizer for ElasticSearch.
 * [moji4j](https://github.com/andree-surya/moji4j) - A Java library to converts between Japanese Hiragana, Katakana, and Romaji scripts.
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - Japanese text normalizer for mecab-neologd
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - The Japanese analysis plugin for elasticsearch


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) | - | - | ⭐ 204 | 🔴 may 2021|
| 🔗 [jakaroma](https://github.com/nicolas-raoul/jakaroma) | - | - | ⭐ 68 | 🟡 june 2025|
| 🔗 [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) | - | - | ⭐ 55 | 🔴 april 2016|
| 🔗 [Kamite](https://github.com/fauu/Kamite) | - | - | ⭐ 132 | 🔴 march 2025|
| 🔗 [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) | - | - | ⭐ 38 | 🔴 june 2023|
| 🔗 [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) | - | - | ⭐ 29 | 🔴 march 2012|
| 🔗 [moji4j](https://github.com/andree-surya/moji4j) | - | - | ⭐ 33 | 🔴 june 2022|
| 🔗 [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) | - | - | ⭐ 5 | 🟢 february|
| 🔗 [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) | - | - | ⭐ 219 | 🟢 february|


## Pretrained model

### Word2Vec
Models that convert words into numeric vectors to capture semantic similarity

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - Word2vec (word to vectors) approach for Japanese language using Gensim and Mecab.
 * [chiVe](https://github.com/WorksApplications/chiVe) - Japanese word embedding with Sudachi and NWJC
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - Elmo (in Japanese)
 * [embedrank](https://github.com/yagays/embedrank) - Python Implementation of EmbedRank
 * [aovec](https://github.com/eggplants/aovec) - Easy aozorabunko Word2Vec Builder - Word2Vec Builder and pre-built model for all books in the Aozora Bunko library.
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - This is a repository for the AI LAB article "係り受けに基づく日本語単語埋込 (Dependency-based Japanese Word Embeddings)" ( Article URL https://ai-lab.lapras.com/nlp/japanese-word-embedding/)
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - Yet Another Japanese-Wikipedia Entity Vectors
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - A script for learning word embedding models such as word2vec, fastText, and GloVe based on the results of morphological analysis using both the IPA dictionary and the latest Neologd dictionary, using MeCab on the latest Japanese Wikipedia dump data.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) | - | - | ⭐ 87 | 🔴 august 2020|
| 🔗 [chiVe](https://github.com/WorksApplications/chiVe) | - | - | ⭐ 171 | 🔴 march 2024|
| 🔗 [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) | - | - | ⭐ 4 | 🔴 october 2019|
| 🔗 [embedrank](https://github.com/yagays/embedrank) | - | - | ⭐ 48 | 🔴 march 2019|
| 🔗 [aovec](https://github.com/eggplants/aovec) | 📥 197 | 📦 82k | ⭐ 3 | 🔴 january 2023|
| 🔗 [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) | - | - | ⭐ 8 | 🔴 august 2019|
| 🔗 [jawikivec](https://github.com/wikiwikification/jawikivec) | - | - | ⭐ 2 | 🔴 november 2018|
| 🔗 [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) | - | - | ⭐ 11 | 🔴 may 2020|


### Transformer based models
Models that use self-attention to understand context and perform advanced language tasks

 * [bert-japanese](https://github.com/cl-tohoku/bert-japanese) - BERT models for Japanese language text.
 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - Code for producing Japanese pretrained models provided by rinna Co., Ltd.
 * [bert-japanese](https://github.com/yoheikikuta/bert-japanese) - BERT with SentencePiece for Japanese text.
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - 日本語のトークナイザー（分かち書きツール）のためのTransformers
 * [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) - Code for evaluating Japanese pretrained models provided by NTT Ltd.
 * [shiba](https://github.com/octanove/shiba) - Pytorch implementation and pre-trained Japanese model for CANINE, the efficient character-level transformer.
 * [Dialog](https://github.com/reppy4620/Dialog) - A PyTorch Implementation of japanese chatbot using BERT and Transformer's decoder
 * [language-pretraining](https://github.com/retarfi/language-pretraining) - BERT and ELECTRA models of PyTorch implementations for Japanese text.
 * [medbertjp](https://github.com/ou-medinfo/medbertjp) - Trials of pre-trained BERT models for the medical domain in Japanese.
 * [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) - ILYS-aoba-chatbot
 * [t5-japanese](https://github.com/megagonlabs/t5-japanese) - Codes to pre-train Japanese T5 models
 * [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) - Using a pre-trained Japanese BERT model with Pytorch.
 * [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) - Laboro BERT Japanese: Japanese BERT Pre-Trained With Web-Corpus
 * [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) - Japanese BERT Pretrained Model
 * [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) - aMLP Transformer Model for Japanese
 * [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) - Japanese BERT trained on Aozora Bunko and Wikipedia, pre-tokenized by MeCab with UniDic & SudachiPy
 * [sbert-ja](https://github.com/colorfulscoop/sbert-ja) - Code to train Sentence BERT Japanese model for Hugging Face Model Hub
 * [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) - Official fine-tuning code for "Emotion Analysis of Japanese Tweets and Comparison to Vaccinations in Japan"
 * [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) - Japanese GPT2 Generation Model
 * [text2text-japanese](https://github.com/tanreinama/text2text-japanese) - gpt-2 based text2text conversion model
 * [gpt-ja](https://github.com/colorfulscoop/gpt-ja) - GPT-2 Japanese model for HuggingFace's transformers
 * [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) - MT model trained using the friendly_JA Corpus attempting to make Japanese easier/more accessible to occidental people by using the Latin/English derived katakana lexicon instead of the standard Sino-Japanese lexicon
 * [albert-japanese](https://github.com/alinear-corp/albert-japanese) - BERT with SentencePiece for Japanese text.
 * [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) - Repository for generating a pre-trained BERT model using the Japanese Wikipedia corpus.
 * [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) - A Japanese DistilBERT pretrained model, which was trained on Wikipedia.
 * [bert](https://github.com/informatix-inc/bert) - This repository provides snippets to use RoBERTa pre-trained on Japanese corpus. Our dataset consists of Japanese Wikipedia and web-scrolled articles, 25GB in total. The released model is built based on that from HuggingFace.
 * [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) - Laboro DistilBERT Japanese
 * [luke](https://github.com/studio-ousia/luke) - LUKE -- Language Understanding with Knowledge-based Embeddings
 * [GPTSAN](https://github.com/tanreinama/GPTSAN) - General-purpose Swich transformer based Japanese language mode
 * [japanese-clip](https://github.com/rinnakk/japanese-clip) - Japanese CLIP by rinna Co., Ltd.
 * [AcademicBART](https://github.com/EhimeNLP/AcademicBART) - We pretrained a BART-based Japanese masked language model on paper abstracts from the academic database CiNii Articles
 * [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) - We pretrained a RoBERTa-based Japanese masked language model on paper abstracts from the academic database CiNii Articles.
 * [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) - DistilBERT model pre-trained on 131 GB of Japanese web text. The teacher model is BERT-base that built in-house at LINE.
 * [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) - Link to the Low-Rank Adapter created by fine-tuning LLaMA using the Stanford Alpaca dataset translated into Japanese, and sample code for generating it.
 * [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) - Pretrained models, codes and guidances to pretrain official ALBERT(https://github.com/google-research/albert) on Japanese Wikipedia Resources
 * [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) - 日本のLLaMa実験
 * [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) - EasyLightChatAssistant は軽量で検閲や規制のないローカル日本語モデルのLightChatAssistant を、KoboldCpp で簡単にお試しする環境です。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bert-japanese](https://github.com/cl-tohoku/bert-japanese) | - | - | ⭐ 543 | 🔴 march 2024|
| 🔗 [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [bert-japanese](https://github.com/yoheikikuta/bert-japanese) | - | - | ⭐ 498 | 🔴 february 2021|
| 🔗 [SudachiTra](https://github.com/WorksApplications/SudachiTra) | 📥 1k | 📦 162k | ⭐ 79 | 🔴 december 2023|
| 🔗 [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) | - | - | ⭐ 245 | 🔴 june 2023|
| 🔗 [shiba](https://github.com/octanove/shiba) | 📥 25 | 📦 7k | ⭐ 89 | 🔴 november 2023|
| 🔗 [Dialog](https://github.com/reppy4620/Dialog) | - | - | ⭐ 72 | 🔴 october 2020|
| 🔗 [language-pretraining](https://github.com/retarfi/language-pretraining) | - | - | ⭐ 50 | 🔴 may 2023|
| 🔗 [medbertjp](https://github.com/ou-medinfo/medbertjp) | - | - | ⭐ 12 | 🔴 november 2020|
| 🔗 [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) | - | - | ⭐ 23 | 🔴 october 2021|
| 🔗 [t5-japanese](https://github.com/megagonlabs/t5-japanese) | - | - | ⭐ 40 | 🔴 september 2021|
| 🔗 [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) | - | - | ⭐ 35 | 🔴 june 2019|
| 🔗 [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) | - | - | ⭐ 73 | 🔴 may 2022|
| 🔗 [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) | - | - | ⭐ 23 | 🔴 november 2021|
| 🔗 [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) | - | - | ⭐ 16 | 🔴 may 2022|
| 🔗 [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) | - | - | ⭐ 40 | 🔴 august 2020|
| 🔗 [sbert-ja](https://github.com/colorfulscoop/sbert-ja) | - | - | ⭐ 11 | 🔴 august 2021|
| 🔗 [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) | - | - | ⭐ 7 | 🔴 may 2022|
| 🔗 [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) | - | - | ⭐ 324 | 🔴 september 2023|
| 🔗 [text2text-japanese](https://github.com/tanreinama/text2text-japanese) | - | - | ⭐ 33 | 🔴 july 2021|
| 🔗 [gpt-ja](https://github.com/colorfulscoop/gpt-ja) | - | - | ⭐ 3 | 🔴 september 2021|
| 🔗 [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) | - | - | ⭐ 1 | 🔴 may 2022|
| 🔗 [albert-japanese](https://github.com/alinear-corp/albert-japanese) | - | - | ⭐ 33 | 🔴 october 2021|
| 🔗 [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) | - | - | ⭐ 115 | 🔴 november 2018|
| 🔗 [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) | - | - | ⭐ 161 | 🔴 april 2020|
| 🔗 [bert](https://github.com/informatix-inc/bert) | - | - | ⭐ 28 | 🔴 april 2022|
| 🔗 [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) | - | - | ⭐ 16 | 🔴 december 2020|
| 🔗 [luke](https://github.com/studio-ousia/luke) | - | - | ⭐ 727 | 🔴 june 2023|
| 🔗 [GPTSAN](https://github.com/tanreinama/GPTSAN) | - | - | ⭐ 118 | 🔴 september 2023|
| 🔗 [japanese-clip](https://github.com/rinnakk/japanese-clip) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [AcademicBART](https://github.com/EhimeNLP/AcademicBART) | - | - | ⭐ 2 | 🔴 july 2024|
| 🔗 [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | - | - | ⭐ 9 | 🔴 september 2024|
| 🔗 [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) | - | - | ⭐ 46 | 🔴 march 2023|
| 🔗 [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) | - | - | ⭐ 141 | 🔴 april 2023|
| 🔗 [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) | - | - | ⭐ 13 | 🔴 september 2023|
| 🔗 [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) | - | - | ⭐ 54 | 🟡 december 2025|
| 🔗 [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) | - | - | ⭐ 42 | 🔴 april 2024|


## ChatGPT
Resources for using ChatGPT and APIs for Japanese dialogue and text generation

 * [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) - A program that allows you to chat using ChatGPT in VRChat.
 * [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) - We are developing the foundation of AITuber.
 * [wanna](https://github.com/hirokidaichi/wanna) - Shell command launcher with natural language
 * [ChatdollKit](https://github.com/uezo/ChatdollKit) - ChatdollKit enables you to make your 3D model into a chatbot
 * [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) - GUI for ChatGPT API For Japanese
 * [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) - This is a Siro Ghost equipped with ChatGPT3.5, called "AI Imouto Aichan". A separate ChatGPT API key is required to use it.
 * [vrchatbot](https://github.com/Geson-anko/vrchatbot) - Repository for creating AI bots in VRChat
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPT will become a YouTuber.
 * [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) - A chatbox application built using Nuxt 3 powered by Open AI Text completion endpoint. You can select different personality of your AI friend. The default will respond in Japanese. You can use this app to practice your Nihongo skills!
 * [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) - This Chrome extension can translate selected Japanese text to Hiragana by using ChatGPT.
 * [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) - In this sample, we demonstrate several approaches to creating an experience similar to ChatGPT for proprietary data using the Retrieval Augmented Generation pattern.
 * [chatvrm](https://github.com/pixiv/chatvrm) - ChatVRM is a demo application that allows you to easily chat with 3D characters in your browser.
 * [sftly-replace](https://github.com/kmizu/sftly-replace) - A Chrome extention to replace the selected text softly
 * [summarize_arxv](https://github.com/rkmt/summarize_arxv) - Summarize arXiv paper with figures
 * [aiavatarkit](https://github.com/uezo/aiavatarkit) - Building AI-based conversational avatars lightning fast
 * [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) - This repository is intended to package and release the flows and other solutions created for the trial use of ChatGPT at Kobe City Hall.
 * [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) - We provide free samples of applications (reference architecture, sample code, and deployment instructions) for the purpose of implementing applications using Azure OpenAI.
 * [character_chat](https://github.com/mutaguchi/character_chat) - This is a chat script that uses OpenAI's API to have a conversation with a character set in Japanese.
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - Slackbot script for using OpenAI's ChatGPT API on Slack (assumes usage in Japanese)
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - This is a sample of ChatGPT's prompt.
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - A Japanese Kanji Flashcard App built using Python and Langchain, enhanced with the intelligence of GPT-4.
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - Evaluating GPT-4 and ChatGPT on Japanese Medical Licensing Examinations
 * [japagen](https://github.com/retrieva/japagen) - Investigation of pseudo-learning data generation using LLM in Japanese language tasks
 * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - Sample prompts for various generative AIs such as ChatGPT and Copilot in Japanese.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) | - | - | ⭐ 15 | 🔴 march 2023|
| 🔗 [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) | - | - | ⭐ 5 | 🔴 march 2023|
| 🔗 [wanna](https://github.com/hirokidaichi/wanna) | 📥 74 | 📦 20k | ⭐ 141 | 🔴 april 2023|
| 🔗 [ChatdollKit](https://github.com/uezo/ChatdollKit) | - | - | ⭐ 1.1k | 🟢 march|
| 🔗 [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) | - | - | ⭐ 1 | 🔴 march 2023|
| 🔗 [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) | - | - | ⭐ 27 | 🔴 may 2023|
| 🔗 [vrchatbot](https://github.com/Geson-anko/vrchatbot) | - | - | ⭐ 29 | 🔴 december 2022|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) | - | - | ⭐ 16 | 🔴 april 2023|
| 🔗 [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) | - | - | ⭐ 1 | 🔴 april 2023|
| 🔗 [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) | - | - | ⭐ 46 | 🔴 december 2023|
| 🔗 [chatvrm](https://github.com/pixiv/chatvrm) | - | - | ⭐ 831 | 🟡 may 2025|
| 🔗 [sftly-replace](https://github.com/kmizu/sftly-replace) | - | - | ⭐ 4 | 🔴 may 2023|
| 🔗 [summarize_arxv](https://github.com/rkmt/summarize_arxv) | - | - | ⭐ 173 | 🔴 may 2023|
| 🔗 [aiavatarkit](https://github.com/uezo/aiavatarkit) | - | - | ⭐ 562 | 🟢 last friday|
| 🔗 [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) | - | - | ⭐ 280 | 🟢 march|
| 🔗 [character_chat](https://github.com/mutaguchi/character_chat) | - | - | ⭐ 16 | 🔴 june 2023|
| 🔗 [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) | - | - | ⭐ 64 | 🔴 july 2024|
| 🔗 [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) | - | - | ⭐ 426 | 🟢 last monday|
| 🔗 [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) | - | - | ⭐ 6 | 🔴 october 2023|
| 🔗 [IgakuQA](https://github.com/jungokasai/IgakuQA) | - | - | ⭐ 49 | 🔴 march 2023|
| 🔗 [japagen](https://github.com/retrieva/japagen) | - | - | ⭐ 1 | 🔴 october 2024|
| 🔗 [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) | - | - | ⭐ 426 | 🟢 last monday|


## Dictionary and IME
Resources for Japanese dictionaries and input method editors (IME)

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - Neologism dictionary based on the language resources on the Web for mecab-ipadic
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - A Japanese accent dictionary generator
 * [jamdict](https://github.com/neocl/jamdict) - Python 3 library for manipulating Jim Breen's JMdict, KanjiDic2, JMnedict and kanji-radical mappings
 * [unidic-py](https://github.com/polm/unidic-py) - Unidic packaged for installation via pip.
 * [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) - Japanese Company Lexicon (JCLdic)
 * [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) - A comprehensive medical dictionary for Sudachi.
 * [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) - Generate SKK/MeCab dictionary from Wikipedia(Japanese edition)
 * [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) - dictionary to find emotion related to text
 * [JumanDIC](https://github.com/ku-nlp/JumanDIC) - This repository contains source dictionary files to build dictionaries for JUMAN and Juman++.
 * [ipadic-py](https://github.com/polm/ipadic-py) - IPAdic packaged for easy use from Python.
 * [unidic-lite](https://github.com/polm/unidic-lite) - A small version of UniDic for easy pip installs.
 * [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) - An IME additional dictionary for inputting emojis in Japanese, such as the Google Japanese Input, which enables conversion from Japanese to emojis through an IME extension dictionary.
 * [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) - An IME additional dictionary called "orange_book" for Japanese-English conversion and expansion of English abbreviations, which enables Japanese-English conversion and expansion of English abbreviations in Google Japanese Input and ATOK.
 * [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) - IME dictionary for the common parts of Nico Nico Daihyakka and Pixiv Encyclopedia.
 * [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) - GoogleIME用カタカナ語辞書プロジェクトのアーカイブです。Project archive of Google IME user dictionary from Katakana word ( Japanese loanword ) to English.
 * [emoticon](https://github.com/tiwanari/emoticon) - Google Japanese Input's emoticon dictionary ∩(,,Ò‿Ó,,)∩
 * [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) - This is a conversion of the open source mozc dictionary to the MeCab dictionary format.
 * [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) - Electric Sound Dictionary: A dictionary of terms related to "Electric Sound Department" intended for use with Microsoft IME and other similar software.
 * [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) - This is a glossary of "Nijisanji" related terms intended for use with Microsoft IME and other similar software.
 * [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) - This is a terminology dictionary that covers the names of all currently known Pokémon, intended for use with Microsoft IME and similar software.
 * [EJDict](https://github.com/kujirahand/EJDict) - English-Japanese Dictionary data (Public Domain) EJDict-hand
 * [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) - Using the precious tobacco box as a visual aid, it is possible to speak proper Japanese.
 * [genshin-dict](https://github.com/kotofurumiya/genshin-dict) - This is a vocabulary dictionary for Genshin Impact that can be used on Windows/macOS.
 * [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) - JMdict and JMnedict in JSON format
 * [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) - Convert external words into Mozc system dictionary
 * [mh-dict-jp](https://github.com/utubo/mh-dict-jp) - I want to create a user dictionary for Monster Hunter...
 * [jitenbot](https://github.com/stephenmk/jitenbot) - Convert data from Japanese dictionary websites and applications into portable file formats
 * [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) - Neologism dictionary based on the language resources on the Web for mecab-unidic
 * [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) - This is a dictionary file about Hololive (Hololive Production). You can use the text files in the ./dictionary folder to add words to your IME. Please refer to README.md for more details.
 * [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) - JMdict, JMnedict, KANJIDIC for Yomitan/Yomichan.
 * [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) - JLPT level tags for words in Yomichan
 * [Jitendex](https://github.com/stephenmk/Jitendex) - A free and openly licensed Japanese-to-English dictionary compatible with multiple dictionary clients
 * [jiten](https://github.com/obfusk/jiten) - japanese android/cli/web dictionary based on jmdict/kanjidic — 日本語　辞典　和英辞典　漢英字典　和独辞典　和蘭辞典
 * [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) - Pixiv Encyclopedia Dictionary for Yomitan
 * [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) - Uchinaaguchi Dictionary (Okinawan Language Dictionary)
 * [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) - Japanese and Chinese dictionaries for Yomitan.
 * [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) - Generic dictionary tool that automatically reads the word you mouse over.
 * [jisyo](https://github.com/skk-dict/jisyo) - New dictionary format for the kana-kanji conversion engine SKK
 * [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) - SKK dictionary for converting Japanese readings to Emoji 😂
 * [anthy](https://github.com/netsphere-labs/anthy) - Anthy is a kana-kanji conversion engine for Japanese. It converts roma-ji to kana, and the kana text to a mixed kana and kanji.
 * [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) - Dictionary for Google Japanese input for AWS service names
 * [cl-skkserv](https://github.com/tani/cl-skkserv) - SKK dictionary server and its extensions using Common Lisp
 * [anthy](https://github.com/xorgy/anthy) - Anthy maintenance
 * [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) - Anthy Unicode - Another Anthy
 * [azooKey](https://github.com/ensan-hcl/azooKey) - azooKey: A Japanese Keyboard iOS Application Fully Developed in Swift
 * [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) - Japanese Input Method azooKey for Desktop, supporting macOS
 * [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) - Japanese input method for fcitx5, powered by azooKey engine
 * [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) - Mozc UT Place Name Dictionary is a dictionary converted from the Japan Post's ZIP code data for Mozc.
 * [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) - Kana-Kanji Conversion Module written in Swift
 * [libkkc](https://github.com/ueno/libkkc) - Japanese Kana Kanji conversion input method library
 * [libskk](https://github.com/ueno/libskk) - Japanese SKK input method library
 * [kanayomi-dict](https://github.com/warihima/kanayomi-dict) - User dictionary in openjtalk format
 * [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) - Dictionary related data of the kanji database
 * [wlsp-classical](https://github.com/yocjyet/wlsp-classical) - Classified vocabulary list data of classical Japanese
 * [kanji-dict](https://github.com/marmooo/kanji-dict) - This is a kanji dictionary for looking up the stroke order, reading, number of strokes, radical, usage examples, and origin of kanji characters. It includes all 98,682 kanji characters in Unicode 15.1.
 * [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) - (๑ ᴖ ᴑ ᴖ ๑) Myon Kaomoji (formerly Kaomoji_proj) is a project to create a dictionary of emoticons for Microsoft's input software, Microsoft IME.
 * [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) - Kotlin Kana Kanji Conversion Program
 * [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) - Japanese-English Dictionary using jisho.org with audio, csv export of entries, and preview of dictionary sites.
 * [ichiran](https://github.com/tshatrov/ichiran) - Linguistic tools for texts in Japanese language
 * [mikan](https://github.com/mojyack/mikan) - A Japanese input method.
 * [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) - A quick reference for the material taught in Colloquial Kansai Japanese.
 * [jisho-open](https://github.com/hlorenzi/jisho-open) - Web frontend for the JMdict Japanese-English dictionary project, with study list support!
 * [macskk](https://github.com/mtgto/macskk) - Yet Another macOS SKK Input Method
 * [nandoku](https://github.com/marmooo/nandoku) - This is a dictionary that compiles difficult kanji characters by grade level.
 * [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) - A FOSS Japanese IME for Android
 * [anthywl](https://github.com/tadeokondrak/anthywl) - Japanese input method for Sway using libanthy
 * [sekka](https://github.com/kiyoka/sekka) - Yet another Japanese Input Method inspired by SKK.
 * [sumibi](https://github.com/kiyoka/sumibi) - Japanese input method powered by ChatGPT API
 * [jinmei-dict](https://github.com/s1r-j/jinmei-dict) - Extracting only personal names from dictionary data, formatting it into JSON format where the reading (in katakana) is the key and the candidate characters are stored in a list.
 * [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) - Violet - a completely offline Japanese keyboard app
 * [japanesearabic](https://github.com/a-hamdi/japanesearabic) - Japanese-Arabic Dictionary (日本語・アラビア語辞書) قاموس اللغة اليابانية والعربية (Yomitan)
 * [o-dic](https://github.com/makotoga/o-dic) - Okinawa Dictionary
 * [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) - SKK Emoji Dictionary
 * [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) - A personal name dictionary for Mozc.
 * [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) - A dictionary converted from SudachiDict for Mozc.
 * [nihongo](https://github.com/sph-mn/nihongo) - 日本語の言語データと辞書
 * [kagome-dict](https://github.com/ikawaha/kagome-dict) - Dictionary Library for Kagome v2
 * [canna](https://github.com/canna-input/canna) - Canna Japanese input system
 * [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) - Kansai Dialect Dictionary - A Japanese dialect accent dictionary containing 4,615 words.
 * [jitendex](https://github.com/jitendex/jitendex) - A free, offline, and openly licensed Japanese-to-English dictionary. Updates monthly!
 * [karukan](https://github.com/togatoga/karukan) - Japanese Input Method System for Linux, Neural Kana-Kanji Conversion Engine + fcitx5 IME
 * [shitto-mania-dic](https://github.com/junikematsu/shitto-mania-dic) - 嫉妬辞書（Shitto-Mania / Jealousy Dictionary）


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) | - | - | ⭐ 2.8k | 🔴 september 2020|
| 🔗 [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) | - | - | ⭐ 124 | 🔴 march 2024|
| 🔗 [jamdict](https://github.com/neocl/jamdict) | 📥 205 | 📦 53k | ⭐ 168 | 🔴 june 2021|
| 🔗 [unidic-py](https://github.com/polm/unidic-py) | 📥 57k | 📦 10M | ⭐ 109 | 🔴 february 2025|
| 🔗 [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) | - | - | ⭐ 100 | 🔴 january 2023|
| 🔗 [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) | - | - | ⭐ 7 | 🔴 april 2021|
| 🔗 [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) | - | - | ⭐ 60 | 🟢 last monday|
| 🔗 [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) | - | - | ⭐ 40 | 🔴 january 2021|
| 🔗 [JumanDIC](https://github.com/ku-nlp/JumanDIC) | - | - | ⭐ 4 | 🔴 august 2022|
| 🔗 [ipadic-py](https://github.com/polm/ipadic-py) | 📥 32k | 📦 7M | ⭐ 24 | 🔴 october 2021|
| 🔗 [unidic-lite](https://github.com/polm/unidic-lite) | 📥 69k | 📦 10M | ⭐ 49 | 🔴 september 2020|
| 🔗 [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) | - | - | ⭐ 365 | 🔴 january 2023|
| 🔗 [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) | - | - | ⭐ 102 | 🔴 january 2023|
| 🔗 [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) | - | - | ⭐ 82 | 🔴 september 2024|
| 🔗 [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) | - | - | ⭐ 58 | 🔴 december 2016|
| 🔗 [emoticon](https://github.com/tiwanari/emoticon) | - | - | ⭐ 44 | 🔴 may 2020|
| 🔗 [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) | - | - | ⭐ 10 | 🔴 january 2018|
| 🔗 [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) | - | - | ⭐ 2 | 🔴 november 2022|
| 🔗 [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) | - | - | ⭐ 36 | 🟢 march|
| 🔗 [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) | - | - | ⭐ 0 | 🔴 january 2020|
| 🔗 [EJDict](https://github.com/kujirahand/EJDict) | - | - | ⭐ 250 | 🟡 november 2025|
| 🔗 [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) | - | - | ⭐ 26 | 🔴 may 2024|
| 🔗 [genshin-dict](https://github.com/kotofurumiya/genshin-dict) | - | - | ⭐ 126 | 🟢 february|
| 🔗 [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) | - | - | ⭐ 340 | 🟢 last monday|
| 🔗 [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) | - | - | ⭐ 69 | 🟡 september 2025|
| 🔗 [mh-dict-jp](https://github.com/utubo/mh-dict-jp) | - | - | ⭐ 5 | 🟡 april 2025|
| 🔗 [jitenbot](https://github.com/stephenmk/jitenbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) | - | - | ⭐ 87 | 🔴 september 2020|
| 🔗 [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) | - | - | ⭐ 24 | 🔴 december 2024|
| 🔗 [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) | - | - | ⭐ 252 | 🟢 february|
| 🔗 [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) | - | - | ⭐ 125 | 🟡 august 2025|
| 🔗 [Jitendex](https://github.com/stephenmk/Jitendex) | - | - | ⭐ 459 | 🟢 today|
| 🔗 [jiten](https://github.com/obfusk/jiten) | - | - | ⭐ 129 | 🔴 december 2023|
| 🔗 [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) | - | - | ⭐ 55 | 🟢 march|
| 🔗 [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) | - | - | ⭐ 4 | 🟢 march|
| 🔗 [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) | - | - | ⭐ 740 | 🟢 last wednesday|
| 🔗 [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) | - | - | ⭐ 72 | 🔴 january 2020|
| 🔗 [jisyo](https://github.com/skk-dict/jisyo) | - | - | ⭐ 28 | 🔴 september 2023|
| 🔗 [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) | - | - | ⭐ 30 | 🔴 march 2018|
| 🔗 [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) | - | - | ⭐ 7 | 🔴 november 2019|
| 🔗 [cl-skkserv](https://github.com/tani/cl-skkserv) | - | - | ⭐ 31 | 🔴 october 2024|
| 🔗 [anthy](https://github.com/xorgy/anthy) | - | - | ⭐ 3 | 🔴 july 2013|
| 🔗 [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) | - | - | ⭐ 41 | 🟢 march|
| 🔗 [azooKey](https://github.com/ensan-hcl/azooKey) | - | - | ⭐ 675 | 🟢 yesterday|
| 🔗 [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) | - | - | ⭐ 861 | 🟢 march|
| 🔗 [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) | - | - | ⭐ 178 | 🟢 february|
| 🔗 [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) | - | - | ⭐ 22 | 🟢 march|
| 🔗 [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) | - | - | ⭐ 138 | 🟢 yesterday|
| 🔗 [libkkc](https://github.com/ueno/libkkc) | - | - | ⭐ 112 | 🔴 august 2024|
| 🔗 [libskk](https://github.com/ueno/libskk) | - | - | ⭐ 100 | 🟢 march|
| 🔗 [kanayomi-dict](https://github.com/warihima/kanayomi-dict) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) | - | - | ⭐ 108 | 🔴 september 2017|
| 🔗 [wlsp-classical](https://github.com/yocjyet/wlsp-classical) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [kanji-dict](https://github.com/marmooo/kanji-dict) | - | - | ⭐ 6 | 🟢 march|
| 🔗 [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) | - | - | ⭐ 11 | 🟡 october 2025|
| 🔗 [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) | - | - | ⭐ 5 | 🟡 november 2025|
| 🔗 [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) | - | - | ⭐ 6 | 🟢 february|
| 🔗 [ichiran](https://github.com/tshatrov/ichiran) | - | - | ⭐ 388 | 🟢 january|
| 🔗 [mikan](https://github.com/mojyack/mikan) | - | - | ⭐ 24 | 🟡 june 2025|
| 🔗 [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) | - | - | ⭐ 9 | 🟢 february|
| 🔗 [jisho-open](https://github.com/hlorenzi/jisho-open) | - | - | ⭐ 57 | 🟢 february|
| 🔗 [macskk](https://github.com/mtgto/macskk) | - | - | ⭐ 281 | 🟢 last friday|
| 🔗 [nandoku](https://github.com/marmooo/nandoku) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [anthywl](https://github.com/tadeokondrak/anthywl) | - | - | ⭐ 34 | 🟡 april 2025|
| 🔗 [sekka](https://github.com/kiyoka/sekka) | - | - | ⭐ 24 | 🟡 july 2025|
| 🔗 [sumibi](https://github.com/kiyoka/sumibi) | - | - | ⭐ 39 | 🟢 march|
| 🔗 [jinmei-dict](https://github.com/s1r-j/jinmei-dict) | - | - | ⭐ 7 | 🔴 april 2020|
| 🔗 [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) | - | - | ⭐ 219 | 🟢 yesterday|
| 🔗 [japanesearabic](https://github.com/a-hamdi/japanesearabic) | - | - | ⭐ 18 | 🟡 may 2025|
| 🔗 [o-dic](https://github.com/makotoga/o-dic) | - | - | ⭐ 6 | 🟢 february|
| 🔗 [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) | - | - | ⭐ 141 | 🔴 january 2025|
| 🔗 [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) | - | - | ⭐ 26 | 🟢 march|
| 🔗 [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) | - | - | ⭐ 22 | 🟢 february|
| 🔗 [nihongo](https://github.com/sph-mn/nihongo) | - | - | ⭐ 19 | 🔴 january 2025|
| 🔗 [kagome-dict](https://github.com/ikawaha/kagome-dict) | - | - | ⭐ 15 | 🟢 march|
| 🔗 [canna](https://github.com/canna-input/canna) | - | - | ⭐ 4 | 🟡 august 2025|
| 🔗 [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) | - | - | ⭐ 1 | 🟡 december 2025|
| 🔗 [jitendex](https://github.com/jitendex/jitendex) | - | - | ⭐ 459 | 🟢 today|
| 🔗 [karukan](https://github.com/togatoga/karukan) | - | - | ⭐ 237 | 🟢 february|
| 🔗 [shitto-mania-dic](https://github.com/junikematsu/shitto-mania-dic) | - | - | ⭐ 0 | 🟢 last tuesday|


## Corpus

### Part-of-speech tagging / Named entity recognition
Corpora annotated with part-of-speech tags and named entities

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - Dataset for extracting named entities in Japanese using Wikipedia
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - Japanese IOB2 tagged corpus for Named Entity Recognition.
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - Capital Japanese Twitter Corpus
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - Parallel Universal Dependencies.
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - Japanese data from the Google UDT 2.0.
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - Kyoto University Web Document Leads Corpus
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - Annotated Fuman Kaitori Center Corpus
 * [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) - Long-unit-word version of UD_Japanese-GSD
 * [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) - This Universal Dependencies (UD) Japanese treebank is based on the definition of UD Japanese convention described in the UD documentation.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) | - | - | ⭐ 142 | 🔴 september 2023|
| 🔗 [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) | - | - | ⭐ 61 | 🔴 february 2020|
| 🔗 [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) | - | - | ⭐ 21 | 🔴 march 2016|
| 🔗 [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) | - | - | ⭐ 0 | 🔴 may 2020|
| 🔗 [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) | - | - | ⭐ 28 | 🔴 may 2022|
| 🔗 [KWDLC](https://github.com/ku-nlp/KWDLC) | - | - | ⭐ 83 | 🔴 december 2023|
| 🔗 [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) | - | - | ⭐ 18 | 🔴 december 2023|
| 🔗 [anthy](https://github.com/netsphere-labs/anthy) | - | - | ⭐ 15 | 🔴 february 2023|
| 🔗 [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) | - | - | ⭐ 3 | 🟡 november 2025|
| 🔗 [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) | - | - | ⭐ 26 | 🟡 november 2025|


### Parallel corpus
Bilingual corpora containing aligned sentences for translation tasks

 * [small_parallel_enja](https://github.com/odashi/small_parallel_enja) - 50k English-Japanese Parallel Corpus for Machine Translation Benchmark.
 * [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) - A Web Crawled Corpus for Japanese-Chinese NMT
 * [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) - Coursera Corpus Mining and Multistage Fine-Tuning for Improving Lectures Translation
 * [JESC](https://github.com/rpryzant/JESC) - A large parallel corpus of English and Japanese
 * [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) - AMI Meeting Parallel Corpus
 * [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) - This directory includes a giant Japanese-English subtitle corpus. The raw data comes from the Stanford’s JESC project.
 * [jesc_small](https://github.com/yusugomori/jesc_small) - Small Japanese-English Subtitle Corpus
 * [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) - This is a Japanese-English parallel corpus that takes into account prohibited language and word levels.
 * [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) - Comparison of computer science terms in Chinese, Japanese, and Korean.
 * [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) - Scripts for creating a Japanese-English parallel corpus and training NMT models
 * [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) - Google vs DeepL - Which one?
 * [matcha](https://github.com/ehimenlp/matcha) - We have created a dataset for simplifying Japanese text from an article on the Japanese tourism media MATCHA for visitors to Japan.
 * [en-ja-el](https://github.com/shigashiyama/en-ja-el) - EnJaEL: En-Ja Parallel Entity Linking Dataset (Version 1.0)


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [small_parallel_enja](https://github.com/odashi/small_parallel_enja) | - | - | ⭐ 98 | 🔴 september 2019|
| 🔗 [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) | - | - | ⭐ 15 | 🔴 september 2023|
| 🔗 [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) | - | - | ⭐ 15 | 🔴 august 2024|
| 🔗 [JESC](https://github.com/rpryzant/JESC) | - | - | ⭐ 87 | 🔴 november 2017|
| 🔗 [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) | - | - | ⭐ 11 | 🔴 december 2020|
| 🔗 [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) | - | - | ⭐ 5 | 🔴 august 2019|
| 🔗 [jesc_small](https://github.com/yusugomori/jesc_small) | - | - | ⭐ 3 | 🔴 july 2019|
| 🔗 [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) | - | - | ⭐ 6 | 🟡 august 2025|
| 🔗 [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) | - | - | ⭐ 149 | 🟢 february|
| 🔗 [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) | - | - | ⭐ 18 | 🔴 november 2021|
| 🔗 [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) | - | - | ⭐ 4 | 🔴 march 2020|
| 🔗 [matcha](https://github.com/ehimenlp/matcha) | - | - | ⭐ 6 | 🔴 january 2025|
| 🔗 [en-ja-el](https://github.com/shigashiyama/en-ja-el) | - | - | ⭐ 2 | 🔴 january 2025|


### Dialog corpus
Collections of conversation data for training dialogue systems

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本映画の推薦対話データセット
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - A dialogue corpus created by crawling the 2channel open forum.
 * [BSD](https://github.com/tsuruoka-lab/BSD) - The Business Scene Dialogue corpus
 * [asdc](https://github.com/megagonlabs/asdc) - Accommodation Search Dialog Corpus (宿泊施設探索対話コーパス)
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - Japanese dialogue data for seq2seq, etc.
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - This repository contains the Japanese–English bilingual chat corpus BPersona-chat published in the paper Chat Translation Error Detection for Assisting Cross-lingual Communications at AACL-IJCNLP 2022's Workshop Eval4NLP 2022.
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - Japanese Daily Dialogue, or 日本語日常対話コーパス in Japanese, is a high-quality multi-turn dialogue dataset containing daily conversations on five topics: dailylife, school, travel, health, and entertainment.
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - Japanese chat dataset for building LLM.
 * [kokorochat](https://github.com/uec-inabalab/kokorochat) - Counseling dialogue dataset collected through role-playing in Japanese
 * [JMultiWOZ-TC](https://github.com/llm-jp/JMultiWOZ-TC) - Evaluation of agent's function calling in multi-turn dialogue
 * [HOTATE](https://github.com/EhimeNLP/HOTATE) - Honne-tatemae Japanese dialogue dataset with true feelings and social facade
 * [ETCDataset](https://github.com/UEC-InabaLab/ETCDataset) - Emotion Transcription in Conversation Dataset は，対話中の各発話に対して話者自身が記述した心情文を含む，約1,000 件の対話からなる日本語対話データセットです．


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JMRD](https://github.com/ku-nlp/JMRD) | - | - | ⭐ 29 | 🔴 july 2022|
| 🔗 [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) | - | - | ⭐ 99 | 🔴 june 2021|
| 🔗 [BSD](https://github.com/tsuruoka-lab/BSD) | - | - | ⭐ 73 | 🔴 november 2021|
| 🔗 [asdc](https://github.com/megagonlabs/asdc) | - | - | ⭐ 25 | 🔴 august 2023|
| 🔗 [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) | - | - | ⭐ 3 | 🔴 october 2018|
| 🔗 [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) | - | - | ⭐ 5 | 🔴 january 2023|
| 🔗 [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) | - | - | ⭐ 56 | 🔴 march 2023|
| 🔗 [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) | - | - | ⭐ 88 | 🔴 january 2024|
| 🔗 [kokorochat](https://github.com/uec-inabalab/kokorochat) | - | - | ⭐ 19 | 🟡 august 2025|
| 🔗 [JMultiWOZ-TC](https://github.com/llm-jp/JMultiWOZ-TC) | - | - | ⭐ 0 | 🟢 march|
| 🔗 [HOTATE](https://github.com/EhimeNLP/HOTATE) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [ETCDataset](https://github.com/UEC-InabaLab/ETCDataset) | - | - | ⭐ 11 | 🟢 january|

### Others
Corpora for tasks such as question answering or entailment recognition

 * [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) - Japanese Realistic Textual Entailment Corpus (NLP 2020, LREC 2020)
 * [kanji-data](https://github.com/davidluzgouveia/kanji-data) - A JSON kanji dataset with updated JLPT levels and WaniKani information
 * [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) - Japanese Word Similarity Dataset
 * [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) - A paraphrase database for Japanese text simplification
 * [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) - chakki's Aspect-Based Sentiment Analysis dataset
 * [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) - JaQuAD: Japanese Question Answering Dataset for Machine Reading Comprehension (2022, Skelter Labs)
 * [JaNLI](https://github.com/verypluming/JaNLI) - Japanese Adversarial Natural Language Inference Dataset
 * [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) - Evidence-based Explanation Dataset (AACL-IJCNLP 2020)
 * [emoji-ja](https://github.com/yagays/emoji-ja) - Japanese pronunciation/keywords/classification dictionary for UNICODE emojis.
 * [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) - Japanese name matching dataset created from Wikipedia.
 * [ja.text8](https://github.com/Hironsan/ja.text8) - Japanese text8 corpus for word embedding.
 * [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) - 3-line summary dataset
 * [japanese](https://github.com/hingston/japanese) - This repo contains a list of the 44,998 most common Japanese words in order of frequency, as determined by the University of Leeds Corpus.
 * [kanji-frequency](https://github.com/scriptin/kanji-frequency) - Kanji usage frequency data collected from various sources
 * [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) - TEDxJP-10K ASR Evaluation Dataset
 * [CoARiJ](https://github.com/chakki-works/CoARiJ) - Corpus of Annual Reports in Japan
 * [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) - A raw corpus/tool that collects technical books written in Japanese.
 * [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) - Chunked word annotation for ITA corpus
 * [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) - Utility scripts for preprocessing Wikipedia texts for NLP
 * [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) - We will collect inappropriate expressions in Japanese. We believe it can be used for data cleaning in natural language processing.
 * [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) - We organized data on factions, members, bills, and interpellation requests from the official website of the House of Councillors.
 * [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) - National Diet Bill Database: House of Representatives
 * [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) - STAIR captions: A Japanese image caption dataset on a large scale.
 * [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) - Japanese Translation of Winograd Schema Challenge
 * [speechBSD](https://github.com/ku-nlp/speechBSD) - An extension of the BSD corpus with audio and speaker attribute information
 * [ita-corpus](https://github.com/mmorise/ita-corpus) - List of sentences in the ITA corpus
 * [rohan4600](https://github.com/mmorise/rohan4600) - Mora balance Japanese corpus
 * [anlp-jp-history](https://github.com/whym/anlp-jp-history) - A complete list and machine-readable version of the presentations at the annual conference of the Association for Computational Linguistics.
 * [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) - Evaluation dataset for honorific language conversion task.
 * [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) - English loanwords in Japanese
 * [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) - Japanese-Wikipedia Wikification Corpus
 * [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) - This is the corpus of Japanese Text that general policy speech of prime minister of Japan
 * [wrime](https://github.com/ids-cv/wrime) - WRIME: Subjective and Objective Emotion Analysis Dataset.
 * [jtubespeech](https://github.com/sarulab-speech/jtubespeech) - JTubeSpeech: Corpus of Japanese speech collected from YouTube
 * [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) - List of frequently used words in Japanese Wikipedia.
 * [kokkosho_data](https://github.com/rindybell/kokkosho_data) - Dataset on vehicle malfunction information.
 * [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) - OCR learning dataset created for digital material OCR text conversion project.
 * [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) - A dataset of furigana created from the National Bibliographic Data.
 * [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) - Creating labels for self-made JVS (Japanese Versatile Speech) corpus.
 * [hirakanadic](https://github.com/po3rin/hirakanadic) - Allows Sudachi to normalize from hiragana to katakana from any compound word list
 * [animedb](https://github.com/anilogia/animedb) - Anime works list database spanning approximately 100 years.
 * [security_words](https://github.com/SaitoLab/security_words) - Japanese-English correspondence of public organizations related to cybersecurity.
 * [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) - Data of Japanese parliament members.
 * [honkoku-data](https://github.com/yuta1984/honkoku-data) - 歴史資料の市民参加型翻刻プラットフォーム「みんなで翻刻」のテキストデータ置き場です。 / Transcription texts created on Minna de Honkoku (https://honkoku.org), a crowdsourced transcription platform for historical Japanese documents.
 * [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) - データセット「wikiHow」（日本語版）
 * [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) - Engineer Vocabulary List in Japanese/English
 * [JSICK](https://github.com/verypluming/JSICK) - Japanese Sentences Involving Compositional Knowledge (JSICK) Dataset/JSICK-stress Test Set
 * [phishurl-list](https://github.com/JPCERTCC/phishurl-list) - Phishing URL dataset from JPCERT/CC
 * [jcms](https://github.com/shigashiyama/jcms) - A Japanese Corpus of Many Specialized Domains (JCMS)
 * [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) - text-only archives of www.aozora.gr.jp
 * [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) - friendly_JA is a parallel Japanese-to-Japanese corpus aimed at making Japanese easier by using the Latin/English derived katakana lexicon instead of the standard Sino-Japanese lexicon
 * [topokanji](https://github.com/scriptin/topokanji) - Topologically ordered lists of kanji for effective learning
 * [isbn4groups](https://github.com/uribo/isbn4groups) - Data related to Japanese publications in ISBN-13 format (978-4-XXXXXXXXX)
 * [NMeCab](https://github.com/komutan/NMeCab) - NMeCab: About Japanese morphological analyzer on .NET
 * [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) - Dataset of n-gram frequency statistics information from OCR text data created from digitized materials.
 * [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) - The complete set of source code for the NDL Ngram Viewer that was renewed in January 2023.
 * [data_set](https://github.com/japanese-law-analysis/data_set) - Dataset related to laws and precedents.
 * [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) - WRIME for huggingface datasets
 * [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) - NDL Classical Text OCR Learning Dataset (Collaborative Transcription and Processing Data)
 * [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) - GIS & Archaeological Simulator is currently in development and is expected to be released in 2023.
 * [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) - Japanese version of LIWC2015
 * [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) - Japanese Livedoor news corpus for huggingface datasets
 * [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) - JGLUE: Japanese General Language Understanding Evaluation for huggingface datasets
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality is a dataset created through crowdsourcing that reflects the commonsense morality of Japanese annotators.
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - COMET-ATOMIC yes
 * [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) - Dialogue Commonsense Graph in Japanese
 * [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) - "Proposal and Evaluation of Japanese Toxicity Schema" provides a schema and dataset for toxicity in the Japanese language.
 * [camera](https://github.com/CyberAgentAILab/camera) - CAMERA (CyberAgent Multimodal Evaluation for Ad Text GeneRAtion) is the Japanese ad text generation dataset.
 * [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) - Japanese Fake News Dataset
 * [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) - jpn_explainable_qa_dataset
 * [copa-japanese](https://github.com/nlp-titech/copa-japanese) - COPAデータセット（日本語）
 * [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) - Word Familiarity Rate for 'Word List by Semantic Principles (WLSP)'
 * [ProSub](https://github.com/matbahasa/ProSub) - A cross-linguistic study of pronoun substitutes and address terms
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality is a dataset created through crowdsourcing that reflects the commonsense morality of Japanese annotators.
 * [ramendb](https://github.com/nuko-yokohama/ramendb) - Scraping tool and collected data from Nantoka Database (https://supleks.jp/).
 * [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) - CAMERA (CyberAgent Multimodal Evaluation for Ad Text GeneRAtion) for huggingface datasets
 * [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) - FactCheckSentenceNLIデータセット
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - This is a dataset that has been translated into Japanese from the databricks-dolly-15k.jsonl file used for training in databricks/dolly-v2-12b.
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELD is an English-Japanese dataset for emotion-aware speech translation based on MELD.
 * [meconaudio](https://github.com/elith-co-jp/meconaudio) - Mecon Audio (Medical Conference Audio) is a dataset of read-out minutes for advanced medical conferences sponsored by the Ministry of Health, Labour and Welfare.
 * [japanese-addresses](https://github.com/geolonia/japanese-addresses) - Open data of address data at the town and block level nationwide (277,191 entries).
 * [aozorasearch](https://github.com/myokoym/aozorasearch) - The full-text search system for Aozora Bunko by Groonga. 青空文庫全文検索ライブラリ兼Webアプリ。
 * [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) - This repository contains scripts to reproduce the LLM-jp corpus.
 * [alpaca_ja](https://github.com/shi3z/alpaca_ja) - This is a Japanese version of the alpaca dataset.
 * [instruction_ja](https://github.com/megagonlabs/instruction_ja) - Japanese instruction data (日本語指示データ)
 * [japanese-family-names](https://github.com/siikamiika/japanese-family-names) - Top 5000 Japanese family names, with readings, ordered by frequency.
 * [kanji-data-media](https://github.com/kanjialive/kanji-data-media) - Japanese language data on kanji, radicals, media files, fonts and related resources from Kanji alive
 * [reazonspeech](https://github.com/reazon-research/reazonspeech) - Construct large-scale Japanese audio corpus at home
 * [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) - Data set of furigana created from Aozora Bunko and Sapie's braille data.
 * [koniwa](https://github.com/koniwa/koniwa) - An open collection of annotated voices in Japanese language
 * [JMMLU](https://github.com/nlp-waseda/JMMLU) - Japanese Massive Multitask Language Understanding Benchmark
 * [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) - Dataset of audio corpus with furigana annotations from Aozora Bunko
 * [jqara](https://github.com/hotchpotch/jqara) - JQaRA: Japanese Question Answering with Retrieval Augmentation - 検索拡張(RAG)評価のための日本語Q&Aデータセット
 * [jemhopqa](https://github.com/aiishii/jemhopqa) - JEMHopQA (Japanese Explainable Multi-hop Question Answering) is a Japanese multi-hop QA dataset that can evaluate internal reasoning.
 * [jacred](https://github.com/youmima/jacred) - Repository for Japanese Document-level Relation Extraction Dataset (plan to be released in March).
 * [jades](https://github.com/naist-nlp/jades) - JADES is a dataset for text simplification in Japanese, described in 'JADES: New Text Simplification Dataset in Japanese Targeted at Non-Native Speakers' (the paper will be available soon).
 * [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) - A safety evaluation dataset "Do-Not-Answer" released by the University of Melbourne in August 2023 has been automatically translated into Japanese for use in the evaluation of Japanese LLM, and further modified to take into account Japanese culture.
 * [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) - This is a dataset that translates OpenAssistant's open source data OASST1 into Japanese.
 * [jacwir](https://github.com/hotchpotch/jacwir) - JaCWIR: Japanese Casual Web IR Small-scale and casual web title and abstract dataset for Japanese information retrieval evaluation.
 * [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) - Comparison table of commonly used katakana and original words in the science and technology industry for Japanese language learners.
 * [j-unimorph](https://github.com/cl-tohoku/j-unimorph) - Dataset of UniMorph in Japanese
 * [GazeVQA](https://github.com/riken-grp/GazeVQA) - Dataset for the LREC-COLING 2024 paper A Gaze-grounded Visual Question Answering Dataset for Clarifying Ambiguous Japanese Questions
 * [J-CRe3](https://github.com/riken-grp/J-CRe3) - Code for J-CRe3 experiments (Ueda et al., LREC-COLING, 2024)
 * [jmed-llm](https://github.com/sociocom/jmed-llm) - JMED-LLM: Japanese Medical Evaluation Dataset for Large Language Models
 * [lawtext](https://github.com/yamachig/lawtext) - Plain text format for Japanese law
 * [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) - OCR learning dataset created in OCR processing program research and development project.
 * [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) - Evaluation set for resolving semantic ambiguity based on topics
 * [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) - Jamp: Controlled Japanese Temporal Inference Dataset for Evaluating Generalization Capacity of Language Models
 * [JSeM](https://github.com/DaisukeBekki/JSeM) - 日本語意味テストスイート（FraCaSの対応および拡張）
 * [niilc-qa](https://github.com/mynlp/niilc-qa) - NIILC QA data
 * [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) - Dataset of paper Verification of Chain-of-Thought Prompting in Japanese
 * [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) - This is a Japanese text corpus that consists of Wikipedia articles with various linguistic annotations.
 * [elaws-history](https://github.com/kissge/elaws-history) - We regularly download and archive all legal data distributed through the e-Gov legal search.
 * [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) - Japanese-RP-Bench is a benchmark for measuring LLM's Japanese role-playing ability.
 * [hdic](https://github.com/shikeda/hdic) - HDIC : Integrated Database of Hanzi Dictionaries in Early Japan
 * [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) - Awesome Japan Open Data - List and Summary of Open Data Information in Japan
 * [kanji-data](https://github.com/mimneko/kanji-data) - Commonly used kanji table, data related to kanji
 * [openchj-genji](https://github.com/togiso/openchj-genji) - "The Tale of Genji" morphological information data
 * [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) - This repository contains data for our paper AdParaphrase: Paraphrase Dataset for Analyzing Linguistic Features toward Generating Attractive Ad Texts.
 * [Jamp_sp](https://github.com/ynklab/Jamp_sp) - アスペクトを考慮した日本語時間推論データセットの構築（Jamp_sp: Controlled Japanese Temporal Inference Dataset Considering Aspect）
 * [jnli-neg](https://github.com/asahi-y/jnli-neg) - This is the public repository for the Japanese Natural Language Inference Dataset for Evaluating Negative Understanding Ability (JNLI-Neg).
 * [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) - This repository provides Python implementation for building Swallow Corpus Version 1, a large Japanese web corpus (Okazaki et al., 2024), from Common Crawl archives.
 * [jalecon](https://github.com/naist-nlp/jalecon) - A Dataset of Japanese Lexical Complexity for Non-Native Readers
 * [multils-japanese](https://github.com/naist-nlp/multils-japanese) - MultiLS-Japanese Lexical Complexity Prediction and Lexical Simplification Dataset for Japanese: annotator profiles, unaggregated annotation, and annotatation guidelines.
 * [nwjc](https://github.com/masayu-a/nwjc) - NINJAL Web Japanese Corpus
 * [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) - Dataset introduced in the paper Towards Fully Automated Manga Translation presented in AAAI21
 * [public-annotations](https://github.com/manga109/public-annotations) - Various annotations of Manga109 dataset
 * [gimei](https://github.com/willnet/gimei) - random Japanese name and address generator
 * [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) - Test set to evaluate the safety behavior of Japanese language models
 * [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) - A simple, open-source collection of Japanese onomatopoeic and mimetic sound words in JSON format. With manga samples.
 * [kanji](https://github.com/sylhare/kanji) - List of Japanese Kanji Radicals to Learn
 * [jethics](https://github.com/language-media-lab/jethics) - Overview page of the Japanese Ethical Understanding Evaluation Dataset JETHICS (to be updated)
 * [waon](https://github.com/llm-jp/waon) - WAON: Large-Scale and High-Quality Japanese Image-Text Dataset for Vision-Language Models
 * [kuci](https://github.com/ku-nlp/kuci) - Kyoto University Commonsense Inference dataset (KUCI)
 * [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) - Test dataset of difficult-to-parse Japanese addresses
 * [jlpt-word-list](https://github.com/elzup/jlpt-word-list) - Japanese word list from JLPT vocabulary
 * [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) - Text image dataset (Hiragana 73 characters version)
 * [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) - Multiple-choice QA dataset on Japanese regulations
 * [yjcaptions](https://github.com/yahoojapan/yjcaptions) - YJ Captions 26k Dataset
 * [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) - 日本のビジュアルジェノムVQAデータセット
 * [lawhub](https://github.com/lwhb/lawhub) - Repository to track Japanese Law in text format
 * [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) - A word frequency list derived from subtitles from Japanese drama, anime and films.
 * [jconj](https://github.com/yamagoya/jconj) - A table-based Japanese word conjugator
 * [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) - Extracts personal names in Wikipedia Japanese.
 * [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) - Frequency dictionary for yomichan based on the Corpus of Everyday Japanese Conversation dataset
 * [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) - Wikipedia Bilingual Reference Data (English)
 * [ajimee-bench](https://github.com/azookey/ajimee-bench) - AJIMEE-Bench (Advanced Japanese IME Evaluation Benchmark)
 * [j-spaw](https://github.com/takamichi-lab/j-spaw) - J-SpAW: Japanese speech corpus for speaker verification and anti-spoofing
 * [camera3](https://github.com/cyberagentailab/camera3) - CAMERA3: An Evaluation Dataset for Controllable Ad Text Generation in Japanese
 * [jgpqa](https://github.com/llm-jp/jgpqa) - Japanese translation of the GPQA dataset
 * [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) - Removing noise from the Tanaka Corpus.
 * [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) - Japanese emotion corpus Tokushima Univ. A-2 Lab.
 * [osworld-jp](https://github.com/karakuri-ai/osworld-jp) - Japanese Version Computer Use Benchmark for Language Consideration Evaluation
 * [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) - Quasi Japanese Reviews (Pseudo Review Data)
 * [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) - Psychiatric initial consultation medical record creation questionnaire dataset
 * [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) - Table of correspondence between old place names that have disappeared due to municipal mergers and new place names.
 * [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) - Japanese text-emoticon data.
 * [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) - 聞き間違えコーパス︱CSV＋Table Schema で約 1 万件を管理し、VS Code＋pre-commit＋Frictionless＋GitHub Actions で自動検証を行う日本語データセット
 * [kotowaza](https://github.com/septn/kotowaza) - Structured JSON dataset of Japanese proverbs (kotowaza) with meanings in Indonesian & English, examples, JLPT levels, and tags.
 * [selective-rag-kasensabo](https://github.com/tk-yasuno/selective-rag-kasensabo) - This is a practical Agentic RAG system MVP that accurately automatically determines the expertise granularity (fine/coarse) of questions related to construction technology standards at 96% and selects the optimal RAG system (ColBERT/Naive). Four RAG systems were built targeting the technical standards of river sand control dams published in November 2025, and accuracy and speed were compared for 200 questions with different granularity of expertise.
 * [jmle2026-bench](https://github.com/naoto-iwase/jmle2026-bench) - LLM benchmark on the 120th Japanese Medical Licensing Examination (Feb 7-8, 2026)
 * [JSTS-Neg](https://github.com/reiko-y/JSTS-Neg) - This is a public repository for the Japanese Semantic Textual Similarity calculation dataset JSTS-Neg, which is used to evaluate negative comprehension ability. JSTS-Neg was created by extending the language inference dataset JSTS included in JGLUE.
 * [business-slide-questions](https://github.com/stockmarkteam/business-slide-questions) - In this repository, we provide a Visual Question Answering (VQA) benchmark called "BusinessSlideVQA" targeting business documents (slides).
 * [WLSP-antonym](https://github.com/masayu-a/WLSP-antonym) - Antonym relations for 'Word List by Semantic Principles (WLSP)'
 * [YouCook2-JP](https://github.com/nlab-mpg/YouCook2-JP) - Japanese translation of the YouCook2 dataset.
 * [E2U](https://github.com/sociocom/E2U) - Data on the spread of transformation
 * [annotation-2025](https://github.com/Tiny-Colony/annotation-2025) - This repository is for releasing data that allows for comparing the "interpretation" of text between manual and LLM outputs.
 * [jhpt](https://github.com/nict-astrec-att/jhpt) - This is a parallel dataset that aligns original texts of historical Japanese language materials with modern language translations (reference translations) on a segment-by-segment basis. Please refer to the paper for more details.
 * [JBE-QA](https://github.com/hancules/JBE-QA) - Japanese Bar Exam QA
 * [j-spaw](https://github.com/takamichi-lab/j-spaw) - J-SpAW: Japanese speech corpus for speaker verification and anti-spoofing
 * [JMedWiC](https://github.com/EhimeNLP/JMedWiC) - Using a masked language model, we automatically extracted pseudo-synonymous and non-synonymous pairs, and determined labels through manual synonym annotation to construct a dataset for determining word sense identity in the Japanese medical field.
 * [jhpt](https://github.com/nict-astrec-att/jhpt) - This is a parallel dataset that aligns original texts of historical Japanese language materials with modern language translations (reference translations) on a segment-by-segment basis. Please refer to the paper for more details.
 * [Doppelganger-JC](https://github.com/0017-alt/Doppelganger-JC) - This is a dataset benchmarking the misuse of cross-lingual homographs between Chinese and Japanese in LLMs.
 * [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) - VLM Evaluation Benchmark for Understanding Software Diagrams (Japanese, English, Korean supported)
 * [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) - Performance evaluation benchmark of Long Context LLM in the Japanese HR domain.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) | - | - | ⭐ 77 | 🔴 june 2023|
| 🔗 [kanji-data](https://github.com/davidluzgouveia/kanji-data) | - | - | ⭐ 208 | 🟢 february|
| 🔗 [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) | - | - | ⭐ 102 | 🔴 december 2021|
| 🔗 [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) | - | - | ⭐ 32 | 🔴 march 2017|
| 🔗 [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) | - | - | ⭐ 140 | 🔴 september 2018|
| 🔗 [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) | - | - | ⭐ 110 | 🔴 january 2022|
| 🔗 [JaNLI](https://github.com/verypluming/JaNLI) | - | - | ⭐ 17 | 🔴 may 2023|
| 🔗 [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) | - | - | ⭐ 18 | 🔴 december 2020|
| 🔗 [emoji-ja](https://github.com/yagays/emoji-ja) | - | - | ⭐ 83 | 🔴 march 2025|
| 🔗 [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) | - | - | ⭐ 35 | 🔴 march 2020|
| 🔗 [ja.text8](https://github.com/Hironsan/ja.text8) | - | - | ⭐ 111 | 🔴 october 2017|
| 🔗 [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) | - | - | ⭐ 31 | 🔴 april 2018|
| 🔗 [japanese](https://github.com/hingston/japanese) | - | - | ⭐ 87 | 🔴 september 2018|
| 🔗 [kanji-frequency](https://github.com/scriptin/kanji-frequency) | - | - | ⭐ 156 | 🟢 yesterday|
| 🔗 [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) | - | - | ⭐ 24 | 🔴 january 2021|
| 🔗 [CoARiJ](https://github.com/chakki-works/CoARiJ) | - | - | ⭐ 94 | 🔴 december 2020|
| 🔗 [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) | - | - | ⭐ 26 | 🔴 july 2023|
| 🔗 [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) | - | - | ⭐ 5 | 🔴 august 2021|
| 🔗 [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) | - | - | ⭐ 78 | 🔴 april 2024|
| 🔗 [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) | - | - | ⭐ 204 | 🔴 december 2021|
| 🔗 [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) | - | - | ⭐ 106 | 🟢 yesterday|
| 🔗 [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) | - | - | ⭐ 177 | 🟢 yesterday|
| 🔗 [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) | - | - | ⭐ 90 | 🔴 july 2018|
| 🔗 [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) | - | - | ⭐ 6 | 🔴 january 2019|
| 🔗 [speechBSD](https://github.com/ku-nlp/speechBSD) | - | - | ⭐ 3 | 🔴 february 2024|
| 🔗 [ita-corpus](https://github.com/mmorise/ita-corpus) | - | - | ⭐ 223 | 🟢 march|
| 🔗 [rohan4600](https://github.com/mmorise/rohan4600) | - | - | ⭐ 68 | 🟢 march|
| 🔗 [anlp-jp-history](https://github.com/whym/anlp-jp-history) | - | - | ⭐ 3 | 🔴 april 2024|
| 🔗 [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) | - | - | ⭐ 21 | 🔴 november 2022|
| 🔗 [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) | - | - | ⭐ 19 | 🔴 january 2021|
| 🔗 [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) | - | - | ⭐ 4 | 🔴 november 2018|
| 🔗 [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) | - | - | ⭐ 6 | 🔴 january 2020|
| 🔗 [wrime](https://github.com/ids-cv/wrime) | - | - | ⭐ 174 | 🟡 september 2025|
| 🔗 [jtubespeech](https://github.com/sarulab-speech/jtubespeech) | - | - | ⭐ 229 | 🔴 march 2023|
| 🔗 [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) | - | - | ⭐ 2 | 🔴 april 2022|
| 🔗 [kokkosho_data](https://github.com/rindybell/kokkosho_data) | - | - | ⭐ 1 | 🔴 july 2019|
| 🔗 [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) | - | - | ⭐ 83 | 🔴 june 2024|
| 🔗 [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) | - | - | ⭐ 31 | 🔴 september 2021|
| 🔗 [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) | - | - | ⭐ 31 | 🔴 february 2021|
| 🔗 [hirakanadic](https://github.com/po3rin/hirakanadic) | 📥 51 | 📦 14k | ⭐ 7 | 🔴 july 2023|
| 🔗 [animedb](https://github.com/anilogia/animedb) | - | - | ⭐ 329 | 🔴 january 2023|
| 🔗 [security_words](https://github.com/SaitoLab/security_words) | - | - | ⭐ 27 | 🔴 august 2023|
| 🔗 [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [honkoku-data](https://github.com/yuta1984/honkoku-data) | - | - | ⭐ 17 | 🟢 march|
| 🔗 [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) | - | - | ⭐ 35 | 🔴 december 2020|
| 🔗 [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) | - | - | ⭐ 1.9k | 🔴 november 2020|
| 🔗 [JSICK](https://github.com/verypluming/JSICK) | - | - | ⭐ 45 | 🔴 may 2023|
| 🔗 [phishurl-list](https://github.com/JPCERTCC/phishurl-list) | - | - | ⭐ 204 | 🟢 march|
| 🔗 [jcms](https://github.com/shigashiyama/jcms) | - | - | ⭐ 9 | 🔴 november 2022|
| 🔗 [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) | - | - | ⭐ 88 | 🔴 march 2023|
| 🔗 [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [topokanji](https://github.com/scriptin/topokanji) | - | - | ⭐ 200 | 🔴 january 2016|
| 🔗 [isbn4groups](https://github.com/uribo/isbn4groups) | - | - | ⭐ 1 | 🔴 june 2024|
| 🔗 [NMeCab](https://github.com/komutan/NMeCab) | - | - | ⭐ 98 | 🔴 march 2024|
| 🔗 [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) | - | - | ⭐ 15 | 🔴 january 2023|
| 🔗 [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) | - | - | ⭐ 3 | 🔴 july 2023|
| 🔗 [data_set](https://github.com/japanese-law-analysis/data_set) | - | - | ⭐ 50 | 🔴 january 2025|
| 🔗 [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) | - | - | ⭐ 4 | 🔴 january 2023|
| 🔗 [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) | - | - | ⭐ 20 | 🟢 march|
| 🔗 [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) | - | - | ⭐ 181 | 🟡 december 2025|
| 🔗 [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) | - | - | ⭐ 2 | 🔴 october 2023|
| 🔗 [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) | - | - | ⭐ 12 | 🔴 march 2025|
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 | 🟡 november 2025|
| 🔗 [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) | - | - | ⭐ 31 | 🔴 march 2024|
| 🔗 [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) | - | - | ⭐ 6 | 🔴 march 2023|
| 🔗 [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) | - | - | ⭐ 21 | 🔴 january 2023|
| 🔗 [camera](https://github.com/CyberAgentAILab/camera) | - | - | ⭐ 26 | 🔴 august 2024|
| 🔗 [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) | - | - | ⭐ 20 | 🔴 may 2021|
| 🔗 [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [copa-japanese](https://github.com/nlp-titech/copa-japanese) | - | - | ⭐ 1 | 🔴 february 2023|
| 🔗 [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) | - | - | ⭐ 12 | 🔴 january 2025|
| 🔗 [ProSub](https://github.com/matbahasa/ProSub) | - | - | ⭐ 5 | 🟡 april 2025|
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 | 🟡 november 2025|
| 🔗 [ramendb](https://github.com/nuko-yokohama/ramendb) | - | - | ⭐ 7 | 🟢 march|
| 🔗 [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) | - | - | ⭐ 3 | 🔴 march 2023|
| 🔗 [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) | - | - | ⭐ 0 | 🔴 march 2021|
| 🔗 [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) | - | - | ⭐ 89 | 🔴 july 2023|
| 🔗 [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) | - | - | ⭐ 0 | 🔴 june 2023|
| 🔗 [meconaudio](https://github.com/elith-co-jp/meconaudio) | - | - | ⭐ 9 | 🔴 october 2023|
| 🔗 [japanese-addresses](https://github.com/geolonia/japanese-addresses) | - | - | ⭐ 761 | 🟡 december 2025|
| 🔗 [aozorasearch](https://github.com/myokoym/aozorasearch) | - | - | ⭐ 21 | 🟢 yesterday|
| 🔗 [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) | - | - | ⭐ 44 | 🔴 october 2023|
| 🔗 [alpaca_ja](https://github.com/shi3z/alpaca_ja) | - | - | ⭐ 86 | 🔴 may 2023|
| 🔗 [instruction_ja](https://github.com/megagonlabs/instruction_ja) | - | - | ⭐ 24 | 🔴 july 2023|
| 🔗 [japanese-family-names](https://github.com/siikamiika/japanese-family-names) | - | - | ⭐ 18 | 🔴 june 2017|
| 🔗 [kanji-data-media](https://github.com/kanjialive/kanji-data-media) | - | - | ⭐ 406 | 🔴 november 2023|
| 🔗 [reazonspeech](https://github.com/reazon-research/reazonspeech) | - | - | ⭐ 374 | 🟢 january|
| 🔗 [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) | - | - | ⭐ 22 | 🔴 january 2024|
| 🔗 [koniwa](https://github.com/koniwa/koniwa) | - | - | ⭐ 57 | 🟡 april 2025|
| 🔗 [JMMLU](https://github.com/nlp-waseda/JMMLU) | - | - | ⭐ 38 | 🟡 october 2025|
| 🔗 [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) | - | - | ⭐ 48 | 🔴 march 2025|
| 🔗 [jqara](https://github.com/hotchpotch/jqara) | - | - | ⭐ 43 | 🟡 september 2025|
| 🔗 [jemhopqa](https://github.com/aiishii/jemhopqa) | - | - | ⭐ 30 | 🟡 april 2025|
| 🔗 [jacred](https://github.com/youmima/jacred) | - | - | ⭐ 7 | 🔴 march 2024|
| 🔗 [jades](https://github.com/naist-nlp/jades) | - | - | ⭐ 0 | 🔴 december 2022|
| 🔗 [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) | - | - | ⭐ 24 | 🔴 december 2023|
| 🔗 [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) | - | - | ⭐ 16 | 🔴 november 2023|
| 🔗 [jacwir](https://github.com/hotchpotch/jacwir) | - | - | ⭐ 8 | 🟡 september 2025|
| 🔗 [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) | - | - | ⭐ 3 | 🔴 november 2024|
| 🔗 [j-unimorph](https://github.com/cl-tohoku/j-unimorph) | - | - | ⭐ 9 | 🟢 january|
| 🔗 [GazeVQA](https://github.com/riken-grp/GazeVQA) | - | - | ⭐ 0 | 🔴 september 2024|
| 🔗 [J-CRe3](https://github.com/riken-grp/J-CRe3) | - | - | ⭐ 9 | 🔴 january 2025|
| 🔗 [jmed-llm](https://github.com/sociocom/jmed-llm) | - | - | ⭐ 56 | 🔴 september 2024|
| 🔗 [lawtext](https://github.com/yamachig/lawtext) | - | - | ⭐ 92 | 🟢 january|
| 🔗 [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) | - | - | ⭐ 15 | 🔴 june 2024|
| 🔗 [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) | - | - | ⭐ 2 | 🔴 september 2018|
| 🔗 [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [JSeM](https://github.com/DaisukeBekki/JSeM) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [niilc-qa](https://github.com/mynlp/niilc-qa) | - | - | ⭐ 18 | 🔴 november 2015|
| 🔗 [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) | - | - | ⭐ 5 | 🔴 september 2023|
| 🔗 [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) | - | - | ⭐ 29 | 🟢 february|
| 🔗 [elaws-history](https://github.com/kissge/elaws-history) | - | - | ⭐ 5 | 🟢 yesterday|
| 🔗 [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) | - | - | ⭐ 18 | 🔴 september 2024|
| 🔗 [hdic](https://github.com/shikeda/hdic) | - | - | ⭐ 40 | 🟢 last wednesday|
| 🔗 [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) | - | - | ⭐ 159 | 🟢 last tuesday|
| 🔗 [kanji-data](https://github.com/mimneko/kanji-data) | - | - | ⭐ 18 | 🟢 february|
| 🔗 [openchj-genji](https://github.com/togiso/openchj-genji) | - | - | ⭐ 2 | 🔴 march 2025|
| 🔗 [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) | - | - | ⭐ 1 | 🟡 may 2025|
| 🔗 [Jamp_sp](https://github.com/ynklab/Jamp_sp) | - | - | ⭐ 0 | 🔴 june 2024|
| 🔗 [jnli-neg](https://github.com/asahi-y/jnli-neg) | - | - | ⭐ 0 | 🟡 december 2025|
| 🔗 [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) | - | - | ⭐ 5 | 🔴 november 2024|
| 🔗 [jalecon](https://github.com/naist-nlp/jalecon) | - | - | ⭐ 5 | 🔴 july 2023|
| 🔗 [multils-japanese](https://github.com/naist-nlp/multils-japanese) | - | - | ⭐ 0 | 🟢 january|
| 🔗 [nwjc](https://github.com/masayu-a/nwjc) | - | - | ⭐ 10 | 🔴 april 2022|
| 🔗 [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) | - | - | ⭐ 199 | 🔴 march 2023|
| 🔗 [gimei](https://github.com/willnet/gimei) | - | - | ⭐ 424 | 🟢 january|
| 🔗 [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) | - | - | ⭐ 9 | 🟡 july 2025|
| 🔗 [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) | - | - | ⭐ 7 | 🟢 march|
| 🔗 [kanji](https://github.com/sylhare/kanji) | - | - | ⭐ 28 | 🟢 march|
| 🔗 [jethics](https://github.com/language-media-lab/jethics) | - | - | ⭐ 2 | 🟡 june 2025|
| 🔗 [waon](https://github.com/llm-jp/waon) | - | - | ⭐ 6 | 🟡 november 2025|
| 🔗 [kuci](https://github.com/ku-nlp/kuci) | - | - | ⭐ 5 | 🔴 february 2024|
| 🔗 [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [jlpt-word-list](https://github.com/elzup/jlpt-word-list) | - | - | ⭐ 62 | 🔴 february 2022|
| 🔗 [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) | - | - | ⭐ 18 | 🔴 april 2020|
| 🔗 [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) | - | - | ⭐ 265 | 🟢 february|
| 🔗 [yjcaptions](https://github.com/yahoojapan/yjcaptions) | - | - | ⭐ 60 | 🔴 november 2016|
| 🔗 [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) | - | - | ⭐ 30 | 🔴 november 2018|
| 🔗 [lawhub](https://github.com/lwhb/lawhub) | - | - | ⭐ 152 | 🔴 november 2020|
| 🔗 [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) | - | - | ⭐ 39 | 🔴 december 2023|
| 🔗 [jconj](https://github.com/yamagoya/jconj) | - | - | ⭐ 35 | 🔴 may 2020|
| 🔗 [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) | - | - | ⭐ 21 | 🔴 december 2022|
| 🔗 [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) | - | - | ⭐ 11 | 🔴 june 2023|
| 🔗 [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) | - | - | ⭐ 5 | 🔴 june 2016|
| 🔗 [ajimee-bench](https://github.com/azookey/ajimee-bench) | - | - | ⭐ 19 | 🔴 january 2025|
| 🔗 [j-spaw](https://github.com/takamichi-lab/j-spaw) | - | - | ⭐ 5 | 🟡 august 2025|
| 🔗 [camera3](https://github.com/cyberagentailab/camera3) | - | - | ⭐ 4 | 🔴 may 2024|
| 🔗 [jgpqa](https://github.com/llm-jp/jgpqa) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) | - | - | ⭐ 2 | 🔴 june 2021|
| 🔗 [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) | - | - | ⭐ 2 | 🔴 september 2024|
| 🔗 [osworld-jp](https://github.com/karakuri-ai/osworld-jp) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) | - | - | ⭐ 1 | 🟡 october 2025|
| 🔗 [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) | - | - | ⭐ 1 | 🔴 may 2022|
| 🔗 [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) | - | - | ⭐ 1 | 🔴 march 2021|
| 🔗 [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) | - | - | ⭐ 1 | 🟢 january|
| 🔗 [kotowaza](https://github.com/septn/kotowaza) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [selective-rag-kasensabo](https://github.com/tk-yasuno/selective-rag-kasensabo) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [jmle2026-bench](https://github.com/naoto-iwase/jmle2026-bench) | - | - | ⭐ 10 | 🟢 march|
| 🔗 [JSTS-Neg](https://github.com/reiko-y/JSTS-Neg) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [business-slide-questions](https://github.com/stockmarkteam/business-slide-questions) | - | - | ⭐ 2 | 🟡 may 2025|
| 🔗 [WLSP-antonym](https://github.com/masayu-a/WLSP-antonym) | - | - | ⭐ 0 | 🔴 march 2021|
| 🔗 [YouCook2-JP](https://github.com/nlab-mpg/YouCook2-JP) | - | - | ⭐ 0 | 🟡 august 2025|
| 🔗 [E2U](https://github.com/sociocom/E2U) | - | - | ⭐ 0 | 🟢 march|
| 🔗 [annotation-2025](https://github.com/Tiny-Colony/annotation-2025) | - | - | ⭐ 0 | 🟢 january|
| 🔗 [jhpt](https://github.com/nict-astrec-att/jhpt) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [JBE-QA](https://github.com/hancules/JBE-QA) | - | - | ⭐ 0 | 🟡 november 2025|
| 🔗 [j-spaw](https://github.com/takamichi-lab/j-spaw) | - | - | ⭐ 5 | 🟡 august 2025|
| 🔗 [JMedWiC](https://github.com/EhimeNLP/JMedWiC) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [jhpt](https://github.com/nict-astrec-att/jhpt) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [Doppelganger-JC](https://github.com/0017-alt/Doppelganger-JC) | - | - | ⭐ 1 | 🟢 january|
| 🔗 [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) | - | - | ⭐ 1 | 🟢 last monday|
| 🔗 [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) | - | - | ⭐ 1 | 🟢 january|


## Tutorial
Guides and tutorials for learning Japanese NLP tools and techniques

 * [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) - spaCy tutorial in English and Japanese. spacy-transformers, BERT, GiNZA.
 * [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) - Tutorial to train fastText with Japanese corpus
 * [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) - AllenNLP-NER-ja: Named Entity Recognition for Japanese using AllenNLP
 * [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) - Experiment for Japanese Text classification using chariot and PyTorch
 * [ginza-examples](https://github.com/poyo46/ginza-examples) - Introduction to the Japanese NLP library GiNZA
 * [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) - DocumentClassificationUsingBERT-Japanese
 * [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) - Google Colaboratoryで日本語のBERTを動かす方法です。
 * [bert-book](https://github.com/stockmarkteam/bert-book) - "Introduction to Natural Language Processing with BERT: Practical Programming using Transformers" Support Page.
 * [janome-tutorial](https://github.com/mocobeta/janome-tutorial) - This is an introductory tutorial on text mining using Janome.
 * [handson-language-models](https://github.com/hnishi/handson-language-models) - This is a hands-on material for a Japanese language model.
 * [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) - Trying Japanese text inference on Google Colab.
 * [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) - deep-learning-with-pytorchの日本語版repositoryです。
 * [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) -【2023年版】BERTによるテキスト分類
 * [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) - This is the support page for "Natural Language Processing with Deep Learning" (published by Kyoritsu Shuppan)
 * [llm-book](https://github.com/ghmagazine/llm-book) - GitHub repository for "Introduction to Large-scale Language Models" (Gijutsu-Hyoronsha, 2023)
 * [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) - NLP2024 Tutorial 3 Creating and Learning a Large-Scale Japanese Language Model - Environment Setup Procedure and Source Code
 * [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) - Japanese Information Retrieval Tutorial
 * [nlpbook](https://github.com/mamorlis/nlpbook) - "Natural Language Processing Textbook" Support Site
 * [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) - Regular Expression Engine for Creating and Learning
 * [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) - Text classification using BERT in the 2024 version
 * [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) - Fine-Tuning Google Gemma for Japanese Instructions
 * [nlp100v2020](https://github.com/upura/nlp100v2020) - Solving "Language Processing 100 Knock 2020" with Python
 * [textmining-ja](https://github.com/paithiov909/textmining-ja) - Practice of natural language processing and text analysis using R
 * [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) - Tutorial materials and source code for "Introduction to Geographic Information and Language Processing in Practice" in NLP2025.
 * [nlp100v2025](https://github.com/upura/nlp100v2025) - Solving "Language Processing 100 Knock 2025" with Python
 * [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) - Notes on "Topic Model" (Machine Learning Professional Series)
 * [slp2025](https://github.com/ryota-komatsu/slp2025) -音学シンポジウム2025チュートリアル「マルチモーダル大規模言語モデル入門」資料
 * [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) - Impress Corporation "IT Fundamentals: Natural Language Processing & Image Analysis"
 * [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) - Source code used in the book "Practical Introduction to Generative AI Agents for Practical Use on the Field" (Kodansha Scientific Co., Ltd.)
 * [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) - 2024 Rikkyo University Graduate School Artificial Intelligence Science Research Department Special Lecture on Natural Language Processing
 * [support-genai-book](https://github.com/yoheikikuta/support-genai-book) - This is the support page for "Generating AI Unraveled from the Original Paper" (published by Gijutsu-Hyohron Co., Ltd.).
 * [ir100](https://github.com/ir100/ir100) - Information Retrieval 100 Knockouts
 * [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) - Support site for "Introduction to Large-scale Language Models with Kaggle - Practical Programming for Natural Language Processing"


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) | - | - | ⭐ 64 | 🔴 january 2020|
| 🔗 [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) | - | - | ⭐ 205 | 🔴 september 2016|
| 🔗 [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) | - | - | ⭐ 5 | 🔴 may 2022|
| 🔗 [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) | - | - | ⭐ 5 | 🔴 march 2019|
| 🔗 [ginza-examples](https://github.com/poyo46/ginza-examples) | - | - | ⭐ 15 | 🔴 january 2021|
| 🔗 [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) | - | - | ⭐ 0 | 🟡 august 2025|
| 🔗 [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) | - | - | ⭐ 29 | 🔴 january 2022|
| 🔗 [bert-book](https://github.com/stockmarkteam/bert-book) | - | - | ⭐ 264 | 🔴 february 2024|
| 🔗 [janome-tutorial](https://github.com/mocobeta/janome-tutorial) | - | - | ⭐ 31 | 🔴 march 2019|
| 🔗 [handson-language-models](https://github.com/hnishi/handson-language-models) | - | - | ⭐ 3 | 🔴 march 2021|
| 🔗 [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) | - | - | ⭐ 6 | 🔴 june 2021|
| 🔗 [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) | - | - | ⭐ 143 | 🔴 may 2021|
| 🔗 [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) | - | - | ⭐ 235 | 🔴 may 2024|
| 🔗 [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) | - | - | ⭐ 10 | 🔴 may 2023|
| 🔗 [llm-book](https://github.com/ghmagazine/llm-book) | - | - | ⭐ 467 | 🟡 december 2025|
| 🔗 [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) | - | - | ⭐ 113 | 🔴 april 2024|
| 🔗 [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) | - | - | ⭐ 3 | 🔴 june 2024|
| 🔗 [nlpbook](https://github.com/mamorlis/nlpbook) | - | - | ⭐ 14 | 🟡 april 2025|
| 🔗 [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) | - | - | ⭐ 22 | 🔴 march 2024|
| 🔗 [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) | - | - | ⭐ 30 | 🔴 july 2024|
| 🔗 [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) | - | - | ⭐ repo not found | 🔴 august 2024|
| 🔗 [nlp100v2020](https://github.com/upura/nlp100v2020) | - | - | ⭐ 90 | 🟡 april 2025|
| 🔗 [textmining-ja](https://github.com/paithiov909/textmining-ja) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) | - | - | ⭐ 17 | 🟢 february|
| 🔗 [nlp100v2025](https://github.com/upura/nlp100v2025) | - | - | ⭐ 90 | 🟡 april 2025|
| 🔗 [public-annotations](https://github.com/manga109/public-annotations) | - | - | ⭐ 13 | 🟡 april 2025|
| 🔗 [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) | - | - | ⭐ 4 | 🟡 may 2025|
| 🔗 [slp2025](https://github.com/ryota-komatsu/slp2025) | - | - | ⭐ 63 | 🟢 last tuesday|
| 🔗 [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) | - | - | ⭐ 4 | 🟡 june 2025|
| 🔗 [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) | - | - | ⭐ 193 | 🟡 september 2025|
| 🔗 [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [support-genai-book](https://github.com/yoheikikuta/support-genai-book) | - | - | ⭐ 91 | 🟢 january|
| 🔗 [ir100](https://github.com/ir100/ir100) | - | - | ⭐ 93 | 🟡 december 2025|
| 🔗 [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) | - | - | ⭐ 27 | 🟢 march|


## Research summary
Summaries of studies and papers in Japanese NLP research

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - A list of pre-trained BERT models for Japanese with word/subword tokenization + vocabulary construction algorithm information
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - Repository for collecting and categorizing Japanese literature on correcting grammar errors.
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - lists of text corpus and more (mainly Japanese)
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - A playbook for systematically maximizing the performance of deep learning models.
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - Trying to consolidate japanese phonetic, and in particular pitch accent resources into one list
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - Summary of Japanese LLM (Open Source)


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) | - | - | ⭐ 131 | 🔴 march 2023|
| 🔗 [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) | - | - | ⭐ 13 | 🟡 april 2025|
| 🔗 [dataset-list](https://github.com/ikegami-yukino/dataset-list) | - | - | ⭐ 118 | 🔴 july 2024|
| 🔗 [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) | - | - | ⭐ 190 | 🔴 january 2023|
| 🔗 [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) | - | - | ⭐ 126 | 🔴 february 2024|
| 🔗 [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) | - | - | ⭐ 1.4k | 🟢 today|


## Reference

 * [自然言語処理の餅屋](https://www.jnlp.org/nlp/top)
 * [yasuokaの日記： 日本語係り受け解析器「2020年の総ざらえ」](https://srad.jp/~yasuoka/journal/643631/)
 * [yasuokaの日記： 日本語係り受け解析器「2021年の総ざらえ」](https://srad.jp/~yasuoka/journal/651542/)
 * https://github.com/topics/japanese?l=python
 * https://github.com/topics/japanese-language?l=python
 * https://github.com/search?o=desc&q=corpus+japanese&s=&type=Repositories
 * https://paperswithcode.com/datasets?lang=japanese
 * https://github.com/himkt/awesome-bert-japanese
 * [Awesome-Rust-MachineLearning-日本語向けのrustクレートや記事等をまとめたもの](https://github.com/vaaaaanquish/Awesome-Rust-MachineLearning/blob/main/README.ja.md)
 * [大規模言語モデル入門Ⅱ 〜生成型LLMの実装と評価](https://gihyo.jp/book/2024/978-4-297-14393-0)


## Contributors

 * [kaisugi](https://github.com/kaisugi) - [website](https://kaisugi.me)
 * [bomin0624](https://github.com/bomin0624) - [twitter](https://twitter.com/bomin0624_c)
 * [passaglia](https://github.com/passaglia) - [twitter](https://twitter.com/SamPassaglia)
 * [sarumaj](https://github.com/sarumaj) - [github](https://github.com/sarumaj)
 * [ln2058](https://github.com/ln2058) - [github](https://github.com/ln2058)
 * [ajtgjmdjp](https://github.com/ajtgjmdjp) - [github](https://github.com/ajtgjmdjp)
