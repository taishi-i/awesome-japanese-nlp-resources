# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of resources dedicated to Python libraries, llms, dictionaries, and corpora of NLP for Japanese

- Listed information on [710 GitHub repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md)
- Listed information on [1972 Hugging Face repositories](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md) (models and datasets)
- Released [a tool 🔎](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search) for searching through a large number of repository information


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## 🎉 The latest additions

**Python**
 * [fastrtc-jp](https://github.com/route250/fastrtc-jp) - Japanese TTS and STT add-on kit for fastrtc

_Updated on Jun 24, 2025_

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


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [jdepp-python](https://github.com/lighttransport/jdepp-python) - Python binding for J.DepP(C++ implementation of Japanese Dependency Parsers)
 * [lightblue](https://github.com/daisukebekki/lightblue) - A CCG parser for Japanese with DTS-representations
 * [natsume-simple](https://github.com/borh-lab/natsume-simple) - natsume-simple is a Japanese dependency relation search system.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Converter

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


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Preprocessor

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - Japanese text normalizer for mecab-neologd
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - A Python-based tool for converting Japanese characters between Hiragana, Katakana, Hankaku, and Zenkaku.
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - A quick converter for Japanese half-width and full-width characters.
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - A powerful text cleaner for Japanese web texts
 * [HojiChar](https://github.com/HojiChar/HojiChar) - A text preprocessing tool that configures and manages multiple preprocessing steps.
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho is a Python module that facilitates bidirectional conversion between half-width katakana and full-width katakana in Japanese.
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - Yet Another Fast Japanese String Converter
 * [kairyou](https://github.com/bikatr7/kairyou) - Quickly preprocesses Japanese text using NLP/NER from SpaCy for Japanese translation or other NLP tasks.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Sentence spliter

 * [Bunkai](https://github.com/megagonlabs/bunkai) - Sentence boundary disambiguation tool for Japanese texts (日本語文境界判定器)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - Japanese Sentence Breaker
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - Yet another sentence-level tokenizer for the Japanese text
 * [budoux](https://github.com/google/budoux) - Standalone. Small. Language-neutral. BudouX is the successor to Budou, the machine learning powered line break organizer tool.
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - japanese sentence segmentation library for python
 * [hasami](https://github.com/mkartawijaya/hasami) - A tool to perform sentence segmentation on Japanese text
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - Japanese Text Segmenter for Python written in Rust
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - Comparison of Japanese Sentence Segmentation Tools


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Sentiment analysis

 * [oseti](https://github.com/ikegami-yukino/oseti) - Dictionary based Sentiment Analysis for Japanese
 * [negapoji](https://github.com/liaoziyang/negapoji) - Japanese document sentiment analysis to determine negative or positive.
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - Emotion analyzer for Japanese text
 * [asari](https://github.com/Hironsan/asari) - Japanese sentiment analyzer implemented in Python.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Machine translation

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - An example usage of JParaCrawl pre-trained Neural Machine Translation (NMT) models.
 * [JASS](https://github.com/Mao-KU/JASS) - JASS: Japanese-specific Sequence to Sequence Pre-training for Neural Machine Translation (LREC2020) & Linguistically Driven Multi-Task Pre-Training for Low-Resource Neural Machine Translation (ACM TALLIP)
 * [PheMT](https://github.com/cl-tohoku/PheMT) - A phenomenon-wise evaluation dataset for Japanese-English machine translation robustness. The dataset is based on the MTNT dataset, with additional annotations of four linguistic phenomena; Proper Noun, Abbreviated Noun, Colloquial Expression, and Variant. COLING 2020.
 * [VISA](https://github.com/ku-nlp/VISA) - An ambiguous subtitles dataset for visual scene-aware machine translation


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Named entity recognition

 * [namaco](https://github.com/chakki-works/namaco) - Character Based Named Entity Recognition.
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia is an Extended Named Entity Dictionary from Wikipedia.
 * [noyaki](https://github.com/ken11/noyaki) - Converts character span label information to tokenized text-based label information.
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - This is a sample code for creating and using a model for named entity recognition task through finetuning of the BERT model.
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - Code for inferring the accuracy of named entity and relation extraction from a case report corpus based on detailed annotation criteria.
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp, A python module for geotagging Japanese texts.
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - Program for fine-tuning Japanese named entity recognition using BERT
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - Examples to finetune encoder-only and encoder-decoder transformers for Japanese language (Hugging Face) Resources


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [owocr](https://github.com/aurorawright/owocr) - Optical character recognition for Japanese text
 * [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) - Yomitoku is an AI-powered document image analysis package designed specifically for the Japanese language.
 * [findtextcenternet](https://github.com/lithium0003/findtextcenternet) - Japanese OCR with CenterNet
 * [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) - A simple OCR for manga (Japanese traditional and Japanese vertical)


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - The repository contains scripts and merge scripts that have been modified to adapt an Alpaca-Lora adapter for LoRA tuning when assuming the use of the "rinna/japanese-gpt-neox..." [gpt-neox] model converted to ggml.
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - This repository was created to evaluate the performance of character role-playing in Japanese LLM.
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - This repository supports YuzuAI's Rakuda leaderboard of Japanese LLMs, which is a Japanese-focused analogue of LMSYS' Vicuna eval.
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - This tool is designed to automatically evaluate large-scale Japanese language models across multiple datasets.
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - This repository contains the code for supervised fine-tuning of LLM-jp models.
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - This is a repository that summarizes the tokenizer related to LLM being developed at the LLM Study Group (LLM-jp).
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - 日本語言模型金融评估工具
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - Japanese Vicuna QA Benchmark
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - Swallow Project Large-Scale Language Model Evaluation Script


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
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


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


## C++

### Morphology analysis

 * [mecab](https://github.com/taku910/mecab) - Yet another Japanese morphological analyzer
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++ (a Morphological Analyzer Toolkit)
 * [kytea](https://github.com/neubig/kytea) - The Kyoto Text Analysis Toolkit for word segmentation and pronunciation estimation, etc.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).

### Parsing

 * [cabocha](https://github.com/taku910/cabocha) - Yet Another Japanese Dependency Structure Analyzer
 * [knp](https://github.com/ku-nlp/knp) - A Japanese Parser


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).

### Others

 * [jsc](https://github.com/yohokuno/jsc) - Joint source channel model for Japanese Kana Kanji conversion, Chinese pinyin input and CJE mixed input.
 * [aquaskk](https://github.com/codefirst/aquaskk) - An input method without morphological analysis.
 * [mozc](https://github.com/google/mozc) - Mozc - a Japanese Input Method Editor designed for multi-platform
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch: An (Exact|Prefix|Approximate) String Matching Library
 * [resembla](https://github.com/tuem/resembla) - Resembla: Word-based Japanese similar sentence search library
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ SKK-like Japanese Input Method Editor for Windows


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


## Rust crate

### Morphology analysis

 * [lindera](https://github.com/lindera-morphology/lindera) - A morphological analysis library.
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto: Very Accelerated POintwise pREdicTion based TOkenizer
 * [goya](https://github.com/Leko/goya) - Japanese Morphological Analysis written in Rust
 * [vibrato](https://github.com/daac-tools/vibrato) - vibrato: Viterbi-based accelerated tokenizer
 * [yoin](https://github.com/agatan/yoin) - A Japanese Morphological Analyzer written in pure Rust
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - Safe Rust bindings for mecab a part-of-speech and morphological analyzer library
 * [awabi](https://github.com/nakagami/awabi) - A morphological analyzer using mecab dictionary
 * [kanpyo](https://github.com/togatoga/kanpyo) - Japanese Morphological Analyzer written in Rust


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Converter

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - Utility library for checking and converting between Japanese characters - Hiragana, Katakana - and Romaji
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - A Rust library to convert Japanese Half-width-kana[半角ｶﾅ] and Wide-alphanumeric[全角英数] into normal ones
 * [kana](https://github.com/gbrlsnchs/kana) - [Mirror] CLI program for transliterating romaji text to either hiragana or katakana
 * [kanaria](https://github.com/samunohito/kanaria) - This library provides functions such as mutual conversion and discrimination of hiragana, katakana, half-width, and full-width characters.
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - This is a library that splits Japanese addresses into prefecture/city or town/village/neighborhood/other.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Search engine library

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy.
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - A Tantivy tokenizer using Vibrato.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [cskk](https://github.com/naokiri/cskk) - SKK (Simple Kana Kanji conversion) library
 * [japanki](https://github.com/tysonwu/japanki) - Learn Japanese vocabs 🇯🇵 by doing quizzes on CLI!
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - Japanese text preprocessor for Text-to-Speech applications (OpenJTalk rewrite in rust language)
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - Software that scrapes and generates a list of case law data from the court's website (https://www.courts.go.jp/index.html)
 * [jisho](https://github.com/eagleflo/jisho) - Jisho is a CLI tool & Rust library that provides a Japanese-English dictionary.
 * [kanalizer](https://github.com/voicevox/kanalizer) - Library that guesses readings from English words.
 * [koharu](https://github.com/mayocream/koharu) - Automated manga translation tool with LLM, written in Rust.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


## JavaScript

### Morphology analysis

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - JavaScript implementation of Japanese morphological analyzer
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) -  Rakuten MA - morphological analyzer (word segmentor + PoS Tagger) for Chinese and Japanese written purely in JavaScript.
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - Yet another mecab wrapper for nodejs
 * [juman-bin](https://github.com/thammin/juman-bin) - a User-Extensible Morphological Analyzer for Japanese. 日本語形態素解析システム
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - Asynchronous japanese morphological analyser using MeCab.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [jaconv](https://github.com/kazuhikoarase/jaconv) - Japanese text conversion library (javascript)
 * [romaji-conv](https://github.com/koozaki/romaji-conv) - Convert romaji into hiragana
 * [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) - National address data API
 * [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) - Convert text words to emojis


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [pitch-accent](https://github.com/shirakaba/pitch-accent) - Predict pitch accent in Japanese
 * [kana2ipa](https://github.com/amanoese/kana2ipa) - Command to convert "hiragana" or "katakana" into International Phonetic Alphabet (IPA) symbols when pronouncing in Japanese.
 * [voicevox](https://github.com/VOICEVOX/voicevox) - Editor for VOICEVOX, a high-quality text-to-speech software that can be used for free.
 * [kamiya-codec](https://github.com/fasiha/kamiya-codec) - Towards a Japanese verb conjugator and deconjugator based on Taeko Kamiya's *The Handbook of Japanese Verbs* and *The Handbook of Japanese Adjectives and Adverbs* opuses.
 * [closewords](https://github.com/otoneko1102/closewords) - A library that searches for the most similar word from a group of words in Japanese (including kanji)


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


## Go

### Morphology analysis

 * [kagome](https://github.com/ikawaha/kagome) - Self-contained Japanese Morphological Analyzer written in pure Go


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Others

 * [ojosama](https://github.com/jiro4989/ojosama) - Converts text into the tone of Lady Salome from the Hundred Celestial Plains.
 * [nihongo](https://github.com/gojp/nihongo) - Japanese Dictionary
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - External dictionary importer for Yomichan.
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - THE IDOLM@STER words dictionary for Japanese IME (by imas-db.jp)
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - Kanji 転写 to hiragana/katakana/romaji, in Go
 * [go-moji](https://github.com/ktnyt/go-moji) - A Go library for Zenkaku/Hankaku conversion
 * [ojichat](https://github.com/greymd/ojichat) - Generate sentences that an uncle would send via LINE or email.
 * [name](https://github.com/kuniwak/name) - 名前検索者


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


## Java

### Morphology analysis

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji is a self-contained and very easy to use Japanese morphological analyzer designed for search
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - A lexicon for Sudachi
 * [meval](https://github.com/teru-oka-1933/meval) - Morphological analyzer performance evaluation system MevAL


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Others

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - Java library for identifying Japanese characters from images
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - Java library and command-line tool to transliterate Japanese kanji to romaji (Latin alphabet)
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Kanji transliteration to hiragana/katakana/romaji, in Java
 * [Kamite](https://github.com/fauu/Kamite) - A desktop language immersion companion for learners of Japanese
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - Async Japanese Tokenizer Native Plugin for React Native for iOS and Android
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - The Japanese analyzer utilizes the Kuromoji Japanese tokenizer for ElasticSearch.
 * [moji4j](https://github.com/andree-surya/moji4j) - A Java library to converts between Japanese Hiragana, Katakana, and Romaji scripts.
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - Japanese text normalizer for mecab-neologd
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - The Japanese analysis plugin for elasticsearch


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) - Pretrained models, codes and guidances to pretrain official ALBERT(https://github.com/google-research/albert) on Japanese Wikipedia Resources
 * [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) - 日本のLLaMa実験
 * [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) - EasyLightChatAssistant は軽量で検閲や規制のないローカル日本語モデルのLightChatAssistant を、KoboldCpp で簡単にお試しする環境です。


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [character_chat](https://github.com/mutaguchi/character_chat) - This is a chat script that uses OpenAI's API to have a conversation with a character set in Japanese.
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - Slackbot script for using OpenAI's ChatGPT API on Slack (assumes usage in Japanese)
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - This is a sample of ChatGPT's prompt.
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - A Japanese Kanji Flashcard App built using Python and Langchain, enhanced with the intelligence of GPT-4.
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - Evaluating GPT-4 and ChatGPT on Japanese Medical Licensing Examinations
 * [japagen](https://github.com/retrieva/japagen) - Investigation of pseudo-learning data generation using LLM in Japanese language tasks
  * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - Sample prompts for various generative AIs such as ChatGPT and Copilot in Japanese.


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


## Dictionary and IME

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


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).



## Corpus

### Part-of-speech tagging / Named entity recognition

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - Dataset for extracting named entities in Japanese using Wikipedia
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - Japanese IOB2 tagged corpus for Named Entity Recognition.
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - Capital Japanese Twitter Corpus
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - Parallel Universal Dependencies.
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - Japanese data from the Google UDT 2.0.
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - Kyoto University Web Document Leads Corpus
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - Annotated Fuman Kaitori Center Corpus
 * [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) - Long-unit-word version of UD_Japanese-GSD


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
 * [matcha](https://github.com/ehimenlp/matcha) - We have created a dataset for simplifying Japanese text from an article on the Japanese tourism media MATCHA for visitors to Japan.
 * [en-ja-el](https://github.com/shigashiyama/en-ja-el) - EnJaEL: En-Ja Parallel Entity Linking Dataset (Version 1.0)


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


### Dialog corpus

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本映画の推薦対話データセット
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - A dialogue corpus created by crawling the 2channel open forum.
 * [BSD](https://github.com/tsuruoka-lab/BSD) - The Business Scene Dialogue corpus
 * [asdc](https://github.com/megagonlabs/asdc) - Accommodation Search Dialog Corpus (宿泊施設探索対話コーパス)
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - Japanese dialogue data for seq2seq, etc.
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - This repository contains the Japanese–English bilingual chat corpus BPersona-chat published in the paper Chat Translation Error Detection for Assisting Cross-lingual Communications at AACL-IJCNLP 2022's Workshop Eval4NLP 2022.
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - Japanese Daily Dialogue, or 日本語日常対話コーパス in Japanese, is a high-quality multi-turn dialogue dataset containing daily conversations on five topics: dailylife, school, travel, health, and entertainment.
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - Japanese chat dataset for building LLM.
 * [kokorochat](https://github.com/uec-inabalab/kokorochat) - Counseling dialogue dataset collected through role-playing in Japanese


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


## Research summary

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - A list of pre-trained BERT models for Japanese with word/subword tokenization + vocabulary construction algorithm information
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - Repository for collecting and categorizing Japanese literature on correcting grammar errors.
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - lists of text corpus and more (mainly Japanese)
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - A playbook for systematically maximizing the performance of deep learning models.
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - Trying to consolidate japanese phonetic, and in particular pitch accent resources into one list
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - Summary of Japanese LLM (Open Source)


To check the statistics table (GitHub stars ⭐ / Downloads 📥), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).


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
