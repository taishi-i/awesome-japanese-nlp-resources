# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of resources dedicated to Python libraries, llms, dictionaries, and corpora of NLP for Japanese

- Listed information on [739 GitHub repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md)
- Listed information on [2152 Hugging Face repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md) (models and datasets)
- Released [a tool 🔎](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search) for searching through a large number of repository information


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## 🎉 The latest additions

**Python**
 * [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) - English to Japanese Transformer from scratch

_Updated on Dec 03, 2025_

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [SudachiPy](https://github.com/WorksApplications/SudachiPy) | 📥 451k/week | 📦 55M total | ⭐ 418 stars |
| 🔗 [Janome](https://github.com/mocobeta/janome) | 📥 36k/week | 📦 11M total | ⭐ 898 stars |
| 🔗 [mecab-python3](https://github.com/SamuraiT/mecab-python3) | 📥 248k/week | 📦 32M total | ⭐ 576 stars |
| 🔗 [mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python) | 📥 4k/week | 📦 587k total | ⭐ 265 stars |
| 🔗 [fugashi](https://github.com/polm/fugashi) | 📥 101k/week | 📦 11M total | ⭐ 489 stars |
| 🔗 [nagisa](https://github.com/taishi-i/nagisa) | 📥 26k/week | 📦 7M total | ⭐ 408 stars |
| 🔗 [pyknp](https://github.com/ku-nlp/pyknp) | 📥 917/week | 📦 3M total | ⭐ 92 stars |
| 🔗 [Mykytea-python](https://github.com/chezou/Mykytea-python) | 📥 2k/week | 📦 541k total | ⭐ 36 stars |
| 🔗 [konoha](https://github.com/himkt/konoha) | 📥 20k/week | 📦 5M total | ⭐ 260 stars |
| 🔗 [natto-py](https://github.com/buruzaemon/natto-py) | 📥 407k/week | 📦 28M total | ⭐ 95 stars |
| 🔗 [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) | 📥 18/week | 📦 26k total | ⭐ 23 stars |
| 🔗 [python-vaporetto](https://github.com/daac-tools/python-vaporetto) | 📥 193/week | 📦 169k total | ⭐ 20 stars |
| 🔗 [dango](https://github.com/mkartawijaya/dango) | 📥 44/week | 📦 25k total | ⭐ 20 stars |
| 🔗 [rhoknp](https://github.com/ku-nlp/rhoknp) | 📥 7k/week | 📦 895k total | ⭐ 36 stars |
| 🔗 [python-vibrato](https://github.com/daac-tools/python-vibrato) | 📥 127/week | 📦 112k total | ⭐ 43 stars |
| 🔗 [jagger-python](https://github.com/lighttransport/jagger-python) | 📥 606/week | 📦 278k total | ⭐ 12 stars |
| 🔗 [Mecari](https://github.com/zbller/Mecari) | - | - | ⭐ 35 stars |


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
 * [natsume-simple](https://github.com/borh-lab/natsume-simple) - natsume-simpleは日本語の係り受け関係検索システム


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [ginza](https://github.com/megagonlabs/ginza) | 📥 10k/week | 📦 2M total | ⭐ 823 stars |
| 🔗 [cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python) | 📥 55/week | 📦 53k total | ⭐ 7 stars |
| 🔗 [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) | 📥 330/week | 📦 319k total | ⭐ 37 stars |
| 🔗 [camphr](https://github.com/PKSHATechnology-Research/camphr) | 📥 390/week | 📦 262k total | ⭐ 338 stars |
| 🔗 [SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic) | 📥 406/week | 📦 115k total | ⭐ 20 stars |
| 🔗 [depccg](https://github.com/masashi-y/depccg) | 📥 50/week | 📦 44k total | ⭐ 98 stars |
| 🔗 [bertknp](https://github.com/ku-nlp/bertknp) | - | - | ⭐ 23 stars |
| 🔗 [esupar](https://github.com/KoichiYasuoka/esupar) | 📥 226/week | 📦 159k total | ⭐ 52 stars |
| 🔗 [yomikata](https://github.com/passaglia/yomikata) | 📥 7/week | 📦 49k total | ⭐ 31 stars |
| 🔗 [jdepp-python](https://github.com/lighttransport/jdepp-python) | 📥 616/week | 📦 264k total | ⭐ 4 stars |
| 🔗 [lightblue](https://github.com/daisukebekki/lightblue) | - | - | ⭐ 26 stars |
| 🔗 [natsume-simple](https://github.com/borh-lab/natsume-simple) | - | - | ⭐ 5 stars |


### Converter
Libraries that convert between character types such as kana, romaji, and full-width/half-width forms

 * [pykakasi](https://github.com/miurahr/pykakasi) - Lightweight converter from Japanese Kana-kanji sentences into Kana-Roman.
 * [cutlet](https://github.com/polm/cutlet) - Japanese to romaji converter in Python
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - Convert English alphabet to Katakana
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - Converts Arabic numerals, or 'western' style numbers, to a Japanese context.
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Mozc for Python: Kana-Kanji converter
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - Japanese text parser to separate Hiragana/Katakana string into morae (syllables).
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - 日本語文を音素列へ変換するスクリプト
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - A fast character conversion and transliteration library based on the scheme defined for Japan National Tax Agency (国税庁) 's
 * [wiredify](https://github.com/eggplants/wiredify) - Convert japanese kana from ba-bi-bu-be-bo into va-vi-vu-ve-vo
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - Simple Python package (CLI/Python API) for getting japanese readings (yomigana) and accents using MeCab.
 * [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) - 数量表現や時間表現の抽出・正規化を行うNormalizeNumexpのPython実装
 * [Jusho](https://github.com/nagataaaas/Jusho) - Easy wrapper for the postal code data of Japan
 * [yurenizer](https://github.com/sea-turt1e/yurenizer) - Japanese text normalizer that resolves spelling inconsistencies. （日本語表記揺れ解消ツール）
 * [e2k](https://github.com/Patchethium/e2k) - A tool for automatic English to Katakana conversion
 * [alkana.py](https://github.com/zomysan/alkana.py) - A tool to get the katakana reading of an alphabetical string.
 * [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) - 英語文字列をカタカナに変換するプログラム


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [pykakasi](https://github.com/miurahr/pykakasi) | 📥 246k/week | 📦 25M total | ⭐ 442 stars |
| 🔗 [cutlet](https://github.com/polm/cutlet) | 📥 13k/week | 📦 1M total | ⭐ 365 stars |
| 🔗 [alphabet2kana](https://github.com/shihono/alphabet2kana) | 📥 212/week | 📦 53k total | ⭐ 14 stars |
| 🔗 [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) | - | - | ⭐ 49 stars |
| 🔗 [mozcpy](https://github.com/ikegami-yukino/mozcpy) | 📥 130/week | 📦 10k total | ⭐ 46 stars |
| 🔗 [jamorasep](https://github.com/tachi-hi/jamorasep) | 📥 64/week | 📦 8k total | ⭐ 10 stars |
| 🔗 [text2phoneme](https://github.com/korguchi/text2phoneme) | - | - | ⭐ 13 stars |
| 🔗 [jntajis-python](https://github.com/opencollector/jntajis-python) | 📥 214/week | 📦 100k total | ⭐ 21 stars |
| 🔗 [wiredify](https://github.com/eggplants/wiredify) | 📥 6/week | 📦 6k total | ⭐ 3 stars |
| 🔗 [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) | 📥 19/week | 📦 4k total | ⭐ 7 stars |
| 🔗 [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) | 📥 31/week | 📦 13k total | ⭐ 8 stars |
| 🔗 [Jusho](https://github.com/nagataaaas/Jusho) | 📥 273/week | 📦 49k total | ⭐ 11 stars |
| 🔗 [yurenizer](https://github.com/sea-turt1e/yurenizer) | 📥 24/week | 📦 16k total | ⭐ 4 stars |
| 🔗 [e2k](https://github.com/Patchethium/e2k) | 📥 104/week | 📦 16k total | ⭐ 15 stars |
| 🔗 [alkana.py](https://github.com/zomysan/alkana.py) | - | - | ⭐ 33 stars |
| 🔗 [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) | - | - | ⭐ 4 stars |


### Preprocessor
Libraries that normalize and clean text before analysis

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - Japanese text normalizer for mecab-neologd
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, and Zenkaku
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - A fast converter between Japanese hankaku and zenkaku characters
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - A powerful text cleaner for Japanese web texts
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 複数の前処理を構成して管理するテキスト前処理ツール
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho is a Python module that facilitates bidirectional conversion between half-width katakana and full-width katakana in Japanese.
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - Yet Another Fast Japanese String Converter
 * [kairyou](https://github.com/bikatr7/kairyou) - Quickly preprocesses Japanese text using NLP/NER from SpaCy for Japanese translation or other NLP tasks.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [neologdn](https://github.com/ikegami-yukino/neologdn) | 📥 8k/week | 📦 1M total | ⭐ 287 stars |
| 🔗 [jaconv](https://github.com/ikegami-yukino/jaconv) | 📥 393k/week | 📦 54M total | ⭐ 336 stars |
| 🔗 [mojimoji](https://github.com/studio-ousia/mojimoji) | 📥 51k/week | 📦 10M total | ⭐ 150 stars |
| 🔗 [text-cleaning](https://github.com/ku-nlp/text-cleaning) | - | - | ⭐ 12 stars |
| 🔗 [HojiChar](https://github.com/HojiChar/HojiChar) | 📥 3k/week | 📦 583k total | ⭐ 124 stars |
| 🔗 [utsuho](https://github.com/juno-rmks/utsuho) | 📥 62/week | 📦 17k total | ⭐ 4 stars |
| 🔗 [python-habachen](https://github.com/Hizuru3/python-habachen) | 📥 4k/week | 📦 2M total | ⭐ 6 stars |
| 🔗 [kairyou](https://github.com/bikatr7/kairyou) | 📥 143/week | 📦 29k total | ⭐ 6 stars |


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


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [bunkai](https://github.com/megagonlabs/bunkai) | 📥 378/week | 📦 101k total | ⭐ 199 stars |
| 🔗 [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) | 📥 11/week | 📦 5k total | ⭐ 14 stars |
| 🔗 [sengiri](https://github.com/ikegami-yukino/sengiri) | 📥 311/week | 📦 135k total | ⭐ 24 stars |
| 🔗 [budoux](https://github.com/google/budoux) | 📥 5k/week | 📦 320k total | ⭐ 1.5k stars |
| 🔗 [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) | 📥 844/week | 📦 162k total | ⭐ 73 stars |
| 🔗 [hasami](https://github.com/mkartawijaya/hasami) | 📥 62/week | 📦 34k total | ⭐ 6 stars |
| 🔗 [kuzukiri](https://github.com/alinear-corp/kuzukiri) | 📥 47/week | 📦 26k total | ⭐ 6 stars |
| 🔗 [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) | - | - | ⭐ 9 stars |
| 🔗 [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) | 📥 64/week | 📦 1k total | ⭐ 62 stars |


### Sentiment analysis
Libraries that detect emotions or polarity in text

 * [oseti](https://github.com/ikegami-yukino/oseti) - Dictionary based Sentiment Analysis for Japanese
 * [negapoji](https://github.com/liaoziyang/negapoji) - Japanese negative positive classification.日本語文書のネガポジを判定。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - Emotion analyzer for Japanese text
 * [asari](https://github.com/Hironsan/asari) - Japanese sentiment analyzer implemented in Python.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [oseti](https://github.com/ikegami-yukino/oseti) | 📥 157/week | 📦 163k total | ⭐ 96 stars |
| 🔗 [negapoji](https://github.com/liaoziyang/negapoji) | - | - | ⭐ 151 stars |
| 🔗 [pymlask](https://github.com/ikegami-yukino/pymlask) | 📥 50/week | 📦 65k total | ⭐ 115 stars |
| 🔗 [asari](https://github.com/Hironsan/asari) | 📥 88/week | 📦 77k total | ⭐ 152 stars |


### Machine translation
Libraries that automatically translate text between languages

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - An example usage of JParaCrawl pre-trained Neural Machine Translation (NMT) models.
 * [JASS](https://github.com/Mao-KU/JASS) - JASS: Japanese-specific Sequence to Sequence Pre-training for Neural Machine Translation (LREC2020) & Linguistically Driven Multi-Task Pre-Training for Low-Resource Neural Machine Translation (ACM TALLIP)
 * [PheMT](https://github.com/cl-tohoku/PheMT) - A phenomenon-wise evaluation dataset for Japanese-English machine translation robustness. The dataset is based on the MTNT dataset, with additional annotations of four linguistic phenomena; Proper Noun, Abbreviated Noun, Colloquial Expression, and Variant. COLING 2020.
 * [VISA](https://github.com/ku-nlp/VISA) - An ambiguous subtitles dataset for visual scene-aware machine translation
 * [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) - A command-line interface for translation using the plamo-2-translate model with local execution.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) | - | - | ⭐ 105 stars |
| 🔗 [JASS](https://github.com/Mao-KU/JASS) | - | - | ⭐ 16 stars |
| 🔗 [PheMT](https://github.com/cl-tohoku/PheMT) | - | - | ⭐ 17 stars |
| 🔗 [VISA](https://github.com/ku-nlp/VISA) | - | - | ⭐ 14 stars |
| 🔗 [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) | - | - | ⭐ 304 stars |


### Named entity recognition
Libraries that extract names of people, places, and organizations from text

 * [namaco](https://github.com/chakki-works/namaco) - Character Based Named Entity Recognition.
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia is an Extended Named Entity Dictionary from Wikipedia.
 * [noyaki](https://github.com/ken11/noyaki) - Converts character span label information to tokenized text-based label information.
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - Code to perform finetuning of the BERT model. BERTモデルのファインチューニングで固有表現抽出用タスクのモデルを作成・使用するサンプルです
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 詳細なアノテーション基準に基づく症例報告コーパスからの固有表現及び関係の抽出精度の推論を行うコード
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp, A python module for geotagging Japanese texts.
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - BERTによる日本語固有表現抽出のファインチューニング用プログラム
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - Examples to finetune encoder-only and encoder-decoder transformers for Japanese language (Hugging Face) Resources
 * [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) - BERTのfine-tuningによる固有表現抽出


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [namaco](https://github.com/chakki-works/namaco) | - | - | ⭐ 40 stars |
| 🔗 [entitypedia](https://github.com/chakki-works/entitypedia) | - | - | ⭐ 13 stars |
| 🔗 [noyaki](https://github.com/ken11/noyaki) | 📥 314/week | 📦 18k total | ⭐ 5 stars |
| 🔗 [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) | - | - | ⭐ 11 stars |
| 🔗 [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) | - | - | ⭐ 1 stars |
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 243/week | 📦 18k total | ⭐ 22 stars |
| 🔗 [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) | - | - | ⭐ 4 stars |
| 🔗 [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) | - | - | ⭐ 16 stars |
| 🔗 [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) | - | - | ⭐ 2 stars |


### OCR
Libraries that recognize and extract text from images

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - About Optical character recognition for Japanese text, with the main focus being Japanese manga
 * [mokuro](https://github.com/kha-white/mokuro) - Read Japanese manga inside browser with selectable text.
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - Handwritten Japanese OCR demo using touch panel to draw the input text using Intel OpenVINO toolkit
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - 日本語OCR
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - NDLOCRのアプリケーション
 * [donut](https://github.com/clovaai/donut) - Official Implementation of OCR-free Document Understanding Transformer (Donut) and Synthetic Document Generator (SynthDoG), ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - manga translator - get japanese manga from url to translate manga image
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - OCR system for recognizing modern Japanese magazines
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - NDLOCR用テキスト認識モジュール
 * [Poricom](https://github.com/blueaxis/Poricom) - Optical character recognition in manga images. Manga OCR desktop application
 * [owocr](https://github.com/aurorawright/owocr) - Optical character recognition for Japanese text
 * [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) - Yomitoku is an AI-powered document image analysis package designed specifically for the Japanese language.
 * [findtextcenternet](https://github.com/lithium0003/findtextcenternet) - Japanese OCR with CenterNet
 * [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) - A simple OCR for manga (Japanese traditional and Japanese vertical)
 * [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) - 日本語の文章画像に対するOCRの性能を評価


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [manga-ocr](https://github.com/kha-white/manga-ocr) | 📥 2k/week | 📦 206k total | ⭐ 2.4k stars |
| 🔗 [mokuro](https://github.com/kha-white/mokuro) | 📥 468/week | 📦 82k total | ⭐ 1.4k stars |
| 🔗 [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) | - | - | ⭐ 38 stars |
| 🔗 [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) | - | - | ⭐ 243 stars |
| 🔗 [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) | - | - | ⭐ 564 stars |
| 🔗 [donut](https://github.com/clovaai/donut) | 📥 495/week | 📦 191k total | ⭐ 6.7k stars |
| 🔗 [JMTrans](https://github.com/ttop32/JMTrans) | - | - | ⭐ 88 stars |
| 🔗 [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) | - | - | ⭐ 152 stars |
| 🔗 [text_recognition](https://github.com/ndl-lab/text_recognition) | - | - | ⭐ 8 stars |
| 🔗 [Poricom](https://github.com/blueaxis/Poricom) | - | - | ⭐ 405 stars |
| 🔗 [owocr](https://github.com/aurorawright/owocr) | - | - | ⭐ 122 stars |
| 🔗 [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) | 📥 1k/week | 📦 56k total | ⭐ 1.2k stars |
| 🔗 [findtextcenternet](https://github.com/lithium0003/findtextcenternet) | - | - | ⭐ 54 stars |
| 🔗 [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-fogi-manga) | - | - | ⭐ 6 stars |
| 🔗 [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) | - | - | ⭐ 1 stars |


### Tool for pretrained models
Libraries that utilize pretrained models to improve accuracy and efficiency

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE: Japanese General Language Understanding Evaluation
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - Use custom tokenizers in spacy-transformers
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - T5による会話生成
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - To investigate various DNN text classifiers including MLP, CNN, RNN, BERT approaches.
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - Deploying sentiment analysis server with FastAPI and BERT
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - Masked Language Model-based Scoring for Japanese and Vietnamese
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - AllenNLP integration for Shiba: Japanese CANINE model
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - script to evaluate pre-trained Japanese word2vec model on Japanese similarity dataset
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - BERT-based GEC tagging for Japanese
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - Japanese-BPEEncoder
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - Japanese-BPEEncoder Version 2
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - 日本語文法誤り訂正ツール
 * [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) - Japanese Stable Diffusion is a Japanese specific latent text-to-image diffusion model capable of generating photo-realistic images given any text input.
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - A BERT model for nagisa
 * [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) - Example code for prefix-tuning GPT/GPT-NeoX models and for inference with trained prefixes
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) - Japanese Tokenizer for transformers library
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP Language Model Evaluation Harness
 * [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) - How do different tokenizers perform on downstream tasks in scriptio continua languages?: A case study in Japanese-ACL SRW 2023
 * [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) - A framework for few-shot evaluation of autoregressive language models.
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classification
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP Language Model Evaluation Harness
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - The repository contains scripts and merge scripts that have been modified to adapt an Alpaca-Lora adapter for LoRA tuning when assuming the use of the "rinna/japanese-gpt-neox..." [gpt-neox] model converted to ggml.
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - このリポジトリは日本語LLMのキャラクターロールプレイに関する性能を評価するために作成しました。
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - This repository supports YuzuAI's Rakuda leaderboard of Japanese LLMs, which is a Japanese-focused analogue of LMSYS' Vicuna eval.
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - このツールは、複数のデータセットを横断して日本語の大規模言語モデルを自動評価するものです．
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - This repository contains the code for supervised fine-tuning of LLM-jp models.
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - LLM勉強会（LLM-jp）で開発しているLLM用のトークナイザー関連をまとめたリポジトリです．
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - Japanese Language Model Financial Evaluation Harness
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - Japanese Vicuna QA Benchmark
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - Swallowプロジェクト 大規模言語モデル 評価スクリプト
 * [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) - Swallowプロジェクト 事後学習ずみ大規模言語モデル 評価フレームワーク


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 328 stars |
| 🔗 [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) | 📥 708/week | 📦 156k total | ⭐ 16 stars |
| 🔗 [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) | - | - | ⭐ 3 stars |
| 🔗 [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) | - | - | ⭐ 9 stars |
| 🔗 [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) | - | - | ⭐ 2 stars |
| 🔗 [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) | - | - | ⭐ 5 stars |
| 🔗 [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) | 📥 25/week | 📦 19k total | ⭐ 12 stars |
| 🔗 [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) | - | - | ⭐ 12 stars |
| 🔗 [gector-ja](https://github.com/jonnyli1125/gector-ja) | - | - | ⭐ 19 stars |
| 🔗 [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) | - | - | ⭐ 41 stars |
| 🔗 [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) | - | - | ⭐ 41 stars |
| 🔗 [transformer-copy](https://github.com/youichiro/transformer-copy) | - | - | ⭐ 29 stars |
| 🔗 [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) | - | - | ⭐ repo not found stars |
| 🔗 [nagisa_bert](https://github.com/taishi-i/nagisa_bert) | 📥 27/week | 📦 53k total | ⭐ 4 stars |
| 🔗 [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) | - | - | ⭐ repo not found stars |
| 🔗 [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) | - | - | ⭐ 17 stars |
| 🔗 [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) | 📥 88/week | 📦 26k total | ⭐ 5 stars |
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 stars |
| 🔗 [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) | - | - | ⭐ 6 stars |
| 🔗 [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) | - | - | ⭐ 1 stars |
| 🔗 [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) | - | - | ⭐ 97 stars |
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 stars |
| 🔗 [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) | - | - | ⭐ 18 stars |
| 🔗 [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) | - | - | ⭐ 40 stars |
| 🔗 [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) | - | - | ⭐ 50 stars |
| 🔗 [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | - | - | ⭐ 140 stars |
| 🔗 [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) | - | - | ⭐ 62 stars |
| 🔗 [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) | - | - | ⭐ 43 stars |
| 🔗 [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | - | - | ⭐ 76 stars |
| 🔗 [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | - | - | ⭐ 33 stars |
| 🔗 [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) | - | - | ⭐ 22 stars |
| 🔗 [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) | - | - | ⭐ 23 stars |


### Others
General-purpose tools supporting Japanese language processing

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - A tool for dividing the Japanese full name into a family name and a given name.
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - A curated list of resources dedicated to Python libraries of NLP for Japanese
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - python版日本語意味役割付与システム（ASA）
 * [toiro](https://github.com/taishi-i/toiro) - A comparison tool of Japanese tokenizers
 * [ja-timex](https://github.com/yagays/ja-timex) - 自然言語で書かれた時間情報表現を抽出/規格化するルールベースの解析器
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
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - Example codes for Japanese Realistic Textual Entailment Corpus
 * [desuwa](https://github.com/megagonlabs/desuwa) - Feature annotator to morphemes and phrases based on KNP rule files (pure-Python)
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - Restaurant Search System through Dialogue in Japanese.
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - Samples codes for natural language processing in Japanese
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - Small example scripts for working with Japanese texts in Python
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - Japanese version of DNorm
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - EventGraph is a development platform for high-level NLP applications in Japanese.
 * [ishi](https://github.com/ku-nlp/ishi) - Ishi: A volition classifier for Japanese
 * [python-npylm](https://github.com/musyoku/python-npylm) - ベイズ階層言語モデルによる教師なし形態素解析
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - 条件付確率場とベイズ階層言語モデルの統合による半教師あり形態素解析
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - 教師なし品詞タグ推定
 * [negima](https://github.com/cocodrips/negima) - Negima is a Python package to extract phrases in Japanese text by using the part-of-speeches based rules you defined.
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - Extractive summarizer using BertSum as summarization model
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - A parser for Japanese number (Kanji, arabic) in the natural language.
 * [kantan](https://github.com/itayperl/kantan) - Lookup japanese words by radical patterns
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - Get Japanese dialogue corpus
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - A summarizer for Japanese articles.
 * [chirptext](https://github.com/letuananh/chirptext) - ChirpText is a collection of text processing tools for Python.
 * [yubin](https://github.com/alvations/yubin) - Japanese Address Munger
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - Japanese Wikipedia Cleaner
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - A python library to convert Japanese to phoneme.
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - This repository contains codes related to the experiments in "An Experimental Evaluation of Japanese Tokenizers for Sentiment-Based Text Classification"
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - About
This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - Generates plain or tokenized text files from the Aozora Bunko
 * [JLM](https://github.com/jiali-ms/JLM) - A fast LSTM Language Model for large vocabulary language like Japanese and Chinese
 * [NTM](https://github.com/m3yrin/NTM) - Testing of Neural Topic Modeling for Japanese articles
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - This is a English-Japanese lexicon for Machine Learning and Deep Learning terminology.
 * [text-generation](https://github.com/discus0434/text-generation) - Easy-to-use scripts to fine-tune GPT-2-JA with your own texts, to generate sentences, and to tweet them automatically.
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - Neural Image Caption (NIC) on chainer, its pretrained models on English and Japanese image caption datasets.
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - The official repository for "UnihanLM: Coarse-to-Fine Chinese-Japanese Language Model Pretraining with the Unihan Database", AACL-IJCNLP 2020
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - Code to perform finetuning of the mBART model.
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - xvector model on jtubespeech
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - TinySegmenter用の学習モデルを自作するためのツール．
 * [Grongish](https://github.com/shogo82148/Grongish) - 日本語とグロンギ語の相互変換スクリプト
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - WordCloudでの日本語文章をMecab（形態素解析エンジン）を使用せずに形態素解析チックな表示を実現するスクリプト
 * [snark](https://github.com/hiraokusky/snark) - 日本語ワードネットを利用したDBアクセスライブラリ
 * [toEmoji](https://github.com/mkan0141/toEmoji) - 日本語文を絵文字だけの文に変換するなにか
 * [termextract](https://github.com/kanjirz50/termextract) - - 専門用語抽出アルゴリズムの実装の練習
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - Japanese-Dialog-Transformerの応答候補に対して、KenLMによるN-gram言語モデルでスコアリングし、フィルタリング若しくはリランキングを行う。
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - Mixture of Unigram Model and Infinite Mixture of Unigram Model in Python. (混合ユニグラムモデルと無限混合ユニグラムモデル)
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - Hidden Markov Model (HMM) and Infinite Hidden Markov Model (iHMM) in Python. (隠れマルコフモデルと無限隠れマルコフモデル)
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
 * [nksnd](https://github.com/yoriyuki/nksnd) - New kana-kanji conversion engine
 * [JaMIE](https://github.com/racerandom/JaMIE) - A Japanese Medical Information Extraction Toolkit
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - fasttextとword2vecの比較と、実行スクリプト、学習スクリプトです
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - 最小のサーチエンジン/PageRank/tf-idf
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - 5chの過去ログをスクレイピングして、過去流行った単語(ex, 香具師, orz)などを追跡調査
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - Twitter日本語評判分析データセットのためのツイートダウンローダ
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - Aggregating Japanese words based on Juman++ and ConceptNet5.5
 * [jinf](https://github.com/hkiyomaru/jinf) - A Japanese inflection converter
 * [kwja](https://github.com/ku-nlp/kwja) - A unified language analyzer for Japanese
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - Reproduced package based on Masked Language Model Scoring (ACL2020).
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - [PyTorch] ClipCap for Japanese
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - [PyTorch] Show, Attend and Tell for Japanese
 * [cihai](https://github.com/cihai/cihai) - Python library for CJK (Chinese, Japanese, and Korean) language dictionary
 * [marine](https://github.com/6gsn/marine) - MARINE : Multi-task leaRnIng-based JapaNese accent Estimation
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - Finetuning Whisper ASR model
 * [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) - A PyTorch Implementation of japanese chatbot using BERT and Transformer's decoder
 * [radicalchar](https://github.com/yamamaya/radicalchar) - 部首文字正規化ライブラリ
 * [akaza](https://github.com/tokuhirom/akaza) - Yet another Japanese IME for IBus/Linux
 * [posuto](https://github.com/polm/posuto) -  Japanese postal code data.
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - Tacotron2 implementation of Japanese
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - ひらがなIME for IBus
 * [furiganapad](https://github.com/esrille/furiganapad) - ふりがなパッド
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - Japanese synonym library
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - Mecab + NEologd + Docker + Python3
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - JapaneseEmbeddingEval
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPTがYouTuberをやります
 * [shuwa](https://github.com/google/shuwa) - Extend GNOME On-Screen Keyboard for Input Methods
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - This repository provides the code for Japanese NLI model, a fine-tuned masked language model.
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - A tool for Japanese-English translation and English-Japanese translation by using FuguMT
 * [fugumt](https://github.com/s-taka/fugumt) - ぷるーふおぶこんせぷと で公開した機械翻訳エンジンを利用する翻訳環境です。 フォームに入力された文字列の翻訳、PDFの翻訳が可能です。
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - JaSPICE: Automatic Evaluation Metric Using Predicate-Argument Structures for Image Captioning Models
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - jp-localization
 * [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) - Python wrapper for OpenJTalk
 * [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) - Make learning Japanese easier by adding readings for every kanji in the eBook
 * [N46Whisper](https://github.com/Ayanaminn/N46Whisper) - Whisper based Japanese subtitle generator
 * [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) - Rinna-3.6B、OpenCALM等の日本語対応LLM(大規模言語モデル)用の簡易Webインタフェースです
 * [pdf-translator](https://github.com/discus0434/pdf-translator) - pdf-translator translates English PDF files into Japanese, preserving the original layout.
 * [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) - Haystack + Elasticsearch + wikipedia(ja) を用いた、日本語の質問応答システムのサンプル
 * [mozc-devices](https://github.com/google/mozc-devices) - Automatically exported from code.google.com/p/mozc-morse
 * [natsume](https://github.com/faruzan0820/natsume) - A Japanese text frontend processing toolkit
 * [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) - 日本語TTS（VITS）の学習と音声合成のGradio WebUI
 * [ja-law-parser](https://github.com/takuyaa/ja-law-parser) - A Japanese law parser
 * [dictation-kit](https://github.com/julius-speech/dictation-kit) - Japanese dictation kit using Julius
 * [julius4seg](https://github.com/Hiroshiba/julius4seg) - Juliusを使ったセグメンテーション支援ツール
 * [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXの音声合成エンジン
 * [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) - LLaVA-JP is a Japanese VLM trained by LLaVA method
 * [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) - Open source RAG with Llama Index for Japanese LLM in low resource settting
 * [bertjsc](https://github.com/er-ri/bertjsc) - Japanese Spelling Error Corrector using BERT(Masked-Language Model). BERTに基づいて日本語校正
 * [llm-leaderboard](https://github.com/wandb/llm-leaderboard) - Project of llm evaluation to Japanese tasks
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - About
Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - Modifying LAVIS' BLIP2 Q-former with models pretrained on Japanese datasets.
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - wikipedia 日本語の文を、各種日本語の embeddings や faiss index へと変換するスクリプト等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - Exploring Japanese SimCSE
 * [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) - Wikipediaの日本語記事を元に、ユーザの質問に回答するGradioベースのRAGのサンプル
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - GPT-4 を用いて、言語モデルの応答を自動評価するスクリプト
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - 日本語T5モデル
 * [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) - A repo for evaluating Japanese LLMs　・　日本語LLMを評価するレポ
 * [jmteb](https://github.com/sbintuitions/jmteb) - The evaluation scripts of JMTEB (Japanese Massive Text Embedding Benchmark)
 * [pydomino](https://github.com/dwangomediavillage/pydomino) - 日本語音声に対して音素ラベルをアラインメントするためのツールです
 * [easynovelassistant](https://github.com/zuntan03/easynovelassistant) - 軽量で規制も検閲もない日本語ローカル LLM『LightChatAssistant-TypeB』による、簡単なノベル生成アシスタントです。ローカル特権の永続生成 Generate forever で、当たりガチャを積み上げます。読み上げにも対応。
 * [clip-japanese](https://github.com/sonoisa/clip-japanese) - 日本語データセットでのqlora instruction tuning学習サンプルコード
 * [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) - Japanese rōmaji input schema for Rime IME
 * [deep-question-generation](https://github.com/sonoisa/deep-question-generation) - 深層学習を用いたクイズ自動生成（日本語T5モデル）
 * [magpie-nemotron](https://github.com/aratako/magpie-nemotron) - Magpieという手法とNemotron-4-340B-Instructを用いて合成対話データセットを作るコード
 * [qlora_ja](https://github.com/sosuke115/qlora_ja) - 日本語データセットでのqlora instruction tuning学習サンプルコード
 * [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) - Mozc UT Jawiki Dictionary is a dictionary generated from the Japanese Wikipedia for Mozc.
 * [shisa-v2](https://github.com/shisa-ai/shisa-v2) - Japanese / English Bilingual LLM
 * [llm-translator](https://github.com/hpprc/llm-translator) - Mixtral-based Ja-En (En-Ja) Translation model
 * [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) - Whisperのデコーダをllm-jp-1.3b-v1.0に置き換えた音声認識モデルを学習させるためのコード
 * [rag-japanese](https://github.com/akimfromparis/rag-japanese) - Open source RAG with Llama Index for Japanese LLM in low resource settting
 * [monaka](https://github.com/komiya-lab/monaka) - A Japanese Parser (including historical Japanese)
 * [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) - A state-of-the-art open-source Japanese <--> English machine translation system based on the latest NMT research.
 * [substring-word-finder](https://github.com/toufu-24/substring-word-finder) - 連続部分文字列の単語判定を行います
 * [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) - This project is a benchmarking tool for evaluating and comparing the performance of various Vision Language Models (VLMs). It uses two datasets: LLaVA-Bench-In-the-Wild and Japanese HERON Bench to measure model performance.
 * [text2dataset](https://github.com/llm-jp/text2dataset) - Easily turn large English text datasets into Japanese text datasets using open LLMs.
 * [mecab-web-api](https://github.com/bungoume/mecab-web-api) - MeCabを利用した日本語形態素解析WebAPI
 * [mecab_controller](https://github.com/ajatt-tools/mecab_controller) - Mecab wrapper to generate furigana readings.
 * [vits](https://github.com/zassou65535/vits) - VITSによるテキスト読み上げ器&ボイスチェンジャー
 * [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) - 音声認識、文章生成、音声合成を使って対話するチャットボットアプリ
 * [kudasai](https://github.com/bikatr7/kudasai) - Streamlining Japanese-English Translation with Advanced Preprocessing and Integrated Translation Technologies
 * [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) - MeCabの形態素解析結果を可視化するツール
 * [add-dictionary](https://github.com/massao000/add-dictionary) - OpenJTalkのユーザ辞書をGUIで追加するアプリ
 * [j-moshi](https://github.com/nu-dialogue/j-moshi) - J-Moshi: A Japanese Full-duplex Spoken Dialogue System
 * [jatts](https://github.com/unilight/jatts) - JATTS: Japanese TTS (for research)
 * [tsukasa-speech](https://github.com/respaired/tsukasa-speech) - a Frontier Japanese Speech Generation net
 * [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) - ElasticsearchやGiNZA、患者表現辞書を使った患者表現揺れ吸収する意味構造検索を試した
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 生成自動評価を行うためのPythonツール
 * [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) - Colaboratory上でAsagi(合成データセットを活用した大規模日本語VLM)をお試しするサンプル
 * [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) - This tool automatically evaluates Japanese multi-modal large language models across multiple datasets.
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 生成自動評価を行うためのPythonツール
 * [manga109api](https://github.com/manga109/manga109api) - Simple python API to read annotation data of Manga109
 * [fastrtc-jp](https://github.com/route250/fastrtc-jp) - fastrtc用の日本語TTSとSTT追加キット
 * [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) - Pythonを使用したWhisperモデルによる音声文字起こしツール
 * [pocket-researcher](https://github.com/u-masao/pocket-researcher) - LLMを活用した自律調査エージェント。手軽に情報収集、概要把握。
 * [jtransbench](https://github.com/webbigdata-jp/jtransbench) - A tool to easily benchmark Japanese translation skills
 * [easyllasa](https://github.com/zuntan03/easyllasa) - EasyLlasa は 5～15秒の日本語音声と日本語テキストから日本語音声を生成する TSTS (TextSpeechToSpeech) です。
 * [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) - 氏名漢字カナ突合モデル
 * [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) - OpenReview論文を自動で発見・分析する日本語対応AIエージェント
 * [pitchbench](https://github.com/shewiiii/pitchbench) - Experimental Japanese pitch accent based LLM Benchmark
 * [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) - English to Japanese Transformer from scratch


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [namedivider-python](https://github.com/rskmoi/namedivider-python) | 📥 709/week | 📦 73k total | ⭐ 251 stars |
| 🔗 [asa-python](https://github.com/ikegami-yukino/asa-python) | 📥 20/week | 📦 30k total | ⭐ 11 stars |
| 🔗 [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) | - | - | ⭐ 22 stars |
| 🔗 [toiro](https://github.com/taishi-i/toiro) | 📥 93/week | 📦 25k total | ⭐ 120 stars |
| 🔗 [ja-timex](https://github.com/yagays/ja-timex) | 📥 327/week | 📦 84k total | ⭐ 140 stars |
| 🔗 [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) | - | - | ⭐ 138 stars |
| 🔗 [daaja](https://github.com/kajyuuen/daaja) | 📥 24/week | 📦 24k total | ⭐ 64 stars |
| 🔗 [accel-brain-code](https://github.com/accel-brain/accel-brain-code) | 📥 244/week | 📦 145k total | ⭐ 320 stars |
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 328 stars |
| 🔗 [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) | 📥 855/week | 📦 41k total | ⭐ 10 stars |
| 🔗 [nlplot](https://github.com/takapy0210/nlplot) | 📥 227/week | 📦 105k total | ⭐ 240 stars |
| 🔗 [rake-ja](https://github.com/kanjirz50/rake-ja) | - | - | ⭐ 21 stars |
| 🔗 [jel](https://github.com/izuna385/jel) | 📥 10/week | 📦 7k total | ⭐ 11 stars |
| 🔗 [MedNER-J](https://github.com/sociocom/MedNER-J) | - | - | ⭐ 18 stars |
| 🔗 [zunda-python](https://github.com/ikegami-yukino/zunda-python) | 📥 4/week | 📦 6k total | ⭐ 10 stars |
| 🔗 [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) | - | - | ⭐ 16 stars |
| 🔗 [showcase](https://github.com/cl-tohoku/showcase) | 📥 6/week | 📦 7k total | ⭐ 6 stars |
| 🔗 [darts-clone-python](https://github.com/rixwew/darts-clone-python) | 📥 3k/week | 📦 9M total | ⭐ 20 stars |
| 🔗 [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) | - | - | ⭐ 3 stars |
| 🔗 [desuwa](https://github.com/megagonlabs/desuwa) | 📥 11/week | 📦 10k total | ⭐ 6 stars |
| 🔗 [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) | - | - | ⭐ 278 stars |
| 🔗 [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) | - | - | ⭐ 65 stars |
| 🔗 [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) | - | - | ⭐ 26 stars |
| 🔗 [DNorm-J](https://github.com/sociocom/DNorm-J) | - | - | ⭐ 9 stars |
| 🔗 [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) | 📥 111/week | 📦 64k total | ⭐ 9 stars |
| 🔗 [ishi](https://github.com/ku-nlp/ishi) | 📥 7/week | 📦 6k total | ⭐ 2 stars |
| 🔗 [python-npylm](https://github.com/musyoku/python-npylm) | - | - | ⭐ 34 stars |
| 🔗 [python-npycrf](https://github.com/musyoku/python-npycrf) | - | - | ⭐ 11 stars |
| 🔗 [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) | - | - | ⭐ 16 stars |
| 🔗 [negima](https://github.com/cocodrips/negima) | 📥 10/week | 📦 16k total | ⭐ 14 stars |
| 🔗 [YouyakuMan](https://github.com/neilctwu/YouyakuMan) | - | - | ⭐ 52 stars |
| 🔗 [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) | 📥 578/week | 📦 2M total | ⭐ 21 stars |
| 🔗 [kantan](https://github.com/itayperl/kantan) | - | - | ⭐ 8 stars |
| 🔗 [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) | - | - | ⭐ 40 stars |
| 🔗 [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) | - | - | ⭐ 10 stars |
| 🔗 [chirptext](https://github.com/letuananh/chirptext) | 📥 581/week | 📦 183k total | ⭐ 6 stars |
| 🔗 [yubin](https://github.com/alvations/yubin) | 📥 1/week | 📦 3k total | ⭐ 3 stars |
| 🔗 [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) | 📥 31/week | 📦 23k total | ⭐ 6 stars |
| 🔗 [japanese2phoneme](https://github.com/iory/japanese2phoneme) | 📥 7/week | 📦 4k total | ⭐ 1 stars |
| 🔗 [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) | - | - | ⭐ 1 stars |
| 🔗 [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) | - | - | ⭐ 11 stars |
| 🔗 [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) | - | - | ⭐ 8 stars |
| 🔗 [JLM](https://github.com/jiali-ms/JLM) | - | - | ⭐ 111 stars |
| 🔗 [NTM](https://github.com/m3yrin/NTM) | - | - | ⭐ 13 stars |
| 🔗 [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) | - | - | ⭐ 40 stars |
| 🔗 [text-generation](https://github.com/discus0434/text-generation) | - | - | ⭐ 19 stars |
| 🔗 [chainer_nic](https://github.com/yuyay/chainer_nic) | - | - | ⭐ 17 stars |
| 🔗 [unihan-lm](https://github.com/JetRunner/unihan-lm) | - | - | ⭐ 2 stars |
| 🔗 [mbart-finetuning](https://github.com/ken11/mbart-finetuning) | - | - | ⭐ 3 stars |
| 🔗 [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) | - | - | ⭐ 46 stars |
| 🔗 [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) | - | - | ⭐ 72 stars |
| 🔗 [Grongish](https://github.com/shogo82148/Grongish) | - | - | ⭐ 25 stars |
| 🔗 [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) | - | - | ⭐ 9 stars |
| 🔗 [snark](https://github.com/hiraokusky/snark) | - | - | ⭐ 10 stars |
| 🔗 [toEmoji](https://github.com/mkan0141/toEmoji) | - | - | ⭐ 4 stars |
| 🔗 [termextract](https://github.com/kanjirz50/termextract) | - | - | ⭐ 18 stars |
| 🔗 [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) | - | - | ⭐ 1 stars |
| 🔗 [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) | - | - | ⭐ 6 stars |
| 🔗 [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) | - | - | ⭐ 5 stars |
| 🔗 [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) | - | - | ⭐ 5 stars |
| 🔗 [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) | - | - | ⭐ 69 stars |
| 🔗 [neural_ime](https://github.com/yohokuno/neural_ime) | - | - | ⭐ 67 stars |
| 🔗 [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) | - | - | ⭐ 178 stars |
| 🔗 [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) | 📥 142k/week | 📦 168k total | ⭐ repo not found stars |
| 🔗 [AugLy-jp](https://github.com/chck/AugLy-jp) | 📥 56/week | 📦 29k total | ⭐ 7 stars |
| 🔗 [furigana4epub](https://github.com/Mumumu4/furigana4epub) | 📥 21/week | 📦 11k total | ⭐ 28 stars |
| 🔗 [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) | 📥 44/week | 📦 19k total | ⭐ 12 stars |
| 🔗 [jageocoder](https://github.com/t-sagara/jageocoder) | 📥 2k/week | 📦 268k total | ⭐ 89 stars |
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 243/week | 📦 18k total | ⭐ 22 stars |
| 🔗 [nksnd](https://github.com/yoriyuki/nksnd) | - | - | ⭐ 26 stars |
| 🔗 [JaMIE](https://github.com/racerandom/JaMIE) | - | - | ⭐ 9 stars |
| 🔗 [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) | - | - | ⭐ 49 stars |
| 🔗 [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) | - | - | ⭐ 19 stars |
| 🔗 [5ch-analysis](https://github.com/GINK03/5ch-analysis) | - | - | ⭐ 73 stars |
| 🔗 [tweet_extructor](https://github.com/tatHi/tweet_extructor) | - | - | ⭐ 3 stars |
| 🔗 [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) | - | - | ⭐ 2 stars |
| 🔗 [jinf](https://github.com/hkiyomaru/jinf) | 📥 608/week | 📦 52k total | ⭐ 4 stars |
| 🔗 [kwja](https://github.com/ku-nlp/kwja) | 📥 344/week | 📦 52k total | ⭐ 137 stars |
| 🔗 [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) | - | - | ⭐ 6 stars |
| 🔗 [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) | - | - | ⭐ 12 stars |
| 🔗 [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) | - | - | ⭐ 2 stars |
| 🔗 [cihai](https://github.com/cihai/cihai) | 📥 464/week | 📦 202k total | ⭐ 94 stars |
| 🔗 [marine](https://github.com/6gsn/marine) | 📥 208/week | 📦 13k total | ⭐ 35 stars |
| 🔗 [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) | - | - | ⭐ 32 stars |
| 🔗 [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) | - | - | ⭐ repo not found stars |
| 🔗 [radicalchar](https://github.com/yamamaya/radicalchar) | - | - | ⭐ 7 stars |
| 🔗 [akaza](https://github.com/tokuhirom/akaza) | - | - | ⭐ 223 stars |
| 🔗 [posuto](https://github.com/polm/posuto) | 📥 4k/week | 📦 601k total | ⭐ 220 stars |
| 🔗 [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) | - | - | ⭐ 269 stars |
| 🔗 [ibus-hiragana](https://github.com/esrille/ibus-hiragana) | - | - | ⭐ 77 stars |
| 🔗 [furiganapad](https://github.com/esrille/furiganapad) | - | - | ⭐ 18 stars |
| 🔗 [chikkarpy](https://github.com/WorksApplications/chikkarpy) | 📥 344/week | 📦 50k total | ⭐ 55 stars |
| 🔗 [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) | - | - | ⭐ 36 stars |
| 🔗 [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) | - | - | ⭐ 183 stars |
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 stars |
| 🔗 [shuwa](https://github.com/google/shuwa) | - | - | ⭐ 143 stars |
| 🔗 [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) | - | - | ⭐ 5 stars |
| 🔗 [tra-fugu](https://github.com/tos-kamiya/tra-fugu) | - | - | ⭐ 6 stars |
| 🔗 [fugumt](https://github.com/s-taka/fugumt) | - | - | ⭐ 63 stars |
| 🔗 [JaSPICE](https://github.com/keio-smilab23/JaSPICE) | 📥 5/week | 📦 2k total | ⭐ 9 stars |
| 🔗 [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) | - | - | ⭐ 48 stars |
| 🔗 [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) | 📥 7k/week | 📦 1M total | ⭐ 240 stars |
| 🔗 [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) | 📥 7/week | 📦 7k total | ⭐ 24 stars |
| 🔗 [N46Whisper](https://github.com/Ayanaminn/N46Whisper) | - | - | ⭐ 1.7k stars |
| 🔗 [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) | - | - | ⭐ 17 stars |
| 🔗 [pdf-translator](https://github.com/discus0434/pdf-translator) | - | - | ⭐ 331 stars |
| 🔗 [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) | - | - | ⭐ 1 stars |
| 🔗 [mozc-devices](https://github.com/google/mozc-devices) | - | - | ⭐ 2.7k stars |
| 🔗 [natsume](https://github.com/faruzan0820/natsume) | 📥 0/week | 📦 3k total | ⭐ repo not found stars |
| 🔗 [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) | - | - | ⭐ 42 stars |
| 🔗 [ja-law-parser](https://github.com/takuyaa/ja-law-parser) | - | - | ⭐ 25 stars |
| 🔗 [dictation-kit](https://github.com/julius-speech/dictation-kit) | - | - | ⭐ 163 stars |
| 🔗 [julius4seg](https://github.com/Hiroshiba/julius4seg) | - | - | ⭐ 7 stars |
| 🔗 [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) | - | - | ⭐ 1.6k stars |
| 🔗 [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) | - | - | ⭐ 63 stars |
| 🔗 [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) | - | - | ⭐ 10 stars |
| 🔗 [bertjsc](https://github.com/er-ri/bertjsc) | - | - | ⭐ 13 stars |
| 🔗 [llm-leaderboard](https://github.com/wandb/llm-leaderboard) | - | - | ⭐ 90 stars |
| 🔗 [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) | - | - | ⭐ 17 stars |
| 🔗 [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) | - | - | ⭐ 13 stars |
| 🔗 [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) | - | - | ⭐ 11 stars |
| 🔗 [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) | - | - | ⭐ 69 stars |
| 🔗 [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) | - | - | ⭐ repo not found stars |
| 🔗 [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) | - | - | ⭐ 16 stars |
| 🔗 [t5-japanese](https://github.com/sonoisa/t5-japanese) | - | - | ⭐ 116 stars |
| 🔗 [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) | - | - | ⭐ 5 stars |
| 🔗 [jmteb](https://github.com/sbintuitions/jmteb) | - | - | ⭐ 77 stars |
| 🔗 [pydomino](https://github.com/dwangomediavillage/pydomino) | - | - | ⭐ 34 stars |
| 🔗 [easynovelassistant](https://github.com/zuntan03/easynovelassistant) | - | - | ⭐ 206 stars |
| 🔗 [clip-japanese](https://github.com/sonoisa/clip-japanese) | - | - | ⭐ 13 stars |
| 🔗 [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) | - | - | ⭐ 43 stars |
| 🔗 [deep-question-generation](https://github.com/sonoisa/deep-question-generation) | - | - | ⭐ 12 stars |
| 🔗 [magpie-nemotron](https://github.com/aratako/magpie-nemotron) | - | - | ⭐ 7 stars |
| 🔗 [qlora_ja](https://github.com/sosuke115/qlora_ja) | - | - | ⭐ 1 stars |
| 🔗 [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) | - | - | ⭐ 26 stars |
| 🔗 [shisa-v2](https://github.com/shisa-ai/shisa-v2) | - | - | ⭐ 28 stars |
| 🔗 [llm-translator](https://github.com/hpprc/llm-translator) | - | - | ⭐ 20 stars |
| 🔗 [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) | - | - | ⭐ 9 stars |
| 🔗 [rag-japanese](https://github.com/akimfromparis/rag-japanese) | - | - | ⭐ 10 stars |
| 🔗 [monaka](https://github.com/komiya-lab/monaka) | - | - | ⭐ 3 stars |
| 🔗 [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) | - | - | ⭐ 3 stars |
| 🔗 [substring-word-finder](https://github.com/toufu-24/substring-word-finder) | - | - | ⭐ 4 stars |
| 🔗 [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) | - | - | ⭐ 6 stars |
| 🔗 [text2dataset](https://github.com/llm-jp/text2dataset) | - | - | ⭐ 24 stars |
| 🔗 [mecab-web-api](https://github.com/bungoume/mecab-web-api) | - | - | ⭐ 40 stars |
| 🔗 [mecab_controller](https://github.com/ajatt-tools/mecab_controller) | - | - | ⭐ 17 stars |
| 🔗 [vits](https://github.com/zassou65535/vits) | - | - | ⭐ 91 stars |
| 🔗 [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) | - | - | ⭐ 48 stars |
| 🔗 [kudasai](https://github.com/bikatr7/kudasai) | - | - | ⭐ 26 stars |
| 🔗 [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) | - | - | ⭐ 2 stars |
| 🔗 [add-dictionary](https://github.com/massao000/add-dictionary) | - | - | ⭐ 3 stars |
| 🔗 [j-moshi](https://github.com/nu-dialogue/j-moshi) | - | - | ⭐ 283 stars |
| 🔗 [jatts](https://github.com/unilight/jatts) | - | - | ⭐ 44 stars |
| 🔗 [tsukasa-speech](https://github.com/respaired/tsukasa-speech) | - | - | ⭐ 59 stars |
| 🔗 [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) | - | - | ⭐ 2 stars |
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 33 stars |
| 🔗 [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) | - | - | ⭐ 1 stars |
| 🔗 [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) | - | - | ⭐ 39 stars |
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 33 stars |
| 🔗 [manga109api](https://github.com/manga109/manga109api) | 📥 83/week | 📦 44k total | ⭐ 127 stars |
| 🔗 [fastrtc-jp](https://github.com/route250/fastrtc-jp) | - | - | ⭐ 4 stars |
| 🔗 [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) | - | - | ⭐ 14 stars |
| 🔗 [pocket-researcher](https://github.com/u-masao/pocket-researcher) | - | - | ⭐ 11 stars |
| 🔗 [jtransbench](https://github.com/webbigdata-jp/jtransbench) | - | - | ⭐ 12 stars |
| 🔗 [easyllasa](https://github.com/zuntan03/easyllasa) | - | - | ⭐ 21 stars |
| 🔗 [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) | - | - | ⭐ 106 stars |
| 🔗 [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) | - | - | ⭐ 11 stars |
| 🔗 [pitchbench](https://github.com/shewiiii/pitchbench) | - | - | ⭐ 1 stars |
| 🔗 [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) | - | - | ⭐ 2 stars |


## C++

### Morphology analysis
High-performance libraries for Japanese morphological analysis

 * [mecab](https://github.com/taku910/mecab) - Yet another Japanese morphological analyzer
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++ (a Morphological Analyzer Toolkit)
 * [kytea](https://github.com/neubig/kytea) - The Kyoto Text Analysis Toolkit for word segmentation and pronunciation estimation, etc.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [mecab](https://github.com/taku910/mecab) | - | - | ⭐ 1.1k stars |
| 🔗 [jumanpp](https://github.com/ku-nlp/jumanpp) | - | - | ⭐ 402 stars |
| 🔗 [kytea](https://github.com/neubig/kytea) | - | - | ⭐ 211 stars |

### Parsing
Libraries for dependency and syntactic parsing of Japanese sentences

 * [cabocha](https://github.com/taku910/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [knp](https://github.com/ku-nlp/knp) - A Japanese Parser


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [cabocha](https://github.com/taku910/cabocha) | - | - | ⭐ 117 stars |
| 🔗 [knp](https://github.com/ku-nlp/knp) | - | - | ⭐ 33 stars |

### Others
Other Japanese NLP and text processing libraries

 * [jsc](https://github.com/yohokuno/jsc) - Joint source channel model for Japanese Kana Kanji conversion, Chinese pinyin input and CJE mixed input.
 * [aquaskk](https://github.com/codefirst/aquaskk) - An input method without morphological analysis.
 * [mozc](https://github.com/google/mozc) - Mozc - a Japanese Input Method Editor designed for multi-platform
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch: An (Exact|Prefix|Approximate) String Matching Library
 * [resembla](https://github.com/tuem/resembla) - Resembla: Word-based Japanese similar sentence search library
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ SKK-like Japanese Input Method Editor for Windows


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [jsc](https://github.com/yohokuno/jsc) | - | - | ⭐ 15 stars |
| 🔗 [aquaskk](https://github.com/codefirst/aquaskk) | - | - | ⭐ 365 stars |
| 🔗 [mozc](https://github.com/google/mozc) | - | - | ⭐ 2.8k stars |
| 🔗 [trimatch](https://github.com/tuem/trimatch) | - | - | ⭐ 2 stars |
| 🔗 [resembla](https://github.com/tuem/resembla) | - | - | ⭐ 73 stars |
| 🔗 [corvusskk](https://github.com/nathancorvussolis/corvusskk) | - | - | ⭐ 346 stars |


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


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [lindera](https://github.com/lindera-morphology/lindera) | - | 📦 728k total | ⭐ 545 stars |
| 🔗 [vaporetto](https://github.com/daac-tools/vaporetto) | - | 📦 144k total | ⭐ 248 stars |
| 🔗 [goya](https://github.com/Leko/goya) | - | 📦 11k total | ⭐ 81 stars |
| 🔗 [vibrato](https://github.com/daac-tools/vibrato) | - | 📦 48k total | ⭐ 386 stars |
| 🔗 [yoin](https://github.com/agatan/yoin) | - | 📦 2.9k total | ⭐ 26 stars |
| 🔗 [mecab-rs](https://github.com/tsurai/mecab-rs) | - | 📦 38k total | ⭐ 65 stars |
| 🔗 [awabi](https://github.com/nakagami/awabi) | - | 📦 24k total | ⭐ 11 stars |
| 🔗 [kanpyo](https://github.com/togatoga/kanpyo) | - | 📦 2.5k total | ⭐ 106 stars |


### Converter
Crates for script and character conversion in Japanese text

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - Utility library for checking and converting between Japanese characters - Hiragana, Katakana - and Romaji
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - A Rust library to convert Japanese Half-width-kana[半角ｶﾅ] and Wide-alphanumeric[全角英数] into normal ones
 * [kana](https://github.com/gbrlsnchs/kana) - [Mirror] CLI program for transliterating romaji text to either hiragana or katakana
 * [kanaria](https://github.com/samunohito/kanaria) - このライブラリは、ひらがな・カタカナ、半角・全角の相互変換や判別を始めとした機能を提供します。
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - 日本の住所を都道府県/市区町村/町名/その他に分割するライブラリです
 * [yosina](https://github.com/yosina-lib/yosina) - Yosina is a transliteration library deals with the letters and symbols used in Japanese writing.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) | - | 📦 240k total | ⭐ 85 stars |
| 🔗 [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) | - | 📦 59k total | ⭐ 19 stars |
| 🔗 [kana](https://github.com/gbrlsnchs/kana) | - | - | ⭐ 11 stars |
| 🔗 [kanaria](https://github.com/samunohito/kanaria) | - | - | ⭐ 21 stars |
| 🔗 [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) | - | - | ⭐ 9 stars |
| 🔗 [yosina](https://github.com/yosina-lib/yosina) | - | - | ⭐ 20 stars |


### Search engine library
Libraries for Japanese full-text search and indexing

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy.
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - A Tantivy tokenizer using Vibrato.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) | - | 📦 140k total | ⭐ 65 stars |
| 🔗 [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) | - | 📦 1.5k total | ⭐ 3 stars |


### Others
Supplementary crates for Japanese text and IME processing

 * [daachorse](https://github.com/daac-tools/daachorse) - A fast implementation of the Aho-Corasick algorithm using the compact double-array data structure in Rust.
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - Finding all pairs of similar documents time- and memory-efficiently
 * [crawdad](https://github.com/daac-tools/crawdad) - Rust library of natural language dictionaries using character-wise double-array tries.
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) -  Comparison code of various tokenizers
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - Here provides benchmark tools to compare the performance of data structures for string matching.
 * [vime](https://github.com/algon-320/vime) - Using Vim as an input method for X11 apps
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXのコア
 * [akaza](https://github.com/akaza-im/akaza) - Yet another Japanese IME for IBus/Linux
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - A free online, self-hostable, multilang Japanese dictionary.
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - Google 日本語入力用DvorakJPローマ字テーブル / DvorakJP Roman Table for Google Japanese Input
 * [niinii](https://github.com/Netdex/niinii) -  Japanese glossator for assisted reading of text using Ichiran
 * [cskk](https://github.com/naokiri/cskk) - SKK (Simple Kana Kanji henkan) library
 * [japanki](https://github.com/tysonwu/japanki) - Learn Japanese vocabs 🇯🇵 by doing quizzes on CLI!
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - Japanese text preprocessor for Text-to-Speech applications (OpenJTalk rewrite in rust language)
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - 裁判例のデータ一覧を裁判所のホームページ(https://www.courts.go.jp/index.html) をスクレイピングして生成するソフトウェア
 * [jisho](https://github.com/eagleflo/jisho) - Jisho is a CLI tool & Rust library that provides a Japanese-English dictionary.
 * [kanalizer](https://github.com/voicevox/kanalizer) - 英単語から読みを推測するライブラリ。
 * [koharu](https://github.com/mayocream/koharu) - Automated manga translation tool with LLM, written in Rust.
 * [yomine](https://github.com/mcgrizzz/yomine) - A Japanese vocabulary mining tool designed to help language learners mine new words and expressions.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [daachorse](https://github.com/daac-tools/daachorse) | - | 📦 600k total | ⭐ 236 stars |
| 🔗 [find-simdoc](https://github.com/legalforce-research/find-simdoc) | - | 📦 29k total | ⭐ 62 stars |
| 🔗 [crawdad](https://github.com/daac-tools/crawdad) | - | 📦 52k total | ⭐ 36 stars |
| 🔗 [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) | - | - | ⭐ 4 stars |
| 🔗 [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) | - | - | ⭐ 3 stars |
| 🔗 [vime](https://github.com/algon-320/vime) | - | - | ⭐ 231 stars |
| 🔗 [voicevox_core](https://github.com/VOICEVOX/voicevox_core) | - | - | ⭐ 1k stars |
| 🔗 [akaza](https://github.com/akaza-im/akaza) | - | - | ⭐ 223 stars |
| 🔗 [Jotoba](https://github.com/WeDontPanic/Jotoba) | - | - | ⭐ 194 stars |
| 🔗 [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) | - | - | ⭐ 55 stars |
| 🔗 [niinii](https://github.com/Netdex/niinii) | - | - | ⭐ 14 stars |
| 🔗 [cskk](https://github.com/naokiri/cskk) | - | - | ⭐ 78 stars |
| 🔗 [japanki](https://github.com/tysonwu/japanki) | - | - | ⭐ 3 stars |
| 🔗 [jpreprocess](https://github.com/jpreprocess/jpreprocess) | - | - | ⭐ 49 stars |
| 🔗 [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) | - | - | ⭐ 5 stars |
| 🔗 [jisho](https://github.com/eagleflo/jisho) | - | - | ⭐ 17 stars |
| 🔗 [kanalizer](https://github.com/voicevox/kanalizer) | - | - | ⭐ 23 stars |
| 🔗 [koharu](https://github.com/mayocream/koharu) | - | - | ⭐ 233 stars |
| 🔗 [yomine](https://github.com/mcgrizzz/yomine) | - | - | ⭐ 28 stars |


## JavaScript

### Morphology analysis
Japanese morphological analysis libraries for browser and Node.js

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - JavaScript implementation of Japanese morphological analyzer
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) -  Rakuten MA - morphological analyzer (word segmentor + PoS Tagger) for Chinese and Japanese written purely in JavaScript.
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - Yet another mecab wrapper for nodejs
 * [juman-bin](https://github.com/thammin/juman-bin) - a User-Extensible Morphological Analyzer for Japanese. 日本語形態素解析システム
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - Asynchronous japanese morphological analyser using MeCab.


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [kuromoji.js](https://github.com/takuyaa/kuromoji.js) | 📥 125k/week/week | 📦 7.2M total | ⭐ 945 stars |
| 🔗 [rakutenma](https://github.com/rakuten-nlp/rakutenma) | 📥 5/week/week | 📦 1k total | ⭐ 472 stars |
| 🔗 [node-mecab-ya](https://github.com/golbin/mecab-ya) | 📥 124/week/week | 📦 6.5k total | ⭐ 110 stars |
| 🔗 [juman-bin](https://github.com/thammin/juman-bin) | 📥 3/week/week | 📦 371 total | ⭐ 3 stars |
| 🔗 [node-mecab-async](https://github.com/hecomi/node-mecab-async) | 📥 5.3k/week/week | 📦 357k total | ⭐ 103 stars |


### Converter
Libraries for converting Japanese scripts and readings

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - Japanese language library for converting Japanese sentence to Hiragana, Katakana or Romaji with furigana and okurigana modes supported.
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - Kuromoji morphological analyzer for kuroshiro.
 * [hepburn](https://github.com/lovell/hepburn) - Node.js module for converting Japanese Hiragana and Katakana script to, and from, Romaji using Hepburn romanisation
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - Converts Japanese Numerals into number
 * [jslingua](https://github.com/kariminf/jslingua) - Javascript libraries to process text: Arabic, Japanese, etc.
 * [WanaKana](https://github.com/WaniKani/WanaKana) - Javascript library for detecting and transliterating Hiragana <--> Katakana <--> Romaji
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - Normalize and fix common issues with Romaji-based Japanese names.
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - Utility collections for making Japanese text old-fashioned
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - オープンソースの住所正規化ライブラリ。
 * [jaconv](https://github.com/kazuhikoarase/jaconv) - 日本語文字変換ライブラリ (javascript)
 * [romaji-conv](https://github.com/koozaki/romaji-conv) - Convert romaji into hiragana
 * [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) - 全国の住所データAPI
 * [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) - テキストの単語を絵文字に変換する


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [kuroshiro](https://github.com/hexenq/kuroshiro) | 📥 7.8k/week/week | 📦 290k total | ⭐ 932 stars |
| 🔗 [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) | 📥 7.4k/week/week | 📦 270k total | ⭐ 67 stars |
| 🔗 [hepburn](https://github.com/lovell/hepburn) | 📥 61k/week/week | 📦 2.6M total | ⭐ 135 stars |
| 🔗 [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) | 📥 36k/week/week | 📦 2M total | ⭐ 59 stars |
| 🔗 [jslingua](https://github.com/kariminf/jslingua) | 📥 78/week/week | 📦 7k total | ⭐ 51 stars |
| 🔗 [WanaKana](https://github.com/WaniKani/WanaKana) | 📥 34k/week/week | 📦 1.9M total | ⭐ 883 stars |
| 🔗 [node-romaji-name](https://github.com/jeresig/node-romaji-name) | 📥 625/week/week | 📦 9.5k total | ⭐ 41 stars |
| 🔗 [kyujitai.js](https://github.com/hakatashi/kyujitai.js) | 📥 19/week/week | 📦 1.2k total | ⭐ 22 stars |
| 🔗 [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) | - | - | ⭐ 938 stars |
| 🔗 [jaconv](https://github.com/kazuhikoarase/jaconv) | - | - | ⭐ 84 stars |
| 🔗 [romaji-conv](https://github.com/koozaki/romaji-conv) | - | - | ⭐ 26 stars |
| 🔗 [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) | - | - | ⭐ 65 stars |
| 🔗 [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) | - | - | ⭐ 2 stars |


### Others
Other libraries for Japanese NLP in JavaScript

 * [bangumi-data](https://github.com/bangumi-data/bangumi-data) - Raw data for Japanese Anime
 * [yomichan](https://github.com/FooSoft/yomichan) - Japanese pop-up dictionary extension for Chrome and Firefox.
 * [proofreading-tool](https://github.com/gecko655/proofreading-tool) - GUIで動作する文書校正ツール GUI tool for textlinting.
 * [kanjigrid](https://github.com/minosvasilias/kanjigrid) - A web-app displaying the 2200 kanji characters taught in James Heisig's "Remembering the Kanji", 6th edition.
 * [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) - Monorepo for Kanji, Furigana, Japanese DB, and others
 * [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) - 文の敬体(ですます調)、常体(である調)を解析するJavaScriptライブラリ
 * [hatsuon](https://github.com/DJTB/hatsuon) - Japanese pitch accent utils
 * [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) - Sentiment Analysis in Japanese. sentiment_ja with JavaScript
 * [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) - mecab-ipadic seed dictionary reader
 * [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) - Well, a different Japanese word everyday.
 * [oskim](https://github.com/esrille/oskim) - Extend GNOME On-Screen Keyboard for Input Methods
 * [tweetMapping](https://github.com/wtnv-lab/tweetMapping) - 東日本大震災発生から24時間以内につぶやかれたジオタグ付きツイートのデジタルアーカイブです。
 * [pitch-accent](https://github.com/shirakaba/pitch-accent) - Predict pitch accent in Japanese
 * [kana2ipa](https://github.com/amanoese/kana2ipa) - 「ひらがな」または「カタカナ」を日本語で発音する際の音声記号(IPA)に変換するコマンド
 * [voicevox](https://github.com/VOICEVOX/voicevox) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXのエディター
 * [kamiya-codec](https://github.com/fasiha/kamiya-codec) - Towards a Japanese verb conjugator and deconjugator based on Taeko Kamiya's *The Handbook of Japanese Verbs* and *The Handbook of Japanese Adjectives and Adverbs* opuses.
 * [closewords](https://github.com/otoneko1102/closewords) - 最も似た単語を単語群から検索する日本語(漢字含む)対応のライブラリ
 * [japanese-analyzer](https://github.com/cokice/japanese-analyzer) - Japanese Sentence Analyzer (日本語文章解析器)


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [bangumi-data](https://github.com/bangumi-data/bangumi-data) | 📥 578/week/week | 📦 63k total | ⭐ 575 stars |
| 🔗 [yomichan](https://github.com/FooSoft/yomichan) | - | - | ⭐ 1.1k stars |
| 🔗 [proofreading-tool](https://github.com/gecko655/proofreading-tool) | - | - | ⭐ 86 stars |
| 🔗 [kanjigrid](https://github.com/minosvasilias/kanjigrid) | - | - | ⭐ 43 stars |
| 🔗 [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) | - | - | ⭐ 60 stars |
| 🔗 [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) | 📥 81k/week/week | 📦 4.5M total | ⭐ 18 stars |
| 🔗 [hatsuon](https://github.com/DJTB/hatsuon) | 📥 24/week/week | 📦 1k total | ⭐ 34 stars |
| 🔗 [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) | - | - | ⭐ 10 stars |
| 🔗 [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) | 📥 104/week/week | 📦 5.4k total | ⭐ 8 stars |
| 🔗 [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) | 📥 2/week/week | 📦 309 total | ⭐ repo not found stars |
| 🔗 [oskim](https://github.com/esrille/oskim) | - | - | ⭐ 2 stars |
| 🔗 [tweetMapping](https://github.com/wtnv-lab/tweetMapping) | - | - | ⭐ 25 stars |
| 🔗 [pitch-accent](https://github.com/shirakaba/pitch-accent) | 📥 0/week/week | 📦 85 total | ⭐ 2 stars |
| 🔗 [kana2ipa](https://github.com/amanoese/kana2ipa) | - | - | ⭐ 16 stars |
| 🔗 [voicevox](https://github.com/VOICEVOX/voicevox) | - | - | ⭐ 3k stars |
| 🔗 [kamiya-codec](https://github.com/fasiha/kamiya-codec) | - | - | ⭐ 17 stars |
| 🔗 [closewords](https://github.com/otoneko1102/closewords) | - | - | ⭐ 1 stars |
| 🔗 [japanese-analyzer](https://github.com/cokice/japanese-analyzer) | - | - | ⭐ 582 stars |


## Go

### Morphology analysis
Lightweight Japanese morphological analysis libraries in Go

 * [kagome](https://github.com/ikawaha/kagome) - Self-contained Japanese Morphological Analyzer written in pure Go


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [kagome](https://github.com/ikawaha/kagome) | - | - | ⭐ 915 stars |


### Others
Additional Go-based Japanese text processing libraries

 * [ojosama](https://github.com/jiro4989/ojosama) - テキストを壱百満天原サロメお嬢様風の口調に変換します
 * [nihongo](https://github.com/gojp/nihongo) - Japanese Dictionary
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - External dictionary importer for Yomichan.
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - THE IDOLM@STER words dictionary for Japanese IME (by imas-db.jp)
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - Kanji transliteration to hiragana/katakana/romaji, in Go
 * [go-moji](https://github.com/ktnyt/go-moji) - A Go library for Zenkaku/Hankaku conversion
 * [ojichat](https://github.com/greymd/ojichat) - おじさんがLINEやメールで送ってきそうな文を生成する
 * [name](https://github.com/kuniwak/name) - Name Searcher in Japanese


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [ojosama](https://github.com/jiro4989/ojosama) | - | - | ⭐ 385 stars |
| 🔗 [nihongo](https://github.com/gojp/nihongo) | - | - | ⭐ 81 stars |
| 🔗 [yomichan-import](https://github.com/FooSoft/yomichan-import) | - | - | ⭐ 85 stars |
| 🔗 [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) | - | - | ⭐ 29 stars |
| 🔗 [go-kakasi](https://github.com/sarumaj/go-kakasi) | - | - | ⭐ 6 stars |
| 🔗 [go-moji](https://github.com/ktnyt/go-moji) | - | - | ⭐ 20 stars |
| 🔗 [ojichat](https://github.com/greymd/ojichat) | - | - | ⭐ 1.3k stars |
| 🔗 [name](https://github.com/kuniwak/name) | - | - | ⭐ 10 stars |


## Java

### Morphology analysis
Japanese morphological analysis and dictionary management libraries

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji is a self-contained and very easy to use Japanese morphological analyzer designed for search
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - A lexicon for Sudachi
 * [meval](https://github.com/teru-oka-1933/meval) - 形態素解析器性能評価システム MevAL


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [kuromoji](https://github.com/atilika/kuromoji) | - | - | ⭐ 1k stars |
| 🔗 [Sudachi](https://github.com/WorksApplications/Sudachi) | - | - | ⭐ 913 stars |
| 🔗 [SudachiDict](https://github.com/WorksApplications/SudachiDict) | - | - | ⭐ 269 stars |
| 🔗 [meval](https://github.com/teru-oka-1933/meval) | - | - | ⭐ 7 stars |


### Others
Java libraries for Japanese NLP and OCR

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - Java library for identifying Japanese characters from images
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - Java library and command-line tool to transliterate Japanese kanji to romaji (Latin alphabet)
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Kanji transliteration to hiragana/katakana/romaji, in Java
 * [Kamite](https://github.com/fauu/Kamite) - A desktop language immersion companion for learners of Japanese
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - Async Japanese Tokenizer Native Plugin for React Native for iOS and Android
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - Japanese analyzer uses kuromoji japanese tokenizer for ElasticSearch
 * [moji4j](https://github.com/andree-surya/moji4j) - A Java library to converts between Japanese Hiragana, Katakana, and Romaji scripts.
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - Japanese text normalizer for mecab-neologd
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - The Japanese analysis plugin for elasticsearch


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) | - | - | ⭐ 202 stars |
| 🔗 [jakaroma](https://github.com/nicolas-raoul/jakaroma) | - | - | ⭐ 67 stars |
| 🔗 [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) | - | - | ⭐ 55 stars |
| 🔗 [Kamite](https://github.com/fauu/Kamite) | - | - | ⭐ 128 stars |
| 🔗 [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) | - | - | ⭐ 38 stars |
| 🔗 [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) | - | - | ⭐ 29 stars |
| 🔗 [moji4j](https://github.com/andree-surya/moji4j) | - | - | ⭐ 33 stars |
| 🔗 [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) | - | - | ⭐ 4 stars |
| 🔗 [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) | - | - | ⭐ 216 stars |


## Pretrained model

### Word2Vec
Models that convert words into numeric vectors to capture semantic similarity

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - Word2vec (word to vectors) approach for Japanese language using Gensim and Mecab.
 * [chiVe](https://github.com/WorksApplications/chiVe) - Japanese word embedding with Sudachi and NWJC
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - elmo-japanese
 * [embedrank](https://github.com/yagays/embedrank) - Python Implementation of EmbedRank
 * [aovec](https://github.com/eggplants/aovec) - Easy aozorabunko Word2Vec Builder - 青空文庫全書籍のWord2Vecビルダー+構築済みモデル
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - This is a repository for the AI LAB article "係り受けに基づく日本語単語埋込 (Dependency-based Japanese Word Embeddings)" ( Article URL https://ai-lab.lapras.com/nlp/japanese-word-embedding/)
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - Yet Another Japanese-Wikipedia Entity Vectors
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 最新の日本語Wikipediaのダンプデータから，MeCabを用いてIPA辞書と最新のNeologd辞書の両方で形態素解析を実施し，その結果に基づいた word2vec，fastText，GloVeの単語分散表現を学習するためのスクリプト


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) | - | - | ⭐ 86 stars |
| 🔗 [chiVe](https://github.com/WorksApplications/chiVe) | - | - | ⭐ 168 stars |
| 🔗 [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) | - | - | ⭐ 5 stars |
| 🔗 [embedrank](https://github.com/yagays/embedrank) | - | - | ⭐ 48 stars |
| 🔗 [aovec](https://github.com/eggplants/aovec) | 📥 81/week | 📦 78k total | ⭐ 3 stars |
| 🔗 [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) | - | - | ⭐ 8 stars |
| 🔗 [jawikivec](https://github.com/wikiwikification/jawikivec) | - | - | ⭐ 2 stars |
| 🔗 [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) | - | - | ⭐ 11 stars |


### Transformer based models
Models that use self-attention to understand context and perform advanced language tasks

 * [bert-japanese](https://github.com/cl-tohoku/bert-japanese) - BERT models for Japanese text.
 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - Code for producing Japanese pretrained models provided by rinna Co., Ltd.
 * [bert-japanese](https://github.com/yoheikikuta/bert-japanese) - BERT with SentencePiece for Japanese text.
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - Japanese tokenizer for Transformers
 * [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) - Code for evaluating Japanese pretrained models provided by NTT Ltd.
 * [shiba](https://github.com/octanove/shiba) - Pytorch implementation and pre-trained Japanese model for CANINE, the efficient character-level transformer.
 * [Dialog](https://github.com/reppy4620/Dialog) - A PyTorch Implementation of japanese chatbot using BERT and Transformer's decoder
 * [language-pretraining](https://github.com/retarfi/language-pretraining) - BERT and ELECTRA models of PyTorch implementations for Japanese text.
 * [medbertjp](https://github.com/ou-medinfo/medbertjp) - Trials of pre-trained BERT models for the medical domain in Japanese.
 * [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) - ILYS-aoba-chatbot
 * [t5-japanese](https://github.com/megagonlabs/t5-japanese) - Codes to pre-train Japanese T5 models
 * [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) - PytorchでBERTの日本語学習済みモデルを利用する
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
 * [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) - 日本語WikipediaコーパスでBERTのPre-Trainedモデルを生成するためのリポジトリ
 * [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) - A Japanese DistilBERT pretrained model, which was trained on Wikipedia.
 * [bert](https://github.com/informatix-inc/bert) - This repository provides snippets to use RoBERTa pre-trained on Japanese corpus. Our dataset consists of Japanese Wikipedia and web-scrolled articles, 25GB in total. The released model is built based on that from HuggingFace.
 * [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) - Laboro DistilBERT Japanese
 * [luke](https://github.com/studio-ousia/luke) - LUKE -- Language Understanding with Knowledge-based Embeddings
 * [GPTSAN](https://github.com/tanreinama/GPTSAN) - General-purpose Swich transformer based Japanese language mode
 * [japanese-clip](https://github.com/rinnakk/japanese-clip) - Japanese CLIP by rinna Co., Ltd.
 * [AcademicBART](https://github.com/EhimeNLP/AcademicBART) - We pretrained a BART-based Japanese masked language model on paper abstracts from the academic database CiNii Articles
 * [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) - We pretrained a RoBERTa-based Japanese masked language model on paper abstracts from the academic database CiNii Articles.
 * [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) - DistilBERT model pre-trained on 131 GB of Japanese web text. The teacher model is BERT-base that built in-house at LINE.
 * [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) - 日本語に翻訳したStanford Alpacaのデータセットを用いてLLaMAをファインチューニングし作成したLow-Rank AdapterのリンクとGenerateサンプルコード
 * [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) - Pretrained models, codes and guidances to pretrain official ALBERT(https://github.com/google-research/albert) on Japanese Wikipedia Resources
 * [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) - Japanese LLaMa experiment
 * [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) - EasyLightChatAssistant は軽量で検閲や規制のないローカル日本語モデルのLightChatAssistant を、KoboldCpp で簡単にお試しする環境です。


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [bert-japanese](https://github.com/cl-tohoku/bert-japanese) | - | - | ⭐ 539 stars |
| 🔗 [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) | - | - | ⭐ repo not found stars |
| 🔗 [bert-japanese](https://github.com/yoheikikuta/bert-japanese) | - | - | ⭐ 498 stars |
| 🔗 [SudachiTra](https://github.com/WorksApplications/SudachiTra) | 📥 586/week | 📦 151k total | ⭐ 79 stars |
| 🔗 [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) | - | - | ⭐ 244 stars |
| 🔗 [shiba](https://github.com/octanove/shiba) | 📥 24/week | 📦 7k total | ⭐ 89 stars |
| 🔗 [Dialog](https://github.com/reppy4620/Dialog) | - | - | ⭐ 73 stars |
| 🔗 [language-pretraining](https://github.com/retarfi/language-pretraining) | - | - | ⭐ 50 stars |
| 🔗 [medbertjp](https://github.com/ou-medinfo/medbertjp) | - | - | ⭐ 12 stars |
| 🔗 [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) | - | - | ⭐ 23 stars |
| 🔗 [t5-japanese](https://github.com/megagonlabs/t5-japanese) | - | - | ⭐ 40 stars |
| 🔗 [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) | - | - | ⭐ 35 stars |
| 🔗 [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) | - | - | ⭐ 73 stars |
| 🔗 [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) | - | - | ⭐ 23 stars |
| 🔗 [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) | - | - | ⭐ 16 stars |
| 🔗 [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) | - | - | ⭐ 40 stars |
| 🔗 [sbert-ja](https://github.com/colorfulscoop/sbert-ja) | - | - | ⭐ 11 stars |
| 🔗 [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) | - | - | ⭐ 7 stars |
| 🔗 [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) | - | - | ⭐ 323 stars |
| 🔗 [text2text-japanese](https://github.com/tanreinama/text2text-japanese) | - | - | ⭐ 33 stars |
| 🔗 [gpt-ja](https://github.com/colorfulscoop/gpt-ja) | - | - | ⭐ 3 stars |
| 🔗 [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) | - | - | ⭐ 1 stars |
| 🔗 [albert-japanese](https://github.com/alinear-corp/albert-japanese) | - | - | ⭐ 33 stars |
| 🔗 [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) | - | - | ⭐ 115 stars |
| 🔗 [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) | - | - | ⭐ 161 stars |
| 🔗 [bert](https://github.com/informatix-inc/bert) | - | - | ⭐ 28 stars |
| 🔗 [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) | - | - | ⭐ 16 stars |
| 🔗 [luke](https://github.com/studio-ousia/luke) | - | - | ⭐ 728 stars |
| 🔗 [GPTSAN](https://github.com/tanreinama/GPTSAN) | - | - | ⭐ 118 stars |
| 🔗 [japanese-clip](https://github.com/rinnakk/japanese-clip) | - | - | ⭐ repo not found stars |
| 🔗 [AcademicBART](https://github.com/EhimeNLP/AcademicBART) | - | - | ⭐ 2 stars |
| 🔗 [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | - | - | ⭐ 9 stars |
| 🔗 [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) | - | - | ⭐ 46 stars |
| 🔗 [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) | - | - | ⭐ 141 stars |
| 🔗 [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) | - | - | ⭐ 13 stars |
| 🔗 [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) | - | - | ⭐ 54 stars |
| 🔗 [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) | - | - | ⭐ 37 stars |


## ChatGPT
Resources for using ChatGPT and APIs for Japanese dialogue and text generation

 * [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) - ChatGPTを使ってVRChat上でお喋り出来るようにするプログラム。
 * [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) - AITuberの基礎となる部分を開発しています
 * [wanna](https://github.com/hirokidaichi/wanna) - Shell command launcher with natural language
 * [ChatdollKit](https://github.com/uezo/ChatdollKit) - ChatdollKit enables you to make your 3D model into a chatbot
 * [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) - GUI for ChatGPT API For Japanese
 * [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) - ChatGPT3.5を搭載した伺かゴースト「AI妹アイちゃん」です。利用には別途ChatGPTのAPIキーが必要です。
 * [vrchatbot](https://github.com/Geson-anko/vrchatbot) - VRChatにAI Botを作るためのリポジトリ
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPTがYouTuberをやります
 * [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) - A chatbox application built using Nuxt 3 powered by Open AI Text completion endpoint. You can select different personality of your AI friend. The default will respond in Japanese. You can use this app to practice your Nihongo skills!
 * [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) - This Chrome extension can translate selected Japanese text to Hiragana by using ChatGPT.
 * [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) - このサンプルでは、Retrieval Augmented Generation パターンを使用して、独自のデータに対してChatGPT のような体験を作成するためのいくつかのアプローチを示しています。
 * [chatvrm](https://github.com/pixiv/chatvrm) - ChatVRMはブラウザで簡単に3Dキャラクターと会話ができるデモアプリケーションです。
 * [sftly-replace](https://github.com/kmizu/sftly-replace) - A Chrome extention to replace the selected text softly
 * [summarize_arxv](https://github.com/rkmt/summarize_arxv) - Summarize arXiv paper with figures
 * [aiavatarkit](https://github.com/uezo/aiavatarkit) - Building AI-based conversational avatars lightning fast
 * [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) - このリポジトリは、神戸市役所でのChatGPTの試行利用に向けて作成したフロー等をソリューション化し公開するものです。
 * [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) - Azure OpenAIを活用したアプリケーション実装のリファレンスを目的として、アプリのサンプル（リファレンスアーキテクチャ、サンプルコードとデプロイ手順）を無償提供しています。
 * [character_chat](https://github.com/mutaguchi/character_chat) - OpenAIのAPIを利用して、設定したキャラクターと日本語で会話するチャットスクリプトです。
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - OpenAIのChatGPT APIをSlack上で利用するためのSlackbotスクリプト (日本語での利用が前提)
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - ChatGPT の Prompt のサンプルです。
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - A Japanese Kanji Flashcard App built using Python and Langchain, enhanced with the intelligence of GPT-4.
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - Evaluating GPT-4 and ChatGPT on Japanese Medical Licensing Examinations
 * [japagen](https://github.com/retrieva/japagen) - 日本語タスクにおけるLLMを用いた疑似学習データ生成の検討
  * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - ChatGPTやCopilotなど各種生成AI用の「日本語]の Prompt のサンプル


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) | - | - | ⭐ 15 stars |
| 🔗 [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) | - | - | ⭐ 5 stars |
| 🔗 [wanna](https://github.com/hirokidaichi/wanna) | 📥 7/week | 📦 19k total | ⭐ 142 stars |
| 🔗 [ChatdollKit](https://github.com/uezo/ChatdollKit) | - | - | ⭐ 1.1k stars |
| 🔗 [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) | - | - | ⭐ 1 stars |
| 🔗 [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) | - | - | ⭐ 26 stars |
| 🔗 [vrchatbot](https://github.com/Geson-anko/vrchatbot) | - | - | ⭐ 28 stars |
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 stars |
| 🔗 [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) | - | - | ⭐ 15 stars |
| 🔗 [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) | - | - | ⭐ 1 stars |
| 🔗 [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) | - | - | ⭐ 46 stars |
| 🔗 [chatvrm](https://github.com/pixiv/chatvrm) | - | - | ⭐ 799 stars |
| 🔗 [sftly-replace](https://github.com/kmizu/sftly-replace) | - | - | ⭐ 4 stars |
| 🔗 [summarize_arxv](https://github.com/rkmt/summarize_arxv) | - | - | ⭐ 173 stars |
| 🔗 [aiavatarkit](https://github.com/uezo/aiavatarkit) | - | - | ⭐ 449 stars |
| 🔗 [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) | - | - | ⭐ repo not found stars |
| 🔗 [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) | - | - | ⭐ 280 stars |
| 🔗 [character_chat](https://github.com/mutaguchi/character_chat) | - | - | ⭐ 16 stars |
| 🔗 [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) | - | - | ⭐ 63 stars |
| 🔗 [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) | - | - | ⭐ 390 stars |
| 🔗 [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) | - | - | ⭐ 6 stars |
| 🔗 [IgakuQA](https://github.com/jungokasai/IgakuQA) | - | - | ⭐ 48 stars |
| 🔗 [japagen](https://github.com/retrieva/japagen) | - | - | ⭐ 1 stars |
| 🔗 [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) | - | - | ⭐ 390 stars |


## Dictionary and IME
Resources for Japanese dictionaries and input method editors (IME)

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - Neologism dictionary based on the language resources on the Web for mecab-ipadic
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - A Japanese accent dictionary generator
 * [jamdict](https://github.com/neocl/jamdict) - Python 3 library for manipulating Jim Breen's JMdict, KanjiDic2, JMnedict and kanji-radical mappings
 * [unidic-py](https://github.com/polm/unidic-py) - Unidic packaged for installation via pip.
 * [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) - Japanese Company Lexicon (JCLdic)
 * [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) - Sudachi向け万病辞書
 * [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) - Generate SKK/MeCab dictionary from Wikipedia(Japanese edition)
 * [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) - dictionary to find emotion related to text
 * [JumanDIC](https://github.com/ku-nlp/JumanDIC) - This repository contains source dictionary files to build dictionaries for JUMAN and Juman++.
 * [ipadic-py](https://github.com/polm/ipadic-py) - IPAdic packaged for easy use from Python.
 * [unidic-lite](https://github.com/polm/unidic-lite) - A small version of UniDic for easy pip installs.
 * [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) - 日本語で絵文字入力をするための IME 追加辞書 orange_book Google 日本語入力などで日本語から絵文字への変換を可能にする IME 拡張辞書
 * [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) - 日英変換・英語略語展開のための IME 追加辞書 orange_book 日本語から英語への和英変換や英語略語の展開を Google 日本語入力や ATOK などで可能にする IME 拡張辞書
 * [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) - ニコニコ大百科とピクシブ百科事典の共通部分のIME辞書
 * [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) - GoogleIME用カタカナ語辞書プロジェクトのアーカイブです。Project archive of Google IME user dictionary from Katakana word ( Japanese loanword ) to English.
 * [emoticon](https://github.com/tiwanari/emoticon) - Google日本語入力の顔文字辞書∩(,,Ò‿Ó,,)∩
 * [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) - open source mozc dictionaryをMeCab辞書のフォーマットに変換したものです。
 * [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) - 電音IME: Microsoft IMEなどで利用することを想定した「電音部」関連用語の辞書
 * [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) - Microsoft IMEなどで利用することを想定した「にじさんじ」関連用語の用語辞書です。
 * [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) - Microsoft IMEなどで利用することを想定した、現状判明している全てのポケモンの名前を網羅した用語辞書です。
 * [EJDict](https://github.com/kujirahand/EJDict) - English-Japanese Dictionary data (Public Domain) EJDict-hand
 * [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) - 贵樣ばこゐ辞畫を使て正レい日本语を使ラことが出來ゑ。
 * [genshin-dict](https://github.com/kotofurumiya/genshin-dict) - Windows/macOSで使える原神の単語辞書です
 * [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) - JMdict and JMnedict in JSON format
 * [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) - Convert external words into Mozc system dictionary
 * [mh-dict-jp](https://github.com/utubo/mh-dict-jp) - MonsterHunterのユーザー辞書を作りたい…
 * [jitenbot](https://github.com/stephenmk/jitenbot) - Convert data from Japanese dictionary websites and applications into portable file formats
 * [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) - Neologism dictionary based on the language resources on the Web for mecab-unidic
 * [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) - ホロライブ（ホロライブプロダクション）に関する辞書ファイルです。./dictionary フォルダ内のテキストファイルを使って、IMEに単語を追加できます。詳細はREADME.mdをご覧ください。
 * [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) - JMdict, JMnedict, KANJIDIC for Yomitan/Yomichan.
 * [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) - JLPT level tags for words in Yomichan
 * [Jitendex](https://github.com/stephenmk/Jitendex) - A free and openly licensed Japanese-to-English dictionary compatible with multiple dictionary clients
 * [jiten](https://github.com/obfusk/jiten) - japanese android/cli/web dictionary based on jmdict/kanjidic — 日本語　辞典　和英辞典　漢英字典　和独辞典　和蘭辞典
 * [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) - Pixiv Encyclopedia Dictionary for Yomitan
 * [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) - うちなーぐち辞典（沖縄語辞典）
 * [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) - Japanese and Chinese dictionaries for Yomitan.
 * [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) - マウスオーバーした単語を自動で読み取る汎用辞書ツール
 * [jisyo](https://github.com/skk-dict/jisyo) - かな漢字変換エンジン SKKのための新しい辞書形式
 * [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) - 日本語の読みから Emoji に変換するための SKK 辞書 😂
 * [anthy](https://github.com/netsphere-labs/anthy) - Anthy is a kana-kanji conversion engine for Japanese. It converts roma-ji to kana, and the kana text to a mixed kana and kanji.
 * [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) - AWSサービス名のGoogle日本語入力向けの辞書
 * [cl-skkserv](https://github.com/tani/cl-skkserv) - Common LispによるSKK辞書サーバーとその拡張
 * [anthy](https://github.com/xorgy/anthy) - Anthy maintenance
 * [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) - Anthy Unicode - Another Anthy
 * [azooKey](https://github.com/ensan-hcl/azooKey) - azooKey: A Japanese Keyboard iOS Application Fully Developed in Swift
 * [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) - Japanese Input Method "azooKey" for Desktop, supporting macOS
 * [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) - Japanese input method for fcitx5, powered by azooKey engine
 * [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) - Mozc UT Place Name Dictionary is a dictionary converted from the Japan Post's ZIP code data for Mozc.
 * [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) - Kana-Kanji Conversion Module written in Swift
 * [libkkc](https://github.com/ueno/libkkc) - Japanese Kana Kanji conversion input method library
 * [libskk](https://github.com/ueno/libskk) - Japanese SKK input method library
 * [kanayomi-dict](https://github.com/warihima/kanayomi-dict) - openjtalk形式のユーザー辞書
 * [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) - 漢字データベースの辞書関連データ
 * [wlsp-classical](https://github.com/yocjyet/wlsp-classical) - 古典日本語の分類語彙表データ
 * [kanji-dict](https://github.com/marmooo/kanji-dict) - 漢字の書き順(筆順)・読み方・画数・部首・用例・成り立ちを調べるための漢字辞書です。Unicode 15.1 のすべての漢字 98,682字を収録しています。
 * [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) - (๑ ᴖ ᴑ ᴖ ๑)みょんかおもじ（旧Kaomoji_proj）はMicrosoft社の入力ソフト、Microsoft IME向けの顔文字の辞書を作成するプロジェクトです。
 * [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) - Kotlin かな漢字変換プログラム
 * [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) - Japanese-English Dictionary using jisho.org with audio, csv export of entries, and preview of dictionary sites.
 * [ichiran](https://github.com/tshatrov/ichiran) - Linguistic tools for texts in Japanese language
 * [mikan](https://github.com/mojyack/mikan) - A Japanese input method.
 * [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) - A quick reference for the material taught in Colloquial Kansai Japanese.
 * [jisho-open](https://github.com/hlorenzi/jisho-open) - Web frontend for the JMdict Japanese-English dictionary project, with study list support!
 * [macskk](https://github.com/mtgto/macskk) - Yet Another macOS SKK Input Method
 * [nandoku](https://github.com/marmooo/nandoku) - 難読漢字を学年別にまとめた辞書です。
 * [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) - A FOSS Japanese IME for Android
 * [anthywl](https://github.com/tadeokondrak/anthywl) - Japanese input method for Sway using libanthy
 * [sekka](https://github.com/kiyoka/sekka) - Yet another Japanese Input Method inspired by SKK.
 * [sumibi](https://github.com/kiyoka/sumibi) - Japanese input method powered by ChatGPT API
 * [jinmei-dict](https://github.com/s1r-j/jinmei-dict) - 辞書データから人名だけを抜き出し、読み仮名（カタカナ）をキーとして、候補となる書き文字をリストで保持するようなJSON形式に整形しています。
 * [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) - スミレ 完全オフラインの日本語キーボードアプリ
 * [japanesearabic](https://github.com/a-hamdi/japanesearabic) - JapaneseArabic Dictionary (日本語・アラビア語辞書) قاموس اللغة اليابانية والعربية (Yomitan)
 * [o-dic](https://github.com/makotoga/o-dic) - 沖縄辞書
 * [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) - SKK 絵文字辞書


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) | - | - | ⭐ 2.8k stars |
| 🔗 [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) | - | - | ⭐ 120 stars |
| 🔗 [jamdict](https://github.com/neocl/jamdict) | 📥 147/week | 📦 48k total | ⭐ 156 stars |
| 🔗 [unidic-py](https://github.com/polm/unidic-py) | 📥 81k/week | 📦 8M total | ⭐ 106 stars |
| 🔗 [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) | - | - | ⭐ 100 stars |
| 🔗 [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) | - | - | ⭐ 7 stars |
| 🔗 [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) | - | - | ⭐ 56 stars |
| 🔗 [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) | - | - | ⭐ 40 stars |
| 🔗 [JumanDIC](https://github.com/ku-nlp/JumanDIC) | - | - | ⭐ 4 stars |
| 🔗 [ipadic-py](https://github.com/polm/ipadic-py) | 📥 63k/week | 📦 6M total | ⭐ 24 stars |
| 🔗 [unidic-lite](https://github.com/polm/unidic-lite) | 📥 76k/week | 📦 8M total | ⭐ 48 stars |
| 🔗 [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) | - | - | ⭐ 365 stars |
| 🔗 [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) | - | - | ⭐ 96 stars |
| 🔗 [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) | - | - | ⭐ 79 stars |
| 🔗 [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) | - | - | ⭐ 55 stars |
| 🔗 [emoticon](https://github.com/tiwanari/emoticon) | - | - | ⭐ 43 stars |
| 🔗 [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) | - | - | ⭐ 10 stars |
| 🔗 [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) | - | - | ⭐ 2 stars |
| 🔗 [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) | - | - | ⭐ 34 stars |
| 🔗 [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) | - | - | ⭐ 0 stars |
| 🔗 [EJDict](https://github.com/kujirahand/EJDict) | - | - | ⭐ 229 stars |
| 🔗 [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) | - | - | ⭐ 26 stars |
| 🔗 [genshin-dict](https://github.com/kotofurumiya/genshin-dict) | - | - | ⭐ 118 stars |
| 🔗 [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) | - | - | ⭐ 305 stars |
| 🔗 [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) | - | - | ⭐ 66 stars |
| 🔗 [mh-dict-jp](https://github.com/utubo/mh-dict-jp) | - | - | ⭐ 4 stars |
| 🔗 [jitenbot](https://github.com/stephenmk/jitenbot) | - | - | ⭐ repo not found stars |
| 🔗 [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) | - | - | ⭐ 86 stars |
| 🔗 [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) | - | - | ⭐ 24 stars |
| 🔗 [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) | - | - | ⭐ 211 stars |
| 🔗 [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) | - | - | ⭐ 109 stars |
| 🔗 [Jitendex](https://github.com/stephenmk/Jitendex) | - | - | ⭐ 416 stars |
| 🔗 [jiten](https://github.com/obfusk/jiten) | - | - | ⭐ 122 stars |
| 🔗 [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) | - | - | ⭐ 41 stars |
| 🔗 [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) | - | - | ⭐ 4 stars |
| 🔗 [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) | - | - | ⭐ 651 stars |
| 🔗 [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) | - | - | ⭐ 72 stars |
| 🔗 [jisyo](https://github.com/skk-dict/jisyo) | - | - | ⭐ 26 stars |
| 🔗 [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) | - | - | ⭐ 29 stars |
| 🔗 [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) | - | - | ⭐ 7 stars |
| 🔗 [cl-skkserv](https://github.com/tani/cl-skkserv) | - | - | ⭐ 31 stars |
| 🔗 [anthy](https://github.com/xorgy/anthy) | - | - | ⭐ 2 stars |
| 🔗 [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) | - | - | ⭐ 36 stars |
| 🔗 [azooKey](https://github.com/ensan-hcl/azooKey) | - | - | ⭐ 527 stars |
| 🔗 [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) | - | - | ⭐ 650 stars |
| 🔗 [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) | - | - | ⭐ 135 stars |
| 🔗 [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) | - | - | ⭐ 20 stars |
| 🔗 [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) | - | - | ⭐ 121 stars |
| 🔗 [libkkc](https://github.com/ueno/libkkc) | - | - | ⭐ 111 stars |
| 🔗 [libskk](https://github.com/ueno/libskk) | - | - | ⭐ 94 stars |
| 🔗 [kanayomi-dict](https://github.com/warihima/kanayomi-dict) | - | - | ⭐ repo not found stars |
| 🔗 [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) | - | - | ⭐ 107 stars |
| 🔗 [wlsp-classical](https://github.com/yocjyet/wlsp-classical) | - | - | ⭐ 2 stars |
| 🔗 [kanji-dict](https://github.com/marmooo/kanji-dict) | - | - | ⭐ 5 stars |
| 🔗 [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) | - | - | ⭐ 11 stars |
| 🔗 [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) | - | - | ⭐ 4 stars |
| 🔗 [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) | - | - | ⭐ 6 stars |
| 🔗 [ichiran](https://github.com/tshatrov/ichiran) | - | - | ⭐ 375 stars |
| 🔗 [mikan](https://github.com/mojyack/mikan) | - | - | ⭐ 24 stars |
| 🔗 [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) | - | - | ⭐ 9 stars |
| 🔗 [jisho-open](https://github.com/hlorenzi/jisho-open) | - | - | ⭐ 56 stars |
| 🔗 [macskk](https://github.com/mtgto/macskk) | - | - | ⭐ 237 stars |
| 🔗 [nandoku](https://github.com/marmooo/nandoku) | - | - | ⭐ 1 stars |
| 🔗 [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) | - | - | ⭐ 2 stars |
| 🔗 [anthywl](https://github.com/tadeokondrak/anthywl) | - | - | ⭐ 33 stars |
| 🔗 [sekka](https://github.com/kiyoka/sekka) | - | - | ⭐ 24 stars |
| 🔗 [sumibi](https://github.com/kiyoka/sumibi) | - | - | ⭐ 32 stars |
| 🔗 [jinmei-dict](https://github.com/s1r-j/jinmei-dict) | - | - | ⭐ 5 stars |
| 🔗 [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) | - | - | ⭐ 183 stars |
| 🔗 [japanesearabic](https://github.com/a-hamdi/japanesearabic) | - | - | ⭐ 16 stars |
| 🔗 [o-dic](https://github.com/makotoga/o-dic) | - | - | ⭐ 5 stars |
| 🔗 [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) | - | - | ⭐ 139 stars |


## Corpus

### Part-of-speech tagging / Named entity recognition
Corpora annotated with part-of-speech tags and named entities

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - Wikipediaを用いた日本語の固有表現抽出データセット
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - Japanese IOB2 tagged corpus for Named Entity Recognition.
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter コーパス
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - Parallel Universal Dependencies.
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - Japanese data from the Google UDT 2.0.
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - Kyoto University Web Document Leads Corpus
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - Annotated Fuman Kaitori Center Corpus
 * [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) - Long-unit-word version of UD_Japanese-GSD


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) | - | - | ⭐ 142 stars |
| 🔗 [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) | - | - | ⭐ 61 stars |
| 🔗 [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) | - | - | ⭐ 21 stars |
| 🔗 [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) | - | - | ⭐ 0 stars |
| 🔗 [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) | - | - | ⭐ 28 stars |
| 🔗 [KWDLC](https://github.com/ku-nlp/KWDLC) | - | - | ⭐ 83 stars |
| 🔗 [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) | - | - | ⭐ 18 stars |
| 🔗 [anthy](https://github.com/netsphere-labs/anthy) | - | - | ⭐ 14 stars |
| 🔗 [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) | - | - | ⭐ 3 stars |


### Parallel corpus
Bilingual corpora containing aligned sentences for translation tasks

 * [small_parallel_enja](https://github.com/odashi/small_parallel_enja) - 50k English-Japanese Parallel Corpus for Machine Translation Benchmark.
 * [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) - A Web Crawled Corpus for Japanese-Chinese NMT
 * [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) - Coursera Corpus Mining and Multistage Fine-Tuning for Improving Lectures Translation
 * [JESC](https://github.com/rpryzant/JESC) - A large parallel corpus of English and Japanese
 * [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) - AMI Meeting Parallel Corpus
 * [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) - This directory includes a giant Japanese-English subtitle corpus. The raw data comes from the Stanford’s JESC project.
 * [jesc_small](https://github.com/yusugomori/jesc_small) - Small Japanese-English Subtitle Corpus
 * [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) - 禁止用語や単語レベルを考慮した日英対訳コーパスです。
 * [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) - CJK computer science terms comparison / 中日韓電腦科學術語對照 / 日中韓のコンピュータ科学の用語対照 / 한·중·일 전산학 용어 대조
 * [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) - Scripts for creating a Japanese-English parallel corpus and training NMT models
 * [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) - google-vs-deepl-je
 * [matcha](https://github.com/ehimenlp/matcha) - 訪日観光客向けメディアMATCHAの記事から、日本語のテキスト平易化のためのデータセットを構築しました。
 * [en-ja-el](https://github.com/shigashiyama/en-ja-el) - EnJaEL: En-Ja Parallel Entity Linking Dataset (Version 1.0)


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [small_parallel_enja](https://github.com/odashi/small_parallel_enja) | - | - | ⭐ 97 stars |
| 🔗 [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) | - | - | ⭐ 14 stars |
| 🔗 [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) | - | - | ⭐ 15 stars |
| 🔗 [JESC](https://github.com/rpryzant/JESC) | - | - | ⭐ 87 stars |
| 🔗 [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) | - | - | ⭐ 11 stars |
| 🔗 [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) | - | - | ⭐ 5 stars |
| 🔗 [jesc_small](https://github.com/yusugomori/jesc_small) | - | - | ⭐ 3 stars |
| 🔗 [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) | - | - | ⭐ 6 stars |
| 🔗 [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) | - | - | ⭐ 142 stars |
| 🔗 [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) | - | - | ⭐ 18 stars |
| 🔗 [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) | - | - | ⭐ 4 stars |
| 🔗 [matcha](https://github.com/ehimenlp/matcha) | - | - | ⭐ 6 stars |
| 🔗 [en-ja-el](https://github.com/shigashiyama/en-ja-el) | - | - | ⭐ 1 stars |


### Dialog corpus
Collections of conversation data for training dialogue systems

 * [JMRD](https://github.com/ku-nlp/JMRD) - Japanese Movie Recommendation Dialogue dataset
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - おーぷん2ちゃんねるをクロールして作成した対話コーパス
 * [BSD](https://github.com/tsuruoka-lab/BSD) - The Business Scene Dialogue corpus
 * [asdc](https://github.com/megagonlabs/asdc) - Accommodation Search Dialog Corpus (宿泊施設探索対話コーパス)
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - 日本語の対話データ for seq2seq etc
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - This repository contains the Japanese–English bilingual chat corpus BPersona-chat published in the paper Chat Translation Error Detection for Assisting Cross-lingual Communications at AACL-IJCNLP 2022's Workshop Eval4NLP 2022.
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - Japanese Daily Dialogue, or 日本語日常対話コーパス in Japanese, is a high-quality multi-turn dialogue dataset containing daily conversations on five topics: dailylife, school, travel, health, and entertainment.
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - LLM構築用の日本語チャットデータセット
 * [kokorochat](https://github.com/uec-inabalab/kokorochat) - ロールプレイで収集した日本語のカウンセリング対話データセット


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [JMRD](https://github.com/ku-nlp/JMRD) | - | - | ⭐ 28 stars |
| 🔗 [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) | - | - | ⭐ 99 stars |
| 🔗 [BSD](https://github.com/tsuruoka-lab/BSD) | - | - | ⭐ 71 stars |
| 🔗 [asdc](https://github.com/megagonlabs/asdc) | - | - | ⭐ 25 stars |
| 🔗 [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) | - | - | ⭐ 3 stars |
| 🔗 [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) | - | - | ⭐ 5 stars |
| 🔗 [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) | - | - | ⭐ 54 stars |
| 🔗 [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) | - | - | ⭐ 86 stars |
| 🔗 [kokorochat](https://github.com/uec-inabalab/kokorochat) | - | - | ⭐ 15 stars |


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
 * [emoji-ja](https://github.com/yagays/emoji-ja) - UNICODE絵文字の日本語読み/キーワード/分類辞書
 * [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) - Wikipediaから作成した日本語名寄せデータセット
 * [ja.text8](https://github.com/Hironsan/ja.text8) - Japanese text8 corpus for word embedding.
 * [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) - 3行要約データセット
 * [japanese](https://github.com/hingston/japanese) - This repo contains a list of the 44,998 most common Japanese words in order of frequency, as determined by the University of Leeds Corpus.
 * [kanji-frequency](https://github.com/scriptin/kanji-frequency) - Kanji usage frequency data collected from various sources
 * [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) - TEDxJP-10K ASR Evaluation Dataset
 * [CoARiJ](https://github.com/chakki-works/CoARiJ) - Corpus of Annual Reports in Japan
 * [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) - 日本語で書かれた技術書を収集した生コーパス/ツール
 * [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) - Chunked word annotation for ITA corpus
 * [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) - Utility scripts for preprocessing Wikipedia texts for NLP
 * [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) - 日本語における不適切表現を収集します。自然言語処理の時のデータクリーニング用等に使えると思います。
 * [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) - 参議院の公式ウェブサイトから会派、議員、議案、質問主意書のデータを整理しました。
 * [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) - 国会議案データベース：衆議院
 * [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) - STAIR captions: large-scale Japanese image caption dataset
 * [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) - Japanese Translation of Winograd Schema Challenge
 * [speechBSD](https://github.com/ku-nlp/speechBSD) - An extension of the BSD corpus with audio and speaker attribute information
 * [ita-corpus](https://github.com/mmorise/ita-corpus) - ITAコーパスの文章リスト
 * [rohan4600](https://github.com/mmorise/rohan4600) - モーラバランス型日本語コーパス
 * [anlp-jp-history](https://github.com/whym/anlp-jp-history) - 言語処理学会年次大会講演の全リスト・機械可読版など
 * [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) - 敬語変換タスクにおける評価用データセット
 * [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) - English loanwords in Japanese
 * [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) - Japanese-Wikipedia Wikification Corpus
 * [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) - This is the corpus of Japanese Text that general policy speech of prime minister of Japan
 * [wrime](https://github.com/ids-cv/wrime) - WRIME: 主観と客観の感情分析データセット
 * [jtubespeech](https://github.com/sarulab-speech/jtubespeech) - JTubeSpeech: Corpus of Japanese speech collected from YouTube
 * [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) - 日本語Wikipediaで使用される頻出単語のリスト
 * [kokkosho_data](https://github.com/rindybell/kokkosho_data) - 車両不具合情報に関するデータセット
 * [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) - デジタル化資料OCRテキスト化事業において作成されたOCR学習用データセット
 * [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) - 全国書誌データから作成した振り仮名のデータセット
 * [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) - JVS (Japanese versatile speech) コーパスの自作のラベル
 * [hirakanadic](https://github.com/po3rin/hirakanadic) - Allows Sudachi to normalize from hiragana to katakana from any compound word list
 * [animedb](https://github.com/anilogia/animedb) - 約100年に渡るアニメ作品リストデータベース
 * [security_words](https://github.com/SaitoLab/security_words) - サイバーセキュリティに関連する公的な組織の日英対応
 * [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) - 日本の国会議員のデータ
 * [honkoku-data](https://github.com/yuta1984/honkoku-data) - 歴史資料の市民参加型翻刻プラットフォーム「みんなで翻刻」のテキストデータ置き場です。 / Transcription texts created on Minna de Honkoku (https://honkoku.org), a crowdsourced transcription platform for historical Japanese documents.
 * [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) - wikiHow dataset (Japanese version)
 * [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) - Engineer Vocabulary List in Japanese/English
 * [JSICK](https://github.com/verypluming/JSICK) - Japanese Sentences Involving Compositional Knowledge (JSICK) Dataset/JSICK-stress Test Set
 * [phishurl-list](https://github.com/JPCERTCC/phishurl-list) - Phishing URL dataset from JPCERT/CC
 * [jcms](https://github.com/shigashiyama/jcms) - A Japanese Corpus of Many Specialized Domains (JCMS)
 * [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) - text-only archives of www.aozora.gr.jp
 * [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) - friendly_JA is a parallel Japanese-to-Japanese corpus aimed at making Japanese easier by using the Latin/English derived katakana lexicon instead of the standard Sino-Japanese lexicon
 * [topokanji](https://github.com/scriptin/topokanji) - Topologically ordered lists of kanji for effective learning
 * [isbn4groups](https://github.com/uribo/isbn4groups) - ISBN-13における日本語での出版物 (978-4-XXXXXXXXX) に関するデータ等
 * [NMeCab](https://github.com/komutan/NMeCab) - NMeCab: About Japanese morphological analyzer on .NET
 * [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) - デジタル化資料から作成したOCRテキストデータのngram頻度統計情報のデータセット
 * [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) - 2023年1月にリニューアルしたNDL Ngram Viewerのソースコード等一式
 * [data_set](https://github.com/japanese-law-analysis/data_set) - 法律・判例関係のデータセット
 * [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) - WRIME for huggingface datasets
 * [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) - NDL古典籍OCR学習用データセット（みんなで翻刻加工データ）
 * [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) - GIS & Archaeological Simulator. 2023 in development.
 * [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) - Japanese version of LIWC2015
 * [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) - Japanese Livedoor news corpus for huggingface datasets
 * [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) - JGLUE: Japanese General Language Understanding Evaluation for huggingface datasets
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality is a dataset created through crowdsourcing that reflects the commonsense morality of Japanese annotators.
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - COMET-ATOMIC ja
 * [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) - Dialogue Commonsense Graph in Japanese
 * [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) - "Proposal and Evaluation of Japanese Toxicity Schema" provides a schema and dataset for toxicity in the Japanese language.
 * [camera](https://github.com/CyberAgentAILab/camera) - CAMERA (CyberAgent Multimodal Evaluation for Ad Text GeneRAtion) is the Japanese ad text generation dataset.
 * [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) - 日本語フェイクニュースデータセット
 * [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) - jpn_explainable_qa_dataset
 * [copa-japanese](https://github.com/nlp-titech/copa-japanese) - COPA Dataset in Japanese
 * [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) - Word Familiarity Rate for 'Word List by Semantic Principles (WLSP)'
 * [ProSub](https://github.com/matbahasa/ProSub) - A cross-linguistic study of pronoun substitutes and address terms
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality is a dataset created through crowdsourcing that reflects the commonsense morality of Japanese annotators.
 * [ramendb](https://github.com/nuko-yokohama/ramendb) - なんとかデータベース( https://supleks.jp/ )からのスクレイピングツールと収集データ
 * [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) - CAMERA (CyberAgent Multimodal Evaluation for Ad Text GeneRAtion) for huggingface datasets
 * [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) - FactCheckSentenceNLIデータセット
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - databricks/dolly-v2-12b の学習データに使用されたdatabricks-dolly-15k.jsonl を日本語に翻訳したデータセットになります。
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELD is an English-Japanese dataset for emotion-aware speech translation based on MELD.
 * [meconaudio](https://github.com/elith-co-jp/meconaudio) - Mecon Audio(Medical Conference Audio)は厚生労働省主催の先進医療会議の議事録の読み上げデータセットです。
 * [japanese-addresses](https://github.com/geolonia/japanese-addresses) - 全国の町丁目レベル（277,191件）の住所データのオープンデータ
 * [aozorasearch](https://github.com/myokoym/aozorasearch) - The full-text search system for Aozora Bunko by Groonga. 青空文庫全文検索ライブラリ兼Webアプリ。
 * [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) - This repository contains scripts to reproduce the LLM-jp corpus.
 * [alpaca_ja](https://github.com/shi3z/alpaca_ja) - alpacaデータセットを日本語化したものです
 * [instruction_ja](https://github.com/megagonlabs/instruction_ja) - Japanese instruction data (日本語指示データ)
 * [japanese-family-names](https://github.com/siikamiika/japanese-family-names) - Top 5000 Japanese family names, with readings, ordered by frequency.
 * [kanji-data-media](https://github.com/kanjialive/kanji-data-media) - Japanese language data on kanji, radicals, media files, fonts and related resources from Kanji alive
 * [reazonspeech](https://github.com/reazon-research/reazonspeech) - Construct large-scale Japanese audio corpus at home
 * [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) - 青空文庫及びサピエの点字データから作成した振り仮名のデータセット
 * [koniwa](https://github.com/koniwa/koniwa) - An open collection of annotated voices in Japanese language
 * [JMMLU](https://github.com/nlp-waseda/JMMLU) - 日本語マルチタスク言語理解ベンチマーク Japanese Massive Multitask Language Understanding Benchmark
 * [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) - 青空文庫振り仮名注釈付き音声コーパスのデータセット
 * [jqara](https://github.com/hotchpotch/jqara) - JQaRA: Japanese Question Answering with Retrieval Augmentation - 検索拡張(RAG)評価のための日本語Q&Aデータセット
 * [jemhopqa](https://github.com/aiishii/jemhopqa) - JEMHopQA (Japanese Explainable Multi-hop Question Answering) is a Japanese multi-hop QA dataset that can evaluate internal reasoning.
 * [jacred](https://github.com/youmima/jacred) - Repository for Japanese Document-level Relation Extraction Dataset (plan to be released in March).
 * [jades](https://github.com/naist-nlp/jades) - JADES is a dataset for text simplification in Japanese, described in "JADES: New Text Simplification Dataset in Japanese Targeted at Non-Native Speakers" (the paper will be available soon).
 * [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) - 2023年8月にメルボルン大学から公開された安全性評価データセット『Do-Not-Answer』を日本語LLMの評価においても使用できるように日本語に自動翻訳し、さらに日本文化も考慮して修正したデータセット。
 * [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) - OpenAssistant のオープンソースデータ OASST1 を日本語に翻訳したデータセットになります。
 * [jacwir](https://github.com/hotchpotch/jacwir) - JaCWIR: Japanese Casual Web IR - 日本語情報検索評価のための小規模でカジュアルなWebタイトルと概要のデータセット
 * [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) - 日本語学習者のための科学技術業界でよく使われる片仮名と元の単語対照表
 * [j-unimorph](https://github.com/cl-tohoku/j-unimorph) - Dataset of UniMorph in Japanese
 * [GazeVQA](https://github.com/riken-grp/GazeVQA) - Dataset for the LREC-COLING 2024 paper "A Gaze-grounded Visual Question Answering Dataset for Clarifying Ambiguous Japanese Questions"
 * [J-CRe3](https://github.com/riken-grp/J-CRe3) - Code for J-CRe3 experiments (Ueda et al., LREC-COLING, 2024)
 * [jmed-llm](https://github.com/sociocom/jmed-llm) - JMED-LLM: Japanese Medical Evaluation Dataset for Large Language Models
 * [lawtext](https://github.com/yamachig/lawtext) - Plain text format for Japanese law
 * [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) - OCR処理プログラム研究開発事業において作成されたOCR学習用データセット
 * [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) - 話題に基づく語義曖昧性解消評価セット
 * [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) - Jamp: Controlled Japanese Temporal Inference Dataset for Evaluating Generalization Capacity of Language Models
 * [JSeM](https://github.com/DaisukeBekki/JSeM) - Japanese semantic test suite (FraCaS counterpart and extensions)
 * [niilc-qa](https://github.com/mynlp/niilc-qa) - NIILC QA data
 * [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) - Dataset of paper "Verification of Chain-of-Thought Prompting in Japanese"
 * [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) - This is a Japanese text corpus that consists of Wikipedia articles with various linguistic annotations.
 * [elaws-history](https://github.com/kissge/elaws-history) - e-Gov 法令検索で配布されている「全ての法令データ」を定期的にダウンロードし、アーカイブしています
 * [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) - Japanese-RP-BenchはLLMの日本語ロールプレイ能力を測定するためのベンチマークです。
 * [hdic](https://github.com/shikeda/hdic) - HDIC : Integrated Database of Hanzi Dictionaries in Early Japan
 * [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) - Awesome Japan Open Data - 日本のオープンデータ情報一覧・まとめ
 * [kanji-data](https://github.com/mimneko/kanji-data) - 常用漢字表他、漢字に関するデータ
 * [openchj-genji](https://github.com/togiso/openchj-genji) - 「源氏物語」形態論情報データ
 * [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) - This repository contains data for our paper "AdParaphrase: Paraphrase Dataset for Analyzing Linguistic Features toward Generating Attractive Ad Texts".
 * [Jamp_sp](https://github.com/ynklab/Jamp_sp) - アスペクトを考慮した日本語時間推論データセットの構築（Jamp_sp: Controlled Japanese Temporal Inference Dataset Considering Aspect）
 * [jnli-neg](https://github.com/asahi-y/jnli-neg) - 否定理解能力を評価するための日本語言語推論データセット JNLI-Neg の公開用リポジトリです。
 * [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) - This repository provides Python implementation for building Swallow Corpus Version 1, a large Japanese web corpus (Okazaki et al., 2024), from Common Crawl archives.
 * [jalecon](https://github.com/naist-nlp/jalecon) - A Dataset of Japanese Lexical Complexity for Non-Native Readers
 * [multils-japanese](https://github.com/naist-nlp/multils-japanese) - MultiLS-Japanese Lexical Complexity Prediction and Lexical Simplification Dataset for Japanese: annotator profiles, unaggregated annotation, and annotatation guidelines.
 * [nwjc](https://github.com/masayu-a/nwjc) - NINJAL Web Japanese Corpus
 * [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) - Dataset introduced in the paper "Towards Fully Automated Manga Translation" presented in AAAI21
 * [public-annotations](https://github.com/manga109/public-annotations) - Various annotations of Manga109 dataset
 * [gimei](https://github.com/willnet/gimei) - random Japanese name and address generator
 * [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) - 日本語言語モデルの安全性の振る舞いを評価するテストセット
 * [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) - A simple, open-source collection of Japanese onomatopoeic and mimetic sound words in JSON format. With manga samples.
 * [kanji](https://github.com/sylhare/kanji) - List of japanese kanji radicals to learn
 * [jethics](https://github.com/language-media-lab/jethics) - 日本語道徳理解度評価用データセットJETHICSの概説ページ (to be update)


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) | - | - | ⭐ 77 stars |
| 🔗 [kanji-data](https://github.com/davidluzgouveia/kanji-data) | - | - | ⭐ 192 stars |
| 🔗 [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) | - | - | ⭐ 102 stars |
| 🔗 [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) | - | - | ⭐ 32 stars |
| 🔗 [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) | - | - | ⭐ 141 stars |
| 🔗 [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) | - | - | ⭐ 108 stars |
| 🔗 [JaNLI](https://github.com/verypluming/JaNLI) | - | - | ⭐ 17 stars |
| 🔗 [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) | - | - | ⭐ 18 stars |
| 🔗 [emoji-ja](https://github.com/yagays/emoji-ja) | - | - | ⭐ 82 stars |
| 🔗 [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) | - | - | ⭐ 35 stars |
| 🔗 [ja.text8](https://github.com/Hironsan/ja.text8) | - | - | ⭐ 111 stars |
| 🔗 [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) | - | - | ⭐ 31 stars |
| 🔗 [japanese](https://github.com/hingston/japanese) | - | - | ⭐ 82 stars |
| 🔗 [kanji-frequency](https://github.com/scriptin/kanji-frequency) | - | - | ⭐ 152 stars |
| 🔗 [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) | - | - | ⭐ 24 stars |
| 🔗 [CoARiJ](https://github.com/chakki-works/CoARiJ) | - | - | ⭐ 94 stars |
| 🔗 [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) | - | - | ⭐ 26 stars |
| 🔗 [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) | - | - | ⭐ 5 stars |
| 🔗 [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) | - | - | ⭐ 78 stars |
| 🔗 [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) | - | - | ⭐ 197 stars |
| 🔗 [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) | - | - | ⭐ 104 stars |
| 🔗 [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) | - | - | ⭐ 173 stars |
| 🔗 [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) | - | - | ⭐ 90 stars |
| 🔗 [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) | - | - | ⭐ 6 stars |
| 🔗 [speechBSD](https://github.com/ku-nlp/speechBSD) | - | - | ⭐ 3 stars |
| 🔗 [ita-corpus](https://github.com/mmorise/ita-corpus) | - | - | ⭐ 216 stars |
| 🔗 [rohan4600](https://github.com/mmorise/rohan4600) | - | - | ⭐ 64 stars |
| 🔗 [anlp-jp-history](https://github.com/whym/anlp-jp-history) | - | - | ⭐ 3 stars |
| 🔗 [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) | - | - | ⭐ 21 stars |
| 🔗 [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) | - | - | ⭐ 19 stars |
| 🔗 [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) | - | - | ⭐ 4 stars |
| 🔗 [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) | - | - | ⭐ 6 stars |
| 🔗 [wrime](https://github.com/ids-cv/wrime) | - | - | ⭐ 172 stars |
| 🔗 [jtubespeech](https://github.com/sarulab-speech/jtubespeech) | - | - | ⭐ 228 stars |
| 🔗 [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) | - | - | ⭐ 2 stars |
| 🔗 [kokkosho_data](https://github.com/rindybell/kokkosho_data) | - | - | ⭐ 1 stars |
| 🔗 [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) | - | - | ⭐ 74 stars |
| 🔗 [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) | - | - | ⭐ 28 stars |
| 🔗 [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) | - | - | ⭐ 31 stars |
| 🔗 [hirakanadic](https://github.com/po3rin/hirakanadic) | 📥 21/week | 📦 13k total | ⭐ 7 stars |
| 🔗 [animedb](https://github.com/anilogia/animedb) | - | - | ⭐ 330 stars |
| 🔗 [security_words](https://github.com/SaitoLab/security_words) | - | - | ⭐ 27 stars |
| 🔗 [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) | - | - | ⭐ 3 stars |
| 🔗 [honkoku-data](https://github.com/yuta1984/honkoku-data) | - | - | ⭐ 17 stars |
| 🔗 [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) | - | - | ⭐ 36 stars |
| 🔗 [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) | - | - | ⭐ 1.8k stars |
| 🔗 [JSICK](https://github.com/verypluming/JSICK) | - | - | ⭐ 45 stars |
| 🔗 [phishurl-list](https://github.com/JPCERTCC/phishurl-list) | - | - | ⭐ 195 stars |
| 🔗 [jcms](https://github.com/shigashiyama/jcms) | - | - | ⭐ 9 stars |
| 🔗 [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) | - | - | ⭐ 82 stars |
| 🔗 [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) | - | - | ⭐ repo not found stars |
| 🔗 [topokanji](https://github.com/scriptin/topokanji) | - | - | ⭐ 196 stars |
| 🔗 [isbn4groups](https://github.com/uribo/isbn4groups) | - | - | ⭐ 1 stars |
| 🔗 [NMeCab](https://github.com/komutan/NMeCab) | - | - | ⭐ 96 stars |
| 🔗 [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) | - | - | ⭐ 14 stars |
| 🔗 [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) | - | - | ⭐ 3 stars |
| 🔗 [data_set](https://github.com/japanese-law-analysis/data_set) | - | - | ⭐ 42 stars |
| 🔗 [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) | - | - | ⭐ 4 stars |
| 🔗 [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) | - | - | ⭐ 16 stars |
| 🔗 [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) | - | - | ⭐ 175 stars |
| 🔗 [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) | - | - | ⭐ 13 stars |
| 🔗 [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) | - | - | ⭐ 2 stars |
| 🔗 [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) | - | - | ⭐ 12 stars |
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 stars |
| 🔗 [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) | - | - | ⭐ 31 stars |
| 🔗 [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) | - | - | ⭐ 6 stars |
| 🔗 [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) | - | - | ⭐ 21 stars |
| 🔗 [camera](https://github.com/CyberAgentAILab/camera) | - | - | ⭐ 26 stars |
| 🔗 [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) | - | - | ⭐ 20 stars |
| 🔗 [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) | - | - | ⭐ repo not found stars |
| 🔗 [copa-japanese](https://github.com/nlp-titech/copa-japanese) | - | - | ⭐ 1 stars |
| 🔗 [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) | - | - | ⭐ 10 stars |
| 🔗 [ProSub](https://github.com/matbahasa/ProSub) | - | - | ⭐ 5 stars |
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 stars |
| 🔗 [ramendb](https://github.com/nuko-yokohama/ramendb) | - | - | ⭐ 7 stars |
| 🔗 [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) | - | - | ⭐ 3 stars |
| 🔗 [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) | - | - | ⭐ 0 stars |
| 🔗 [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) | - | - | ⭐ 88 stars |
| 🔗 [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) | - | - | ⭐ 0 stars |
| 🔗 [meconaudio](https://github.com/elith-co-jp/meconaudio) | - | - | ⭐ 9 stars |
| 🔗 [japanese-addresses](https://github.com/geolonia/japanese-addresses) | - | - | ⭐ 748 stars |
| 🔗 [aozorasearch](https://github.com/myokoym/aozorasearch) | - | - | ⭐ 21 stars |
| 🔗 [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) | - | - | ⭐ 43 stars |
| 🔗 [alpaca_ja](https://github.com/shi3z/alpaca_ja) | - | - | ⭐ 86 stars |
| 🔗 [instruction_ja](https://github.com/megagonlabs/instruction_ja) | - | - | ⭐ 24 stars |
| 🔗 [japanese-family-names](https://github.com/siikamiika/japanese-family-names) | - | - | ⭐ 17 stars |
| 🔗 [kanji-data-media](https://github.com/kanjialive/kanji-data-media) | - | - | ⭐ 395 stars |
| 🔗 [reazonspeech](https://github.com/reazon-research/reazonspeech) | - | - | ⭐ 339 stars |
| 🔗 [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) | - | - | ⭐ 17 stars |
| 🔗 [koniwa](https://github.com/koniwa/koniwa) | - | - | ⭐ 54 stars |
| 🔗 [JMMLU](https://github.com/nlp-waseda/JMMLU) | - | - | ⭐ 38 stars |
| 🔗 [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) | - | - | ⭐ 41 stars |
| 🔗 [jqara](https://github.com/hotchpotch/jqara) | - | - | ⭐ 37 stars |
| 🔗 [jemhopqa](https://github.com/aiishii/jemhopqa) | - | - | ⭐ 29 stars |
| 🔗 [jacred](https://github.com/youmima/jacred) | - | - | ⭐ 7 stars |
| 🔗 [jades](https://github.com/naist-nlp/jades) | - | - | ⭐ 0 stars |
| 🔗 [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) | - | - | ⭐ 24 stars |
| 🔗 [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) | - | - | ⭐ 16 stars |
| 🔗 [jacwir](https://github.com/hotchpotch/jacwir) | - | - | ⭐ 8 stars |
| 🔗 [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) | - | - | ⭐ 3 stars |
| 🔗 [j-unimorph](https://github.com/cl-tohoku/j-unimorph) | - | - | ⭐ 7 stars |
| 🔗 [GazeVQA](https://github.com/riken-grp/GazeVQA) | - | - | ⭐ 0 stars |
| 🔗 [J-CRe3](https://github.com/riken-grp/J-CRe3) | - | - | ⭐ 9 stars |
| 🔗 [jmed-llm](https://github.com/sociocom/jmed-llm) | - | - | ⭐ 53 stars |
| 🔗 [lawtext](https://github.com/yamachig/lawtext) | - | - | ⭐ 89 stars |
| 🔗 [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) | - | - | ⭐ 14 stars |
| 🔗 [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) | - | - | ⭐ 2 stars |
| 🔗 [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) | - | - | ⭐ 1 stars |
| 🔗 [JSeM](https://github.com/DaisukeBekki/JSeM) | - | - | ⭐ 13 stars |
| 🔗 [niilc-qa](https://github.com/mynlp/niilc-qa) | - | - | ⭐ 18 stars |
| 🔗 [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) | - | - | ⭐ 5 stars |
| 🔗 [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) | - | - | ⭐ 11 stars |
| 🔗 [elaws-history](https://github.com/kissge/elaws-history) | - | - | ⭐ 4 stars |
| 🔗 [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) | - | - | ⭐ 15 stars |
| 🔗 [hdic](https://github.com/shikeda/hdic) | - | - | ⭐ 40 stars |
| 🔗 [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) | - | - | ⭐ 150 stars |
| 🔗 [kanji-data](https://github.com/mimneko/kanji-data) | - | - | ⭐ 8 stars |
| 🔗 [openchj-genji](https://github.com/togiso/openchj-genji) | - | - | ⭐ 2 stars |
| 🔗 [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) | - | - | ⭐ 1 stars |
| 🔗 [Jamp_sp](https://github.com/ynklab/Jamp_sp) | - | - | ⭐ 0 stars |
| 🔗 [jnli-neg](https://github.com/asahi-y/jnli-neg) | - | - | ⭐ 0 stars |
| 🔗 [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) | - | - | ⭐ 5 stars |
| 🔗 [jalecon](https://github.com/naist-nlp/jalecon) | - | - | ⭐ 5 stars |
| 🔗 [multils-japanese](https://github.com/naist-nlp/multils-japanese) | - | - | ⭐ 0 stars |
| 🔗 [nwjc](https://github.com/masayu-a/nwjc) | - | - | ⭐ 10 stars |
| 🔗 [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) | - | - | ⭐ 195 stars |
| 🔗 [gimei](https://github.com/willnet/gimei) | - | - | ⭐ 424 stars |
| 🔗 [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) | - | - | ⭐ 9 stars |
| 🔗 [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) | - | - | ⭐ 6 stars |
| 🔗 [kanji](https://github.com/sylhare/kanji) | - | - | ⭐ 28 stars |
| 🔗 [jethics](https://github.com/language-media-lab/jethics) | - | - | ⭐ 2 stars |


## Tutorial
Guides and tutorials for learning Japanese NLP tools and techniques

 * [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) - spaCy tutorial in English and Japanese. spacy-transformers, BERT, GiNZA.
 * [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) - Tutorial to train fastText with Japanese corpus
 * [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) - AllenNLP-NER-ja: AllenNLP による日本語を対象とした固有表現抽出
 * [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) - Experiment for Japanese Text classification using chariot and PyTorch
 * [ginza-examples](https://github.com/poyo46/ginza-examples) - 日本語NLPライブラリGiNZAのすゝめ
 * [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) - DocumentClassificationUsingBERT-Japanese
 * [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) - Google Colaboratoryで日本語のBERTを動かす方法です。
 * [bert-book](https://github.com/stockmarkteam/bert-book) - 「BERTによる自然言語処理入門: Transformersを使った実践プログラミング」サポートページ
 * [janome-tutorial](https://github.com/mocobeta/janome-tutorial) - Janome を使ったテキストマイニング入門チュートリアルです。
 * [handson-language-models](https://github.com/hnishi/handson-language-models) - 日本語の言語モデルのハンズオン資料です
 * [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) - Google Colabで日本語テキスト推論を試す
 * [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) - deep-learning-with-pytorchの日本語版repositoryです。
 * [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) -【2023年版】BERTによるテキスト分類
 * [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) - ディープラーニングによる自然言語処理（共立出版）のサポートページです
 * [llm-book](https://github.com/ghmagazine/llm-book) - 「大規模言語モデル入門」（技術評論社, 2023）のGitHubリポジトリ
 * [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) - NLP2024 チュートリアル３ 作って学ぶ日本語大規模言語モデル - 環境構築手順とソースコード
 * [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) - 日本語情報検索チュートリアル
 * [nlpbook](https://github.com/mamorlis/nlpbook) - 「自然言語処理の教科書」サポートサイト
 * [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) - 作って学ぶ正規表現エンジン
 * [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) - 【2024年版】BERTによるテキスト分類
 * [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) - Fine-Tuning Google Gemma for Japanese Instructions
 * [nlp100v2020](https://github.com/upura/nlp100v2020) - 「言語処理100本ノック 2020」をPythonで解く
 * [textmining-ja](https://github.com/paithiov909/textmining-ja) - Rによる自然言語処理・テキスト分析の練習
 * [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) - NLP2025 のチュートリアル「地理情報と言語処理 実践入門」の資料とソースコード
 * [nlp100v2025](https://github.com/upura/nlp100v2025) - 「言語処理100本ノック 2025」をPythonで解く
 * [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) - 『トピックモデル』(機械学習プロフェッショナルシリーズ)のノート
 * [slp2025](https://github.com/ryota-komatsu/slp2025) -音学シンポジウム2025チュートリアル「マルチモーダル大規模言語モデル入門」資料
 * [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) - インプレス出版「IT基礎教養 自然言語処理＆画像解析」
 * [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) - 書籍「現場で活用するための生成AIエージェント実践入門」（講談社サイエンティフィック社）で利用されるソースコード
 * [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) - 2024年度 立教大学大学院 人工知能科学研究科 自然言語処理特論
 * [support-genai-book](https://github.com/yoheikikuta/support-genai-book) - 原論文から解き明かす生成AI（技術評論社）のサポートページです


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) | - | - | ⭐ 63 stars |
| 🔗 [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) | - | - | ⭐ 205 stars |
| 🔗 [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) | - | - | ⭐ 5 stars |
| 🔗 [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) | - | - | ⭐ 5 stars |
| 🔗 [ginza-examples](https://github.com/poyo46/ginza-examples) | - | - | ⭐ 16 stars |
| 🔗 [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) | - | - | ⭐ 0 stars |
| 🔗 [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) | - | - | ⭐ 29 stars |
| 🔗 [bert-book](https://github.com/stockmarkteam/bert-book) | - | - | ⭐ 263 stars |
| 🔗 [janome-tutorial](https://github.com/mocobeta/janome-tutorial) | - | - | ⭐ 31 stars |
| 🔗 [handson-language-models](https://github.com/hnishi/handson-language-models) | - | - | ⭐ 3 stars |
| 🔗 [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) | - | - | ⭐ 6 stars |
| 🔗 [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) | - | - | ⭐ 142 stars |
| 🔗 [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) | - | - | ⭐ 236 stars |
| 🔗 [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) | - | - | ⭐ 10 stars |
| 🔗 [llm-book](https://github.com/ghmagazine/llm-book) | - | - | ⭐ 447 stars |
| 🔗 [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) | - | - | ⭐ 112 stars |
| 🔗 [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) | - | - | ⭐ 3 stars |
| 🔗 [nlpbook](https://github.com/mamorlis/nlpbook) | - | - | ⭐ 14 stars |
| 🔗 [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) | - | - | ⭐ 22 stars |
| 🔗 [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) | - | - | ⭐ 30 stars |
| 🔗 [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) | - | - | ⭐ repo not found stars |
| 🔗 [nlp100v2020](https://github.com/upura/nlp100v2020) | - | - | ⭐ 91 stars |
| 🔗 [textmining-ja](https://github.com/paithiov909/textmining-ja) | - | - | ⭐ 3 stars |
| 🔗 [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) | - | - | ⭐ 17 stars |
| 🔗 [nlp100v2025](https://github.com/upura/nlp100v2025) | - | - | ⭐ 91 stars |
| 🔗 [public-annotations](https://github.com/manga109/public-annotations) | - | - | ⭐ 12 stars |
| 🔗 [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) | - | - | ⭐ 4 stars |
| 🔗 [slp2025](https://github.com/ryota-komatsu/slp2025) | - | - | ⭐ 60 stars |
| 🔗 [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) | - | - | ⭐ 4 stars |
| 🔗 [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) | - | - | ⭐ 165 stars |
| 🔗 [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) | - | - | ⭐ repo not found stars |
| 🔗 [support-genai-book](https://github.com/yoheikikuta/support-genai-book) | - | - | ⭐ 80 stars |


## Research summary
Summaries of studies and papers in Japanese NLP research

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - A list of pre-trained BERT models for Japanese with word/subword tokenization + vocabulary construction algorithm information
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 文法誤り訂正に関する日本語文献を収集・分類するためのリポジトリ
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - lists of text corpus and more (mainly Japanese)
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - ディープラーニングモデルの性能を体系的に最大化するためのプレイブック
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - Trying to consolidate japanese phonetic, and in particular pitch accent resources into one list
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - オープンソースの日本語LLMまとめ


|Name|downloads/week|total downloads|stars|
-|-|-|-
| 🔗 [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) | - | - | ⭐ 131 stars |
| 🔗 [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) | - | - | ⭐ 11 stars |
| 🔗 [dataset-list](https://github.com/ikegami-yukino/dataset-list) | - | - | ⭐ 117 stars |
| 🔗 [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) | - | - | ⭐ 188 stars |
| 🔗 [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) | - | - | ⭐ 117 stars |
| 🔗 [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) | - | - | ⭐ 1.3k stars |


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
