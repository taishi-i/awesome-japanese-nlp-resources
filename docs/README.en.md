# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of resources dedicated to Python libraries, pre-trained models, dictionaries, and corpora of NLP for Japanese

This list includes 490 Japanese NLP repositories.
A tool for searching these repositories is [available](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search) on Hugging Face Spaces.

Your contributions are always welcome!
Please read the [Contribution guidelines](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/contributing.md) before contributing.

Resources that are not available on GitHub are added to the [wiki](https://github.com/taishi-i/awesome-japanese-nlp-resources/wiki).


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)

_☝ By using ChatGPT, we were able to improve the translation results._


## The latest additions 🎉

**Python**
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP Language Model Evaluation Harness

_Updated on Aug 16, 2023_

## Contents
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
 * [Dictionary](#dictionary)
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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[SudachiPy](https://github.com/WorksApplications/SudachiPy)|[![Downloads](https://pepy.tech/badge/sudachipy/week)](https://pepy.tech/project/sudachipy)|[![Downloads](https://pepy.tech/badge/sudachipy)](https://pepy.tech/project/sudachipy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiPy?style=social)|
|[Janome](https://github.com/mocobeta/janome)|[![Downloads](https://pepy.tech/badge/janome/week)](https://pepy.tech/project/janome)|[![Downloads](https://pepy.tech/badge/janome)](https://pepy.tech/project/janome)|![GitHub Repo stars](https://img.shields.io/github/stars/mocobeta/janome?style=social)|
|[mecab-python3](https://github.com/SamuraiT/mecab-python3)|[![Downloads](https://pepy.tech/badge/mecab-python3/week)](https://pepy.tech/project/mecab-python3)|[![Downloads](https://pepy.tech/badge/mecab-python3)](https://pepy.tech/project/mecab-python3)|![GitHub Repo stars](https://img.shields.io/github/stars/SamuraiT/mecab-python3?style=social)|
|[mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python)|[![Downloads](https://pepy.tech/badge/mecab/week)](https://pepy.tech/project/mecab)|[![Downloads](https://pepy.tech/badge/mecab)](https://pepy.tech/project/mecab)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/mecab?style=social)|
|[fugashi](https://github.com/polm/fugashi)|[![Downloads](https://pepy.tech/badge/fugashi/week)](https://pepy.tech/project/fugashi)|[![Downloads](https://pepy.tech/badge/fugashi)](https://pepy.tech/project/fugashi)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/fugashi?style=social)|
|[nagisa](https://github.com/taishi-i/nagisa)|[![Downloads](https://pepy.tech/badge/nagisa/week)](https://pepy.tech/project/nagisa)|[![Downloads](https://pepy.tech/badge/nagisa)](https://pepy.tech/project/nagisa)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/nagisa?style=social)|
|[pyknp](https://github.com/ku-nlp/pyknp)|[![Downloads](https://pepy.tech/badge/pyknp/week)](https://pepy.tech/project/pyknp)|[![Downloads](https://pepy.tech/badge/pyknp)](https://pepy.tech/project/pyknp)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/pyknp?style=social)|
|[Mykytea-python](https://github.com/chezou/Mykytea-python)|[![Downloads](https://pepy.tech/badge/kytea/week)](https://pepy.tech/project/kytea)|[![Downloads](https://pepy.tech/badge/kytea)](https://pepy.tech/project/kytea)|![GitHub Repo stars](https://img.shields.io/github/stars/chezou/Mykytea-python?style=social)|
|[konoha](https://github.com/himkt/konoha)|[![Downloads](https://pepy.tech/badge/konoha/week)](https://pepy.tech/project/konoha)|[![Downloads](https://pepy.tech/badge/konoha)](https://pepy.tech/project/konoha)|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/konoha?style=social)|
|[natto-py](https://github.com/buruzaemon/natto-py)|[![Downloads](https://pepy.tech/badge/natto-py/week)](https://pepy.tech/project/natto-py)|[![Downloads](https://pepy.tech/badge/natto-py)](https://pepy.tech/project/natto-py)|![GitHub Repo stars](https://img.shields.io/github/stars/buruzaemon/natto-py?style=social)|
|[rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python)|[![Downloads](https://pepy.tech/badge/rakutenma/week)](https://pepy.tech/project/rakutenma)|[![Downloads](https://pepy.tech/badge/rakutenma)](https://pepy.tech/project/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/rakutenma-python?style=social)|
|[python-vaporetto](https://github.com/daac-tools/python-vaporetto)|[![Downloads](https://pepy.tech/badge/vaporetto/week)](https://pepy.tech/project/vaporetto)|[![Downloads](https://pepy.tech/badge/vaporetto)](https://pepy.tech/project/vaporetto)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/python-vaporetto?style=social)|
|[dango](https://github.com/mkartawijaya/dango)|[![Downloads](https://pepy.tech/badge/dango/week)](https://pepy.tech/project/dango)|[![Downloads](https://pepy.tech/badge/dango)](https://pepy.tech/project/dango)|![GitHub Repo stars](https://img.shields.io/github/stars/mkartawijaya/dango?style=social)|
|[rhoknp](https://github.com/ku-nlp/rhoknp)|[![Downloads](https://pepy.tech/badge/rhoknp/week)](https://pepy.tech/project/rhoknp)|[![Downloads](https://pepy.tech/badge/rhoknp)](https://pepy.tech/project/rhoknp)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/rhoknp?style=social)|
|[python-vibrato](https://github.com/daac-tools/python-vibrato)|[![Downloads](https://pepy.tech/badge/vibrato/week)](https://pepy.tech/project/vibrato)|[![Downloads](https://pepy.tech/badge/vibrato)](https://pepy.tech/project/vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/python-vibrato?style=social)|


### Parsing

 * [ginza](https://github.com/megagonlabs/ginza) - A Japanese NLP Library using spaCy as framework based on Universal Dependencies
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - Camphr - NLP libary for creating pipeline components
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese with BERT models
 * [depccg](https://github.com/masashi-y/depccg) - A* CCG Parser with a Supertag and Dependency Factored Model
 * [bertknp](https://github.com/ku-nlp/bertknp) - A Japanese dependency parser based on BERT
 * [esupar](https://github.com/KoichiYasuoka/esupar) - Tokenizer POS-Tagger and Dependency-parser with BERT/RoBERTa/DeBERTa models for Japanese and other languages
 * [yomikata](https://github.com/passaglia/yomikata) - Heteronym disambiguation library using a fine-tuned BERT model.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ginza](https://github.com/megagonlabs/ginza)|[![Downloads](https://pepy.tech/badge/ginza/week)](https://pepy.tech/project/ginza)|[![Downloads](https://pepy.tech/badge/ginza)](https://pepy.tech/project/ginza)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ginza?style=social)|
|[cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python)|[![Downloads](https://pepy.tech/badge/cabocha-python/week)](https://pepy.tech/project/cabocha-python)|[![Downloads](https://pepy.tech/badge/cabocha-python)](https://pepy.tech/project/cabocha-python)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/cabocha?style=social)|
|[UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD)|[![Downloads](https://pepy.tech/badge/UniDic2UD/week)](https://pepy.tech/project/UniDic2UD)|[![Downloads](https://pepy.tech/badge/UniDic2UD)](https://pepy.tech/project/UniDic2UD)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/UniDic2UD?style=social)|
|[camphr](https://github.com/PKSHATechnology-Research/camphr)|[![Downloads](https://pepy.tech/badge/camphr/week)](https://pepy.tech/project/camphr)|[![Downloads](https://pepy.tech/badge/camphr)](https://pepy.tech/project/camphr)|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/camphr?style=social)|
|[SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic)|[![Downloads](https://pepy.tech/badge/SuParUniDic/week)](https://pepy.tech/project/SuParUniDic)|[![Downloads](https://pepy.tech/badge/SuParUniDic)](https://pepy.tech/project/SuParUniDic)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/SuPar-UniDic?style=social)|
|[depccg](https://github.com/masashi-y/depccg)|[![Downloads](https://pepy.tech/badge/depccg/week)](https://pepy.tech/project/depccg)|[![Downloads](https://pepy.tech/badge/depccg)](https://pepy.tech/project/depccg)|![GitHub Repo stars](https://img.shields.io/github/stars/masashi-y/depccg?style=social)|
|[bertknp](https://github.com/ku-nlp/bertknp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/bertknp?style=social)|
|[esupar](https://github.com/KoichiYasuoka/esupar)|[![Downloads](https://pepy.tech/badge/esupar/week)](https://pepy.tech/project/esupar)|[![Downloads](https://pepy.tech/badge/esupar)](https://pepy.tech/project/esupar)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/esupar?style=social)|
|[yomikata](https://github.com/passaglia/yomikata)|[![Downloads](https://pepy.tech/badge/yomikata/week)](https://pepy.tech/project/yomikata)|[![Downloads](https://pepy.tech/badge/yomikata)](https://pepy.tech/project/yomikata)|![GitHub Repo stars](https://img.shields.io/github/stars/passaglia/yomikata?style=social)|

### Converter

 * [pykakasi](https://github.com/miurahr/pykakasi) - Lightweight converter from Japanese Kana-kanji sentences into Kana-Roman.
 * [cutlet](https://github.com/polm/cutlet) - Japanese to romaji converter in Python
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - Convert English alphabet to Katakana
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - Converts Arabic numerals, or 'western' style numbers, to a Japanese context.
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Mozc for Python: Kana-Kanji converter
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - Japanese text parser that separates Hiragana/Katakana strings into morae (syllables).
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - Script to convert Japanese text into phoneme sequence.
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - A fast character conversion and transliteration library based on the scheme defined for Japan National Tax Agency (国税庁) 's corporate number (法人番号) system.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[pykakasi](https://github.com/miurahr/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi/week)](https://pepy.tech/project/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi)](https://pepy.tech/project/pykakasi)|![GitHub Repo stars](https://img.shields.io/github/stars/miurahr/pykakasi?style=social)|
|[cutlet](https://github.com/polm/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet/week)](https://pepy.tech/project/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet)](https://pepy.tech/project/cutlet)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/cutlet?style=social)|
|[alphabet2kana](https://github.com/shihono/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana/week)](https://pepy.tech/project/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana)](https://pepy.tech/project/alphabet2kana)|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/alphabet2kana?style=social)|
|[Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Greatdane/Convert-Numbers-to-Japanese?style=social)|
|[mozcpy](https://github.com/ikegami-yukino/mozcpy)|[![Downloads](https://pepy.tech/badge/mozcpy/week)](https://pepy.tech/project/mozcpy)|[![Downloads](https://pepy.tech/badge/mozcpy)](https://pepy.tech/project/mozcpy)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/mozcpy?style=social)|
|[jamorasep](https://github.com/tachi-hi/jamorasep)|[![Downloads](https://pepy.tech/badge/jamorasep/week)](https://pepy.tech/project/jamorasep)|[![Downloads](https://pepy.tech/badge/jamorasep)](https://pepy.tech/project/jamorasep)|![GitHub Repo stars](https://img.shields.io/github/stars/tachi-hi/jamorasep?style=social)|
|[text2phoneme](https://github.com/korguchi/text2phoneme)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/korguchi/text2phoneme?style=social)|
|[jntajis-python](https://github.com/opencollector/jntajis-python)|[![Downloads](https://pepy.tech/badge/jntajis-python/week)](https://pepy.tech/project/jntajis-python)|[![Downloads](https://pepy.tech/badge/jntajis-python)](https://pepy.tech/project/jntajis-python)|![GitHub Repo stars](https://img.shields.io/github/stars/opencollector/jntajis-python?style=social)|


### Preprocessor

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - Japanese text normalizer for mecab-neologd
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - A Python-based tool for converting Japanese characters between Hiragana, Katakana, Hankaku, and Zenkaku.
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - A quick converter for Japanese half-width and full-width characters.
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - A powerful text cleaner for Japanese web texts
 * [HojiChar](https://github.com/HojiChar/HojiChar) - A text preprocessing tool that configures and manages multiple preprocessing steps.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[neologdn](https://github.com/ikegami-yukino/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn/week)](https://pepy.tech/project/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn)](https://pepy.tech/project/neologdn)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/neologdn?style=social)|
|[jaconv](https://github.com/ikegami-yukino/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv/week)](https://pepy.tech/project/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv)](https://pepy.tech/project/jaconv)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/jaconv?style=social)|
|[mojimoji](https://github.com/studio-ousia/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji/week)](https://pepy.tech/project/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji)](https://pepy.tech/project/mojimoji)|![GitHub Repo stars](https://img.shields.io/github/stars/studio-ousia/mojimoji?style=social)|
|[text-cleaning](https://github.com/ku-nlp/text-cleaning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/text-cleaning?style=social)|
|[HojiChar](https://github.com/HojiChar/HojiChar)|[![Downloads](https://pepy.tech/badge/HojiChar/week)](https://pepy.tech/project/HojiChar)|[![Downloads](https://pepy.tech/badge/HojiChar)](https://pepy.tech/project/HojiChar)|![GitHub Repo stars](https://img.shields.io/github/stars/HojiChar/HojiChar?style=social)|


### Sentence spliter

 * [Bunkai](https://github.com/megagonlabs/bunkai) - Sentence boundary disambiguation tool for Japanese texts (日本語文境界判定器)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - Japanese Sentence Breaker
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - Yet another sentence-level tokenizer for the Japanese text
 * [budoux](https://github.com/google/budoux) - Standalone. Small. Language-neutral. BudouX is the successor to Budou, the machine learning powered line break organizer tool.
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - japanese sentence segmentation library for python
 * [hasami](https://github.com/mkartawijaya/hasami) - A tool to perform sentence segmentation on Japanese text
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - Japanese Text Segmenter for Python written in Rust
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - Comparison of Japanese Sentence Segmentation Tools


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bunkai](https://github.com/megagonlabs/bunkai)|[![Downloads](https://pepy.tech/badge/bunkai/week)](https://pepy.tech/project/bunkai)|[![Downloads](https://pepy.tech/badge/bunkai)](https://pepy.tech/project/bunkai)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/bunkai?style=social)|
|[japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker)|[![Downloads](https://pepy.tech/badge/japanese-sentence-breaker/week)](https://pepy.tech/project/japanese-sentence-breaker)|[![Downloads](https://pepy.tech/badge/japanese-sentence-breaker)](https://pepy.tech/project/japanese-sentence-breaker)|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/japanese-sentence-breaker?style=social)|
|[sengiri](https://github.com/ikegami-yukino/sengiri)|[![Downloads](https://pepy.tech/badge/sengiri/week)](https://pepy.tech/project/sengiri)|[![Downloads](https://pepy.tech/badge/sengiri)](https://pepy.tech/project/sengiri)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/sengiri?style=social)|
|[budoux](https://github.com/google/budoux)|[![Downloads](https://pepy.tech/badge/budoux/week)](https://pepy.tech/project/budoux)|[![Downloads](https://pepy.tech/badge/budoux)](https://pepy.tech/project/budoux)|![GitHub Repo stars](https://img.shields.io/github/stars/google/budoux?style=social)|
|[ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter)|[![Downloads](https://pepy.tech/badge/ja_sentence_segmenter/week)](https://pepy.tech/project/ja_sentence_segmenter)|[![Downloads](https://pepy.tech/badge/ja_sentence_segmenter)](https://pepy.tech/project/ja_sentence_segmenter)|![GitHub Repo stars](https://img.shields.io/github/stars/wwwcojp/ja_sentence_segmenter?style=social)|
|[hasami](https://github.com/mkartawijaya/hasami)|[![Downloads](https://pepy.tech/badge/hasami/week)](https://pepy.tech/project/hasami)|[![Downloads](https://pepy.tech/badge/hasami)](https://pepy.tech/project/hasami)|![GitHub Repo stars](https://img.shields.io/github/stars/mkartawijaya/hasami?style=social)|
|[kuzukiri](https://github.com/alinear-corp/kuzukiri)|[![Downloads](https://pepy.tech/badge/kuzukiri/week)](https://pepy.tech/project/kuzukiri)|[![Downloads](https://pepy.tech/badge/kuzukiri)](https://pepy.tech/project/kuzukiri)|![GitHub Repo stars](https://img.shields.io/github/stars/alinear-corp/kuzukiri?style=social)|
|[ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/ja-senter-benchmark?style=social)|


### Sentiment analysis

 * [oseti](https://github.com/ikegami-yukino/oseti) - Dictionary based Sentiment Analysis for Japanese
 * [negapoji](https://github.com/liaoziyang/negapoji) - Japanese document sentiment analysis to determine negative or positive.
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - Emotion analyzer for Japanese text
 * [asari](https://github.com/Hironsan/asari) - Japanese sentiment analyzer implemented in Python.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[oseti](https://github.com/ikegami-yukino/oseti)|[![Downloads](https://pepy.tech/badge/oseti/week)](https://pepy.tech/project/oseti)|[![Downloads](https://pepy.tech/badge/oseti)](https://pepy.tech/project/oseti)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/oseti?style=social)|
|[negapoji](https://github.com/liaoziyang/negapoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/liaoziyang/negapoji?style=social)|
|[pymlask](https://github.com/ikegami-yukino/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask/week)](https://pepy.tech/project/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask)](https://pepy.tech/project/pymlask)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/pymlask?style=social)|
|[asari](https://github.com/Hironsan/asari)|[![Downloads](https://pepy.tech/badge/asari/week)](https://pepy.tech/project/asari)|[![Downloads](https://pepy.tech/badge/asari)](https://pepy.tech/project/asari)|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/asari?style=social)|


### Machine translation

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - An example usage of JParaCrawl pre-trained Neural Machine Translation (NMT) models.
 * [JASS](https://github.com/Mao-KU/JASS) - JASS: Japanese-specific Sequence to Sequence Pre-training for Neural Machine Translation (LREC2020) & Linguistically Driven Multi-Task Pre-Training for Low-Resource Neural Machine Translation (ACM TALLIP)
 * [PheMT](https://github.com/cl-tohoku/PheMT) - A phenomenon-wise evaluation dataset for Japanese-English machine translation robustness. The dataset is based on the MTNT dataset, with additional annotations of four linguistic phenomena; Proper Noun, Abbreviated Noun, Colloquial Expression, and Variant. COLING 2020.
 * [VISA](https://github.com/ku-nlp/VISA) - An ambiguous subtitles dataset for visual scene-aware machine translation


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MorinoseiMorizo/jparacrawl-finetune?style=social)|
|[JASS](https://github.com/Mao-KU/JASS)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Mao-KU/JASS?style=social)|
|[PheMT](https://github.com/cl-tohoku/PheMT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/PheMT?style=social)|
|[VISA](https://github.com/ku-nlp/VISA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/VISA?style=social)|


### Named entity recognition

 * [namaco](https://github.com/chakki-works/namaco) - Character Based Named Entity Recognition.
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia is an Extended Named Entity Dictionary from Wikipedia.
 * [noyaki](https://github.com/ken11/noyaki) - Converts character span label information to tokenized text-based label information.
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - This is a sample code for creating and using a model for named entity recognition task through finetuning of the BERT model.
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - Code for inferring the accuracy of named entity and relation extraction from a case report corpus based on detailed annotation criteria.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namaco](https://github.com/chakki-works/namaco)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/namaco?style=social)|
|[entitypedia](https://github.com/chakki-works/entitypedia)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/entitypedia?style=social)|
|[noyaki](https://github.com/ken11/noyaki)|[![Downloads](https://pepy.tech/badge/noyaki/week)](https://pepy.tech/project/noyaki)|[![Downloads](https://pepy.tech/badge/noyaki)](https://pepy.tech/project/noyaki)|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/noyaki?style=social)|
|[bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/bert-japanese-ner-finetuning?style=social)|
|[joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aih-uth/joint-information-extraction-hs?style=social)|


### OCR

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[manga-ocr](https://github.com/kha-white/manga-ocr)|[![Downloads](https://pepy.tech/badge/manga-ocr/week)](https://pepy.tech/project/manga-ocr)|[![Downloads](https://pepy.tech/badge/manga-ocr)](https://pepy.tech/project/manga-ocr)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/manga-ocr?style=social)|
|[mokuro](https://github.com/kha-white/mokuro)|[![Downloads](https://pepy.tech/badge/mokuro/week)](https://pepy.tech/project/mokuro)|[![Downloads](https://pepy.tech/badge/mokuro)](https://pepy.tech/project/mokuro)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/mokuro?style=social)|
|[handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yas-sim/handwritten-japanese-ocr?style=social)|
|[OCR_Japanease](https://github.com/tanreinama/OCR_Japanease)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/OCR_Japanease?style=social)|
|[ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndlocr_cli?style=social)|
|[donut](https://github.com/clovaai/donut)|[![Downloads](https://pepy.tech/badge/donut-python/week)](https://pepy.tech/project/donut-python)|[![Downloads](https://pepy.tech/badge/donut-python)](https://pepy.tech/project/donut-python)|![GitHub Repo stars](https://img.shields.io/github/stars/clovaai/donut?style=social)|
|[JMTrans](https://github.com/ttop32/JMTrans)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ttop32/JMTrans?style=social)|
|[Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ducanh841988/Kindai-OCR?style=social)|
|[text_recognition](https://github.com/ndl-lab/text_recognition)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/text_recognition?style=social)|
|[Poricom](https://github.com/blueaxis/Poricom)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/blueaxis/Poricom?style=social)|


### Tool for pretrained models

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[JGLUE](https://github.com/yahoojapan/JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yahoojapan/JGLUE?style=social)|
|[ginza-transformers](https://github.com/megagonlabs/ginza-transformers)|[![Downloads](https://pepy.tech/badge/ginza-transformers/week)](https://pepy.tech/project/ginza-transformers)|[![Downloads](https://pepy.tech/badge/ginza-transformers)](https://pepy.tech/project/ginza-transformers)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ginza-transformers?style=social)|
|[t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Jinyamyzk/t5_japanese_dialogue_generation?style=social)|
|[japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Masao-Taketani/japanese_text_classification?style=social)|
|[Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/izuna385/Japanese-BERT-Sentiment-Analyzer?style=social)|
|[jmlm_scoring](https://github.com/minhpqn/jmlm_scoring)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/minhpqn/jmlm_scoring?style=social)|
|[allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model)|[![Downloads](https://pepy.tech/badge/allennlp-shiba/week)](https://pepy.tech/project/allennlp-shiba)|[![Downloads](https://pepy.tech/badge/allennlp-shiba)](https://pepy.tech/project/allennlp-shiba)|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/allennlp-shiba-model?style=social)|
|[evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/evaluate_japanese_w2v?style=social)|
|[gector-ja](https://github.com/jonnyli1125/gector-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jonnyli1125/gector-ja?style=social)|
|[Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-BPEEncoder?style=social)|
|[Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-BPEEncoder_V2?style=social)|
|[transformer-copy](https://github.com/youichiro/transformer-copy)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/youichiro/transformer-copy?style=social)|
|[japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-stable-diffusion?style=social)|
|[nagisa_bert](https://github.com/taishi-i/nagisa_bert)|[![Downloads](https://pepy.tech/badge/nagisa_bert/week)](https://pepy.tech/project/nagisa_bert)|[![Downloads](https://pepy.tech/badge/nagisa_bert)](https://pepy.tech/project/nagisa_bert)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/nagisa_bert?style=social)|
|[prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/prefix-tuning-gpt?style=social)|
|[JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nobu-g/JGLUE-benchmark?style=social)|
|[jptranstokenizer](https://github.com/retarfi/jptranstokenizer)|[![Downloads](https://pepy.tech/badge/jptranstokenizer/week)](https://pepy.tech/project/jptranstokenizer)|[![Downloads](https://pepy.tech/badge/jptranstokenizer)](https://pepy.tech/project/jptranstokenizer)|![GitHub Repo stars](https://img.shields.io/github/stars/retarfi/jptranstokenizer?style=social)|
|[jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Stability-AI/lm-evaluation-harness?style=social)|
|[compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hitachi-nlp/compare-ja-tokenizer?style=social)|
|[lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tdc-yamada-ya/lm-evaluation-harness-jp-stable?style=social)|
|[llm-lora-classification](https://github.com/hppRC/llm-lora-classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/llm-lora-classification?style=social)|
|[jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Stability-AI/lm-evaluation-harness?style=social)|


### Others

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
This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namedivider-python](https://github.com/rskmoi/namedivider-python)|[![Downloads](https://pepy.tech/badge/namedivider-python/week)](https://pepy.tech/project/namedivider-python)|[![Downloads](https://pepy.tech/badge/namedivider-python)](https://pepy.tech/project/namedivider-python)|![GitHub Repo stars](https://img.shields.io/github/stars/rskmoi/namedivider-python?style=social)|
|[asa-python](https://github.com/ikegami-yukino/asa-python)|[![Downloads](https://pepy.tech/badge/asa/week)](https://pepy.tech/project/asa)|[![Downloads](https://pepy.tech/badge/asa)](https://pepy.tech/project/asa)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/asa-python?style=social)|
|[python_asa](https://github.com/Takeuchi-Lab-LM/python_asa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Takeuchi-Lab-LM/python_asa?style=social)|
|[toiro](https://github.com/taishi-i/toiro)|[![Downloads](https://pepy.tech/badge/toiro/week)](https://pepy.tech/project/toiro)|[![Downloads](https://pepy.tech/badge/toiro)](https://pepy.tech/project/toiro)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/toiro?style=social)|
|[ja-timex](https://github.com/yagays/ja-timex)|[![Downloads](https://pepy.tech/badge/ja-timex/week)](https://pepy.tech/project/ja-timex)|[![Downloads](https://pepy.tech/badge/ja-timex)](https://pepy.tech/project/ja-timex)|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/ja-timex?style=social)|
|[JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Kensuke-Mitsuzawa/JapaneseTokenizers?style=social)|
|[daaja](https://github.com/kajyuuen/daaja)|[![Downloads](https://pepy.tech/badge/daaja/week)](https://pepy.tech/project/daaja)|[![Downloads](https://pepy.tech/badge/daaja)](https://pepy.tech/project/daaja)|![GitHub Repo stars](https://img.shields.io/github/stars/kajyuuen/daaja?style=social)|
|[accel-brain-code](https://github.com/accel-brain/accel-brain-code)|[![Downloads](https://pepy.tech/badge/pysummarization/week)](https://pepy.tech/project/pysummarization)|[![Downloads](https://pepy.tech/badge/pysummarization)](https://pepy.tech/project/pysummarization)|![GitHub Repo stars](https://img.shields.io/github/stars/accel-brain/accel-brain-code?style=social)|
|[JGLUE](https://github.com/yahoojapan/JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yahoojapan/JGLUE?style=social)|
|[kyoto-reader](https://github.com/ku-nlp/kyoto-reader)|[![Downloads](https://pepy.tech/badge/kyoto-reader/week)](https://pepy.tech/project/kyoto-reader)|[![Downloads](https://pepy.tech/badge/kyoto-reader)](https://pepy.tech/project/kyoto-reader)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/kyoto-reader?style=social)|
|[nlplot](https://github.com/takapy0210/nlplot)|[![Downloads](https://pepy.tech/badge/nlplot/week)](https://pepy.tech/project/nlplot)|[![Downloads](https://pepy.tech/badge/nlplot)](https://pepy.tech/project/nlplot)|![GitHub Repo stars](https://img.shields.io/github/stars/takapy0210/nlplot?style=social)|
|[rake-ja](https://github.com/kanjirz50/rake-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kanjirz50/rake-ja?style=social)|
|[jel](https://github.com/izuna385/jel)|[![Downloads](https://pepy.tech/badge/jel/week)](https://pepy.tech/project/jel)|[![Downloads](https://pepy.tech/badge/jel)](https://pepy.tech/project/jel)|![GitHub Repo stars](https://img.shields.io/github/stars/izuna385/jel?style=social)|
|[MedNER-J](https://github.com/sociocom/MedNER-J)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/MedNER-J?style=social)|
|[zunda-python](https://github.com/ikegami-yukino/zunda-python)|[![Downloads](https://pepy.tech/badge/zunda-python/week)](https://pepy.tech/project/zunda-python)|[![Downloads](https://pepy.tech/badge/zunda-python)](https://pepy.tech/project/zunda-python)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/zunda-python?style=social)|
|[AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/AIO2_DPR_baseline?style=social)|
|[showcase](https://github.com/cl-tohoku/showcase)|[![Downloads](https://pepy.tech/badge/showcase-parser/week)](https://pepy.tech/project/showcase-parser)|[![Downloads](https://pepy.tech/badge/showcase-parser)](https://pepy.tech/project/showcase-parser)|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/showcase?style=social)|
|[darts-clone-python](https://github.com/rixwew/darts-clone-python)|[![Downloads](https://pepy.tech/badge/dartsclone/week)](https://pepy.tech/project/dartsclone)|[![Downloads](https://pepy.tech/badge/dartsclone)](https://pepy.tech/project/dartsclone)|![GitHub Repo stars](https://img.shields.io/github/stars/rixwew/darts-clone-python?style=social)|
|[jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/jrte-corpus_example?style=social)|
|[desuwa](https://github.com/megagonlabs/desuwa)|[![Downloads](https://pepy.tech/badge/desuwa/week)](https://pepy.tech/project/desuwa)|[![Downloads](https://pepy.tech/badge/desuwa)](https://pepy.tech/project/desuwa)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/desuwa?style=social)|
|[HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/HotPepperGourmetDialogue?style=social)|
|[nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/upura/nlp-recipes-ja?style=social)|
|[Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/olsgaard/Japanese_nlp_scripts?style=social)|
|[DNorm-J](https://github.com/sociocom/DNorm-J)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/DNorm-J?style=social)|
|[pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph)|[![Downloads](https://pepy.tech/badge/pyknp-eventgraph/week)](https://pepy.tech/project/pyknp-eventgraph)|[![Downloads](https://pepy.tech/badge/pyknp-eventgraph)](https://pepy.tech/project/pyknp-eventgraph)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/pyknp-eventgraph?style=social)|
|[ishi](https://github.com/ku-nlp/ishi)|[![Downloads](https://pepy.tech/badge/ishi/week)](https://pepy.tech/project/ishi)|[![Downloads](https://pepy.tech/badge/ishi)](https://pepy.tech/project/ishi)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/ishi?style=social)|
|[python-npylm](https://github.com/musyoku/python-npylm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/python-npylm?style=social)|
|[python-npycrf](https://github.com/musyoku/python-npycrf)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/python-npycrf?style=social)|
|[unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/unsupervised-pos-tagging?style=social)|
|[negima](https://github.com/cocodrips/negima)|[![Downloads](https://pepy.tech/badge/negima/week)](https://pepy.tech/project/negima)|[![Downloads](https://pepy.tech/badge/negima)](https://pepy.tech/project/negima)|![GitHub Repo stars](https://img.shields.io/github/stars/cocodrips/negima?style=social)|
|[YouyakuMan](https://github.com/neilctwu/YouyakuMan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neilctwu/YouyakuMan?style=social)|
|[japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python)|[![Downloads](https://pepy.tech/badge/japanese-numbers-python/week)](https://pepy.tech/project/japanese-numbers-python)|[![Downloads](https://pepy.tech/badge/japanese-numbers-python)](https://pepy.tech/project/japanese-numbers-python)|![GitHub Repo stars](https://img.shields.io/github/stars/takumakanari/japanese-numbers-python?style=social)|
|[kantan](https://github.com/itayperl/kantan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/itayperl/kantan?style=social)|
|[make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/knok/make-meidai-dialogue?style=social)|
|[japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ryuryukke/japanese_summarizer?style=social)|
|[chirptext](https://github.com/letuananh/chirptext)|[![Downloads](https://pepy.tech/badge/chirptext/week)](https://pepy.tech/project/chirptext)|[![Downloads](https://pepy.tech/badge/chirptext)](https://pepy.tech/project/chirptext)|![GitHub Repo stars](https://img.shields.io/github/stars/letuananh/chirptext?style=social)|
|[yubin](https://github.com/alvations/yubin)|[![Downloads](https://pepy.tech/badge/yubin/week)](https://pepy.tech/project/yubin)|[![Downloads](https://pepy.tech/badge/yubin)](https://pepy.tech/project/yubin)|![GitHub Repo stars](https://img.shields.io/github/stars/alvations/yubin?style=social)|
|[jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner)|[![Downloads](https://pepy.tech/badge/jawiki-cleaner/week)](https://pepy.tech/project/jawiki-cleaner)|[![Downloads](https://pepy.tech/badge/jawiki-cleaner)](https://pepy.tech/project/jawiki-cleaner)|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/jawiki-cleaner?style=social)|
|[japanese2phoneme](https://github.com/iory/japanese2phoneme)|[![Downloads](https://pepy.tech/badge/japanese2phoneme/week)](https://pepy.tech/project/japanese2phoneme)|[![Downloads](https://pepy.tech/badge/japanese2phoneme)](https://pepy.tech/project/japanese2phoneme)|![GitHub Repo stars](https://img.shields.io/github/stars/iory/japanese2phoneme?style=social)
|[anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/arusl/anlp_nlp2021_d3-1?style=social)|
|[aozora_classification](https://github.com/shibuiwilliam/aozora_classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shibuiwilliam/aozora_classification?style=social)|
|[aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/borh/aozora-corpus-generator?style=social)|
|[JLM](https://github.com/jiali-ms/JLM)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jiali-ms/JLM?style=social)|
|[NTM](https://github.com/m3yrin/NTM)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/m3yrin/NTM?style=social)|
|[EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Machine-Learning-Tokyo/EN-JP-ML-Lexicon?style=social)|
|[text-generation](https://github.com/discus0434/text-generation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/discus0434/text-generation?style=social)|
|[chainer_nic](https://github.com/yuyay/chainer_nic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuyay/chainer_nic?style=social)|
|[unihan-lm](https://github.com/JetRunner/unihan-lm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/JetRunner/unihan-lm?style=social)|
|[mbart-finetuning](https://github.com/ken11/mbart-finetuning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/mbart-finetuning?style=social)|
|[xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarulab-speech/xvector_jtubespeech?style=social)|
|[TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shogo82148/TinySegmenterMaker?style=social)|
|[Grongish](https://github.com/shogo82148/Grongish)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shogo82148/Grongish?style=social)|
|[WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aocattleya/WordCloud-Japanese?style=social)|
|[snark](https://github.com/hiraokusky/snark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hiraokusky/snark?style=social)|
|[toEmoji](https://github.com/mkan0141/toEmoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mkan0141/toEmoji?style=social)|
|[termextract](https://github.com/kanjirz50/termextract)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kanjirz50/termextract?style=social)|
|[JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/TUT-SLP-lab/JDT-with-KenLM-scoring?style=social)|
|[mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KentoW/mixture-of-unigram-model?style=social)|
|[hidden-markov-model](https://github.com/KentoW/hidden-markov-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KentoW/hidden-markov-model?style=social)|
|[Ngram-language-model](https://github.com/KentoW/Ngram-language-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KentoW/Ngram-language-model?style=social)|
|[ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/JeanMaximilienCadic/ASRDeepSpeech?style=social)|
|[neural_ime](https://github.com/yohokuno/neural_ime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yohokuno/neural_ime?style=social)|
|[neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Kyubyong/neural_japanese_transliterator?style=social)|
|[tinysegmenter](https://github.com/SamuraiT/tinysegmenter)|[![Downloads](https://pepy.tech/badge/tinysegmenter/week)](https://pepy.tech/project/tinysegmenter3)|[![Downloads](https://pepy.tech/badge/tinysegmenter3)](https://pepy.tech/project/tinysegmenter3)|![GitHub Repo stars](https://img.shields.io/github/stars/SamuraiT/tinysegmenter3?style=social)|
|[AugLy-jp](https://github.com/chck/AugLy-jp)|[![Downloads](https://pepy.tech/badge/AugLy-jp/week)](https://pepy.tech/project/AugLy-jp)|[![Downloads](https://pepy.tech/badge/AugLy-jp)](https://pepy.tech/project/AugLy-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/chck/AugLy-jp?style=social)|
|[furigana4epub](https://github.com/Mumumu4/furigana4epub)|[![Downloads](https://pepy.tech/badge/furigana4epub/week)](https://pepy.tech/project/furigana4epub)|[![Downloads](https://pepy.tech/badge/furigana4epub)](https://pepy.tech/project/furigana4epub)|![GitHub Repo stars](https://img.shields.io/github/stars/Mumumu4/furigana4epub?style=social)|
|[PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou)|[![Downloads](https://pepy.tech/badge/PyKatsuyou/week)](https://pepy.tech/project/PyKatsuyou)|[![Downloads](https://pepy.tech/badge/PyKatsuyou)](https://pepy.tech/project/PyKatsuyou)|![GitHub Repo stars](https://img.shields.io/github/stars/SmashinFries/PyKatsuyou?style=social)|
|[jageocoder](https://github.com/t-sagara/jageocoder)|[![Downloads](https://pepy.tech/badge/jageocoder/week)](https://pepy.tech/project/jageocoder)|[![Downloads](https://pepy.tech/badge/jageocoder)](https://pepy.tech/project/jageocoder)|![GitHub Repo stars](https://img.shields.io/github/stars/t-sagara/jageocoder?style=social)|
|[pygeonlp](https://github.com/geonlp-platform/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp/week)](https://pepy.tech/project/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp)](https://pepy.tech/project/pygeonlp)|![GitHub Repo stars](https://img.shields.io/github/stars/geonlp-platform/pygeonlp?style=social)|
|[nksnd](https://github.com/yoriyuki/nksnd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yoriyuki/nksnd?style=social)|
|[JaMIE](https://github.com/racerandom/JaMIE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/racerandom/JaMIE?style=social)|
|[fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/fasttext-vs-word2vec-on-twitter-data?style=social)|
|[minimal-search-engine](https://github.com/GINK03/minimal-search-engine)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/minimal-search-engine?style=social)|
|[5ch-analysis](https://github.com/GINK03/5ch-analysis)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/5ch-analysis?style=social)|
|[tweet_extructor](https://github.com/tatHi/tweet_extructor)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tatHi/tweet_extructor?style=social)|
|[japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/japanese-word-aggregation?style=social)|
|[jinf](https://github.com/hkiyomaru/jinf)|[![Downloads](https://pepy.tech/badge/jinf/week)](https://pepy.tech/project/jinf)|[![Downloads](https://pepy.tech/badge/jinf)](https://pepy.tech/project/jinf)|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/jinf?style=social)|
|[kwja](https://github.com/ku-nlp/kwja)|[![Downloads](https://pepy.tech/badge/kwja/week)](https://pepy.tech/project/kwja)|[![Downloads](https://pepy.tech/badge/kwja)](https://pepy.tech/project/kwja)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/kwja?style=social)|
|[mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Ryutaro-A/mlm-scoring-transformers?style=social)|
|[ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Japanese-Image-Captioning/ClipCap-for-Japanese?style=social)|
|[SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Japanese-Image-Captioning/SAT-for-Japanese?style=social)|
|[cihai](https://github.com/cihai/cihai)|[![Downloads](https://pepy.tech/badge/cihai/week)](https://pepy.tech/project/cihai)|[![Downloads](https://pepy.tech/badge/cihai)](https://pepy.tech/project/cihai)|![GitHub Repo stars](https://img.shields.io/github/stars/cihai/cihai?style=social)|
|[marine](https://github.com/6gsn/marine)|[![Downloads](https://pepy.tech/badge/marine/week)](https://pepy.tech/project/marine)|[![Downloads](https://pepy.tech/badge/marine)](https://pepy.tech/project/marine)|![GitHub Repo stars](https://img.shields.io/github/stars/6gsn/marine?style=social)|
|[whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarulab-speech/whisper-asr-finetune?style=social)|
|[japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CjangCjengh/japanese_chatbot?style=social)|
|[radicalchar](https://github.com/yamamaya/radicalchar)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yamamaya/radicalchar?style=social)|
|[akaza](https://github.com/tokuhirom/akaza)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tokuhirom/akaza?style=social)|
|[posuto](https://github.com/polm/posuto)|[![Downloads](https://pepy.tech/badge/posuto/week)](https://pepy.tech/project/posuto)|[![Downloads](https://pepy.tech/badge/posuto)](https://pepy.tech/project/posuto)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/posuto?style=social)|
|[tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CjangCjengh/tacotron2-japanese?style=social)|
|[ibus-hiragana](https://github.com/esrille/ibus-hiragana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/ibus-hiragana?style=social)|
|[furiganapad](https://github.com/esrille/furiganapad)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/furiganapad?style=social)|
|[chikkarpy](https://github.com/WorksApplications/chikkarpy)|[![Downloads](https://pepy.tech/badge/chikkarpy/week)](https://pepy.tech/project/chikkarpy)|[![Downloads](https://pepy.tech/badge/chikkarpy)](https://pepy.tech/project/chikkarpy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/chikkarpy?style=social)|
|[ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/p-geon/ja-tokenizer-docker-py?style=social)|
|[JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/oshizo/JapaneseEmbeddingEval?style=social)|
|[gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/karakuri-ai/gptuber-by-langchain?style=social)|
|[shuwa](https://github.com/google/shuwa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/shuwa?style=social)|
|[japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CyberAgentAILab/japanese-nli-model?style=social)|
|[tra-fugu](https://github.com/tos-kamiya/tra-fugu)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tos-kamiya/tra-fugu?style=social)|
|[fugumt](https://github.com/s-taka/fugumt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/s-taka/fugumt?style=social)|
|[JaSPICE](https://github.com/keio-smilab23/JaSPICE)|[![Downloads](https://pepy.tech/badge/JaSPICE/week)](https://pepy.tech/project/JaSPICE)|[![Downloads](https://pepy.tech/badge/JaSPICE)](https://pepy.tech/project/JaSPICE)|![GitHub Repo stars](https://img.shields.io/github/stars/keio-smilab23/JaSPICE?style=social)|
|[Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization?style=social)|
|[pyopenjtalk](https://github.com/r9y9/pyopenjtalk)|[![Downloads](https://pepy.tech/badge/pyopenjtalk/week)](https://pepy.tech/project/pyopenjtalk)|[![Downloads](https://pepy.tech/badge/pyopenjtalk)](https://pepy.tech/project/pyopenjtalk)|![GitHub Repo stars](https://img.shields.io/github/stars/r9y9/pyopenjtalk?style=social)|
|[yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook)|[![Downloads](https://pepy.tech/badge/yomigana-ebook/week)](https://pepy.tech/project/yomigana-ebook)|[![Downloads](https://pepy.tech/badge/yomigana-ebook)](https://pepy.tech/project/yomigana-ebook)|![GitHub Repo stars](https://img.shields.io/github/stars/rabbit19981023/yomigana-ebook?style=social)|
|[N46Whisper](https://github.com/Ayanaminn/N46Whisper)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Ayanaminn/N46Whisper?style=social)|


## C++

### Morphology analysis

 * [mecab](https://github.com/taku910/mecab) - Yet another Japanese morphological analyzer
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++ (a Morphological Analyzer Toolkit)
 * [kytea](https://github.com/neubig/kytea) - The Kyoto Text Analysis Toolkit for word segmentation and pronunciation estimation, etc.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab](https://github.com/taku910/mecab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/mecab?style=social)|
|[jumanpp](https://github.com/ku-nlp/jumanpp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/jumanpp?style=social)|
|[kytea](https://github.com/neubig/kytea)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neubig/kytea?style=social)|

### Parsing

 * [cabocha](https://github.com/taku910/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [knp](https://github.com/ku-nlp/knp) - A Japanese Parser


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[cabocha](https://github.com/taku910/cabocha)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/cabocha?style=social)|
|[knp](https://github.com/ku-nlp/knp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/knp?style=social)|

### Others

 * [jsc](https://github.com/yohokuno/jsc) - Joint source channel model for Japanese Kana Kanji conversion, Chinese pinyin input and CJE mixed input.
 * [aquaskk](https://github.com/codefirst/aquaskk) - An input method without morphological analysis.
 * [mozc](https://github.com/google/mozc) - Mozc - a Japanese Input Method Editor designed for multi-platform
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch: An (Exact|Prefix|Approximate) String Matching Library
 * [resembla](https://github.com/tuem/resembla) - Resembla: Word-based Japanese similar sentence search library
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ SKK-like Japanese Input Method Editor for Windows


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jsc](https://github.com/yohokuno/jsc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yohokuno/jsc?style=social)|
|[aquaskk](https://github.com/codefirst/aquaskk)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/codefirst/aquaskk?style=social)|
|[mozc](https://github.com/google/mozc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/mozc?style=social)|
|[trimatch](https://github.com/tuem/trimatch)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/trimatch?style=social)|
|[resembla](https://github.com/tuem/resembla)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/resembla?style=social)|
|[corvusskk](https://github.com/nathancorvussolis/corvusskk)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nathancorvussolis/corvusskk?style=social)|


## Rust crate

### Morphology analysis

 * [lindera](https://github.com/lindera-morphology/lindera) - A morphological analysis library.
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto: Very Accelerated POintwise pREdicTion based TOkenizer
 * [goya](https://github.com/Leko/goya) - Japanese Morphological Analysis written in Rust
 * [vibrato](https://github.com/daac-tools/vibrato) - vibrato: Viterbi-based accelerated tokenizer
 * [yoin](https://github.com/agatan/yoin) - A Japanese Morphological Analyzer written in pure Rust
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - Safe Rust bindings for mecab a part-of-speech and morphological analyzer library
 * [awabi](https://github.com/nakagami/awabi) - A morphological analyzer using mecab dictionary


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[lindera](https://github.com/lindera-morphology/lindera)|-|![Crates.io](https://img.shields.io/crates/d/lindera)|![GitHub Repo stars](https://img.shields.io/github/stars/lindera-morphology/lindera?style=social)|
|[vaporetto](https://github.com/daac-tools/vaporetto)|-|![Crates.io](https://img.shields.io/crates/d/vaporetto)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/vaporetto?style=social)|
|[goya](https://github.com/Leko/goya)|-|![Crates.io](https://img.shields.io/crates/d/goya)|![GitHub Repo stars](https://img.shields.io/github/stars/Leko/goya?style=social)|
|[vibrato](https://github.com/daac-tools/vibrato)|-|![Crates.io](https://img.shields.io/crates/d/vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/vibrato?style=social)|
|[yoin](https://github.com/agatan/yoin)|-|![Crates.io](https://img.shields.io/crates/d/yoin)|![GitHub Repo stars](https://img.shields.io/github/stars/agatan/yoin?style=social)|
|[mecab-rs](https://github.com/tsurai/mecab-rs)|-|![Crates.io](https://img.shields.io/crates/d/mecab)|![GitHub Repo stars](https://img.shields.io/github/stars/tsurai/mecab-rs?style=social)|
|[awabi](https://github.com/nakagami/awabi)|-|![Crates.io](https://img.shields.io/crates/d/awabi)|![GitHub Repo stars](https://img.shields.io/github/stars/nakagami/awabi?style=social)|


### Converter

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - Utility library for checking and converting between Japanese characters - Hiragana, Katakana - and Romaji
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - A Rust library to convert Japanese Half-width-kana[半角ｶﾅ] and Wide-alphanumeric[全角英数] into normal ones
 * [kana](https://github.com/gbrlsnchs/kana) - [Mirror] CLI program for transliterating romaji text to either hiragana or katakana


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[wana_kana_rust](https://github.com/PSeitz/wana_kana_rust)|-|![Crates.io](https://img.shields.io/crates/d/wana_kana)|![GitHub Repo stars](https://img.shields.io/github/stars/PSeitz/wana_kana_rust?style=social)|
|[unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs)|-|![Crates.io](https://img.shields.io/crates/d/unicode-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/gemmarx/unicode-jp-rs?style=social)|
|[kana](https://github.com/gbrlsnchs/kana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gbrlsnchs/kana?style=social)|


### Search engine library

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy.
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - A Tantivy tokenizer using Vibrato.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy)|-|![Crates.io](https://img.shields.io/crates/d/lindera-tantivy)|![GitHub Repo stars](https://img.shields.io/github/stars/lindera-morphology/lindera-tantivy?style=social)|
|[tantivy-vibrato](https://github.com/akr4/tantivy-vibrato)|-|![Crates.io](https://img.shields.io/crates/d/tantivy-vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/akr4/tantivy-vibrato?style=social)|


### Others

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[daachorse](https://github.com/daac-tools/daachorse)|-|![Crates.io](https://img.shields.io/crates/d/daachorse)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/daachorse?style=social)|
|[find-simdoc](https://github.com/legalforce-research/find-simdoc)|-|![Crates.io](https://img.shields.io/crates/d/find-simdoc)|![GitHub Repo stars](https://img.shields.io/github/stars/legalforce-research/find-simdoc?style=social)|
|[crawdad](https://github.com/daac-tools/crawdad)|-|![Crates.io](https://img.shields.io/crates/d/crawdad)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/crawdad?style=social)|
|[tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/legalforce-research/tokenizer-speed-bench?style=social)|
|[stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/legalforce-research/stringmatch-bench?style=social)|
|[vime](https://github.com/algon-320/vime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/algon-320/vime?style=social)
|[voicevox_core](https://github.com/VOICEVOX/voicevox_core)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/VOICEVOX/voicevox_core?style=social)|
|[akaza](https://github.com/akaza-im/akaza)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/akaza-im/akaza?style=social)
|[Jotoba](https://github.com/WeDontPanic/Jotoba)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WeDontPanic/Jotoba?style=social)|
|[dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shinespark/dvorakjp-romantable?style=social)|
|[niinii](https://github.com/Netdex/niinii)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Netdex/niinii?style=social)|


## JavaScript

### Morphology analysis

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - JavaScript implementation of Japanese morphological analyzer
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) -  Rakuten MA - morphological analyzer (word segmentor + PoS Tagger) for Chinese and Japanese written purely in JavaScript.
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - Yet another mecab wrapper for nodejs
 * [juman-bin](https://github.com/thammin/juman-bin) - a User-Extensible Morphological Analyzer for Japanese. 日本語形態素解析システム
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - Asynchronous japanese morphological analyser using MeCab.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji.js](https://github.com/takuyaa/kuromoji.js)|![npm](https://img.shields.io/npm/dw/kuromoji)|![npm](https://img.shields.io/npm/dt/kuromoji)|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/kuromoji.js?style=social)|
|[rakutenma](https://github.com/rakuten-nlp/rakutenma)|![npm](https://img.shields.io/npm/dw/rakutenma)|![npm](https://img.shields.io/npm/dt/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/rakuten-nlp/rakutenma?style=social)|
|[node-mecab-ya](https://github.com/golbin/mecab-ya)|![npm](https://img.shields.io/npm/dw/mecab-ya)|![npm](https://img.shields.io/npm/dt/mecab-ya)|![GitHub Repo stars](https://img.shields.io/github/stars/golbin/node-mecab-ya?style=social)|
|[juman-bin](https://github.com/thammin/juman-bin)|![npm](https://img.shields.io/npm/dw/juman-bin)|![npm](https://img.shields.io/npm/dt/juman-bin)|![GitHub Repo stars](https://img.shields.io/github/stars/thammin/juman-bin?style=social)|
|[node-mecab-async](https://github.com/hecomi/node-mecab-async)|![npm](https://img.shields.io/npm/dw/mecab-async)|![npm](https://img.shields.io/npm/dt/mecab-async)|![GitHub Repo stars](https://img.shields.io/github/stars/hecomi/node-mecab-async?style=social)|


### Converter

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - Japanese language library for converting Japanese sentence to Hiragana, Katakana or Romaji with furigana and okurigana modes supported.
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - Kuromoji morphological analyzer for kuroshiro.
 * [hepburn](https://github.com/lovell/hepburn) - Node.js module for converting Japanese Hiragana and Katakana script to, and from, Romaji using Hepburn romanisation
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - Converts Japanese Numerals into number
 * [jslingua](https://github.com/kariminf/jslingua) - Javascript libraries for text processing: Arabic, Japanese, and more.
 * [WanaKana](https://github.com/WaniKani/WanaKana) - A Javascript library that can detect and transliterate between Hiragana, Katakana, and Romaji.
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - Normalize and fix common issues with Romaji-based Japanese names.
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - Utility collections for making Japanese text old-fashioned
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - Open source address normalization library.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuroshiro](https://github.com/hexenq/kuroshiro)|![npm](https://img.shields.io/npm/dw/kuroshiro)|![npm](https://img.shields.io/npm/dt/kuroshiro)|![GitHub Repo stars](https://img.shields.io/github/stars/hexenq/kuroshiro?style=social)|
|[kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji)|![npm](https://img.shields.io/npm/dw/kuroshiro-analyzer-kuromoji)|![npm](https://img.shields.io/npm/dt/kuroshiro-analyzer-kuromoji)|![GitHub Repo stars](https://img.shields.io/github/stars/hexenq/kuroshiro-analyzer-kuromoji?style=social)|
|[hepburn](https://github.com/lovell/hepburn)|![npm](https://img.shields.io/npm/dw/hepburn)|![npm](https://img.shields.io/npm/dt/hepburn)|![GitHub Repo stars](https://img.shields.io/github/stars/lovell/hepburn?style=social)|
|[japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number)|![npm](https://img.shields.io/npm/dw/japanese-numerals-to-number)|![npm](https://img.shields.io/npm/dt/japanese-numerals-to-number)|![GitHub Repo stars](https://img.shields.io/github/stars/twada/japanese-numerals-to-number?style=social)|
|[jslingua](https://github.com/kariminf/jslingua)|![npm](https://img.shields.io/npm/dw/jslingua)|![npm](https://img.shields.io/npm/dt/jslingua)|![GitHub Repo stars](https://img.shields.io/github/stars/kariminf/jslingua?style=social)|
|[WanaKana](https://github.com/WaniKani/WanaKana)|![npm](https://img.shields.io/npm/dw/wanakana)|![npm](https://img.shields.io/npm/dt/wanakana)|![GitHub Repo stars](https://img.shields.io/github/stars/WaniKani/WanaKana?style=social)|
|[node-romaji-name](https://github.com/jeresig/node-romaji-name)|![npm](https://img.shields.io/npm/dw/romaji-name)|![npm](https://img.shields.io/npm/dt/romaji-name)|![GitHub Repo stars](https://img.shields.io/github/stars/jeresig/node-romaji-name?style=social)|
|[kyujitai.js](https://github.com/hakatashi/kyujitai.js)|![npm](https://img.shields.io/npm/dw/kyujitai)|![npm](https://img.shields.io/npm/dt/kyujitai)|![GitHub Repo stars](https://img.shields.io/github/stars/hakatashi/kyujitai.js?style=social)|
|[normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/geolonia/normalize-japanese-addresses?style=social)|


### Others

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bangumi-data](https://github.com/bangumi-data/bangumi-data)|![npm](https://img.shields.io/npm/dw/bangumi-data)|![npm](https://img.shields.io/npm/dt/bangumi-data)|![GitHub Repo stars](https://img.shields.io/github/stars/bangumi-data/bangumi-data?style=social)|
|[yomichan](https://github.com/FooSoft/yomichan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/FooSoft/yomichan?style=social)|
|[proofreading-tool](https://github.com/gecko655/proofreading-tool)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gecko655/proofreading-tool?style=social)|
|[kanjigrid](https://github.com/minosvasilias/kanjigrid)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/minosvasilias/kanjigrid?style=social)|
|[japanese-toolkit](https://github.com/echamudi/japanese-toolkit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/echamudi/japanese-toolkit?style=social)|
|[analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu)|![npm](https://img.shields.io/npm/dw/analyze-desumasu-dearu)|![npm](https://img.shields.io/npm/dt/analyze-desumasu-dearu)|![GitHub Repo stars](https://img.shields.io/github/stars/textlint-ja/analyze-desumasu-dearu?style=social)|
|[hatsuon](https://github.com/DJTB/hatsuon)|![npm](https://img.shields.io/npm/dw/hatsuon)|![npm](https://img.shields.io/npm/dt/hatsuon)|![GitHub Repo stars](https://img.shields.io/github/stars/DJTB/hatsuon?style=social)|
|[sentiment_ja_js](https://github.com/otodn/sentiment_ja_js)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/otodn/sentiment_ja_js?style=social)|
|[mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed)|![npm](https://img.shields.io/npm/dw/mecab-ipadic-seed)|![npm](https://img.shields.io/npm/dt/mecab-ipadic-seed)|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/mecab-ipadic-seed?style=social)|
|[Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day)|![npm](https://img.shields.io/npm/dw/japanese-wotd)|![npm](https://img.shields.io/npm/dt/japanese-wotd)|![GitHub Repo stars](https://img.shields.io/github/stars/LuanRT/Japanese-Word-Of-The-Day?style=social)|
|[oskim](https://github.com/esrille/oskim)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/oskim?style=social)|
|[tweetMapping](https://github.com/wtnv-lab/tweetMapping)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wtnv-lab/tweetMapping?style=social)|


## Go

### Morphology analysis

 * [kagome](https://github.com/ikawaha/kagome) - Self-contained Japanese Morphological Analyzer written in pure Go


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kagome](https://github.com/ikawaha/kagome)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikawaha/kagome?style=social)|


### Others

 * [ojosama](https://github.com/jiro4989/ojosama) - Converts text into the tone of Lady Salome from the Hundred Celestial Plains.
 * [nihongo](https://github.com/gojp/nihongo) - Japanese Dictionary
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - External dictionary importer for Yomichan.
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - THE IDOLM@STER words dictionary for Japanese IME (by imas-db.jp)
 * [go-moji](https://github.com/ktnyt/go-moji) - A Go library for Zenkaku/Hankaku conversion


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ojosama](https://github.com/jiro4989/ojosama)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jiro4989/ojosama?style=social)|
|[nihongo](https://github.com/gojp/nihongo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gojp/nihongo?style=social)|
|[yomichan-import](https://github.com/FooSoft/yomichan-import)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/FooSoft/yomichan-import?style=social)|
|[imas-ime-dic](https://github.com/maruamyu/imas-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/maruamyu/imas-ime-dic?style=social)|
|[go-moji](https://github.com/ktnyt/go-moji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ktnyt/go-moji?style=social)|


## Java

### Morphology analysis

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji is a self-contained and very easy to use Japanese morphological analyzer designed for search
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - A lexicon for Sudachi


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji](https://github.com/atilika/kuromoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/atilika/kuromoji?style=social)|
|[Sudachi](https://github.com/WorksApplications/Sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/Sudachi?style=social)|
|[SudachiDict](https://github.com/WorksApplications/SudachiDict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiDict?style=social)|


### Others

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - Java library for identifying Japanese characters from images
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - Java library and command-line tool to transliterate Japanese kanji to romaji (Latin alphabet)
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Kanji transliteration to hiragana/katakana/romaji, in Java
 * [Kamite](https://github.com/fauu/Kamite) - A desktop language immersion companion for learners of Japanese
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - Async Japanese Tokenizer Native Plugin for React Native for iOS and Android
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - The Japanese analyzer utilizes the Kuromoji Japanese tokenizer for ElasticSearch.
 * [moji4j](https://github.com/andree-surya/moji4j) - A Java library to converts between Japanese Hiragana, Katakana, and Romaji scripts.
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - Japanese text normalizer for mecab-neologd


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sakarika/kanjitomo-ocr?style=social)|
|[jakaroma](https://github.com/nicolas-raoul/jakaroma)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nicolas-raoul/jakaroma?style=social)|
|[kakasi-java](https://github.com/nicolas-raoul/kakasi-java)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nicolas-raoul/kakasi-java?style=social)|
|[Kamite](https://github.com/fauu/Kamite)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/fauu/Kamite?style=social)|
|[react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/craftzdog/react-native-japanese-tokenizer?style=social)|
|[elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/suguru/elasticsearch-analysis-japanese?style=social)|
|[moji4j](https://github.com/andree-surya/moji4j)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/andree-surya/moji4j?style=social)|
|[neologdn-java](https://github.com/ikegami-yukino/neologdn-java)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/neologdn-java?style=social)|


## Pretrained model

### Word2Vec

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - Word2vec (word to vectors) approach for Japanese language using Gensim and Mecab.
 * [chiVe](https://github.com/WorksApplications/chiVe) - Japanese word embedding with Sudachi and NWJC
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - Elmo (in Japanese)
 * [embedrank](https://github.com/yagays/embedrank) - Python Implementation of EmbedRank
 * [aovec](https://github.com/eggplants/aovec) - Easy aozorabunko Word2Vec Builder - Word2Vec Builder and pre-built model for all books in the Aozora Bunko library.
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - This is a repository for the AI LAB article "係り受けに基づく日本語単語埋込 (Dependency-based Japanese Word Embeddings)" ( Article URL https://ai-lab.lapras.com/nlp/japanese-word-embedding/)
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - Yet Another Japanese-Wikipedia Entity Vectors
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - A script for learning word embedding models such as word2vec, fastText, and GloVe based on the results of morphological analysis using both the IPA dictionary and the latest Neologd dictionary, using MeCab on the latest Japanese Wikipedia dump data.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/philipperemy/japanese-words-to-vectors?style=social)|
|[chiVe](https://github.com/WorksApplications/chiVe)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/chiVe?style=social)|
|[elmo-japanese](https://github.com/cl-tohoku/elmo-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/elmo-japanese?style=social)|
|[embedrank](https://github.com/yagays/embedrank)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/embedrank?style=social)|
|[aovec](https://github.com/eggplants/aovec)|[![Downloads](https://pepy.tech/badge/aovec/week)](https://pepy.tech/project/aovec)|[![Downloads](https://pepy.tech/badge/aovec)](https://pepy.tech/project/aovec)|![GitHub Repo stars](https://img.shields.io/github/stars/eggplants/aovec?style=social)|
|[dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/lapras-inc/dependency-based-japanese-word-embeddings?style=social)|
|[jawikivec](https://github.com/wikiwikification/jawikivec)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wikiwikification/jawikivec?style=social)|
|[jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kamigaito/jawiki_word_vector_updater?style=social)|


### Transformer based models

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
 * [japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) - This repository provides a Japanese GPT-NeoX model of 3.6 billion parameters. The model was trained using code based on EleutherAI/gpt-neox.
 * [japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft) - This repository provides a Japanese GPT-NeoX model of 3.6 billion parameters. The model is based on rinna/japanese-gpt-neox-3.6b and has been finetuned to serve as a instruction-following conversational agent.
 * [japanese-hubert-base](https://huggingface.co/rinna/japanese-hubert-base) - This is a Japanese HuBERT (Hidden Unit Bidirectional Encoder Representations from Transformers) model trained by rinna Co., Ltd.
 * [open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - OpenCALM is a suite of decoder-only language models pre-trained on Japanese datasets, developed by CyberAgent, Inc.
 * [luke-japanese-base-finetuned-ner](https://huggingface.co/Mizuiro-sakura/luke-japanese-base-finetuned-ner) - This model fine-tunes luke-japanese-base to be used for named entity recognition (NER).
 * [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) - Pretrained models, codes and guidances to pretrain official ALBERT(https://github.com/google-research/albert) on Japanese Wikipedia Resources
 * [japanese-mpt-7b](https://huggingface.co/lightblue/japanese-mpt-7b) - light blue/japanese-mpt-7b


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bert-japanese](https://github.com/cl-tohoku/bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/bert-japanese?style=social)|
|[japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-pretrained-models?style=social)|
|[bert-japanese](https://github.com/yoheikikuta/bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yoheikikuta/bert-japanese?style=social)|
|[SudachiTra](https://github.com/WorksApplications/SudachiTra)|[![Downloads](https://pepy.tech/badge/SudachiTra/week)](https://pepy.tech/project/SudachiTra)|[![Downloads](https://pepy.tech/badge/SudachiTra)](https://pepy.tech/project/SudachiTra)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiTra?style=social)|
|[japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nttcslab/japanese-dialog-transformers?style=social)|
|[shiba](https://github.com/octanove/shiba)|[![Downloads](https://pepy.tech/badge/shiba-model/week)](https://pepy.tech/project/shiba-model)|[![Downloads](https://pepy.tech/badge/shiba-model)](https://pepy.tech/project/shiba-model)|![GitHub Repo stars](https://img.shields.io/github/stars/octanove/shiba?style=social)|
|[Dialog](https://github.com/reppy4620/Dialog)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/reppy4620/Dialog?style=social)|
|[language-pretraining](https://github.com/retarfi/language-pretraining)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/retarfi/language-pretraining?style=social)|
|[medbertjp](https://github.com/ou-medinfo/medbertjp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ou-medinfo/medbertjp?style=social)|
|[ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/ILYS-aoba-chatbot?style=social)|
|[t5-japanese](https://github.com/megagonlabs/t5-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/t5-japanese?style=social)|
|[pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/pytorch_bert_japanese?style=social)|
|[Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/Laboro-BERT-Japanese?style=social)|
|[RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/RoBERTa-japanese?style=social)|
|[aMLP-japanese](https://github.com/tanreinama/aMLP-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/aMLP-japanese?style=social)|
|[bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/akirakubo/bert-japanese-aozora?style=social)|
|[sbert-ja](https://github.com/colorfulscoop/sbert-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/colorfulscoop/sbert-ja?style=social)|
|[BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/PatrickJohnRamos/BERT-Japan-vaccination?style=social)|
|[gpt2-japanese](https://github.com/tanreinama/gpt2-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/gpt2-japanese?style=social)|
|[text2text-japanese](https://github.com/tanreinama/text2text-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/text2text-japanese?style=social)|
|[gpt-ja](https://github.com/colorfulscoop/gpt-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/colorfulscoop/gpt-ja?style=social)|
|[friendly_JA-Model](https://github.com/astremo/friendly_JA-Model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/astremo/friendly_JA-Model?style=social)|
|[albert-japanese](https://github.com/alinear-corp/albert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/alinear-corp/albert-japanese?style=social)|
|[ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Kosuke-Szk/ja_text_bert?style=social)|
|[DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/BandaiNamcoResearchInc/DistilBERT-base-jp?style=social)|
|[bert](https://github.com/informatix-inc/bert)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/informatix-inc/bert?style=social)|
|[Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/Laboro-DistilBERT-Japanese?style=social)|
|[luke](https://github.com/studio-ousia/luke)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/studio-ousia/luke?style=social)|
|[GPTSAN](https://github.com/tanreinama/GPTSAN)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/GPTSAN?style=social)|
|[japanese-clip](https://github.com/rinnakk/japanese-clip)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-clip?style=social)|
|[AcademicBART](https://github.com/EhimeNLP/AcademicBART)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/EhimeNLP/AcademicBART?style=social)|
|[AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/EhimeNLP/AcademicRoBERTa?style=social)|
|[LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/line/LINE-DistilBERT-Japanese?style=social)|
|[Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kunishou/Japanese-Alpaca-LoRA?style=social)|
|[japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b)|-|-|-|
|[japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft)|-|-|-|
|[japanese-hubert-base](https://huggingface.co/rinna/japanese-hubert-base)|-|-|-|
|[open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b)|-|-|-|
|[luke-japanese-base-finetuned-ner](https://huggingface.co/Mizuiro-sakura/luke-japanese-base-finetuned-ner)|-|-|-|
|[albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nknytk/albert-japanese-tinysegmenter?style=social)|
|[japanese-mpt-7b](https://huggingface.co/lightblue/japanese-mpt-7b)|-|-|-|


## ChatGPT

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Yuchi-Games/VRChatGPT?style=social)|
|[AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/M-gen/AITuberDegikkoMirii?style=social)|
|[wanna](https://github.com/hirokidaichi/wanna)|[![Downloads](https://pepy.tech/badge/wanna/week)](https://pepy.tech/project/wanna)|[![Downloads](https://pepy.tech/badge/wanna)](https://pepy.tech/project/wanna)|![GitHub Repo stars](https://img.shields.io/github/stars/hirokidaichi/wanna?style=social)|
|[ChatdollKit](https://github.com/uezo/ChatdollKit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/uezo/ChatdollKit?style=social)|
|[ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gyokuro33/ChuanhuChatGPTJapanese?style=social)|
|[AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/manju-summoner/AISisterAIChan?style=social)|
|[vrchatbot](https://github.com/Geson-anko/vrchatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Geson-anko/vrchatbot?style=social)|
|[gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/karakuri-ai/gptuber-by-langchain?style=social)|
|[openai-chatfriend](https://github.com/supershaneski/openai-chatfriend)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/supershaneski/openai-chatfriend?style=social)|
|[chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt?style=social)|
|[azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nohanaga/azure-search-openai-demo?style=social)|
|[chatvrm](https://github.com/pixiv/chatvrm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/pixiv/chatvrm?style=social)|
|[sftly-replace](https://github.com/kmizu/sftly-replace)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kmizu/sftly-replace?style=social)|
|[summarize_arxv](https://github.com/rkmt/summarize_arxv)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rkmt/summarize_arxv?style=social)|
|[aiavatarkit](https://github.com/uezo/aiavatarkit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/uezo/aiavatarkit?style=social)|
|[pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/City-of-Kobe/pva-aoai-integration-solution?style=social)|
|[jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/azure-samples/jp-azureopenai-samples?style=social)|


## Dictionary

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neologd/mecab-ipadic-neologd?style=social)|
|[tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/tdmelodic?style=social)|
|[jamdict](https://github.com/neocl/jamdict)|[![Downloads](https://pepy.tech/badge/jamdict/week)](https://pepy.tech/project/jamdict)|[![Downloads](https://pepy.tech/badge/jamdict)](https://pepy.tech/project/jamdict)|![GitHub Repo stars](https://img.shields.io/github/stars/neocl/jamdict?style=social)|
|[unidic-py](https://github.com/polm/unidic-py)|[![Downloads](https://pepy.tech/badge/unidic/week)](https://pepy.tech/project/unidic)|[![Downloads](https://pepy.tech/badge/unidic)](https://pepy.tech/project/unidic)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/unidic-py?style=social)|
|[Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/Japanese-Company-Lexicon?style=social)|
|[manbyo-sudachi](https://github.com/yagays/manbyo-sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/manbyo-sudachi?style=social)|
|[jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tokuhirom/jawiki-kana-kanji-dict?style=social)|
|[JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/JIWC-Dictionary?style=social)|
|[JumanDIC](https://github.com/ku-nlp/JumanDIC)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/JumanDIC?style=social)|
|[ipadic-py](https://github.com/polm/ipadic-py)|[![Downloads](https://pepy.tech/badge/ipadic/week)](https://pepy.tech/project/ipadic)|[![Downloads](https://pepy.tech/badge/ipadic)](https://pepy.tech/project/ipadic)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/ipadic-py?style=social)|
|[unidic-lite](https://github.com/polm/unidic-lite)|[![Downloads](https://pepy.tech/badge/unidic-lite/week)](https://pepy.tech/project/unidic-lite)|[![Downloads](https://pepy.tech/badge/unidic-lite)](https://pepy.tech/project/unidic-lite)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/unidic-lite?style=social)|
|[emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/peaceiris/emoji-ime-dictionary?style=social)|
|[google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/peaceiris/google-ime-dictionary?style=social)|
|[dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ncaq/dic-nico-intersection-pixiv?style=social)|
|[google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KEINOS/google-ime-user-dictionary-ja-en?style=social)|
|[emoticon](https://github.com/tiwanari/emoticon)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tiwanari/emoticon?style=social)|
|[mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/akirakubo/mecab-mozcdic?style=social)|
|[denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/albno273/denonbu-ime-dic?style=social)|
|[nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Umichang/nijisanji-ime-dic?style=social)|
|[pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Umichang/pokemon-ime-dic?style=social)|
|[EJDict](https://github.com/kujirahand/EJDict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kujirahand/EJDict?style=social)|
|[Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Rinrin0413/Ayashiy-Nipongo-Dic?style=social)|
|[genshin-dict](https://github.com/kotofurumiya/genshin-dict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kotofurumiya/genshin-dict?style=social)|
|[jmdict-simplified](https://github.com/scriptin/jmdict-simplified)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/scriptin/jmdict-simplified?style=social)|
|[mozcdict-ext](https://github.com/reasonset/mozcdict-ext)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/reasonset/mozcdict-ext?style=social)|
|[mh-dict-jp](https://github.com/utubo/mh-dict-jp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/utubo/mh-dict-jp?style=social)|


## Corpus

### Part-of-speech tagging / Named entity recognition

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - Dataset for extracting named entities in Japanese using Wikipedia
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - Japanese IOB2 tagged corpus for Named Entity Recognition.
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - Capital Japanese Twitter Corpus
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - Parallel Universal Dependencies.
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - Japanese data from the Google UDT 2.0.
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - Kyoto University Web Document Leads Corpus
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - Annotated Fuman Kaitori Center Corpus


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/stockmarkteam/ner-wikipedia-dataset?style=social)|
|[IOB2Corpus](https://github.com/Hironsan/IOB2Corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/IOB2Corpus?style=social)|
|[TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/TwitterCorpus?style=social)|
|[UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/UD_Japanese-PUD?style=social)|
|[UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/UD_Japanese-GSD?style=social)|
|[KWDLC](https://github.com/ku-nlp/KWDLC)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/KWDLC?style=social)|
|[AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/AnnotatedFKCCorpus?style=social)|


### Parallel corpus

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[small_parallel_enja](https://github.com/odashi/small_parallel_enja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/odashi/small_parallel_enja?style=social)|
|[Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT?style=social)|
|[CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shyyhs/CourseraParallelCorpusMining?style=social)|
|[JESC](https://github.com/rpryzant/JESC)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rpryzant/JESC?style=social)|
|[AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tsuruoka-lab/AMI-Meeting-Parallel-Corpus?style=social)|
|[giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/DayuanJiang/giant_ja-en_parallel_corpus?style=social)|
|[jesc_small](https://github.com/yusugomori/jesc_small)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yusugomori/jesc_small?style=social)|
|[graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/marmooo/graded-enja-corpus?style=social)|
|[cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/dahlia/cjk-compsci-terms?style=social)|
|[Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/Laboro-ParaCorpus?style=social)|
|[google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Tzawa/google-vs-deepl-je?style=social)|


### Dialog corpus

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本映画の推薦対話データセット
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - A dialogue corpus created by crawling the 2channel open forum.
 * [BSD](https://github.com/tsuruoka-lab/BSD) - The Business Scene Dialogue corpus
 * [asdc](https://github.com/megagonlabs/asdc) - Accommodation Search Dialog Corpus (宿泊施設探索対話コーパス)
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - Japanese dialogue data for seq2seq, etc.
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - This repository contains the Japanese–English bilingual chat corpus BPersona-chat published in the paper Chat Translation Error Detection for Assisting Cross-lingual Communications at AACL-IJCNLP 2022's Workshop Eval4NLP 2022.
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - Japanese Daily Dialogue, or 日本語日常対話コーパス in Japanese, is a high-quality multi-turn dialogue dataset containing daily conversations on five topics: dailylife, school, travel, health, and entertainment.
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - Japanese chat dataset for building LLM.

|Name|downloads/week|total downloads|stars|
-|-|-|-
|[JMRD](https://github.com/ku-nlp/JMRD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/JMRD?style=social)|
|[open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/1never/open2ch-dialogue-corpus?style=social)|
|[BSD](https://github.com/tsuruoka-lab/BSD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tsuruoka-lab/BSD?style=social)|
|[asdc](https://github.com/megagonlabs/asdc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/asdc?style=social)|
|[japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MokkeMeguru/japanese-corpus?style=social)|
|[BPersona-chat](https://github.com/cl-tohoku/BPersona-chat)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/BPersona-chat?style=social)|
|[japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jqk09a/japanese-daily-dialogue?style=social)|
|[llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/masanorihirano/llm-japanese-dataset?style=social)|

### Others

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jrte-corpus](https://github.com/megagonlabs/jrte-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/jrte-corpus?style=social)|
|[kanji-data](https://github.com/davidluzgouveia/kanji-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/davidluzgouveia/kanji-data?style=social)|
|[JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/JapaneseWordSimilarityDataset?style=social)|
|[simple-jppdb](https://github.com/tmu-nlp/simple-jppdb)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/simple-jppdb?style=social)|
|[chABSA-dataset](https://github.com/chakki-works/chABSA-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/chABSA-dataset?style=social)|
|[JaQuAD](https://github.com/SkelterLabsInc/JaQuAD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/SkelterLabsInc/JaQuAD?style=social)|
|[JaNLI](https://github.com/verypluming/JaNLI)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/verypluming/JaNLI?style=social)|
|[ebe-dataset](https://github.com/megagonlabs/ebe-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ebe-dataset?style=social)|
|[emoji-ja](https://github.com/yagays/emoji-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/emoji-ja?style=social)|
|[nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/nayose-wikipedia-ja?style=social)|
|[ja.text8](https://github.com/Hironsan/ja.text8)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/ja.text8?style=social)|
|[ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KodairaTomonori/ThreeLineSummaryDataset?style=social)|
|[japanese](https://github.com/hingston/japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hingston/japanese?style=social)|
|[kanji-frequency](https://github.com/scriptin/kanji-frequency)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/scriptin/kanji-frequency?style=social)|
|[TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/TEDxJP-10K?style=social)|
|[CoARiJ](https://github.com/chakki-works/CoARiJ)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/CoARiJ?style=social)|
|[technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/textlint-ja/technological-book-corpus-ja?style=social)|
|[ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shirayu/ita-corpus-chuwa?style=social)|
|[wikipedia-utils](https://github.com/singletongue/wikipedia-utils)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/singletongue/wikipedia-utils?style=social)|
|[inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MosasoM/inappropriate-words-ja?style=social)|
|[house-of-councillors](https://github.com/smartnews-smri/house-of-councillors)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/smartnews-smri/house-of-councillors?style=social)|
|[house-of-representatives](https://github.com/smartnews-smri/house-of-representatives)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/smartnews-smri/house-of-representatives?style=social)|
|[STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/STAIR-Lab-CIT/STAIR-captions?style=social)|
|[Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/Winograd-Schema-Challenge-Ja?style=social)|
|[speechBSD](https://github.com/ku-nlp/speechBSD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/speechBSD?style=social)|
|[ita-corpus](https://github.com/mmorise/ita-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mmorise/ita-corpus?style=social)|
|[rohan4600](https://github.com/mmorise/rohan4600)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mmorise/rohan4600?style=social)|
|[anlp-jp-history](https://github.com/whym/anlp-jp-history)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/whym/anlp-jp-history?style=social)|
|[keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/keigo_transfer_task?style=social)|
|[loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jamesohortle/loanwords_gairaigo?style=social)|
|[jawikicorpus](https://github.com/wikiwikification/jawikicorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wikiwikification/jawikicorpus?style=social)|
|[GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan?style=social)|
|[wrime](https://github.com/ids-cv/wrime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ids-cv/wrime?style=social)|
|[jtubespeech](https://github.com/sarulab-speech/jtubespeech)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarulab-speech/jtubespeech?style=social)|
|[WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/maeda6uiui-backup/WikipediaWordFrequencyList?style=social)|
|[kokkosho_data](https://github.com/rindybell/kokkosho_data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rindybell/kokkosho_data?style=social)|
|[pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/pdmocrdataset-part1?style=social)|
|[huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/huriganacorpus-ndlbib?style=social)|
|[jvs_hiho](https://github.com/Hiroshiba/jvs_hiho)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hiroshiba/jvs_hiho?style=social)|
|[hirakanadic](https://github.com/po3rin/hirakanadic)|[![Downloads](https://pepy.tech/badge/hirakanadic/week)](https://pepy.tech/project/hirakanadic)|[![Downloads](https://pepy.tech/badge/hirakanadic)](https://pepy.tech/project/hirakanadic)|![GitHub Repo stars](https://img.shields.io/github/stars/po3rin/hirakanadic?style=social)|
|[animedb](https://github.com/anilogia/animedb)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/anilogia/animedb?style=social)|
|[security_words](https://github.com/SaitoLab/security_words)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/SaitoLab/security_words?style=social)|
|[Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sugi2000/Data-on-Japanese-Diet-Members?style=social)|
|[honkoku-data](https://github.com/yuta1984/honkoku-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuta1984/honkoku-data?style=social)|
|[wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Katsumata420/wikihow_japanese?style=social)|
|[engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mercari/engineer-vocabulary-list?style=social)|
|[JSICK](https://github.com/verypluming/JSICK)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/verypluming/JSICK?style=social)|
|[phishurl-list](https://github.com/JPCERTCC/phishurl-list)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/JPCERTCC/phishurl-list?style=social)|
|[jcms](https://github.com/shigashiyama/jcms)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shigashiyama/jcms?style=social)|
|[aozorabunko_text](https://github.com/aozorahack/aozorabunko_text)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aozorahack/aozorabunko_text?style=social)|
|[friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/astremo/friendly_JA-Corpus?style=social)|
|[topokanji](https://github.com/scriptin/topokanji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/scriptin/topokanji?style=social)|
|[isbn4groups](https://github.com/uribo/isbn4groups)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/uribo/isbn4groups?style=social)|
|[NMeCab](https://github.com/komutan/NMeCab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/komutan/NMeCab?style=social)|
|[ndlngramdata](https://github.com/ndl-lab/ndlngramdata)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndlngramdata?style=social)|
|[ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndlngramviewer_v2?style=social)|
|[data_set](https://github.com/japanese-law-analysis/data_set)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/japanese-law-analysis/data_set?style=social)|
|[huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_wrime?style=social)|
|[ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndl-minhon-ocrdataset?style=social)|
|[PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/AsPJT/PAX_SAPIENTICA?style=social)|
|[j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tasukuigarashi/j-liwc2015?style=social)|
|[huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_livedoor-news-corpus?style=social)|
|[huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_JGLUE?style=social)|
|[commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Language-Media-Lab/commonsense-moral-ja?style=social)|
|[comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-waseda/comet-atomic-ja?style=social)|
|[dcsg-ja](https://github.com/nlp-waseda/dcsg-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-waseda/dcsg-ja?style=social)|
|[japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/inspection-ai/japanese-toxic-dataset?style=social)|
|[camera](https://github.com/CyberAgentAILab/camera)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CyberAgentAILab/camera?style=social)|
|[Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-Fakenews-Dataset?style=social)|
|[jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aiishii/jpn_explainable_qa_dataset?style=social)|
|[copa-japanese](https://github.com/nlp-titech/copa-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-titech/copa-japanese?style=social)|
|[WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/masayu-a/WLSP-familiarity?style=social)|
|[ProSub](https://github.com/matbahasa/ProSub)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/matbahasa/ProSub?style=social)|
|[commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Language-Media-Lab/commonsense-moral-ja?style=social)|
|[ramendb](https://github.com/nuko-yokohama/ramendb)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nuko-yokohama/ramendb?style=social)|
|[huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_CAMERA?style=social)|
|[FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-waseda/FactCheckSentenceNLI-FCSNLI-?style=social)|
|[databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kunishou/databricks-dolly-15k-ja?style=social)|
|[EaST-MELD](https://github.com/ku-nlp/EaST-MELD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/EaST-MELD?style=social)|
|[meconaudio](https://github.com/elith-co-jp/meconaudio)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/elith-co-jp/meconaudio?style=social)|
|[japanese-addresses](https://github.com/geolonia/japanese-addresses)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/geolonia/japanese-addresses?style=social)|
|[aozorasearch](https://github.com/myokoym/aozorasearch)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/myokoym/aozorasearch?style=social)|
|[llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/llm-jp/llm-jp-corpus?style=social)|


## Tutorial

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


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[spacy_tutorial](https://github.com/yuibi/spacy_tutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuibi/spacy_tutorial?style=social)|
|[fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/icoxfog417/fastTextJapaneseTutorial?style=social)|
|[allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/allennlp-NER-ja?style=social)|
|[chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ymym3412/chariot-PyTorch-Japanese-text-classification?style=social)|
|[ginza-examples](https://github.com/poyo46/ginza-examples)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/poyo46/ginza-examples?style=social)|
|[DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nekoumei/DocumentClassificationUsingBERT-Japanese?style=social)|
|[BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/YutaroOgawa/BERT_Japanese_Google_Colaboratory?style=social)|
|[bert-book](https://github.com/stockmarkteam/bert-book)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/stockmarkteam/bert-book?style=social)|
|[janome-tutorial](https://github.com/mocobeta/janome-tutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mocobeta/janome-tutorial?style=social)|
|[handson-language-models](https://github.com/hnishi/handson-language-models)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hnishi/handson-language-models?style=social)|
|[JapaneseNLI](https://github.com/verypluming/JapaneseNLI)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/verypluming/JapaneseNLI?style=social)|
|[deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Gin5050/deep-learning-with-pytorch-ja?style=social)|
|[bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/bert-classification-tutorial?style=social)|
|[python-nlp-book](https://github.com/python-nlp-book/python-nlp-book)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/python-nlp-book/python-nlp-book?style=social)|
|[llm-book](https://github.com/ghmagazine/llm-book)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ghmagazine/llm-book?style=social)|


## Research summary

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - A list of pre-trained BERT models for Japanese with word/subword tokenization + vocabulary construction algorithm information
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - Repository for collecting and categorizing Japanese literature on correcting grammar errors.
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - lists of text corpus and more (mainly Japanese)
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - A playbook for systematically maximizing the performance of deep learning models.
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - Trying to consolidate japanese phonetic, and in particular pitch accent resources into one list
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - Summary of Japanese LLM (Open Source)


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/awesome-bert-japanese?style=social)|
|[GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gotutiyan/GEC-Info-ja?style=social)|
|[dataset-list](https://github.com/ikegami-yukino/dataset-list)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/dataset-list?style=social)|
|[tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Valkyrja3607/tuning_playbook_ja?style=social)|
|[japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/olety/japanese-pitch-accent-resources?style=social)|
|[awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/llm-jp/awesome-japanese-llm?style=social)|


## Reference

 * [自然言語処理の餅屋](https://www.jnlp.org/nlp/top)
 * [フリーで使える日本語の主な大規模言語モデルまとめ](https://zenn.dev/hellorusk/articles/ddee520a5e4318)
 * [yasuokaの日記： 日本語係り受け解析器「2020年の総ざらえ」](https://srad.jp/~yasuoka/journal/643631/)
 * [yasuokaの日記： 日本語係り受け解析器「2021年の総ざらえ」](https://srad.jp/~yasuoka/journal/651542/)
 * https://github.com/topics/japanese?l=python
 * https://github.com/topics/japanese-language?l=python
 * https://github.com/search?o=desc&q=corpus+japanese&s=&type=Repositories
 * https://paperswithcode.com/datasets?lang=japanese
 * https://github.com/himkt/awesome-bert-japanese
 * [Awesome-Rust-MachineLearning-日本語向けのrustクレートや記事等をまとめたもの](https://github.com/vaaaaanquish/Awesome-Rust-MachineLearning/blob/main/README.ja.md)


## Contributors

 * [kaisugi](https://github.com/kaisugi) - [website](https://hellorusk.net)
 * [bomin0624](https://github.com/bomin0624) - [twitter](https://twitter.com/bomin0624_c)
 * [passaglia](https://github.com/passaglia) - [twitter](https://twitter.com/SamPassaglia)
