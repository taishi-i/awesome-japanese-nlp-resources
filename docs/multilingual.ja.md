# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語向けの機能を備えた多言語 GitHub リポジトリを厳選してまとめた一覧です。
このページでは、日本語の言語判定、日本語トークナイザーやアナライザー、日本語の音声・OCRモデル、データセットの日本語分割など、日本語向けの具体的な機能を備えた多言語ライブラリ・モデル・データセットを掲載しています。現在、155件のリポジトリを掲載しています。

_2026年9月18日更新_

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
日本語モデルやトークナイザーを同梱した汎用の多言語NLPフレームワーク

 * [spaCy](https://github.com/explosion/spaCy) - 💫 Python による産業レベルの自然言語処理（NLP）。
 * [stanza](https://github.com/stanfordnlp/stanza) - トークン化・文分割・固有表現認識、および多数の言語の構文解析のための Stanford NLP の Python ライブラリ。
 * [HanLP](https://github.com/hankcs/HanLP) - 次の10年のための自然言語処理。単語分割、品詞タグ付け、固有表現認識、統語・意味依存構造解析、文書分類。
 * [trankit](https://github.com/nlp-uoregon/trankit) - Trankit は、多言語自然言語処理のための軽量な Transformer ベースの Python ツールキットです。
 * [udpipe](https://github.com/ufal/udpipe) - UDPipe：Universal Treebanks やその他の CoNLL-U ファイルのトークン化・タグ付け・見出し語化・構文解析を行う、学習可能なパイプライン。
 * [spark-nlp](https://github.com/JohnSnowLabs/spark-nlp) - 最先端の自然言語処理。
 * [openmed](https://github.com/maziyarpanahi/openmed) - ローカルファーストのヘルスケアAI：完全にオンデバイスで動作する臨床固有表現認識と HIPAA 準拠の個人情報匿名化。2,200以上の医療モデル、21言語、Apple MLX + Python 対応。クラウド不要で、患者データがネットワーク外に出ることはありません。Apache-2.0。
 * [transformers](https://github.com/huggingface/transformers) - 🤗 Transformers：テキスト・画像・音声・マルチモーダルの最先端機械学習モデルのためのモデル定義フレームワークで、推論と学習の両方に対応。
 * [nltk](https://github.com/nltk/nltk) - NLTK のソースコード。


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
日本語テキストに対応したサブワード・単語・文境界の分割ツール

 * [sentencepiece](https://github.com/google/sentencepiece) - ニューラルネットワークによるテキスト生成のための教師なしテキストトークナイザー。
 * [icu](https://github.com/unicode-org/icu) - ICU プロジェクトのソースコードのホーム。
 * [wtpsplit](https://github.com/segment-any-text/wtpsplit) - テキストを文や他の意味単位に、頑健かつ効率的で適応性の高い方法で分割するツールキット。
 * [charabia](https://github.com/meilisearch/charabia) - Meilisearch がクエリとドキュメントをトークン化するために使用するライブラリ。
 * [gse](https://github.com/go-ego/gse) - 効率的な多言語 NLP とテキスト分割のための Go ライブラリ。英語・中国語・日本語などに対応。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [sentencepiece](https://github.com/google/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece/week)](https://pepy.tech/project/sentencepiece) | [![Downloads](https://static.pepy.tech/badge/sentencepiece)](https://pepy.tech/project/sentencepiece) | ⭐ 12k | 🟢 last wednesday|
| 🔗 [icu](https://github.com/unicode-org/icu) | - | - | ⭐ 3.6k | 🟢 yesterday|
| 🔗 [wtpsplit](https://github.com/segment-any-text/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit/week)](https://pepy.tech/project/wtpsplit) | [![Downloads](https://static.pepy.tech/badge/wtpsplit)](https://pepy.tech/project/wtpsplit) | ⭐ 1.3k | 🟡 april|
| 🔗 [charabia](https://github.com/meilisearch/charabia) | - | ![Crates.io](https://img.shields.io/crates/d/charabia) | ⭐ 358 | 🟢 august|
| 🔗 [gse](https://github.com/go-ego/gse) | - | - | ⭐ 2.8k | 🟢 last saturday|


## Language identification
テキストの言語を判定するライブラリ（判定対象に日本語を含む）

 * [fastText](https://github.com/facebookresearch/fastText) - 高速なテキスト表現と分類のためのライブラリ。
 * [lingua-py](https://github.com/pemistahl/lingua-py) - Python 向けの最も高精度な自然言語判定ライブラリで、短文や多言語混在テキストに適している。
 * [lingua](https://github.com/pemistahl/lingua) - Java および JVM 向けの最も高精度な自然言語判定ライブラリで、長文・短文のいずれにも適している。
 * [lingua-rs](https://github.com/pemistahl/lingua-rs) - Rust 向けの最も高精度な自然言語判定ライブラリで、短文や多言語混在テキストに適している。
 * [lingua-go](https://github.com/pemistahl/lingua-go) - Go 向けの最も高精度な自然言語判定ライブラリで、短文や多言語混在テキストに適している。
 * [langdetect](https://github.com/Mimino666/langdetect) - Google の language-detection ライブラリの Python 移植版。
 * [GlotLID](https://github.com/cisnlp/GlotLID) - [EMNLP 2023] 💬 2000以上のラベルに対応した言語識別。
 * [whatlang-rs](https://github.com/greyblake/whatlang-rs) - Rust 向けの自然言語判定ライブラリ。オンラインデモはこちら：https://whatlang.org/。
 * [franc](https://github.com/wooorm/franc) - 自然言語判定。
 * [whichlang](https://github.com/quickwit-oss/whichlang) - Rust 向けの非常に高速で軽量な言語判定ライブラリ。


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
日本語を含む言語ペアに対応した翻訳モデル・エンジン・サービス

 * [seamless_communication](https://github.com/facebookresearch/seamless_communication) - 最先端の音声・テキスト翻訳のための基盤モデル。
 * [argos-translate](https://github.com/argosopentech/argos-translate) - Python で書かれたオープンソースのオフライン翻訳ライブラリ。
 * [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) - 無料でオープンソースの機械翻訳API。セルフホスト可能で、オフライン対応かつ簡単にセットアップできる。
 * [Opus-MT](https://github.com/Helsinki-NLP/Opus-MT) - オープンなニューラル機械翻訳モデルとウェブサービス。
 * [Seed-X-7B](https://github.com/ByteDance-Seed/Seed-X-7B) - Seed-X は、7Bパラメータに収まる強力なオープンソースの多言語翻訳言語モデル群で、指示モデル・強化学習モデル・報酬モデルを含む。
 * [Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2) - Hy-MT2 は、複雑な実世界のシナリオ向けに設計された「高速思考」多言語翻訳モデル群で、1.8B・7B・30B-A3B の3サイズを展開。
 * [Hy-MT](https://github.com/Tencent-Hunyuan/Hy-MT) - Hunyuan 翻訳モデル バージョン1.5。1.8Bの翻訳モデル（HY-MT1.5-1.8B）と7Bの翻訳モデル（HY-MT1.5-7B）を含む。
 * [gemmax](https://github.com/xiaomi-research/gemmax) - Gemma ベースの多言語機械翻訳モデル。
 * [ALMA](https://github.com/fe1ixxu/ALMA) - 最先端のLLMベース翻訳モデル。


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
日本語に対応した多言語音声認識モデル・ツールキット・アライナー

 * [whisper](https://github.com/openai/whisper) - 大規模弱教師あり学習によるロバストな音声認識。
 * [whisper.cpp](https://github.com/ggml-org/whisper.cpp) - OpenAI の Whisper モデルの C/C++ 移植版。
 * [faster-whisper](https://github.com/SYSTRAN/faster-whisper) - CTranslate2 による高速な Whisper 文字起こし。
 * [whisperX](https://github.com/m-bain/whisperX) - WhisperX：単語レベルのタイムスタンプ（＆話者分離）を備えた自動音声認識。
 * [argmax-oss-swift](https://github.com/argmaxinc/argmax-oss-swift) - Apple Silicon 向けのオンデバイス音声AI。
 * [Qwen3-ASR](https://github.com/QwenLM/Qwen3-ASR) - Qwen3-ASR は、Alibaba Cloud の Qwen チームが開発したオープンソースの音声認識モデル群で、安定した多言語の音声・音楽・歌唱認識、言語判定、タイムスタンプ予測に対応。
 * [SenseVoice](https://github.com/QwenAudio/SenseVoice) - 北京語・広東語・英語・日本語・韓国語の音声認識、言語識別、感情認識、音響イベント検出に対応したオープンソースモデル SenseVoiceSmall。
 * [FunASR](https://github.com/modelscope/FunASR) - 学習・推論・ストリーミング音声認識・VAD・句読点付与・話者分離パイプライン、および OpenAI 互換/MCP 提供に対応したオープンソース音声認識ツールキット。
 * [omnilingual-asr](https://github.com/facebookresearch/omnilingual-asr) - Omnilingual ASR：1600以上の言語に対応したオープンソースの多言語音声認識。
 * [moonshine](https://github.com/moonshine-ai/moonshine) - 音声エージェントやインターフェースの構築に向けた、超低遅延の音声認識・意図認識・音声合成。
 * [Dolphin](https://github.com/DataoceanAI/Dolphin) - Dolphin は、DataoceanAI と清華大学が共同で学習した多言語・マルチタスク音声認識モデル。
 * [NeMo Speech](https://github.com/NVIDIA-NeMo/Speech) - 大規模言語モデル・マルチモーダル・音声AI（自動音声認識とテキスト読み上げ）に取り組む研究者・開発者向けに構築された、スケーラブルな生成AIフレームワーク。
 * [espnet](https://github.com/espnet/espnet) - エンドツーエンド音声処理ツールキット。
 * [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) - 次世代 Kaldi と onnxruntime を用いた、インターネット接続不要の音声認識・音声合成・話者分離・音声強調・音源分離・VAD。組み込みシステム、Android、iOS、HarmonyOS、Raspberry Pi、RISC-V、RK NPU、Axera NPU、Ascend NPU、x86_64サーバー、WebSocketサーバー/クライアントに対応し、12のプログラミング言語をサポート。
 * [icefall](https://github.com/k2-fsa/icefall) - icefall プロジェクトは、k2-fsa と lhotse を用いた各種データセット向けの音声関連レシピを収録。
 * [vosk-api](https://github.com/alphacep/vosk-api) - Android・iOS・Raspberry Pi・サーバー向けのオフライン音声認識API。Python・Java・C#・Node に対応。
 * [Montreal-Forced-Aligner](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) - Kaldi を用いた強制アラインメントのためのコマンドラインツール。
 * [Fun-ASR](https://github.com/QwenAudio/Fun-ASR) - Fun-ASR 音声認識モデル群。Fun-ASR-Nano は Hugging Face Transformers にネイティブ対応し、別途 FunASR・vLLM・llama.cpp によるデプロイ経路も提供。
 * [FluidAudio](https://github.com/FluidInference/FluidAudio) - アプリに組み込める最先端の CoreML 音声モデル ── 音声合成、音声認識、発話区間検出、話者分離。Swift 製で、最先端のオープンソースを活用。
 * [CrispASR](https://github.com/CrispStrobe/CrispASR) - 多言語の音声認識・音声合成モデル向けの C++（ggml）ランタイムハブ：Cohere Transcribe、Parakeet TDT、Voxtral、Canary 1B v2 など、さらに汎用の強制アラインメントなども提供。
 * [transcribe.cpp](https://github.com/handy-computer/transcribe.cpp) - 16以上のモデルファミリーに対応した ggml による音声認識推論。
 * [kaldi](https://github.com/kaldi-asr/kaldi) - kaldi-asr/kaldi は Kaldi プロジェクトの公式リポジトリ。
 * [julius](https://github.com/julius-speech/julius) - オープンソースの大語彙連続音声認識エンジン。


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
日本語を話せる多言語音声合成・声質クローンシステム

 * [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) - Qwen3-TTS は、Alibaba Cloud の Qwen チームが開発したオープンソースの音声合成モデル群で、安定した表現力豊かなストリーミング音声生成、自由な音声デザイン、生き生きとした声質クローンに対応。
 * [CosyVoice](https://github.com/QwenAudio/CosyVoice) - 多言語大規模音声生成モデルで、推論・学習・デプロイのフルスタック機能を提供。
 * [fish-speech](https://github.com/fishaudio/fish-speech) - 最先端のオープンソース音声合成。
 * [chatterbox](https://github.com/resemble-ai/chatterbox) - 最先端のオープンソース音声合成。
 * [coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) - 🐸💬 ── 研究・実運用の両方で実績のある、音声合成のためのディープラーニングツールキット。
 * [MeloTTS](https://github.com/myshell-ai/MeloTTS) - MyShell.ai による高品質な多言語音声合成ライブラリ。英語・スペイン語・フランス語・中国語・日本語・韓国語に対応。
 * [OpenVoice](https://github.com/myshell-ai/OpenVoice) - MIT と MyShell による即時声質クローン。音声基盤モデル。
 * [kokoro](https://github.com/hexgrad/kokoro) - https://hf.co/hexgrad/Kokoro-82M。
 * [bark](https://github.com/suno-ai/bark) - 🔊 テキストプロンプトによる生成音声モデル。
 * [Zonos](https://github.com/Zyphra/Zonos) - Zonos-v0.1 は、20万時間以上の多様な多言語音声で学習した最先端のオープンウェイト音声合成モデルで、トップクラスの音声合成プロバイダーに匹敵する、あるいはそれを上回る表現力と品質を実現。
 * [GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) - わずか1分の音声データでも、優れた音声合成モデルを学習できる！（少数サンプルによる声質クローン）
 * [Amphion](https://github.com/open-mmlab/Amphion) - Amphion（/æmˈfaɪən/）は、音声・音楽・発話生成のためのツールキット。再現可能な研究を支援し、若手研究者やエンジニアが音声・音楽・発話生成の研究開発分野に入るのを助けることを目的とする。
 * [index-tts](https://github.com/index-tts/index-tts) - 産業レベルで制御可能かつ効率的なゼロショット音声合成システム。
 * [VoxCPM](https://github.com/OpenBMB/VoxCPM) - VoxCPM2：トークナイザー不要の音声合成で、多言語音声生成・クリエイティブな音声デザイン・実物さながらの声質クローンを実現。
 * [Step-Audio-EditX](https://github.com/stepfun-ai/Step-Audio-EditX) - 強力な30億パラメータのLLMベース強化学習音声編集モデルで、感情・話し方・パラ言語情報の編集に優れ、堅牢なゼロショット音声合成機能も備える。
 * [FireRedTTS2](https://github.com/FireRedTeam/FireRedTTS2) - 複数話者の対話生成のための長尺ストリーミング音声合成システム。
 * [OuteTTS](https://github.com/edwko/OuteTTS) - OuteTTS モデルのインターフェース。
 * [MOSS-TTS](https://github.com/OpenMOSS/MOSS-TTS) - 長尺音声、対話合成、音声デザイン、効果音、リアルタイムストリーミング音声合成のためのオープンソースモデル群。
 * [MOSS-TTS-Nano](https://github.com/OpenMOSS/MOSS-TTS-Nano) - リアルタイムCPU推論、声質クローン、48kHzステレオ生成に対応した1億パラメータの多言語音声合成モデル。
 * [mlx-audio](https://github.com/Blaizzy/mlx-audio) - Apple の MLX フレームワーク上に構築された音声合成（TTS）・音声認識（STT）・音声変換（STS）ライブラリで、Apple Silicon 上で効率的な音声解析を実現。
 * [Genie-TTS](https://github.com/High-Logic/Genie-TTS) - GPT-SoVITS 用の ONNX 推論エンジン兼モデル変換ツール。
 * [MOSS-TTSD](https://github.com/OpenMOSS/MOSS-TTSD) - 柔軟な話者制御とゼロショット声質クローンを備えた、長尺・複数話者の対話音声合成のための多言語モデル。
 * [Confucius4-TTS](https://github.com/netease-youdao/Confucius4-TTS) - Confucius4-TTS：多言語・クロスリンガル対応のゼロショット音声合成エンジン。
 * [kani-tts](https://github.com/nineninesix-ai/kani-tts) - ニューラル音声コーデックと因果言語モデルを用いた音声合成。
 * [OmniVoice](https://github.com/k2-fsa/OmniVoice) - 600以上の言語に対応した高品質な声質クローン音声合成。
 * [T5Gemma-TTS](https://github.com/Aratako/T5Gemma-TTS) - T5Gemma エンコーダー・デコーダー型LLMをベースにした、声質クローンと発話時間制御に対応する多言語音声合成モデル。
 * [audio.cpp](https://github.com/0xShug0/audio.cpp) - ggml を基盤とした、音声モデル向けオールインワンの純粋な C++ 推論エンジン。音声合成・音声認識・VAD・声質変換・音楽生成などに対応し、高度に最適化された性能を持つ。Python 依存なし。


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
日本語の文字を扱える文字認識・文書解析ツール

 * [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - あらゆるPDFや画像ドキュメントをAI向けの構造化データに変換。画像・PDFとLLMの橋渡しをする、強力で軽量なOCRツールキット。100以上の言語に対応。
 * [tesseract](https://github.com/tesseract-ocr/tesseract) - Tesseract オープンソースOCRエンジン（メインリポジトリ）
 * [EasyOCR](https://github.com/JaidedAI/EasyOCR) - 80以上の言語と、ラテン文字・中国語・アラビア語・デーヴァナーガリー・キリル文字などの主要な文字体系に対応した、すぐに使えるOCR。
 * [surya](https://github.com/datalab-to/surya) - 90以上の言語に対応したOCR、レイアウト解析、読み順推定、表認識。
 * [chandra](https://github.com/datalab-to/chandra) - 複雑な表・フォーム・手書き文字をレイアウト全体を含めて処理できるOCRモデル。
 * [MinerU](https://github.com/opendatalab/MinerU) - PDFやOffice文書などの複雑なドキュメントを、エージェント型ワークフロー向けのLLM対応 Markdown/JSON に変換。
 * [RapidOCR](https://github.com/RapidAI/RapidOCR) - 📄 ONNX Runtime・OpenVINO・MNN・PaddlePaddle・TensorRT・PyTorch をベースにした、複数のプログラミング言語に対応する優れたOCRツールキット。
 * [Pix2Text](https://github.com/breezedeus/Pix2Text) - 小型モデルを用いたオープンソースの Python3 ツールで、画像内のレイアウト・表・数式（LaTeX）・テキストを認識し、Markdown 形式に変換する。Mathpix の無料代替として、視覚コンテンツをテキスト表現へシームレスに変換できる。80以上の言語に対応。
 * [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) - AI対応データのためのPDFパーサー。PDFアクセシビリティを自動化。オープンソース。
 * [TurboOCR](https://github.com/aiptimizer/TurboOCR) - TurboOCR、OmnidocBench で200枚/秒以上。TensorRT FP16、PP-OCRv6、HTTP + gRPC 対応。
 * [tesseract.js](https://github.com/naptha/tesseract.js) - 100以上の言語に対応した純粋な JavaScript 製OCR 📖🎉🖥。
 * [pdfminer.six](https://github.com/pdfminer/pdfminer.six) - コミュニティによってメンテナンスされている pdfminer のフォーク ── 私たちはPDFを解き明かす。
 * [PyMuPDF](https://github.com/pymupdf/PyMuPDF) - PyMuPDF は、PDF（およびその他の）文書のデータ抽出・解析・変換・操作を行う高性能な Python ライブラリ。


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
日本語に対応したモデルを使える埋め込みライブラリ、日本語の学習済み埋め込み、日本語インデックスを備えた検索ツールキット

 * [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) - Wikipedia から単語とエンティティのベクトル表現を学習するツール。
 * [pyserini](https://github.com/castorini/pyserini) - Pyserini は、疎表現・密表現による再現可能な情報検索研究のための Python ツールキット。
 * [sentence-transformers](https://github.com/huggingface/sentence-transformers) - 最先端の埋め込み・検索・リランキング。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wikipedia2vec](https://github.com/wikipedia2vec/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec/week)](https://pepy.tech/project/wikipedia2vec) | [![Downloads](https://static.pepy.tech/badge/wikipedia2vec)](https://pepy.tech/project/wikipedia2vec) | ⭐ 972 | 🔴 january 2024|
| 🔗 [pyserini](https://github.com/castorini/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini/week)](https://pepy.tech/project/pyserini) | [![Downloads](https://static.pepy.tech/badge/pyserini)](https://pepy.tech/project/pyserini) | ⭐ 2.2k | 🟢 last wednesday|
| 🔗 [sentence-transformers](https://github.com/huggingface/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers/week)](https://pepy.tech/project/sentence-transformers) | [![Downloads](https://static.pepy.tech/badge/sentence-transformers)](https://pepy.tech/project/sentence-transformers) | ⭐ 19k | 🟢 last wednesday|


## Full-text search
日本語アナライザーやトークナイザーを備えた検索エンジン・データベース

 * [lucene](https://github.com/apache/lucene) - Apache Lucene のオープンソース検索ソフトウェア。
 * [elasticsearch](https://github.com/elastic/elasticsearch) - 無料でオープンソースの、分散型 RESTful 検索エンジン。
 * [OpenSearch](https://github.com/opensearch-project/OpenSearch) - 🔎 オープンソースの分散型 RESTful 検索エンジン。
 * [solr](https://github.com/apache/solr) - Apache Solr のオープンソース検索ソフトウェア。
 * [meilisearch](https://github.com/meilisearch/meilisearch) - サイトやアプリケーションにAI駆動のハイブリッド検索をもたらす、超高速な検索エンジンAPI。
 * [typesense](https://github.com/typesense/typesense) - Algolia + Pinecone のオープンソース代替であり、ElasticSearch よりも使いやすい代替でもある ⚡ 🔍 ✨ 快適な検索体験を構築するための、高速でタイポに強いインメモリのあいまい検索エンジン。
 * [groonga](https://github.com/groonga/groonga) - 組み込み可能な全文検索エンジン。Groonga は Senna の後継プロジェクト。
 * [pgroonga](https://github.com/pgroonga/pgroonga) - PGroonga は、Groonga をインデックスとして利用する PostgreSQL 拡張機能。PGroonga により、PostgreSQL はあらゆる言語に対応した高速な全文検索プラットフォームになる！
 * [mroonga](https://github.com/mroonga/mroonga) - Groonga をベースにした MySQL 用のプラガブルストレージエンジン。
 * [pg_bigm](https://github.com/pgbigm/pg_bigm) - pg_bigm モジュールは PostgreSQL に全文検索機能を提供する。このモジュールにより、より高速な全文検索のための2-gram（バイグラム）インデックスを作成できる。
 * [paradedb](https://github.com/paradedb/paradedb) - アプリケーションデータ・全文検索・ベクトル検索・集計を1つの Postgres で。pg_search 拡張機能のホーム。
 * [weaviate](https://github.com/weaviate/weaviate) - Weaviate は、オブジェクトとベクトルの両方を保存するオープンソースのベクトルデータベース。クラウドネイティブなデータベースが持つ耐障害性とスケーラビリティを備えつつ、ベクトル検索と構造化フィルタリングを組み合わせられる。
 * [milvus](https://github.com/milvus-io/milvus) - Milvus は、スケーラブルなベクトル近似最近傍探索（ANN検索）のために構築された、高性能でクラウドネイティブなベクトルデータベース。
 * [qdrant](https://github.com/qdrant/qdrant) - Qdrant ── 次世代AIのための高性能・大規模ベクトルデータベース兼ベクトル検索エンジン。クラウド版（https://cloud.qdrant.io/）も利用可能。
 * [flexsearch](https://github.com/nextapps-de/flexsearch) - ブラウザと Node.js 向けの次世代全文検索ライブラリ。
 * [sonic](https://github.com/valeriansaliou/sonic) - 🦔 高速・軽量でスキーマレスな検索バックエンド。数MBのRAMで動作する、Elasticsearchの代替。
 * [orama](https://github.com/oramasearch/orama) - 🌌 ブラウザ・サーバー・エッジネットワーク上で動く、完全な検索エンジン兼RAGパイプライン。2kB未満で全文検索・ベクトル検索・ハイブリッド検索に対応。
 * [pagefind](https://github.com/Pagefind/pagefind) - 大規模な静的サイト向けの低帯域幅検索。
 * [lancedb](https://github.com/lancedb/lancedb) - マルチモーダルAI向けの、開発者に優しいオープンソースの組み込み型検索ライブラリ。「もっと検索を、もっと少ない管理を」。
 * [bleve](https://github.com/blevesearch/bleve) - Go 向けの、テキスト・数値・地理空間・ベクトルに対応したモダンな索引ライブラリ。
 * [lunr-languages](https://github.com/MihaiValentin/lunr-languages) - 検索ライブラリ Lunr（JavaScript）向けの、各言語のステマーとストップワードのコレクション。


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
日本語のルールやデータを備えたテキスト正規化・ローマ字化・読み変換（G2P）ツール

 * [NeMo-text-processing](https://github.com/NVIDIA/NeMo-text-processing) - 音声認識・音声合成のための NeMo テキスト処理。
 * [WeTextProcessing](https://github.com/wenet-e2e/WeTextProcessing) - テキスト正規化と逆テキスト正規化。
 * [misaki](https://github.com/hexgrad/misaki) - G2P（書記素から音素への変換）。
 * [espeak-ng](https://github.com/espeak-ng/espeak-ng) - eSpeak NG は、100以上の言語・アクセントに対応したオープンソースの音声合成エンジン。
 * [epitran](https://github.com/dmort27/epitran) - 正書法のテキストをIPA（国際音声記号）に変換するツール。
 * [uroman](https://github.com/isi-nlp/uroman) - あらゆる Unicode 文字体系をローマ字（ラテン文字）に変換できる汎用ローマ字化ツール。
 * [num2words](https://github.com/savoirfairelinux/num2words) - 数値を単語に変換するモジュール。42 --> forty-two。
 * [dateparser](https://github.com/scrapinghub/dateparser) - 人が読める形式の日付を解析する Python パーサー。
 * [ipa-dict](https://github.com/open-dict-data/ipa-dict) - IPA による発音情報付きの単言語単語リスト。
 * [Recognizers-Text](https://github.com/microsoft/Recognizers-Text) - Microsoft.Recognizers.Text は、複数言語（中国語・英語・フランス語・スペイン語・ポルトガル語・ドイツ語・イタリア語・トルコ語・ヒンディー語・オランダ語。日本語・韓国語・アラビア語・スウェーデン語は部分対応）で、数値・単位・日時などの認識と解決を行う。パッケージ：https://www.nuget.org/profiles/Recognizers.Text 、https://www.npmjs.com/~recognizers.text 。
 * [chrono](https://github.com/wanasit/chrono) - JavaScript による自然言語の日付パーサー。


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
日本語向けの設定を備えた評価ツールと、日本語を含む多言語データセット

 * [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) - 言語モデルのfew-shot評価のためのフレームワーク。
 * [mteb](https://github.com/embeddings-benchmark/mteb) - MTEB：言語とモダリティを横断した、埋め込みの最先端評価。
 * [sacrebleu](https://github.com/mjpost/sacrebleu) - テストセットを自動ダウンロードし、研究機関間の比較を容易にするバージョン文字列を出力する、標準的な BLEU 実装。
 * [xtreme](https://github.com/google-research/xtreme) - XTREME は、事前学習済み多言語モデルの言語横断的な汎化能力を評価するためのベンチマークで、類型的に多様な40言語をカバーし、9つのタスクを含む。
 * [belebele](https://github.com/facebookresearch/belebele) - 大規模多言語読解データセット Belebele のリポジトリ。
 * [miracl](https://github.com/project-miracl/miracl) - 情報検索のための大規模多言語データセット。18の多様な言語にわたる、徹底した人手アノテーション。
 * [mr.tydi](https://github.com/castorini/mr.tydi) - Mr. TyDi は、TyDi をベースに構築された多言語ベンチマークデータセットで、類型的に多様な11言語をカバーする。
 * [tydiqa](https://github.com/google-research-datasets/tydiqa) - TyDi QA は、類型的に多様な11言語で作成された20万件の人手アノテーション付き質問応答ペアを収録し、回答を見ずかつ翻訳を用いずに作成されており、自動質問応答システムの学習・評価のために設計されている。このリポジトリは、このデータセット向けの評価コードとベースラインシステムを提供する。
 * [ml-mkqa](https://github.com/apple-aiml-research/ml-mkqa) - オープンドメイン質問応答の評価セット MKQA を紹介する。類型的に多様な26言語にわたって整列された1万件の質問応答ペア（合計26万件）から成る。このデータセットの目的は、幅広い言語における質問応答品質の困難なベンチマークを提供することである。詳細は論文「MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering」を参照。
 * [massive](https://github.com/alexa/massive) - MASSIVE データセット向けのツールとモデリングコード。
 * [paws](https://github.com/google-research-datasets/paws) - このデータセットには、10万8,463件の人手ラベル付きペアと65万6,000件のノイズを含むラベル付きペアが含まれており、言い換え識別の課題において構造・文脈・語順情報をモデル化することの重要性を示している。
 * [xl-sum](https://github.com/csebuetnlp/xl-sum) - このリポジトリには、ACL-IJCNLP 2021 の Findings of the Association for Computational Linguistics に掲載された論文「XL-Sum: Large-Scale Multilingual Abstractive Summarization for 44 Languages」のコード・データ・モデルが含まれる。
 * [url-nlp (MGSM)](https://github.com/google-research/url-nlp) - MGSM は、論文「Language models are multilingual chain-of-thought reasoners」で提案された、小学校レベルの算数問題からなるベンチマーク。
 * [M-IFEval](https://github.com/lightblue-tech/M-IFEval) - このリポジトリには、M-IFEval：多言語指示追従評価のソースコードとデータが含まれる。
 * [mintaka](https://github.com/amazon-science/mintaka) - 論文「Mintaka: A Complex, Natural, and Multilingual Dataset for End-to-End Question Answering」（COLING 2022）によるデータセット。
 * [Wikilingua](https://github.com/esdurmus/Wikilingua) - WikiHow から抽出した多言語抽象型要約データセット。


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
日本語固有の処理を備えたコーパス処理・単語頻度・語彙データベースのツール

 * [datatrove](https://github.com/huggingface/datatrove) - プラットフォームに依存しないカスタマイズ可能なパイプライン処理ブロック群を提供することで、データ処理をスクリプトの混沌から解放する。
 * [Wordless](https://github.com/BLKSerene/Wordless) - 言語・文学・翻訳研究のための、多言語対応の統合コーパスツール。
 * [wordfreq](https://github.com/rspeer/wordfreq) - さまざまな自然言語の単語頻度データベースにアクセスできる。
 * [wn](https://github.com/goodmami/wn) - Python 向けの、モダンで言語横断的なワードネットインターフェース。
 * [wiktextract](https://github.com/tatuylonen/wiktextract) - Wiktionary のダンプファイルパーサー兼多言語データ抽出ツール。
 * [scattertext](https://github.com/JasonKessler/scattertext) - 文書の種類によって言語がどのように異なるかを美しく可視化。
 * [sumy](https://github.com/miso-belica/sumy) - テキスト文書や HTML ページを自動要約するモジュール。
 * [textlint](https://github.com/textlint/textlint) - textlint は、自然言語テキストのためのプラガブルな校正ツール。


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

