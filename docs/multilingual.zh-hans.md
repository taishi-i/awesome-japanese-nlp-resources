# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

并非专为日语打造、但同样支持日语的多语言库、模型与数据集精选列表。
本页面收录具备日语具体功能的多语言库、模型与数据集，例如日语语种识别、日语分词器与分析器、日语语音与 OCR 模型，以及数据集中的日语部分。目前共收录155个仓库。

_更新于2026年9月18日_

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
内置日语模型或分词器的通用多语言NLP框架

 * [spaCy](https://github.com/explosion/spaCy) - 💫 Python 实现的工业级自然语言处理（NLP）。
 * [stanza](https://github.com/stanfordnlp/stanza) - 用于分词、分句、命名实体识别以及多种人类语言句法分析的 Stanford NLP Python 库。
 * [HanLP](https://github.com/hankcs/HanLP) - 面向下一个十年的自然语言处理。分词、词性标注、命名实体识别、句法与语义依存分析、文档分类。
 * [trankit](https://github.com/nlp-uoregon/trankit) - Trankit 是一个基于 Transformer 的轻量级多语言自然语言处理 Python 工具包。
 * [udpipe](https://github.com/ufal/udpipe) - UDPipe：用于对 Universal Treebanks 及其他 CoNLL-U 文件进行分词、标注、词形还原和句法分析的可训练流水线。
 * [spark-nlp](https://github.com/JohnSnowLabs/spark-nlp) - 最先进的自然语言处理。
 * [openmed](https://github.com/maziyarpanahi/openmed) - 本地优先的医疗 AI：完全在设备端运行的临床命名实体识别与符合 HIPAA 的个人信息去标识化。拥有2200多个医疗模型，支持21种语言，兼容 Apple MLX + Python，无需云端，患者数据不会离开您的网络。Apache-2.0 许可。
 * [transformers](https://github.com/huggingface/transformers) - 🤗 Transformers：面向文本、视觉、音频及多模态领域最先进机器学习模型的模型定义框架，同时支持推理与训练。
 * [nltk](https://github.com/nltk/nltk) - NLTK 源代码。


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
适用于日语文本的子词、单词及句子边界切分工具

 * [sentencepiece](https://github.com/google/sentencepiece) - 面向基于神经网络的文本生成的无监督文本分词器。
 * [icu](https://github.com/unicode-org/icu) - ICU 项目源代码的所在地。
 * [wtpsplit](https://github.com/segment-any-text/wtpsplit) - 以稳健、高效且可适配的方式将文本切分为句子或其他语义单元的工具包。
 * [charabia](https://github.com/meilisearch/charabia) - Meilisearch 用于对查询和文档进行分词的库。
 * [gse](https://github.com/go-ego/gse) - 高效的 Go 语言多语言 NLP 与文本切分库，支持英语、中文、日语等。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [sentencepiece](https://github.com/google/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece/week)](https://pepy.tech/project/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece)](https://pepy.tech/project/sentencepiece) | ⭐ 12k | 🟢 last wednesday|
| 🔗 [icu](https://github.com/unicode-org/icu) | - | - | ⭐ 3.6k | 🟢 yesterday|
| 🔗 [wtpsplit](https://github.com/segment-any-text/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit/week)](https://pepy.tech/project/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit)](https://pepy.tech/project/wtpsplit) | ⭐ 1.3k | 🟡 april|
| 🔗 [charabia](https://github.com/meilisearch/charabia) | - | ![Crates.io](https://img.shields.io/crates/d/charabia) | ⭐ 358 | 🟢 august|
| 🔗 [gse](https://github.com/go-ego/gse) | - | - | ⭐ 2.8k | 🟢 last saturday|


## Language identification
判定文本语言的库（支持的标签包含日语）

 * [fastText](https://github.com/facebookresearch/fastText) - 用于快速文本表示与分类的库。
 * [lingua-py](https://github.com/pemistahl/lingua-py) - 面向 Python 的最精准自然语言检测库，适用于短文本和多语言混合文本。
 * [lingua](https://github.com/pemistahl/lingua) - 面向 Java 和 JVM 的最精准自然语言检测库，同样适用于长文本和短文本。
 * [lingua-rs](https://github.com/pemistahl/lingua-rs) - 面向 Rust 的最精准自然语言检测库，适用于短文本和多语言混合文本。
 * [lingua-go](https://github.com/pemistahl/lingua-go) - 面向 Go 的最精准自然语言检测库，适用于短文本和多语言混合文本。
 * [langdetect](https://github.com/Mimino666/langdetect) - Google language-detection 库的 Python 移植版。
 * [GlotLID](https://github.com/cisnlp/GlotLID) - [EMNLP 2023] 💬 支持2000多个标签的语言识别。
 * [whatlang-rs](https://github.com/greyblake/whatlang-rs) - 面向 Rust 的自然语言检测库。在线演示：https://whatlang.org/。
 * [franc](https://github.com/wooorm/franc) - 自然语言检测。
 * [whichlang](https://github.com/quickwit-oss/whichlang) - 面向 Rust 的极速轻量语言检测库。


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
支持含日语语言对的翻译模型、引擎与服务

 * [seamless_communication](https://github.com/facebookresearch/seamless_communication) - 面向最先进语音与文本翻译的基础模型。
 * [argos-translate](https://github.com/argosopentech/argos-translate) - 使用 Python 编写的开源离线翻译库。
 * [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) - 免费开源的机器翻译 API，可自托管、支持离线，且易于搭建。
 * [Opus-MT](https://github.com/Helsinki-NLP/Opus-MT) - 开放的神经网络机器翻译模型与网络服务。
 * [Seed-X-7B](https://github.com/ByteDance-Seed/Seed-X-7B) - Seed-X 是一个强大的开源多语言翻译语言模型系列，参数量为70亿，包含指令模型、强化学习模型和奖励模型。
 * [Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2) - Hy-MT2 是一系列面向复杂真实场景设计的“快思考”多语言翻译模型，提供 1.8B、7B、30B-A3B 三种规模。
 * [Hy-MT](https://github.com/Tencent-Hunyuan/Hy-MT) - 混元翻译模型 1.5 版本，包含一个18亿参数翻译模型（HY-MT1.5-1.8B）和一个70亿参数翻译模型（HY-MT1.5-7B）。
 * [gemmax](https://github.com/xiaomi-research/gemmax) - 基于 Gemma 的多语言机器翻译模型。
 * [ALMA](https://github.com/fe1ixxu/ALMA) - 最先进的基于大语言模型的翻译模型。


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
覆盖日语的多语言语音识别模型、工具包与对齐工具

 * [whisper](https://github.com/openai/whisper) - 通过大规模弱监督实现的鲁棒语音识别。
 * [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - OpenAI Whisper 模型的 C/C++ 移植版。
 * [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - 基于 CTranslate2 的更快 Whisper 转写。
 * [whisperX](https://github.com/m-bain/whisperX) - WhisperX：具备词级时间戳（及说话人分离）的自动语音识别。
 * [argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) - 面向 Apple Silicon 的端侧语音 AI。
 * [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) - Qwen3-ASR 是阿里云通义千问团队开发的开源语音识别模型系列，支持稳定的多语言语音/音乐/歌曲识别、语种识别与时间戳预测。
 * [SenseVoice](https://github.com/QwenAudio/SenseVoice) - 开源模型 SenseVoiceSmall，支持普通话、粤语、英语、日语和韩语的语音识别、语种识别、情感识别和音频事件检测。
 * [FunASR](https://github.com/modelscope/FunASR) - 支持训练、推理、流式语音识别、VAD、标点、说话人分离流水线以及兼容 OpenAI/MCP 服务的开源语音识别工具包。
 * [omnilingual-asr](https://github.com/facebookresearch/omnilingual-asr) - Omnilingual ASR：支持1600多种语言的开源多语言语音识别。
 * [moonshine](https://github.com/moonshine-ai/moonshine) - 面向构建语音代理与界面的超低延迟语音转文字、意图识别与文字转语音。
 * [Dolphin](https://github.com/DataoceanAI/Dolphin) - Dolphin 是由 DataoceanAI 与清华大学联合训练的多语言多任务语音识别模型。
 * [NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) - 为从事大语言模型、多模态与语音 AI（自动语音识别与文字转语音）研究和开发的人员打造的可扩展生成式 AI 框架。
 * [espnet](https://github.com/espnet/espnet) - 端到端语音处理工具包。
 * [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) - 基于新一代 Kaldi 与 onnxruntime、无需联网的语音识别、语音合成、说话人分离、语音增强、声源分离与 VAD。支持嵌入式系统、Android、iOS、HarmonyOS、Raspberry Pi、RISC-V、RK NPU、Axera NPU、Ascend NPU、x86_64 服务器、WebSocket 服务端/客户端，并支持12种编程语言。
 * [icefall](https://github.com/k2-fsa/icefall) - icefall 项目收录了使用 k2-fsa 与 lhotse、面向多种数据集的语音相关训练配方。
 * [vosk-api](https://github.com/alphacep/vosk-api) - 面向 Android、iOS、Raspberry Pi 及服务器的离线语音识别 API，支持 Python、Java、C# 和 Node。
 * [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) - 使用 Kaldi 进行强制对齐的命令行工具。
 * [Fun-ASR](https://github.com/QwenAudio/Fun-ASR) - Fun-ASR 语音识别模型系列，其中 Fun-ASR-Nano 原生支持 Hugging Face Transformers，并另外提供 FunASR、vLLM 与 llama.cpp 部署途径。
 * [FluidAudio](https://github.com/FluidInference/FluidAudio) - 可嵌入应用的前沿 CoreML 音频模型 —— 语音合成、语音识别、语音活动检测与说话人分离。基于 Swift，采用 SOTA 开源技术。
 * [CrispASR](https://github.com/CrispStrobe/CrispASR) - 面向多语言语音识别与语音合成模型的 C++（ggml）运行时中心：Cohere Transcribe、Parakeet TDT、Voxtral、Canary 1B v2 等，另提供通用强制对齐等功能。
 * [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) - 支持16个以上模型系列的 ggml 语音转文字推理。
 * [kaldi](https://github.com/kaldi-asr/kaldi) - kaldi-asr/kaldi 是 Kaldi 项目的官方所在地。
 * [julius](https://github.com/julius-speech/julius) - 开源大词汇量连续语音识别引擎。


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
能够合成日语语音的多语言语音合成与声音克隆系统

 * [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) - Qwen3-TTS 是阿里云通义千问团队开发的开源语音合成模型系列，支持稳定、富有表现力的流式语音生成、自由声音设计与生动的声音克隆。
 * [CosyVoice](https://github.com/QwenAudio/CosyVoice) - 多语言大型语音生成模型，提供推理、训练与部署的全栈能力。
 * [fish-speech](https://github.com/fishaudio/fish-speech) - SOTA 开源语音合成。
 * [chatterbox](https://github.com/resemble-ai/chatterbox) - SoTA 开源语音合成。
 * [coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) - 🐸💬 —— 在研究与生产环境中久经考验的语音合成深度学习工具包。
 * [MeloTTS](https://github.com/myshell-ai/MeloTTS) - MyShell.ai 推出的高质量多语言语音合成库，支持英语、西班牙语、法语、中文、日语和韩语。
 * [OpenVoice](https://github.com/myshell-ai/OpenVoice) - MIT 与 MyShell 推出的即时声音克隆。音频基础模型。
 * [kokoro](https://github.com/hexgrad/kokoro) - https://hf.co/hexgrad/Kokoro-82M。
 * [bark](https://github.com/suno-ai/bark) - 🔊 基于文本提示的生成式音频模型。
 * [Zonos](https://github.com/Zyphra/Zonos) - Zonos-v0.1 是基于超过20万小时多样化多语言语音训练的领先开放权重语音合成模型，其表现力与质量可媲美甚至超越顶尖的语音合成服务商。
 * [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 仅需1分钟的语音数据即可训练出优秀的语音合成模型！（少样本声音克隆）
 * [Amphion](https://github.com/open-mmlab/Amphion) - Amphion（/æmˈfaɪən/）是一个用于音频、音乐与语音生成的工具包，旨在支持可复现的研究，并帮助初级研究人员和工程师入门音频、音乐与语音生成的研究与开发领域。
 * [index-tts](https://github.com/index-tts/index-tts) - 工业级、可控且高效的零样本语音合成系统。
 * [VoxCPM](https://github.com/OpenBMB/VoxCPM) - VoxCPM2：无需分词器的语音合成，实现多语言语音生成、创意声音设计与逼真的声音克隆。
 * [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) - 一个强大的30亿参数、基于大语言模型的强化学习音频编辑模型，擅长编辑情感、说话风格与副语言特征，并具备稳健的零样本语音合成能力。
 * [FireRedTTS2](https://github.com/FireRedTeam/FireRedTTS2) - 面向多说话人对话生成的长篇流式语音合成系统。
 * [OuteTTS](https://github.com/edwko/OuteTTS) - OuteTTS 模型的接口。
 * [MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - 面向长篇语音、对话合成、声音设计、音效与实时流式语音合成的开源模型系列。
 * [MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) - 支持 CPU 实时推理、声音克隆与48kHz立体声生成的1亿参数多语言语音合成模型。
 * [mlx-audio](https://github.com/Blaizzy/mlx-audio) - 基于 Apple MLX 框架构建的语音合成（TTS）、语音识别（STT）与语音转换（STS）库，在 Apple Silicon 上提供高效的语音分析。
 * [Genie-TTS](https://github.com/High-Logic/Genie-TTS) - GPT-SoVITS 的 ONNX 推理引擎与模型转换工具。
 * [MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) - 面向长篇多说话人对话合成的多语言模型，具备灵活的说话人控制与零样本声音克隆能力。
 * [Confucius4-TTS](https://github.com/netease-youdao/Confucius4-TTS) - Confucius4-TTS：多语言、跨语言的零样本语音合成引擎。
 * [kani-tts](https://github.com/nineninesix-ai/kani-tts) - 使用神经音频编解码器与因果语言模型实现的文字转语音。
 * [OmniVoice](https://github.com/k2-fsa/OmniVoice) - 支持600多种语言的高质量声音克隆语音合成。
 * [T5Gemma-TTS](https://github.com/Aratako/T5Gemma-TTS) - 基于 T5Gemma 编码器-解码器大语言模型的多语言语音合成模型，支持声音克隆与时长控制。
 * [audio.cpp](https://github.com/0xShug0/audio.cpp) - 基于 ggml 打造的音频模型一体化纯 C++ 推理引擎，支持语音合成、语音识别、VAD、声音转换、音乐生成等，性能高度优化，且不依赖 Python。


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
能够处理日文文字的文字识别与文档解析工具

 * [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 将任意 PDF 或图像文档转换为可供 AI 使用的结构化数据。一个连接图像/PDF 与大语言模型的强大、轻量级 OCR 工具包，支持100多种语言。
 * [tesseract](https://github.com/tesseract-ocr/tesseract) - Tesseract 开源 OCR 引擎（主仓库）
 * [EasyOCR](https://github.com/JaidedAI/EasyOCR) - 开箱即用的 OCR，支持80多种语言以及拉丁字母、中文、阿拉伯文、天城文、西里尔字母等主流书写体系。
 * [surya](https://github.com/datalab-to/surya) - 支持90多种语言的 OCR、版面分析、阅读顺序与表格识别。
 * [chandra](https://github.com/datalab-to/chandra) - 可处理复杂表格、表单与手写内容并保留完整版面的 OCR 模型。
 * [MinerU](https://github.com/opendatalab/MinerU) - 将 PDF 与 Office 文档等复杂文档转换为适用于智能体工作流、可供大语言模型使用的 Markdown/JSON。
 * [RapidOCR](https://github.com/RapidAI/RapidOCR) - 📄 基于 ONNX Runtime、OpenVINO、MNN、PaddlePaddle、TensorRT 和 PyTorch 的多编程语言 OCR 工具包。
 * [Pix2Text](https://github.com/breezedeus/Pix2Text) - 一个使用小型模型的开源 Python3 工具，可识别图像中的版面、表格、数学公式（LaTeX）与文字，并将其转换为 Markdown 格式，是 Mathpix 的免费替代方案，可无缝将视觉内容转换为文本表示，支持80多种语言。
 * [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) - 面向 AI 就绪数据的 PDF 解析器，可自动化 PDF 无障碍处理，开源。
 * [TurboOCR](https://github.com/aiptimizer/TurboOCR) - TurboOCR，在 OmnidocBench 上速度超过每秒200张图。支持 TensorRT FP16、PP-OCRv6、HTTP + gRPC。
 * [tesseract.js](https://github.com/naptha/tesseract.js) - 支持100多种语言的纯 JavaScript OCR 📖🎉🖥。
 * [pdfminer.six](https://github.com/pdfminer/pdfminer.six) - 由社区维护的 pdfminer 分支——我们探究 PDF。
 * [PyMuPDF](https://github.com/pymupdf/PyMuPDF) - PyMuPDF 是一个用于 PDF（及其他）文档数据提取、分析、转换与操作的高性能 Python 库。


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
可使用支持日语模型的嵌入库、日语预训练嵌入以及提供日语索引的检索工具包

 * [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) - 从维基百科学习词语与实体向量表示的工具。
 * [pyserini](https://github.com/castorini/pyserini) - Pyserini 是一个支持稀疏与稠密表示、用于可复现信息检索研究的 Python 工具包。
 * [sentence-transformers](https://github.com/huggingface/sentence-transformers) - 最先进的嵌入、检索与重排序。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec/week)](https://pepy.tech/project/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec)](https://pepy.tech/project/wikipedia2vec) | ⭐ 972 | 🔴 january 2024|
| 🔗 [pyserini](https://github.com/castorini/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini/week)](https://pepy.tech/project/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini)](https://pepy.tech/project/pyserini) | ⭐ 2.2k | 🟢 last wednesday|
| 🔗 [sentence-transformers](https://github.com/huggingface/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers/week)](https://pepy.tech/project/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers)](https://pepy.tech/project/sentence-transformers) | ⭐ 19k | 🟢 last wednesday|


## Full-text search
内置日语分析器或分词器的搜索引擎与数据库

 * [lucene](https://github.com/apache/lucene) - Apache Lucene 开源搜索软件。
 * [elasticsearch](https://github.com/elastic/elasticsearch) - 免费开源的分布式 RESTful 搜索引擎。
 * [OpenSearch](https://github.com/opensearch-project/OpenSearch) - 🔎 开源分布式 RESTful 搜索引擎。
 * [solr](https://github.com/apache/solr) - Apache Solr 开源搜索软件。
 * [meilisearch](https://github.com/meilisearch/meilisearch) - 为您的网站和应用带来 AI 驱动混合搜索的极速搜索引擎 API。
 * [typesense](https://github.com/typesense/typesense) - Algolia + Pinecone 的开源替代方案，也是比 ElasticSearch 更易用的替代方案 ⚡ 🔍 ✨ 快速、容错拼写错误的内存模糊搜索引擎，用于打造愉悦的搜索体验。
 * [groonga](https://github.com/groonga/groonga) - 可嵌入的全文搜索引擎。Groonga 是 Senna 的后继项目。
 * [pgroonga](https://github.com/pgroonga/pgroonga) - PGroonga 是一个将 Groonga 用作索引的 PostgreSQL 扩展。PGroonga 让 PostgreSQL 成为支持所有语言的快速全文搜索平台！
 * [mroonga](https://github.com/mroonga/mroonga) - 基于 Groonga 的 MySQL 可插拔存储引擎。
 * [pg_bigm](https://github.com/pgbigm/pg_bigm) - pg_bigm 模块为 PostgreSQL 提供全文搜索能力，允许用户创建 2-gram（二元组）索引以加快全文搜索速度。
 * [paradedb](https://github.com/paradedb/paradedb) - 用一个 Postgres 统一处理应用数据、全文搜索、向量检索与聚合。pg_search 扩展的所在地。
 * [weaviate](https://github.com/weaviate/weaviate) - Weaviate 是一个开源向量数据库，可同时存储对象与向量，并以云原生数据库的容错性和可扩展性，实现向量搜索与结构化过滤的结合。
 * [milvus](https://github.com/milvus-io/milvus) - Milvus 是一个专为可扩展向量近似最近邻（ANN）搜索打造的高性能云原生向量数据库。
 * [qdrant](https://github.com/qdrant/qdrant) - Qdrant —— 面向下一代 AI 的高性能大规模向量数据库与向量搜索引擎，也提供云端版本 https://cloud.qdrant.io/。
 * [flexsearch](https://github.com/nextapps-de/flexsearch) - 面向浏览器和 Node.js 的下一代全文搜索库。
 * [sonic](https://github.com/valeriansaliou/sonic) - 🦔 快速、轻量且无模式的搜索后端，仅需数 MB 内存即可运行，是 Elasticsearch 的替代方案。
 * [orama](https://github.com/oramasearch/orama) - 🌌 可在浏览器、服务器或边缘网络中运行的完整搜索引擎与 RAG 流水线，体积不到 2kb，支持全文、向量与混合搜索。
 * [pagefind](https://github.com/Pagefind/pagefind) - 面向大规模静态网站的低带宽搜索。
 * [lancedb](https://github.com/lancedb/lancedb) - 面向多模态 AI、对开发者友好的开源嵌入式检索库。搜索更多，管理更少。
 * [bleve](https://github.com/blevesearch/bleve) - 面向 Go 的现代文本/数值/地理空间/向量索引库。
 * [lunr-languages](https://github.com/MihaiValentin/lunr-languages) - 为 Lunr JavaScript 库提供的多语言词干提取器与停用词合集。


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
具备日语规则或数据的文本规范化、罗马字转写与字音转换（G2P）工具

 * [NeMo-text-processing](https://github.com/NVIDIA/NeMo-text-processing) - 面向语音识别与语音合成的 NeMo 文本处理。
 * [WeTextProcessing](https://github.com/wenet-e2e/WeTextProcessing) - 文本规范化与逆文本规范化。
 * [misaki](https://github.com/hexgrad/misaki) - G2P（字音转换）。
 * [espeak-ng](https://github.com/espeak-ng/espeak-ng) - eSpeak NG 是一个支持100多种语言与口音的开源语音合成器。
 * [epitran](https://github.com/dmort27/epitran) - 将正字法文本转写为国际音标（IPA）的工具。
 * [uroman](https://github.com/isi-nlp/uroman) - 可将任意 Unicode 文字系统转换为罗马字母（拉丁字母）的通用罗马化工具。
 * [num2words](https://github.com/savoirfairelinux/num2words) - 将数字转换为文字的模块。42 --> forty-two。
 * [dateparser](https://github.com/scrapinghub/dateparser) - 解析人类可读日期的 Python 解析器。
 * [ipa-dict](https://github.com/open-dict-data/ipa-dict) - 带有 IPA 发音信息的单语词表。
 * [Recognizers-Text](https://github.com/microsoft/Recognizers-Text) - Microsoft.Recognizers.Text 提供多语言（中文、英语、法语、西班牙语、葡萄牙语、德语、意大利语、土耳其语、印地语、荷兰语；日语、韩语、阿拉伯语、瑞典语为部分支持）的数字、单位、日期/时间等的识别与解析。软件包地址：https://www.nuget.org/profiles/Recognizers.Text 、https://www.npmjs.com/~recognizers.text 。
 * [chrono](https://github.com/wanasit/chrono) - JavaScript 实现的自然语言日期解析器。


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
具备日语设置的评测工具以及包含日语的多语言数据集

 * [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) - 用于语言模型少样本评测的框架。
 * [mteb](https://github.com/embeddings-benchmark/mteb) - MTEB：跨语言与跨模态的最先进嵌入评测。
 * [sacrebleu](https://github.com/mjpost/sacrebleu) - 自动下载测试集并输出版本字符串以便于跨实验室比较的参考 BLEU 实现。
 * [xtreme](https://github.com/google-research/xtreme) - XTREME 是一个用于评测预训练多语言模型跨语言泛化能力的基准，涵盖40种类型多样的语言，包含九项任务。
 * [belebele](https://github.com/facebookresearch/belebele) - 大规模多语言阅读理解数据集 Belebele 的仓库。
 * [miracl](https://github.com/project-miracl/miracl) - 面向信息检索的大规模多语言数据集，在18种不同语言上进行了全面的人工标注。
 * [mr.tydi](https://github.com/castorini/mr.tydi) - Mr. TyDi 是基于 TyDi 构建的多语言基准数据集，涵盖11种类型多样的语言。
 * [tydiqa](https://github.com/google-research-datasets/tydiqa) - TyDi QA 包含20万个在11种类型多样语言中人工标注的问答对，这些问答在未见答案且未使用翻译的情况下编写，专为自动问答系统的训练与评测而设计。本仓库提供该数据集的评测代码与基线系统。
 * [ml-mkqa](https://github.com/apple-aiml-research/ml-mkqa) - 我们介绍开放域问答评测集 MKQA，包含在26种类型多样的语言间对齐的1万个问答对（共计26万个问答对）。该数据集旨在为跨广泛语言的问答质量提供具有挑战性的基准。详情请参阅论文《MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering》。
 * [massive](https://github.com/alexa/massive) - 面向 MASSIVE 数据集的工具与建模代码。
 * [paws](https://github.com/google-research-datasets/paws) - 该数据集包含108,463个人工标注对和656k个含噪声标注对，用以体现在释义识别问题中，对结构、上下文与词序信息进行建模的重要性。
 * [xl-sum](https://github.com/csebuetnlp/xl-sum) - 本仓库包含发表于 Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021 的论文《XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages》的代码、数据与模型。
 * [url-nlp (MGSM)](https://github.com/google-research/url-nlp) - MGSM 是论文《Language models are multilingual chain-of-thought reasoners》中提出的小学数学题基准。
 * [M-IFEval](https://github.com/lightblue-tech/M-IFEval) - 本仓库包含 M-IFEval（多语言指令遵循评测）的源代码与数据。
 * [mintaka](https://github.com/amazon-science/mintaka) - 来自论文《Mintaka: A Complex, Natural, and Multilingual Dataset for End-to-End Question Answering》（COLING 2022）的数据集。
 * [Wikilingua](https://github.com/esdurmus/Wikilingua) - 从 WikiHow 抽取的多语言生成式摘要数据集。


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
具备日语专门处理的语料处理、词频与词汇数据库工具

 * [datatrove](https://github.com/huggingface/datatrove) - 通过提供一组平台无关、可自定义的流水线处理模块，将数据处理从繁琐的脚本编写中解放出来。
 * [Wordless](https://github.com/BLKSerene/Wordless) - 面向语言、文学与翻译研究、支持多语言的综合语料库工具。
 * [wordfreq](https://github.com/rspeer/wordfreq) - 访问多种自然语言的词频数据库。
 * [wn](https://github.com/goodmami/wn) - 面向 Python 的现代跨语言 WordNet 接口。
 * [wiktextract](https://github.com/tatuylonen/wiktextract) - 维基词典转储文件解析器与多语言数据提取工具。
 * [scattertext](https://github.com/JasonKessler/scattertext) - 精美地可视化不同文档类型之间语言使用的差异。
 * [sumy](https://github.com/miso-belica/sumy) - 用于对文本文档与 HTML 页面进行自动摘要的模块。
 * [textlint](https://github.com/textlint/textlint) - textlint 是面向自然语言文本的可插拔校对工具。


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

