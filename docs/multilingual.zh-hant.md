# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

具備日語功能的多語言 GitHub 儲存庫精選列表。
本頁面收錄具備日語具體功能的多語言函式庫、模型與資料集，例如日語語種識別、日語分詞器與分析器、日語語音與 OCR 模型，以及資料集中的日語部分。目前共收錄155個儲存庫。

_更新於2026年9月18日_

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
內建日語模型或分詞器的通用多語言NLP框架

 * [spaCy](https://github.com/explosion/spaCy) - 💫 Python 實現的工業級自然語言處理（NLP）。
 * [stanza](https://github.com/stanfordnlp/stanza) - 用於分詞、分句、命名實體識別以及多種人類語言句法分析的 Stanford NLP Python 函式庫。
 * [HanLP](https://github.com/hankcs/HanLP) - 面向下一個十年的自然語言處理。分詞、詞性標註、命名實體識別、句法與語義依存分析、文件分類。
 * [trankit](https://github.com/nlp-uoregon/trankit) - Trankit 是一個基於 Transformer 的輕量級多語言自然語言處理 Python 工具包。
 * [udpipe](https://github.com/ufal/udpipe) - UDPipe：用於對 Universal Treebanks 及其他 CoNLL-U 檔案進行分詞、標註、詞形還原和句法分析的可訓練管線。
 * [spark-nlp](https://github.com/JohnSnowLabs/spark-nlp) - 最先進的自然語言處理。
 * [openmed](https://github.com/maziyarpanahi/openmed) - 本地優先的醫療 AI：完全在裝置端執行的臨床命名實體辨識與符合 HIPAA 的個人資訊去識別化。擁有2200多個醫療模型，支援21種語言，相容 Apple MLX + Python，無需雲端，病患資料不會離開您的網路。Apache-2.0 授權。
 * [transformers](https://github.com/huggingface/transformers) - 🤗 Transformers：面向文字、視覺、音訊及多模態領域最先進機器學習模型的模型定義框架，同時支援推論與訓練。
 * [nltk](https://github.com/nltk/nltk) - NLTK 原始碼。


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
適用於日語文本的子詞、單詞及句子邊界切分工具

 * [sentencepiece](https://github.com/google/sentencepiece) - 面向基於神經網路的文字生成之無監督文字分詞器。
 * [icu](https://github.com/unicode-org/icu) - ICU 專案原始碼的所在地。
 * [wtpsplit](https://github.com/segment-any-text/wtpsplit) - 以穩健、高效且可調適的方式將文字切分為句子或其他語意單元的工具包。
 * [charabia](https://github.com/meilisearch/charabia) - Meilisearch 用於對查詢和文件進行分詞的函式庫。
 * [gse](https://github.com/go-ego/gse) - 高效的 Go 語言多語言 NLP 與文字切分函式庫，支援英語、中文、日語等。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [sentencepiece](https://github.com/google/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece/week)](https://pepy.tech/project/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece)](https://pepy.tech/project/sentencepiece) | ⭐ 12k | 🟢 last wednesday|
| 🔗 [icu](https://github.com/unicode-org/icu) | - | - | ⭐ 3.6k | 🟢 yesterday|
| 🔗 [wtpsplit](https://github.com/segment-any-text/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit/week)](https://pepy.tech/project/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit)](https://pepy.tech/project/wtpsplit) | ⭐ 1.3k | 🟡 april|
| 🔗 [charabia](https://github.com/meilisearch/charabia) | - | ![Crates.io](https://img.shields.io/crates/d/charabia) | ⭐ 358 | 🟢 august|
| 🔗 [gse](https://github.com/go-ego/gse) | - | - | ⭐ 2.8k | 🟢 last saturday|


## Language identification
判定文本語言的函式庫（支援的標籤包含日語）

 * [fastText](https://github.com/facebookresearch/fastText) - 用於快速文字表示與分類的函式庫。
 * [lingua-py](https://github.com/pemistahl/lingua-py) - 面向 Python 的最精準自然語言偵測函式庫，適用於短文本和多語言混合文本。
 * [lingua](https://github.com/pemistahl/lingua) - 面向 Java 和 JVM 的最精準自然語言偵測函式庫，同樣適用於長文本和短文本。
 * [lingua-rs](https://github.com/pemistahl/lingua-rs) - 面向 Rust 的最精準自然語言偵測函式庫，適用於短文本和多語言混合文本。
 * [lingua-go](https://github.com/pemistahl/lingua-go) - 面向 Go 的最精準自然語言偵測函式庫，適用於短文本和多語言混合文本。
 * [langdetect](https://github.com/Mimino666/langdetect) - Google language-detection 函式庫的 Python 移植版。
 * [GlotLID](https://github.com/cisnlp/GlotLID) - [EMNLP 2023] 💬 支援2000多個標籤的語言識別。
 * [whatlang-rs](https://github.com/greyblake/whatlang-rs) - 面向 Rust 的自然語言偵測函式庫。線上示範：https://whatlang.org/。
 * [franc](https://github.com/wooorm/franc) - 自然語言偵測。
 * [whichlang](https://github.com/quickwit-oss/whichlang) - 面向 Rust 的極速輕量語言偵測函式庫。


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
支援含日語語言對的翻譯模型、引擎與服務

 * [seamless_communication](https://github.com/facebookresearch/seamless_communication) - 面向最先進語音與文字翻譯的基礎模型。
 * [argos-translate](https://github.com/argosopentech/argos-translate) - 使用 Python 編寫的開源離線翻譯函式庫。
 * [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) - 免費開源的機器翻譯 API，可自行架設、支援離線，且易於設定。
 * [Opus-MT](https://github.com/Helsinki-NLP/Opus-MT) - 開放的神經網路機器翻譯模型與網路服務。
 * [Seed-X-7B](https://github.com/ByteDance-Seed/Seed-X-7B) - Seed-X 是一個強大的開源多語言翻譯語言模型系列，參數量為70億，包含指令模型、強化學習模型和獎勵模型。
 * [Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2) - Hy-MT2 是一系列面向複雜真實場景設計的「快思考」多語言翻譯模型，提供 1.8B、7B、30B-A3B 三種規模。
 * [Hy-MT](https://github.com/Tencent-Hunyuan/Hy-MT) - 混元翻譯模型 1.5 版本，包含一個18億參數翻譯模型（HY-MT1.5-1.8B）和一個70億參數翻譯模型（HY-MT1.5-7B）。
 * [gemmax](https://github.com/xiaomi-research/gemmax) - 基於 Gemma 的多語言機器翻譯模型。
 * [ALMA](https://github.com/fe1ixxu/ALMA) - 最先進的基於大型語言模型的翻譯模型。


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
涵蓋日語的多語言語音辨識模型、工具包與對齊工具

 * [whisper](https://github.com/openai/whisper) - 透過大規模弱監督實現的穩健語音辨識。
 * [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - OpenAI Whisper 模型的 C/C++ 移植版。
 * [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - 基於 CTranslate2 的更快 Whisper 轉寫。
 * [whisperX](https://github.com/m-bain/whisperX) - WhisperX：具備詞級時間戳（及說話者分離）的自動語音辨識。
 * [argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) - 面向 Apple Silicon 的端側語音 AI。
 * [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) - Qwen3-ASR 是阿里雲通義千問團隊開發的開源語音辨識模型系列，支援穩定的多語言語音/音樂/歌曲辨識、語種識別與時間戳預測。
 * [SenseVoice](https://github.com/QwenAudio/SenseVoice) - 開源模型 SenseVoiceSmall，支援普通話、粵語、英語、日語和韓語的語音辨識、語種識別、情緒辨識和音訊事件偵測。
 * [FunASR](https://github.com/modelscope/FunASR) - 支援訓練、推論、串流語音辨識、VAD、標點、說話者分離管線以及相容 OpenAI/MCP 服務的開源語音辨識工具包。
 * [omnilingual-asr](https://github.com/facebookresearch/omnilingual-asr) - Omnilingual ASR：支援1600多種語言的開源多語言語音辨識。
 * [moonshine](https://github.com/moonshine-ai/moonshine) - 面向建構語音代理與介面的超低延遲語音轉文字、意圖識別與文字轉語音。
 * [Dolphin](https://github.com/DataoceanAI/Dolphin) - Dolphin 是由 DataoceanAI 與清華大學聯合訓練的多語言多任務語音辨識模型。
 * [NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) - 為從事大型語言模型、多模態與語音 AI（自動語音辨識與文字轉語音）研究和開發的人員打造的可擴充生成式 AI 框架。
 * [espnet](https://github.com/espnet/espnet) - 端到端語音處理工具包。
 * [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) - 基於新一代 Kaldi 與 onnxruntime、無需連網的語音辨識、語音合成、說話者分離、語音增強、聲源分離與 VAD。支援嵌入式系統、Android、iOS、HarmonyOS、Raspberry Pi、RISC-V、RK NPU、Axera NPU、Ascend NPU、x86_64 伺服器、WebSocket 伺服端/用戶端，並支援12種程式語言。
 * [icefall](https://github.com/k2-fsa/icefall) - icefall 專案收錄了使用 k2-fsa 與 lhotse、面向多種資料集的語音相關訓練配方。
 * [vosk-api](https://github.com/alphacep/vosk-api) - 面向 Android、iOS、Raspberry Pi 及伺服器的離線語音辨識 API，支援 Python、Java、C# 和 Node。
 * [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) - 使用 Kaldi 進行強制對齊的命令列工具。
 * [Fun-ASR](https://github.com/QwenAudio/Fun-ASR) - Fun-ASR 語音辨識模型系列，其中 Fun-ASR-Nano 原生支援 Hugging Face Transformers，並另外提供 FunASR、vLLM 與 llama.cpp 部署途徑。
 * [FluidAudio](https://github.com/FluidInference/FluidAudio) - 可嵌入應用程式的前沿 CoreML 音訊模型 —— 語音合成、語音辨識、語音活動偵測與說話者分離。基於 Swift，採用 SOTA 開源技術。
 * [CrispASR](https://github.com/CrispStrobe/CrispASR) - 面向多語言語音辨識與語音合成模型的 C++（ggml）執行環境中心：Cohere Transcribe、Parakeet TDT、Voxtral、Canary 1B v2 等，另提供通用強制對齊等功能。
 * [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) - 支援16個以上模型系列的 ggml 語音轉文字推論。
 * [kaldi](https://github.com/kaldi-asr/kaldi) - kaldi-asr/kaldi 是 Kaldi 專案的官方所在地。
 * [julius](https://github.com/julius-speech/julius) - 開源大詞彙量連續語音辨識引擎。


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
能夠合成日語語音的多語言語音合成與聲音複製系統

 * [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) - Qwen3-TTS 是阿里雲通義千問團隊開發的開源語音合成模型系列，支援穩定、富有表現力的串流語音生成、自由聲音設計與生動的聲音複製。
 * [CosyVoice](https://github.com/QwenAudio/CosyVoice) - 多語言大型語音生成模型，提供推論、訓練與部署的全端能力。
 * [fish-speech](https://github.com/fishaudio/fish-speech) - SOTA 開源語音合成。
 * [chatterbox](https://github.com/resemble-ai/chatterbox) - SoTA 開源語音合成。
 * [coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) - 🐸💬 —— 在研究與生產環境中久經考驗的語音合成深度學習工具包。
 * [MeloTTS](https://github.com/myshell-ai/MeloTTS) - MyShell.ai 推出的高品質多語言語音合成函式庫，支援英語、西班牙語、法語、中文、日語和韓語。
 * [OpenVoice](https://github.com/myshell-ai/OpenVoice) - MIT 與 MyShell 推出的即時聲音複製。音訊基礎模型。
 * [kokoro](https://github.com/hexgrad/kokoro) - https://hf.co/hexgrad/Kokoro-82M。
 * [bark](https://github.com/suno-ai/bark) - 🔊 基於文字提示的生成式音訊模型。
 * [Zonos](https://github.com/Zyphra/Zonos) - Zonos-v0.1 是基於超過20萬小時多樣化多語言語音訓練的領先開放權重語音合成模型，其表現力與品質可媲美甚至超越頂尖的語音合成服務商。
 * [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - 僅需1分鐘的語音資料即可訓練出優秀的語音合成模型！（少樣本聲音複製）
 * [Amphion](https://github.com/open-mmlab/Amphion) - Amphion（/æmˈfaɪən/）是一個用於音訊、音樂與語音生成的工具包，旨在支援可重現的研究，並協助初級研究人員與工程師入門音訊、音樂與語音生成的研究與開發領域。
 * [index-tts](https://github.com/index-tts/index-tts) - 工業級、可控且高效的零樣本語音合成系統。
 * [VoxCPM](https://github.com/OpenBMB/VoxCPM) - VoxCPM2：無需分詞器的語音合成，實現多語言語音生成、創意聲音設計與逼真的聲音複製。
 * [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) - 一個強大的30億參數、基於大型語言模型的強化學習音訊編輯模型，擅長編輯情緒、說話風格與副語言特徵，並具備穩健的零樣本語音合成能力。
 * [FireRedTTS2](https://github.com/FireRedTeam/FireRedTTS2) - 面向多說話者對話生成的長篇串流語音合成系統。
 * [OuteTTS](https://github.com/edwko/OuteTTS) - OuteTTS 模型的介面。
 * [MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - 面向長篇語音、對話合成、聲音設計、音效與即時串流語音合成的開源模型系列。
 * [MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) - 支援 CPU 即時推論、聲音複製與48kHz立體聲生成的1億參數多語言語音合成模型。
 * [mlx-audio](https://github.com/Blaizzy/mlx-audio) - 基於 Apple MLX 框架建構的語音合成（TTS）、語音辨識（STT）與語音轉換（STS）函式庫，在 Apple Silicon 上提供高效的語音分析。
 * [Genie-TTS](https://github.com/High-Logic/Genie-TTS) - GPT-SoVITS 的 ONNX 推論引擎與模型轉換工具。
 * [MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) - 面向長篇多說話者對話合成的多語言模型，具備靈活的說話者控制與零樣本聲音複製能力。
 * [Confucius4-TTS](https://github.com/netease-youdao/Confucius4-TTS) - Confucius4-TTS：多語言、跨語言的零樣本語音合成引擎。
 * [kani-tts](https://github.com/nineninesix-ai/kani-tts) - 使用神經音訊編解碼器與因果語言模型實現的文字轉語音。
 * [OmniVoice](https://github.com/k2-fsa/OmniVoice) - 支援600多種語言的高品質聲音複製語音合成。
 * [T5Gemma-TTS](https://github.com/Aratako/T5Gemma-TTS) - 基於 T5Gemma 編碼器-解碼器大型語言模型的多語言語音合成模型，支援聲音複製與時長控制。
 * [audio.cpp](https://github.com/0xShug0/audio.cpp) - 基於 ggml 打造的音訊模型一體化純 C++ 推論引擎，支援語音合成、語音辨識、VAD、聲音轉換、音樂生成等，效能高度最佳化，且不依賴 Python。


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
能夠處理日文文字的文字辨識與文件解析工具

 * [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 將任意 PDF 或影像文件轉換為可供 AI 使用的結構化資料。一個連接影像/PDF 與大型語言模型的強大、輕量級 OCR 工具包，支援100多種語言。
 * [tesseract](https://github.com/tesseract-ocr/tesseract) - Tesseract 開源 OCR 引擎（主儲存庫）
 * [EasyOCR](https://github.com/JaidedAI/EasyOCR) - 開箱即用的 OCR，支援80多種語言以及拉丁字母、中文、阿拉伯文、天城文、西里爾字母等主流書寫體系。
 * [surya](https://github.com/datalab-to/surya) - 支援90多種語言的 OCR、版面分析、閱讀順序與表格辨識。
 * [chandra](https://github.com/datalab-to/chandra) - 可處理複雜表格、表單與手寫內容並保留完整版面的 OCR 模型。
 * [MinerU](https://github.com/opendatalab/MinerU) - 將 PDF 與 Office 文件等複雜文件轉換為適用於代理工作流程、可供大型語言模型使用的 Markdown/JSON。
 * [RapidOCR](https://github.com/RapidAI/RapidOCR) - 📄 基於 ONNX Runtime、OpenVINO、MNN、PaddlePaddle、TensorRT 和 PyTorch 的多程式語言 OCR 工具包。
 * [Pix2Text](https://github.com/breezedeus/Pix2Text) - 一個使用小型模型的開源 Python3 工具，可辨識影像中的版面、表格、數學公式（LaTeX）與文字，並將其轉換為 Markdown 格式，是 Mathpix 的免費替代方案，可無縫將視覺內容轉換為文字表示，支援80多種語言。
 * [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) - 面向 AI 就緒資料的 PDF 解析器，可自動化 PDF 無障礙處理，開源。
 * [TurboOCR](https://github.com/aiptimizer/TurboOCR) - TurboOCR，在 OmnidocBench 上速度超過每秒200張圖。支援 TensorRT FP16、PP-OCRv6、HTTP + gRPC。
 * [tesseract.js](https://github.com/naptha/tesseract.js) - 支援100多種語言的純 JavaScript OCR 📖🎉🖥。
 * [pdfminer.six](https://github.com/pdfminer/pdfminer.six) - 由社群維護的 pdfminer 分支——我們探究 PDF。
 * [PyMuPDF](https://github.com/pymupdf/PyMuPDF) - PyMuPDF 是一個用於 PDF（及其他）文件資料擷取、分析、轉換與操作的高效能 Python 函式庫。


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
可使用支援日語模型的嵌入函式庫、日語預訓練嵌入以及提供日語索引的檢索工具包

 * [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) - 從維基百科學習詞語與實體向量表示的工具。
 * [pyserini](https://github.com/castorini/pyserini) - Pyserini 是一個支援稀疏與稠密表示、用於可重現資訊檢索研究的 Python 工具包。
 * [sentence-transformers](https://github.com/huggingface/sentence-transformers) - 最先進的嵌入、檢索與重排序。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec/week)](https://pepy.tech/project/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec)](https://pepy.tech/project/wikipedia2vec) | ⭐ 972 | 🔴 january 2024|
| 🔗 [pyserini](https://github.com/castorini/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini/week)](https://pepy.tech/project/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini)](https://pepy.tech/project/pyserini) | ⭐ 2.2k | 🟢 last wednesday|
| 🔗 [sentence-transformers](https://github.com/huggingface/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers/week)](https://pepy.tech/project/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers)](https://pepy.tech/project/sentence-transformers) | ⭐ 19k | 🟢 last wednesday|


## Full-text search
內建日語分析器或分詞器的搜尋引擎與資料庫

 * [lucene](https://github.com/apache/lucene) - Apache Lucene 開源搜尋軟體。
 * [elasticsearch](https://github.com/elastic/elasticsearch) - 免費開源的分散式 RESTful 搜尋引擎。
 * [OpenSearch](https://github.com/opensearch-project/OpenSearch) - 🔎 開源分散式 RESTful 搜尋引擎。
 * [solr](https://github.com/apache/solr) - Apache Solr 開源搜尋軟體。
 * [meilisearch](https://github.com/meilisearch/meilisearch) - 為您的網站和應用程式帶來 AI 驅動混合搜尋的極速搜尋引擎 API。
 * [typesense](https://github.com/typesense/typesense) - Algolia + Pinecone 的開源替代方案，也是比 ElasticSearch 更易用的替代方案 ⚡ 🔍 ✨ 快速、容錯拼字錯誤的記憶體內模糊搜尋引擎，用於打造愉悅的搜尋體驗。
 * [groonga](https://github.com/groonga/groonga) - 可嵌入的全文搜尋引擎。Groonga 是 Senna 的後繼專案。
 * [pgroonga](https://github.com/pgroonga/pgroonga) - PGroonga 是一個將 Groonga 用作索引的 PostgreSQL 擴充功能。PGroonga 讓 PostgreSQL 成為支援所有語言的快速全文搜尋平台！
 * [mroonga](https://github.com/mroonga/mroonga) - 基於 Groonga 的 MySQL 可插拔儲存引擎。
 * [pg_bigm](https://github.com/pgbigm/pg_bigm) - pg_bigm 模組為 PostgreSQL 提供全文搜尋能力，允許使用者建立 2-gram（二元組）索引以加快全文搜尋速度。
 * [paradedb](https://github.com/paradedb/paradedb) - 用一個 Postgres 統一處理應用程式資料、全文搜尋、向量檢索與聚合。pg_search 擴充功能的所在地。
 * [weaviate](https://github.com/weaviate/weaviate) - Weaviate 是一個開源向量資料庫，可同時儲存物件與向量，並以雲原生資料庫的容錯性和可擴充性，實現向量搜尋與結構化篩選的結合。
 * [milvus](https://github.com/milvus-io/milvus) - Milvus 是一個專為可擴充向量近似最近鄰（ANN）搜尋打造的高效能雲原生向量資料庫。
 * [qdrant](https://github.com/qdrant/qdrant) - Qdrant —— 面向下一代 AI 的高效能大規模向量資料庫與向量搜尋引擎，也提供雲端版本 https://cloud.qdrant.io/。
 * [flexsearch](https://github.com/nextapps-de/flexsearch) - 面向瀏覽器和 Node.js 的下一代全文搜尋函式庫。
 * [sonic](https://github.com/valeriansaliou/sonic) - 🦔 快速、輕量且無結構描述的搜尋後端，僅需數 MB 記憶體即可執行，是 Elasticsearch 的替代方案。
 * [orama](https://github.com/oramasearch/orama) - 🌌 可在瀏覽器、伺服器或邊緣網路中執行的完整搜尋引擎與 RAG 管線，體積不到 2kb，支援全文、向量與混合搜尋。
 * [pagefind](https://github.com/Pagefind/pagefind) - 面向大規模靜態網站的低頻寬搜尋。
 * [lancedb](https://github.com/lancedb/lancedb) - 面向多模態 AI、對開發者友善的開源嵌入式檢索函式庫。搜尋更多，管理更少。
 * [bleve](https://github.com/blevesearch/bleve) - 面向 Go 的現代文字/數值/地理空間/向量索引函式庫。
 * [lunr-languages](https://github.com/MihaiValentin/lunr-languages) - 為 Lunr JavaScript 函式庫提供的多語言詞幹擷取器與停用詞合集。


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
具備日語規則或資料的文本正規化、羅馬字轉寫與字音轉換（G2P）工具

 * [NeMo-text-processing](https://github.com/NVIDIA/NeMo-text-processing) - 面向語音辨識與語音合成的 NeMo 文字處理。
 * [WeTextProcessing](https://github.com/wenet-e2e/WeTextProcessing) - 文本正規化與逆文本正規化。
 * [misaki](https://github.com/hexgrad/misaki) - G2P（字音轉換）。
 * [espeak-ng](https://github.com/espeak-ng/espeak-ng) - eSpeak NG 是一個支援100多種語言與口音的開源語音合成器。
 * [epitran](https://github.com/dmort27/epitran) - 將正字法文本轉寫為國際音標（IPA）的工具。
 * [uroman](https://github.com/isi-nlp/uroman) - 可將任意 Unicode 文字系統轉換為羅馬字母（拉丁字母）的通用羅馬化工具。
 * [num2words](https://github.com/savoirfairelinux/num2words) - 將數字轉換為文字的模組。42 --> forty-two。
 * [dateparser](https://github.com/scrapinghub/dateparser) - 解析人類可讀日期的 Python 解析器。
 * [ipa-dict](https://github.com/open-dict-data/ipa-dict) - 帶有 IPA 發音資訊的單語詞表。
 * [Recognizers-Text](https://github.com/microsoft/Recognizers-Text) - Microsoft.Recognizers.Text 提供多語言（中文、英語、法語、西班牙語、葡萄牙語、德語、義大利語、土耳其語、印地語、荷蘭語；日語、韓語、阿拉伯語、瑞典語為部分支援）的數字、單位、日期/時間等的識別與解析。套件位址：https://www.nuget.org/profiles/Recognizers.Text 、https://www.npmjs.com/~recognizers.text 。
 * [chrono](https://github.com/wanasit/chrono) - JavaScript 實現的自然語言日期解析器。


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
具備日語設定的評測工具以及包含日語的多語言資料集

 * [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) - 用於語言模型少樣本評測的框架。
 * [mteb](https://github.com/embeddings-benchmark/mteb) - MTEB：跨語言與跨模態的最先進嵌入評測。
 * [sacrebleu](https://github.com/mjpost/sacrebleu) - 自動下載測試集並輸出版本字串以便於跨實驗室比較的參考 BLEU 實作。
 * [xtreme](https://github.com/google-research/xtreme) - XTREME 是一個用於評測預訓練多語言模型跨語言泛化能力的基準，涵蓋40種類型多樣的語言，包含九項任務。
 * [belebele](https://github.com/facebookresearch/belebele) - 大規模多語言閱讀理解資料集 Belebele 的儲存庫。
 * [miracl](https://github.com/project-miracl/miracl) - 面向資訊檢索的大規模多語言資料集，在18種不同語言上進行了全面的人工標註。
 * [mr.tydi](https://github.com/castorini/mr.tydi) - Mr. TyDi 是基於 TyDi 建構的多語言基準資料集，涵蓋11種類型多樣的語言。
 * [tydiqa](https://github.com/google-research-datasets/tydiqa) - TyDi QA 包含20萬個在11種類型多樣語言中人工標註的問答對，這些問答在未見答案且未使用翻譯的情況下撰寫，專為自動問答系統的訓練與評測而設計。本儲存庫提供該資料集的評測程式碼與基線系統。
 * [ml-mkqa](https://github.com/apple-aiml-research/ml-mkqa) - 我們介紹開放域問答評測集 MKQA，包含在26種類型多樣的語言間對齊的1萬個問答對（共計26萬個問答對）。該資料集旨在為跨廣泛語言的問答品質提供具有挑戰性的基準。詳情請參閱論文《MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering》。
 * [massive](https://github.com/alexa/massive) - 面向 MASSIVE 資料集的工具與建模程式碼。
 * [paws](https://github.com/google-research-datasets/paws) - 該資料集包含108,463個人工標註對和656k個含雜訊標註對，用以體現在釋義識別問題中，對結構、上下文與詞序資訊進行建模的重要性。
 * [xl-sum](https://github.com/csebuetnlp/xl-sum) - 本儲存庫包含發表於 Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021 的論文《XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages》的程式碼、資料與模型。
 * [url-nlp (MGSM)](https://github.com/google-research/url-nlp) - MGSM 是論文《Language models are multilingual chain-of-thought reasoners》中提出的小學數學題基準。
 * [M-IFEval](https://github.com/lightblue-tech/M-IFEval) - 本儲存庫包含 M-IFEval（多語言指令遵循評測）的原始碼與資料。
 * [mintaka](https://github.com/amazon-science/mintaka) - 來自論文《Mintaka: A Complex, Natural, and Multilingual Dataset for End-to-End Question Answering》（COLING 2022）的資料集。
 * [Wikilingua](https://github.com/esdurmus/Wikilingua) - 從 WikiHow 擷取的多語言生成式摘要資料集。


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
具備日語專門處理的語料處理、詞頻與詞彙資料庫工具

 * [datatrove](https://github.com/huggingface/datatrove) - 透過提供一組平台無關、可自訂的管線處理模組，將資料處理從繁瑣的指令碼編寫中解放出來。
 * [Wordless](https://github.com/BLKSerene/Wordless) - 面向語言、文學與翻譯研究、支援多語言的綜合語料庫工具。
 * [wordfreq](https://github.com/rspeer/wordfreq) - 存取多種自然語言的詞頻資料庫。
 * [wn](https://github.com/goodmami/wn) - 面向 Python 的現代跨語言 WordNet 介面。
 * [wiktextract](https://github.com/tatuylonen/wiktextract) - 維基詞典傾印檔案解析器與多語言資料擷取工具。
 * [scattertext](https://github.com/JasonKessler/scattertext) - 精美地視覺化不同文件類型之間語言使用的差異。
 * [sumy](https://github.com/miso-belica/sumy) - 用於對文字文件與 HTML 頁面進行自動摘要的模組。
 * [textlint](https://github.com/textlint/textlint) - textlint 是面向自然語言文本的可插拔校對工具。


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

