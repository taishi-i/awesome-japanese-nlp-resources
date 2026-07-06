# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語向けのNLPに関する、Pythonライブラリ、LLM、辞書、コーパスに特化したリソースを厳選してまとめた一覧です。
このページでは、Hugging Faceで利用可能な日本語NLP特化のモデルとデータセットを掲載しています。現在、171件のモデルと133件のデータセットが含まれています。

_2026年7月6日更新_

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)

## Contents
 * [Ranking](#Ranking)
   * [Models](#models-ranking)
   * [Datasets](#datasets-ranking)
 * [Models](#Models)
   * [text-generation](#text-generation)
   * [fill-mask](#fill-mask)
   * [sentence-similarity](#sentence-similarity)
   * [automatic-speech-recognition](#automatic-speech-recognition)
   * [feature-extraction](#feature-extraction)
   * [text-ranking](#text-ranking)
   * [translation](#translation)
   * [image-to-text](#image-to-text)
   * [token-classification](#token-classification)
   * [text-classification](#text-classification)
   * [text-to-speech](#text-to-speech)
   * [any-to-any](#any-to-any)
   * [audio-to-audio](#audio-to-audio)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | モデル名 | Downloads | Likes | カテゴリ |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 6M | ⭐ 61 | automatic-speech-recognition |
| 2 | [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) | 📥 2M | ⭐ 39 | fill-mask |
| 3 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 758k | ⭐ 15 | translation |
| 4 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 682k | ⭐ 81 | sentence-similarity |
| 5 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 481k | ⭐ 9 | fill-mask |
| 6 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 417k | ⭐ 176 | image-to-text |
| 7 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 390k | ⭐ 76 | fill-mask |
| 8 | [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) | 📥 358k | ⭐ 5 | text-ranking |
| 9 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 299k | ⭐ 15 | text-generation |
| 10 | [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) | 📥 280k | ⭐ 14 | text-ranking |
| 11 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 219k | ⭐ 10 | sentence-similarity |
| 12 | [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) | 📥 216k | ⭐ 115 | automatic-speech-recognition |
| 13 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 213k | ⭐ 41 | fill-mask |
| 14 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 187k | ⭐ 12 | translation |
| 15 | [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) | 📥 133k | ⭐ 24 | sentence-similarity |
| 16 | [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) | 📥 133k | ⭐ 56 | feature-extraction |
| 17 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 122k | ⭐ 11 | others |
| 18 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 98k | ⭐ 59 | text-generation |
| 19 | [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) | 📥 76k | ⭐ 64 | others |
| 20 | [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) | 📥 70k | ⭐ 6 | fill-mask |

### Datasets-ranking

| # | データセット名 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 2M | ⭐ 62 |
| 2 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 14k | ⭐ 9 |
| 3 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 12k | ⭐ 32 |
| 4 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 8k | ⭐ 7 |
| 5 | [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) | 📥 6k | ⭐ 17 |
| 6 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 5k | ⭐ 35 |
| 7 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 5k | ⭐ 11 |
| 8 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 5k | ⭐ 121 |
| 9 | [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) | 📥 3k | ⭐ 5 |
| 10 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 3k | ⭐ 47 |
| 11 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 3k | ⭐ 49 |
| 12 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 99 |
| 13 | [Lux-Japanese-Speech-Corpus](https://huggingface.co/datasets/Lami/Lux-Japanese-Speech-Corpus) | 📥 2k | ⭐ 5 |
| 14 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 2k | ⭐ 7 |
| 15 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 2k | ⭐ 18 |
| 16 | [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) | 📥 2k | ⭐ 24 |
| 17 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 2k | ⭐ 141 |
| 18 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 1k | ⭐ 20 |
| 19 | [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) | 📥 1k | ⭐ 18 |
| 20 | [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) | 📥 1k | ⭐ 8 |

## Models
### text-generation
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 299k / ⭐ 15 / CC‑100、C4、Wikipedia で学習された12‑layer、768‑hidden の日本語 GPT‑NeoX モデル。Huggingface と互換性があり、各文の末尾に必ず笑顔の絵文字を付けるオプションのトイプレフィックス調整ウェイトが付属しています。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 98k / ⭐ 59 / 2.7Bパラメータの日本語 GPT‑NeoX モデルは、ABEJA Inc. が日本語 CC‑100 と OSCAR で学習し、Hugging Face Transformers パイプラインまたは PyTorch で利用可能で、MIT license の下で公開されています。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 51k / ⭐ 42 / NIIから提供される8 BパラメータのLLM‑jp‑4‑8b‑thinking日本語言語モデルを、pre-/mid‑trainingで訓練し、SFT/DPOで調整済みとして、torch‑transformersで使用可能かつ詳細なクックブック指示付きで提供します。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 50k / ⭐ 8 / 「LLM‑jp‑3‑150m」は、情報学研究所のLLM R&D Centerが開発した150Mパラメータを有する日本語言語モデルです。Hugging Face Transformers形式で配布され、torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8 が必要です。Japanese Wikipedia、Common Crawl、WARP/PDF、WARP/HTML、Kaken データを使用し、unigram byte‑fallback tokenizer で事前学習されています。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 45k / ⭐ 36 / 32億パラメータの日本語トランスフォーマーLLM（llm‑jp‑4‑32b‑a3b‑thinking）は、国立情報学研究所（National Institute of Informatics）からのもので、教師付きファインチューニングと直接的な好み最適化（direct preference optimization）を用いてプリトレーニングと整合化されました。強化学習は使用していません。ユニグラム・バイトフォールバック・トークナイザー（unigram byte‑fallback tokenizer）を採用しています。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 32k / ⭐ 139 / 9 billionパラメータの日本語最適化LLM、NVIDIA Nemotron‑Nano‑9B‑v2‑Japaneseは、2024年9月までのデータでハイブリッド Mamba-2/MLP/4-layer-attentionアーキテクチャを用いて学習され、Nemotron-Personas-Japan tool‑callingデータセットでファインチューニングされます。最終回答を生成する前に制御可能な推論トレースをオプションで生成でき、商用利用が可能です。
 * [Llama-3.3-Swallow-70B-Instruct-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-Instruct-v0.4) - 📥 24k / ⭐ 13 / Llama 3.3 Swallowは、MetaのLlama 3.3を継続的なプレトレーニングとインストラクション調整によるファインチューニングで構築された70ビリオンドーパラメータの日本語強化大型言語モデルです。複数のバリアント（例：v0.4）がHugging FaceおよびSwallowウェブサイトで公開されています。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 20k / ⭐ 21 / OpenCALM は、decoder‑only 日本語 Transformer 言語モデル（160 M〜6.8 B パラメータ）のスイートで、CyberAgent, Inc. によって CC‑BY‑SA 4.0 の下でリリースされました。日本語 Wikipedia と Common Crawl でトレーニングされ、Hugging Face の torch‑transformers を通じて利用可能です。
 * [LFM2.5-1.2B-JP-202606](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606) - 📥 18k / ⭐ 63 / LFM 2.5‑1.2B‑JP‑202606 は、高性能で汎用性のある日本語チャットモデルです。知識、指示従順性、数学、コード、およびツール使用において、同等のサブ-2 B モデルを上回るため、日本語アプリケーションの文化的ニュアンスを重視する開発者に最適です。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 12k / ⭐ 7 / 日本語で事前学習済み TinyLlama (≈50 k ステップ) は、約3 B OSCAR/mC4トークンで構築され、HuggingFace Transformers または VLLM で使用可能です。Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru、Renju Aoki が作成しました。
 * [LFM2.5-1.2B-JP-202606-ONNX](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-ONNX) - 📥 12k / ⭐ 1 / 日本語版 LFM2.5‑1.2B モデルを ONNX にエクスポートし、ONNX Runtime、Transformers.js、および WebGPU でのクロスプラットフォーム推論を可能にします。FP32、FP16、INT4/FP16 混合など複数の精度バリアントが用意されており、WebGPU に適した INT4+FP16 フォーマットを推奨しています
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 12k / ⭐ 39 / SB Intuitionsから提供される自己回帰型日本語モデル（sarashina2.2‑3B‑instruct‑v0.1）を、他のモデルとベンチマークし、使用例スクリプト付きで提供。安全性トレーニングは限定的である旨の注意書きが付いています。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 11k / ⭐ 17 / 日本語大規模言語モデル（1.8 b から 172 b beta1、インストラクションバリアント付き）のコレクションで、NIIの研究開発センターから提供され、Hugging Face Transformers 形式でパッケージ化され、1兆語以上の日本語・英語・Web コーパスを混合して事前学習されています。torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5 が必要です。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 9k / ⭐ 10 / llm‑jp‑4‑8b‑instructは、NIIのLLM‑jp‑4シリーズからの4.1 Bパラメータを持つ日本語LLMで、大規模コーパスで事前学習され、次に教師付き指示データのみでファインチューニングされ（DPO/REINFORCEは使用していない）、料理本スタイルの使用ガイドとbyte‑fallbackユニグラムトークナイザーが付属します。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 9k / ⭐ 2 / Qwen3‑Swallow v0.2 は、CPT、SFT、および RLVR で訓練された 30‑B と 32‑B の日本語‑英語バイリンガル LLM を提供し、日本語の正確性、翻訳、数学、コーディングを向上させて、オリジナルの Qwen3 と同等または上回ります。9 本のモデル（CPT、SFT、RL）および AWQ 量子化版を含み、GPT‑OSS‑Swallow もリリースされています。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 9k / ⭐ 21 / Llama3 Swallowは、2024年7月1日にリリースされた、日本語拡張のMeta Llama 3ファミリーで、Instructとchat形式の8Bおよび70Bバリアントを提供し、SFTとChat VectorでMegatron‑LM上で微調整され、主要な日本語NLPタスクでベンチマークされている。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 8k / ⭐ 85 / Rinnaの24層、1024ユニットの日本語GPT‑2‑mediumモデルは、CC‑100とWikipediaをSentencePieceトークナイゼーションで学習され、rinna/japanese‑pretrained‑modelsリポジトリで入手できます（MITライセンス、2021年4月7日リリース、2021年8月25日更新）。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 8k / ⭐ 19 / Llama 3.1 Swallowは、MetaのLlama 3.1の事前学習を継続して日本語性能を向上させ、合成日本語データで指示ファインチューニングを行う8‑Bおよび70‑Bモデルのセットです。これにより、gemma‑3‑27b‑itと同等の会話挙動を備えた複数のリリースバリアントが提供されます。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 実験的な日本語モデルは、lightblue/suzume‑llama‑3‑8B‑japanese と Meta‑Llama‑3‑8B‑Instruct の違いを chat‑vector approach を使って抽出し、upsampled して Meta‑Llama‑3‑70B‑Instruct に適用した結果、ほとんど変更がなく、将来のスケーリング計画を立てている。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 7k / ⭐ 149 / Llama‑3‑ELYZA‑JP‑8B は、ELYZA によって開発された日本語強化版で、8 billion パラメータ（80億）を持つ Llama 3 モデルで、Meta‑Llama‑3‑8B‑Instruct 上で日本語用に微調整されています。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 6k / ⭐ 10 / リポジトリは、Massed Compute ハードウェアで作成され、TheBloke の a16z ファンド付き LLM 仕事の一部として、Stability AI の日本語 StableLM Instruct Gamma 7B の GGUF 形式で量子化されたモデルファイルを提供します。
 * [LFM2.5-1.2B-JP-202606-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-GGUF) - 📥 6k / ⭐ 21 / Liquid AI の Hybrid LFM2 モデル（例：1.2 B 日本語 GGUF バージョン）は、高品質で高速、かつメモリ効率の良いエッジAIをオンデバイス展開に提供し、Hugging Face リポジトリ経由で llama.cpp を使ってローカル実行できます。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 6k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b は、Meta の Llama‑2 モデルの 6.27B パラメータ拡張で、インストラクトとファストバリアントで日本語データ上で事前学習され、Hugging Face Transformers を通じて利用できるものです。
 * [Qwen3-Swallow-8B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2-AWQ-INT4) - 📥 5k / ⭐ 1 / Qwen3‑Swallow v0.2 は、Continual Pre‑Training、Supervised Fine‑Tuning、および Reinforcement Learning with Verifiable Rewards を通じて Qwen3 上に構築されたバイリンガル日本語-英語 30B‑A3B と 32B モデルを提供し、日本語の熟練度、翻訳、数学およびコーディング推論を向上させつつ、コア Qwen3 のパフォーマンスを維持し、いくつかの量子化バリアントを備えています。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 5k / ⭐ 24 / Llama 3.1 Swallowは、継続的なプレトレーニングと日本語特有のインストラクションファインチューニングで訓練された8B / 70B Llama 3.1モデルの日本語強化シリーズです。最新の8B‑Instruct‑v0.3は、日本語MT‑Benchで最先端の結果を示しています。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 4k / ⭐ 6 / 8.6 Bパラメータの llm-jp-4-8b-base トランスフォーマーをホストするリポジトリ。  
National Institute of Informatics の LLM R&D Center で事前学習・ミドルトレーニングを経て、監督付きファインチューニングと直接的な好み最適化（強化学習は使用していない）で訓練され、PyTorch-transformers の使用ガイドを提供しています。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 4k / ⭐ 27 / rinnaの日本語GPT‑2 smallは、12層、768ユニットの隠れ層を持つtransformerで、日本語CC‑100とWikipediaをデータとして学習され、SentencePieceでトークナイズされ、MITライセンスのもとで2021年8月25日にリリースされました（Hugging Face: rinna/japanese‑gpt2‑small、詳細は https://arxiv.org/abs/2404.01657 を参照）。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 4k / ⭐ 15 / SB Intuitionsの Sarashina2.2‑0.5B instruct v0.1は、5億パラメータの日本語オートレグレッシブモデルで、日本語と英語のMTベンチマークで良好な性能を示し、torch-transformers経由でロード可能です。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 3k / ⭐ 35 / TinySwallow‑1.5Bは、Sakana AIとSwallow Teamによるコンパクトな日本語指示‑フォロー型言語モデルで、Qwen2.5‑32B‑InstructからのTAID蒸留を利用し、さらに日本語テキストで事前学習が追加され、研究利用のみを目的としてApache 2.0でリリースされています。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 3k / ⭐ 11 / Qwen3‑Swallow v0.2は、日本語―英語のLLM（30B‑A3B と 32B）を提供し、CPT、SFT、RLVR によってトレーニングされ、強力な数式・コーディング・推論能力を保持し、9 つのリリース済みモデルと AWQ 量子化バリアントを備えています。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 3k / ⭐ 49 / 日本語で継続的にプレトレーニングされたMistral‑Nemoモデル（Mistral‑Nemo‑Japanese‑Instruct‑2408）は、mistralai/Mistral‑Nemo‑Instruct‑2407 を基に構築され、device mapping と ChatML プロンプトを備えた transformers で利用可能で、Apache‑2.0 ライセンスの下で Ryo Ishigami により公開されました。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 3k / ⭐ 21 / NIIから提供される1.8 Bパラメータのllm‑jp‑3.1‑1.8b‑instruct4日本語指示‑調整モデルは、Hugging Face TransformersおよびTorch ≥ 2.3.0に互換性があり、事前学習済みと微調整済みのチェックポイント、ならびに使用例を含みます。
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 3k / ⭐ 12 / 東京Tech-LLM が開発した大規模言語モデルは、LLaMA‑2 をベースに日本語データ（SFT）で微調整されており、Swallow‑7b/13b/70b のバリアントとその instruct, NVE、および “plus” バージョンが 2023年12月から 2024年4月までにリリースされています。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 3k / ⭐ 21 / OpenCALMは、CyberAgentが開発した日本語専用のデコーダオンリートランスフォーマー言語モデル（160 M〜6.8 Bパラメータ）のファミリーです。日本語のWikipediaとCommon Crawlで学習され、CC BY‑SA 4.0の下でリリースされています。
 * [LFM2-350M-PII-Extract-JP](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP) - 📥 2k / ⭐ 56 / LFM2‑350M‑PII‑Extract‑JP は、350 millionパラメータを備えたオンデバイスの日本語 PII‑extraction モデルで、GPT‑5 と同等の性能を実現し、契約書、メール、医療レポートにおける機密データのマスキングを可能にします。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 2k / ⭐ 25 / Hugging Face‑互換の日本語中心のトランスフォーマーモデル（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct）は情報学研究所から提供され、Wikipedia、Common Crawl、WARP、Kaken、Dolma を含む多様な日本語・英語コーパスで事前学習されており、torch ≥ 2.3、transformers ≥ 4.40、accelerate、flash‑attn を必要とします。
 * [llm-jp-3-1.8b-instruct3](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct3) - 📥 2k / ⭐ 2 / Repository は llm‑jp‑3‑1.8b‑instruct3 をホストしており、これは国立情報学研究所の 1.8 b パラメータ日本語 LLM で、日本語 Wikipedia と Common Crawl で事前学習されており、Hugging Face Transformers（torch ≥ 2.3, transformers ≥ 4.40）で使用可能です。
 * [llm-jp-3-150m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-150m-instruct3) - 📥 2k / ⭐ 4 / 日本の国立情報学研究所（Japan’s National Institute of Informatics）から提供される150‑M‑parameter Instructional LLM は、torch ≥ 2.3.0 と transformers ≥ 4.40.1 を必要とする Hugging Face 互換の Transformer モデルとして利用可能です。
 * [Wanabi-Gemma4-31B-GGUF](https://huggingface.co/kawaimasa/Wanabi-Gemma4-31B-GGUF) - 📥 2k / ⭐ 5 / GoogleのGemma 4 31BをファインチューニングしたGGUFバージョンで、Project Wannabeの構造化プロンプト形式と日本語創作ライティングに最適化されており、一般的な対話や推論機能も保持しています。
 * [japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - 📥 2k / ⭐ 74 / 3.6 B パラメータの日本語 GPT‑NeoX モデル（36層、2816次元の隠れ層を持つトランスフォーマー）は、翻訳された Anthropic データで PPO‑based RLHF によって訓練され、指示スタイルの会話に従い、約30 ％のヒューマンベースの PPO 勝率と34 ％の ChatGPT ベースの PPO 勝率を示すが、繰り返しテキストを生成する傾向がある。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 2k / ⭐ 17 / TokyoTech‑LLM リポジトリは、Swallow Llama‑2 ファミリーの LLaMA‑2 モデルを提供しており、日本語データで拡張された 7B、13B、70B バリアントを含みます。これらには instruction‑tuned、NVE‑tuned、7B Plus バージョンがあり、2023年12月以降にリリースされました。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 148 / LFM2.5‑1.2B‑JPは日本語最適化されたチャットモデルで、LFM2より日本語知識と指示に従う能力で優れ、LoRAによるファインチューニング、Transformers、vLLM、llama.cppを使った推論をサポートし、50.7 JMMLU、58.1 M‑IFEval、56.0 GSM8Kのスコアを達成しています。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 58 / TinySwallow‑1.5B‑Instruct は、TAID を用いて Qwen2.5‑32B‑Instruct から蒸留された 1.5 B の日本語インストラクション調整済みオートレグレッシブ言語モデルであり、研究目的のみに利用されることを想定しています。
 * [sarashina2.2-1b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1) - 📥 2k / ⭐ 16 / このリポジトリは、SB Intuitions の 1 B‑パラメータ自動回帰日本語指示モデル sarashina2.2‑1b‑instruct‑v0.1 をホストし、他の日本語‑BERT と比較して日本語と英語の MT と指示タスクでベンチマークを行っています。さらに、torch‑transformer の使用例と安全性トレーニングが限定的である旨の警告も付録として含まれています。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 2k / ⭐ 15 / LLM‑jp は 13 B と 1.3 B の transformer 言語モデルを提供しています。複数の指示チューニング済みバリアントを含むモデルは、Megatron‑DeepSpeed および Hugging Face Transformers エコシステムで構築されています。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 2k / ⭐ 16 / 6層、512ユニットの隠れ層を持つトランスフォーマーで、Japanese GPT‑2 xSmall と呼ばれ、Japanese CC‑100 および Wikipedia を SentencePiece でトークナイズして学習された。2021年8月25日に MIT ライセンスで公開され、Hugging Face（rinna/japanese‑gpt2‑xsmall）にホストされ、arXiv 2404.01657 で引用されている。
 * [gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - 📥 1k / ⭐ 18 / 大型の日本語 GPT‑2 モデルは、ABEJA, Inc. が Japanese CC‑100、Wikipedia、OSCAR でトレーニングし、sentencepiece でトークナイズされ、MIT ライセンスの下で PyTorch または TensorFlow で Hugging Face transformers を通じて利用できます。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking-gguf) - 📥 1k / ⭐ 8 / LLM‑jp‑4‑8b‑thinking‑gguf は、情報科学研究所から提供される約 8 B パラメータの日本語大規模言語モデルであり、ミッドトレーニングのみで事前学習し、「思考」バリアント向けに教師付き学習と直接的好み最適化（DPO）で微調整されています。GGUF 形式で利用可能で、詳細な使用手順はクックブックに記載されています。
 * [Sakura-13B-Galgame-GGUF](https://huggingface.co/QuantFactory/Sakura-13B-Galgame-GGUF) - 📥 1k / ⭐ 2 / 量子化されたオフライン対応の Galgame/軽小説翻訳モデル（Sakura-13B-Galgame-GGUF）は、llama.cppで構築されており、GPT‑3.5レベルの性能、OpenAI‑API互換性を提供し、Qwen/Qwen2ベースに基づく複数のGGUFバリアントがあります。CC BY‑NC‑SA 4.0の下でリリースされており、非商用利用に対する使用警告が付いています。
 * [open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - 📥 1k / ⭐ 4 / OpenCALM は CyberAgent の日本語デコーダーのみトランスフォーマー言語モデルスイートで、パラメータ数は 160 M から 6.8 B まであり、日本語 Wikipedia と Common Crawl で訓練され、CC BY‑SA 4.0 の下でリリースされています。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 1k / ⭐ 30 / LFM2.5‑1.2B‑JPは、LFM2.5ハイブリッドアーキテクチャ上に構築された1.2 Bパラメータの日本語テキスト生成モデルで、生成と完了タスク向けに最適化され、Hugging Faceにホストされ、llama.cpp経由で実行可能です。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 1k / ⭐ 108 / 1.3Bパラメータ、24層のトランスフォーマー GPT-1Bは、日本語C4、CC-100、およびWikipediaで学習され、rinna Co. によって2022年1月26日にリリースされ、MITライセンスの下で利用可能です。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 1k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 は、13‑B の指示事前学習済み日本語言語モデルで、NII の R&D Center によって開発され、Hugging‑Face Transformers のチェックポイントとして UNIGRAM‑byte‑fallback トークナイザー付きで公開されました。

### fill-mask
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 2M / ⭐ 39 / Japanese‑Roberta‑Base は rinna Co., Ltd. が開発した事前学習済みのマスク言語モデルで、正しいロード方法、トークン前処理、位置ID処理、および使用例に関するガイドラインがあり、先頭に `[CLS]` トークンが必要であることと、一貫したトークン化を強調しています。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 481k / ⭐ 9 / 171 GBの日本語Wikipedia、CC‑100、OSCARでトレーニングされた日本語DeBERTa V2 large modelは、文字レベルのsentencepieceトークナイズと全単語マスキングを使用し、Hugging Face Transformersを通じて下流でのファインチューニングに準備できています。
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 390k / ⭐ 76 / 2019年の日本語Wikipediaを対象に、IPA辞書と全単語マスキングを用いて事前学習されたJapanese BERT‑base、12層、768次元、32,000語語彙、512トークンシーケンス、1Mステップ、CC‑BY‑SAの下でcl‑tohoku/bert‑japaneseから入手可能。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 213k / ⭐ 41 / 約17 Mの日本語Wikipedia文（2.6 GB）で事前学習済みのBERT base modelで、IPA dictionaryとWordPieceでトークナイズし、12層／768-dim hidden states／12 headsを有し、32 000-token vocabularyを備え、1 MステップでCloud TPUs上で訓練され、CC‑BY‑SA 3.0でリリースされています。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 70k / ⭐ 6 / BERT‑base Japanese model（12層、768‑次元の hidden states、12ヘッド）を、30 M Wikipedia 文（約4 GB）で Unidic 2.1.2 を用いた単語レベルトークン化の後、文字レベルトークン化と全単語マスクを行い、512トークンのシーケンス、256バッチ、1 M トレーニングステップで訓練しました。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 16k / ⭐ 25 / ModernBERT‑Ja‑310M は local‑global attention と RoPE を組み合わせた日本語 BERT 変種で、4.09 T tokens の日本語／英語テキストで訓練され、102 400語の語彙、8 192トークンのシーケンスをサポートし、Flash Attention 2 用に最適化されています。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 14k / ⭐ 49 / LINE DistilBERT Japanese は、インハウスの BERT‑base 先生を用いて 131 GB の日本語ウェブテキストで事前学習された 66 百万パラメータの DistilBERT モデルであり、JGLUE で評価され、MeCab Unidic と SentencePiece でトークナイズされ、Apache 2.0 ライセンスの下でリリースされました。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 13k / ⭐ 49 / 132 Mパラメータの日本語 ModernBERT モデルで、ローカルグローバルとRoPE注意を組み合わせ、4.39 T トークン（日本語/英語）で訓練され、102 kサイズの語彙、最大8,192トークン長、Flash Attention 2 に最適化されています
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 11k / ⭐ 8 / 日本語のBERT‑baseモデル（12層、768次元の隠れレイヤー、12ヘッド）は、MeCab IPA単語レベルトークン化を経て文字レベルトークン化で4000語語彙に変換し、約1700万文（2.6 GB）の日本語Wikipediaで事前学習されました。学習コードはcl‑tohoku/bert‑japaneseにあり、CC BY‑SA 3.0 でリリースされています。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 8k / ⭐ 26 / Japanese BERT‑base (12 layers, 768 hidden, 12 heads) は、Unidic 2.1.2 単語レベルトークナイゼーション、WordPiece サブトークナイズ、および whole‑word マスクリングを使用し、4 GBの日本語Wikipedia（約30 M文）で事前学習されています。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 4k / ⭐ 5 / DeBERTaV2 base は日本語コーパス（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）でトレーニングされ、FP‑16 ファインチューニングで NLU タスク（JSTS、JNLI、JCommonsenseQA）に適用され、CC BY‑SA 4.0 の下でリリースされ、日本の研究助成金で資金提供されました。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 4k / ⭐ 7 / ModernBERT‑Ja‑30Mは、ローカルおよびグローバル注意機構をRoPEと組み合わせた日本語BERTバリアントです。4.39 TBの日本語／英語テキストで訓練され、8,192トークンのシーケンスをサポートし、30 Mから130 Mパラメータのサイズで提供され、Flash Attention 2との組み合わせで最も効果的です。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 3k / ⭐ 30 / 日本語 DeBERTa V2 ベースモデルは、171 GBの日本語 Wikipedia、CC‑100、OSCAR データを用いて Juman++ セグメンテーションと SentencePiece トークン化で事前学習され、8枚の NVIDIA A100 GPU を 3週間使用してトレーニングされ、ファインチューニングに向けて準備ができています。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 3k / ⭐ 1 / 日本語のDeBERTa‑V2ベースモデルで、171 GBの日本語Wikipedia、CC‑100、およびOSCARテキストをキャラクターレベルトークン化とワードレベルマスクで事前学習し、8台のA100 GPUで20日間訓練済みで、下流のファインチューニングに準備完了です。
 * [llm-jp-modernbert-base](https://huggingface.co/llm-jp/llm-jp-modernbert-base) - 📥 2k / ⭐ 12 / ModernBERT‑base モデルは 3.4 TB 日本語 llm‑jp‑corpus v4 で学習され、2 段階（max_seq_len 1024 → 8192）で微調整され、0.92 JSTS、0.91 JNLI、0.88 JCoLA を達成します。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 2k / ⭐ 4 / JSTから取得した約1 600 MBの医療科学アブストラクト（約10 M件）で事前学習されたJapanese RoBERTa‑baseモデル。SentencePiece Unigram（30k語彙）でトークナイズされ、CC‑BY‑4.0ライセンスの下で利用可能で、Hugging Faceパイプラインを介してファインチューニングできます。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 2k / ⭐ 2 / Japanese DeBERTa V2 tinyは、約171 GBの日本語Wikipedia、CC‑100、およびOSCARコーパスで事前学習され、Juman++による形態素解析が必要です。8台のNVIDIA A100 GPUを使用して33時間で訓練され、下流タスクに微調整できます。
 * [modernbert-base-japanese-wikipedia](https://huggingface.co/KoichiYasuoka/modernbert-base-japanese-wikipedia) - 📥 2k / ⭐ 5 / 日本語版Wikipediaと青空文庫で事前学習されたModernBERTモデル。NVIDIA A100 GPUで56時間訓練され、POSタグ付けや依存構造解析などの下流タスクへのファインチューニングに準備完了。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 2k / ⭐ 7 / ModernBERT‑Ja‑70M は、ローカルとグローバル注意を RoPE と組み合わせた軽量な日本語 BERT 変種です。4.39 T の混合言語トークンでトレーニングされ、語彙数 102 400、最大 8 192 トークンをサポートし、Flash Attention 2 に対応しています。パラメータ数は 30 M から 310 M の複数サイズで提供されます。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 682k / ⭐ 81 / Ruri v3 は、ModernBERT‑Ja をベースとした最先端の日本語テキスト埋め込みモデルで、最大8,192トークンの入力、100Kトークンの語彙、FlashAttention で加速された推論、および高速な sentence‑transformer での使用のための複数サイズバリアントをサポートします。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 219k / ⭐ 10 / Ruri v3 は、ModernBERT‑Ja をベースに構築された最先端の日本語テキスト埋め込みモデルで、最大 8,192 トークン、100 k‑トークン語彙、FlashAttention 加速、37 M から 315 M の複数サイズに対応しています。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 133k / ⭐ 24 / GLuCoSE v2 は CPU‑フレンドリーな日本語テキスト埋め込みモデルで、蒸留とマルチステージ対照学習によって微調整され、MIRACL や関連ベンチマークで同規模のモデルを上回る優れた意味的類似度と検索性能を提供します。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 59k / ⭐ 3 / Ruri v3は、8192トークンまでの高性能日本語テキスト埋め込み、100kトークン語彙、FlashAttentionサポート、および30 m–310 mの複数モデルサイズを備え、sentence‑transformersを介した効率的な推論とファインチューニングを可能にします。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 53k / ⭐ 47 / PLaMo‑Embedding‑1B は、Preferred Networks が提供する日本語テキスト埋め込みモデルで、情報検索、分類、クラスタリングのために日本語テキストをベクトルに変換します。JMTEB ベンチマークで高い性能を示し、Apache v2.0 license の下で無料で利用できます。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 44k / ⭐ 6 / Ruri v3は、ModernBERT‑Jaをベースに構築された最先端の日本語テキスト埋め込みモデルで、8192トークンまでのシーケンス、10万語の語彙、FlashAttentionに対応し、sentence‑transformers用に30 M〜310 Mパラメータのサイズでリリースされます。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 19k / ⭐ 34 / GLuCoSEは、LUKEをベースに構築された日本語文埋め込みモデルであり、ウェブおよびNLI／検索データで訓練され、最大512トークンまでの768次元平均プールベクトルを出力します。類似度ベンチマークで0.864のSpearmanと0.818のPearsonを達成しています。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 17k / ⭐ 45 / リリース準備済みのRuri v3日本語テキスト埋め込みモデル（30m–310m）のコレクションで、SentenceTransformerの使用ヒント、クエリ/パッセージプレフィックス、JMTEBベンチマーク結果を含み、他の日本語および多言語埋め込みと比較しています。
 * [ruri-large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2) - 📥 15k / ⭐ 10 / 日本語一般テキスト埋め込みリポジトリ Ruri は、30 M から 310 M パラメータまでの v3 モデルを提供し、JMTEB スコアを提示しています。sentence_transformers で（「クエリ: 」／「文章: 」接頭辞を使用）ロードする方法を示し、複数の日本語埋め込みモデルを比較したベンチマーク結果を提供します。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 13k / ⭐ 9 / Ruri v3 Japanese text embeddings（30 M–310 M parameters, 8192‑token limit, JMTEB 74.5–77.2）を含み、Sentence Transformers 用の「クエリ:」または「文章:」prefixes での指示、および Sup/Unsup SimCSE、GLuCoSE、LaBSE など複数の日本語モデルのベンチマーク結果を含みます。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 9k / ⭐ 12 / 日本語一般テキスト埋め込みモデル（Ruri‑v3、30‑310 Mパラメータ、8192‑token最大、JMTEBスコアが高い）は、Sentence‑Transformers使用例と他の日本語埋め込みとのベンチマーク比較とともに提供されています。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 7k / ⭐ 16 / JaColBERTv2は、日本語専用のColBERTベースの検索モデルで、MMarcoで知識蒸留（31）ノルゲート／1件の正例、250kステップ、バッチ32）を使って訓練されており、現在はmultilingual‑e5‑large、BGE‑M3、JaColBERTを上回っています。完全な評価は保留中です。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 3k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite は 768 次元の sentence‑transformer で、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、shunk031/jsnli 上で 1 エポックでトレーニングされ、クラスタリング、セマンティック検索、さらに Sentence‑Transformers と HuggingFace の両方の使用例を含んでいます。
 * [simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) - 📥 2k / ⭐ 15 / JSNLIデータセットでファインチューニングされた、tohok u/bert‑base‑japanese‑v2から派生した日本語SimCSEモデル。CC‑BY‑SA 4.0の下でリリースされ、fugashi/unidic‑liteトークナイゼーションを使用したsentence‑transformersで利用可能です
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 1k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B は、1.2 B パラメータを持つ日本語テキスト埋め込みモデルで、Sarashina2.1‑1B をベースに構築され、多段階対照学習で訓練され、JMTEB で最先端のスコアを達成しつつ、非商用ライセンス下で意味的類似性、検索、分類のために1,792 次元の密ベクトルを生成します。
 * [ruri-base-v2](https://huggingface.co/cl-nagoya/ruri-base-v2) - 📥 1k / ⭐ 5 / リポジトリは新しいJapanese text‑embedding v3モデル（30M〜310Mパラメータ、8 k‑token最大、JMTEB 74‑77）を提供し、sentence_transformers（query/passageプレフィックスを使用）でロードでき、supervised/unsupervised SimCSE、LaBSE、E5、その他のモデルとのベンチマーク比較を含みます。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 6M / ⭐ 61 / Japanese wav2vec‑2 XLSR‑53 は Common Voice 6.1、CSS10、JSUT で微調整され、16 kHz オーディオを必要とし、HuggingSound または HuggingFace パイプラインで使用できます。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 216k / ⭐ 115 / Kotoba‑Whisper‑v2.2 は、HuggingFace‑Transformers パイプラインを通じて統合された話者分離と自動句読点機能を備えた kotoba‑whisper‑v2.0 を拡張した日本語 ASR モデルであり、Asahi Ushio と Kotoba Technologies と協力して構築されました。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 35k / ⭐ 141 / Anime Whisperは、約5,300時間のanime‑style dialogueで微調整された軽量の日本語ASRモデルで、低 hallucination、リズムに合わせた句読点、非言語音声およびNSFW contentの正確な文字起こしを実現し、初期プロンプトなしで実行する必要があります。
 * [japanese-hubert-base-phoneme-ctc](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc) - 📥 11k / ⭐ 5 / rinna/japanese‑hubert‑base をベースにしたファインチューニング済みの日本語音素 CTC モデル。ReazonSpeech v2 データと pyopenjtalk‑plus ラベルで訓練され、新しい v2 リリース（prj-beatrice/japanese-hubert-base-phoneme-ctc-v2）で精度が向上しています。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 10k / ⭐ 93 / Kotoba‑Whisper v2.0 は、OpenAI Whisper large‑v3 から蒸留された日本語 ASR モデルで、7.2 million ReazonSpeech クリップで訓練され、ドメイン内テストで教師の CER/WER と同等の性能を維持しつつ 6.3 倍速で動作します。stable‑ts/punctuation のサポートと完全なトレーニングコードが GitHub にあります。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 9k / ⭐ 11 / facebook/wav2vec2‑large‑xlsr‑53 を Common Voice と JSUT コーパスでファインチューニングした日本語音声認識モデルで、16 kHz の音声入力に最適化されています。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 9k / ⭐ 56 / NVIDIA NeMo の 0.6 B‑parameter Hybrid FastConformer‑TDT‑CTC ASR model は、日本語音声を句読点付きで文字起こしし、NeMo フレームワーク内で推論またはファインチューニングに利用可能です。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 7k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 は、日本語と英語の ASR 用に 6.3 倍速化された distilled Whisper モデルを提供し、さらに双方向音声からテキストへの翻訳機能を備えています。これらは、OpenAI の Whisper large‑v3 をベースに、knowledge distillation を用いて構築され、クロスエントロピーと KL‑divergence loss を利用しています。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 3k / ⭐ 18 / Kotoba‑Whisper‑v2.1は、日本語のASRモデルであり、統合されたpunctuation‑postprocessing pipelinesを備えてkotoba‑whisper‑v2.0を拡張しています。これにより、同等のCER性能を保持しながら、シームレスでpunctuation‑aware transcriptionが可能になります。
 * [Qwen3-ASR-1.7B-JA](https://huggingface.co/neosophie/Qwen3-ASR-1.7B-JA) - 📥 3k / ⭐ 5 / Fine‑tuned Qwen3‑ASR‑1.7B for Japanese ASR、固有名詞・組織名・製品名、漢字が多い混在した日本語/英語の技術用語を正確に転写できるよう最適化されました
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 2k / ⭐ 25 / Kotoba Whisper v2.0 は CTranslate2 と faster‑whisper で使用するために CTranslate2 フォーマットに変換され、インストール手順、推論例、Apple M2 ベンチマーク、変換手順を提供します。
 * [japanese-hubert-base-phoneme-ctc-v3](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v3) - 📥 1k / ⭐ 5 / CTC音素認識（v3）用にファインチューニングされた日本語HuBERT‑base、MeCab N‑bestをpyopenjtalk‑plusで後処理し、CTCとMeCabコストを組み合わせた加重損失、更新された除外ルール、新しい「ty」音素を追加。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 1k / ⭐ 38 / reazonspeech‑nemo‑v2は、619 Mパラメータの日本語長文ASRモデルで、改良版Fast‑Conformerと線形スケーラブル注意機構を採用し、ReazonSpeech v2.0コーパスで訓練されました。3000トークンSentencePieceを用いたsubword RNN‑Tデコーダにより、多時間推論を提供し、Apache 2.0で配布されています。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 1k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh は、ReazonSpeech v2.0 Japanese ASR corpus でファインチューニングされた 96.7 M‑パラメータの wav2vec 2.0 Base モデルで、13.22 % の CER を達成し、Hugging Face transformers でデプロイ可能、Apache 2.0 ライセンスで公開されています。
 * [parakeet-tdt-0.6b-ja-GGUF](https://huggingface.co/cstr/parakeet-tdt-0.6b-ja-GGUF) - 📥 1k / ⭐ 1 / GGUF変換された0.6 B日本語パラケートTDT‑CTCモデルは、CrispASRのCLIでTDTデコーディング（CTCフォールバック）に使用でき、JSUTで6.4 % CERを達成し、ワードレベルタイムスタンプを提供します。完全な1.24 GBビット正確ビルドと約470 MBのQ4_K量子化バリアント（8トークン後に劣化するためF16が推奨）で利用可能です。

### feature-extraction
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 133k / ⭐ 56 / 日本語対応の T5 モデルは、Wikipedia と OSCAR データ約100 GB を SentencePiece トークナイズで事前学習し、ニュース分類ベンチマークで Google’s multilingual T5 を上回るが、ファインチューニングが必要で、バイアスのある出力が生成される可能性がある。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 43k / ⭐ 51 / 日本語 Sentence‑BERT v2 は、cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking を MultipleNegativesRankingLoss でファインチューニングし、v1 に比べて約1.5〜2 % の精度向上を実現。sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 としてリリースされました。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 32k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 は、ViT‑B/16 をベースにした Apache‑2.0 ライセンスの日本語 CLIP モデルで、CC12M のキャプションを日本語に翻訳して訓練され、2022 年 5 月 12 日にリリースされました。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 24k / ⭐ 18 / Japanese CLIP モデル clip‑japanese‑base‑v2 は、約20億画像‑テキストペアと蒸留でアップグレードされ、Eva02‑B 画像エンコーダと12層 BERT テキストエンコーダをペアリングし、前モデルよりも高い ImageNet‑1k 精度（0.708）を達成します。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 24k / ⭐ 30 / LY Corporation の clip‑japanese‑base は、約 1 B の画像‑テキストペアで学習された日本語 CLIP モデルで、Eva02‑B トランスフォーマー画像エンコーダーと12層の BERT テキストエンコーダーを使用し、STAIR で R@1 0.30、Recruit で 0.89 の精度、ImageNet‑1K で 0.58 の精度を達成し、ゼロショット画像分類と検索をサポートしています。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 22k / ⭐ 11 / 文埋め込みを生成するJapanese Sentence‑BERT (v1) モデルで、改良版v2が利用可能で、Hugging Face Transformers とカスタム `SentenceBertJapanese` クラスを使用したサンプル使用例があります。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 9k / ⭐ 14 / 日本語Sentence‑LUKEモデルは、Sentence‑BERTと同じデータセットで訓練され、同等にするかそれを上回る性能を有し、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、Hugging Face Transformers の MLukeTokenizer と LukeModel を介して使用される。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 7k / ⭐ 2 / ja_ginza_electra は、mC4 と UD_Japanese_BCCWJ r2.8（megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator をベースにしたもの）でファインチューニングされた日本語 ELECTRA モデルを提供する spaCy v3 の Python パッケージです。カスタム bunsetu‑phrase 検出機能を備え、MIT ライセンスで配布されています。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 3k / ⭐ 3 / 日本語 BERT‑base モデルを JSNLI 上で教師付き SimCSE によってファインチューニングし、Sentence‑Transformers または HuggingFace を通じて CLS プーリングで公開、512 バッチサイズで 1 M のサンプルを用いて学習率 5 × 10⁻⁵、温度 5 × 10⁻⁵、64 タークン制限、BFloat16 精度でトレーニング。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 2k / ⭐ 25 / Sarashina‑Embedding‑v2‑1B は、1,792 次元の日本語文変換器であり、マルチステージ対照学習 (multi‑stage contrastive learning) によって訓練され、最先端の JMTEB スコアを達成しています。また、意味的類似度、検索、パラフレーズ・マイニング、分類、クラスタリングに利用でき、Sentence‑Transformers を通じてオプションの instruction prefixes 付きで使用可能です。
 * [llm-jp-4-vl-9b-beta](https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta) - 📥 1k / ⭐ 14 / LLM‑jp‑4‑VL 9B beta は、llm‑jp‑4‑8b‑instruct と SigLIP‑2 を基に構築された 90億パラメータの日本語ビジョン‑ランゲージモデルで、InternVL3.0‑style の動的タイル処理と軽量 MLP プロジェクターを採用し、FineVision と Jagle での学習後に日本語ベンチマークで競合する性能を実現しています。

### text-ranking
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 358k / ⭐ 5 / 日本語でトレーニングされた CrossEncoder リランクラーは xsmall (384) から large (1024) まであり、さらに BGE‑v2‑m3‑v1 モデルも含まれます。ファインチューニング、推論、JQaRA、JaCWIR、MIRACL、JSQuAD のベンチマークスコアの例コードが付属しています。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 280k / ⭐ 14 / Ruri‑v3 Reranker は、ModernBERT‑Ja をベースにした堅牢な日本語テキストリランカーで、最大 8,192 トークンのシーケンス、100k トークンの語彙、FlashAttention および SentencePiece tokenizer をサポートし、sentence‑transformers 経由で使用できます。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 56k / ⭐ 7 / Japanese CrossEncoderリランカーモデルは、xsmall から large（BGE を含む）まであり、JQaRA、JaCWIR、MIRACL、JSQuAD で評価済み。sentence_transformers と HuggingFace 用の、すぐに利用可能な統合例も用意されています。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 50k / ⭐ 6 / 高速で軽量な日本語 Reranker v2 モデル（tiny、xsmall、small、base）は、ベンチマークスコアと GPU スピードを備え、sentence_transformers CrossEncoder と transformers ≥ v4.48 で使用でき、flash‑attn で高速化も可能です。また、CPU/ARM 用に ONNX/quantized フォーマットでも利用可能です。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 7k / ⭐ 12 / Sentence Transformersで構築された日本語クロスエンコーダリランカーは、各サイズのRuri‑Rerankerモデルに対する推論利用例とベンチマーク結果を示します。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 7k / ⭐ 2 / Sentence Transformers（クロスエンコーダー）で構築された日本語リランカー モデルは、`trust_remote_code` を介してロードでき、JQaRA、JaCWIR、およびMIRACL データセットでベンチマークされ、hotchpotch 組織から小〜大サイズで入手可能です。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / Japanese CrossEncoder Reranker モデル (xsmall, small, base, large, BGE‑v2 m3) は、hidden size が 384–1024 の範囲です。sentence_transformers と Hugging Face を用いた推論例で、JQaRA、JaCWIR、MIRACL、JSQuAD で 0.71–0.97+ のスコアを記録しています。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 2k / ⭐ 8 / 日本語Reranker v2スイートは、CrossEncoderとベースモデルをtinyからlargeまで公開し、各モデルにベンチマークスコアとGPU推論時間を添付します。また、HuggingFace Transformers ≥ 4.48（高速推論のためにオプションで flash‑attn）が必要です。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 1k / ⭐ 6 / コンパクトで高速な日本語リランカーライブラリ（v2）は、tiny-through-base および cross-encoder モデルを提供し、詳細なレイテンシと精度統計を備え、Transformers ≥ 4.48（オプションで Flash‑Attention 2）を必要とし、CPU/ARM デプロイメント向けに ONNX/quantization をサポートします。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 1k / ⭐ 16 / 日本語向け CrossEncoder リランカー モデル（xsmall から large まで）は、日本語テキストで学習され、sentence_transformers を通じて公開され、JQaRA、JaCWIR、MIRACL、JSQuAD で評価されます。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 758k / ⭐ 15 / 新しい VNTL データセットに基づく LLaMA 3 Youko qlora ファインチューニング。日本のビジュアルノベルを英語へ正確かつ文字通りに翻訳することに最適化されており、チャットモードは使用せず、デフォルトの LLaMA 3 プロンプトを使用し、ニュートラルサンプリング（温度 0、繰り返しペナルティ無し）を推奨する。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 187k / ⭐ 12 / Sugoi LLM 14B Ultra (GGUF) は、BLEUスコアが21.38の日本語‑英語翻訳モデルで、以前の13.67のほぼ二倍に近い点数です。RPG‑Makerの括弧付きテキストに優れ、プロンプトに強く従う性質と、インタラクティブチャットUIs用のJSON出力を実現します。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 40k / ⭐ 75 / OpusコーパスからのJapanese‑to‑English Transformer‑Align MT modelは、正規化とSentencePiece前処理を使用して、Tatoebaテストセットで41.7 BLEUと0.589 chr‑Fを達成します。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 6k / ⭐ 123 / PLaMo Translation Model は Preferred Networks が開発した翻訳タスク向けの大規模言語モデルで、ベース、ポストトレーニング、評価バリアントが用意されています。PLaMo community license の下で公開され、チャットやその他のダウンストリーム用途向けにインストラクションチューンは行われていません。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 3k / ⭐ 33 / FuguMT は、日本語→英語の Marian‑NMT 翻訳モデルで、transformers と SentencePiece により構築され、Tatoeba で 39.1 BLEU を記録しました。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 2k / ⭐ 35 / Fine‑tuned, GGUF‑quantized LFM2‑350M checkpoint は、短〜中長テキストに対するほぼリアルタイムの bi‑directional Japanese‑English 翻訳に使用でき、llama.cpp で利用可能です。
 * [opus-tatoeba-en-ja](https://huggingface.co/Helsinki-NLP/opus-tatoeba-en-ja) - 📥 1k / ⭐ 15 / 15.2 BLEUを持つ英語‑日本語の transformer‑align MTモデルは、opus+bt‑2021‑04‑10 をベースに正規化 + SentencePiece を使用して構築され、Tatoeba Challenge にてホストされています。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 1k / ⭐ 55 / FuguMTはHugging Face TransformersおよびSentencePieceで構築されたMarian‑NMTベースの英日翻訳モデルで、Tatoebaで32.7のBLEUスコアを達成しています。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 417k / ⭐ 176 / Manga OCR は、縦書きと横書きの日本語漫画テキスト（フリガナを含む）を、さまざまなフォントと低品質画像でも読み取る Vision Encoder-Decoder OCR ツールで、ソースコードは無料で入手可能です。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 66k / ⭐ 6 / Meikiocrの `meiki.text.recognition.v0`――D‑FINEベースのMobileNetV4モデルで、日本語ビデオゲームテキストに特化して微調整されたもので――は、960×32入力から最大48文字まで検出し、それぞれの文字をバウンディングボックスと信頼度スコアとともに出力することで、水平テキストに対して最先端の精度と遅延を実現します。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 49k / ⭐ 3 / meikiocr は、ビデオゲーム向けに D‑FINE ベースのオープンウェイトテキスト検出モデル（v0.1、MobileNet‑v4 バックボーン、2種類の解像度バリアント、64 ボックス制限）と、実験的低遅延 tiny および small バリアント（日本のビデオゲームと漫画で訓練済み）を提供します。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 2k / ⭐ 4 / Manga OCRは、さまざまなフォントと低品質画像に対して縦書き・横書きテキストとふりがなオーバーレイを含む日本漫画の高品質なOCRを提供するVision Encoder‑Decoder systemです。また、一般的な印刷された日本語OCRにも使用できます。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 1k / ⭐ 31 / Sarashina2.2‑OCRは、3BパラメータのエンドツーエンドOCRモデルであり、人間の嗜好最適化後に日本語と英語の文書をMarkdownに解析し、テーブルはHTML、数式はLaTeX、図像はバウンディングボックスアノテーションに変換します。高解像度の視覚‑言語理解を実現するため、SigLIP2ベースのビジョンエンコーダとSarashina2.2‑3B‑Instruct LLMを統合しています。

### token-classification
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 15k / ⭐ 11 / cl‑tohoku/bert‑base‑japanese‑v2 を使用した日本語 NER は、`BertForTokenClassification` を介して 8 つのエンティティタイプ（企業、政治・その他組織、施設、製品、イベント）を抽出し、Stockmark Wikipedia データセットで学習済みです。CC BY‑SA 3.0 ライセンスの下で `transformers`、`unidic_lite`、`fugashi` でインストール可能です。
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 9k / ⭐ 4 / 日本語に特化した DeBERTa V3 モデルで、xsmall、base、large の各バリアントがあります。このモデルは推論時に形態素解析器を使用せず、語境界を尊重し、語彙を縮小（large モデルのみで BPE あり）し、Hugging Face と互換性があります。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 8k / ⭐ 26 / 日本語NERコーパス（タグ PER, ORG, LOC, INS, PRD, EVT）上で、5エポックのAdam（lr 5e‑5、バッチ12）を使用してFine‑tuneしたXLM‑RoBERTa‑baseは、0.0173の検証ロスを達成し、Transformers 4.23.1とPyTorch 1.12.1でリリースされました。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 4k / ⭐ 11 / Wikipediaデータセット上の固有表現認識用に微調整された日本語 BERT‑Base は、*Large Language Model Introduction* の第6章で紹介され、Hugging Face transformers パイプライン（Apache 2.0 ライセンス）でデプロイできるものです。
 * [yomi-linter-modernbert-ja-130m](https://huggingface.co/ayousanz/yomi-linter-modernbert-ja-130m) - 📥 1k / ⭐ 3 / 日本語TTSプレフライトエラー検出のためにModernBERT‑Ja‑130mモデルをファインチューニングし、OpenJTalk、piper‑plus、VOICEVOXなどG2P/辞書ベースシステムで誤読されやすいスパンを特定しました。再現率は高く（≈80 %）、動的INT8量子化もサポートしています

### text-classification
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 10k / ⭐ 16 / Amazonの商品レビューに対して感情分類のためにFine‑tuned Japanese BERT (cl‑tohoku/bert‑base‑japanese‑v2) を使用し、6エポックで学習率 2 × 10⁻⁵ を設定した結果、約81 % の精度と0.73のF1スコアを達成しました。
 * [bert-for-japanese-twitter-sentiment](https://huggingface.co/LoneWolfgang/bert-for-japanese-twitter-sentiment) - 📥 10k / ⭐ 2 / JTS1kデータセット上で日本のTwitter感情分析用に微調整されたBERTで、ツイートをネガティブ（0）、ニュートラル（1）、ポジティブ（2）のラベルに分類し、transformersパイプラインでの使用に準備完了。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 3k / ⭐ 2 / 「Large Language Model Introduction」の第5章で紹介された、日本語 BERT‑based モデル。JGLUE JSTS データセットで意味的類似度スコアリングのためにファインチューニングされ、Colab ノートブック、transformers‑pipeline の使用方法、Apache 2.0 ライセンス付き。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 2k / ⭐ 15 / 日本語感情分析モデルは、chABSAデータセットで学習され、損失0.0001、精度1.0、F1スコア1.0を達成しました。Transformers 4.24.0およびPyTorch 1.12.1+cu113で構築され、Adam（学習率2e‑05、10エポック、バッチサイズ16）で最適化され、`model(**inputs)`で評価されました。
 * [bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - 📥 2k / ⭐ 9 / MARC‑ja JGLUE データセットで感情分析用にファインチューニングされた Japanese BERT‑Base v3、cl‑tohoku/bert‑base‑japanese‑v3 から構築され、Hugging Face `pipeline` と互換性があり、Apache License 2.0 の下でリリースされています。

### text-to-speech
 * [sarashina2.2-tts](https://huggingface.co/sbintuitions/sarashina2.2-tts) - 📥 60k / ⭐ 63 / sarashina2.2-tts は、SB Intuitions LLM‑based の日本語中心の TTS システムで、高精度な日本語と英語合成を自然で表現豊かな声で提供し、ゼロショットクローン、クロスリンガル一貫性、およびシームレスなコードスイッチングを実現します。
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 2k / ⭐ 11 / 日本語のTTSモデル **tsukuyomi‑wavlm** は、tsukuyomiコーパスの100発話に対して300エポックでファインチューニングされ、WavLMディスクリミネーターとA1/A2/A3プロソディ特徴をVITSアーキテクチャ上で使用し、22.05kHzの合成を生成する61 MBのONNXファイルとしてエクスポートされます。

### any-to-any
 * [gemma-4-12B-it-qat-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-12B-it-qat-UD-japanese-imatrix) - 📥 20k / ⭐ 9 / CPUに優しい日本語最適化量子化Gemma 4モデル（1/4サイズ、Apache 2.0）で、完全にオンプレミスで動作し、開発者サポートと堅牢なベンチマークをオプションで提供します

### audio-to-audio
 * [LFM2.5-Audio-1.5B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF) - 📥 5k / ⭐ 23 / LiquidAI の LFM 2.5‑Audio 1.5B JP モデルの量子化 GGUF バージョン（言語、オーディオエンコーダー、およびボコーダー重み：F32/F16/Q8_0/Q4_0）と、llama.cpp を使用した ASR と TTS の CLI/Server ランナー。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 122k / ⭐ 11 / Japanese‑language BERT‑Base (12 layers, 768‑dim, 12 heads)は、Unidic‑based word‑level plus character‑level tokenizationとwhole‑word maskingをCC‑100と2023 Wikipediaで事前学習し、7,027‑token vocabularyを生成する。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 76k / ⭐ 64 / Japanese BERT‑base（12層、768次元の隠れ層、12ヘッド、32k語彙）は、CC‑100と2023‑Jan Wikipediaで全単語マスキングを用いて事前学習され、Unidic 2.1.2の単語レベルトークナイゼーション＋WordPieceを併用し、200万ステップで学習しました。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 69k / ⭐ 14 / Japanese‑BERT‑Large は CC‑100 と Wikipedia に対して訓練され、Unidic‑lite のワードレベルトークナイゼーションを使用し、WordPiece サブワードとホールワードマスクリングを採用しています（24 層、隠れ層 1024 次元、16 ヘッド、32k 語彙）。プリトレーニングコードは cl‑tohoku/bert‑japanese にあります。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 16k / ⭐ 11 / ≈100 GB の Wikipedia と OSCAR CC‑100 データ（SentencePiece で 10:1 の混合、byte‑fallback を有する）で事前学習された日本語 T5‑v1.1 モデルで、下流タスクの微調整が必要です。転移学習サンプルコードが含まれ、出力に潜在的なバイアスを示唆しています。ライセンスは CC‑BY‑SA 4.0 です。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 7k / ⭐ 13 / moonshotaiのMoonlight‑16B‑A3B‑InstructをTFMCのimatrix Japanese datasetで訓練したgguf-format版をリリースしました。llama.cpp（CUDA‑enabled）で使用でき、recipe‑request promptを実行して確認できます。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 5k / ⭐ 17 / 高性能日本語 SPLADE v2 は、WebUI demo を通じてスパース‑ベクトル変換と推論を可能にし、YAST でトレーニングを行い、YASEM 埋め込みを提供し、JMTEB ベンチマーク結果を報告します。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 4k / ⭐ 19 / Japanese DeBERTa V3 base は、LLM‑jp v1.0 から 540 B トークンで事前学習され、修正された DeBERTa V3 セットアップで訓練され、形態素解析器を使用しないユニグラム・バイトフォールバックトークナイザーを使用し、JGLUE NLUタスク用に微調整済みです。
 * [kana-whisper](https://huggingface.co/sbintuitions/kana-whisper) - 📥 3k / ⭐ 6 / Whisper large‑v3‑turboをファインチューニングしたモデルで、日本語音声をカタカナに文字起こしするASRコンポーネントとして、Sarashina2.2‑TTSプロジェクト内のJoyo Kanji Yomi Benchmarkに使用され、Kana CER Usage With Transformersパイプラインを動かします。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 75 / Llama‑3‑ELYZA‑JP‑8B は、日本語向けに強化された 8‑B Llama 3 モデルで、GGUF（Q4_K_M）と AWQ 量子化を備え、llama.cpp、LM Studio、または OpenAI‑compatible API で実行できます。
 * [Qwen3.5-0.8B-JP-Tuned-v1.0](https://huggingface.co/CloudGoat/Qwen3.5-0.8B-JP-Tuned-v1.0) - 📥 2k / ⭐ 1 / Fine‑tuned Qwen3.5‑0.8B on 3.72 M Japanese tokens, achieving 61.39% JCommonsenseQA, 49.88% JNLI, 54.01% JSQuAD, and 70.43% MARC‑ja with a 3.53% overall response‑rate improvement.
 * [llm-jp-4-kappa-32b-a3b-v0.1-gguf](https://huggingface.co/mmnga-o/llm-jp-4-kappa-32b-a3b-v0.1-gguf) - 📥 2k / ⭐ 2 / TFMC/imatrix-dataset-for-japanese-llm の imatrix データで構築され、CUDA 対応の llama.cpp から利用できる、third‑intelligence の llm‑jp‑4‑kappa‑32b‑a3b‑v0.1 を GGUF に変換したバージョンです。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 は、8 billion パラメータを持つ LLM で、Meta の Llama 3.1 を日本語とコード／数式推論で改善しつつ英語の流暢さを保持し、継続的なプリトレーニングと指示調整ファインチューニングを合成日本語データで実現したものです。
 * [gemma-4-E2B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E2B-it-UD-japanese-imatrix) - 📥 2k / ⭐ 2 / GGUF変換されたGemma‑4‑E2B‑itモデルで、日本語熟練度向上のためにファインチューニングされ、Unsloth® Dynamic Quantization 2.0で構築され、コミュニティのバグ修正や日本語キャリブレーションデータが含まれ、llama.cppを介してCPU（≥8 GB RAM、≥4 GBディスク）で実行できます。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 2k / ⭐ 15 / Sarashina2.2 は、SB Intuitions が三段階パイプラインと合成データを用いて訓練した 0.5‑B、1‑B、および 3‑B の言語モデルを提供し、最高の日本語 QA、数学、およびコーディングスコアを達成し、指示調整されていない事前学習済みの重みを提供するが、偏った出力を生み出す可能性があります。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 22 / pfnet の plamo‑2‑translate を imatrix データから構築し、TFMC/imatrix‑dataset‑for‑japanese‑LLM に基づく GGUF‑format リリースで、CUDA 対応ハードウェア上で llama.cpp を通じてコンパイル・実行する手順を含む。
 * [tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf](https://huggingface.co/mmnga/tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf) - 📥 1k / ⭐ 4 / Repository は、tokyotech‑llm の Llama‑3.1‑Swallow‑8B‑Instruct‑v0.3 モデルの gguf-format 変換をホストしており、imatrix データセットで構築され、llama.cpp で実行可能です。
 * [t5-base-japanese-web](https://huggingface.co/megagonlabs/t5-base-japanese-web) - 📥 1k / ⭐ 21 / 32K語彙を持つT5モデルは、byte‑fallback機能付きで、日本語ウェブテキスト（mC4 + Wikipedia）に対して事前学習され、TPU v3‑8上で100万ステップ訓練され、Apache 2.0ライセンスの下で公開されています。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 1k / ⭐ 1 / 高度に最適化されたGGUFバージョンのgoogle/gemma‑4‑E4B‑itは、Unsloth Dynamic Quantization 2.0と広範なバグ修正を使用して日本語能力に最適化されており、llama.cppで動作し、最低16 GBのRAMと6 GBのディスクが必要で、GPUは任意です。
 * [sarashina2.2-1b](https://huggingface.co/sbintuitions/sarashina2.2-1b) - 📥 1k / ⭐ 13 / 1 ビリオンパラメータの日本語LLM「Sarashina2.2‑1B」は、ベーストレーニング、数学/コーディング用合成データファインチューニング、小規模データタスクチューニングという3段階で訓練され、QA・数学・コーディングのベンチマークで以前のモデルを上回りますが、インストラクションフォローに対しては調整されておらず、バイアスや不正確な出力を生成する可能性があります。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5-gguf](https://huggingface.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf) - 📥 1k / ⭐ 2 / tokyotech‑llm による Llama‑3.1‑Swallow‑8B‑Instruct‑v0.5 の GGUF conversion、TFMC/imatrix‑dataset‑for‑japanese‑LLM を組み込んだ、llama.cpp の Build/Run instructions 付き。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 2M / ⭐ 62 / 2009年から2024年までのNicoNico Liveのコメントログ（150GB超）を集約し、転換前・転換後・リアルタイムNX‑Jikkyoのキャプチャも含む、歴史的なTV‑broadcastディスカッションを簡単に取得できるAPIを提供します。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 14k / ⭐ 9 / Cauldron‑JAは、DeepL APIを使ってThe Cauldronから翻訳された44個のサブデータセットからなる日本語ビジョン‑ランゲージデータセットです。HuggingFace’s datasets library を通じて入手可能で、オリジナルセットと同一のライセンスで提供され、プロンプトはCC‑BY‑4.0でリリースされています。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 12k / ⭐ 32 / FineWeb2 Edu Japanese は FineWeb2 からの約1億2000万の高品質教育用日本語テキスト（約893億トークン）を提供し、DeepSeek‑API クラスフィケーター（スコア ≥ 2.5）でフィルタリングし、ModernBERT‑Ja‑130M でトークナイズされ、512 トークン以下の小規模サブセットを含みます。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 8k / ⭐ 7 / VOICEVOX生成の合成音声データセットで、445,793件の.wavファイル（総計577時間51分23秒）から構成され、ITA、つくよみちゃん、およびROHANコーパスを使用して作られた。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 6k / ⭐ 17 / Reazon Speech v2 データセットのミラーリリースで、UVR を使用してノイズ除去およびバックグラウンド音楽を削除したオーディオファイルが含まれています（4096 ファイル中 3674 ファイルが約10日間にわたり8 台の A800 GPU で処理されました）。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 5k / ⭐ 35 / Galgame VisualNovelデータセット (OOPPEENN/566973746F6F6372656164656C65746572) の再構成された再アップロード。Hugging Face datasets の効率的な読み込みのため、すべてのオリジナル音声/テキストを保持し、複数のゲームサブセットオプションを備えた抽出スクリプトを提供します。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 5k / ⭐ 11 / Hugging FaceにホストされているReazon Speech v2 Japaneseデータセットのミラー。CDLA‑Sharing‑1.0の下で配布され、利用は日本著作権法第30‑4条に限定されます。16 kHz FLAC音声ファイルが4,096件、対応する転写がTSV/CSV形式で含まれています。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 5k / ⭐ 121 / Nemotron‑Personas‑Japan は、CC BY 4.0 のオープンソースデータセットであり、高品質の合成生成された日本人ペルソナ（名前、性別、年齢、背景、婚姻状況、学歴、職業、所在地を含む）で、実際の人口統計・地理・人格分布に基づいており、確率的グラフィカルモデルと GPT‑OSS‑120B を用いて多様性を高め、バイアスを減らし、モデル崩壊を防ぎ、主権 AI の開発を支援し、商業利用をサポートするよう設計されています。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 3k / ⭐ 5 / Japanese JaQuAD、QG‑Bench のサブセットは、文レベルおよび段落レベルのデータを提供し、ハイライトされた回答トークンを用いて日本語の質問生成モデルの学習に利用でき、BLEU4、METEOR、ROUGE‑L、BERTScore、MoverScore で評価されます。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 3k / ⭐ 47 / Aozora Bunkoから取得したパブリックドメイン日本語テキストのユーザーフレンドリーで重複除去済みCSVデータセット。globis-org/aozorabunko‑extractorで処理され、現代日本語機械学習用途に合わせてクリーニング済み。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 3k / ⭐ 49 / Japanese‑Eroge‑Voice‑V2は、匿名化された1,033,142件のエロゲ音声–文字起こしペア（主に女性、NSFW）を2,657時間提供し、学術研究向けにMITライセンスで配布します。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 99 / 注釈付きタスク（要約訂正、数学推論、翻訳、創造的生成、ユーザー意図理解など）を網羅した100サンプルの日本語インストラクション・チューニング評価データセット。微調整モデルを手動または自動で5点評価できるよう設計されている。
 * [Lux-Japanese-Speech-Corpus](https://huggingface.co/datasets/Lami/Lux-Japanese-Speech-Corpus) - 📥 2k / ⭐ 5 / 96 kHz/16‑bit 原音およびクリーニング済み WAV ファイルを備えた、オリジナルキャラクター「Lux」を収録した日本語スピーチデータセット。トランスクライブメタデータは `metadata.csv` に、全体のデータセット情報は `dataset_infos.json` に記載されており、TTS 研究・応用向けに CC BY 4.0 ライセンスで利用可能です
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 2k / ⭐ 7 / JMedBenchは日本語医療・生物医学用LLMベンチマークであり、20のデータセットをMCQA、NER、STSなどを含む5つのタスクにまたがって構成しています。データセットはMedMCQA、PubMedQA、MMLUなどから取得されており、それぞれに独自のライセンスが付属しています。また、翻訳にバイアスが含まれる可能性があるため、人間によるレビューが必要であるという注意事項が記載されています。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEBは日本語テキスト埋め込みベンチマークで、5つのタスク（クラスタリング、分類、STS、検索、リランキング）と28のデータセットを特徴とし、1行で評価できるスクリプトを提供し、コミュニティの貢献を歓迎する。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 2k / ⭐ 24 / 2300万本の個人的に収集された日本語ウェブ小説で構成されるデータセットで、合計80.85億文字を含み、正当な機械学習利用にのみ提供され、詳細なアクセスリクエストが必要です。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 2k / ⭐ 141 / Japanese Anime Speech Dataset V2は、292,637件の整理済みオーディオ‑テキストペア（約397.5時間のSFW、および52.4時間のNSFWコンテンツ）を、セーフティ別に分割された128‑kbps MP3ファイルとして提供し、特に自動音声認識モデルのトレーニング用に設計されています。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 1k / ⭐ 20 / JMMMUは、日本語のマルチモーダルベンチマークで、ネイティブ専門家が翻訳した1,320の文化的に多様な質問（720は文化に依存しない、600は文化固有）に拡張され、現在は公開リーダーボードを備えています。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 1k / ⭐ 18 / Databricks‑dolly‑15k‑ja dataset は、instruction tuning 用に作られた databricks‑dolly‑15k の日本語版で、DeepL で翻訳されました。日本の LLM‑jp プロジェクトが作成し、著者は Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama、Takumi Okamoto です。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 1k / ⭐ 8 / llm‑jp‑instructions は、手作業でキュレーションされた日本語の指示データセット (v1.0) で、train、dev、test のスプリットが load_dataset を通じてアクセス可能です。
 * [CAT-Thinking-Dataset](https://huggingface.co/datasets/cyberagent/CAT-Thinking-Dataset) - 📥 1k / ⭐ 2 / CAT-Thinking 用のトレーニングデータセット：Swallow-Nemotron、Big-Math-RL、DAPO-Math、rStar-Coder、AReaL-boba-2-RL-Code、extraction-wiki-ja、magpie など、日本語推論タスクのキュレーションされたサブセット。トラジェクトリープロンプトと完了を含み、すべて CC BY 4.0 または Apache 2.0 ライセンス下で提供されます。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 1k / ⭐ 13 / LLM‑jpは、英語サブセット oasst2（kunishou/oasst2‑135k‑ja から派生）の DeepL 翻訳による日本語指示チューニングデータセットを提供し、Kiyomaru と Kodama によってコンパイルされています。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 1k / ⭐ 118 / ReazonSpeech は、FLAC エンコードされた日本語音声コーパスで、文字起こし付きです。8.5 h から 35,000 h までの 5 つのサイズで提供され、Hugging Face 経由で CDLA‑Sharing‑1.0 ライセンスの下でダウンロードでき、日本著作権法第 30‑4 条の規定により使用が制限されています。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 1k / ⭐ 6 / 日本語のMC4データセット (mc4-ja) のデータセットカード
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 1k / ⭐ 3 / 312,396 行のフィルタリングされたサブセットを Oscar 2023 データセットから Hugging Face (if001/oscar_2023_filtered) で読み込み、if001/HojiChar_OSCAR_sample GitHub リポジトリでサンプルコードを提供します。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 1k / ⭐ 2 / WAONは、サイズ、SigLIPスコアフィルタリングと重複排除（URL、キャプション、pHashによる）で構築された、大規模で高品質な日本語の画像‑テキストペアデータセットです。情報分析のためにApache 2.0の下でHuggingFaceに公開されました。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 938 / ⭐ 4 / 日本語の検索/QAデータセットを提供し、5つの多言語/日本語リランカー（例：BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）によって算出されたクエリごとのスコアを含む。各クエリごとに約200件の正例と負例ドキュメントの平均スコアも含まれる。
 * [japanese-qa-reasoning-100k](https://huggingface.co/datasets/hotchpotch/japanese-qa-reasoning-100k) - 📥 921 / ⭐ 3 / DeepSeek‑R1を使用してfineweb2-edu-japaneseテキストから生成された質問、キーワード、および回答の日本語データセットで、推論も含み、元のテストセットからのテストサンプルがあり、ODC-BYの下でライセンスされています。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 900 / ⭐ 89 / databricks‑dolly‑15k データセットの自動翻訳された日本語版、CC‑BY‑SA‑3.0 ライセンス、2023‑05‑11に最終更新。
 * [japan-law](https://huggingface.co/datasets/y2lan/japan-law) - 📥 847 / ⭐ 22 / 日本のe‑Gov法令データセットで、番号・題名・ID・施行日・全文を含み、2023年8月1日時点で最新有効版に重複除外されたもの。
 * [Medical-o1-Reasoning-SFT-Japanese](https://huggingface.co/datasets/ronantakizawa/Medical-o1-Reasoning-SFT-Japanese) - 📥 845 / ⭐ 3 / FreedomIntelligence の医療-o1-reasoning-SFT データセット（19,688 エントリ）は、OpenAI Batch API 経由で GPT‑4o‑mini によって生成され、翻訳された質問、思考過程、回答とともに元の英語テキストが含まれています。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 837 / ⭐ 3 / 2010年の日本語ウェブコーパスは、HuggingFace にアップロードされ、2009年の著作権改革に基づき研究利用のライセンスが付与されており、形態素ベースの解析と変換スクリプトによる自動句読点付加テキストを含んでいます。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 807 / ⭐ 8 / Rakuda は 40 件の日本語質問—歴史・社会・政府に関する自由回答形式と地理に特化した質問—を提供し、日本語 AI アシスタントのベンチマークに使用でき、vicuna‑eval と比較可能で、`datasets.load_dataset` で読み込むことができます。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 801 / ⭐ 2 / 18,612 の日本語訳された Python の指示–応答ペア（GPT‑4o‑mini で生成し、元の英語プロンプト、コード、および例を保持）で、訓練、微調整、チャットボット、研究、教育などの多様なコーディングタスクを提供し、すべて MIT ライセンスで公開されています。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 789 / ⭐ 17 / oasst1‑21k‑ja は、DeepL によって英語版 OASST1 サブセットから派生した日本語の instruction‑tuning データセットであり、LLM‑jp コラボレーティブプロジェクトにより日本で作成されました。お問い合わせは llm‑jp@nii.ac.jp、著者には Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama、Okamoto が含まれます。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 780 / ⭐ 6 / JamC‑QA は、8つの日本文化・知識カテゴリにわたる多肢選択問題のバイリンガルベンチマークで、リーダーボードメトリクスで最先端モデルを比較します。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 779 / ⭐ 2 / 日本語 Common Voice 17.0 サブセットを 30‑300 サンプルずつの 649 クライアント ID までフィルタリングし、8:2 の比率で訓練/検証に分割、1,000 サンプルの Parquet ファイルにバッチ化、合計 45,668 サンプル（CC0 ライセンス）
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 769 / ⭐ 57 / AnswerCarefully Datasetは、商業利用または非商業利用のLLM安全向上のために日本語および多言語データを提供し、他の使用（安全迂回を含む）を禁止し、帰属を伴う派生作品を許可し、害やサービス変更に対する非責任の創作者免責事項を付帯しています。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 747 / ⭐ 47 / 日本語 NLP ベンチマーク（Yahoo Japan と早稲田大学が作成）に対する JGLUE データセットカードとロードスクリプトを更新しました。テキスト分類（MARC‑ja、JCoLA）、文対分類（JNLI）、QA（JSQuAD、JCommonsenseQA）をカバーし、リリースは GitHub と Hugging Face にリンクされています。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 733 / ⭐ 5 / Fate/Stay Nightのキャラクター「Emilia」の対話とロアのデータセットで、会話型言語モデルのトレーニングと評価のためにフォーマットされています。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 708 / ⭐ 14 / EDINET‑Bench は、10 年分の EDINET‑API 公開レポートを使用して、会計不正検出、収益予測、業界予測などのタスクで LLM を評価する日本の金融ベンチマークです。構築・評価コードが提供され、データセットは PDL 1.0 に再ライセンスされています。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 682 / ⭐ 7 / 音声言語モデルに対する音声入力とテキスト入力の知能ギャップを定量化したデータセットで、Elyza‑tasks‑100、M‑IFEval、JamC‑QAベンチマークから合成された音声を4つのサブセットに分割した構成です。テキストはCC‑BY‑SA 4.0の下、音声は非商用・非再配布の使用に限定されます。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 645 / ⭐ 5 / 再配布、AIトレーニング、商業利用を禁止し、アクセスには手動承認が必要なゲート付き非商用派生データセット（EDINET XBRL財務データ）
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 621 / ⭐ 4 / ArknightsワイフのJP Voice‑Text Dataset: 10,905件の日本語音声クリップ（合計26.3 h）を単一俳優キャラクターから収集。ASR/ASVモデルのファインチューニングや評価に有用です
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 595 / ⭐ 155 / Japanese Anime Speech Dataset は、73,004 の音声‑テキストペア（合計110時間、V1 から V5 へと進化）を提供し、OpenAI’s Whisper などの ASR モデルを強化します。すべての利用に対してオープンライセンスが適用され、クレジットの表記があれば感謝します。
 * [jaCappella](https://huggingface.co/datasets/jaCappella/jaCappella) - 📥 575 / ⭐ 5 / jaCappella corpusは、ジャズ・パンクロック・ボサノヴァ・ポピュラー・レゲエ・演歌・中立・バラード・EDM・ソウル/ファンクなどのジャンルにわたる曲の六部構成スコアと分離されたオーディオを備えた日本語アカペラボーカル団体データセットです。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 566 / ⭐ 3 / 日本語の指示データセットで、632,636 のマルチターンサンプル（約6.35 Bトークン）と、GPT‑OSS‑120b の推論トレースが含まれ、オープンエンド、数学、執筆、MCQA タスクで、135 の金融トピックと 20 の一般トピックを網羅し、LLM の推論を金融でファインチューニングするよう設計されています。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 565 / ⭐ 5 / ダウンロード可能な81歳の日本人女性の音声コーパス（生データとノイズ除去後のwav、フォニーム/カナ＋プロソディラベルを含む）は、学術利用が無料で「Fusic Saoyoshi Voice Corpus」に帰属表示を伴って使用できます。
 * [OpenSakura-DS-260220-LN-ja-zh-COT-Lilith](https://huggingface.co/datasets/OpenSakura/OpenSakura-DS-260220-LN-ja-zh-COT-Lilith) - 📥 565 / ⭐ 2 / OpenSakura-DS-260220-LN-ja-zh-COT-Lilithは、1.64百万行の日本語から中国語へのライトノベル翻訳データセット（約18 GB）であり、マッピングベースの5分割を備え、推論内容とuuid、episode、segmentインデックスなどの構造化フィールドを保持しています。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 511 / ⭐ 3 / 日本語版Wikipediaの文はさまざまな埋め込みとFAISSインデックスに変換され、Hugging Face Spaceデモ、変換スクリプト、検索・Q&A・OpenAI text‑embedding‑3‑smallを用いたRAGの評価が提供されます。埋め込みはOpenAIライセンス対象で、その他はCC‑BY‑SA‑4.0です。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 509 / ⭐ 142 / 日本語インストラクション・チャットデータセット（LLMのファインチューニング用（例：LoRA）、9 M+サンプル）。最近更新され、ライセンス付きAlpacaデータを除外し、クリーンなWikipediaとALT出力を含め、CC‑BY‑SA 4.0でリリース。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 503 / ⭐ 27 / WRIMEデータセットは、日本語の投稿42,200件からなるコレクションで、筆者、3名の読者、およびその平均に対してPlutchikの8つの感情でアノテーションされています。感情分析タスク向けに、40kトレーニング、1.2kバリデーション、2kテストのスプリットで構成されています。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 472 / ⭐ 7 / Japanese Medical VQA 12M は、Open‑PMC‑18M から派生した、1200万枚を超える日本語医療画像とキャプションを含む商用利用可能なマルチモーダルデータセットです。Parquet/Webdataset 形式で提供され、オリジナルと日本語翻訳画像、充実したキャプション、および InternVL3.5、Qwen3‑30B、GPT‑oss 120B を使用して生成された VQA スタイルの Q&A ペアを含みます。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 445 / ⭐ 13 / 「wikipedia-ja-20230720」日本語ウィキペディアスナップショットのデータセットカード。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 445 / ⭐ 17 / JA‑VG‑VQA‑500 は、日本語 Visual Genome VQA データセットの 500 サンプルのサブセットで、CC BY 4.0 ライセンスが付与され、EvoVLM‑JP‑v1‑7B のベンチマークに使用されます。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 420 / ⭐ 24 / cc100-jaは、cc100データセットの日本語部分を集めたもので、シャーディングされたParquetファイルとして提供されています。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 420 / ⭐ 7 / JHumanEval は HumanEval benchmark の手翻訳版で、164 の Python programming problems を提供し、並行した英語と日本語のコメント付きで、日本語‑LLM のコード生成を評価しつつ、元の英語のエラーを保持します。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 401 / ⭐ 7 / Livedoor News Corpus は、日本語ニュース記事データセットを提供し、5,894件のトレーニング、737件の検証、736件のテストのインスタンスに分割され、HTMLタグを除去して Creative Commons Attribution‑NoDerivs ライセンスの下で公開されています。
 * [JParaCrawl-Filtered-English-Japanese-Parallel-Corpus](https://huggingface.co/datasets/Verah/JParaCrawl-Filtered-English-Japanese-Parallel-Corpus) - 📥 399 / ⭐ 3 / 日本語-英語のクリーンな翻訳コーパスと、各ペアを評価するファインチューニング済みのMistral/Stable‑LMモデルが提供されており、高品質の翻訳のみを受け入れ、不完全・不正確・下手に書かれたものは拒否します。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 394 / ⭐ 5 / 日本語変種「mc4‑ja‑filter‑ja‑normal」のデータセットカード、追加情報は保留中です。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 377 / ⭐ 3 / WildGuardTestJPは、1,725サンプルの日本語評価データセットであり、WildGuardTestから多段階の改良パイプライン（Seed‑X‑PPO‑7B, gpt‑oss‑120b, Qwen2.5‑72B‑Instruct, gemma‑3‑27b‑it）を通じて忠実に翻訳されたものです。Hugging FaceでODC‑BY ライセンスの下で公開されています。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 366 / ⭐ 35 / Syosetu711Kは、2023年3月26日〜27日に小説家になろうからスクレイピングされた約711,700本の小説で構成される日本語データセットです。全テキストとメタデータ（タイトル、著者、NCode、あらすじ等）を提供し、教師なしテキスト生成および分類タスクに利用されます。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 365 / ⭐ 4 / 266時間の日本語音声データセットは、Emilia dataset から取得され、Scribe v1（ElevenLabs STT/ASR）で分類され、Facebook audio aesthetics prefiltering が適用されています。このデータセットは HuggingFace と Discord で協力のために利用可能です
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 355 / ⭐ 34 / 409時間の日本語エロゲ音声データセットで、2パス loudnorm（‑23 LUFS、‑1 dB peak、11 LRA）で処理され、litagin/anime-whisper により文字起こしされ、匿名化され、WebDataset（FLAC、JSON、TXT）として保存されています。主に女性の声が収録されており、AI文字起こしのエラーが存在する可能性があります。MIT‑licensed for academic research.
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 342 / ⭐ 4 / 日本語と英語のウェブコーパスの集合体―9 Bトークンの日本語セット（JA‑WEB‑9B）、63 Bトークンの英語および日本語セット（EN‑WEB‑63B、JA‑WEB‑63B）や、パラフレーズされた JA‑PARAPHRASE‑63B、指示スタイルの JA‑INSTRUCT‑63B、翻訳済みの JA‑TRANSLATE‑63B などの合成バージョン―を含む。このコーパスは、データ制約環境下で日本語LLMの事前学習におけるデータ拡張を研究するために使用されます。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 333 / ⭐ 14 / JMMLUは、56科目に跨る7,536問の教師作成質問を収録した、日本語のマルチタスク言語理解ベンチマークです。含まれる科目は、専門医学・心理学・会計学・哲学、及び多様な高校科目です。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 330 / ⭐ 9 / llm‑book/wrime‑sentiment のデータセットカードは、WRIME から派生した二項式日本語感情分析セットを提供し、Avg. Readers_Sentiment に基づいて「positive」または「negative」とラベル付けされます（中立ケースを含めるオプション付き）。このセットは、“Introduction to Large Language Models” のサンプルデータとして意図されています。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 318 / ⭐ 16 / Jagleは、画像–テキストペアとPDFコーパスから構築された約920万件のインスタンスを持つ日本語マルチモーダルポストトレーニングデータセットであり、LLM‑jp‑4‑VL 9B betaの訓練に使用され、日本語ビジョン・ランゲージタスクで性能向上が示されています。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 317 / ⭐ 16 / 日本語および多言語のQA、NLI、パラフレーズデータセットのカタログで、各データセットの検索またはQAタスクとライセンス（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）を詳細に記載。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 314 / ⭐ 17 / Galgame_Speech_SER_16kHzは、Galgame_Speech_ASR_16kHzから派生した3.7 百万ファイル（5,353時間、104 GB）の感情音声データセットで、ローカルLLMによって注釈付けされ、GNU GPL v3.0に基づき商業利用が禁止されています。このデータセットを使って訓練されたモデルはオープンソースでなければならず、必須の引用は不要です。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 314 / ⭐ 9 / JMMMU‑Pro は、Vibe Construction を通じて構築された日本語のマルチモーダルベンチマークであり、生成型モデリングと人間による検証を組み合わせて、低コストかつ高品質な画像‑QA データを生成し、オープンソース LMMs の欠点を明らかにし、将来の VQA 研究を導くものです。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/llm-book/ner-wikipedia-dataset) - 📥 310 / ⭐ 4 / 「Wikipediaベースの固有表現抽出」(v2.0) は、Stockmark が作成し、CC-BY-SA 3.0 の下で公開された書籍 *Large Language Models: An Introduction* に使用されている日本語 NER データセットです
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 310 / ⭐ 47 / Galgame_Speech_ASR_16kHz は 16 kHz の ASR データセットで、3.75 百万ペア（≈5,354 時間）が含まれ、Galgame_Dataset から派生しており、GPL v3.0 の下で公開され、商用利用は禁止され、訓練済みモデルはオープンソースであることが求められます（引用は任意）。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 309 / ⭐ 5 / STAIR‑Captionsは2017年にリリースされ、キャプション生成、マルチモーダル検索、画像生成に利用できる820,310の日本語キャプションを提供します。詳細なアノテーション、メタデータ、Creative Commons BY‑4.0 ライセンス付きです。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 298 / ⭐ 3 / 『Introduction to Large‑Scale LLM II』で使用され、llm‑jp‑eval によって作成されたクロスデータセットの日本語LLM評価用のja‑vicuna‑qa‑benchmarkのデータセットカード（Apache 2.0）。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 295 / ⭐ 6 / J-HARD‑TTS‑Eval は、短シーケンス安定性、繰り返し処理、およびコンテキスト補完において、自己回帰型日本語 TTS モデルの強靭性をベンチマークします。データセットは Hugging Face で入手可能です（short、repetition、rhyme、continuation）。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 295 / ⭐ 5 / JAMMEval は七つの日本語 VQA データセットを蒸留したベンチマークであり、曖昧さと非視覚的質問を除去するために二回のヒトアノテーションで改良され、マルチモーダル日本語タスクにおけるビジョン‑ランゲージモデルの信頼性の高い評価を提供します。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 291 / ⭐ 6 / 『oscar2301‑ja‑filter‑ja‑normal』のデータセットカード―Oscarコーパスの日本語フィルタリング済みかつノーマルサブセット。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 289 / ⭐ 15 / 『Large Language Model Introduction』で使われるJGLUE datasetのデータセットカード。元のリポジトリ (original repo) から取得し、コードはCC BY‑SA 4.0でライセンス、データは配布者のライセンスに基づく。Kurihara & Kawahara（日本語）を引用し、Shunsuke Kitada’s repository をベースに構築。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 287 / ⭐ 20 / Retrieval‑Augmented Generation (RAG) を評価するための日本語 QA データセットで、JAQKET 質問と Wikipedia パッセージから構築され、金ラベル付きの検索関連性ラベルを持つ。HuggingFace と GitHub でリリースされ、主に nDCG@10 で評価される。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 254 / ⭐ 3 / 機械学習により非監督的に粗く10,000 グループにクラスタリングされた洗練された日本語ウェブコーパス（例：mc4‑ja）は、合法的な分析に使用でき、Parquet 形式のファイルのうち一部のみが「out」フォルダにリストされており、Git LFS 経由でダウンロード可能です。
 * [JDocQA-Reasoning](https://huggingface.co/datasets/ricoh-ai/JDocQA-Reasoning) - 📥 253 / ⭐ 5 / リコーがGENIACプロジェクトの一環として公開した「JDocQA Reasoning Bench」と呼ばれる日本語ベンチマークは、実際のドキュメント画像から図表・テーブル・ダイアグラムや複雑なテキストを解釈することを含む1,286件の推論問題に対して、大規模多モーダル言語モデルを評価し、LLM‑as‑Judgeシステムによる自動スコアリングを行います。
 * [Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k) - 📥 249 / ⭐ 7 / 39,600サンプルの日本語クリエイティブライティングデータセット。deepseek-ai/DeepSeek-V3-0324 で構築され、各エントリは OpenAI スタイルのメッセージターン（instruction_1/output_1 と instruction_2/output_2）を含み、一部 NSFW コンテンツが含まれます。MIT ライセンス下で公開されています。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 244 / ⭐ 12 / JaQuADは2022年作成の日本語QAデータセットで、Wikipediaから抽出した39,696ペアのSQuAD‑style抽出クエリで構成され、総サイズは73.2 MBです。BERT‑Japaneseでファインチューニングすると78.92 % F1（63.38 % EM）を達成します。
 * [Umamusume-voice-transcription](https://huggingface.co/datasets/TLME/Umamusume-voice-transcription) - 📥 232 / ⭐ 8 / Umamusume‑voice‑transcriptionは、各競走馬キャラクターの文字起こしファイルを含む77文字データセットであり、それぞれの音声総再生時間（秒）をリストしています（例：「东商变革」799 s、「北部玄驹」1128 s）。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 231 / ⭐ 3 / 64,139件の日本人名を生物学的性別でラベル付けしたデータセット―漢字、ひらがな、ローマ字で表記―は、トレーニング44.9k、検証6.41k、テスト12.8kに分割され、ISDA'23で採択されました。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 230 / ⭐ 2 / JCommonsenseQA は、日本語の複数選択データセットで、CommonsenseQA の適応版として共通認識推論を対象にしています。CC BY‑SA 4.0 のライセンスの下で公開され、doi:10.5715/jnlp.30.63 として引用されています。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 229 / ⭐ 9 / JSICKは、SICKコーパスを翻訳して作成された日本語-英語のNLIとSTSデータセットであり、ワードオーダーや格助詞の扱いを検証するストレステストセットが含まれており、異なる文法関係に対して1 666、797、および1 006の句対を持っています。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 226 / ⭐ 5 / CC-100、OSCAR-2301、HPLT v1.2、および wiki40b-ja から抽出された5.6 Bトークンの日本語–英語コードデータセット。LOCAL AI HACKATHON #000 “calm2-chat” のために Contrail‑200m‑64k を事前学習する目的で使用されるが、文境界とパープレキシティフィルタリングは欠如している。
 * [OpenAI-MRCR-Translation-JPN](https://huggingface.co/datasets/abeja/OpenAI-MRCR-Translation-JPN) - 📥 223 / ⭐ 2 / OpenAIの長文コンテキストMRCRからLLMsを使用して翻訳された日本語評価データセットで、元の構造を保持しつつ新しいアシスタント応答を生成し、MITライセンスを維持しています。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 219 / ⭐ 22 / AI生成されたアニメイラストには英語のプロンプトとPhi‑3 Vision由来のキャプション（英語と日本語）が付いており、パブリックドメインで無料利用が可能です。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 215 / ⭐ 5 / 20,800件のWAVファイルからなる195人の日本語AItuberペルソナ（リファレンス、オリジナル、説明的、感情的発話を含む）データセットが、詳細なペルソナと音声メタデータを含み、データサイエンスAPI経由で取得可能です。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 204 / ⭐ 33 / 日本語のRAGベンチマークを、金融・通信・製造・公共・小売という5つの業界ドメインで提供し、データセットの公開、自動評価フレームワーク、および Claude 3.5‑Sonnet、GPT‑4o などのモデルの比較結果を掲載します。
 * [ScreenTalk_JA2ZH-XS](https://huggingface.co/datasets/Itbanque/ScreenTalk_JA2ZH-XS) - 📥 201 / ⭐ 3 / 約30時間の日本語音声と整列された簡体字中国語テキストを含む10,000サンプルペアデータセット（Parquet形式、CC BY 4.0）は、音声→テキスト翻訳および多言語ASR+MT研究向けに設計されています。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 198 / ⭐ 2 / LLM生成の日本語クエリと回答のデータセットで、パラフレーズされたWikipediaテキストから作成され、CC‑BY‑SA 4.0の下で公開されています。
 * [swallow-magpie-ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1) - 📥 185 / ⭐ 5 / Swallow‑Magpie‑Ultra‑v0.1 の一部としてリリースされた、tokyotech‑llm モデルのトレーニング用に magpie‑ultra‑v0.1 から抽出した平均的に良質な日本語–英語指示チューニングデータセット（各42kペア）
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 176 / ⭐ 3 / Whisper Large‑V2 を使用して動画から桐生真希のVNダイアログを文字起こしし、pydub で分割しました。未整形テキストは TTS モデル学習用です（著作権は保有していません）。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 175 / ⭐ 33 / LoRA などを用いた instruction‑response 微調整向けの日本語チャットデータセットで、llm‑japanese‑dataset から日本語‑英語翻訳例を除外して派生したもの。バージョン付きリリースで 180 万〜250 万件のエントリを提供し、CC‑BY‑SA 4.0 の下でライセンスされ、DOI 10.1109/BigData59044.2023.10386605 で引用されます。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 175 / ⭐ 10 / 日本語から英語への並列コーパスで、kakenサブセットの llm‑jp‑corpus‑v3 を Qwen/Qwen2.5‑32B‑Instruct で翻訳し、独自の翻訳列を備え、CC‑BY‑4.0 の下でライセンスされています。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 169 / ⭐ 2 / 年間証券報告書の表から直接セル値を抽出するためのマルチモーダル日本語テーブル‑QAデータセットで、画像、OCRテキスト（境界ボックス付き）、質問と回答が含まれ、CC‑BY‑4.0 ライセンス下に提供されます。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 169 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) は、Integration、Reasoning、Logical、Table、Abstention を網羅したマルチカテゴリ QA dataset を提供し、日本語 RAG ジェネレーターの評価を目的としています。このデータセットは人手と GPT‑4.1 によって構築され、CC BY‑SA 4.0 の下でリリースされています。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 168 / ⭐ 18 / 1月 2024年のHTMLダンプから抽出され、パラグラフ構造、メタデータ（disambiguation, sexual, violent flags, templates, timestamps）を保持し、GitHubにホストされた抽出スクリプトも付属するNLP-ready Wikipedia記事データセット。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 163 / ⭐ 6 / Range3のwikipedia‑ja‑20230101リポジトリは、完全なWikipediaデータセットから抽出され、Pythonコードで生成された日本語Wikipediaテキストのみを含むParquetファイルを提供しています。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 154 / ⭐ 26 / このリポジトリは、OpenAssistant/oasst1 データセットの日本語訳をホストしており、エラーフラグ付きの自動翻訳エントリ、約2,000件の手動修正、チャット形式のサブセット、およびデータを指示‑出力ペアに変換してファインチューニングに使用するスクリプトを含みます。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 148 / ⭐ 2 / COVID‑19 Japanese Twitter datasetは、日本のツイートIDと評価コード（63–68）を提供し、COVID‑19の関連性および事実／意見のステータスを示すことで、テキスト分類研究を可能にします。
 * [DEJIMA-dataset](https://huggingface.co/datasets/MIL-UT/DEJIMA-dataset) - 📥 148 / ⭐ 4 / 3.88 M枚の画像とLLM生成キャプション、オープンエンドQAペアを含む日本語ウェブ規模データセット。重複除外でフィルタリングされ、検出タグで拡張。単純版・洗練版・検出版・全体版など複数バリエーションがあり、Hugging Faceにホストされています。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 147 / ⭐ 21 / SNOW T15/T23 日本語簡易化コーパスのデータセットカードで、50 k件の手動で照合されたオリジナルと簡易化済み日本語（≤2 k語彙）と英訳レコード、35 k件の拡張セットを含み、日英テキスト簡易化・翻訳に使用されます。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 144 / ⭐ 4 / GuoらによるWiki40Bデータセットの日本語セクションを再フォーマットしました。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 140 / ⭐ 15 / Zundamonキャラクター設定のシンプルなデータセット—オンラインソースおよび管理データから編纂された—は、character‑LLMsのテスト用に、指定されたライセンスの下でzmnjp.jsonlおよびzmn.jsonl形式で提供されます。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 137 / ⭐ 10 / JA‑Multi‑Image‑VQAは、39枚の画像と55問の質問からなるデータセットで、マニュアルで作成された日本語のQ&Aが含まれ、マルチイメージVQA用に設計されています。load_dataset経由でアクセスでき、テキストはApache 2.0ライセンスで提供されます（画像の使用は制限されています）。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 137 / ⭐ 7 / SentenceTransformers に適した列と構造に再フォーマットされた日本語データセットで、RelRank スコアによって複数の HuggingFace ソースから対照学習用に正例（≥0.7）と負例（≤0.3）のペアへフィルタリングされています。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 132 / ⭐ 6 / Japanese XL‑Sum subset は PaLM‑2 15‑gram overlap を通じてフィルタリングされ、4,215件のトレーニング例、758件の検証例、766件のテスト例を含みます。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 131 / ⭐ 5 / JAQKET は、Wikipedia から派生した日本語のオープンドメイン QA データセットであり、複数選択式のクイズ質問を含むバージョン 1.0（13,061 件の学習データ、271 件の検証データ）と、質問プロンプトのみで抽出された回答を要求するバージョン 2.0（2,154 件の学習データ、1,164 件の検証データ）を提供し、QA システムの研究を促進するように設計されています。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 129 / ⭐ 16 / Hachi‑AlpacaはStanford Alpacaを元に‑mistralai/Mixtral‑8x22B‑Instruct‑v0.1で作成された日本語合成データセットで、同モデルによってクリーニングされ、Deepinfra上で提供され、Alpaca‑jp researchのためにApache‑2.0ライセンスで公開されています。
 * [japanese-confidential-information-extraction-sft](https://huggingface.co/datasets/akiFQC/japanese-confidential-information-extraction-sft) - 📥 127 / ⭐ 2 / 日本語のSFTデータセットで、テキストから11種類の機密エンティティを抽出するよう設計されており、LFM2モデルのLoRAファインチューニング用です。40,897サンプルが含まれ、訓練/検証セットに分割されています。すべてのキーを持つJSON形式で出力し、該当なしの場合は空リストになります。
 * [pjsk-emu-dataset](https://huggingface.co/datasets/chitsanfei/pjsk-emu-dataset) - 📥 126 / ⭐ 11 / CC‑BY‑NC 4.0 ライセンス（帰属表示と非営利制限付き）の 2735 ファイルからなる WAV 音声データセット。so‑vits‑svc 4.0 用で、研究目的のみメールでのリクエストにより入手可能です。
 * [danbooru-ja-tag-pair-20241015](https://huggingface.co/datasets/p1atdev/danbooru-ja-tag-pair-20241015) - 📥 124 / ⭐ 9 / Danbooruタグと日本語訳の150Kエントリデータセット（2024年10月15日更新）、拡張Wikiソースから構築、FastTextで非日本語タグを除外し、欠損項目にはfew-shot Calam Chat翻訳を追加しました。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 123 / ⭐ 2 / 5つのNLPタスク（広告受容性、一貫性、性能推定、A3認識、および類似度）に対する日本語オンライン広告データセット。train/dev/test の分割は TSV 形式です。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 119 / ⭐ 13 / 日本語ロールプレイ対話データセットで、十分な長さを持つマルチポスター記録のみをフィルタリングし、ポスター名を正規化し、上位スピーカーを均衡させたもの。機械学習用途を想定しています。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 117 / ⭐ 24 / AutoWikiQA は、Swallow-MX と LLMs（ルールベースのテンプレートを使わず）を用いて Wikipedia から自動生成された質問–回答ペアを手作業でフィルタリングし、230 万件以上の無料の日本語 QA データセットです。知識教示および検索強化生成アプリケーションをサポートします。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 116 / ⭐ 4 / 日本語版のExplainable Multi-hop Question Answering dataset は、質問、回答、Wikipedia記事を結びつけるステップバイステップの導出を特徴とし、導出フォーマットが更新され、複数のバージョンがリリースされています。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 115 / ⭐ 3 / BBH‑jaはBIG‑Bench Hardデータセットの日本語訳を提供し、JSON‑L（入力・正解ターゲット）とYAML（入力・ターゲット）のChain‑of‑Thoughtプロンプトを含む評価問題を提供し、PLaMoモデルで翻訳しています。
 * [sakura_japanese_dataset](https://huggingface.co/datasets/saldra/sakura_japanese_dataset) - 📥 114 / ⭐ 20 / Sakura_datasetは、DbCL v1.0でライセンスされている商用利用可能な超小型高品質の日本語データセットです。共通知識質問応答（commonsense QA）、数学問題（Calc‑ape210k）およびカスタム日本語共通知識質問を網羅しており、rinna/japanese‑gpt‑neox‑3.6b などのモデルに対する LoRA 微調整で使用できます。
 * [med-slm-ja-before-after](https://huggingface.co/datasets/genshiai-daichi/med-slm-ja-before-after) - 📥 113 / ⭐ 2 / 2010〜2024年の日本語医療ガイドラインにおける46,705件の変更データセット。変更は改訂、追加、新概念、不関連項目に分類され、各変更には出典が示されています。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 112 / ⭐ 82 / 日本語ウェブ小説章データセットと英語ファン翻訳がペアになっており、バージョン2では106Kの整列された文に拡張されています。シリーズメタデータを含み、品質フィルタリングは行われていません。フェアユース/Apache 2.0 の下で配布され、テイクダウン条項が設けられています。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 107 / ⭐ 4 / 「大規模言語モデル入門」に掲載され、RONWIT が提供する livedoor News Corpus から派生した日本語 NER データセット。CC BY‑ND 2.1 JP ライセンスの下でクリーンアップされた HTML 記事で構成されています。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 105 / ⭐ 2 / KokoroChatは、最も大規模な日本語心理カウンセリング対話データセットであり、480名の訓練済みカウンセラーによる6,589件のロールプレイングセッション（各平均91発話）を含む。豊富かつ長文形式の会話、20次元詳細クライアントフィードバックを備え、共感的応答生成、対話評価、およびメンタルヘルス言語モデリングに関する研究を支援し、ACL 2025で受理された。
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 104 / ⭐ 24 / RealPersonaChatは、対話データとスピーカーのペルソナおよびBig Five性格特性（評価スコアと人口統計属性を含む）を組み合わせた約14,000エントリの日本語対話コーパスであり、再同定やなりすましに注意するよう警告しています。
 * [alpaca_jp_python](https://huggingface.co/datasets/HachiML/alpaca_jp_python) - 📥 103 / ⭐ 8 / Apache 2.0の下でリリースされた、HachiMLプロジェクトの一部として、mistralai/Mixtral‑8x22B‑Instruct‑v0.1 を使用して生成し、Deepinfra によって洗練された Synthetic Japanese Alpaca データセット。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 102 / ⭐ 22 / MOMIJI（約5600万ページ、1100億文字、2億4900万枚の画像）という日本語ウェブドキュメントと画像データセットは、ビジョン‑ラングエージモデルの訓練用に設計されており、関連するインタラクティブ可視化ツールとテキストフィールド生成ユーティリティスクリプトが付属しています。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 101 / ⭐ 11 / 大型の日本語PDFベースのQAデータセット（JDocQA）は、5 504文書と11 600件の注釈付き質問–回答ペア（yes/no、factoid、numerical、およびopen‑ended）の4種類を含み、画像、答えられない例を備え、train/validation/testセットに分割されています。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 101 / ⭐ 5 / 日本のアニメ音声データセット、元の joujiboi/japanese‑anime‑speech‑v2 コレクションを分割した版。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 101 / ⭐ 11 / 検証済みのchain‑of‑thought 推論を備えた高品質な合成日本語数学問題データセット。PRM800K と GSM8K を Qwen2‑7B‑Instruct で翻訳し、正確性をフィルタリングして作成。Hugging Face datasets ライブラリ経由で利用可能。
