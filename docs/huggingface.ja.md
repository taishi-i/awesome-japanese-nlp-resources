# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語向けのNLPに関する、Pythonライブラリ、LLM、辞書、コーパスに特化したリソースを厳選してまとめた一覧です。
このページでは、Hugging Faceで利用可能な日本語NLP特化のモデルとデータセットを掲載しています。現在、192件のモデルと142件のデータセットが含まれています。

_2026年8月9日更新_

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)

## Contents
 * [Ranking](#Ranking)
   * [Models](#models-ranking)
   * [Datasets](#datasets-ranking)
 * [Models](#Models)
   * [text-generation](#text-generation)
   * [automatic-speech-recognition](#automatic-speech-recognition)
   * [fill-mask](#fill-mask)
   * [sentence-similarity](#sentence-similarity)
   * [feature-extraction](#feature-extraction)
   * [text-ranking](#text-ranking)
   * [translation](#translation)
   * [image-to-text](#image-to-text)
   * [text-classification](#text-classification)
   * [token-classification](#token-classification)
   * [text-to-speech](#text-to-speech)
   * [any-to-any](#any-to-any)
   * [text-to-image](#text-to-image)
   * [audio-to-audio](#audio-to-audio)
   * [image-text-to-text](#image-text-to-text)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | モデル名 | Downloads | Likes | カテゴリ |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 4M | ⭐ 62 | automatic-speech-recognition |
| 2 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 743k | ⭐ 16 | translation |
| 3 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 673k | ⭐ 81 | sentence-similarity |
| 4 | [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) | 📥 557k | ⭐ 51 | feature-extraction |
| 5 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 474k | ⭐ 9 | fill-mask |
| 6 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 458k | ⭐ 177 | image-to-text |
| 7 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 432k | ⭐ 15 | text-generation |
| 8 | [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) | 📥 372k | ⭐ 40 | fill-mask |
| 9 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 369k | ⭐ 76 | fill-mask |
| 10 | [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) | 📥 308k | ⭐ 15 | text-ranking |
| 11 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 237k | ⭐ 10 | sentence-similarity |
| 12 | [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) | 📥 208k | ⭐ 24 | sentence-similarity |
| 13 | [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) | 📥 206k | ⭐ 56 | feature-extraction |
| 14 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 181k | ⭐ 14 | translation |
| 15 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 157k | ⭐ 42 | fill-mask |
| 16 | [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) | 📥 150k | ⭐ 124 | automatic-speech-recognition |
| 17 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 126k | ⭐ 11 | others |
| 18 | [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) | 📥 115k | ⭐ 5 | feature-extraction |
| 19 | [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) | 📥 105k | ⭐ 49 | fill-mask |
| 20 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 78k | ⭐ 59 | text-generation |

### Datasets-ranking

| # | データセット名 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 1M | ⭐ 74 |
| 2 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 12k | ⭐ 7 |
| 3 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 10k | ⭐ 33 |
| 4 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 6k | ⭐ 9 |
| 5 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 5k | ⭐ 11 |
| 6 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 3k | ⭐ 126 |
| 7 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 3k | ⭐ 36 |
| 8 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 3k | ⭐ 18 |
| 9 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 2k | ⭐ 47 |
| 10 | [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) | 📥 2k | ⭐ 15 |
| 11 | [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) | 📥 2k | ⭐ 6 |
| 12 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 100 |
| 13 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 2k | ⭐ 7 |
| 14 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 2k | ⭐ 144 |
| 15 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 1k | ⭐ 49 |
| 16 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 1k | ⭐ 47 |
| 17 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 1k | ⭐ 6 |
| 18 | [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) | 📥 1k | ⭐ 2 |
| 19 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 1k | ⭐ 16 |
| 20 | [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) | 📥 997 | ⭐ 14 |

## Models
### text-generation
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 432k / ⭐ 15 / CC‑100、C4、Wikipedia で学習された12‑layer、768‑hidden の日本語 GPT‑NeoX モデル。Huggingface と互換性があり、各文の末尾に必ず笑顔の絵文字を付けるオプションのトイプレフィックス調整ウェイトが付属しています。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 78k / ⭐ 59 / 2.7Bパラメータの日本語 GPT‑NeoX モデルは、ABEJA Inc. が日本語 CC‑100 と OSCAR で学習し、Hugging Face Transformers パイプラインまたは PyTorch で利用可能で、MIT license の下で公開されています。
 * [Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4) - 📥 49k / ⭐ 2 / Qwen3‑Swallow v0.2 では、Bilingual Japanese‑English LLMs（30B‑A3B / 32B）が CPT、SFT、RLVR を通じて訓練され、数学とコーディングの性能を維持し推論力を高め、Hugging Face 上で複数の量子化版とともにリリースされました。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 28k / ⭐ 8 / 「LLM‑jp‑3‑150m」は、情報学研究所のLLM R&D Centerが開発した150Mパラメータを有する日本語言語モデルです。Hugging Face Transformers形式で配布され、torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8 が必要です。Japanese Wikipedia、Common Crawl、WARP/PDF、WARP/HTML、Kaken データを使用し、unigram byte‑fallback tokenizer で事前学習されています。
 * [LFM2.5-1.2B-JP-202606](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606) - 📥 22k / ⭐ 73 / LFM 2.5‑1.2B‑JP‑202606 は、高性能で汎用性のある日本語チャットモデルです。知識、指示従順性、数学、コード、およびツール使用において、同等のサブ-2 B モデルを上回るため、日本語アプリケーションの文化的ニュアンスを重視する開発者に最適です。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 19k / ⭐ 18 / Japanese Stable LM Base Gamma 7BをShisa 7B dataでFine‑tunedし、JA MT‑Benchで強い結果を得ました。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 15k / ⭐ 15 / SB Intuitionsの Sarashina2.2‑0.5B instruct v0.1は、5億パラメータの日本語オートレグレッシブモデルで、日本語と英語のMTベンチマークで良好な性能を示し、torch-transformers経由でロード可能です。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 14k / ⭐ 19 / Llama 3.1 Swallowは、MetaのLlama 3.1の事前学習を継続して日本語性能を向上させ、合成日本語データで指示ファインチューニングを行う8‑Bおよび70‑Bモデルのセットです。これにより、gemma‑3‑27b‑itと同等の会話挙動を備えた複数のリリースバリアントが提供されます。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 12k / ⭐ 17 / 日本語大規模言語モデル（1.8 b から 172 b beta1、インストラクションバリアント付き）のコレクションで、NIIの研究開発センターから提供され、Hugging Face Transformers 形式でパッケージ化され、1兆語以上の日本語・英語・Web コーパスを混合して事前学習されています。torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5 が必要です。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 11k / ⭐ 11 / llm‑jp‑4‑8b‑instructは、NIIのLLM‑jp‑4シリーズからの4.1 Bパラメータを持つ日本語LLMで、大規模コーパスで事前学習され、次に教師付き指示データのみでファインチューニングされ（DPO/REINFORCEは使用していない）、料理本スタイルの使用ガイドとbyte‑fallbackユニグラムトークナイザーが付属します。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 11k / ⭐ 3 / Qwen3‑Swallow v0.2 は、CPT、SFT、および RLVR で訓練された 30‑B と 32‑B の日本語‑英語バイリンガル LLM を提供し、日本語の正確性、翻訳、数学、コーディングを向上させて、オリジナルの Qwen3 と同等または上回ります。9 本のモデル（CPT、SFT、RL）および AWQ 量子化版を含み、GPT‑OSS‑Swallow もリリースされています。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 10k / ⭐ 1 / 日本語対応・指示調整済みのGemma‑2モデルは、Llama（2b/9b/27b 事前学習版と指示版）に基づいて構築され、2025年5月19日にリリースされ、HuggingFaceとSwallowチームのウェブサイトから入手できます。
 * [LFM2.5-1.2B-JP-202606-ONNX](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-ONNX) - 📥 10k / ⭐ 6 / 日本語版 LFM2.5‑1.2B モデルを ONNX にエクスポートし、ONNX Runtime、Transformers.js、および WebGPU でのクロスプラットフォーム推論を可能にします。FP32、FP16、INT4/FP16 混合など複数の精度バリアントが用意されており、WebGPU に適した INT4+FP16 フォーマットを推奨しています
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 8k / ⭐ 21 / Llama3 Swallowは、2024年7月1日にリリースされた、日本語拡張のMeta Llama 3ファミリーで、Instructとchat形式の8Bおよび70Bバリアントを提供し、SFTとChat VectorでMegatron‑LM上で微調整され、主要な日本語NLPタスクでベンチマークされている。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 実験的な日本語モデルは、lightblue/suzume‑llama‑3‑8B‑japanese と Meta‑Llama‑3‑8B‑Instruct の違いを chat‑vector approach を使って抽出し、upsampled して Meta‑Llama‑3‑70B‑Instruct に適用した結果、ほとんど変更がなく、将来のスケーリング計画を立てている。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 7k / ⭐ 150 / Llama‑3‑ELYZA‑JP‑8B は、ELYZA によって開発された日本語強化版で、8 billion パラメータ（80億）を持つ Llama 3 モデルで、Meta‑Llama‑3‑8B‑Instruct 上で日本語用に微調整されています。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 6k / ⭐ 44 / NIIから提供される8 BパラメータのLLM‑jp‑4‑8b‑thinking日本語言語モデルを、pre-/mid‑trainingで訓練し、SFT/DPOで調整済みとして、torch‑transformersで使用可能かつ詳細なクックブック指示付きで提供します。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 6k / ⭐ 21 / OpenCALM は、decoder‑only 日本語 Transformer 言語モデル（160 M〜6.8 B パラメータ）のスイートで、CyberAgent, Inc. によって CC‑BY‑SA 4.0 の下でリリースされました。日本語 Wikipedia と Common Crawl でトレーニングされ、Hugging Face の torch‑transformers を通じて利用可能です。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 6k / ⭐ 25 / Hugging Face‑互換の日本語中心のトランスフォーマーモデル（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct）は情報学研究所から提供され、Wikipedia、Common Crawl、WARP、Kaken、Dolma を含む多様な日本語・英語コーパスで事前学習されており、torch ≥ 2.3、transformers ≥ 4.40、accelerate、flash‑attn を必要とします。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 6k / ⭐ 85 / Rinnaの24層、1024ユニットの日本語GPT‑2‑mediumモデルは、CC‑100とWikipediaをSentencePieceトークナイゼーションで学習され、rinna/japanese‑pretrained‑modelsリポジトリで入手できます（MITライセンス、2021年4月7日リリース、2021年8月25日更新）。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 5k / ⭐ 39 / SB Intuitionsから提供される自己回帰型日本語モデル（sarashina2.2‑3B‑instruct‑v0.1）を、他のモデルとベンチマークし、使用例スクリプト付きで提供。安全性トレーニングは限定的である旨の注意書きが付いています。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 5k / ⭐ 6 / 8.6 Bパラメータの llm-jp-4-8b-base トランスフォーマーをホストするリポジトリ。  
National Institute of Informatics の LLM R&D Center で事前学習・ミドルトレーニングを経て、監督付きファインチューニングと直接的な好み最適化（強化学習は使用していない）で訓練され、PyTorch-transformers の使用ガイドを提供しています。
 * [DeepSeek-R1-Distill-Qwen-32B-Japanese](https://huggingface.co/cyberagent/DeepSeek-R1-Distill-Qwen-32B-Japanese) - 📥 5k / ⭐ 254 / トランスフォーマーを用いてテキスト生成するための、日本語にファインチューニングされたDeepSeek‑R1‑Distill‑Qwen‑32Bモデル（MITライセンス）で、カスタムプロンプト形式とストリーミング出力に対応しています。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 5k / ⭐ 10 / リポジトリは、Massed Compute ハードウェアで作成され、TheBloke の a16z ファンド付き LLM 仕事の一部として、Stability AI の日本語 StableLM Instruct Gamma 7B の GGUF 形式で量子化されたモデルファイルを提供します。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 4k / ⭐ 27 / rinnaの日本語GPT‑2 smallは、12層、768ユニットの隠れ層を持つtransformerで、日本語CC‑100とWikipediaをデータとして学習され、SentencePieceでトークナイズされ、MITライセンスのもとで2021年8月25日にリリースされました（Hugging Face: rinna/japanese‑gpt2‑small、詳細は https://arxiv.org/abs/2404.01657 を参照）。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 4k / ⭐ 13 / Qwen3‑Swallow v0.2は、日本語―英語のLLM（30B‑A3B と 32B）を提供し、CPT、SFT、RLVR によってトレーニングされ、強力な数式・コーディング・推論能力を保持し、9 つのリリース済みモデルと AWQ 量子化バリアントを備えています。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 3k / ⭐ 140 / 9 billionパラメータの日本語最適化LLM、NVIDIA Nemotron‑Nano‑9B‑v2‑Japaneseは、2024年9月までのデータでハイブリッド Mamba-2/MLP/4-layer-attentionアーキテクチャを用いて学習され、Nemotron-Personas-Japan tool‑callingデータセットでファインチューニングされます。最終回答を生成する前に制御可能な推論トレースをオプションで生成でき、商用利用が可能です。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/ash2813/llm-jp-4-32b-a3b-thinking-gguf) - 📥 3k / ⭐ 3 / Q4_K_M GGUF量子化版の llm‑jp/llm‑jp‑4‑32b‑a3b‑thinking 日本語モデルを提供します。これは、重要度行列を llm‑jp‑corpus‑v4 でキャリブレーションしたもので、学術領域での性能を維持しつつ、校正データ、スワップシャード用スクリプト、およびオプションの f16 シャードを供給します。
 * [asmr-qwen3.5-9b-zh-cn-echo-mtp-gguf-v0.1](https://huggingface.co/mmis1000/asmr-qwen3.5-9b-zh-cn-echo-mtp-gguf-v0.1) - 📥 3k / ⭐ 2 / Fine‑tuned Qwen3.5 MTP in GGUF format that translates Japanese ASMR transcriptions into Simplified Chinese while echoing the source text, applying domain glossaries, and preserving emotion with several quantized versions (q4_k_m, q6_k, q8_0, bf16).
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 3k / ⭐ 24 / Llama 3.1 Swallowは、継続的なプレトレーニングと日本語特有のインストラクションファインチューニングで訓練された8B / 70B Llama 3.1モデルの日本語強化シリーズです。最新の8B‑Instruct‑v0.3は、日本語MT‑Benchで最先端の結果を示しています。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 3k / ⭐ 58 / TinySwallow‑1.5B‑Instruct は、TAID を用いて Qwen2.5‑32B‑Instruct から蒸留された 1.5 B の日本語インストラクション調整済みオートレグレッシブ言語モデルであり、研究目的のみに利用されることを想定しています。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 3k / ⭐ 153 / LFM2.5‑1.2B‑JPは日本語最適化されたチャットモデルで、LFM2より日本語知識と指示に従う能力で優れ、LoRAによるファインチューニング、Transformers、vLLM、llama.cppを使った推論をサポートし、50.7 JMMLU、58.1 M‑IFEval、56.0 GSM8Kのスコアを達成しています。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 2k / ⭐ 36 / 32億パラメータの日本語トランスフォーマーLLM（llm‑jp‑4‑32b‑a3b‑thinking）は、国立情報学研究所（National Institute of Informatics）からのもので、教師付きファインチューニングと直接的な好み最適化（direct preference optimization）を用いてプリトレーニングと整合化されました。強化学習は使用していません。ユニグラム・バイトフォールバック・トークナイザー（unigram byte‑fallback tokenizer）を採用しています。
 * [Qwen3-Swallow-8B-CPT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2) - 📥 2k / ⭐ 1 / Bilingual 30 B- と 32 B-パラメータの LLM、Qwen3‑Swallow v0.2 は CPT、SFT、RLVR で構築され、日本語、日本語‑英語翻訳、数学、コーディングで優れた性能を発揮し、Qwen3 と同等またはそれを上回り、AWQ‑量子化された形式で Hugging Face にリリースされました。
 * [LFM2.5-1.2B-JP-202606-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-GGUF) - 📥 2k / ⭐ 27 / Liquid AI の Hybrid LFM2 モデル（例：1.2 B 日本語 GGUF バージョン）は、高品質で高速、かつメモリ効率の良いエッジAIをオンデバイス展開に提供し、Hugging Face リポジトリ経由で llama.cpp を使ってローカル実行できます。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking-gguf) - 📥 2k / ⭐ 6 / NIIのLLM R&D Centerが提供するLarge‑language models llm-jp-4‑32b‑a3b‑thinking‑gguf は 32 B パラメータを持ち、プレ／ミッドトレーニングと SFT/DPO（または instruct バリアントでは SFT のみ）で訓練され、クックブック形式の使用ガイドが提供されています
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 2k / ⭐ 49 / 日本語で継続的にプレトレーニングされたMistral‑Nemoモデル（Mistral‑Nemo‑Japanese‑Instruct‑2408）は、mistralai/Mistral‑Nemo‑Instruct‑2407 を基に構築され、device mapping と ChatML プロンプトを備えた transformers で利用可能で、Apache‑2.0 ライセンスの下で Ryo Ishigami により公開されました。
 * [LFM2-350M-PII-Extract-JP](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP) - 📥 2k / ⭐ 59 / LFM2‑350M‑PII‑Extract‑JP は、350 millionパラメータを備えたオンデバイスの日本語 PII‑extraction モデルで、GPT‑5 と同等の性能を実現し、契約書、メール、医療レポートにおける機密データのマスキングを可能にします。
 * [sarashina2.2-1b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1) - 📥 2k / ⭐ 16 / このリポジトリは、SB Intuitions の 1 B‑パラメータ自動回帰日本語指示モデル sarashina2.2‑1b‑instruct‑v0.1 をホストし、他の日本語‑BERT と比較して日本語と英語の MT と指示タスクでベンチマークを行っています。さらに、torch‑transformer の使用例と安全性トレーニングが限定的である旨の警告も付録として含まれています。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 2k / ⭐ 17 / TokyoTech‑LLM リポジトリは、Swallow Llama‑2 ファミリーの LLaMA‑2 モデルを提供しており、日本語データで拡張された 7B、13B、70B バリアントを含みます。これらには instruction‑tuned、NVE‑tuned、7B Plus バージョンがあり、2023年12月以降にリリースされました。
 * [japanese-stablelm-instruct-beta-70B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-70B-GGUF) - 📥 2k / ⭐ 12 / GGUF形式でハードウェア量子化されたモデルファイルを提供し、Stability AI の 70 billion パラメータの日本語 StableLM Instruct Beta を LLaMA‑cpp ベースツールで使用できるようにします。
 * [japanese-stablelm-instruct-beta-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-7B-GGUF) - 📥 2k / ⭐ 1 / Repo は GGUF‑formatted 7B 日本語 StableLM Instruct Beta モデルをホストしており、Massed Compute ハードウェアで量子化されているため、llama.cpp および人気のある AI UI フレームワークとともに使用できます。
 * [aibuncho-japanese-novel-gpt-j-6b-gguf](https://huggingface.co/mmnga/aibuncho-japanese-novel-gpt-j-6b-gguf) - 📥 1k / ⭐ 4 / 日本語小説用のGPT‑J‑6BをGGUFに変換し、llama.cpp（branch mmnga‑dev）で使用できるようにしました。利用例は提供されていますが、llama.cpp がネイティブな gptneox または gpt2 のサポートを採用すると互換性がなくなる可能性があります。
 * [Wanabi-Gemma4-31B-GGUF](https://huggingface.co/kawaimasa/Wanabi-Gemma4-31B-GGUF) - 📥 1k / ⭐ 8 / GoogleのGemma 4 31BをファインチューニングしたGGUFバージョンで、Project Wannabeの構造化プロンプト形式と日本語創作ライティングに最適化されており、一般的な対話や推論機能も保持しています。
 * [jinen-v1.1-beta.gguf](https://huggingface.co/togatogah/jinen-v1.1-beta.gguf) - 📥 1k / ⭐ 1 / NFKC正規化されたプロンプト用に最適化された「jinen」（v1.1‑beta）日本語かな漢字変換モデルのGGUF形式プロトタイプ。AJIMEE‑Benchでベンチマークし、Accuracy@1が80 %で、さまざまな量子化（f16, Q8_0, Q5_K_M, Q4_K_M）を実施しました
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 1k / ⭐ 21 / NIIから提供される1.8 Bパラメータのllm‑jp‑3.1‑1.8b‑instruct4日本語指示‑調整モデルは、Hugging Face TransformersおよびTorch ≥ 2.3.0に互換性があり、事前学習済みと微調整済みのチェックポイント、ならびに使用例を含みます。
 * [Gemma-2-Llama-Swallow-2b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-2b-it-v0.1) - 📥 1k / ⭐ 4 / 日本語強化 Gemma‑2 “Swallow” 言語モデルは、継続的な事前学習と指示調整ファインチューニングで構築されており、Hugging Face で 2 b、9 b、および 27 b のバリアントが利用可能です
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 1k / ⭐ 12 / 東京Tech-LLM が開発した大規模言語モデルは、LLaMA‑2 をベースに日本語データ（SFT）で微調整されており、Swallow‑7b/13b/70b のバリアントとその instruct, NVE、および “plus” バージョンが 2023年12月から 2024年4月までにリリースされています。
 * [ABEJA-Qwen2.5-32b-Japanese-v1.0](https://huggingface.co/abeja/ABEJA-Qwen2.5-32b-Japanese-v1.0) - 📥 1k / ⭐ 6 / 日本向けに最適化された Qwen 2.5‑32B モデルで、SFT と DPO を使用して abeja/ABEJA‑Qwen2.5-32b-Japanese‑v0.1 からファインチューニングされ、ABEAJA‑Qwen2.5‑32b‑Japanese‑v1.0 としてリリースされた。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 1k / ⭐ 35 / LFM2.5‑1.2B‑JPは、LFM2.5ハイブリッドアーキテクチャ上に構築された1.2 Bパラメータの日本語テキスト生成モデルで、生成と完了タスク向けに最適化され、Hugging Faceにホストされ、llama.cpp経由で実行可能です。
 * [Murasaki-8B-v0.2-GGUF](https://huggingface.co/Murasaki-Project/Murasaki-8B-v0.2-GGUF) - 📥 1k / ⭐ 2 / Murasaki‑8B‑v0.2は、ACGNコンテンツ（ライトノベル、脚本、短文）向けに最適化された8 BパラメータのSystem 2チェーンオブソート翻訳モデルで、アニメとGalGame字幕を用いて訓練データを3倍に拡張し、専用CoTプロンプトを3種類サポートし、効率的なデプロイメントのために複数のGGUF量子化を提供します。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 1k / ⭐ 20 / GPT‑OSS‑Swallow v0.1 は、CPT、SFT、RLVR によって訓練された 20B と 120B の日本語―英語バイリンガルLLM を提供し、数式とコーディング課題で GPT‑OSS を上回るか同等の性能を示し、2026年2月にリリースされ、4 つの SFT/RL バリエーションと今後の量子化版を予定しています。
 * [llm-jp-3-3.7b-instruct](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct) - 📥 1k / ⭐ 13 / NIIのLarge Language Models R&D Centerがリリースした、日本語・多言語言語モデル（1.8 bn〜13 bnパラメータ、base・instructバリアント）は、Hugging Face Transformers向けにパッケージ化され、Japanese Wikipedia、Common Crawl、WARP/PDF/HTML、Kaken、English Wikipedia、Dolmaデータセットで事前学習されています。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 4M / ⭐ 62 / Japanese wav2vec‑2 XLSR‑53 は Common Voice 6.1、CSS10、JSUT で微調整され、16 kHz オーディオを必要とし、HuggingSound または HuggingFace パイプラインで使用できます。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 150k / ⭐ 124 / Kotoba‑Whisper‑v2.2 は、HuggingFace‑Transformers パイプラインを通じて統合された話者分離と自動句読点機能を備えた kotoba‑whisper‑v2.0 を拡張した日本語 ASR モデルであり、Asahi Ushio と Kotoba Technologies と協力して構築されました。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 61k / ⭐ 11 / facebook/wav2vec2‑large‑xlsr‑53 を Common Voice と JSUT コーパスでファインチューニングした日本語音声認識モデルで、16 kHz の音声入力に最適化されています。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 51k / ⭐ 147 / Anime Whisperは、約5,300時間のanime‑style dialogueで微調整された軽量の日本語ASRモデルで、低 hallucination、リズムに合わせた句読点、非言語音声およびNSFW contentの正確な文字起こしを実現し、初期プロンプトなしで実行する必要があります。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 13k / ⭐ 95 / Kotoba‑Whisper v2.0 は、OpenAI Whisper large‑v3 から蒸留された日本語 ASR モデルで、7.2 million ReazonSpeech クリップで訓練され、ドメイン内テストで教師の CER/WER と同等の性能を維持しつつ 6.3 倍速で動作します。stable‑ts/punctuation のサポートと完全なトレーニングコードが GitHub にあります。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 12k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 は、日本語と英語の ASR 用に 6.3 倍速化された distilled Whisper モデルを提供し、さらに双方向音声からテキストへの翻訳機能を備えています。これらは、OpenAI の Whisper large‑v3 をベースに、knowledge distillation を用いて構築され、クロスエントロピーと KL‑divergence loss を利用しています。
 * [Qwen3-ASR-1.7B-JA](https://huggingface.co/neosophie/Qwen3-ASR-1.7B-JA) - 📥 10k / ⭐ 6 / Fine‑tuned Qwen3‑ASR‑1.7B for Japanese ASR、固有名詞・組織名・製品名、漢字が多い混在した日本語/英語の技術用語を正確に転写できるよう最適化されました
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 5k / ⭐ 60 / NVIDIA NeMo の 0.6 B‑parameter Hybrid FastConformer‑TDT‑CTC ASR model は、日本語音声を句読点付きで文字起こしし、NeMo フレームワーク内で推論またはファインチューニングに利用可能です。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 4k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh は、ReazonSpeech v2.0 Japanese ASR corpus でファインチューニングされた 96.7 M‑パラメータの wav2vec 2.0 Base モデルで、13.22 % の CER を達成し、Hugging Face transformers でデプロイ可能、Apache 2.0 ライセンスで公開されています。
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 3k / ⭐ 25 / Kotoba Whisper v2.0 は CTranslate2 と faster‑whisper で使用するために CTranslate2 フォーマットに変換され、インストール手順、推論例、Apple M2 ベンチマーク、変換手順を提供します。
 * [japanese-hubert-base-phoneme-ctc-v4](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v4) - 📥 2k / ⭐ 4 / Fine‑tuned Japanese Hubert‑Base for CTC phoneme recognition (v4) は、更新された sentence‑filtering rules、pronunciation adjustments、GPU を A6000 に切り替えた上で、110k ステップでトレーニングを停止しました。
 * [qwen3-asr-1.7b-ja-anime-GGUF](https://huggingface.co/cstr/qwen3-asr-1.7b-ja-anime-GGUF) - 📥 2k / ⭐ 2 / GGUF量子化されたQwen3‑ASR‑1.7Bは日本のアニメ/ギャルゲームの音声向けにファインチューニングされており、30以上の言語とCrispASRをサポートします。サイズは約1.3 GB（Q4_K）と約2.5 GB（Q8_0）の2種類があり、Apache 2.0ライセンスで提供されています
 * [japanese-hubert-base-phoneme-ctc](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc) - 📥 2k / ⭐ 5 / rinna/japanese‑hubert‑base をベースにしたファインチューニング済みの日本語音素 CTC モデル。ReazonSpeech v2 データと pyopenjtalk‑plus ラベルで訓練され、新しい v2 リリース（prj-beatrice/japanese-hubert-base-phoneme-ctc-v2）で精度が向上しています。
 * [parakeet-tdt-0.6b-ja-GGUF](https://huggingface.co/cstr/parakeet-tdt-0.6b-ja-GGUF) - 📥 2k / ⭐ 1 / GGUF変換された0.6 B日本語パラケートTDT‑CTCモデルは、CrispASRのCLIでTDTデコーディング（CTCフォールバック）に使用でき、JSUTで6.4 % CERを達成し、ワードレベルタイムスタンプを提供します。完全な1.24 GBビット正確ビルドと約470 MBのQ4_K量子化バリアント（8トークン後に劣化するためF16が推奨）で利用可能です。
 * [kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) - 📥 2k / ⭐ 34 / Kotoba‑Whisper v1.1 は、kotoba‑whisper‑v1.0 を拡張し、シームレスな punctuation‑adding 後処理パイプラインを備えた日本語ASRモデルです。複数の Whisper ベースラインと比較して、文字起こしの精度が向上し、レイテンシが低減されます。
 * [Qwen3-ASR-1.7B-JA-Anime-Galgame-hf](https://huggingface.co/jaykwok/Qwen3-ASR-1.7B-JA-Anime-Galgame-hf) - 📥 1k / ⭐ 1 / Hugging Face互換のQwen3‑ASR‑1.7B‑JA‑Anime‑Galgameチェックポイント変換で、微調整済み重みを保持しつつ、レイアウトをネイティブTransformers読み込みに適応させ、日本語アニメ/ギャルゲーム音声生成をサポートします
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 1k / ⭐ 18 / Kotoba‑Whisper‑v2.1は、日本語のASRモデルであり、統合されたpunctuation‑postprocessing pipelinesを備えてkotoba‑whisper‑v2.0を拡張しています。これにより、同等のCER性能を保持しながら、シームレスでpunctuation‑aware transcriptionが可能になります。
 * [wav2vec2-large-japanese](https://huggingface.co/NTQAI/wav2vec2-large-japanese) - 📥 1k / ⭐ 9 / ファインチューニング済みの日本語Wav2Vec 2.0 largeモデル（Facebookのwav2vec2‑large‑xlsr‑53をベース）で、Common Voice、JSUT、TEDxJPなど600時間以上のパブリックデータで訓練され、16 kHz音声認識に正確な性能を発揮します。Hugging Face Transformers経由で利用可能で、PyTorchでの使用例も付属しています

### fill-mask
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 474k / ⭐ 9 / 171 GBの日本語Wikipedia、CC‑100、OSCARでトレーニングされた日本語DeBERTa V2 large modelは、文字レベルのsentencepieceトークナイズと全単語マスキングを使用し、Hugging Face Transformersを通じて下流でのファインチューニングに準備できています。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 372k / ⭐ 40 / Japanese‑Roberta‑Base は rinna Co., Ltd. が開発した事前学習済みのマスク言語モデルで、正しいロード方法、トークン前処理、位置ID処理、および使用例に関するガイドラインがあり、先頭に `[CLS]` トークンが必要であることと、一貫したトークン化を強調しています。
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 369k / ⭐ 76 / 2019年の日本語Wikipediaを対象に、IPA辞書と全単語マスキングを用いて事前学習されたJapanese BERT‑base、12層、768次元、32,000語語彙、512トークンシーケンス、1Mステップ、CC‑BY‑SAの下でcl‑tohoku/bert‑japaneseから入手可能。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 157k / ⭐ 42 / 約17 Mの日本語Wikipedia文（2.6 GB）で事前学習済みのBERT base modelで、IPA dictionaryとWordPieceでトークナイズし、12層／768-dim hidden states／12 headsを有し、32 000-token vocabularyを備え、1 MステップでCloud TPUs上で訓練され、CC‑BY‑SA 3.0でリリースされています。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 105k / ⭐ 49 / 132 Mパラメータの日本語 ModernBERT モデルで、ローカルグローバルとRoPE注意を組み合わせ、4.39 T トークン（日本語/英語）で訓練され、102 kサイズの語彙、最大8,192トークン長、Flash Attention 2 に最適化されています
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 61k / ⭐ 6 / BERT‑base Japanese model（12層、768‑次元の hidden states、12ヘッド）を、30 M Wikipedia 文（約4 GB）で Unidic 2.1.2 を用いた単語レベルトークン化の後、文字レベルトークン化と全単語マスクを行い、512トークンのシーケンス、256バッチ、1 M トレーニングステップで訓練しました。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 26k / ⭐ 26 / ModernBERT‑Ja‑310M は local‑global attention と RoPE を組み合わせた日本語 BERT 変種で、4.09 T tokens の日本語／英語テキストで訓練され、102 400語の語彙、8 192トークンのシーケンスをサポートし、Flash Attention 2 用に最適化されています。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 17k / ⭐ 26 / Japanese BERT‑base (12 layers, 768 hidden, 12 heads) は、Unidic 2.1.2 単語レベルトークナイゼーション、WordPiece サブトークナイズ、および whole‑word マスクリングを使用し、4 GBの日本語Wikipedia（約30 M文）で事前学習されています。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 13k / ⭐ 8 / 日本語のBERT‑baseモデル（12層、768次元の隠れレイヤー、12ヘッド）は、MeCab IPA単語レベルトークン化を経て文字レベルトークン化で4000語語彙に変換し、約1700万文（2.6 GB）の日本語Wikipediaで事前学習されました。学習コードはcl‑tohoku/bert‑japaneseにあり、CC BY‑SA 3.0 でリリースされています。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 7k / ⭐ 2 / Japanese DeBERTa V2 tinyは、約171 GBの日本語Wikipedia、CC‑100、およびOSCARコーパスで事前学習され、Juman++による形態素解析が必要です。8台のNVIDIA A100 GPUを使用して33時間で訓練され、下流タスクに微調整できます。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 6k / ⭐ 1 / 日本語のDeBERTa‑V2ベースモデルで、171 GBの日本語Wikipedia、CC‑100、およびOSCARテキストをキャラクターレベルトークン化とワードレベルマスクで事前学習し、8台のA100 GPUで20日間訓練済みで、下流のファインチューニングに準備完了です。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 6k / ⭐ 30 / 日本語 DeBERTa V2 ベースモデルは、171 GBの日本語 Wikipedia、CC‑100、OSCAR データを用いて Juman++ セグメンテーションと SentencePiece トークン化で事前学習され、8枚の NVIDIA A100 GPU を 3週間使用してトレーニングされ、ファインチューニングに向けて準備ができています。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 6k / ⭐ 50 / LINE DistilBERT Japanese は、インハウスの BERT‑base 先生を用いて 131 GB の日本語ウェブテキストで事前学習された 66 百万パラメータの DistilBERT モデルであり、JGLUE で評価され、MeCab Unidic と SentencePiece でトークナイズされ、Apache 2.0 ライセンスの下でリリースされました。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 5k / ⭐ 5 / DeBERTaV2 base は日本語コーパス（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）でトレーニングされ、FP‑16 ファインチューニングで NLU タスク（JSTS、JNLI、JCommonsenseQA）に適用され、CC BY‑SA 4.0 の下でリリースされ、日本の研究助成金で資金提供されました。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 2k / ⭐ 8 / ModernBERT‑Ja‑30Mは、ローカルおよびグローバル注意機構をRoPEと組み合わせた日本語BERTバリアントです。4.39 TBの日本語／英語テキストで訓練され、8,192トークンのシーケンスをサポートし、30 Mから130 Mパラメータのサイズで提供され、Flash Attention 2との組み合わせで最も効果的です。
 * [bigbird-base-japanese](https://huggingface.co/nlp-waseda/bigbird-base-japanese) - 📥 1k / ⭐ 5 / 日本語のWikipedia、CC‑100、およびOSCARで事前学習されたJapanese BigBird‑Baseモデル。Juman++とSentencePieceを用いてトークナイズされ、下流タスクに対して微調整可能であり、JGLUEベンチマークで報告された性能がある。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 2.6 GBのWikipedia（約1700万文）で訓練された12層、768次元のBERT‑Base日本語モデルで、IPA‑dictionary文字トークナイズとwhole‑word maskingを使用し、CC‑BY‑SA 3.0でリリースされた。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 1k / ⭐ 32 / Japanese RoBERTa‑baseはJapanese WikipediaとJapanese CC‑100で事前学習され、Juman++の単語分割とSentencePieceのトークナイズを使用し、1週間で8台のNVIDIA A100 GPU上でAdam（lr = 1e‑4、native AMP）で訓練され、微調整可能で、JGLUEにおける結果が報告されている。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 673k / ⭐ 81 / Ruri v3 は、ModernBERT‑Ja をベースとした最先端の日本語テキスト埋め込みモデルで、最大8,192トークンの入力、100Kトークンの語彙、FlashAttention で加速された推論、および高速な sentence‑transformer での使用のための複数サイズバリアントをサポートします。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 237k / ⭐ 10 / Ruri v3 は、ModernBERT‑Ja をベースに構築された最先端の日本語テキスト埋め込みモデルで、最大 8,192 トークン、100 k‑トークン語彙、FlashAttention 加速、37 M から 315 M の複数サイズに対応しています。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 208k / ⭐ 24 / GLuCoSE v2 は CPU‑フレンドリーな日本語テキスト埋め込みモデルで、蒸留とマルチステージ対照学習によって微調整され、MIRACL や関連ベンチマークで同規模のモデルを上回る優れた意味的類似度と検索性能を提供します。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 47k / ⭐ 7 / Ruri v3は、ModernBERT‑Jaをベースに構築された最先端の日本語テキスト埋め込みモデルで、8192トークンまでのシーケンス、10万語の語彙、FlashAttentionに対応し、sentence‑transformers用に30 M〜310 Mパラメータのサイズでリリースされます。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 26k / ⭐ 5 / Ruri v3は、8192トークンまでの高性能日本語テキスト埋め込み、100kトークン語彙、FlashAttentionサポート、および30 m–310 mの複数モデルサイズを備え、sentence‑transformersを介した効率的な推論とファインチューニングを可能にします。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 25k / ⭐ 34 / GLuCoSEは、LUKEをベースに構築された日本語文埋め込みモデルであり、ウェブおよびNLI／検索データで訓練され、最大512トークンまでの768次元平均プールベクトルを出力します。類似度ベンチマークで0.864のSpearmanと0.818のPearsonを達成しています。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 16k / ⭐ 45 / リリース準備済みのRuri v3日本語テキスト埋め込みモデル（30m–310m）のコレクションで、SentenceTransformerの使用ヒント、クエリ/パッセージプレフィックス、JMTEBベンチマーク結果を含み、他の日本語および多言語埋め込みと比較しています。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 10k / ⭐ 13 / 日本語一般テキスト埋め込みモデル（Ruri‑v3、30‑310 Mパラメータ、8192‑token最大、JMTEBスコアが高い）は、Sentence‑Transformers使用例と他の日本語埋め込みとのベンチマーク比較とともに提供されています。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 8k / ⭐ 48 / PLaMo‑Embedding‑1B は、Preferred Networks が提供する日本語テキスト埋め込みモデルで、情報検索、分類、クラスタリングのために日本語テキストをベクトルに変換します。JMTEB ベンチマークで高い性能を示し、Apache v2.0 license の下で無料で利用できます。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 7k / ⭐ 17 / JaColBERTv2は、日本語専用のColBERTベースの検索モデルで、MMarcoで知識蒸留（31）ノルゲート／1件の正例、250kステップ、バッチ32）を使って訓練されており、現在はmultilingual‑e5‑large、BGE‑M3、JaColBERTを上回っています。完全な評価は保留中です。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 7k / ⭐ 9 / Ruri v3 Japanese text embeddings（30 M–310 M parameters, 8192‑token limit, JMTEB 74.5–77.2）を含み、Sentence Transformers 用の「クエリ:」または「文章:」prefixes での指示、および Sup/Unsup SimCSE、GLuCoSE、LaBSE など複数の日本語モデルのベンチマーク結果を含みます。
 * [ruri-large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2) - 📥 3k / ⭐ 10 / 日本語一般テキスト埋め込みリポジトリ Ruri は、30 M から 310 M パラメータまでの v3 モデルを提供し、JMTEB スコアを提示しています。sentence_transformers で（「クエリ: 」／「文章: 」接頭辞を使用）ロードする方法を示し、複数の日本語埋め込みモデルを比較したベンチマーク結果を提供します。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 3k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite は 768 次元の sentence‑transformer で、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、shunk031/jsnli 上で 1 エポックでトレーニングされ、クラスタリング、セマンティック検索、さらに Sentence‑Transformers と HuggingFace の両方の使用例を含んでいます。
 * [simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) - 📥 1k / ⭐ 15 / JSNLIデータセットでファインチューニングされた、tohok u/bert‑base‑japanese‑v2から派生した日本語SimCSEモデル。CC‑BY‑SA 4.0の下でリリースされ、fugashi/unidic‑liteトークナイゼーションを使用したsentence‑transformersで利用可能です

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 557k / ⭐ 51 / 日本語 Sentence‑BERT v2 は、cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking を MultipleNegativesRankingLoss でファインチューニングし、v1 に比べて約1.5〜2 % の精度向上を実現。sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 としてリリースされました。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 206k / ⭐ 56 / 日本語対応の T5 モデルは、Wikipedia と OSCAR データ約100 GB を SentencePiece トークナイズで事前学習し、ニュース分類ベンチマークで Google’s multilingual T5 を上回るが、ファインチューニングが必要で、バイアスのある出力が生成される可能性がある。
 * [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) - 📥 115k / ⭐ 5 / Japanese HuBERT Base、12層トランスフォーマーでrinnaのオリジナルを模倣し、約19,000時間のReazonSpeech v1日本語音声で訓練され、Apache 2.0ライセンスで公開されています。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 33k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 は、ViT‑B/16 をベースにした Apache‑2.0 ライセンスの日本語 CLIP モデルで、CC12M のキャプションを日本語に翻訳して訓練され、2022 年 5 月 12 日にリリースされました。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 26k / ⭐ 30 / LY Corporation の clip‑japanese‑base は、約 1 B の画像‑テキストペアで学習された日本語 CLIP モデルで、Eva02‑B トランスフォーマー画像エンコーダーと12層の BERT テキストエンコーダーを使用し、STAIR で R@1 0.30、Recruit で 0.89 の精度、ImageNet‑1K で 0.58 の精度を達成し、ゼロショット画像分類と検索をサポートしています。
 * [japanese-hubert-large](https://huggingface.co/yky-h/japanese-hubert-large) - 📥 15k / ⭐ 2 / Japanese HuBERT Largeは、rinna Co., Ltd.が開発した24層、16ヘッドのTransformerモデルで、ReazonSpeech v1日本語音声約19,000時間を用いて訓練されました。2024年3月7日にApache 2.0ライセンスの下で公開されています。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 13k / ⭐ 11 / 文埋め込みを生成するJapanese Sentence‑BERT (v1) モデルで、改良版v2が利用可能で、Hugging Face Transformers とカスタム `SentenceBertJapanese` クラスを使用したサンプル使用例があります。
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 9k / ⭐ 4 / fastTextは軽量でオープンソースのライブラリで、標準CPU上で単語および文の埋め込みと分類器を高速に学習します。数十億語を数分で学習でき、モバイル用途向けに圧縮可能で、分類や言語識別のための事前学習済みベクトルを提供します。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 4k / ⭐ 27 / Sarashina‑Embedding‑v2‑1B は、1,792 次元の日本語文変換器であり、マルチステージ対照学習 (multi‑stage contrastive learning) によって訓練され、最先端の JMTEB スコアを達成しています。また、意味的類似度、検索、パラフレーズ・マイニング、分類、クラスタリングに利用でき、Sentence‑Transformers を通じてオプションの instruction prefixes 付きで使用可能です。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 3k / ⭐ 14 / 日本語Sentence‑LUKEモデルは、Sentence‑BERTと同じデータセットで訓練され、同等にするかそれを上回る性能を有し、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、Hugging Face Transformers の MLukeTokenizer と LukeModel を介して使用される。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 3k / ⭐ 2 / ja_ginza_electra は、mC4 と UD_Japanese_BCCWJ r2.8（megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator をベースにしたもの）でファインチューニングされた日本語 ELECTRA モデルを提供する spaCy v3 の Python パッケージです。カスタム bunsetu‑phrase 検出機能を備え、MIT ライセンスで配布されています。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 3k / ⭐ 18 / Japanese CLIP モデル clip‑japanese‑base‑v2 は、約20億画像‑テキストペアと蒸留でアップグレードされ、Eva02‑B 画像エンコーダと12層 BERT テキストエンコーダをペアリングし、前モデルよりも高い ImageNet‑1k 精度（0.708）を達成します。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 2k / ⭐ 3 / 日本語 BERT‑base モデルを JSNLI 上で教師付き SimCSE によってファインチューニングし、Sentence‑Transformers または HuggingFace を通じて CLS プーリングで公開、512 バッチサイズで 1 M のサンプルを用いて学習率 5 × 10⁻⁵、温度 5 × 10⁻⁵、64 タークン制限、BFloat16 精度でトレーニング。
 * [llm-jp-4-vl-9b-beta](https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta) - 📥 1k / ⭐ 16 / LLM‑jp‑4‑VL 9B beta は、llm‑jp‑4‑8b‑instruct と SigLIP‑2 を基に構築された 90億パラメータの日本語ビジョン‑ランゲージモデルで、InternVL3.0‑style の動的タイル処理と軽量 MLP プロジェクターを採用し、FineVision と Jagle での学習後に日本語ベンチマークで競合する性能を実現しています。

### text-ranking
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 308k / ⭐ 15 / Ruri‑v3 Reranker は、ModernBERT‑Ja をベースにした堅牢な日本語テキストリランカーで、最大 8,192 トークンのシーケンス、100k トークンの語彙、FlashAttention および SentencePiece tokenizer をサポートし、sentence‑transformers 経由で使用できます。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 72k / ⭐ 5 / 日本語でトレーニングされた CrossEncoder リランクラーは xsmall (384) から large (1024) まであり、さらに BGE‑v2‑m3‑v1 モデルも含まれます。ファインチューニング、推論、JQaRA、JaCWIR、MIRACL、JSQuAD のベンチマークスコアの例コードが付属しています。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 58k / ⭐ 7 / Japanese CrossEncoderリランカーモデルは、xsmall から large（BGE を含む）まであり、JQaRA、JaCWIR、MIRACL、JSQuAD で評価済み。sentence_transformers と HuggingFace 用の、すぐに利用可能な統合例も用意されています。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 43k / ⭐ 6 / 高速で軽量な日本語 Reranker v2 モデル（tiny、xsmall、small、base）は、ベンチマークスコアと GPU スピードを備え、sentence_transformers CrossEncoder と transformers ≥ v4.48 で使用でき、flash‑attn で高速化も可能です。また、CPU/ARM 用に ONNX/quantized フォーマットでも利用可能です。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 6k / ⭐ 2 / Sentence Transformers（クロスエンコーダー）で構築された日本語リランカー モデルは、`trust_remote_code` を介してロードでき、JQaRA、JaCWIR、およびMIRACL データセットでベンチマークされ、hotchpotch 組織から小〜大サイズで入手可能です。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 2k / ⭐ 8 / 日本語Reranker v2スイートは、CrossEncoderとベースモデルをtinyからlargeまで公開し、各モデルにベンチマークスコアとGPU推論時間を添付します。また、HuggingFace Transformers ≥ 4.48（高速推論のためにオプションで flash‑attn）が必要です。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 2k / ⭐ 12 / Sentence Transformersで構築された日本語クロスエンコーダリランカーは、各サイズのRuri‑Rerankerモデルに対する推論利用例とベンチマーク結果を示します。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / Japanese CrossEncoder Reranker モデル (xsmall, small, base, large, BGE‑v2 m3) は、hidden size が 384–1024 の範囲です。sentence_transformers と Hugging Face を用いた推論例で、JQaRA、JaCWIR、MIRACL、JSQuAD で 0.71–0.97+ のスコアを記録しています。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 1k / ⭐ 3 / Japanese‑reranker‑small‑v2は、軽量で高速な日本語リランクモデルシリーズ（v2）です。tiny〜baseバリアントを提供し、平均スコア0.89まで達し、2〜15秒のGPU推論で実行できます。さらにクロスエンコーダオプションも利用可能です。加速のためにオプションでFlash Attention 2を使用できるHugging Face Transformers v4.48+が必要です。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 1k / ⭐ 16 / 日本語向け CrossEncoder リランカー モデル（xsmall から large まで）は、日本語テキストで学習され、sentence_transformers を通じて公開され、JQaRA、JaCWIR、MIRACL、JSQuAD で評価されます。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 743k / ⭐ 16 / 新しい VNTL データセットに基づく LLaMA 3 Youko qlora ファインチューニング。日本のビジュアルノベルを英語へ正確かつ文字通りに翻訳することに最適化されており、チャットモードは使用せず、デフォルトの LLaMA 3 プロンプトを使用し、ニュートラルサンプリング（温度 0、繰り返しペナルティ無し）を推奨する。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 181k / ⭐ 14 / Sugoi LLM 14B Ultra (GGUF) は、BLEUスコアが21.38の日本語‑英語翻訳モデルで、以前の13.67のほぼ二倍に近い点数です。RPG‑Makerの括弧付きテキストに優れ、プロンプトに強く従う性質と、インタラクティブチャットUIs用のJSON出力を実現します。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 48k / ⭐ 75 / OpusコーパスからのJapanese‑to‑English Transformer‑Align MT modelは、正規化とSentencePiece前処理を使用して、Tatoebaテストセットで41.7 BLEUと0.589 chr‑Fを達成します。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 27k / ⭐ 33 / FuguMT は、日本語→英語の Marian‑NMT 翻訳モデルで、transformers と SentencePiece により構築され、Tatoeba で 39.1 BLEU を記録しました。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 3k / ⭐ 55 / FuguMTはHugging Face TransformersおよびSentencePieceで構築されたMarian‑NMTベースの英日翻訳モデルで、Tatoebaで32.7のBLEUスコアを達成しています。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 2k / ⭐ 123 / PLaMo Translation Model は Preferred Networks が開発した翻訳タスク向けの大規模言語モデルで、ベース、ポストトレーニング、評価バリアントが用意されています。PLaMo community license の下で公開され、チャットやその他のダウンストリーム用途向けにインストラクションチューンは行われていません。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 2k / ⭐ 39 / Fine‑tuned, GGUF‑quantized LFM2‑350M checkpoint は、短〜中長テキストに対するほぼリアルタイムの bi‑directional Japanese‑English 翻訳に使用でき、llama.cpp で利用可能です。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 458k / ⭐ 177 / Manga OCR は、縦書きと横書きの日本語漫画テキスト（フリガナを含む）を、さまざまなフォントと低品質画像でも読み取る Vision Encoder-Decoder OCR ツールで、ソースコードは無料で入手可能です。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 68k / ⭐ 6 / Meikiocrの `meiki.text.recognition.v0`――D‑FINEベースのMobileNetV4モデルで、日本語ビデオゲームテキストに特化して微調整されたもので――は、960×32入力から最大48文字まで検出し、それぞれの文字をバウンディングボックスと信頼度スコアとともに出力することで、水平テキストに対して最先端の精度と遅延を実現します。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 35k / ⭐ 3 / meikiocr は、ビデオゲーム向けに D‑FINE ベースのオープンウェイトテキスト検出モデル（v0.1、MobileNet‑v4 バックボーン、2種類の解像度バリアント、64 ボックス制限）と、実験的低遅延 tiny および small バリアント（日本のビデオゲームと漫画で訓練済み）を提供します。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 2k / ⭐ 4 / Manga OCRは、さまざまなフォントと低品質画像に対して縦書き・横書きテキストとふりがなオーバーレイを含む日本漫画の高品質なOCRを提供するVision Encoder‑Decoder systemです。また、一般的な印刷された日本語OCRにも使用できます。
 * [manga-ocr-2025-onnx](https://huggingface.co/l0wgear/manga-ocr-2025-onnx) - 📥 2k / ⭐ 9 / ONNX Vision‑Encoder‑Decoder Manga OCRモデルは、kha‑whiteのmanga‑ocrとjzhang533の2025ベースラインに基づいて構築されており、縦書き・横書き日本語テキスト、ふりがな、オーバーレイ、および低品質画像をサポートします。manga109‑sと合成データで訓練され、Hugging Face Optimum経由でTrOCRProcessorおよびORTModelForVision2Seqを使用してデプロイ可能です
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 1k / ⭐ 32 / Sarashina2.2‑OCRは、3BパラメータのエンドツーエンドOCRモデルであり、人間の嗜好最適化後に日本語と英語の文書をMarkdownに解析し、テーブルはHTML、数式はLaTeX、図像はバウンディングボックスアノテーションに変換します。高解像度の視覚‑言語理解を実現するため、SigLIP2ベースのビジョンエンコーダとSarashina2.2‑3B‑Instruct LLMを統合しています。

### text-classification
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 28k / ⭐ 16 / Amazonの商品レビューに対して感情分類のためにFine‑tuned Japanese BERT (cl‑tohoku/bert‑base‑japanese‑v2) を使用し、6エポックで学習率 2 × 10⁻⁵ を設定した結果、約81 % の精度と0.73のF1スコアを達成しました。
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 15k / ⭐ 6 / 日本語版 BERT BASE を WRIME データセットでファインチューニングしたモデルは、作家と読者の 8 つの感情（喜び、悲しみ、期待、驚き、怒り、不安、嫌悪、信頼）に対して 0〜4 の強度スコアを予測し、コードは公開済みです。K80 GPU 上で 3 時間で訓練し、作家では約 0.6 MSE、読者では約 0.2 MSE を達成しました。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 3k / ⭐ 2 / 「Large Language Model Introduction」の第5章で紹介された、日本語 BERT‑based モデル。JGLUE JSTS データセットで意味的類似度スコアリングのためにファインチューニングされ、Colab ノートブック、transformers‑pipeline の使用方法、Apache 2.0 ライセンス付き。
 * [bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - 📥 3k / ⭐ 9 / MARC‑ja JGLUE データセットで感情分析用にファインチューニングされた Japanese BERT‑Base v3、cl‑tohoku/bert‑base‑japanese‑v3 から構築され、Hugging Face `pipeline` と互換性があり、Apache License 2.0 の下でリリースされています。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 2k / ⭐ 15 / 日本語感情分析モデルは、chABSAデータセットで学習され、損失0.0001、精度1.0、F1スコア1.0を達成しました。Transformers 4.24.0およびPyTorch 1.12.1+cu113で構築され、Adam（学習率2e‑05、10エポック、バッチサイズ16）で最適化され、`model(**inputs)`で評価されました。

### token-classification
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 12k / ⭐ 11 / cl‑tohoku/bert‑base‑japanese‑v2 を使用した日本語 NER は、`BertForTokenClassification` を介して 8 つのエンティティタイプ（企業、政治・その他組織、施設、製品、イベント）を抽出し、Stockmark Wikipedia データセットで学習済みです。CC BY‑SA 3.0 ライセンスの下で `transformers`、`unidic_lite`、`fugashi` でインストール可能です。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 9k / ⭐ 11 / Wikipediaデータセット上の固有表現認識用に微調整された日本語 BERT‑Base は、*Large Language Model Introduction* の第6章で紹介され、Hugging Face transformers パイプライン（Apache 2.0 ライセンス）でデプロイできるものです。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 3k / ⭐ 27 / 日本語NERコーパス（タグ PER, ORG, LOC, INS, PRD, EVT）上で、5エポックのAdam（lr 5e‑5、バッチ12）を使用してFine‑tuneしたXLM‑RoBERTa‑baseは、0.0173の検証ロスを達成し、Transformers 4.23.1とPyTorch 1.12.1でリリースされました。
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 2k / ⭐ 4 / 日本語に特化した DeBERTa V3 モデルで、xsmall、base、large の各バリアントがあります。このモデルは推論時に形態素解析器を使用せず、語境界を尊重し、語彙を縮小（large モデルのみで BPE あり）し、Hugging Face と互換性があります。

### text-to-speech
 * [sarashina2.2-tts](https://huggingface.co/sbintuitions/sarashina2.2-tts) - 📥 12k / ⭐ 66 / sarashina2.2-tts は、SB Intuitions LLM‑based の日本語中心の TTS システムで、高精度な日本語と英語合成を自然で表現豊かな声で提供し、ゼロショットクローン、クロスリンガル一貫性、およびシームレスなコードスイッチングを実現します。
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 3k / ⭐ 11 / 日本語のTTSモデル **tsukuyomi‑wavlm** は、tsukuyomiコーパスの100発話に対して300エポックでファインチューニングされ、WavLMディスクリミネーターとA1/A2/A3プロソディ特徴をVITSアーキテクチャ上で使用し、22.05kHzの合成を生成する61 MBのONNXファイルとしてエクスポートされます。

### any-to-any
 * [gemma-4-12B-it-qat-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-12B-it-qat-UD-japanese-imatrix) - 📥 3k / ⭐ 12 / CPUに優しい日本語最適化量子化Gemma 4モデル（1/4サイズ、Apache 2.0）で、完全にオンプレミスで動作し、開発者サポートと堅牢なベンチマークをオプションで提供します

### text-to-image
 * [stable-diffusion-xl-jp-base-1.0](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0) - 📥 2k / ⭐ 5 / 5.8 billion パラメータの SD‑XL 1.0 ベースモデルで、日本語用にファインチューニングされたもの。OpenCLIP‑ViT テキストエンコーダと multilingual‑e5 埋め込みを使用し、約28 百万の WMT‑Japanese/English ペアと約13 百万のフィルタ済み LAION2B キャプション（英語に翻訳）で訓練され、Open RAIL++‑M ライセンスの下でリリースされています。

### audio-to-audio
 * [LFM2.5-Audio-1.5B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF) - 📥 2k / ⭐ 31 / LiquidAI の LFM 2.5‑Audio 1.5B JP モデルの量子化 GGUF バージョン（言語、オーディオエンコーダー、およびボコーダー重み：F32/F16/Q8_0/Q4_0）と、llama.cpp を使用した ASR と TTS の CLI/Server ランナー。

### image-text-to-text
 * [Stockmark-Nemotron-3-Nano-Omni-JapanDocReader](https://huggingface.co/stockmark/Stockmark-Nemotron-3-Nano-Omni-JapanDocReader) - 📥 1k / ⭐ 8 / Stockmark‑Nemotron‑3‑Nano‑Omni‑JapanDocReaderは、NVIDIAのNemotron‑3‑Nano‑Omniをベースに構築された日本語多モーダルドキュメントリーディングモデルであり、混合VQAと構造化パーシングデータで微調整され、DAPOによって強化されて、VQA推論を保持しつつドキュメントパース品質を向上させています。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 126k / ⭐ 11 / Japanese‑language BERT‑Base (12 layers, 768‑dim, 12 heads)は、Unidic‑based word‑level plus character‑level tokenizationとwhole‑word maskingをCC‑100と2023 Wikipediaで事前学習し、7,027‑token vocabularyを生成する。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 69k / ⭐ 14 / Japanese‑BERT‑Large は CC‑100 と Wikipedia に対して訓練され、Unidic‑lite のワードレベルトークナイゼーションを使用し、WordPiece サブワードとホールワードマスクリングを採用しています（24 層、隠れ層 1024 次元、16 ヘッド、32k 語彙）。プリトレーニングコードは cl‑tohoku/bert‑japanese にあります。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 60k / ⭐ 64 / Japanese BERT‑base（12層、768次元の隠れ層、12ヘッド、32k語彙）は、CC‑100と2023‑Jan Wikipediaで全単語マスキングを用いて事前学習され、Unidic 2.1.2の単語レベルトークナイゼーション＋WordPieceを併用し、200万ステップで学習しました。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 16k / ⭐ 11 / ≈100 GB の Wikipedia と OSCAR CC‑100 データ（SentencePiece で 10:1 の混合、byte‑fallback を有する）で事前学習された日本語 T5‑v1.1 モデルで、下流タスクの微調整が必要です。転移学習サンプルコードが含まれ、出力に潜在的なバイアスを示唆しています。ライセンスは CC‑BY‑SA 4.0 です。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 8k / ⭐ 19 / Japanese DeBERTa V3 base は、LLM‑jp v1.0 から 540 B トークンで事前学習され、修正された DeBERTa V3 セットアップで訓練され、形態素解析器を使用しないユニグラム・バイトフォールバックトークナイザーを使用し、JGLUE NLUタスク用に微調整済みです。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 8k / ⭐ 13 / moonshotaiのMoonlight‑16B‑A3B‑InstructをTFMCのimatrix Japanese datasetで訓練したgguf-format版をリリースしました。llama.cpp（CUDA‑enabled）で使用でき、recipe‑request promptを実行して確認できます。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 5k / ⭐ 17 / 高性能日本語 SPLADE v2 は、WebUI demo を通じてスパース‑ベクトル変換と推論を可能にし、YAST でトレーニングを行い、YASEM 埋め込みを提供し、JMTEB ベンチマーク結果を報告します。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-32b-a3b-thinking-gguf) - 📥 4k / ⭐ 12 / TFMCの imatrix データセットで構築された llm‑jp‑4‑32b‑a3b‑thinking の GGUF フォーマット変換、CUDA 対応推論用に llama.cpp 経由で。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 3k / ⭐ 3 / A T5 v1.1 日本語モデルは、mC4/ja と Wikipedia で事前学習され、GEGLU 活性化を特徴とし、事前学習時にドロップアウトがなく、埋め込み/分類器層が分離され、d_model が大きくヘッド数が少ない構成です。商用利用は CC‑BY‑SA 4.0 ライセンスで許可されています。
 * [kana-whisper](https://huggingface.co/sbintuitions/kana-whisper) - 📥 3k / ⭐ 8 / Whisper large‑v3‑turboをファインチューニングしたモデルで、日本語音声をカタカナに文字起こしするASRコンポーネントとして、Sarashina2.2‑TTSプロジェクト内のJoyo Kanji Yomi Benchmarkに使用され、Kana CER Usage With Transformersパイプラインを動かします。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5-gguf](https://huggingface.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf) - 📥 3k / ⭐ 2 / tokyotech‑llm による Llama‑3.1‑Swallow‑8B‑Instruct‑v0.5 の GGUF conversion、TFMC/imatrix‑dataset‑for‑japanese‑LLM を組み込んだ、llama.cpp の Build/Run instructions 付き。
 * [Qwen3.5-2B-Ideal-TSUNDERE-Loli-Girl-Japanese-v1-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.5-2B-Ideal-TSUNDERE-Loli-Girl-Japanese-v1-i1-GGUF) - 📥 3k / ⭐ 1 / Weighted と imatrix の量子化は、Qwen3.5‑2B “Ideal TSUNDERE Loli Girl Japanese” モデルに対して GGUF 形式で提供されます（0.1 GB から 1.7 GB までのさまざまな IQ/K レベル）。リンク先には Hugging Face のページ、静的ダウンロード、およびマルチパートファイルを使用する方法に関するガイダンスが含まれています。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 75 / Llama‑3‑ELYZA‑JP‑8B は、日本語向けに強化された 8‑B Llama 3 モデルで、GGUF（Q4_K_M）と AWQ 量子化を備え、llama.cpp、LM Studio、または OpenAI‑compatible API で実行できます。
 * [YuisekinAIEvol-Mistral-7B-ja-math-v0.1.1-gguf](https://huggingface.co/mmnga/YuisekinAIEvol-Mistral-7B-ja-math-v0.1.1-gguf) - 📥 2k / ⭐ 2 / GGUF形式のYuisekinAIEvol-Mistral-7B-ja-math-v0.1.1（TFMC/imatrix-datasetベース）で、llama.cppで使用できるように準備済み。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 2k / ⭐ 16 / Sarashina2.2 は、SB Intuitions が三段階パイプラインと合成データを用いて訓練した 0.5‑B、1‑B、および 3‑B の言語モデルを提供し、最高の日本語 QA、数学、およびコーディングスコアを達成し、指示調整されていない事前学習済みの重みを提供するが、偏った出力を生み出す可能性があります。
 * [umiyuki-Umievo-itr012-Gleipnir-7B-gguf](https://huggingface.co/mmnga/umiyuki-Umievo-itr012-Gleipnir-7B-gguf) - 📥 2k / ⭐ 9 / gguf 形式の Umievo‑itr012‑Gleipnir‑7B（TFMC/imatrix‑dataset‑for‑japanese‑llm で訓練済み）が llama.cpp で動作できる状態です。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 2k / ⭐ 2 / DataPilotのArrowPro‑7B‑RobinHoodモデルをGGUFに変換したバージョンで、TFMC/imatrix データセットから構築され、llama.cpp とともに日本語 LLM タスクで使用可能です。
 * [llm-jp-4-8b-instruct-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-instruct-gguf) - 📥 2k / ⭐ 6 / imatrixデータから構築された「llm‑jp‑4‑8b‑instruct」のgguf‑format変換用コンテナ、LMStudio設定およびllama.cpp CUDAコマンドの例を含む。
 * [umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf](https://huggingface.co/mmnga/umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf) - 📥 2k / ⭐ 3 / GGUF変換済みの日本語チャットモデル「Japanese-Chat-Umievo-itr001-7b」は、TFMC/imatrix データセットから構築され、単一ファイルコマンドラインで llama.cpp で使用できます。
 * [sarashina2.2-3b-instruct-v0.1-gguf](https://huggingface.co/mmnga/sarashina2.2-3b-instruct-v0.1-gguf) - 📥 2k / ⭐ 9 / TFMC / imatrix‑dataset‑for‑japanese‑llm で構築された sbintuitions の sarashina2.2‑3b‑instruct‑v0.1 モデルの GGUF フォーマット変換。CUDA 対応推論は llama.cpp 経由で実行可能です
 * [Fugaku-LLM-13B-instruct-gguf](https://huggingface.co/mmnga/Fugaku-LLM-13B-instruct-gguf) - 📥 2k / ⭐ 6 / Fugaku‑LLM‑13B‑instruct‑gguf は、Fugaku‑LLM‑13B‑instruct の gguf フォーマット変換であり、TFMC/imatrix-dataset-for-japanese-llm からの imatrix データを使用して構築されており、ユーザーは利用規約に同意する必要があります。
 * [lightblue-suzume-llama-3-8B-japanese-gguf](https://huggingface.co/mmnga/lightblue-suzume-llama-3-8B-japanese-gguf) - 📥 2k / ⭐ 2 / Lightblue の suzume‑Llama‑3‑8B の日本語最適化 GGUF バージョン。TFMC/imatrix データで構築され、推論には llama.cpp と互換性があります。
 * [tokyotech-llm-Swallow-70b-instruct-v0.1-gguf](https://huggingface.co/mmnga/tokyotech-llm-Swallow-70b-instruct-v0.1-gguf) - 📥 1k / ⭐ 1 / 東京Tech LLMからGGUF変換された70 B Swallow‑instructモデルで、imatrix Japanese datasetで訓練され、llama.cppを使った推論に利用可能です。
 * [pfnet-nekomata-14b-pfn-qfin-gguf](https://huggingface.co/mmnga/pfnet-nekomata-14b-pfn-qfin-gguf) - 📥 1k / ⭐ 1 / pfnetのnekomata-14b-pfn-qfinモデルをGGUFに変換したバージョンで、TFMC/imatrixデータで構築され、Tongyi Qianwenライセンスの下でライセンスされています。llama.cppで使用する準備ができています
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 22 / pfnet の plamo‑2‑translate を imatrix データから構築し、TFMC/imatrix‑dataset‑for‑japanese‑LLM に基づく GGUF‑format リリースで、CUDA 対応ハードウェア上で llama.cpp を通じてコンパイル・実行する手順を含む。
 * [tokyotech-llm-Swallow-13b-instruct-v0.1-gguf](https://huggingface.co/mmnga/tokyotech-llm-Swallow-13b-instruct-v0.1-gguf) - 📥 1k / ⭐ 1 / 東京Tech-LLMのGGUF形式で提供される13B命令モデルで、TFMCの日本語データセットでファインチューニングされており、日本語プロンプト用にllama.cppと互換性があります。
 * [Llama-3-ELYZA-JP-8B-gguf](https://huggingface.co/mmnga/Llama-3-ELYZA-JP-8B-gguf) - 📥 1k / ⭐ 4 / GGUF‑converted Llama‑3‑ELYZA‑JP‑8B は elyza によって構築され、TFMC/imatrix‑dataset‑for‑japanese‑LLM で作られ、llama.cpp で使用できます。
 * [ArrowPro-7B-KillerWhale-gguf](https://huggingface.co/mmnga/ArrowPro-7B-KillerWhale-gguf) - 📥 1k / ⭐ 1 / ggufに変換されたArrowPro‑7B‑KillerWhaleモデル（TFMC/imatrix‑dataset-for-japanese‑LLMで訓練済み）が、llama.cppで使用可能です。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct-gguf](https://huggingface.co/mmnga/ELYZA-japanese-Llama-2-7b-fast-instruct-gguf) - 📥 1k / ⭐ 45 / ELYZAの7 b Japanese Llama‑2 instructモデルのGGUFを変換し、1.8×高速化のために日本語語彙を追加し、llama.cppでLlama 2 licenseの下で実行可能にしました。
 * [Vecteus-v1-gguf](https://huggingface.co/mmnga/Vecteus-v1-gguf) - 📥 1k / ⭐ 7 / Local‑Novel‑LLMからのVecteus‑v1のgguf形式変換で、imatrixデータセットを使用して構築され、llama.cppで`Vecteus‑v1‑Q4_0.gguf`経由で実行でき、他の関連モデルをリストしています。
 * [DataPilot-ArrowPro-7B-KUJIRA-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-KUJIRA-gguf) - 📥 1k / ⭐ 10 / GGUF形式のArrowPro‑7B‑KUJIRA、DataPilotが公開し、TFMC/imatrix-dataset-for-japanese-LLMから構築されたもので、Japanese LLM推論にllama.cppで使用可能です。
 * [karakuri-lm-8x7b-instruct-v0.1-gguf](https://huggingface.co/mmnga/karakuri-lm-8x7b-instruct-v0.1-gguf) - 📥 1k / ⭐ 2 / karakuri-aiがリリースしたGGUF形式のkarakuri‑lm‑8x7b‑instruct‑v0.1で、TFMC/imatrix‑dataset‑for‑japanese‑llmを使って訓練されており、提供されたコマンドライン経由で llama.cpp で使用できます
 * [Ninja-v1-NSFW-128k-gguf](https://huggingface.co/mmnga/Ninja-v1-NSFW-128k-gguf) - 📥 1k / ⭐ 11 / TFMC/imatrix‑dataset‑for‑japanese‑LLMから構築されたNinja‑v1‑NSFW‑128kモデルのGGUF‑format conversionを提供するリポジトリで、llama.cppで実行して日本語小説テキストを生成する手順が記載されています。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 1k / ⭐ 9 / Llama 3.1 Swallow v0.5 は、8 billion パラメータを持つ LLM で、Meta の Llama 3.1 を日本語とコード／数式推論で改善しつつ英語の流暢さを保持し、継続的なプリトレーニングと指示調整ファインチューニングを合成日本語データで実現したものです。
 * [tokyotech-llm-Llama-3.3-Swallow-70B-Instruct-v0.4-gguf](https://huggingface.co/mmnga/tokyotech-llm-Llama-3.3-Swallow-70B-Instruct-v0.4-gguf) - 📥 1k / ⭐ 1 / tokyotech-llmのLlama 3.3 Swallow 70B InstructモデルをGGUFに変換したバージョンで、TFMC imatrixデータセットから構築され、CUDA上のllama.cppと共に使用可能です
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 1k / ⭐ 1 / 高度に最適化されたGGUFバージョンのgoogle/gemma‑4‑E4B‑itは、Unsloth Dynamic Quantization 2.0と広範なバグ修正を使用して日本語能力に最適化されており、llama.cppで動作し、最低16 GBのRAMと6 GBのディスクが必要で、GPUは任意です。
 * [Llama-3-Swallow-70B-Instruct-v0.1-gguf](https://huggingface.co/mmnga/Llama-3-Swallow-70B-Instruct-v0.1-gguf) - 📥 1k / ⭐ 8 / tokyotech‑llm がリリースした Llama‑3‑Swallow‑70B‑Instruct‑v0.1 の gguf フォーマット変換。TFMC/imatrix‑dataset‑for‑japanese‑llm で訓練され、llama.cpp（例：`./main -m 'Llama-3-Swallow-70B-Instruct-v0.1-Q4_0.gguf'`）経由で利用可能です。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 1M / ⭐ 74 / 2009年から2024年までのNicoNico Liveのコメントログ（150GB超）を集約し、転換前・転換後・リアルタイムNX‑Jikkyoのキャプチャも含む、歴史的なTV‑broadcastディスカッションを簡単に取得できるAPIを提供します。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 12k / ⭐ 7 / VOICEVOX生成の合成音声データセットで、445,793件の.wavファイル（総計577時間51分23秒）から構成され、ITA、つくよみちゃん、およびROHANコーパスを使用して作られた。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 10k / ⭐ 33 / FineWeb2 Edu Japanese は FineWeb2 からの約1億2000万の高品質教育用日本語テキスト（約893億トークン）を提供し、DeepSeek‑API クラスフィケーター（スコア ≥ 2.5）でフィルタリングし、ModernBERT‑Ja‑130M でトークナイズされ、512 トークン以下の小規模サブセットを含みます。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 6k / ⭐ 9 / Cauldron‑JAは、DeepL APIを使ってThe Cauldronから翻訳された44個のサブデータセットからなる日本語ビジョン‑ランゲージデータセットです。HuggingFace’s datasets library を通じて入手可能で、オリジナルセットと同一のライセンスで提供され、プロンプトはCC‑BY‑4.0でリリースされています。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 5k / ⭐ 11 / Hugging FaceにホストされているReazon Speech v2 Japaneseデータセットのミラー。CDLA‑Sharing‑1.0の下で配布され、利用は日本著作権法第30‑4条に限定されます。16 kHz FLAC音声ファイルが4,096件、対応する転写がTSV/CSV形式で含まれています。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 3k / ⭐ 126 / Nemotron‑Personas‑Japan は、CC BY 4.0 のオープンソースデータセットであり、高品質の合成生成された日本人ペルソナ（名前、性別、年齢、背景、婚姻状況、学歴、職業、所在地を含む）で、実際の人口統計・地理・人格分布に基づいており、確率的グラフィカルモデルと GPT‑OSS‑120B を用いて多様性を高め、バイアスを減らし、モデル崩壊を防ぎ、主権 AI の開発を支援し、商業利用をサポートするよう設計されています。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 3k / ⭐ 36 / Galgame VisualNovelデータセット (OOPPEENN/566973746F6F6372656164656C65746572) の再構成された再アップロード。Hugging Face datasets の効率的な読み込みのため、すべてのオリジナル音声/テキストを保持し、複数のゲームサブセットオプションを備えた抽出スクリプトを提供します。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 3k / ⭐ 18 / JMTEBは日本語テキスト埋め込みベンチマークで、5つのタスク（クラスタリング、分類、STS、検索、リランキング）と28のデータセットを特徴とし、1行で評価できるスクリプトを提供し、コミュニティの貢献を歓迎する。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 2k / ⭐ 47 / Aozora Bunkoから取得したパブリックドメイン日本語テキストのユーザーフレンドリーで重複除去済みCSVデータセット。globis-org/aozorabunko‑extractorで処理され、現代日本語機械学習用途に合わせてクリーニング済み。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 2k / ⭐ 15 / 『Large Language Model Introduction』で使われるJGLUE datasetのデータセットカード。元のリポジトリ (original repo) から取得し、コードはCC BY‑SA 4.0でライセンス、データは配布者のライセンスに基づく。Kurihara & Kawahara（日本語）を引用し、Shunsuke Kitada’s repository をベースに構築。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 2k / ⭐ 6 / 日本語のMC4データセット (mc4-ja) のデータセットカード
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 100 / 注釈付きタスク（要約訂正、数学推論、翻訳、創造的生成、ユーザー意図理解など）を網羅した100サンプルの日本語インストラクション・チューニング評価データセット。微調整モデルを手動または自動で5点評価できるよう設計されている。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 2k / ⭐ 7 / JMedBenchは日本語医療・生物医学用LLMベンチマークであり、20のデータセットをMCQA、NER、STSなどを含む5つのタスクにまたがって構成しています。データセットはMedMCQA、PubMedQA、MMLUなどから取得されており、それぞれに独自のライセンスが付属しています。また、翻訳にバイアスが含まれる可能性があるため、人間によるレビューが必要であるという注意事項が記載されています。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 2k / ⭐ 144 / Japanese Anime Speech Dataset V2は、292,637件の整理済みオーディオ‑テキストペア（約397.5時間のSFW、および52.4時間のNSFWコンテンツ）を、セーフティ別に分割された128‑kbps MP3ファイルとして提供し、特に自動音声認識モデルのトレーニング用に設計されています。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 1k / ⭐ 49 / Japanese‑Eroge‑Voice‑V2は、匿名化された1,033,142件のエロゲ音声–文字起こしペア（主に女性、NSFW）を2,657時間提供し、学術研究向けにMITライセンスで配布します。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 1k / ⭐ 47 / 日本語 NLP ベンチマーク（Yahoo Japan と早稲田大学が作成）に対する JGLUE データセットカードとロードスクリプトを更新しました。テキスト分類（MARC‑ja、JCoLA）、文対分類（JNLI）、QA（JSQuAD、JCommonsenseQA）をカバーし、リリースは GitHub と Hugging Face にリンクされています。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 6 / JamC‑QA は、8つの日本文化・知識カテゴリにわたる多肢選択問題のバイリンガルベンチマークで、リーダーボードメトリクスで最先端モデルを比較します。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 1k / ⭐ 2 / 18,612 の日本語訳された Python の指示–応答ペア（GPT‑4o‑mini で生成し、元の英語プロンプト、コード、および例を保持）で、訓練、微調整、チャットボット、研究、教育などの多様なコーディングタスクを提供し、すべて MIT ライセンスで公開されています。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 1k / ⭐ 16 / 日本語および多言語のQA、NLI、パラフレーズデータセットのカタログで、各データセットの検索またはQAタスクとライセンス（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）を詳細に記載。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 997 / ⭐ 14 / EDINET‑Bench は、10 年分の EDINET‑API 公開レポートを使用して、会計不正検出、収益予測、業界予測などのタスクで LLM を評価する日本の金融ベンチマークです。構築・評価コードが提供され、データセットは PDL 1.0 に再ライセンスされています。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 902 / ⭐ 14 / 「wikipedia-ja-20230720」日本語ウィキペディアスナップショットのデータセットカード。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 859 / ⭐ 5 / 再配布、AIトレーニング、商業利用を禁止し、アクセスには手動承認が必要なゲート付き非商用派生データセット（EDINET XBRL財務データ）
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 838 / ⭐ 6 / 『oscar2301‑ja‑filter‑ja‑normal』のデータセットカード―Oscarコーパスの日本語フィルタリング済みかつノーマルサブセット。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 809 / ⭐ 5 / 日本語変種「mc4‑ja‑filter‑ja‑normal」のデータセットカード、追加情報は保留中です。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 741 / ⭐ 89 / databricks‑dolly‑15k データセットの自動翻訳された日本語版、CC‑BY‑SA‑3.0 ライセンス、2023‑05‑11に最終更新。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 739 / ⭐ 3 / 日本語の指示データセットで、632,636 のマルチターンサンプル（約6.35 Bトークン）と、GPT‑OSS‑120b の推論トレースが含まれ、オープンエンド、数学、執筆、MCQA タスクで、135 の金融トピックと 20 の一般トピックを網羅し、LLM の推論を金融でファインチューニングするよう設計されています。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 727 / ⭐ 4 / JFWIRは、6 400万件を超える文書–クエリペアから構成される大規模な日本語情報検索データセットです。高品質の教育ウェブコンテンツから生成され、7種類のクエリタイプとハードネガティブを備えており、対照学習の改善やJQaRA、MIRACL(ja)、jsquad、JaCWIRなどのタスクにおける性能ベンチマークに利用されます。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 708 / ⭐ 8 / Rakuda は 40 件の日本語質問—歴史・社会・政府に関する自由回答形式と地理に特化した質問—を提供し、日本語 AI アシスタントのベンチマークに使用でき、vicuna‑eval と比較可能で、`datasets.load_dataset` で読み込むことができます。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 707 / ⭐ 5 / Japanese JaQuAD、QG‑Bench のサブセットは、文レベルおよび段落レベルのデータを提供し、ハイライトされた回答トークンを用いて日本語の質問生成モデルの学習に利用でき、BLEU4、METEOR、ROUGE‑L、BERTScore、MoverScore で評価されます。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 688 / ⭐ 61 / AnswerCarefully Datasetは、商業利用または非商業利用のLLM安全向上のために日本語および多言語データを提供し、他の使用（安全迂回を含む）を禁止し、帰属を伴う派生作品を許可し、害やサービス変更に対する非責任の創作者免責事項を付帯しています。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 679 / ⭐ 157 / Japanese Anime Speech Dataset は、73,004 の音声‑テキストペア（合計110時間、V1 から V5 へと進化）を提供し、OpenAI’s Whisper などの ASR モデルを強化します。すべての利用に対してオープンライセンスが適用され、クレジットの表記があれば感謝します。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 630 / ⭐ 5 / Fate/Stay Nightのキャラクター「Emilia」の対話とロアのデータセットで、会話型言語モデルのトレーニングと評価のためにフォーマットされています。
 * [ogiri-bokete](https://huggingface.co/datasets/YANS-official/ogiri-bokete) - 📥 605 / ⭐ 4 / ボケテクラウドソーシングサイトからの日本語のみデータセットで、テキスト→テキスト、画像→テキスト、テキスト内画像補完という3つのタスクに分割されており、1 000件のプロンプト（画像500件、その他各100件）と、1つのプロンプトあたり最大約2 300件の回答が含まれます。OCRで前処理され、不適切コンテンツはフィルタリングされ、CLoT‑Oogiri‑Go CVPR2024 コーパスから派生しています。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 584 / ⭐ 141 / 日本語インストラクション・チャットデータセット（LLMのファインチューニング用（例：LoRA）、9 M+サンプル）。最近更新され、ライセンス付きAlpacaデータを除外し、クリーンなWikipediaとALT出力を含め、CC‑BY‑SA 4.0でリリース。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 565 / ⭐ 2 / 日本語 Common Voice 17.0 サブセットを 30‑300 サンプルずつの 649 クライアント ID までフィルタリングし、8:2 の比率で訓練/検証に分割、1,000 サンプルの Parquet ファイルにバッチ化、合計 45,668 サンプル（CC0 ライセンス）
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 564 / ⭐ 24 / cc100-jaは、cc100データセットの日本語部分を集めたもので、シャーディングされたParquetファイルとして提供されています。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 558 / ⭐ 14 / JMMLUは、56科目に跨る7,536問の教師作成質問を収録した、日本語のマルチタスク言語理解ベンチマークです。含まれる科目は、専門医学・心理学・会計学・哲学、及び多様な高校科目です。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 555 / ⭐ 6 / Range3のwikipedia‑ja‑20230101リポジトリは、完全なWikipediaデータセットから抽出され、Pythonコードで生成された日本語Wikipediaテキストのみを含むParquetファイルを提供しています。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 548 / ⭐ 7 / JHumanEval は HumanEval benchmark の手翻訳版で、164 の Python programming problems を提供し、並行した英語と日本語のコメント付きで、日本語‑LLM のコード生成を評価しつつ、元の英語のエラーを保持します。
 * [honkoku-lines](https://huggingface.co/datasets/yuta1984/honkoku-lines) - 📥 546 / ⭐ 2 / 1,169,304 本の日本語歴史的行を 79,086 件の IIIF ページ画像から文字起こしした市民科学データセット。約 1 GB の WebDataset シャードとして提供され、JPEG 行切り抜き（高さ 256 px）と付随メタデータが含まれ、トレーニング／検証／テスト分割用に準備済みです。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 544 / ⭐ 118 / ReazonSpeech は、FLAC エンコードされた日本語音声コーパスで、文字起こし付きです。8.5 h から 35,000 h までの 5 つのサイズで提供され、Hugging Face 経由で CDLA‑Sharing‑1.0 ライセンスの下でダウンロードでき、日本著作権法第 30‑4 条の規定により使用が制限されています。
 * [JapaneseSummarization-FW2EduJa-Distill](https://huggingface.co/datasets/hachi-intelligence/JapaneseSummarization-FW2EduJa-Distill) - 📥 529 / ⭐ 2 / 約10億トークン規模の日本語要約データセット。fineweb‑2‑edu‑japanese から構築し、Qwen3‑30B や GPT‑OSS‑120B といったLLM を使用して抽出型の抽象的な要約を生成。事実・固有名詞・数値・年代順序・因果関係を保持しつつ、専門分野向けに作成。Apache 2.0 の下で公開。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 524 / ⭐ 2 / A BEJA‑CC‑JA リポジトリは、AWS Open Data の「abeja‑cc‑ja」(https://registry.opendata.aws/abeja-cc-ja/) の Hugging Face ミラーをホストしており、Abeja テックブログの追加情報への参照も含んでいます。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 522 / ⭐ 13 / LLM‑jpは、英語サブセット oasst2（kunishou/oasst2‑135k‑ja から派生）の DeepL 翻訳による日本語指示チューニングデータセットを提供し、Kiyomaru と Kodama によってコンパイルされています。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 511 / ⭐ 3 / WildGuardTestJPは、1,725サンプルの日本語評価データセットであり、WildGuardTestから多段階の改良パイプライン（Seed‑X‑PPO‑7B, gpt‑oss‑120b, Qwen2.5‑72B‑Instruct, gemma‑3‑27b‑it）を通じて忠実に翻訳されたものです。Hugging FaceでODC‑BY ライセンスの下で公開されています。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 494 / ⭐ 20 / JMMMUは、日本語のマルチモーダルベンチマークで、ネイティブ専門家が翻訳した1,320の文化的に多様な質問（720は文化に依存しない、600は文化固有）に拡張され、現在は公開リーダーボードを備えています。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 480 / ⭐ 4 / 日本語の検索/QAデータセットを提供し、5つの多言語/日本語リランカー（例：BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）によって算出されたクエリごとのスコアを含む。各クエリごとに約200件の正例と負例ドキュメントの平均スコアも含まれる。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 467 / ⭐ 8 / Livedoor News Corpus は、日本語ニュース記事データセットを提供し、5,894件のトレーニング、737件の検証、736件のテストのインスタンスに分割され、HTMLタグを除去して Creative Commons Attribution‑NoDerivs ライセンスの下で公開されています。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 453 / ⭐ 5 / 日本語と英語のウェブコーパスの集合体―9 Bトークンの日本語セット（JA‑WEB‑9B）、63 Bトークンの英語および日本語セット（EN‑WEB‑63B、JA‑WEB‑63B）や、パラフレーズされた JA‑PARAPHRASE‑63B、指示スタイルの JA‑INSTRUCT‑63B、翻訳済みの JA‑TRANSLATE‑63B などの合成バージョン―を含む。このコーパスは、データ制約環境下で日本語LLMの事前学習におけるデータ拡張を研究するために使用されます。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 445 / ⭐ 3 / 日本語版Wikipediaの文はさまざまな埋め込みとFAISSインデックスに変換され、Hugging Face Spaceデモ、変換スクリプト、検索・Q&A・OpenAI text‑embedding‑3‑smallを用いたRAGの評価が提供されます。埋め込みはOpenAIライセンス対象で、その他はCC‑BY‑SA‑4.0です。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 440 / ⭐ 18 / 1月 2024年のHTMLダンプから抽出され、パラグラフ構造、メタデータ（disambiguation, sexual, violent flags, templates, timestamps）を保持し、GitHubにホストされた抽出スクリプトも付属するNLP-ready Wikipedia記事データセット。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 438 / ⭐ 3 / 2010年の日本語ウェブコーパスは、HuggingFace にアップロードされ、2009年の著作権改革に基づき研究利用のライセンスが付与されており、形態素ベースの解析と変換スクリプトによる自動句読点付加テキストを含んでいます。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 438 / ⭐ 5 / 20,800件のWAVファイルからなる195人の日本語AItuberペルソナ（リファレンス、オリジナル、説明的、感情的発話を含む）データセットが、詳細なペルソナと音声メタデータを含み、データサイエンスAPI経由で取得可能です。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 430 / ⭐ 7 / 音声言語モデルに対する音声入力とテキスト入力の知能ギャップを定量化したデータセットで、Elyza‑tasks‑100、M‑IFEval、JamC‑QAベンチマークから合成された音声を4つのサブセットに分割した構成です。テキストはCC‑BY‑SA 4.0の下、音声は非商用・非再配布の使用に限定されます。
 * [cc100-ja-documents](https://huggingface.co/datasets/hotchpotch/cc100-ja-documents) - 📥 425 / ⭐ 4 / Hugging Faceで公開されたcc100‑jaの行単位に分割されたテキストを完全な文書単位に統合したリポジトリ。元のcc100条項に基づいてライセンスされています。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 416 / ⭐ 5 / STAIR‑Captionsは2017年にリリースされ、キャプション生成、マルチモーダル検索、画像生成に利用できる820,310の日本語キャプションを提供します。詳細なアノテーション、メタデータ、Creative Commons BY‑4.0 ライセンス付きです。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 392 / ⭐ 35 / Syosetu711Kは、2023年3月26日〜27日に小説家になろうからスクレイピングされた約711,700本の小説で構成される日本語データセットです。全テキストとメタデータ（タイトル、著者、NCode、あらすじ等）を提供し、教師なしテキスト生成および分類タスクに利用されます。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 389 / ⭐ 12 / JaQuADは2022年作成の日本語QAデータセットで、Wikipediaから抽出した39,696ペアのSQuAD‑style抽出クエリで構成され、総サイズは73.2 MBです。BERT‑Japaneseでファインチューニングすると78.92 % F1（63.38 % EM）を達成します。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 381 / ⭐ 11 / 検証済みのchain‑of‑thought 推論を備えた高品質な合成日本語数学問題データセット。PRM800K と GSM8K を Qwen2‑7B‑Instruct で翻訳し、正確性をフィルタリングして作成。Hugging Face datasets ライブラリ経由で利用可能。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 377 / ⭐ 4 / 266時間の日本語音声データセットは、Emilia dataset から取得され、Scribe v1（ElevenLabs STT/ASR）で分類され、Facebook audio aesthetics prefiltering が適用されています。このデータセットは HuggingFace と Discord で協力のために利用可能です
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 361 / ⭐ 20 / Retrieval‑Augmented Generation (RAG) を評価するための日本語 QA データセットで、JAQKET 質問と Wikipedia パッセージから構築され、金ラベル付きの検索関連性ラベルを持つ。HuggingFace と GitHub でリリースされ、主に nDCG@10 で評価される。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 339 / ⭐ 2 / JCommonsenseQA は、日本語の複数選択データセットで、CommonsenseQA の適応版として共通認識推論を対象にしています。CC BY‑SA 4.0 のライセンスの下で公開され、doi:10.5715/jnlp.30.63 として引用されています。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 331 / ⭐ 43 / 日本語ビジュアルノベルを英訳する際のセマンティック精度で大型言語モデルをランキングするリーダーボード。256サンプルに対してコサイン類似度を用い、Sugoi Translator、Google Translate、Naver Papago、Alibaba Translate などと比較するため chrF スコアを報告します。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 325 / ⭐ 17 / JA‑VG‑VQA‑500 は、日本語 Visual Genome VQA データセットの 500 サンプルのサブセットで、CC BY 4.0 ライセンスが付与され、EvoVLM‑JP‑v1‑7B のベンチマークに使用されます。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 325 / ⭐ 7 / SentenceTransformers に適した列と構造に再フォーマットされた日本語データセットで、RelRank スコアによって複数の HuggingFace ソースから対照学習用に正例（≥0.7）と負例（≤0.3）のペアへフィルタリングされています。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 313 / ⭐ 3 / 機械学習により非監督的に粗く10,000 グループにクラスタリングされた洗練された日本語ウェブコーパス（例：mc4‑ja）は、合法的な分析に使用でき、Parquet 形式のファイルのうち一部のみが「out」フォルダにリストされており、Git LFS 経由でダウンロード可能です。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 305 / ⭐ 24 / AI生成されたアニメイラストには英語のプロンプトとPhi‑3 Vision由来のキャプション（英語と日本語）が付いており、パブリックドメインで無料利用が可能です。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 292 / ⭐ 16 / Apache 2.0ライセンスの下で「_cleaned」エントリが指示の明確さ、言語の一貫性、および関連性を検証済みの、日本語アルパカスタイル合成データセット。mistralai/Mixtral‑8x22B‑Instruct‑v0.1 で作成され、Deepinfra により洗練されています。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 290 / ⭐ 5 / ダウンロード可能な81歳の日本人女性の音声コーパス（生データとノイズ除去後のwav、フォニーム/カナ＋プロソディラベルを含む）は、学術利用が無料で「Fusic Saoyoshi Voice Corpus」に帰属表示を伴って使用できます。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 286 / ⭐ 5 / JAMMEval は七つの日本語 VQA データセットを蒸留したベンチマークであり、曖昧さと非視覚的質問を除去するために二回のヒトアノテーションで改良され、マルチモーダル日本語タスクにおけるビジョン‑ランゲージモデルの信頼性の高い評価を提供します。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 284 / ⭐ 9 / llm‑jp‑instructions は、手作業でキュレーションされた日本語の指示データセット (v1.0) で、train、dev、test のスプリットが load_dataset を通じてアクセス可能です。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 280 / ⭐ 22 / MOMIJI（約5600万ページ、1100億文字、2億4900万枚の画像）という日本語ウェブドキュメントと画像データセットは、ビジョン‑ラングエージモデルの訓練用に設計されており、関連するインタラクティブ可視化ツールとテキストフィールド生成ユーティリティスクリプトが付属しています。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 277 / ⭐ 2 / 年間証券報告書の表から直接セル値を抽出するためのマルチモーダル日本語テーブル‑QAデータセットで、画像、OCRテキスト（境界ボックス付き）、質問と回答が含まれ、CC‑BY‑4.0 ライセンス下に提供されます。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 276 / ⭐ 24 / AutoWikiQA は、Swallow-MX と LLMs（ルールベースのテンプレートを使わず）を用いて Wikipedia から自動生成された質問–回答ペアを手作業でフィルタリングし、230 万件以上の無料の日本語 QA データセットです。知識教示および検索強化生成アプリケーションをサポートします。
 * [ScreenTalk_JA2ZH-XS](https://huggingface.co/datasets/Itbanque/ScreenTalk_JA2ZH-XS) - 📥 276 / ⭐ 3 / 約30時間の日本語音声と整列された簡体字中国語テキストを含む10,000サンプルペアデータセット（Parquet形式、CC BY 4.0）は、音声→テキスト翻訳および多言語ASR+MT研究向けに設計されています。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 256 / ⭐ 17 / Jagleは、画像–テキストペアとPDFコーパスから構築された約920万件のインスタンスを持つ日本語マルチモーダルポストトレーニングデータセットであり、LLM‑jp‑4‑VL 9B betaの訓練に使用され、日本語ビジョン・ランゲージタスクで性能向上が示されています。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 250 / ⭐ 2 / KokoroChatは、最も大規模な日本語心理カウンセリング対話データセットであり、480名の訓練済みカウンセラーによる6,589件のロールプレイングセッション（各平均91発話）を含む。豊富かつ長文形式の会話、20次元詳細クライアントフィードバックを備え、共感的応答生成、対話評価、およびメンタルヘルス言語モデリングに関する研究を支援し、ACL 2025で受理された。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 238 / ⭐ 5 / JetCopper‑10Bは、CC‑100、OSCAR‑2301、HPLT v1.2、およびwiki40b‑jaから派生し、クリーンアップと重複除去後に約4.7 bnトークン（＋0.9 bnの英語コード）を含む日本語テキストコーパスです。LOCAL AI HACKATHON #000 calm2‑chat用にContrail‑200m‑64kの事前学習に使用されますが、文境界とパープレキシティフィルタリングは欠けています。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 232 / ⭐ 3 / 64,139件の日本人名を生物学的性別でラベル付けしたデータセット―漢字、ひらがな、ローマ字で表記―は、トレーニング44.9k、検証6.41k、テスト12.8kに分割され、ISDA'23で採択されました。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 222 / ⭐ 33 / 日本語のRAGベンチマークを、金融・通信・製造・公共・小売という5つの業界ドメインで提供し、データセットの公開、自動評価フレームワーク、および Claude 3.5‑Sonnet、GPT‑4o などのモデルの比較結果を掲載します。
 * [OpenSakura-DS-260220-LN-ja-zh-COT-Lilith](https://huggingface.co/datasets/OpenSakura/OpenSakura-DS-260220-LN-ja-zh-COT-Lilith) - 📥 221 / ⭐ 2 / OpenSakura-DS-260220-LN-ja-zh-COT-Lilithは、1.64百万行の日本語から中国語へのライトノベル翻訳データセット（約18 GB）であり、マッピングベースの5分割を備え、推論内容とuuid、episode、segmentインデックスなどの構造化フィールドを保持しています。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 219 / ⭐ 18 / Databricks‑dolly‑15k‑ja dataset は、instruction tuning 用に作られた databricks‑dolly‑15k の日本語版で、DeepL で翻訳されました。日本の LLM‑jp プロジェクトが作成し、著者は Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama、Takumi Okamoto です。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 218 / ⭐ 47 / Galgame_Speech_ASR_16kHz は 16 kHz の ASR データセットで、3.75 百万ペア（≈5,354 時間）が含まれ、Galgame_Dataset から派生しており、GPL v3.0 の下で公開され、商用利用は禁止され、訓練済みモデルはオープンソースであることが求められます（引用は任意）。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 216 / ⭐ 26 / このリポジトリは、OpenAssistant/oasst1 データセットの日本語訳をホストしており、エラーフラグ付きの自動翻訳エントリ、約2,000件の手動修正、チャット形式のサブセット、およびデータを指示‑出力ペアに変換してファインチューニングに使用するスクリプトを含みます。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 211 / ⭐ 21 / SNOW T15/T23 日本語簡易化コーパスのデータセットカードで、50 k件の手動で照合されたオリジナルと簡易化済み日本語（≤2 k語彙）と英訳レコード、35 k件の拡張セットを含み、日英テキスト簡易化・翻訳に使用されます。
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 211 / ⭐ 3 / 312,396 行のフィルタリングされたサブセットを Oscar 2023 データセットから Hugging Face (if001/oscar_2023_filtered) で読み込み、if001/HojiChar_OSCAR_sample GitHub リポジトリでサンプルコードを提供します。
 * [Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k) - 📥 210 / ⭐ 8 / 深度探索-ai/DeepSeek-V3-0324で生成された39,600サンプルの日本語小説執筆タスクデータセット。2ターンのOpenAIスタイル対話（任意のNSFWコンテンツを含む）で構成され、MITライセンスの下で公開されています
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 207 / ⭐ 2 / COVID‑19 Japanese Twitter datasetは、日本のツイートIDと評価コード（63–68）を提供し、COVID‑19の関連性および事実／意見のステータスを示すことで、テキスト分類研究を可能にします。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 204 / ⭐ 4 / 「大規模言語モデル入門」に掲載され、RONWIT が提供する livedoor News Corpus から派生した日本語 NER データセット。CC BY‑ND 2.1 JP ライセンスの下でクリーンアップされた HTML 記事で構成されています。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 204 / ⭐ 3 / 『Introduction to Large‑Scale LLM II』で使用され、llm‑jp‑eval によって作成されたクロスデータセットの日本語LLM評価用のja‑vicuna‑qa‑benchmarkのデータセットカード（Apache 2.0）。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 202 / ⭐ 7 / Japanese Medical VQA 12Mは、元の言語と日本語の両方でオリジナルおよび拡張キャプションを備えた約1,200万サンプルからなる大規模なマルチモーダルデータセットです。生成されたVQA質問回答ペアも含まれ、Parquet/Webdataset形式で公開されます。このデータセットはOpen‑PMC‑18Mから構築され、InternVL3.5を使用して拡張し、Qwen3‑30B‑A3Bで翻訳、GPT‑OSS 120BでVQA生成が行われています。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 200 / ⭐ 4 / Guo、Mandy；Dai、Zihang、およびVrandečić、Dennyによって執筆されたWiki40Bデータセットの日本語サブセットを再フォーマットしました。
 * [joyo-kanji-yomi-benchmark](https://huggingface.co/datasets/sbintuitions/joyo-kanji-yomi-benchmark) - 📥 192 / ⭐ 10 / 日本語のTTSベンチマークで、全2,136字（常用漢字）に対して4,378読みを評価し、13,095文のネイティブスピーカー検証済み文章を使用。各文は単一の読みを対象とし、自動CER計算用に注釈付けされ、MITライセンスで提供されます。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 191 / ⭐ 4 / 日本語のアニメ字幕データセット（Advanced SubStation Alpha（SSA/ASS）形式）。`ass` PythonライブラリやAegisubなどの字幕編集ソフトで利用可能。ODC‑BY ライセンス下にあります。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 189 / ⭐ 2 / WAONは、サイズ、SigLIPスコアフィルタリングと重複排除（URL、キャプション、pHashによる）で構築された、大規模で高品質な日本語の画像‑テキストペアデータセットです。情報分析のためにApache 2.0の下でHuggingFaceに公開されました。
 * [JA_audio_JA_text_180k_samples](https://huggingface.co/datasets/Sin2pi/JA_audio_JA_text_180k_samples) - 📥 187 / ⭐ 9 / MeCab IPADIC Neologd 日本語辞書で使用される正規表現ルールを記載した Wiki ページ。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 185 / ⭐ 2 / 5つのNLPタスク（広告受容性、一貫性、性能推定、A3認識、および類似度）に対する日本語オンライン広告データセット。train/dev/test の分割は TSV 形式です。
 * [Japanese-Heron-Bench](https://huggingface.co/datasets/turing-motors/Japanese-Heron-Bench) - 📥 183 / ⭐ 11 / Japanese‑Heron‑Bench は、7つのサブカテゴリからなる21枚の画像と、それぞれが3カテゴリ（Conversation、Detail、Complex）の質問にペアリングされた日本語 VLM ベンチマークであり、CC BY ライセンス下で合計102件のクエリを含みます。
 * [Japanese-RP-Bench-testdata-SFW](https://huggingface.co/datasets/Aratako/Japanese-RP-Bench-testdata-SFW) - 📥 182 / ⭐ 5 / 日本語‑RP‑Benchテストデータ（日本語LLMのロールプレイスキルを測定するため）、ジャンル、タグ、world_setting、scene_setting、user/assistant設定、対話トーン、first_user_input、response_format、およびidが含まれています。特別な使用制限はありませんが、モデルの学習に利用することは禁止されています。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 180 / ⭐ 17 / oasst1‑21k‑ja は、DeepL によって英語版 OASST1 サブセットから派生した日本語の instruction‑tuning データセットであり、LLM‑jp コラボレーティブプロジェクトにより日本で作成されました。お問い合わせは llm‑jp@nii.ac.jp、著者には Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama、Okamoto が含まれます。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 175 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) は、Integration、Reasoning、Logical、Table、Abstention を網羅したマルチカテゴリ QA dataset を提供し、日本語 RAG ジェネレーターの評価を目的としています。このデータセットは人手と GPT‑4.1 によって構築され、CC BY‑SA 4.0 の下でリリースされています。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 172 / ⭐ 16 / 日本語ロールプレイ対話データセットで、十分な長さを持つマルチポスター記録のみをフィルタリングし、ポスター名を正規化し、上位スピーカーを均衡させたもの。機械学習用途を想定しています。
 * [LiquidAI-Hackathon-Tokyo-SFT-Data](https://huggingface.co/datasets/Aratako/LiquidAI-Hackathon-Tokyo-SFT-Data) - 📥 167 / ⭐ 3 / 東京で開催されたLiquid AI Hackathonで構築したモデルの教師付きファインチューニングに使用されたデータセット。
 * [danbooru-ja-tag-pair-20241015](https://huggingface.co/datasets/p1atdev/danbooru-ja-tag-pair-20241015) - 📥 162 / ⭐ 9 / Danbooruタグと日本語訳の150Kエントリデータセット（2024年10月15日更新）、拡張Wikiソースから構築、FastTextで非日本語タグを除外し、欠損項目にはfew-shot Calam Chat翻訳を追加しました。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 155 / ⭐ 16 / Zundamonキャラクター設定のシンプルなデータセット—オンラインソースおよび管理データから編纂された—は、character‑LLMsのテスト用に、指定されたライセンスの下でzmnjp.jsonlおよびzmn.jsonl形式で提供されます。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 153 / ⭐ 14 / 商用利用可能な、180万例の日本語翻訳を含むOpenMathInstruct-1数学指示チューニングデータセット—GSM8KおよびMATHベンチマーク問題から生成され、Mixtral-8x7Bソリューションが正確性検証済み—はNVIDIAライセンスの下で配布されており、再配布時にライセンス継承を要求します。
 * [alpaca_jp_python](https://huggingface.co/datasets/HachiML/alpaca_jp_python) - 📥 153 / ⭐ 8 / Apache 2.0 の下でリリースされた、mistralai/Mixtral‑8x22B‑Instruct‑v0.1 で構築され、Deepinfra によってクリーンアップされ、検証済みプロンプトを使用した日本語合成 Alpaca データセット。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 152 / ⭐ 29 / 政府のウェブサイトから手作業で抽出された日本語FAQデータセット。CC‑BY‑4.0ライセンスで、ハイクオリティなQ&AペアとソースURLを提供し、大規模言語モデルの指示チューニングおよびRAGテストに使用することを目的としています。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 149 / ⭐ 2 / LLM生成の日本語クエリと回答のデータセットで、パラフレーズされたWikipediaテキストから作成され、CC‑BY‑SA 4.0の下で公開されています。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 149 / ⭐ 17 / 16 kHzで音声が収録された104 GB、370万ファイルのGalgameスピーチデータセット。感情ラベルはLLMによって自動アノテーションされており、精度は保証されません。GNU GPL v3に準拠し、商用利用は禁止されています。また、このデータセットで訓練されたオープンソースモデルの使用が義務付けられています
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 147 / ⭐ 34 / 409時間の日本語エロゲ音声データセットで、2パス loudnorm（‑23 LUFS、‑1 dB peak、11 LRA）で処理され、litagin/anime-whisper により文字起こしされ、匿名化され、WebDataset（FLAC、JSON、TXT）として保存されています。主に女性の声が収録されており、AI文字起こしのエラーが存在する可能性があります。MIT‑licensed for academic research.
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 143 / ⭐ 3 / 2ch.sc の大規模な匿名掲示板データセット。スレッドのメタデータ（ID、タイトル、地域、板名、返信数）とネストされた投稿（ユーザー名、メールアドレス、日付ID、本体、任意のタイトル）が含まれる JSONL.ZST ファイルです
 * [extraction-wiki-ja](https://huggingface.co/datasets/llm-jp/extraction-wiki-ja) - 📥 140 / ⭐ 4 / LLM‑jpからキュレーションされたWikipediaのサブセットを元にしたInstruction‑tuned Japanese dialogue datasetで、Qwen/Qwen2.5‑32B‑Instructでフィルタリングされ、二ターンと四ターンフォーマットで利用可能です。
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 138 / ⭐ 4 / ArknightsワイフのJP Voice‑Text Dataset: 10,905件の日本語音声クリップ（合計26.3 h）を単一俳優キャラクターから収集。ASR/ASVモデルのファインチューニングや評価に有用です
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 137 / ⭐ 82 / 日本語ウェブ小説章データセットと英語ファン翻訳がペアになっており、バージョン2では106Kの整列された文に拡張されています。シリーズメタデータを含み、品質フィルタリングは行われていません。フェアユース/Apache 2.0 の下で配布され、テイクダウン条項が設けられています。
 * [ChouBun](https://huggingface.co/datasets/SakanaAI/ChouBun) - 📥 136 / ⭐ 10 / ChouBunは長文コンテキストLLM評価用の日本語ベンチマークで、抽出型QAと要約生成型要約という2つのタスクカテゴリを備えています。4つのデータセット（wiki_qa、edinet_qa、corp_sec_qa、corp_sec_sum）があり、各文書につき最大200件のQAペアまたは5つの参考サマリーを提供します。標準化されたフォーマットと可変の最大入力長が使用されています。
 * [Wiki-JA-Pair](https://huggingface.co/datasets/llm-jp/Wiki-JA-Pair) - 📥 136 / ⭐ 2 / jawiki-20250501 記事から作成された日本語 Wikipedia 画像キャプションデータセットで、1,054,434 個のユニーク (画像, キャプション) ペアと 1,047,565 個のダウンロード済み画像を含み、サイズ、ハッシュ、ページ情報などのメタデータが付属し、99.35% のダウンロード成功率を記録しています。
 * [japan-law](https://huggingface.co/datasets/y2lan/japan-law) - 📥 134 / ⭐ 22 / 日本のe‑Gov法令データセットで、番号・題名・ID・施行日・全文を含み、2023年8月1日時点で最新有効版に重複除外されたもの。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 132 / ⭐ 9 / JMMMU‑Proは、現実的なモデルと人間による検証で視覚質問を生成して作成された画像ベースの日本語マルチモーダルベンチマークです。現在のオープンソースLMMがこのベンチマークで低い性能を示すことを明らかにし、将来のVQAベンチマーク開発に対して費用効果の高い方法を提供します。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 131 / ⭐ 27 / WRIMEデータセットは、日本語の投稿42,200件からなるコレクションで、筆者、3名の読者、およびその平均に対してPlutchikの8つの感情でアノテーションされています。感情分析タスク向けに、40kトレーニング、1.2kバリデーション、2kテストのスプリットで構成されています。
 * [Magpie-Tanuki-8B-annotated-96k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-annotated-96k) - 📥 130 / ⭐ 6 / カンマイメソッドを適用してTanuki‑8Bに対し96kサンプルのデータセットを注釈付けし、各指示の難易度・品質・カテゴリをcalm3ベースのプロンプトでスコアリングしました。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 129 / ⭐ 9 / JSICKは、SICKコーパスを翻訳して作成された日本語-英語のNLIとSTSデータセットであり、ワードオーダーや格助詞の扱いを検証するストレステストセットが含まれており、異なる文法関係に対して1 666、797、および1 006の句対を持っています。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 129 / ⭐ 17 / 日本語の仮名→漢字変換用の190MペアJSONLデータセット。左コンテキスト–入力–出力の三連で構成され、事前学習済みモデル（medium、small、xsmall）とAJIMEE-Benchベンチマークを含む。CC BY‑SA 4.0 の下で公開され、Wikipedia と Common Crawl からライセンスされたサブセットが使用されています。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 127 / ⭐ 6 / Japanese XL‑Sum subset は PaLM‑2 15‑gram overlap を通じてフィルタリングされ、4,215件のトレーニング例、758件の検証例、766件のテスト例を含みます。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 126 / ⭐ 6 / J-HARD‑TTS‑Eval は、短シーケンス安定性、繰り返し処理、およびコンテキスト補完において、自己回帰型日本語 TTS モデルの強靭性をベンチマークします。データセットは Hugging Face で入手可能です（short、repetition、rhyme、continuation）。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 125 / ⭐ 5 / 日本語のオープンドメインQAデータセット「JAQKET」は、クイズ形式の複数選択問題（v1.0）と自由記述回答生成（v2.0）を提供し、v1.0では13 061件の訓練例と271件の検証例、v2.0では2 154件の訓練例と1 164件の検証例が含まれています。
 * [DEJIMA-dataset](https://huggingface.co/datasets/MIL-UT/DEJIMA-dataset) - 📥 123 / ⭐ 4 / DEJIMAは、厳格なフィルタリング・重複排除・検出駆動型証拠抽出・グラウンディング制約を経て生成されたLLM生成キャプションとVQA回答がペアになった3.88 M画像からなる日本のウェブスケールデータセットであり、分析用に複数のキャプショニングおよびVQAバリアントが利用可能です。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 122 / ⭐ 14 / Wikipediaから抽出された日本語NERデータセット、CC‑BY‑SA 3.0ライセンスで提供され、Stockmark Inc.によって作成されました。
 * [KokushiMD-10](https://huggingface.co/datasets/humanalysis-square/KokushiMD-10) - 📥 120 / ⭐ 7 / KokushiMD‑10は、10種類の日本語医療職向けの多言語ベンチマークであり、テキストのみと画像を用いた単一選択・複数選択・計算・穴埋め問題が含まれ、チェーンオブソート説明付きです。日本語、英語、または混合の分割で入手可能です。
 * [OpenAI-MRCR-Translation-JPN](https://huggingface.co/datasets/abeja/OpenAI-MRCR-Translation-JPN) - 📥 120 / ⭐ 2 / OpenAIの長文コンテキストMRCRからLLMsを使用して翻訳された日本語評価データセットで、元の構造を保持しつつ新しいアシスタント応答を生成し、MITライセンスを維持しています。
 * [fgo_voices_jp](https://huggingface.co/datasets/deepghs/fgo_voices_jp) - 📥 119 / ⭐ 16 / FGOワイフのためのJP Voice‑Text Dataset：30,800件、66.4時間の日本語音声コレクション。単一ボイスアクターのキャラクターロライン（1行約7.76 秒）で、ASR/ASVのファインチューニングと評価に有用です。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 116 / ⭐ 9 / llm‑book/wrime‑sentiment のデータセットカードは、WRIME から派生した二項式日本語感情分析セットを提供し、Avg. Readers_Sentiment に基づいて「positive」または「negative」とラベル付けされます（中立ケースを含めるオプション付き）。このセットは、“Introduction to Large Language Models” のサンプルデータとして意図されています。
 * [Magpie-Tanuki-8B-97k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-97k) - 📥 115 / ⭐ 12 / 97,269件の日本語対話データセット。Magpie の手法を weblab‑GENIAC/Tanuki‑8B‑dpo‑v1.0 に適用して作成され、後処理は行われておらず、低品質なレコードが含まれている可能性があります。
 * [mbpp-ja](https://huggingface.co/datasets/llm-jp/mbpp-ja) - 📥 113 / ⭐ 3 / mbpp‑ja は、DeepL と HuggingFace および GitHub からのオリジナル mbpp データセットを使用した日本語共同 LLM-jp プロジェクトであり、著者は Namgi Han、Masatoshi Otake、Shintaro Ozaki、および Yusuke Miyao です。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 111 / ⭐ 11 / 日本語テキストは llm-jp-corpus-v3 の kaken サブセットから抽出され、Qwen/Qwen2.5-32B-Instruct で英訳されました。このデータは CC‑BY 4.0 ライセンスの下で公開され、元のデータセットの条件を継承しています。
 * [NMLE](https://huggingface.co/datasets/longisland3/NMLE) - 📥 107 / ⭐ 5 / 日本国医療国家試験データセット（NMLE）は、110–117の試験から構造化された質問を提供し、モデル評価、進化的統合、およびRAGタスクに使用されます。CC‑BY‑NC‑ND4.0 ライセンスで非商用利用のみが許可されています。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 107 / ⭐ 5 / 日本のアニメ音声データセット、元の joujiboi/japanese‑anime‑speech‑v2 コレクションを分割した版。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 106 / ⭐ 5 / SNLI自然言語推論ベンチマーク（JSNLI）の日本語訳で、TSV形式にて形態素分割済みの前提と仮説を提供し、フィルタ済み・未フィルタ済み両方の訓練データセット、および3,916ペアの検証セットをCC BY‑SA 4.0で提供。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 104 / ⭐ 16 / データセット「japanese_alpaca_data」は、masa3141 の Japanese‑Alpaca‑LORA 作業を基にしており、研究やアプリケーション向けのキュレーション済み日本語 Alpaca データセットを提供します
 * [oasst1-chat-44k-ja](https://huggingface.co/datasets/kunishou/oasst1-chat-44k-ja) - 📥 104 / ⭐ 10 / オリジナルのOASST1データから変換された日本語チャット形式データセット（oasst1‑89k‑ja）は、マルチターン微調整に適しており、ShareGPTフォーマットで提供されます。大きなトークン長を持つため、相当な計算リソースが必要です
 * [hh-rlhf-12k-ja](https://huggingface.co/datasets/llm-jp/hh-rlhf-12k-ja) - 📥 103 / ⭐ 14 / LLM‑jpがDeepLを使用して作成したhh‑rlhfデータセットの一部の日本語訳で、著者はアルファベット順に並べられ、連絡先はllm-jp(at)nii.ac.jpです。
 * [swallow-magpie-ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1) - 📥 101 / ⭐ 5 / Swallow‑Magpie‑Ultra‑v0.1 の一部としてリリースされた、tokyotech‑llm モデルのトレーニング用に magpie‑ultra‑v0.1 から抽出した平均的に良質な日本語–英語指示チューニングデータセット（各42kペア）
