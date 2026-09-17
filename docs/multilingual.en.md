# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

A curated list of multilingual GitHub repositories with Japanese language features
This page lists multilingual libraries, models and datasets that provide concrete Japanese features, such as Japanese language detection, Japanese tokenizers and analyzers, Japanese speech and OCR models, and Japanese splits of datasets. Currently, it includes 155 repositories.

_Updated on Sep 18, 2026_

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/multilingual.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/multilingual.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/multilingual.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/multilingual.zh-hans.md)

## Contents
 * [NLP pipelines](#nlp-pipelines)
 * [Tokenization and segmentation](#tokenization-and-segmentation)
 * [Language identification](#language-identification)
 * [Machine translation](#machine-translation)
 * [Speech recognition](#speech-recognition)
 * [Speech synthesis](#speech-synthesis)
 * [OCR and document AI](#ocr-and-document-ai)
 * [Embeddings and retrieval](#embeddings-and-retrieval)
 * [Full-text search](#full-text-search)
 * [Text normalization and phonetics](#text-normalization-and-phonetics)
 * [Evaluation and datasets](#evaluation-and-datasets)
 * [Text processing utilities](#text-processing-utilities)

## NLP pipelines
General-purpose multilingual NLP frameworks that ship Japanese models or tokenizers

 * [spaCy](https://github.com/explosion/spaCy) - 💫 Industrial-strength Natural Language Processing (NLP) in Python.
 * [stanza](https://github.com/stanfordnlp/stanza) - Stanford NLP Python library for tokenization, sentence segmentation, NER, and parsing of many human languages.
 * [HanLP](https://github.com/hankcs/HanLP) - Natural Language Processing for the next decade. Tokenization, Part-of-Speech Tagging, Named Entity Recognition, Syntactic & Semantic Dependency Parsing, Document Classification.
 * [trankit](https://github.com/nlp-uoregon/trankit) - Trankit is a Light-Weight Transformer-based Python Toolkit for Multilingual Natural Language Processing.
 * [udpipe](https://github.com/ufal/udpipe) - UDPipe: Trainable pipeline for tokenizing, tagging, lemmatizing and parsing Universal Treebanks and other CoNLL-U files.
 * [spark-nlp](https://github.com/JohnSnowLabs/spark-nlp) - State of the Art Natural Language Processing.
 * [openmed](https://github.com/maziyarpanahi/openmed) - Local-first healthcare AI: clinical NER & HIPAA PII de-identification that runs 100% on-device. 2,200+ medical models, 21 languages, Apple MLX + Python, no cloud, no patient data leaving your network. Apache-2.0.
 * [transformers](https://github.com/huggingface/transformers) - 🤗 Transformers: the model-definition framework for state-of-the-art machine learning models in text, vision, audio, and multimodal models, for both inference and training.
 * [nltk](https://github.com/nltk/nltk) - NLTK Source.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [spaCy](https://github.com/explosion/spaCy) | [![Downloads](https://static.pepy.tech/badge/spacy/week)](https://pepy.tech/project/spacy) | [![Downloads](https://static.pepy.tech/badge/spacy)](https://pepy.tech/project/spacy) | ⭐ 34k | 🟢 august|
| 🔗 [stanza](https://github.com/stanfordnlp/stanza) | [![Downloads](https://static.pepy.tech/badge/stanza/week)](https://pepy.tech/project/stanza) | [![Downloads](https://static.pepy.tech/badge/stanza)](https://pepy.tech/project/stanza) | ⭐ 7.9k | 🟢 july|
| 🔗 [HanLP](https://github.com/hankcs/HanLP) | [![Downloads](https://static.pepy.tech/badge/hanlp/week)](https://pepy.tech/project/hanlp) | [![Downloads](https://static.pepy.tech/badge/hanlp)](https://pepy.tech/project/hanlp) | ⭐ 36k | 🟢 last tuesday|
| 🔗 [trankit](https://github.com/nlp-uoregon/trankit) | [![Downloads](https://static.pepy.tech/badge/trankit/week)](https://pepy.tech/project/trankit) | [![Downloads](https://static.pepy.tech/badge/trankit)](https://pepy.tech/project/trankit) | ⭐ 799 | 🔴 july 2025|
| 🔗 [udpipe](https://github.com/ufal/udpipe) | [![Downloads](https://static.pepy.tech/badge/ufal.udpipe/week)](https://pepy.tech/project/ufal.udpipe) | [![Downloads](https://static.pepy.tech/badge/ufal.udpipe)](https://pepy.tech/project/ufal.udpipe) | ⭐ 419 | 🟡 june|
| 🔗 [spark-nlp](https://github.com/JohnSnowLabs/spark-nlp) | [![Downloads](https://static.pepy.tech/badge/spark-nlp/week)](https://pepy.tech/project/spark-nlp) | [![Downloads](https://static.pepy.tech/badge/spark-nlp)](https://pepy.tech/project/spark-nlp) | ⭐ 4.2k | 🟡 june|
| 🔗 [openmed](https://github.com/maziyarpanahi/openmed) | [![Downloads](https://static.pepy.tech/badge/openmed/week)](https://pepy.tech/project/openmed) | [![Downloads](https://static.pepy.tech/badge/openmed)](https://pepy.tech/project/openmed) | ⭐ 5.3k | 🟢 last wednesday|
| 🔗 [transformers](https://github.com/huggingface/transformers) | [![Downloads](https://static.pepy.tech/badge/transformers/week)](https://pepy.tech/project/transformers) | [![Downloads](https://static.pepy.tech/badge/transformers)](https://pepy.tech/project/transformers) | ⭐ 166k | 🟢 yesterday|
| 🔗 [nltk](https://github.com/nltk/nltk) | [![Downloads](https://static.pepy.tech/badge/nltk/week)](https://pepy.tech/project/nltk) | [![Downloads](https://static.pepy.tech/badge/nltk)](https://pepy.tech/project/nltk) | ⭐ 15k | 🟢 yesterday|


## Tokenization and segmentation
Subword, word and sentence boundary handling that works on Japanese text

 * [sentencepiece](https://github.com/google/sentencepiece) - Unsupervised text tokenizer for Neural Network-based text generation.
 * [icu](https://github.com/unicode-org/icu) - The home of the ICU project source code.
 * [wtpsplit](https://github.com/segment-any-text/wtpsplit) - Toolkit to segment text into sentences or other semantic units in a robust, efficient and adaptable way.
 * [charabia](https://github.com/meilisearch/charabia) - Library used by Meilisearch to tokenize queries and documents.
 * [gse](https://github.com/go-ego/gse) - Go efficient multilingual NLP and text segmentation; support English, Chinese, Japanese and others.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [sentencepiece](https://github.com/google/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece/week)](https://pepy.tech/project/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece)](https://pepy.tech/project/sentencepiece) | ⭐ 12k | 🟢 last wednesday|
| 🔗 [icu](https://github.com/unicode-org/icu) | - | - | ⭐ 3.6k | 🟢 yesterday|
| 🔗 [wtpsplit](https://github.com/segment-any-text/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit/week)](https://pepy.tech/project/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit)](https://pepy.tech/project/wtpsplit) | ⭐ 1.3k | 🟡 april|
| 🔗 [charabia](https://github.com/meilisearch/charabia) | - | ![Crates.io](https://img.shields.io/crates/d/charabia) | ⭐ 358 | 🟢 august|
| 🔗 [gse](https://github.com/go-ego/gse) | - | - | ⭐ 2.8k | 🟢 last saturday|


## Language identification
Detecting which language a text is written in, with Japanese among the supported labels

 * [fastText](https://github.com/facebookresearch/fastText) - Library for fast text representation and classification.
 * [lingua-py](https://github.com/pemistahl/lingua-py) - The most accurate natural language detection library for Python, suitable for short text and mixed-language text.
 * [lingua](https://github.com/pemistahl/lingua) - The most accurate natural language detection library for Java and the JVM, suitable for long and short text alike.
 * [lingua-rs](https://github.com/pemistahl/lingua-rs) - The most accurate natural language detection library for Rust, suitable for short text and mixed-language text.
 * [lingua-go](https://github.com/pemistahl/lingua-go) - The most accurate natural language detection library for Go, suitable for short text and mixed-language text.
 * [langdetect](https://github.com/Mimino666/langdetect) - Port of Google's language-detection library to Python.
 * [GlotLID](https://github.com/cisnlp/GlotLID) - [EMNLP 2023] 💬 Language Identification with Support for More Than 2000 Labels.
 * [whatlang-rs](https://github.com/greyblake/whatlang-rs) - Natural language detection library for Rust. Try demo online: https://whatlang.org/.
 * [franc](https://github.com/wooorm/franc) - Natural language detection.
 * [whichlang](https://github.com/quickwit-oss/whichlang) - A blazingly fast and lightweight language detection library for Rust.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [fastText](https://github.com/facebookresearch/fastText) | [![Downloads](https://static.pepy.tech/badge/fasttext/week)](https://pepy.tech/project/fasttext) | [![Downloads](https://static.pepy.tech/badge/fasttext)](https://pepy.tech/project/fasttext) | ⭐ 27k | 🔴 march 2024|
| 🔗 [lingua-py](https://github.com/pemistahl/lingua-py) | [![Downloads](https://static.pepy.tech/badge/lingua-language-detector/week)](https://pepy.tech/project/lingua-language-detector) | [![Downloads](https://static.pepy.tech/badge/lingua-language-detector)](https://pepy.tech/project/lingua-language-detector) | ⭐ 1.8k | 🟡 march|
| 🔗 [lingua](https://github.com/pemistahl/lingua) | - | - | ⭐ 823 | 🔴 december 2024|
| 🔗 [lingua-rs](https://github.com/pemistahl/lingua-rs) | - | ![Crates.io](https://img.shields.io/crates/d/lingua) | ⭐ 1.1k | 🟢 september|
| 🔗 [lingua-go](https://github.com/pemistahl/lingua-go) | - | - | ⭐ 1.4k | 🔴 december 2024|
| 🔗 [langdetect](https://github.com/Mimino666/langdetect) | [![Downloads](https://static.pepy.tech/badge/langdetect/week)](https://pepy.tech/project/langdetect) | [![Downloads](https://static.pepy.tech/badge/langdetect)](https://pepy.tech/project/langdetect) | ⭐ 1.9k | 🔴 march 2025|
| 🔗 [GlotLID](https://github.com/cisnlp/GlotLID) | - | - | ⭐ 217 | 🟡 april|
| 🔗 [whatlang-rs](https://github.com/greyblake/whatlang-rs) | - | ![Crates.io](https://img.shields.io/crates/d/whatlang) | ⭐ 1.1k | 🟡 december 2025|
| 🔗 [franc](https://github.com/wooorm/franc) | ![npm](https://img.shields.io/npm/dw/franc) | ![npm](https://img.shields.io/npm/dt/franc) | ⭐ 4.4k | 🔴 march 2024|
| 🔗 [whichlang](https://github.com/quickwit-oss/whichlang) | - | ![Crates.io](https://img.shields.io/crates/d/whichlang) | ⭐ 458 | 🟡 march|


## Machine translation
Translation models, engines and services with Japanese language pairs

 * [seamless_communication](https://github.com/facebookresearch/seamless_communication) - Foundational Models for State-of-the-Art Speech and Text Translation.
 * [argos-translate](https://github.com/argosopentech/argos-translate) - Open-source offline translation library written in Python.
 * [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) - Free and Open Source Machine Translation API. Self-hosted, offline capable and easy to setup.
 * [Opus-MT](https://github.com/Helsinki-NLP/Opus-MT) - Open neural machine translation models and web services.
 * [Seed-X-7B](https://github.com/ByteDance-Seed/Seed-X-7B) - Seed-X, a powerful series of open-source multilingual translation language models, including an instruction model, a reinforcement learning model, and a reward model, within 7 billion parameters.
 * [Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2) - Hy-MT2 is a family of "fast-thinking" multilingual translation models designed for complex real-world scenarios, in three sizes: 1.8B, 7B, and 30B-A3B.
 * [Hy-MT](https://github.com/Tencent-Hunyuan/Hy-MT) - Hunyuan Translation Model Version 1.5, including a 1.8B translation model (HY-MT1.5-1.8B) and a 7B translation model (HY-MT1.5-7B).
 * [gemmax](https://github.com/xiaomi-research/gemmax) - Gemma-based Multilingual Machine Translation Models.
 * [ALMA](https://github.com/fe1ixxu/ALMA) - State-of-the-art LLM-based translation models.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [seamless_communication](https://github.com/facebookresearch/seamless_communication) | - | - | ⭐ 12k | 🟢 september|
| 🔗 [argos-translate](https://github.com/argosopentech/argos-translate) | [![Downloads](https://static.pepy.tech/badge/argostranslate/week)](https://pepy.tech/project/argostranslate) | [![Downloads](https://static.pepy.tech/badge/argostranslate)](https://pepy.tech/project/argostranslate) | ⭐ 6.5k | 🟢 august|
| 🔗 [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) | [![Downloads](https://static.pepy.tech/badge/libretranslate/week)](https://pepy.tech/project/libretranslate) | [![Downloads](https://static.pepy.tech/badge/libretranslate)](https://pepy.tech/project/libretranslate) | ⭐ 17k | 🟢 september|
| 🔗 [Opus-MT](https://github.com/Helsinki-NLP/Opus-MT) | - | - | ⭐ 861 | 🟡 february|
| 🔗 [Seed-X-7B](https://github.com/ByteDance-Seed/Seed-X-7B) | - | - | ⭐ 171 | 🔴 august 2025|
| 🔗 [Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2) | - | - | ⭐ 613 | 🟢 august|
| 🔗 [Hy-MT](https://github.com/Tencent-Hunyuan/Hy-MT) | - | - | ⭐ 823 | 🟡 june|
| 🔗 [gemmax](https://github.com/xiaomi-research/gemmax) | - | - | ⭐ 91 | 🟢 august|
| 🔗 [ALMA](https://github.com/fe1ixxu/ALMA) | - | - | ⭐ 593 | 🔴 april 2025|


## Speech recognition
Multilingual ASR models, toolkits and aligners with Japanese coverage

 * [whisper](https://github.com/openai/whisper) - Robust Speech Recognition via Large-Scale Weak Supervision.
 * [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - Port of OpenAI's Whisper model in C/C++.
 * [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - Faster Whisper transcription with CTranslate2.
 * [whisperX](https://github.com/m-bain/whisperX) - WhisperX: Automatic Speech Recognition with Word-level Timestamps (& Diarization)
 * [argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) - On-device Speech AI for Apple Silicon.
 * [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) - Qwen3-ASR is an open-source series of ASR models developed by the Qwen team at Alibaba Cloud, supporting stable multilingual speech/music/song recognition, language detection and timestamp prediction.
 * [SenseVoice](https://github.com/QwenAudio/SenseVoice) - Open-source SenseVoiceSmall model for Mandarin, Cantonese, English, Japanese, and Korean ASR, language ID, emotion recognition, and audio event detection.
 * [FunASR](https://github.com/modelscope/FunASR) - Open-source speech recognition toolkit for training, inference, streaming ASR, VAD, punctuation, speaker diarization pipelines, and OpenAI-compatible/MCP serving.
 * [omnilingual-asr](https://github.com/facebookresearch/omnilingual-asr) - Omnilingual ASR Open-Source Multilingual SpeechRecognition for 1600+ Languages.
 * [moonshine](https://github.com/moonshine-ai/moonshine) - Very low latency speech to text, intent recognition, and text to speech, for building voice agents and interfaces.
 * [Dolphin](https://github.com/DataoceanAI/Dolphin) - Dolphin is a multilingual, multitask ASR model jointly trained by DataoceanAI and Tsinghua University.
 * [NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) - A scalable generative AI framework built for researchers and developers working on Large Language Models, Multimodal, and Speech AI (Automatic Speech Recognition and Text-to-Speech)
 * [espnet](https://github.com/espnet/espnet) - End-to-End Speech Processing Toolkit.
 * [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) - Speech-to-text, text-to-speech, speaker diarization, speech enhancement, source separation, and VAD using next-gen Kaldi with onnxruntime without Internet connection. Support embedded systems, Android, iOS, HarmonyOS, Raspberry Pi, RISC-V, RK NPU, Axera NPU, Ascend NPU, x86_64 servers, websocket server/client, support 12 programming languages.
 * [icefall](https://github.com/k2-fsa/icefall) - The icefall project contains speech-related recipes for various datasets using k2-fsa and lhotse.
 * [vosk-api](https://github.com/alphacep/vosk-api) - Offline speech recognition API for Android, iOS, Raspberry Pi and servers with Python, Java, C# and Node.
 * [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) - Command line utility for forced alignment using Kaldi.
 * [Fun-ASR](https://github.com/QwenAudio/Fun-ASR) - Fun-ASR speech recognition models, with native Hugging Face Transformers support for Fun-ASR-Nano and separate FunASR, vLLM and llama.cpp deployment paths.
 * [FluidAudio](https://github.com/FluidInference/FluidAudio) - Frontier CoreML audio models in your apps — text-to-speech, speech-to-text, voice activity detection, and speaker diarization. In Swift, powered by SOTA open source.
 * [CrispASR](https://github.com/CrispStrobe/CrispASR) - C++ ggml runtime hub for multilingual ASR and TTS models: Cohere Transcribe, Parakeet TDT, Voxtral, Canary 1B v2, etc, plus universal forced alignment, and more.
 * [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) - ggml speech-to-text inference for 16+ model families.
 * [kaldi](https://github.com/kaldi-asr/kaldi) - kaldi-asr/kaldi is the official location of the Kaldi project.
 * [julius](https://github.com/julius-speech/julius) - Open-Source Large Vocabulary Continuous Speech Recognition Engine.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [whisper](https://github.com/openai/whisper) | [![Downloads](https://static.pepy.tech/badge/openai-whisper/week)](https://pepy.tech/project/openai-whisper) | [![Downloads](https://static.pepy.tech/badge/openai-whisper)](https://pepy.tech/project/openai-whisper) | ⭐ 109k | 🟢 august|
| 🔗 [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | - | - | ⭐ 54k | 🟢 last tuesday|
| 🔗 [faster-whisper](https://github.com/SYSTRAN/faster-whisper) | [![Downloads](https://static.pepy.tech/badge/faster-whisper/week)](https://pepy.tech/project/faster-whisper) | [![Downloads](https://static.pepy.tech/badge/faster-whisper)](https://pepy.tech/project/faster-whisper) | ⭐ 25k | 🟡 november 2025|
| 🔗 [whisperX](https://github.com/m-bain/whisperX) | [![Downloads](https://static.pepy.tech/badge/whisperx/week)](https://pepy.tech/project/whisperx) | [![Downloads](https://static.pepy.tech/badge/whisperx)](https://pepy.tech/project/whisperx) | ⭐ 24k | 🟢 july|
| 🔗 [argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) | - | - | ⭐ 6.4k | 🟢 august|
| 🔗 [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) | [![Downloads](https://static.pepy.tech/badge/qwen-asr/week)](https://pepy.tech/project/qwen-asr) | [![Downloads](https://static.pepy.tech/badge/qwen-asr)](https://pepy.tech/project/qwen-asr) | ⭐ 3.6k | 🟡 june|
| 🔗 [SenseVoice](https://github.com/QwenAudio/SenseVoice) | - | - | ⭐ 9.3k | 🟢 september|
| 🔗 [FunASR](https://github.com/modelscope/FunASR) | [![Downloads](https://static.pepy.tech/badge/funasr/week)](https://pepy.tech/project/funasr) | [![Downloads](https://static.pepy.tech/badge/funasr)](https://pepy.tech/project/funasr) | ⭐ 20k | 🟢 last wednesday|
| 🔗 [omnilingual-asr](https://github.com/facebookresearch/omnilingual-asr) | [![Downloads](https://static.pepy.tech/badge/omnilingual-asr/week)](https://pepy.tech/project/omnilingual-asr) | [![Downloads](https://static.pepy.tech/badge/omnilingual-asr)](https://pepy.tech/project/omnilingual-asr) | ⭐ 2.9k | 🟡 december 2025|
| 🔗 [moonshine](https://github.com/moonshine-ai/moonshine) | [![Downloads](https://static.pepy.tech/badge/moonshine-voice/week)](https://pepy.tech/project/moonshine-voice) | [![Downloads](https://static.pepy.tech/badge/moonshine-voice)](https://pepy.tech/project/moonshine-voice) | ⭐ 11k | 🟢 august|
| 🔗 [Dolphin](https://github.com/DataoceanAI/Dolphin) | [![Downloads](https://static.pepy.tech/badge/dataoceanai-dolphin/week)](https://pepy.tech/project/dataoceanai-dolphin) | [![Downloads](https://static.pepy.tech/badge/dataoceanai-dolphin)](https://pepy.tech/project/dataoceanai-dolphin) | ⭐ 789 | 🟡 may|
| 🔗 [NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) | [![Downloads](https://static.pepy.tech/badge/nemo-toolkit/week)](https://pepy.tech/project/nemo-toolkit) | [![Downloads](https://static.pepy.tech/badge/nemo-toolkit)](https://pepy.tech/project/nemo-toolkit) | ⭐ 18k | 🟢 last wednesday|
| 🔗 [espnet](https://github.com/espnet/espnet) | [![Downloads](https://static.pepy.tech/badge/espnet/week)](https://pepy.tech/project/espnet) | [![Downloads](https://static.pepy.tech/badge/espnet)](https://pepy.tech/project/espnet) | ⭐ 10k | 🟢 yesterday|
| 🔗 [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) | [![Downloads](https://static.pepy.tech/badge/sherpa-onnx/week)](https://pepy.tech/project/sherpa-onnx) | [![Downloads](https://static.pepy.tech/badge/sherpa-onnx)](https://pepy.tech/project/sherpa-onnx) | ⭐ 15k | 🟢 yesterday|
| 🔗 [icefall](https://github.com/k2-fsa/icefall) | - | - | ⭐ 1.5k | 🟢 july|
| 🔗 [vosk-api](https://github.com/alphacep/vosk-api) | [![Downloads](https://static.pepy.tech/badge/vosk/week)](https://pepy.tech/project/vosk) | [![Downloads](https://static.pepy.tech/badge/vosk)](https://pepy.tech/project/vosk) | ⭐ 15k | 🟢 august|
| 🔗 [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) | [![Downloads](https://static.pepy.tech/badge/montreal-forced-aligner/week)](https://pepy.tech/project/montreal-forced-aligner) | [![Downloads](https://static.pepy.tech/badge/montreal-forced-aligner)](https://pepy.tech/project/montreal-forced-aligner) | ⭐ 1.9k | 🟢 august|
| 🔗 [Fun-ASR](https://github.com/QwenAudio/Fun-ASR) | - | - | ⭐ 1.5k | 🟢 september|
| 🔗 [FluidAudio](https://github.com/FluidInference/FluidAudio) | - | - | ⭐ 2.8k | 🟢 last monday|
| 🔗 [CrispASR](https://github.com/CrispStrobe/CrispASR) | - | - | ⭐ 640 | 🟢 yesterday|
| 🔗 [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) | - | - | ⭐ 1.9k | 🟢 last wednesday|
| 🔗 [kaldi](https://github.com/kaldi-asr/kaldi) | - | - | ⭐ 15k | 🔴 september 2025|
| 🔗 [julius](https://github.com/julius-speech/julius) | - | - | ⭐ 1.9k | 🔴 june 2025|


## Speech synthesis
Multilingual text-to-speech and voice cloning systems that can speak Japanese

 * [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) - Qwen3-TTS is an open-source series of TTS models developed by the Qwen team at Alibaba Cloud, supporting stable, expressive, and streaming speech generation, free-form voice design, and vivid voice cloning.
 * [CosyVoice](https://github.com/QwenAudio/CosyVoice) - Multi-lingual large voice generation model, providing inference, training and deployment full-stack ability.
 * [fish-speech](https://github.com/fishaudio/fish-speech) - SOTA Open Source TTS.
 * [chatterbox](https://github.com/resemble-ai/chatterbox) - SoTA open-source TTS.
 * [coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) - 🐸💬 - a deep learning toolkit for Text-to-Speech, battle-tested in research and production.
 * [MeloTTS](https://github.com/myshell-ai/MeloTTS) - High-quality multi-lingual text-to-speech library by MyShell.ai. Support English, Spanish, French, Chinese, Japanese and Korean.
 * [OpenVoice](https://github.com/myshell-ai/OpenVoice) - Instant voice cloning by MIT and MyShell. Audio foundation model.
 * [kokoro](https://github.com/hexgrad/kokoro) - https://hf.co/hexgrad/Kokoro-82M.
 * [bark](https://github.com/suno-ai/bark) - 🔊 Text-Prompted Generative Audio Model.
 * [Zonos](https://github.com/Zyphra/Zonos) - Zonos-v0.1 is a leading open-weight text-to-speech model trained on more than 200k hours of varied multilingual speech, delivering expressiveness and quality on par with—or even surpassing—top TTS providers.
 * [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 1 min voice data can also be used to train a good TTS model! (few shot voice cloning)
 * [Amphion](https://github.com/open-mmlab/Amphion) - Amphion (/æmˈfaɪən/) is a toolkit for Audio, Music, and Speech Generation. Its purpose is to support reproducible research and help junior researchers and engineers get started in the field of audio, music, and speech generation research and development.
 * [index-tts](https://github.com/index-tts/index-tts) - An Industrial-Level Controllable and Efficient Zero-Shot Text-To-Speech System.
 * [VoxCPM](https://github.com/OpenBMB/VoxCPM) - VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning.
 * [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) - A powerful 3B-parameter, LLM-based Reinforcement Learning audio edit model excels at editing emotion, speaking style, and paralinguistics, and features robust zero-shot text-to-speech.
 * [FireRedTTS2](https://github.com/FireRedTeam/FireRedTTS2) - Long-form streaming TTS system for multi-speaker dialogue generation.
 * [OuteTTS](https://github.com/edwko/OuteTTS) - Interface for OuteTTS models.
 * [MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - An open-source model family for long-form speech, dialogue synthesis, voice design, sound effects, and real-time streaming TTS.
 * [MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) - A 100M-parameter multilingual TTS model for real-time CPU inference, voice cloning, and 48 kHz stereo generation.
 * [mlx-audio](https://github.com/Blaizzy/mlx-audio) - A text-to-speech (TTS), speech-to-text (STT) and speech-to-speech (STS) library built on Apple's MLX framework, providing efficient speech analysis on Apple Silicon.
 * [Genie-TTS](https://github.com/High-Logic/Genie-TTS) - GPT-SoVITS ONNX Inference Engine & Model Converter.
 * [MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) - A multilingual model for long-form, multi-speaker dialogue synthesis with flexible speaker control and zero-shot voice cloning.
 * [Confucius4-TTS](https://github.com/netease-youdao/Confucius4-TTS) - Confucius4-TTS: a Multilingual and Cross-Lingual Zero-Shot TTS Engine.
 * [kani-tts](https://github.com/nineninesix-ai/kani-tts) - Text-to-speech using neural audio codec and causal language models.
 * [OmniVoice](https://github.com/k2-fsa/OmniVoice) - High-Quality Voice Cloning TTS for 600+ Languages.
 * [T5Gemma-TTS](https://github.com/Aratako/T5Gemma-TTS) - Multilingual TTS model with voice cloning and duration control, based on T5Gemma encoder-decoder LLM.
 * [audio.cpp](https://github.com/0xShug0/audio.cpp) - An all-in-one, pure C++ inference engine for audio models, powered by ggml. Supports TTS, STT, VAD, voice conversion, music generation, and more, with highly optimized performance. No Python dependency.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) | [![Downloads](https://static.pepy.tech/badge/qwen-tts/week)](https://pepy.tech/project/qwen-tts) | [![Downloads](https://static.pepy.tech/badge/qwen-tts)](https://pepy.tech/project/qwen-tts) | ⭐ 13k | 🟡 march|
| 🔗 [CosyVoice](https://github.com/QwenAudio/CosyVoice) | - | - | ⭐ 24k | 🟡 may|
| 🔗 [fish-speech](https://github.com/fishaudio/fish-speech) | [![Downloads](https://static.pepy.tech/badge/fish-speech/week)](https://pepy.tech/project/fish-speech) | [![Downloads](https://static.pepy.tech/badge/fish-speech)](https://pepy.tech/project/fish-speech) | ⭐ 33k | 🟢 last wednesday|
| 🔗 [chatterbox](https://github.com/resemble-ai/chatterbox) | [![Downloads](https://static.pepy.tech/badge/chatterbox-tts/week)](https://pepy.tech/project/chatterbox-tts) | [![Downloads](https://static.pepy.tech/badge/chatterbox-tts)](https://pepy.tech/project/chatterbox-tts) | ⭐ 26k | 🟢 july|
| 🔗 [coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) | [![Downloads](https://static.pepy.tech/badge/coqui-tts/week)](https://pepy.tech/project/coqui-tts) | [![Downloads](https://static.pepy.tech/badge/coqui-tts)](https://pepy.tech/project/coqui-tts) | ⭐ 2.3k | 🟡 june|
| 🔗 [MeloTTS](https://github.com/myshell-ai/MeloTTS) | - | - | ⭐ 7.6k | 🔴 december 2024|
| 🔗 [OpenVoice](https://github.com/myshell-ai/OpenVoice) | - | - | ⭐ 38k | 🔴 april 2025|
| 🔗 [kokoro](https://github.com/hexgrad/kokoro) | [![Downloads](https://static.pepy.tech/badge/kokoro/week)](https://pepy.tech/project/kokoro) | [![Downloads](https://static.pepy.tech/badge/kokoro)](https://pepy.tech/project/kokoro) | ⭐ 8.9k | 🔴 august 2025|
| 🔗 [bark](https://github.com/suno-ai/bark) | - | - | ⭐ 39k | 🔴 april 2024|
| 🔗 [Zonos](https://github.com/Zyphra/Zonos) | - | - | ⭐ 7.2k | 🔴 march 2025|
| 🔗 [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) | - | - | ⭐ 62k | 🟢 august|
| 🔗 [Amphion](https://github.com/open-mmlab/Amphion) | - | - | ⭐ 10k | 🟡 march|
| 🔗 [index-tts](https://github.com/index-tts/index-tts) | - | - | ⭐ 24k | 🟢 august|
| 🔗 [VoxCPM](https://github.com/OpenBMB/VoxCPM) | [![Downloads](https://static.pepy.tech/badge/voxcpm/week)](https://pepy.tech/project/voxcpm) | [![Downloads](https://static.pepy.tech/badge/voxcpm)](https://pepy.tech/project/voxcpm) | ⭐ 38k | 🟢 september|
| 🔗 [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) | - | - | ⭐ 977 | 🟡 april|
| 🔗 [FireRedTTS2](https://github.com/FireRedTeam/FireRedTTS2) | - | - | ⭐ 1.4k | 🟡 october 2025|
| 🔗 [OuteTTS](https://github.com/edwko/OuteTTS) | [![Downloads](https://static.pepy.tech/badge/outetts/week)](https://pepy.tech/project/outetts) | [![Downloads](https://static.pepy.tech/badge/outetts)](https://pepy.tech/project/outetts) | ⭐ 1.4k | 🟡 march|
| 🔗 [MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) | - | - | ⭐ 4.1k | 🟢 september|
| 🔗 [MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) | - | - | ⭐ 4.4k | 🟢 september|
| 🔗 [mlx-audio](https://github.com/Blaizzy/mlx-audio) | [![Downloads](https://static.pepy.tech/badge/mlx-audio/week)](https://pepy.tech/project/mlx-audio) | [![Downloads](https://static.pepy.tech/badge/mlx-audio)](https://pepy.tech/project/mlx-audio) | ⭐ 7.9k | 🟢 last tuesday|
| 🔗 [Genie-TTS](https://github.com/High-Logic/Genie-TTS) | [![Downloads](https://static.pepy.tech/badge/genie-tts/week)](https://pepy.tech/project/genie-tts) | [![Downloads](https://static.pepy.tech/badge/genie-tts)](https://pepy.tech/project/genie-tts) | ⭐ 1.8k | 🟢 august|
| 🔗 [MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) | - | - | ⭐ 1.4k | 🟢 september|
| 🔗 [Confucius4-TTS](https://github.com/netease-youdao/Confucius4-TTS) | - | - | ⭐ 796 | 🟢 september|
| 🔗 [kani-tts](https://github.com/nineninesix-ai/kani-tts) | [![Downloads](https://static.pepy.tech/badge/kani-tts/week)](https://pepy.tech/project/kani-tts) | [![Downloads](https://static.pepy.tech/badge/kani-tts)](https://pepy.tech/project/kani-tts) | ⭐ 459 | 🟡 november 2025|
| 🔗 [OmniVoice](https://github.com/k2-fsa/OmniVoice) | [![Downloads](https://static.pepy.tech/badge/omnivoice/week)](https://pepy.tech/project/omnivoice) | [![Downloads](https://static.pepy.tech/badge/omnivoice)](https://pepy.tech/project/omnivoice) | ⭐ 13k | 🟢 august|
| 🔗 [T5Gemma-TTS](https://github.com/Aratako/T5Gemma-TTS) | - | - | ⭐ 312 | 🟡 april|
| 🔗 [audio.cpp](https://github.com/0xShug0/audio.cpp) | - | - | ⭐ 2.8k | 🟢 yesterday|


## OCR and document AI
Text recognition and document parsing that handles Japanese scripts

 * [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - Turn any PDF or image document into structured data for your AI. A powerful, lightweight OCR toolkit that bridges the gap between images/PDFs and LLMs. Supports 100+ languages.
 * [tesseract](https://github.com/tesseract-ocr/tesseract) - Tesseract Open Source OCR Engine (main repository)
 * [EasyOCR](https://github.com/JaidedAI/EasyOCR) - Ready-to-use OCR with 80+ supported languages and all popular writing scripts including Latin, Chinese, Arabic, Devanagari, Cyrillic and etc.
 * [surya](https://github.com/datalab-to/surya) - OCR, layout analysis, reading order, table recognition in 90+ languages.
 * [chandra](https://github.com/datalab-to/chandra) - OCR model that handles complex tables, forms, handwriting with full layout.
 * [MinerU](https://github.com/opendatalab/MinerU) - Transforms complex documents like PDFs and Office docs into LLM-ready markdown/JSON for your Agentic workflows.
 * [RapidOCR](https://github.com/RapidAI/RapidOCR) - 📄 Awesome OCR multiple programing languages toolkits based on ONNX Runtime, OpenVINO, MNN, PaddlePaddle, TensorRT and PyTorch.
 * [Pix2Text](https://github.com/breezedeus/Pix2Text) - An Open-Source Python3 tool with SMALL models for recognizing layouts, tables, math formulas (LaTeX), and text in images, converting them into Markdown format. A free alternative to Mathpix, empowering seamless conversion of visual content into text-based representations. 80+ languages are supported.
 * [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) - PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.
 * [TurboOCR](https://github.com/aiptimizer/TurboOCR) - TurboOCR, >200 img/s OmnidocBench. TensorRT FP16, PP-OCRv6, HTTP + gRPC.
 * [tesseract.js](https://github.com/naptha/tesseract.js) - Pure Javascript OCR for more than 100 Languages 📖🎉🖥.
 * [pdfminer.six](https://github.com/pdfminer/pdfminer.six) - Community maintained fork of pdfminer - we fathom PDF.
 * [PyMuPDF](https://github.com/pymupdf/PyMuPDF) - PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) | [![Downloads](https://static.pepy.tech/badge/paddleocr/week)](https://pepy.tech/project/paddleocr) | [![Downloads](https://static.pepy.tech/badge/paddleocr)](https://pepy.tech/project/paddleocr) | ⭐ 90k | 🟢 last wednesday|
| 🔗 [tesseract](https://github.com/tesseract-ocr/tesseract) | - | - | ⭐ 77k | 🟢 september|
| 🔗 [EasyOCR](https://github.com/JaidedAI/EasyOCR) | [![Downloads](https://static.pepy.tech/badge/easyocr/week)](https://pepy.tech/project/easyocr) | [![Downloads](https://static.pepy.tech/badge/easyocr)](https://pepy.tech/project/easyocr) | ⭐ 30k | 🟡 december 2025|
| 🔗 [surya](https://github.com/datalab-to/surya) | [![Downloads](https://static.pepy.tech/badge/surya-ocr/week)](https://pepy.tech/project/surya-ocr) | [![Downloads](https://static.pepy.tech/badge/surya-ocr)](https://pepy.tech/project/surya-ocr) | ⭐ 21k | 🟢 september|
| 🔗 [chandra](https://github.com/datalab-to/chandra) | [![Downloads](https://static.pepy.tech/badge/chandra-ocr/week)](https://pepy.tech/project/chandra-ocr) | [![Downloads](https://static.pepy.tech/badge/chandra-ocr)](https://pepy.tech/project/chandra-ocr) | ⭐ 12k | 🟡 june|
| 🔗 [MinerU](https://github.com/opendatalab/MinerU) | [![Downloads](https://static.pepy.tech/badge/mineru/week)](https://pepy.tech/project/mineru) | [![Downloads](https://static.pepy.tech/badge/mineru)](https://pepy.tech/project/mineru) | ⭐ 80k | 🟢 yesterday|
| 🔗 [RapidOCR](https://github.com/RapidAI/RapidOCR) | [![Downloads](https://static.pepy.tech/badge/rapidocr/week)](https://pepy.tech/project/rapidocr) | [![Downloads](https://static.pepy.tech/badge/rapidocr)](https://pepy.tech/project/rapidocr) | ⭐ 7.9k | 🟢 last tuesday|
| 🔗 [Pix2Text](https://github.com/breezedeus/Pix2Text) | [![Downloads](https://static.pepy.tech/badge/pix2text/week)](https://pepy.tech/project/pix2text) | [![Downloads](https://static.pepy.tech/badge/pix2text)](https://pepy.tech/project/pix2text) | ⭐ 3.2k | 🟢 august|
| 🔗 [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) | [![Downloads](https://static.pepy.tech/badge/opendataloader-pdf/week)](https://pepy.tech/project/opendataloader-pdf) | [![Downloads](https://static.pepy.tech/badge/opendataloader-pdf)](https://pepy.tech/project/opendataloader-pdf) | ⭐ 29k | 🟢 yesterday|
| 🔗 [TurboOCR](https://github.com/aiptimizer/TurboOCR) | - | - | ⭐ 1.1k | 🟢 september|
| 🔗 [tesseract.js](https://github.com/naptha/tesseract.js) | ![npm](https://img.shields.io/npm/dw/tesseract.js) | ![npm](https://img.shields.io/npm/dt/tesseract.js) | ⭐ 39k | 🟡 may|
| 🔗 [pdfminer.six](https://github.com/pdfminer/pdfminer.six) | [![Downloads](https://static.pepy.tech/badge/pdfminer.six/week)](https://pepy.tech/project/pdfminer.six) | [![Downloads](https://static.pepy.tech/badge/pdfminer.six)](https://pepy.tech/project/pdfminer.six) | ⭐ 7k | 🟡 march|
| 🔗 [PyMuPDF](https://github.com/pymupdf/PyMuPDF) | [![Downloads](https://static.pepy.tech/badge/pymupdf/week)](https://pepy.tech/project/pymupdf) | [![Downloads](https://static.pepy.tech/badge/pymupdf)](https://pepy.tech/project/pymupdf) | ⭐ 11k | 🟢 last wednesday|


## Embeddings and retrieval
Embedding libraries with Japanese-capable models, pretrained Japanese embeddings and retrieval toolkits with Japanese indexes

 * [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) - A tool for learning vector representations of words and entities from Wikipedia.
 * [pyserini](https://github.com/castorini/pyserini) - Pyserini is a Python toolkit for reproducible information retrieval research with sparse and dense representations.
 * [sentence-transformers](https://github.com/huggingface/sentence-transformers) - State-of-the-Art Embeddings, Retrieval, and Reranking.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec/week)](https://pepy.tech/project/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec)](https://pepy.tech/project/wikipedia2vec) | ⭐ 972 | 🔴 january 2024|
| 🔗 [pyserini](https://github.com/castorini/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini/week)](https://pepy.tech/project/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini)](https://pepy.tech/project/pyserini) | ⭐ 2.2k | 🟢 last wednesday|
| 🔗 [sentence-transformers](https://github.com/huggingface/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers/week)](https://pepy.tech/project/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers)](https://pepy.tech/project/sentence-transformers) | ⭐ 19k | 🟢 last wednesday|


## Full-text search
Search engines and databases with built-in Japanese analyzers or tokenizers

 * [lucene](https://github.com/apache/lucene) - Apache Lucene open-source search software.
 * [elasticsearch](https://github.com/elastic/elasticsearch) - Free and Open Source, Distributed, RESTful Search Engine.
 * [OpenSearch](https://github.com/opensearch-project/OpenSearch) - 🔎 Open source distributed and RESTful search engine.
 * [solr](https://github.com/apache/solr) - Apache Solr open-source search software.
 * [meilisearch](https://github.com/meilisearch/meilisearch) - A lightning-fast search engine API bringing AI-powered hybrid search to your sites and applications.
 * [typesense](https://github.com/typesense/typesense) - Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to ElasticSearch ⚡ 🔍 ✨ Fast, typo tolerant, in-memory fuzzy Search Engine for building delightful search experiences.
 * [groonga](https://github.com/groonga/groonga) - An embeddable fulltext search engine. Groonga is the successor project to Senna.
 * [pgroonga](https://github.com/pgroonga/pgroonga) - PGroonga is a PostgreSQL extension to use Groonga as index. PGroonga makes PostgreSQL fast full text search platform for all languages!
 * [mroonga](https://github.com/mroonga/mroonga) - A MySQL pluggable storage engine based on Groonga.
 * [pg_bigm](https://github.com/pgbigm/pg_bigm) - The pg_bigm module provides full text search capability in PostgreSQL. This module allows a user to create 2-gram (bigram) index for faster full text search.
 * [paradedb](https://github.com/paradedb/paradedb) - One Postgres for your application data, full-text search, vector retrieval, and aggregations. Home of the pg_search extension.
 * [weaviate](https://github.com/weaviate/weaviate) - Weaviate is an open-source vector database that stores both objects and vectors, allowing for the combination of vector search with structured filtering with the fault tolerance and scalability of a cloud-native database.
 * [milvus](https://github.com/milvus-io/milvus) - Milvus is a high-performance, cloud-native vector database built for scalable vector ANN search.
 * [qdrant](https://github.com/qdrant/qdrant) - Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/.
 * [flexsearch](https://github.com/nextapps-de/flexsearch) - Next-generation full-text search library for Browser and Node.js.
 * [sonic](https://github.com/valeriansaliou/sonic) - 🦔 Fast, lightweight & schema-less search backend. An alternative to Elasticsearch that runs on a few MBs of RAM.
 * [orama](https://github.com/oramasearch/orama) - 🌌 A complete search engine and RAG pipeline in your browser, server or edge network with support for full-text, vector, and hybrid search in less than 2kb.
 * [pagefind](https://github.com/Pagefind/pagefind) - Static low-bandwidth search at scale.
 * [lancedb](https://github.com/lancedb/lancedb) - Developer-friendly OSS embedded retrieval library for multimodal AI. Search More; Manage Less.
 * [bleve](https://github.com/blevesearch/bleve) - A modern text/numeric/geo-spatial/vector indexing library for go.
 * [lunr-languages](https://github.com/MihaiValentin/lunr-languages) - A collection of languages stemmers and stopwords for Lunr Javascript library.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lucene](https://github.com/apache/lucene) | - | - | ⭐ 3.6k | 🟢 last wednesday|
| 🔗 [elasticsearch](https://github.com/elastic/elasticsearch) | - | - | ⭐ 78k | 🟢 yesterday|
| 🔗 [OpenSearch](https://github.com/opensearch-project/OpenSearch) | - | - | ⭐ 14k | 🟢 yesterday|
| 🔗 [solr](https://github.com/apache/solr) | - | - | ⭐ 1.7k | 🟢 yesterday|
| 🔗 [meilisearch](https://github.com/meilisearch/meilisearch) | - | - | ⭐ 59k | 🟢 yesterday|
| 🔗 [typesense](https://github.com/typesense/typesense) | - | - | ⭐ 27k | 🟢 last wednesday|
| 🔗 [groonga](https://github.com/groonga/groonga) | - | - | ⭐ 858 | 🟢 yesterday|
| 🔗 [pgroonga](https://github.com/pgroonga/pgroonga) | - | - | ⭐ 749 | 🟢 last tuesday|
| 🔗 [mroonga](https://github.com/mroonga/mroonga) | - | - | ⭐ 191 | 🟢 september|
| 🔗 [pg_bigm](https://github.com/pgbigm/pg_bigm) | - | - | ⭐ 156 | 🟢 august|
| 🔗 [paradedb](https://github.com/paradedb/paradedb) | - | - | ⭐ 9.3k | 🟢 yesterday|
| 🔗 [weaviate](https://github.com/weaviate/weaviate) | - | - | ⭐ 17k | 🟢 yesterday|
| 🔗 [milvus](https://github.com/milvus-io/milvus) | - | - | ⭐ 46k | 🟢 yesterday|
| 🔗 [qdrant](https://github.com/qdrant/qdrant) | - | - | ⭐ 35k | 🟢 september|
| 🔗 [flexsearch](https://github.com/nextapps-de/flexsearch) | ![npm](https://img.shields.io/npm/dw/flexsearch) | ![npm](https://img.shields.io/npm/dt/flexsearch) | ⭐ 14k | 🟡 may|
| 🔗 [sonic](https://github.com/valeriansaliou/sonic) | - | ![Crates.io](https://img.shields.io/crates/d/sonic-server) | ⭐ 21k | 🟢 last tuesday|
| 🔗 [orama](https://github.com/oramasearch/orama) | ![npm](https://img.shields.io/npm/dw/@orama/orama) | ![npm](https://img.shields.io/npm/dt/@orama/orama) | ⭐ 11k | 🟢 july|
| 🔗 [pagefind](https://github.com/Pagefind/pagefind) | ![npm](https://img.shields.io/npm/dw/pagefind) | ![npm](https://img.shields.io/npm/dt/pagefind) | ⭐ 5.5k | 🟢 last wednesday|
| 🔗 [lancedb](https://github.com/lancedb/lancedb) | [![Downloads](https://static.pepy.tech/badge/lancedb/week)](https://pepy.tech/project/lancedb) | [![Downloads](https://static.pepy.tech/badge/lancedb)](https://pepy.tech/project/lancedb) | ⭐ 11k | 🟢 yesterday|
| 🔗 [bleve](https://github.com/blevesearch/bleve) | - | - | ⭐ 11k | 🟢 august|
| 🔗 [lunr-languages](https://github.com/MihaiValentin/lunr-languages) | ![npm](https://img.shields.io/npm/dw/lunr-languages) | ![npm](https://img.shields.io/npm/dt/lunr-languages) | ⭐ 458 | 🟢 last tuesday|


## Text normalization and phonetics
Normalization, romanization and grapheme-to-phoneme tools with Japanese rules or data

 * [NeMo-text-processing](https://github.com/NVIDIA/NeMo-text-processing) - NeMo text processing for ASR and TTS.
 * [WeTextProcessing](https://github.com/wenet-e2e/WeTextProcessing) - Text Normalization & Inverse Text Normalization.
 * [misaki](https://github.com/hexgrad/misaki) - G2P.
 * [espeak-ng](https://github.com/espeak-ng/espeak-ng) - eSpeak NG is an open source speech synthesizer that supports more than hundred languages and accents.
 * [epitran](https://github.com/dmort27/epitran) - A tool for transcribing orthographic text as IPA (International Phonetic Alphabet)
 * [uroman](https://github.com/isi-nlp/uroman) - Universal Romanizer that can convert any unicode script to roman (latin) script.
 * [num2words](https://github.com/savoirfairelinux/num2words) - Modules to convert numbers to words. 42 --> forty-two.
 * [dateparser](https://github.com/scrapinghub/dateparser) - python parser for human readable dates.
 * [ipa-dict](https://github.com/open-dict-data/ipa-dict) - Monolingual wordlists with pronunciation information in IPA.
 * [Recognizers-Text](https://github.com/microsoft/Recognizers-Text) - Microsoft.Recognizers.Text provides recognition and resolution of numbers, units, date/time, etc. in multiple languages (ZH, EN, FR, ES, PT, DE, IT, TR, HI, NL. Partial support for JA, KO, AR, SV). Packages available at: https://www.nuget.org/profiles/Recognizers.Text, https://www.npmjs.com/~recognizers.text.
 * [chrono](https://github.com/wanasit/chrono) - A natural language date parser in Javascript.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [NeMo-text-processing](https://github.com/NVIDIA/NeMo-text-processing) | [![Downloads](https://static.pepy.tech/badge/nemo-text-processing/week)](https://pepy.tech/project/nemo-text-processing) | [![Downloads](https://static.pepy.tech/badge/nemo-text-processing)](https://pepy.tech/project/nemo-text-processing) | ⭐ 505 | 🟢 july|
| 🔗 [WeTextProcessing](https://github.com/wenet-e2e/WeTextProcessing) | [![Downloads](https://static.pepy.tech/badge/wetextprocessing/week)](https://pepy.tech/project/wetextprocessing) | [![Downloads](https://static.pepy.tech/badge/wetextprocessing)](https://pepy.tech/project/wetextprocessing) | ⭐ 825 | 🟢 july|
| 🔗 [misaki](https://github.com/hexgrad/misaki) | [![Downloads](https://static.pepy.tech/badge/misaki/week)](https://pepy.tech/project/misaki) | [![Downloads](https://static.pepy.tech/badge/misaki)](https://pepy.tech/project/misaki) | ⭐ 507 | 🔴 august 2025|
| 🔗 [espeak-ng](https://github.com/espeak-ng/espeak-ng) | - | - | ⭐ 6.8k | 🟢 september|
| 🔗 [epitran](https://github.com/dmort27/epitran) | [![Downloads](https://static.pepy.tech/badge/epitran/week)](https://pepy.tech/project/epitran) | [![Downloads](https://static.pepy.tech/badge/epitran)](https://pepy.tech/project/epitran) | ⭐ 838 | 🟡 june|
| 🔗 [uroman](https://github.com/isi-nlp/uroman) | [![Downloads](https://static.pepy.tech/badge/uroman/week)](https://pepy.tech/project/uroman) | [![Downloads](https://static.pepy.tech/badge/uroman)](https://pepy.tech/project/uroman) | ⭐ 252 | 🔴 july 2024|
| 🔗 [num2words](https://github.com/savoirfairelinux/num2words) | [![Downloads](https://static.pepy.tech/badge/num2words/week)](https://pepy.tech/project/num2words) | [![Downloads](https://static.pepy.tech/badge/num2words)](https://pepy.tech/project/num2words) | ⭐ 967 | 🔴 may 2025|
| 🔗 [dateparser](https://github.com/scrapinghub/dateparser) | [![Downloads](https://static.pepy.tech/badge/dateparser/week)](https://pepy.tech/project/dateparser) | [![Downloads](https://static.pepy.tech/badge/dateparser)](https://pepy.tech/project/dateparser) | ⭐ 2.9k | 🟢 last wednesday|
| 🔗 [ipa-dict](https://github.com/open-dict-data/ipa-dict) | - | - | ⭐ 799 | 🔴 may 2025|
| 🔗 [Recognizers-Text](https://github.com/microsoft/Recognizers-Text) | [![Downloads](https://static.pepy.tech/badge/recognizers-text-suite/week)](https://pepy.tech/project/recognizers-text-suite) | [![Downloads](https://static.pepy.tech/badge/recognizers-text-suite)](https://pepy.tech/project/recognizers-text-suite) | ⭐ 1.8k | 🟡 january|
| 🔗 [chrono](https://github.com/wanasit/chrono) | ![npm](https://img.shields.io/npm/dw/chrono-node) | ![npm](https://img.shields.io/npm/dt/chrono-node) | ⭐ 5.3k | 🟢 september|


## Evaluation and datasets
Evaluation tools with Japanese settings and multilingual datasets that include Japanese

 * [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) - A framework for few-shot evaluation of language models.
 * [mteb](https://github.com/embeddings-benchmark/mteb) - MTEB: State-of-the-art evaluation of embeddings across languages and modalities.
 * [sacrebleu](https://github.com/mjpost/sacrebleu) - Reference BLEU implementation that auto-downloads test sets and reports a version string to facilitate cross-lab comparisons.
 * [xtreme](https://github.com/google-research/xtreme) - XTREME is a benchmark for the evaluation of the cross-lingual generalization ability of pre-trained multilingual models that covers 40 typologically diverse languages and includes nine tasks.
 * [belebele](https://github.com/facebookresearch/belebele) - Repo for the Belebele dataset, a massively multilingual reading comprehension dataset.
 * [miracl](https://github.com/project-miracl/miracl) - A large-scale multilingual dataset for Information Retrieval. Thorough human-annotations across 18 diverse languages.
 * [mr.tydi](https://github.com/castorini/mr.tydi) - Mr. TyDi is a multi-lingual benchmark dataset built on TyDi, covering eleven typologically diverse languages.
 * [tydiqa](https://github.com/google-research-datasets/tydiqa) - TyDi QA contains 200k human-annotated question-answer pairs in 11 Typologically Diverse languages, written without seeing the answer and without the use of translation, and is designed for the training and evaluation of automatic question answering systems. This repository provides evaluation code and a baseline system for the dataset.
 * [ml-mkqa](https://github.com/apple-aiml-research/ml-mkqa) - We introduce MKQA, an open-domain question answering evaluation set comprising 10k question-answer pairs aligned across 26 typologically diverse languages (260k question-answer pairs in total). The goal of this dataset is to provide a challenging benchmark for question answering quality across a wide set of languages. Please refer to our paper for details, MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering.
 * [massive](https://github.com/alexa/massive) - Tools and Modeling Code for the MASSIVE dataset.
 * [paws](https://github.com/google-research-datasets/paws) - This dataset contains 108,463 human-labeled and 656k noisily labeled pairs that feature the importance of modeling structure, context, and word order information for the problem of paraphrase identification.
 * [xl-sum](https://github.com/csebuetnlp/xl-sum) - This repository contains the code, data, and models of the paper titled "XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages" published in Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021.
 * [url-nlp (MGSM)](https://github.com/google-research/url-nlp) - MGSM is a benchmark of grade-school math problems, proposed in the paper Language models are multilingual chain-of-thought reasoners.
 * [M-IFEval](https://github.com/lightblue-tech/M-IFEval) - This repository contains source code and data for M-IFEval: Multilingual Instruction-Following Evaluation.
 * [mintaka](https://github.com/amazon-science/mintaka) - Dataset from the paper "Mintaka: A Complex, Natural, and Multilingual Dataset for End-to-End Question Answering" (COLING 2022)
 * [Wikilingua](https://github.com/esdurmus/Wikilingua) - Multilingual abstractive summarization dataset extracted from WikiHow.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | [![Downloads](https://static.pepy.tech/badge/lm-eval/week)](https://pepy.tech/project/lm-eval) | [![Downloads](https://static.pepy.tech/badge/lm-eval)](https://pepy.tech/project/lm-eval) | ⭐ 14k | 🟢 last monday|
| 🔗 [mteb](https://github.com/embeddings-benchmark/mteb) | [![Downloads](https://static.pepy.tech/badge/mteb/week)](https://pepy.tech/project/mteb) | [![Downloads](https://static.pepy.tech/badge/mteb)](https://pepy.tech/project/mteb) | ⭐ 3.4k | 🟢 last wednesday|
| 🔗 [sacrebleu](https://github.com/mjpost/sacrebleu) | [![Downloads](https://static.pepy.tech/badge/sacrebleu/week)](https://pepy.tech/project/sacrebleu) | [![Downloads](https://static.pepy.tech/badge/sacrebleu)](https://pepy.tech/project/sacrebleu) | ⭐ 1.3k | 🟢 august|
| 🔗 [xtreme](https://github.com/google-research/xtreme) | - | - | ⭐ 651 | 🔴 january 2023|
| 🔗 [belebele](https://github.com/facebookresearch/belebele) | - | - | ⭐ 338 | 🔴 december 2024|
| 🔗 [miracl](https://github.com/project-miracl/miracl) | - | - | ⭐ 213 | 🔴 july 2024|
| 🔗 [mr.tydi](https://github.com/castorini/mr.tydi) | - | - | ⭐ 83 | 🔴 february 2022|
| 🔗 [tydiqa](https://github.com/google-research-datasets/tydiqa) | - | - | ⭐ 319 | 🔴 april 2020|
| 🔗 [ml-mkqa](https://github.com/apple-aiml-research/ml-mkqa) | - | - | ⭐ 196 | 🟢 september|
| 🔗 [massive](https://github.com/alexa/massive) | - | - | ⭐ 569 | 🔴 november 2022|
| 🔗 [paws](https://github.com/google-research-datasets/paws) | - | - | ⭐ 572 | 🔴 january 2022|
| 🔗 [xl-sum](https://github.com/csebuetnlp/xl-sum) | - | - | ⭐ 278 | 🔴 march 2024|
| 🔗 [url-nlp (MGSM)](https://github.com/google-research/url-nlp) | - | - | ⭐ 278 | 🔴 august 2025|
| 🔗 [M-IFEval](https://github.com/lightblue-tech/M-IFEval) | - | - | ⭐ 12 | 🔴 july 2025|
| 🔗 [mintaka](https://github.com/amazon-science/mintaka) | - | - | ⭐ 119 | 🔴 october 2022|
| 🔗 [Wikilingua](https://github.com/esdurmus/Wikilingua) | - | - | ⭐ 99 | 🔴 march 2025|


## Text processing utilities
Corpus processing, word frequency and lexical database tools with Japanese-specific handling

 * [datatrove](https://github.com/huggingface/datatrove) - Freeing data processing from scripting madness by providing a set of platform-agnostic customizable pipeline processing blocks.
 * [Wordless](https://github.com/BLKSerene/Wordless) - An Integrated Corpus Tool With Multilingual Support for the Study of Language, Literature, and Translation.
 * [wordfreq](https://github.com/rspeer/wordfreq) - Access a database of word frequencies, in various natural languages.
 * [wn](https://github.com/goodmami/wn) - A modern, interlingual wordnet interface for Python.
 * [wiktextract](https://github.com/tatuylonen/wiktextract) - Wiktionary dump file parser and multilingual data extractor.
 * [scattertext](https://github.com/JasonKessler/scattertext) - Beautiful visualizations of how language differs among document types.
 * [sumy](https://github.com/miso-belica/sumy) - Module for automatic summarization of text documents and HTML pages.
 * [textlint](https://github.com/textlint/textlint) - textlint is the pluggable linter for natural language text.


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [datatrove](https://github.com/huggingface/datatrove) | [![Downloads](https://static.pepy.tech/badge/datatrove/week)](https://pepy.tech/project/datatrove) | [![Downloads](https://static.pepy.tech/badge/datatrove)](https://pepy.tech/project/datatrove) | ⭐ 3.3k | 🟢 yesterday|
| 🔗 [Wordless](https://github.com/BLKSerene/Wordless) | - | - | ⭐ 758 | 🟡 october 2025|
| 🔗 [wordfreq](https://github.com/rspeer/wordfreq) | [![Downloads](https://static.pepy.tech/badge/wordfreq/week)](https://pepy.tech/project/wordfreq) | [![Downloads](https://static.pepy.tech/badge/wordfreq)](https://pepy.tech/project/wordfreq) | ⭐ 1.7k | 🔴 january 2025|
| 🔗 [wn](https://github.com/goodmami/wn) | [![Downloads](https://static.pepy.tech/badge/wn/week)](https://pepy.tech/project/wn) | [![Downloads](https://static.pepy.tech/badge/wn)](https://pepy.tech/project/wn) | ⭐ 301 | 🟢 september|
| 🔗 [wiktextract](https://github.com/tatuylonen/wiktextract) | [![Downloads](https://static.pepy.tech/badge/wiktextract/week)](https://pepy.tech/project/wiktextract) | [![Downloads](https://static.pepy.tech/badge/wiktextract)](https://pepy.tech/project/wiktextract) | ⭐ 1.3k | 🟢 last monday|
| 🔗 [scattertext](https://github.com/JasonKessler/scattertext) | [![Downloads](https://static.pepy.tech/badge/scattertext/week)](https://pepy.tech/project/scattertext) | [![Downloads](https://static.pepy.tech/badge/scattertext)](https://pepy.tech/project/scattertext) | ⭐ 2.3k | 🟢 july|
| 🔗 [sumy](https://github.com/miso-belica/sumy) | [![Downloads](https://static.pepy.tech/badge/sumy/week)](https://pepy.tech/project/sumy) | [![Downloads](https://static.pepy.tech/badge/sumy)](https://pepy.tech/project/sumy) | ⭐ 3.7k | 🟢 september|
| 🔗 [textlint](https://github.com/textlint/textlint) | ![npm](https://img.shields.io/npm/dw/textlint) | ![npm](https://img.shields.io/npm/dt/textlint) | ⭐ 3.2k | 🟢 yesterday|

