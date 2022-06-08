# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of resources dedicated to **Python libraries** of NLP for Japanese


## Contents

 * [Morphology analysis](#Morphology-analysis)
 * [Parsing](#Parsing)
 * [Converter](#Converter)
 * [Preprocessor](#Preprocessor)
 * [Sentence spliter](#Sentence-spliter)
 * [Sentiment Analysis](#Sentiment-Analysis)
 * [OCR](#OCR)
 * [Others](#Others)
 * [Pretrained model](#Pretrained-model)
 * [Dictionary](#Dictionary)
 * [Reference](#Reference)


## Morphology analysis

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - SudachiPy 0.6* and above are developed as Sudachi.rs.
 * [Janome](https://github.com/mocobeta/janome) - Japanese morphological analysis engine written in pure Python
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - mecab-python. mecab-python. you can find original version here:http://taku910.github.io/mecab/
 * [fugashi](https://github.com/polm/fugashi) - A Cython MeCab wrapper for fast, pythonic Japanese tokenization and morphological analysis.
 * [nagisa](https://github.com/taishi-i/nagisa) - A Japanese tokenizer based on recurrent neural networks
 * [pyknp](https://github.com/ku-nlp/pyknp) - A Python Module for JUMAN++/KNP
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - Python wrapper for KyTea
 * [konoha](https://github.com/himkt/konoha) - Konoha: Simple wrapper of Japanese Tokenizers
 * [natto-py](https://github.com/buruzaemon/natto-py) - natto-py combines the Python programming language with MeCab, the part-of-speech and morphological analyzer for the Japanese language.
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - Rakuten MA (Python version)


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[SudachiPy](https://github.com/WorksApplications/SudachiPy)|[![Downloads](https://pepy.tech/badge/sudachipy/week)](https://pepy.tech/project/sudachipy)|[![Downloads](https://pepy.tech/badge/sudachipy)](https://pepy.tech/project/sudachipy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiPy?style=social)|
|[Janome](https://github.com/mocobeta/janome)|[![Downloads](https://pepy.tech/badge/janome/week)](https://pepy.tech/project/janome)|[![Downloads](https://pepy.tech/badge/janome)](https://pepy.tech/project/janome)|![GitHub Repo stars](https://img.shields.io/github/stars/mocobeta/janome?style=social)|
|[mecab-python3](https://github.com/SamuraiT/mecab-python3)|[![Downloads](https://pepy.tech/badge/mecab-python3/week)](https://pepy.tech/project/mecab-python3)|[![Downloads](https://pepy.tech/badge/mecab-python3)](https://pepy.tech/project/mecab-python3)|![GitHub Repo stars](https://img.shields.io/github/stars/SamuraiT/mecab-python3?style=social)|
|[fugashi](https://github.com/polm/fugashi)|[![Downloads](https://pepy.tech/badge/fugashi/week)](https://pepy.tech/project/fugashi)|[![Downloads](https://pepy.tech/badge/fugashi)](https://pepy.tech/project/fugashi)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/fugashi?style=social)|
|[nagisa](https://github.com/taishi-i/nagisa)|[![Downloads](https://pepy.tech/badge/nagisa/week)](https://pepy.tech/project/nagisa)|[![Downloads](https://pepy.tech/badge/nagisa)](https://pepy.tech/project/nagisa)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/nagisa?style=social)|
|[pyknp](https://github.com/ku-nlp/pyknp)|[![Downloads](https://pepy.tech/badge/pyknp/week)](https://pepy.tech/project/pyknp)|[![Downloads](https://pepy.tech/badge/pyknp)](https://pepy.tech/project/pyknp)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/pyknp?style=social)|
|[Mykytea-python](https://github.com/chezou/Mykytea-python)|[![Downloads](https://pepy.tech/badge/kytea/week)](https://pepy.tech/project/kytea)|[![Downloads](https://pepy.tech/badge/kytea)](https://pepy.tech/project/kytea)|![GitHub Repo stars](https://img.shields.io/github/stars/chezou/Mykytea-python?style=social)|
|[konoha](https://github.com/himkt/konoha)|[![Downloads](https://pepy.tech/badge/konoha/week)](https://pepy.tech/project/konoha)|[![Downloads](https://pepy.tech/badge/konoha)](https://pepy.tech/project/konoha)|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/konoha?style=social)|
|[natto-py](https://github.com/buruzaemon/natto-py)|[![Downloads](https://pepy.tech/badge/natto-py/week)](https://pepy.tech/project/natto-py)|[![Downloads](https://pepy.tech/badge/natto-py)](https://pepy.tech/project/natto-py)|![GitHub Repo stars](https://img.shields.io/github/stars/buruzaemon/natto-py?style=social)|
|[rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python)|[![Downloads](https://pepy.tech/badge/rakutenma/week)](https://pepy.tech/project/rakutenma)|[![Downloads](https://pepy.tech/badge/rakutenma)](https://pepy.tech/project/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/rakutenma-python?style=social)|




## Parsing

 * [ginza](https://github.com/megagonlabs/ginza) - A Japanese NLP Library using spaCy as framework based on Universal Dependencies
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - Camphr - NLP libary for creating pipeline components
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - Tokenizer POS-tagger Lemmatizer and Dependency-parser for modern and contemporary Japanese with BERT models
 * [depccg](https://github.com/masashi-y/depccg) - A* CCG Parser with a Supertag and Dependency Factored Model


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ginza](https://github.com/megagonlabs/ginza)|[![Downloads](https://pepy.tech/badge/ginza/week)](https://pepy.tech/project/ginza)|[![Downloads](https://pepy.tech/badge/ginza)](https://pepy.tech/project/ginza)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ginza?style=social)|
|[UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD)|[![Downloads](https://pepy.tech/badge/UniDic2UD/week)](https://pepy.tech/project/UniDic2UD)|[![Downloads](https://pepy.tech/badge/UniDic2UD)](https://pepy.tech/project/UniDic2UD)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/UniDic2UD?style=social)|
|[camphr](https://github.com/PKSHATechnology-Research/camphr)|[![Downloads](https://pepy.tech/badge/camphr/week)](https://pepy.tech/project/camphr)|[![Downloads](https://pepy.tech/badge/camphr)](https://pepy.tech/project/camphr)|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/camphr?style=social)|
|[SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic)|[![Downloads](https://pepy.tech/badge/SuParUniDic/week)](https://pepy.tech/project/SuParUniDic)|[![Downloads](https://pepy.tech/badge/SuParUniDic)](https://pepy.tech/project/SuParUniDic)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/SuPar-UniDic?style=social)|
|[depccg](https://github.com/masashi-y/depccg)|[![Downloads](https://pepy.tech/badge/depccg/week)](https://pepy.tech/project/depccg)|[![Downloads](https://pepy.tech/badge/depccg)](https://pepy.tech/project/depccg)|![GitHub Repo stars](https://img.shields.io/github/stars/masashi-y/depccg?style=social)|




## Converter

 * [pykakasi](https://github.com/miurahr/pykakasi) - Lightweight converter from Japanese Kana-kanji sentences into Kana-Roman.
 * [cutlet](https://github.com/polm/cutlet) - Japanese to romaji converter in Python
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - Convert English alphabet to Katakana


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[pykakasi](https://github.com/miurahr/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi/week)](https://pepy.tech/project/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi)](https://pepy.tech/project/pykakasi)|![GitHub Repo stars](https://img.shields.io/github/stars/miurahr/pykakasi?style=social)|
|[cutlet](https://github.com/polm/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet/week)](https://pepy.tech/project/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet)](https://pepy.tech/project/cutlet)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/cutlet?style=social)|
|[alphabet2kana](https://github.com/shihono/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana/week)](https://pepy.tech/project/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana)](https://pepy.tech/project/alphabet2kana)|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/alphabet2kana?style=social)|


## Preprocessor

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - Japanese text normalizer for mecab-neologd
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, and Zenkaku
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - A fast converter between Japanese hankaku and zenkaku characters


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[neologdn](https://github.com/ikegami-yukino/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn/week)](https://pepy.tech/project/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn)](https://pepy.tech/project/neologdn)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/neologdn?style=social)|
|[jaconv](https://github.com/ikegami-yukino/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv/week)](https://pepy.tech/project/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv)](https://pepy.tech/project/jaconv)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/jaconv?style=social)|
|[mojimoji](https://github.com/studio-ousia/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji/week)](https://pepy.tech/project/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji)](https://pepy.tech/project/mojimoji)|![GitHub Repo stars](https://img.shields.io/github/stars/studio-ousia/mojimoji?style=social)|


## Sentence spliter

 * [Bunkai](https://github.com/megagonlabs/bunkai) - Sentence boundary disambiguation tool for Japanese texts (日本語文境界判定器)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - Japanese Sentence Breaker
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - Yet another sentence-level tokenizer for the Japanese text


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bunkai](https://github.com/megagonlabs/bunkai)|[![Downloads](https://pepy.tech/badge/bunkai/week)](https://pepy.tech/project/bunkai)|[![Downloads](https://pepy.tech/badge/bunkai)](https://pepy.tech/project/bunkai)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/bunkai?style=social)|
|[japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker)|[![Downloads](https://pepy.tech/badge/japanese-sentence-breaker/week)](https://pepy.tech/project/japanese-sentence-breaker)|[![Downloads](https://pepy.tech/badge/japanese-sentence-breaker)](https://pepy.tech/project/japanese-sentence-breaker)|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/japanese-sentence-breaker?style=social)|
|[sengiri](https://github.com/ikegami-yukino/sengiri)|[![Downloads](https://pepy.tech/badge/sengiri/week)](https://pepy.tech/project/sengiri)|[![Downloads](https://pepy.tech/badge/sengiri)](https://pepy.tech/project/sengiri)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/sengiri?style=social)|


## Sentiment Analysis

 * [oseti](https://github.com/ikegami-yukino/oseti) - Dictionary based Sentiment Analysis for Japanese
 * [negapoji](https://github.com/liaoziyang/negapoji) - Japanese negative positive classification.日本語文書のネガポジを判定。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - Emotion analyzer for Japanese text


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[oseti](https://github.com/ikegami-yukino/oseti)|[![Downloads](https://pepy.tech/badge/oseti/week)](https://pepy.tech/project/oseti)|[![Downloads](https://pepy.tech/badge/oseti)](https://pepy.tech/project/oseti)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/oseti?style=social)|
|[negapoji](https://github.com/liaoziyang/negapoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/liaoziyang/negapoji?style=social)|
|[pymlask](https://github.com/ikegami-yukino/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask/week)](https://pepy.tech/project/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask)](https://pepy.tech/project/pymlask)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/pymlask?style=social)|



## OCR

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - About Optical character recognition for Japanese text, with the main focus being Japanese manga
 * [mokuro](https://github.com/kha-white/mokuro) - Read Japanese manga inside browser with selectable text.
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - Handwritten Japanese OCR demo using touch panel to draw the input text using Intel OpenVINO toolkit


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[manga-ocr](https://github.com/kha-white/manga-ocr)|[![Downloads](https://pepy.tech/badge/manga-ocr/week)](https://pepy.tech/project/manga-ocr)|[![Downloads](https://pepy.tech/badge/manga-ocr)](https://pepy.tech/project/manga-ocr)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/manga-ocr?style=social)|
|[mokuro](https://github.com/kha-white/mokuro)|[![Downloads](https://pepy.tech/badge/mokuro/week)](https://pepy.tech/project/mokuro)|[![Downloads](https://pepy.tech/badge/mokuro)](https://pepy.tech/project/mokuro)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/mokuro?style=social)|
|[handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yas-sim/handwritten-japanese-ocr?style=social)|

## Others

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - A tool for dividing the Japanese full name into a family name and a given name.
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - A curated list of resources dedicated to Python libraries of NLP for Japanese
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - python版日本語意味役割付与システム（ASA）
 * [toiro](https://github.com/taishi-i/toiro) - A comparison tool of Japanese tokenizers
 * [ja-timex](https://github.com/yagays/ja-timex) - 自然言語で書かれた時間情報表現を抽出/規格化するルールベースの解析器
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - A set of metrics for feature selection from text data
 * [daaja](https://github.com/kajyuuen/daaja) - This repository has implementations of data augmentation for NLP for Japanese.
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - The purpose of this repository is to make prototypes as case study in the context of proof of concept(PoC) and research and development(R&D) that I have written in my website. The main research topics are Auto-Encoders in relation to the representation learning, the statistical machine learning for energy-based models, adversarial generation net…
 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE: Japanese General Language Understanding Evaluation
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - A processor for KyotoCorpus, KWDLC, and AnnotatedFKCCorpus

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


## Pretrained model

 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - Code for producing Japanese pretrained models provided by rinna Co., Ltd.
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - Japanese tokenizer for Transformers
 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - A list of pre-trained BERT models for Japanese with word/subword tokenization + vocabulary construction algorithm information
 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - Word2vec (word to vectors) approach for Japanese language using Gensim and Mecab.

|Name|downloads/week|total downloads|stars|
-|-|-|-
|[japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-pretrained-models?style=social)|
|[SudachiTra](https://github.com/WorksApplications/SudachiTra)|[![Downloads](https://pepy.tech/badge/SudachiTra/week)](https://pepy.tech/project/SudachiTra)|[![Downloads](https://pepy.tech/badge/SudachiTra)](https://pepy.tech/project/SudachiTra)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiTra?style=social)|
|[awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/awesome-bert-japanese?style=social)|
|[japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/philipperemy/japanese-words-to-vectors?style=social)|




## Dictionary

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - Neologism dictionary based on the language resources on the Web for mecab-ipadic
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - A Japanese accent dictionary generator
 * [jamdict](https://github.com/neocl/jamdict) - Python 3 library for manipulating Jim Breen's JMdict, KanjiDic2, JMnedict and kanji-radical mappings
 * [unidic-py](https://github.com/polm/unidic-py) - Unidic packaged for installation via pip.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neologd/mecab-ipadic-neologd?style=social)|
|[tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/tdmelodic?style=social)|
|[jamdict](https://github.com/neocl/jamdict)|[![Downloads](https://pepy.tech/badge/jamdict/week)](https://pepy.tech/project/jamdict)|[![Downloads](https://pepy.tech/badge/jamdict)](https://pepy.tech/project/jamdict)|![GitHub Repo stars](https://img.shields.io/github/stars/neocl/jamdict?style=social)|
|[unidic-py](https://github.com/polm/unidic-py)|[![Downloads](https://pepy.tech/badge/unidic/week)](https://pepy.tech/project/unidic)|[![Downloads](https://pepy.tech/badge/unidic)](https://pepy.tech/project/unidic)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/unidic-py?style=social)|



## Corpus

 * [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) - Japanese Realistic Textual Entailment Corpus (NLP 2020, LREC 2020)
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - おーぷん2ちゃんねるをクロールして作成した対話コーパス
 * [kanji-data](https://github.com/davidluzgouveia/kanji-data) - A JSON kanji dataset with updated JLPT levels and WaniKani information
 * [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) - Japanese Word Similarity Dataset
 * [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) - A paraphrase database for Japanese text simplification
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter コーパス


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jrte-corpus](https://github.com/megagonlabs/jrte-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/jrte-corpus?style=social)|
|[open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/1never/open2ch-dialogue-corpus?style=social)|
|[kanji-data](https://github.com/davidluzgouveia/kanji-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/davidluzgouveia/kanji-data?style=social)|
|[JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/JapaneseWordSimilarityDataset?style=social)|
|[simple-jppdb](https://github.com/tmu-nlp/simple-jppdb)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/simple-jppdb?style=social)|
|[TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/TwitterCorpus?style=social)|


## Reference

 * [自然言語処理の餅屋](https://www.jnlp.org/nlp/top)
 * [フリーで使える日本語の主な大規模言語モデルまとめ](https://zenn.dev/hellorusk/articles/ddee520a5e4318)
 * [yasuokaの日記： 日本語係り受け解析器「2020年の総ざらえ」](https://srad.jp/~yasuoka/journal/643631/)
 * [yasuokaの日記： 日本語係り受け解析器「2021年の総ざらえ」](https://srad.jp/~yasuoka/journal/651542/)
 * https://github.com/topics/japanese?l=python
 * https://github.com/topics/japanese-language?l=python
