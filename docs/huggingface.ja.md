# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語向けのNLPに関する、Pythonライブラリ、LLM、辞書、コーパスに特化したリソースを厳選してまとめた一覧です。
このページでは、Hugging Faceで利用可能な日本語NLP特化のモデルとデータセットを掲載しています。現在、164件のモデルと109件のデータセットが含まれています。

_2026年3月22日更新_

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)

## Contents
 * [Ranking](#Ranking)
   * [Models](#models-ranking)
   * [Datasets](#datasets-ranking)
 * [Models](#Models)
   * [text-generation](#text-generation)
   * [fill-mask](#fill-mask)
   * [feature-extraction](#feature-extraction)
   * [sentence-similarity](#sentence-similarity)
   * [automatic-speech-recognition](#automatic-speech-recognition)
   * [text-ranking](#text-ranking)
   * [text-classification](#text-classification)
   * [translation](#translation)
   * [token-classification](#token-classification)
   * [image-to-text](#image-to-text)
   * [image-text-to-text](#image-text-to-text)
   * [text-to-speech](#text-to-speech)
   * [audio-to-audio](#audio-to-audio)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | モデル名 | Downloads | Likes | カテゴリ |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 3M | ⭐ 53 | automatic-speech-recognition |
| 2 | [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) | 📥 777k | ⭐ 3 | text-classification |
| 3 | [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) | 📥 633k | ⭐ 22 | sentence-similarity |
| 4 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 480k | ⭐ 15 | text-generation |
| 5 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 470k | ⭐ 76 | fill-mask |
| 6 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 448k | ⭐ 67 | sentence-similarity |
| 7 | [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) | 📥 444k | ⭐ 131 | text-generation |
| 8 | [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) | 📥 395k | ⭐ 11 | sentence-similarity |
| 9 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 338k | ⭐ 12 | translation |
| 10 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 312k | ⭐ 169 | image-to-text |
| 11 | [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) | 📥 238k | ⭐ 15 | text-classification |
| 12 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 234k | ⭐ 41 | fill-mask |
| 13 | [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 📥 219k | ⭐ 20 | text-generation |
| 14 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 179k | ⭐ 8 | sentence-similarity |
| 15 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 177k | ⭐ 9 | fill-mask |
| 16 | [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) | 📥 129k | ⭐ 9 | sentence-similarity |
| 17 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 118k | ⭐ 58 | text-generation |
| 18 | [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) | 📥 111k | ⭐ 5 | image-to-text |
| 19 | [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) | 📥 102k | ⭐ 3 | image-to-text |
| 20 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 90k | ⭐ 11 | others |

### Datasets-ranking

| # | データセット名 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 3M | ⭐ 23 |
| 2 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 158k | ⭐ 7 |
| 3 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 17k | ⭐ 16 |
| 4 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 11k | ⭐ 9 |
| 5 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 9k | ⭐ 109 |
| 6 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 5k | ⭐ 28 |
| 7 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 5k | ⭐ 4 |
| 8 | [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) | 📥 3k | ⭐ 110 |
| 9 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 3k | ⭐ 39 |
| 10 | [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) | 📥 3k | ⭐ 16 |
| 11 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 3k | ⭐ 99 |
| 12 | [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) | 📥 2k | ⭐ 5 |
| 13 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 2k | ⭐ 36 |
| 14 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 2k | ⭐ 4 |
| 15 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 2k | ⭐ 19 |
| 16 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 2k | ⭐ 18 |
| 17 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 2k | ⭐ 47 |
| 18 | [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) | 📥 1k | ⭐ 89 |
| 19 | [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) | 📥 1k | ⭐ 4 |
| 20 | [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) | 📥 1k | ⭐ 6 |

## Models
### text-generation
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 480k / ⭐ 15 / CC‑100、C4、Wikipedia で学習された12‑layer、768‑hidden の日本語 GPT‑NeoX モデル。Huggingface と互換性があり、各文の末尾に必ず笑顔の絵文字を付けるオプションのトイプレフィックス調整ウェイトが付属しています。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 444k / ⭐ 131 / 9 billionパラメータの日本語最適化LLM、NVIDIA Nemotron‑Nano‑9B‑v2‑Japaneseは、2024年9月までのデータでハイブリッド Mamba-2/MLP/4-layer-attentionアーキテクチャを用いて学習され、Nemotron-Personas-Japan tool‑callingデータセットでファインチューニングされます。最終回答を生成する前に制御可能な推論トレースをオプションで生成でき、商用利用が可能です。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 219k / ⭐ 20 / OpenCALM は、decoder‑only 日本語 Transformer 言語モデル（160 M〜6.8 B パラメータ）のスイートで、CyberAgent, Inc. によって CC‑BY‑SA 4.0 の下でリリースされました。日本語 Wikipedia と Common Crawl でトレーニングされ、Hugging Face の torch‑transformers を通じて利用可能です。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 118k / ⭐ 58 / 2.7Bパラメータの日本語 GPT‑NeoX モデルは、ABEJA Inc. が日本語 CC‑100 と OSCAR で学習し、Hugging Face Transformers パイプラインまたは PyTorch で利用可能で、MIT license の下で公開されています。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 40k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 は、13‑B の指示事前学習済み日本語言語モデルで、NII の R&D Center によって開発され、Hugging‑Face Transformers のチェックポイントとして UNIGRAM‑byte‑fallback トークナイザー付きで公開されました。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 39k / ⭐ 28 / LFM2.5‑1.2B‑JPは、LFM2.5ハイブリッドアーキテクチャ上に構築された1.2 Bパラメータの日本語テキスト生成モデルで、生成と完了タスク向けに最適化され、Hugging Faceにホストされ、llama.cpp経由で実行可能です。
 * [llm-jp-3.1-13b](https://huggingface.co/llm-jp/llm-jp-3.1-13b) - 📥 24k / ⭐ 2 / llm‑jp‑3.1‑13b は NII の R&D Center が開発した 13 B パラメータのトランスフォーマー LLM であり、日本語テキストで事前学習されており、Hugging Face 形式で提供され、torch ≥2.3、transformers ≥4.40 に対応し、ファインチューニング済みチェックポイントと unigram byte‑fallback tokenizer が含まれます。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 17k / ⭐ 18 / Japanese Stable LM Base Gamma 7BをShisa 7B dataでFine‑tunedし、JA MT‑Benchで強い結果を得ました。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 14k / ⭐ 146 / Llama‑3‑ELYZA‑JP‑8B は、ELYZA によって開発された日本語強化版で、8 billion パラメータ（80億）を持つ Llama 3 モデルで、Meta‑Llama‑3‑8B‑Instruct 上で日本語用に微調整されています。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 13k / ⭐ 56 / TinySwallow‑1.5B‑Instruct は、TAID を用いて Qwen2.5‑32B‑Instruct から蒸留された 1.5 B の日本語インストラクション調整済みオートレグレッシブ言語モデルであり、研究目的のみに利用されることを想定しています。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 11k / ⭐ 21 / Llama3 Swallowは、2024年7月1日にリリースされた、日本語拡張のMeta Llama 3ファミリーで、Instructとchat形式の8Bおよび70Bバリアントを提供し、SFTとChat VectorでMegatron‑LM上で微調整され、主要な日本語NLPタスクでベンチマークされている。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 11k / ⭐ 18 / Llama 3.1 Swallowは、MetaのLlama 3.1の事前学習を継続して日本語性能を向上させ、合成日本語データで指示ファインチューニングを行う8‑Bおよび70‑Bモデルのセットです。これにより、gemma‑3‑27b‑itと同等の会話挙動を備えた複数のリリースバリアントが提供されます。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 10k / ⭐ 25 / rinnaの日本語GPT‑2 smallは、12層、768ユニットの隠れ層を持つtransformerで、日本語CC‑100とWikipediaをデータとして学習され、SentencePieceでトークナイズされ、MITライセンスのもとで2021年8月25日にリリースされました（Hugging Face: rinna/japanese‑gpt2‑small、詳細は https://arxiv.org/abs/2404.01657 を参照）。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 10k / ⭐ 50 / GGUF形式のNVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese、imatrix datasetから再構築され、CUDA上で llama.cpp で実行できるようになりました。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 9k / ⭐ 24 / Llama 3.1 Swallowは、継続的なプレトレーニングと日本語特有のインストラクションファインチューニングで訓練された8B / 70B Llama 3.1モデルの日本語強化シリーズです。最新の8B‑Instruct‑v0.3は、日本語MT‑Benchで最先端の結果を示しています。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 9k / ⭐ 4 / 実験的な日本語モデルは、lightblue/suzume‑llama‑3‑8B‑japanese と Meta‑Llama‑3‑8B‑Instruct の違いを chat‑vector approach を使って抽出し、upsampled して Meta‑Llama‑3‑70B‑Instruct に適用した結果、ほとんど変更がなく、将来のスケーリング計画を立てている。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 7k / ⭐ 18 / GPT‑OSS‑Swallow v0.1 は、CPT、SFT、RLVR によって訓練された 20B と 120B の日本語―英語バイリンガルLLM を提供し、数式とコーディング課題で GPT‑OSS を上回るか同等の性能を示し、2026年2月にリリースされ、4 つの SFT/RL バリエーションと今後の量子化版を予定しています。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 7k / ⭐ 19 / NIIから提供される1.8 Bパラメータのllm‑jp‑3.1‑1.8b‑instruct4日本語指示‑調整モデルは、Hugging Face TransformersおよびTorch ≥ 2.3.0に互換性があり、事前学習済みと微調整済みのチェックポイント、ならびに使用例を含みます。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 5k / ⭐ 8 / Qwen3‑Swallow v0.2は、日本語―英語のLLM（30B‑A3B と 32B）を提供し、CPT、SFT、RLVR によってトレーニングされ、強力な数式・コーディング・推論能力を保持し、9 つのリリース済みモデルと AWQ 量子化バリアントを備えています。
 * [Qwen3-Swallow-8B-CPT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2) - 📥 4k / ⭐ 1 / Bilingual 30 B- と 32 B-パラメータの LLM、Qwen3‑Swallow v0.2 は CPT、SFT、RLVR で構築され、日本語、日本語‑英語翻訳、数学、コーディングで優れた性能を発揮し、Qwen3 と同等またはそれを上回り、AWQ‑量子化された形式で Hugging Face にリリースされました。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 3k / ⭐ 20 / OpenCALMは、CyberAgentが開発した日本語専用のデコーダオンリートランスフォーマー言語モデル（160 M〜6.8 Bパラメータ）のファミリーです。日本語のWikipediaとCommon Crawlで学習され、CC BY‑SA 4.0の下でリリースされています。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 3k / ⭐ 107 / 1.3Bパラメータ、24層のトランスフォーマー GPT-1Bは、日本語C4、CC-100、およびWikipediaで学習され、rinna Co. によって2022年1月26日にリリースされ、MITライセンスの下で利用可能です。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 3k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b は、Meta の Llama‑2 モデルの 6.27B パラメータ拡張で、インストラクトとファストバリアントで日本語データ上で事前学習され、Hugging Face Transformers を通じて利用できるものです。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 3k / ⭐ 85 / Rinnaの24層、1024ユニットの日本語GPT‑2‑mediumモデルは、CC‑100とWikipediaをSentencePieceトークナイゼーションで学習され、rinna/japanese‑pretrained‑modelsリポジトリで入手できます（MITライセンス、2021年4月7日リリース、2021年8月25日更新）。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 3k / ⭐ 26 / 日本語用 3.6 B‑parameter GPT‑NeoX モデルで、指示に従うことを目的として fine‑tuned（SFT‑v2）。ChatGPT での以前の SFT と比較して 100 件のプロンプトで評価され、2023年3月31日にリリース。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 3k / ⭐ 7 / 日本語で事前学習済み TinyLlama (≈50 k ステップ) は、約3 B OSCAR/mC4トークンで構築され、HuggingFace Transformers または VLLM で使用可能です。Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru、Renju Aoki が作成しました。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 3k / ⭐ 35 / TinySwallow‑1.5Bは、Sakana AIとSwallow Teamによるコンパクトな日本語指示‑フォロー型言語モデルで、Qwen2.5‑32B‑InstructからのTAID蒸留を利用し、さらに日本語テキストで事前学習が追加され、研究利用のみを目的としてApache 2.0でリリースされています。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 3k / ⭐ 36 / SB Intuitionsから提供される自己回帰型日本語モデル（sarashina2.2‑3B‑instruct‑v0.1）を、他のモデルとベンチマークし、使用例スクリプト付きで提供。安全性トレーニングは限定的である旨の注意書きが付いています。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 2k / ⭐ 10 / リポジトリは、Massed Compute ハードウェアで作成され、TheBloke の a16z ファンド付き LLM 仕事の一部として、Stability AI の日本語 StableLM Instruct Gamma 7B の GGUF 形式で量子化されたモデルファイルを提供します。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 140 / LFM2.5‑1.2B‑JPは日本語最適化されたチャットモデルで、LFM2より日本語知識と指示に従う能力で優れ、LoRAによるファインチューニング、Transformers、vLLM、llama.cppを使った推論をサポートし、50.7 JMMLU、58.1 M‑IFEval、56.0 GSM8Kのスコアを達成しています。
 * [GPT-OSS-Swallow-20B-SFT-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-SFT-v0.1) - 📥 2k / ⭐ 5 / GPT‑OSS‑Swallow v0.1 は、継続的事前学習、教師付き微調整、検証可能な報酬付き強化学習を通じて数学とコーディング性能を保持するように訓練された、20B & 120B の日本語‑英語バイリンガルモデルファミリーです。現在、SFT と RL バリアントがリリースされ、量子化バージョンも計画されています。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 2k / ⭐ 21 / youri‑7bは、Llama2‑7bをベースに構築された32層、4096ユニットの隠れ層を持つトランスフォーマーです。CC‑100、C4、OSCAR、Pile、Wikipediaから約40 Bの日本語トークンで継続的に事前学習され、2023年10月31日にリリースされました。AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA、Winograndeで競合力のあるスコアを達成しています。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 1k / ⭐ 1 / Qwen3‑Swallow v0.2 は、CPT、SFT、および RLVR で訓練された 30‑B と 32‑B の日本語‑英語バイリンガル LLM を提供し、日本語の正確性、翻訳、数学、コーディングを向上させて、オリジナルの Qwen3 と同等または上回ります。9 本のモデル（CPT、SFT、RL）および AWQ 量子化版を含み、GPT‑OSS‑Swallow もリリースされています。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 1k / ⭐ 3 / 「LLM‑jp‑3‑150m」は、情報学研究所のLLM R&D Centerが開発した150Mパラメータを有する日本語言語モデルです。Hugging Face Transformers形式で配布され、torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8 が必要です。Japanese Wikipedia、Common Crawl、WARP/PDF、WARP/HTML、Kaken データを使用し、unigram byte‑fallback tokenizer で事前学習されています。
 * [japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) - 📥 1k / ⭐ 75 / 3.6 billionパラメータの日本語 GPT-NeoX モデルは、約650 GBの日本語テキスト（C4、CC‑100、Oscar、ウェブクローリング）で訓練され、内部C4検証で7.50のパープレキシティを達成し、Apache 2.0の下でリリースされます。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ](https://huggingface.co/dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ) - 📥 1k / ⭐ 3 / MetaのLlama‑2 7B（ELYZA‑japanese‑Llama‑2‑7b‑fast‑instruct）の4ビット、4.11 GB量子化版を提供し、メモリを削減するが指示従い性能を低下させ、GPUとautoGPTQが必要で、AWQ、llama.cpp、およびgguf量子化とベンチマーク結果への参照を含む。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 1k / ⭐ 16 / 6層、512ユニットの隠れ層を持つトランスフォーマーで、Japanese GPT‑2 xSmall と呼ばれ、Japanese CC‑100 および Wikipedia を SentencePiece でトークナイズして学習された。2021年8月25日に MIT ライセンスで公開され、Hugging Face（rinna/japanese‑gpt2‑xsmall）にホストされ、arXiv 2404.01657 で引用されている。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 82 / ELYZA の Japanese‑enhanced Llama‑2‑7B は、standard、instruct、fast バリアントで拡張日本語対応を実現するよう事前学習され、詳細な使用例、開発者クレジットが付随し、Meta の Llama‑2 Community License の下でライセンスされています。
 * [Murasaki-4B-v0.3-GGUF](https://huggingface.co/Murasaki-Project/Murasaki-4B-v0.3-GGUF) - 📥 1k / ⭐ 1 / Murasaki‑4B‑v0.3は、ACGNの日本語→英語翻訳に最適化された4 億パラメータを有するGGUF System 2推論モデルです。プロンプト制御のCoTスイッチ、強化されたNon‑thinkモード、BF16ベンチマーク、複数の量子化を備え、すべてCC BY‑NC‑SA 4.0でライセンスされています。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 1k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑7b は、Meta の Llama‑2‑7B の 6.27B パラメータを持つ日本語拡張で、さらに日本語言語タスク向けに事前学習済みです。base、instruct、fast、fast‑instruct の各バリエーションで提供され、ELYZA チームが Llama 2 Community License の下で保守しています。
 * [japanese-stablelm-instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b) - 📥 1k / ⭐ 26 / Japanese‑StableLM‑Instruct‑Beta‑70B は、70 billion パラメータの日本語用デコーダーのみ Llama2 ベースの言語モデルで、Dolly‑15k、Anthropic HH、その他の公開データでファインチューニングされています。7 billion パラメータのバリアントも利用可能で、Llama2 Community License の下で公開されています。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 1k / ⭐ 96 / ELYZA-japanese-Llama-2-7bは、MetaのLlama-2 7 Bの日本語最適化拡張で、インストラクトバリアントとファストバリアントを提供し、6.27–6.37 Bパラメータを有し、Hugging‑Face Transformers libraryを通じてアクセスできます。
 * [stockmark-13b](https://huggingface.co/stockmark/stockmark-13b) - 📥 1k / ⭐ 39 / Stockmark‑13bは、約2200億トークン（＋インストラクションチューニングされたバリアント）でトレーニングされた13‑Bパラメータを持つ日本語LLMで、AWS Trainium上にneuronx‑nemo‑megatronを使用して構築され、MITライセンスの下でStockmark Incよりリリースされました。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 1k / ⭐ 15 / LLM‑jp は 13 B と 1.3 B の transformer 言語モデルを提供しています。複数の指示チューニング済みバリアントを含むモデルは、Megatron‑DeepSpeed および Hugging Face Transformers エコシステムで構築されています。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 1k / ⭐ 16 / 日本語大規模言語モデル（1.8 b から 172 b beta1、インストラクションバリアント付き）のコレクションで、NIIの研究開発センターから提供され、Hugging Face Transformers 形式でパッケージ化され、1兆語以上の日本語・英語・Web コーパスを混合して事前学習されています。torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5 が必要です。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 470k / ⭐ 76 / 2019年の日本語Wikipediaを対象に、IPA辞書と全単語マスキングを用いて事前学習されたJapanese BERT‑base、12層、768次元、32,000語語彙、512トークンシーケンス、1Mステップ、CC‑BY‑SAの下でcl‑tohoku/bert‑japaneseから入手可能。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 234k / ⭐ 41 / 約17 Mの日本語Wikipedia文（2.6 GB）で事前学習済みのBERT base modelで、IPA dictionaryとWordPieceでトークナイズし、12層／768-dim hidden states／12 headsを有し、32 000-token vocabularyを備え、1 MステップでCloud TPUs上で訓練され、CC‑BY‑SA 3.0でリリースされています。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 177k / ⭐ 9 / 171 GBの日本語Wikipedia、CC‑100、OSCARでトレーニングされた日本語DeBERTa V2 large modelは、文字レベルのsentencepieceトークナイズと全単語マスキングを使用し、Hugging Face Transformersを通じて下流でのファインチューニングに準備できています。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 89k / ⭐ 8 / 日本語のBERT‑baseモデル（12層、768次元の隠れレイヤー、12ヘッド）は、MeCab IPA単語レベルトークン化を経て文字レベルトークン化で4000語語彙に変換し、約1700万文（2.6 GB）の日本語Wikipediaで事前学習されました。学習コードはcl‑tohoku/bert‑japaneseにあり、CC BY‑SA 3.0 でリリースされています。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 44k / ⭐ 6 / BERT‑base Japanese model（12層、768‑次元の hidden states、12ヘッド）を、30 M Wikipedia 文（約4 GB）で Unidic 2.1.2 を用いた単語レベルトークン化の後、文字レベルトークン化と全単語マスクを行い、512トークンのシーケンス、256バッチ、1 M トレーニングステップで訓練しました。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 28k / ⭐ 5 / ModernBERT‑Ja‑30Mは、ローカルおよびグローバル注意機構をRoPEと組み合わせた日本語BERTバリアントです。4.39 TBの日本語／英語テキストで訓練され、8,192トークンのシーケンスをサポートし、30 Mから130 Mパラメータのサイズで提供され、Flash Attention 2との組み合わせで最も効果的です。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 16k / ⭐ 48 / LINE DistilBERT Japanese は、インハウスの BERT‑base 先生を用いて 131 GB の日本語ウェブテキストで事前学習された 66 百万パラメータの DistilBERT モデルであり、JGLUE で評価され、MeCab Unidic と SentencePiece でトークナイズされ、Apache 2.0 ライセンスの下でリリースされました。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 13k / ⭐ 27 / Japanese BERT‑base (12 layers, 768 hidden, 12 heads) は、Unidic 2.1.2 単語レベルトークナイゼーション、WordPiece サブトークナイズ、および whole‑word マスクリングを使用し、4 GBの日本語Wikipedia（約30 M文）で事前学習されています。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 11k / ⭐ 39 / Japanese‑Roberta‑Base は rinna Co., Ltd. が開発した事前学習済みのマスク言語モデルで、正しいロード方法、トークン前処理、位置ID処理、および使用例に関するガイドラインがあり、先頭に `[CLS]` トークンが必要であることと、一貫したトークン化を強調しています。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 6k / ⭐ 3 / 日本語RoBERTa‑baseモデルは、約10 M件の日本語医学要旨と1.4 M件のJST本文で事前学習され、30 kトークンのSentencePieceでトークナイズされ、CC BY‑4.0で公開され、Hugging Face pipelinesで利用可能です。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 6k / ⭐ 47 / 132 Mパラメータの日本語 ModernBERT モデルで、ローカルグローバルとRoPE注意を組み合わせ、4.39 T トークン（日本語/英語）で訓練され、102 kサイズの語彙、最大8,192トークン長、Flash Attention 2 に最適化されています
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 5k / ⭐ 30 / 日本語 DeBERTa V2 ベースモデルは、171 GBの日本語 Wikipedia、CC‑100、OSCAR データを用いて Juman++ セグメンテーションと SentencePiece トークン化で事前学習され、8枚の NVIDIA A100 GPU を 3週間使用してトレーニングされ、ファインチューニングに向けて準備ができています。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 5k / ⭐ 2 / Japanese DeBERTa V2 tinyは、約171 GBの日本語Wikipedia、CC‑100、およびOSCARコーパスで事前学習され、Juman++による形態素解析が必要です。8台のNVIDIA A100 GPUを使用して33時間で訓練され、下流タスクに微調整できます。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 5k / ⭐ 20 / ModernBERT‑Ja‑310M は local‑global attention と RoPE を組み合わせた日本語 BERT 変種で、4.09 T tokens の日本語／英語テキストで訓練され、102 400語の語彙、8 192トークンのシーケンスをサポートし、Flash Attention 2 用に最適化されています。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 2k / ⭐ 4 / DeBERTaV2 base は日本語コーパス（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）でトレーニングされ、FP‑16 ファインチューニングで NLU タスク（JSTS、JNLI、JCommonsenseQA）に適用され、CC BY‑SA 4.0 の下でリリースされ、日本の研究助成金で資金提供されました。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 2.6 GBのWikipedia（約1700万文）で訓練された12層、768次元のBERT‑Base日本語モデルで、IPA‑dictionary文字トークナイズとwhole‑word maskingを使用し、CC‑BY‑SA 3.0でリリースされた。
 * [deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 📥 1k / ⭐ 9 / 日本語の DeBERTa‑V2 大規模モデルは、171 GB の日本語テキスト (Wikipedia、CC‑100、OSCAR) を Juman++ 区切りで事前学習し、8 台の A100 GPU で 36 日間訓練され、下流タスクに対して微調整可能です。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 52k / ⭐ 11 / 文埋め込みを生成するJapanese Sentence‑BERT (v1) モデルで、改良版v2が利用可能で、Hugging Face Transformers とカスタム `SentenceBertJapanese` クラスを使用したサンプル使用例があります。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 48k / ⭐ 51 / 日本語 Sentence‑BERT v2 は、cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking を MultipleNegativesRankingLoss でファインチューニングし、v1 に比べて約1.5〜2 % の精度向上を実現。sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 としてリリースされました。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 44k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 は、ViT‑B/16 をベースにした Apache‑2.0 ライセンスの日本語 CLIP モデルで、CC12M のキャプションを日本語に翻訳して訓練され、2022 年 5 月 12 日にリリースされました。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 22k / ⭐ 29 / LY Corporation の clip‑japanese‑base は、約 1 B の画像‑テキストペアで学習された日本語 CLIP モデルで、Eva02‑B トランスフォーマー画像エンコーダーと12層の BERT テキストエンコーダーを使用し、STAIR で R@1 0.30、Recruit で 0.89 の精度、ImageNet‑1K で 0.58 の精度を達成し、ゼロショット画像分類と検索をサポートしています。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 13k / ⭐ 22 / Sarashina‑Embedding‑v2‑1B は、1,792 次元の日本語文変換器であり、マルチステージ対照学習 (multi‑stage contrastive learning) によって訓練され、最先端の JMTEB スコアを達成しています。また、意味的類似度、検索、パラフレーズ・マイニング、分類、クラスタリングに利用でき、Sentence‑Transformers を通じてオプションの instruction prefixes 付きで使用可能です。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 12k / ⭐ 2 / ja_ginza_electra は、mC4 と UD_Japanese_BCCWJ r2.8（megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator をベースにしたもの）でファインチューニングされた日本語 ELECTRA モデルを提供する spaCy v3 の Python パッケージです。カスタム bunsetu‑phrase 検出機能を備え、MIT ライセンスで配布されています。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 10k / ⭐ 14 / 日本語Sentence‑LUKEモデルは、Sentence‑BERTと同じデータセットで訓練され、同等にするかそれを上回る性能を有し、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、Hugging Face Transformers の MLukeTokenizer と LukeModel を介して使用される。
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 9k / ⭐ 4 / fastTextは軽量でオープンソースのライブラリで、標準CPU上で単語および文の埋め込みと分類器を高速に学習します。数十億語を数分で学習でき、モバイル用途向けに圧縮可能で、分類や言語識別のための事前学習済みベクトルを提供します。
 * [japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16) - 📥 7k / ⭐ 13 / Japanese CLOOB‑VIT-B-16、vit‑base‑patch16‑224 をベースとした Vision‑Language モデルで、翻訳された CC12M のキャプションで訓練され、rinna Co., Ltd. により 2022年5月12日に Apache 2.0 ライセンスの下でリリースされたもの。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 5k / ⭐ 17 / Japanese CLIP モデル clip‑japanese‑base‑v2 は、約20億画像‑テキストペアと蒸留でアップグレードされ、Eva02‑B 画像エンコーダと12層 BERT テキストエンコーダをペアリングし、前モデルよりも高い ImageNet‑1k 精度（0.708）を達成します。
 * [japanese-avhubert-base_noise_pt](https://huggingface.co/enactic/japanese-avhubert-base_noise_pt) - 📥 4k / ⭐ 1 / 日本語の AVHuBERT AV‑SR modelのリポジトリで、約2,250時間の音声-視覚データで事前学習済みで、広範なノイズ増幅により堅牢な音声認識を実現しています。
 * [japanese-avhubert-large_noise_pt](https://huggingface.co/enactic/japanese-avhubert-large_noise_pt) - 📥 2k / ⭐ 1 / 2,250時間の事前学習済みAVHuBERT Large自己教師付きモデル。日本語の音声・映像データにノイズ拡張を施し、音声・映像音声認識を堅牢にサポートするように訓練されている。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 2k / ⭐ 55 / 日本語対応の T5 モデルは、Wikipedia と OSCAR データ約100 GB を SentencePiece トークナイズで事前学習し、ニュース分類ベンチマークで Google’s multilingual T5 を上回るが、ファインチューニングが必要で、バイアスのある出力が生成される可能性がある。
 * [amber-large](https://huggingface.co/retrieva-jp/amber-large) - 📥 2k / ⭐ 7 / AMBERはRetrieva Inc.が開発した3億1500万パラメータの埋め込みモデルで、日本語向けにsbintuitions/modernbert‑ja‑310mを拡張したもので、オプションで英語サポートも可能です。768次元のプロンプト駆動型埋め込みを提供し、Apache 2.0 ライセンスでリリースされています。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 2k / ⭐ 3 / 日本語 BERT‑base モデルを JSNLI 上で教師付き SimCSE によってファインチューニングし、Sentence‑Transformers または HuggingFace を通じて CLS プーリングで公開、512 バッチサイズで 1 M のサンプルを用いて学習率 5 × 10⁻⁵、温度 5 × 10⁻⁵、64 タークン制限、BFloat16 精度でトレーニング。

### sentence-similarity
 * [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) - 📥 633k / ⭐ 22 / 最終 JaColBERTv2.5 チェックポイントの重みは、新しいレシピで JaColBERTv2 データのわずか 40 % でトレーニングされ、すべてのデータセットにおいて、以前のモデルすべて（BGE‑M3 などの JaColBERTV2 多言語バリアントを含む）を上回っています。
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 448k / ⭐ 67 / Ruri v3 は、ModernBERT‑Ja をベースとした最先端の日本語テキスト埋め込みモデルで、最大8,192トークンの入力、100Kトークンの語彙、FlashAttention で加速された推論、および高速な sentence‑transformer での使用のための複数サイズバリアントをサポートします。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 395k / ⭐ 11 / 日本語一般テキスト埋め込みモデル（Ruri‑v3、30‑310 Mパラメータ、8192‑token最大、JMTEBスコアが高い）は、Sentence‑Transformers使用例と他の日本語埋め込みとのベンチマーク比較とともに提供されています。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 179k / ⭐ 8 / Ruri v3 は、ModernBERT‑Ja をベースに構築された最先端の日本語テキスト埋め込みモデルで、最大 8,192 トークン、100 k‑トークン語彙、FlashAttention 加速、37 M から 315 M の複数サイズに対応しています。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 129k / ⭐ 9 / Ruri v3 Japanese text embeddings（30 M–310 M parameters, 8192‑token limit, JMTEB 74.5–77.2）を含み、Sentence Transformers 用の「クエリ:」または「文章:」prefixes での指示、および Sup/Unsup SimCSE、GLuCoSE、LaBSE など複数の日本語モデルのベンチマーク結果を含みます。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 32k / ⭐ 44 / PLaMo‑Embedding‑1B は、Preferred Networks が提供する日本語テキスト埋め込みモデルで、情報検索、分類、クラスタリングのために日本語テキストをベクトルに変換します。JMTEB ベンチマークで高い性能を示し、Apache v2.0 license の下で無料で利用できます。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 30k / ⭐ 34 / GLuCoSEは、LUKEをベースに構築された日本語文埋め込みモデルであり、ウェブおよびNLI／検索データで訓練され、最大512トークンまでの768次元平均プールベクトルを出力します。類似度ベンチマークで0.864のSpearmanと0.818のPearsonを達成しています。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 28k / ⭐ 4 / Ruri v3は、ModernBERT‑Jaをベースに構築された最先端の日本語テキスト埋め込みモデルで、8192トークンまでのシーケンス、10万語の語彙、FlashAttentionに対応し、sentence‑transformers用に30 M〜310 Mパラメータのサイズでリリースされます。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 28k / ⭐ 16 / JaColBERTv2は、日本語専用のColBERTベースの検索モデルで、MMarcoで知識蒸留（31）ノルゲート／1件の正例、250kステップ、バッチ32）を使って訓練されており、現在はmultilingual‑e5‑large、BGE‑M3、JaColBERTを上回っています。完全な評価は保留中です。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 21k / ⭐ 22 / GLuCoSE v2 は CPU‑フレンドリーな日本語テキスト埋め込みモデルで、蒸留とマルチステージ対照学習によって微調整され、MIRACL や関連ベンチマークで同規模のモデルを上回る優れた意味的類似度と検索性能を提供します。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 21k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite は 768 次元の sentence‑transformer で、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、shunk031/jsnli 上で 1 エポックでトレーニングされ、クラスタリング、セマンティック検索、さらに Sentence‑Transformers と HuggingFace の両方の使用例を含んでいます。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 11k / ⭐ 44 / リリース準備済みのRuri v3日本語テキスト埋め込みモデル（30m–310m）のコレクションで、SentenceTransformerの使用ヒント、クエリ/パッセージプレフィックス、JMTEBベンチマーク結果を含み、他の日本語および多言語埋め込みと比較しています。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 10k / ⭐ 2 / Ruri v3は、8192トークンまでの高性能日本語テキスト埋め込み、100kトークン語彙、FlashAttentionサポート、および30 m–310 mの複数モデルサイズを備え、sentence‑transformersを介した効率的な推論とファインチューニングを可能にします。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 3M / ⭐ 53 / Japanese wav2vec‑2 XLSR‑53 は Common Voice 6.1、CSS10、JSUT で微調整され、16 kHz オーディオを必要とし、HuggingSound または HuggingFace パイプラインで使用できます。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 18k / ⭐ 89 / Kotoba‑Whisper v2.0 は、OpenAI Whisper large‑v3 から蒸留された日本語 ASR モデルで、7.2 million ReazonSpeech クリップで訓練され、ドメイン内テストで教師の CER/WER と同等の性能を維持しつつ 6.3 倍速で動作します。stable‑ts/punctuation のサポートと完全なトレーニングコードが GitHub にあります。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 15k / ⭐ 96 / Kotoba‑Whisper‑v2.2 は、HuggingFace‑Transformers パイプラインを通じて統合された話者分離と自動句読点機能を備えた kotoba‑whisper‑v2.0 を拡張した日本語 ASR モデルであり、Asahi Ushio と Kotoba Technologies と協力して構築されました。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 9k / ⭐ 128 / Anime Whisperは、約5,300時間のanime‑style dialogueで微調整された軽量の日本語ASRモデルで、低 hallucination、リズムに合わせた句読点、非言語音声およびNSFW contentの正確な文字起こしを実現し、初期プロンプトなしで実行する必要があります。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 8k / ⭐ 46 / NVIDIA NeMo の 0.6 B‑parameter Hybrid FastConformer‑TDT‑CTC ASR model は、日本語音声を句読点付きで文字起こしし、NeMo フレームワーク内で推論またはファインチューニングに利用可能です。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 8k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 は、日本語と英語の ASR 用に 6.3 倍速化された distilled Whisper モデルを提供し、さらに双方向音声からテキストへの翻訳機能を備えています。これらは、OpenAI の Whisper large‑v3 をベースに、knowledge distillation を用いて構築され、クロスエントロピーと KL‑divergence loss を利用しています。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 3k / ⭐ 19 / Kotoba‑Whisper‑v2.1は、日本語のASRモデルであり、統合されたpunctuation‑postprocessing pipelinesを備えてkotoba‑whisper‑v2.0を拡張しています。これにより、同等のCER性能を保持しながら、シームレスでpunctuation‑aware transcriptionが可能になります。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 2k / ⭐ 37 / reazonspeech‑nemo‑v2は、619 Mパラメータの日本語長文ASRモデルで、改良版Fast‑Conformerと線形スケーラブル注意機構を採用し、ReazonSpeech v2.0コーパスで訓練されました。3000トークンSentencePieceを用いたsubword RNN‑Tデコーダにより、多時間推論を提供し、Apache 2.0で配布されています。
 * [moonshine-tiny-ja](https://huggingface.co/UsefulSensors/moonshine-tiny-ja) - 📥 2k / ⭐ 11 / 小型でエッジ対応のASRモデル（Moonshine AI）は、日本語音声をリアルタイムで文字起こしし、低リソースデプロイメント向けにmodel cardで詳細が記載されています。
 * [kotoba-whisper-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0) - 📥 2k / ⭐ 58 / Kotoba‑Whisper v1.0、OpenAI の Whisper large‑v3 から蒸留された日本語 ASR モデルは、同等の精度で 6.3 倍の速度向上を実現し、ReazonSpeech の 1,253 時間でトレーニングされ、コード（および Hugging Face 上の新しい v2.0 バリアント）は公開されています。

### text-ranking
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 46k / ⭐ 7 / Japanese CrossEncoderリランカーモデルは、xsmall から large（BGE を含む）まであり、JQaRA、JaCWIR、MIRACL、JSQuAD で評価済み。sentence_transformers と HuggingFace 用の、すぐに利用可能な統合例も用意されています。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 19k / ⭐ 6 / 高速で軽量な日本語 Reranker v2 モデル（tiny、xsmall、small、base）は、ベンチマークスコアと GPU スピードを備え、sentence_transformers CrossEncoder と transformers ≥ v4.48 で使用でき、flash‑attn で高速化も可能です。また、CPU/ARM 用に ONNX/quantized フォーマットでも利用可能です。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 8k / ⭐ 13 / Ruri‑v3 Reranker は、ModernBERT‑Ja をベースにした堅牢な日本語テキストリランカーで、最大 8,192 トークンのシーケンス、100k トークンの語彙、FlashAttention および SentencePiece tokenizer をサポートし、sentence‑transformers 経由で使用できます。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 3k / ⭐ 2 / Japanese‑reranker‑small‑v2は、軽量で高速な日本語リランクモデルシリーズ（v2）です。tiny〜baseバリアントを提供し、平均スコア0.89まで達し、2〜15秒のGPU推論で実行できます。さらにクロスエンコーダオプションも利用可能です。加速のためにオプションでFlash Attention 2を使用できるHugging Face Transformers v4.48+が必要です。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 3k / ⭐ 2 / Sentence TransformersのCrossEncoderに基づく日本語文の再ランカーで、推論コード、ベンチマーク結果、複数のモデルサイズを提供します。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 2k / ⭐ 15 / Japanese CrossEncoder リランキングスイート（xsmall、small、base、large、および japanese-bge-reranker-v2-m3-v1 を含む）と、使用例、複数ベンチマークにおける評価指標、およびサポートドキュメントが揃っています
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 2k / ⭐ 16 / 日本語向け CrossEncoder リランカー モデル（xsmall から large まで）は、日本語テキストで学習され、sentence_transformers を通じて公開され、JQaRA、JaCWIR、MIRACL、JSQuAD で評価されます。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 1k / ⭐ 4 / 日本語でトレーニングされた CrossEncoder リランクラーは xsmall (384) から large (1024) まであり、さらに BGE‑v2‑m3‑v1 モデルも含まれます。ファインチューニング、推論、JQaRA、JaCWIR、MIRACL、JSQuAD のベンチマークスコアの例コードが付属しています。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 1k / ⭐ 12 / Sentence Transformersで構築された日本語クロスエンコーダリランカーは、各サイズのRuri‑Rerankerモデルに対する推論利用例とベンチマーク結果を示します。

### text-classification
 * [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) - 📥 777k / ⭐ 3 / Finance Sentiment JA (base) は、翻訳された Financial PhraseBank で訓練された BERT‑ベースの日本語感情モデルで、金融ニュースを positive、negative、neutral に分類し、macro f1 0.959、accuracy 0.967、134.9 samples per second で動作します。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 238k / ⭐ 15 / Amazonの商品レビューに対して感情分類のためにFine‑tuned Japanese BERT (cl‑tohoku/bert‑base‑japanese‑v2) を使用し、6エポックで学習率 2 × 10⁻⁵ を設定した結果、約81 % の精度と0.73のF1スコアを達成しました。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 11k / ⭐ 15 / 日本語感情分析モデルは、chABSAデータセットで学習され、損失0.0001、精度1.0、F1スコア1.0を達成しました。Transformers 4.24.0およびPyTorch 1.12.1+cu113で構築され、Adam（学習率2e‑05、10エポック、バッチサイズ16）で最適化され、`model(**inputs)`で評価されました。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 4k / ⭐ 2 / 「Large Language Model Introduction」の第5章で紹介された、日本語 BERT‑based モデル。JGLUE JSTS データセットで意味的類似度スコアリングのためにファインチューニングされ、Colab ノートブック、transformers‑pipeline の使用方法、Apache 2.0 ライセンス付き。
 * [luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 📥 3k / ⭐ 43 / 日本語のLUKEモデルで、WRIMEデータセットで微調整され、文章内で表現されている8つの感情（喜び、悲しみ、期待、驚き、怒り、恐怖、嫌悪、信頼）のうちどれかを分類する。
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 1k / ⭐ 6 / 日本語版 BERT BASE を WRIME データセットでファインチューニングしたモデルは、作家と読者の 8 つの感情（喜び、悲しみ、期待、驚き、怒り、不安、嫌悪、信頼）に対して 0〜4 の強度スコアを予測し、コードは公開済みです。K80 GPU 上で 3 時間で訓練し、作家では約 0.6 MSE、読者では約 0.2 MSE を達成しました。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 338k / ⭐ 12 / 新しい VNTL データセットに基づく LLaMA 3 Youko qlora ファインチューニング。日本のビジュアルノベルを英語へ正確かつ文字通りに翻訳することに最適化されており、チャットモードは使用せず、デフォルトの LLaMA 3 プロンプトを使用し、ニュートラルサンプリング（温度 0、繰り返しペナルティ無し）を推奨する。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 54k / ⭐ 73 / OpusコーパスからのJapanese‑to‑English Transformer‑Align MT modelは、正規化とSentencePiece前処理を使用して、Tatoebaテストセットで41.7 BLEUと0.589 chr‑Fを達成します。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 47k / ⭐ 28 / Fine‑tuned, GGUF‑quantized LFM2‑350M checkpoint は、短〜中長テキストに対するほぼリアルタイムの bi‑directional Japanese‑English 翻訳に使用でき、llama.cpp で利用可能です。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 12k / ⭐ 118 / PLaMo Translation Model は Preferred Networks が開発した翻訳タスク向けの大規模言語モデルで、ベース、ポストトレーニング、評価バリアントが用意されています。PLaMo community license の下で公開され、チャットやその他のダウンストリーム用途向けにインストラクションチューンは行われていません。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 2k / ⭐ 8 / Sugoi LLM 14B Ultra (GGUF) は、BLEUスコアが21.38の日本語‑英語翻訳モデルで、以前の13.67のほぼ二倍に近い点数です。RPG‑Makerの括弧付きテキストに優れ、プロンプトに強く従う性質と、インタラクティブチャットUIs用のJSON出力を実現します。

### token-classification
 * [MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - 📥 57k / ⭐ 12 / 日本語医療文書 NER モデル（5 つのファイルをダウンロードし、**predict.py** を実行すると、病気、薬、日付などのタグが出力されます。）NAISTSOC 2022 NTCIR‑16 Real‑MedNLP タスクで使用された。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 17k / ⭐ 10 / Wikipediaデータセット上の固有表現認識用に微調整された日本語 BERT‑Base は、*Large Language Model Introduction* の第6章で紹介され、Hugging Face transformers パイプライン（Apache 2.0 ライセンス）でデプロイできるものです。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 15k / ⭐ 11 / cl‑tohoku/bert‑base‑japanese‑v2 を使用した日本語 NER は、`BertForTokenClassification` を介して 8 つのエンティティタイプ（企業、政治・その他組織、施設、製品、イベント）を抽出し、Stockmark Wikipedia データセットで学習済みです。CC BY‑SA 3.0 ライセンスの下で `transformers`、`unidic_lite`、`fugashi` でインストール可能です。
 * [bert-base-japanese-v3-crf-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset) - 📥 2k / ⭐ 2 / CRF‑強化された BERT‑base‑japanese‑v3 を、日本語のNER用に Wikipedia データでファインチューニングしたモデルは、『Large‑Language‑Model Intro』という書籍に掲載されている（Apache 2.0 ライセンス）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 日本語NERコーパス（タグ PER, ORG, LOC, INS, PRD, EVT）上で、5エポックのAdam（lr 5e‑5、バッチ12）を使用してFine‑tuneしたXLM‑RoBERTa‑baseは、0.0173の検証ロスを達成し、Transformers 4.23.1とPyTorch 1.12.1でリリースされました。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 312k / ⭐ 169 / Manga OCR は、縦書きと横書きの日本語漫画テキスト（フリガナを含む）を、さまざまなフォントと低品質画像でも読み取る Vision Encoder-Decoder OCR ツールで、ソースコードは無料で入手可能です。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 111k / ⭐ 5 / Meikiocrの `meiki.text.recognition.v0`――D‑FINEベースのMobileNetV4モデルで、日本語ビデオゲームテキストに特化して微調整されたもので――は、960×32入力から最大48文字まで検出し、それぞれの文字をバウンディングボックスと信頼度スコアとともに出力することで、水平テキストに対して最先端の精度と遅延を実現します。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 102k / ⭐ 3 / meikiocr は、ビデオゲーム向けに D‑FINE ベースのオープンウェイトテキスト検出モデル（v0.1、MobileNet‑v4 バックボーン、2種類の解像度バリアント、64 ボックス制限）と、実験的低遅延 tiny および small バリアント（日本のビデオゲームと漫画で訓練済み）を提供します。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 1k / ⭐ 16 / Sarashina2.2‑Vision‑3B は、Sarashina2.2‑3B‑Instruct と SigLIP 画像エンコーダーをベースに構築された 3 B パラメータを持つ日本語大規模ビジョン‑ラングエージングモデルであり、日本語 VQA ベンチマークで高い性能を達成しています。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 2k / ⭐ 121 / PaddleOCR‑VL からファインチューニングされた PaddleOCR‑VL‑For‑Manga は、Manga109 の吹き出し切り抜きで 70 % の全文正確性を達成し、27 % のベースラインを 3 倍以上上回ります。多言語データセットを使用し、トレーニングコードと開発者ガイドが含まれます。
 * [Heron-NVILA-Lite-15B](https://huggingface.co/turing-motors/Heron-NVILA-Lite-15B) - 📥 1k / ⭐ 14 / Heron‑NVILA‑Lite‑15B‑hf は、日本語中心のビジョン・ランゲージ・モデルで、NVILA‑Lite アーキテクチャに基づいて構築され、PALIGEMMA‑SIGLIP ビジョンエンコーダ、MLP‑downsample プロジェクター、および Qwen2.5‑14B‑Instruct LLM を備え、簡易的な Hugging Face 統合で日本語と英語をサポートしています。

### text-to-speech
 * [Anime-Llasa-3B](https://huggingface.co/NandemoGHS/Anime-Llasa-3B) - 📥 1k / ⭐ 26 / Anime‑Llasa‑3B は、HKUSTAudio/Llasa‑3B に基づく日本語 TTS モデルで、より多くのトレーニングデータで表現力と安定性を向上させ、CC‑BY‑NC‑4.0 のライセンスが適用されています。
 * [japanese-parler-tts-mini](https://huggingface.co/2121-8/japanese-parler-tts-mini) - 📥 1k / ⭐ 26 / Japanese Parler‑TTS Mini は、軽量で高品質な日本語 TTS モデルで、parler‑tts‑mini‑v1 をファインチューニングして効率的な音声生成を提供します。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 2k / ⭐ 14 / Anime‑XCodec2‑44.1kHz‑v2は、16 kHzの日本語音声を44.1 kHzの高音質オーディオにアップサンプリングし、デコーダー専用RMS‑lossファインチューニングを行い、encoder/codebookをフリーズしたまま、同一の音声トークンを保持します。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 90k / ⭐ 11 / Japanese‑language BERT‑Base (12 layers, 768‑dim, 12 heads)は、Unidic‑based word‑level plus character‑level tokenizationとwhole‑word maskingをCC‑100と2023 Wikipediaで事前学習し、7,027‑token vocabularyを生成する。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 81k / ⭐ 61 / Japanese BERT‑base（12層、768次元の隠れ層、12ヘッド、32k語彙）は、CC‑100と2023‑Jan Wikipediaで全単語マスキングを用いて事前学習され、Unidic 2.1.2の単語レベルトークナイゼーション＋WordPieceを併用し、200万ステップで学習しました。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 67k / ⭐ 14 / Japanese‑BERT‑Large は CC‑100 と Wikipedia に対して訓練され、Unidic‑lite のワードレベルトークナイゼーションを使用し、WordPiece サブワードとホールワードマスクリングを採用しています（24 層、隠れ層 1024 次元、16 ヘッド、32k 語彙）。プリトレーニングコードは cl‑tohoku/bert‑japanese にあります。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / ≈100 GB の Wikipedia と OSCAR CC‑100 データ（SentencePiece で 10:1 の混合、byte‑fallback を有する）で事前学習された日本語 T5‑v1.1 モデルで、下流タスクの微調整が必要です。転移学習サンプルコードが含まれ、出力に潜在的なバイアスを示唆しています。ライセンスは CC‑BY‑SA 4.0 です。
 * [GPT-OSS-Swallow-20B-SFT-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-SFT-v0.1-gguf) - 📥 12k / ⭐ 1 / GPT‑OSS‑Swallow‑20B‑SFT‑v0.1‑ggufは、tokyotech‑llm GPT‑OSS‑Swallow 20B SFTモデルをggufに変換したバージョンで、TFMC/imatrix‑dataset‑for‑japanese‑LLM でトレーニングされ、CUDA対応 llama.cpp 用に構築されており、llama‑cli で実行可能です（例：プロフェッショナルシェフのレシピプロンプト）。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 9k / ⭐ 1 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 はトップタレ、Japanese‑focused GGUF モデルで、Unsloth Dynamic Quantization 2.0 を使用し、広範な日本語キャリブレーションとコミュニティ修正済みバグが含まれ、GPU がなくても、少なくとも 8 GB RAM と 3 GB のディスク空き容量があれば llama.cpp で実行できます。
 * [GPT-OSS-Swallow-20B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-RL-v0.1-gguf) - 📥 9k / ⭐ 4 / TFMC/imatrix‑dataset‑for‑japanese‑llm の imatrix data で構築された GPT‑OSS‑Swallow 20B RL v0.1 モデルを gguf‑format へ変換し、CUDA support を備えた llama.cpp で実行できるようになっています。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 6k / ⭐ 4 / 日本語向けにファインチューニングされた Qwen 3.5‑9B GGUF モデル。Unsloth Dynamic Quantization 2.0 を採用し、広範なバグ修正と大規模な日本語キャリブレーションを実施。llama.cpp を介して 16 GB RAM と 6 GB ディスクを備えた CPU 上で実行可能。
 * [Qwen3.5-0.8B-JP-gguf](https://huggingface.co/tatsuyaaaaaaa/Qwen3.5-0.8B-JP-gguf) - 📥 5k / ⭐ 1 / Holy-foxからのgguf変換済みQwen3.5‑0.8B‑JPで、TFMC/imatrix‑dataset‑for‑japanese‑llmデータセットを使用して量子化されています。
 * [GPT-OSS-Swallow-120B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-120B-RL-v0.1-gguf) - 📥 5k / ⭐ 5 / gguf-format で120 B GPT‑OSS‑Swallow RL モデルを変換し、TFMC/imatrix 日本語データセットで構築し、CUDA 対応で llama.cpp をコンパイルし、llama‑cli でモデルを実行する手順。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 3k / ⭐ 17 / Japanese DeBERTa V3 base は、LLM‑jp v1.0 から 540 B トークンで事前学習され、修正された DeBERTa V3 セットアップで訓練され、形態素解析器を使用しないユニグラム・バイトフォールバックトークナイザーを使用し、JGLUE NLUタスク用に微調整済みです。
 * [Qwen3-8B-JP-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/Qwen3-8B-JP-Uncensored-i1-GGUF) - 📥 3k / ⭐ 1 / Qwen3‑8B‑JP‑Uncensoredモデル向けに、2.2 GB IQ1バリアントから6.8 GB IQ6までの幅広いweightedおよびimatrix GGUF量子化を提供し、使用手順、static‑quantリンク、サポートリソースが含まれています。
 * [GPT-OSS-Swallow-20B-RL-v0.1-MXFP4](https://huggingface.co/dahara1/GPT-OSS-Swallow-20B-RL-v0.1-MXFP4) - 📥 3k / ⭐ 2 / GPT‑OSS‑Swallow‑20B‑RL‑v0.1‑MXFP4は、無料かつGPU非搭載のGPT‑4o‑miniレベルAIで、ggufファイルとして配布され、日本語に最適化されたコミュニティで発見されたバグ修正、ベンチマーク由来の設定を備え、デフォルトのMXFP4形式のみ（ダイナミック量子化または大型imatrixは含まない）です。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 3k / ⭐ 72 / Llama‑3‑ELYZA‑JP‑8B は、日本語向けに強化された 8‑B Llama 3 モデルで、GGUF（Q4_K_M）と AWQ 量子化を備え、llama.cpp、LM Studio、または OpenAI‑compatible API で実行できます。
 * [SIP-jmed-llm-3-13b-OP-4k-base](https://huggingface.co/SIP-med-LLM/SIP-jmed-llm-3-13b-OP-4k-base) - 📥 3k / ⭐ 1 / SIP‑jmed‑llm‑3‑13b‑OP‑4k‑base は、Apache‑2.0 ライセンスの下に提供される、ドメイン適応された日本語‑英語医療 LLM で、llm‑jp‑3.1‑13b をベースに構築されています。SIP の第三期プログラムにより医療知識の研究プロトタイプとして開発されましたが、臨床用途を意図したものではありません。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 は、8 billion パラメータを持つ LLM で、Meta の Llama 3.1 を日本語とコード／数式推論で改善しつつ英語の流暢さを保持し、継続的なプリトレーニングと指示調整ファインチューニングを合成日本語データで実現したものです。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 2k / ⭐ 22 / pfnet の plamo‑2‑translate を imatrix データから構築し、TFMC/imatrix‑dataset‑for‑japanese‑LLM に基づく GGUF‑format リリースで、CUDA 対応ハードウェア上で llama.cpp を通じてコンパイル・実行する手順を含む。
 * [Holy-fox-Qwen3.5-0.8B-JP-gguf](https://huggingface.co/mmnga-o/Holy-fox-Qwen3.5-0.8B-JP-gguf) - 📥 2k / ⭐ 1 / Holy‑fox の Qwen3.5‑0.8B‑JP モデルを TFMC/imatrix‑dataset-for-japanese‑LLM から構築したものの GGUF フォーマット変換を提供し、CUDA サポート付きで llama.cpp をコンパイルして実行する手順を添付します。
 * [gemma-2-2b-it-gguf](https://huggingface.co/mmnga/gemma-2-2b-it-gguf) - 📥 2k / ⭐ 1 / Googleのgemma‑2‑2b‑itモデルを、TFMC/imatrix‑dataset‑for‑japanese‑llmのimatrixデータを使用してGGUF形式に変換し、llama.cpp使用手順を付ける。
 * [Qwen3.5-REAP-212B-A17B-gguf](https://huggingface.co/mmnga-o/Qwen3.5-REAP-212B-A17B-gguf) - 📥 2k / ⭐ 5 / GGUF変換された OpenMOSE Qwen3.5‑REAP‑212B‑A17B、TFMC/imatrix 日本語LLM データセットから再構築され、llama.cpp の標準 CLI を介した CUDA 対応推論が可能です。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 2k / ⭐ 17 / 高性能日本語 SPLADE v2 は、WebUI demo を通じてスパース‑ベクトル変換と推論を可能にし、YAST でトレーニングを行い、YASEM 埋め込みを提供し、JMTEB ベンチマーク結果を報告します。
 * [Qwen3-Swallow-8B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-8B-SFT-v0.2-gguf) - 📥 1k / ⭐ 1 / 日本語LLM用にgguf変換されたQwen3‑Swallow‑8B‑SFT‑v0.2モデル、imatrixデータを使用して構築し、推論にはllama.cpp手順を備えている。
 * [llm-jp-moshi-v1](https://huggingface.co/llm-jp/llm-jp-moshi-v1) - 📥 1k / ⭐ 35 / LLM‑jp‑Moshi‑v1 は、7BパラメータのMoshiアーキテクチャをベースに構築された実験的な日本語の全二重音声チャットモデルで、J‑CHATとZoom対話データで微調整され、Linux GPUシステム向けのweb‑UIデモとともに Apache 2.0 ライセンスの下でリリースされました。
 * [Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf) - 📥 1k / ⭐ 2 / GGUF形式のQwen3‑Swallow‑30B‑A3B‑SFT‑v0.2モデル、tokyotech‑llm によってリリースされ、TFMC/imatrix‑dataset‑for‑japanese‑LLM から取得した imatrix データで構築され、llama.cpp CUDA で使用可能な状態です。
 * [SIP-jmed-llm-3-8x13b-OP-32k-R0.1-GGUF](https://huggingface.co/hiratagoh/SIP-jmed-llm-3-8x13b-OP-32k-R0.1-GGUF) - 📥 1k / ⭐ 3 / GGUF に変換され、量子化された、研究専用の日本語 SIP‑jmed‑llm‑3‑8x13b‑OP‑32k‑R0.1 主権医療推論モデルは、日本の SIP プログラムのもとで安全かつオープンな医療 LLM 用に開発され、研究・デモ用途（例：Ollama + Dify）に備えられていますが、臨床意思決定には使用しません。
 * [RakutenAI-3.0-gguf](https://huggingface.co/mmnga-o/RakutenAI-3.0-gguf) - 📥 1k / ⭐ 5 / GGUFに変換されたバージョンの RakutenAI‑3.0 は、imatrix データセットから構築され、llama.cppで日本語のLLMを実行するために使用できます。
 * [cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf](https://huggingface.co/mmnga/cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf) - 📥 1k / ⭐ 55 / Cyberagent の gguf‑converted DeepSeek‑R1‑Distill‑Qwen‑14B‑Japanese モデル（TFMC imatrix dataset から構築）は mmnga の下で利用可能で、CUDA サポートを使用して llama.cpp で実行できます。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 1k / ⭐ 3 / T5 v1.1モデルで、日本語WikipediaとmC4/jaで事前学習済み。GEGLU活性化関数を採用し、事前学習中にドロップアウトは使用せず、埋め込み層と分類器の共有は行っていない。CC‑BY‑SA 4.0 の下で配布（商用利用は事前連絡が必要）。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 1k / ⭐ 2 / DataPilot-ArrowPro-7B-RobinHood‑gguf は、imatrix Japanese LLM データセットを用いて DataPilot の ArrowPro‑7B‑RobinHood モデルを gguf フォーマットに変換したもので、llama.cpp で推論可能です。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 12 / Sarashina2.2 は、SB Intuitions が三段階パイプラインと合成データを用いて訓練した 0.5‑B、1‑B、および 3‑B の言語モデルを提供し、最高の日本語 QA、数学、およびコーディングスコアを達成し、指示調整されていない事前学習済みの重みを提供するが、偏った出力を生み出す可能性があります。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 3M / ⭐ 23 / 2009年から2024年までのNicoNico Liveのコメントログ（150GB超）を集約し、転換前・転換後・リアルタイムNX‑Jikkyoのキャプチャも含む、歴史的なTV‑broadcastディスカッションを簡単に取得できるAPIを提供します。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 158k / ⭐ 7 / VOICEVOXで作成された人工音声データセットで、ITA、Tsukuyomi‑chan、ROHANコーパスから構成され、445,793個のWAVファイルを含み、総再生時間が577時間51分23秒です。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 17k / ⭐ 16 / 日本語および多言語のQA、NLI、パラフレーズデータセットのカタログで、各データセットの検索またはQAタスクとライセンス（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）を詳細に記載。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 11k / ⭐ 9 / Cauldron‑JAは、DeepL APIを使ってThe Cauldronから翻訳された44個のサブデータセットからなる日本語ビジョン‑ランゲージデータセットです。HuggingFace’s datasets library を通じて入手可能で、オリジナルセットと同一のライセンスで提供され、プロンプトはCC‑BY‑4.0でリリースされています。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 9k / ⭐ 109 / Nemotron‑Personas‑Japan は、CC BY 4.0 のオープンソースデータセットであり、高品質の合成生成された日本人ペルソナ（名前、性別、年齢、背景、婚姻状況、学歴、職業、所在地を含む）で、実際の人口統計・地理・人格分布に基づいており、確率的グラフィカルモデルと GPT‑OSS‑120B を用いて多様性を高め、バイアスを減らし、モデル崩壊を防ぎ、主権 AI の開発を支援し、商業利用をサポートするよう設計されています。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 5k / ⭐ 28 / FineWeb2 Edu Japanese は FineWeb2 からの約1億2000万の高品質教育用日本語テキスト（約893億トークン）を提供し、DeepSeek‑API クラスフィケーター（スコア ≥ 2.5）でフィルタリングし、ModernBERT‑Ja‑130M でトークナイズされ、512 トークン以下の小規模サブセットを含みます。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 5k / ⭐ 4 / Japanese Medical VQA 12M は、Open‑PMC‑18M から派生した、1200万枚を超える日本語医療画像とキャプションを含む商用利用可能なマルチモーダルデータセットです。Parquet/Webdataset 形式で提供され、オリジナルと日本語翻訳画像、充実したキャプション、および InternVL3.5、Qwen3‑30B、GPT‑oss 120B を使用して生成された VQA スタイルの Q&A ペアを含みます。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 3k / ⭐ 110 / ReazonSpeech は、FLAC エンコードされた日本語音声コーパスで、文字起こし付きです。8.5 h から 35,000 h までの 5 つのサイズで提供され、Hugging Face 経由で CDLA‑Sharing‑1.0 ライセンスの下でダウンロードでき、日本著作権法第 30‑4 条の規定により使用が制限されています。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 3k / ⭐ 39 / Aozora Bunkoから取得したパブリックドメイン日本語テキストのユーザーフレンドリーで重複除去済みCSVデータセット。globis-org/aozorabunko‑extractorで処理され、現代日本語機械学習用途に合わせてクリーニング済み。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 3k / ⭐ 16 / Reazon Speech v2 dataset のミラー: Stardust‑minus によって 10 日間にわたり 8 枚の A800 GPU で UVR を使用して処理された 3,674 本のノイズ除去された音声ファイル、CDLA‑Sharing‑1.0 でリリースされ、トランスクリプトなし。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 3k / ⭐ 99 / 注釈付きタスク（要約訂正、数学推論、翻訳、創造的生成、ユーザー意図理解など）を網羅した100サンプルの日本語インストラクション・チューニング評価データセット。微調整モデルを手動または自動で5点評価できるよう設計されている。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 2k / ⭐ 5 / JAQKET は、Wikipedia から派生した日本語のオープンドメイン QA データセットであり、複数選択式のクイズ質問を含むバージョン 1.0（13,061 件の学習データ、271 件の検証データ）と、質問プロンプトのみで抽出された回答を要求するバージョン 2.0（2,154 件の学習データ、1,164 件の検証データ）を提供し、QA システムの研究を促進するように設計されています。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 2k / ⭐ 36 / Japanese‑Eroge‑Voice‑V2は、匿名化された1,033,142件のエロゲ音声–文字起こしペア（主に女性、NSFW）を2,657時間提供し、学術研究向けにMITライセンスで配布します。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 2k / ⭐ 4 / JamC‑QA は、8つの日本文化・知識カテゴリにわたる多肢選択問題のバイリンガルベンチマークで、リーダーボードメトリクスで最先端モデルを比較します。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 2k / ⭐ 19 / JMMMUは、日本語のマルチモーダルベンチマークで、ネイティブ専門家が翻訳した1,320の文化的に多様な質問（720は文化に依存しない、600は文化固有）に拡張され、現在は公開リーダーボードを備えています。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEBは日本語テキスト埋め込みベンチマークで、5つのタスク（クラスタリング、分類、STS、検索、リランキング）と28のデータセットを特徴とし、1行で評価できるスクリプトを提供し、コミュニティの貢献を歓迎する。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 2k / ⭐ 47 / 日本語 NLP ベンチマーク（Yahoo Japan と早稲田大学が作成）に対する JGLUE データセットカードとロードスクリプトを更新しました。テキスト分類（MARC‑ja、JCoLA）、文対分類（JNLI）、QA（JSQuAD、JCommonsenseQA）をカバーし、リリースは GitHub と Hugging Face にリンクされています。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 1k / ⭐ 89 / databricks‑dolly‑15k データセットの自動翻訳された日本語版、CC‑BY‑SA‑3.0 ライセンス、2023‑05‑11に最終更新。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 1k / ⭐ 4 / 日本語の検索/QAデータセットを提供し、5つの多言語/日本語リランカー（例：BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）によって算出されたクエリごとのスコアを含む。各クエリごとに約200件の正例と負例ドキュメントの平均スコアも含まれる。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 1k / ⭐ 6 / Japanese XL‑Sum subset は PaLM‑2 15‑gram overlap を通じてフィルタリングされ、4,215件のトレーニング例、758件の検証例、766件のテスト例を含みます。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 978 / ⭐ 23 / cc100-jaは、cc100データセットの日本語部分を集めたもので、シャーディングされたParquetファイルとして提供されています。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 919 / ⭐ 7 / JMedBenchは日本語医療・生物医学用LLMベンチマークであり、20のデータセットをMCQA、NER、STSなどを含む5つのタスクにまたがって構成しています。データセットはMedMCQA、PubMedQA、MMLUなどから取得されており、それぞれに独自のライセンスが付属しています。また、翻訳にバイアスが含まれる可能性があるため、人間によるレビューが必要であるという注意事項が記載されています。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 918 / ⭐ 133 / Japanese Anime Speech Dataset V2は、292,637件の整理済みオーディオ‑テキストペア（約397.5時間のSFW、および52.4時間のNSFWコンテンツ）を、セーフティ別に分割された128‑kbps MP3ファイルとして提供し、特に自動音声認識モデルのトレーニング用に設計されています。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 827 / ⭐ 2 / 日本語ウィキペディアテキストのパラフレーズから生成されたLLM生成クエリと回答のデータセット。ライセンス制限付きモデルを使用せずに構築され、CC‑BY‑SA 4.0で公開されています。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 798 / ⭐ 2 / 匿名の 2ch.sc/2ch.net スレッドの大規模圧縮 JSON‑Lines データセット。スレッド ID、タイトル、掲示板と地域情報、返信数、完全な投稿メタデータ（投稿者、メール、日付、本文）を含む。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 787 / ⭐ 32 / 409時間の日本語エロゲ音声データセットで、2パス loudnorm（‑23 LUFS、‑1 dB peak、11 LRA）で処理され、litagin/anime-whisper により文字起こしされ、匿名化され、WebDataset（FLAC、JSON、TXT）として保存されています。主に女性の声が収録されており、AI文字起こしのエラーが存在する可能性があります。MIT‑licensed for academic research.
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 731 / ⭐ 11 / JMMLUは、56科目に跨る7,536問の教師作成質問を収録した、日本語のマルチタスク言語理解ベンチマークです。含まれる科目は、専門医学・心理学・会計学・哲学、及び多様な高校科目です。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 706 / ⭐ 148 / Japanese Anime Speech Dataset は、73,004 の音声‑テキストペア（合計110時間、V1 から V5 へと進化）を提供し、OpenAI’s Whisper などの ASR モデルを強化します。すべての利用に対してオープンライセンスが適用され、クレジットの表記があれば感謝します。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 690 / ⭐ 4 / Fate/Stay Nightのキャラクター「Emilia」の対話とロアのデータセットで、会話型言語モデルのトレーニングと評価のためにフォーマットされています。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 681 / ⭐ 8 / Rakuda は 40 件の日本語質問—歴史・社会・政府に関する自由回答形式と地理に特化した質問—を提供し、日本語 AI アシスタントのベンチマークに使用でき、vicuna‑eval と比較可能で、`datasets.load_dataset` で読み込むことができます。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 665 / ⭐ 32 / Galgame VisualNovelデータセット (OOPPEENN/566973746F6F6372656164656C65746572) の再構成された再アップロード。Hugging Face datasets の効率的な読み込みのため、すべてのオリジナル音声/テキストを保持し、複数のゲームサブセットオプションを備えた抽出スクリプトを提供します。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 592 / ⭐ 12 / EDINET‑Bench は、10 年分の EDINET‑API 公開レポートを使用して、会計不正検出、収益予測、業界予測などのタスクで LLM を評価する日本の金融ベンチマークです。構築・評価コードが提供され、データセットは PDL 1.0 に再ライセンスされています。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 563 / ⭐ 33 / Syosetu711Kは、2023年3月26日〜27日に小説家になろうからスクレイピングされた約711,700本の小説で構成される日本語データセットです。全テキストとメタデータ（タイトル、著者、NCode、あらすじ等）を提供し、教師なしテキスト生成および分類タスクに利用されます。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 553 / ⭐ 17 / JA‑VG‑VQA‑500 は、日本語 Visual Genome VQA データセットの 500 サンプルのサブセットで、CC BY 4.0 ライセンスが付与され、EvoVLM‑JP‑v1‑7B のベンチマークに使用されます。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 549 / ⭐ 6 / 日本語のMC4データセット (mc4-ja) のデータセットカード
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 545 / ⭐ 44 / Galgame_Speech_ASR_16kHz は 16 kHz の ASR データセットで、3.75 百万ペア（≈5,354 時間）が含まれ、Galgame_Dataset から派生しており、GPL v3.0 の下で公開され、商用利用は禁止され、訓練済みモデルはオープンソースであることが求められます（引用は任意）。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 536 / ⭐ 141 / 日本語インストラクション・チャットデータセット（LLMのファインチューニング用（例：LoRA）、9 M+サンプル）。最近更新され、ライセンス付きAlpacaデータを除外し、クリーンなWikipediaとALT出力を含め、CC‑BY‑SA 4.0でリリース。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 474 / ⭐ 22 / 日本語ウェブコレクションの56百万件の文書、110 B文字、249百万枚の画像は、大規模なビジョン-言語モデルのトレーニングに使用されます。momiji_generatorによるデータポピュレーション、OBELICS‑style visualization、サンプルモデル（Heron‑NVILA‑Lite）を提供します。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 439 / ⭐ 3 / Japanese Guardrail モデル評価データセット（1,725サンプル）で、WildGuardTest の高品質なマルチステージ翻訳で、ODC-BY ライセンスで公開され、Hugging Face で入手可能です。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 418 / ⭐ 5 / Japanese JaQuAD、QG‑Bench のサブセットは、文レベルおよび段落レベルのデータを提供し、ハイライトされた回答トークンを用いて日本語の質問生成モデルの学習に利用でき、BLEU4、METEOR、ROUGE‑L、BERTScore、MoverScore で評価されます。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 404 / ⭐ 10 / 日本語から英語への並列コーパスで、kakenサブセットの llm‑jp‑corpus‑v3 を Qwen/Qwen2.5‑32B‑Instruct で翻訳し、独自の翻訳列を備え、CC‑BY‑4.0 の下でライセンスされています。
 * [jhle](https://huggingface.co/datasets/llm-jp/jhle) - 📥 396 / ⭐ 96 / LLM‑jp によってキュレーションされた日本語訳の “Humanity’s Last Exam” データセット。画像質問は省略され、raw_subject ごとに5件をサンプリングし、機械翻訳・専門家レビュー済みです。著者は Yuji Tamakoshi、Kouta Nakayama、Yusuke Miyao で、トレーニングコーパスとして決して使用してはならない。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 388 / ⭐ 6 / 日本語データセットをSentenceTransformers対応のカラムに変換し、複数のHuggingFaceソースから取得したRerankスコア（≥0.7 を正例、≤0.3 を負例）で例をフィルタリングし、オリジナルのライセンスを尊重しつつ対照学習をサポートしました。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 378 / ⭐ 5 / STAIR‑Captionsは2017年にリリースされ、キャプション生成、マルチモーダル検索、画像生成に利用できる820,310の日本語キャプションを提供します。詳細なアノテーション、メタデータ、Creative Commons BY‑4.0 ライセンス付きです。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 361 / ⭐ 11 / JDocQAは、日本語PDFベースのQAデータセットで、5,504件のドキュメントと11,600件の質問回答ペアを含み、視覚情報とテキスト情報の両方を用いて、はい／いいえ、事実・数値・オープンエンド・不可回答の理解をテストする。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 340 / ⭐ 27 / WRIMEデータセットは、日本語の投稿42,200件からなるコレクションで、筆者、3名の読者、およびその平均に対してPlutchikの8つの感情でアノテーションされています。感情分析タスク向けに、40kトレーニング、1.2kバリデーション、2kテストのスプリットで構成されています。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 340 / ⭐ 16 / Japanese Alpaca Data は、masa3141 の Japanese Alpaca‑LoRA 作業から派生したもので、追加情報についてはオリジナルリポジトリへの参照があります。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 338 / ⭐ 2 / 日本語 Callhome 音声ファイルを WAV に変換し、JSON 形式のメタデータ配列と RTMM 話者ラベルファイルを評価用に付随させる。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 323 / ⭐ 13 / 「wikipedia-ja-20230720」日本語ウィキペディアスナップショットのデータセットカード。
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 322 / ⭐ 6 / 重複除外済み、NFKC正規化済みの mQA クエリ–パッセージペアで、pos_ids/neg_ids は collection のインデックスにマッピングされ、collection[pos_id] による直接取得が可能であり、元データセットの利用規約に基づきライセンスされています。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 319 / ⭐ 3 / 日本語版のExplainable Multi-hop Question Answering dataset は、質問、回答、Wikipedia記事を結びつけるステップバイステップの導出を特徴とし、導出フォーマットが更新され、複数のバージョンがリリースされています。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 318 / ⭐ 18 / *Project Sekai* の草薙寧々（ソースCV Machico）のボーカルトラックの一部データセットで、nene_org.txt ラベルファイルを含み、データ拡張と標準化の計画があり、リポジトリをスター、アイデアを共有し、フルコレクションのためのQQグループに参加するよう呼びかけている。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 306 / ⭐ 21 / AI生成されたアニメイラストには英語のプロンプトとPhi‑3 Vision由来のキャプション（英語と日本語）が付いており、パブリックドメインで無料利用が可能です。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 293 / ⭐ 3 / BBH‑jaはBIG‑Bench Hardデータセットの日本語訳を提供し、JSON‑L（入力・正解ターゲット）とYAML（入力・ターゲット）のChain‑of‑Thoughtプロンプトを含む評価問題を提供し、PLaMoモデルで翻訳しています。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 283 / ⭐ 3 / クリーンされた日本語ウェブコーパス（mc4‑ja など）は、教師なし学習で約10 k 文書にクラスター化され、一部のファイルのみが Parquet 形式です。ファイルリストは out フォルダーにあり、法的に許可された情報分析用途のために Git LFS でダウンロードできます。
 * [LLMChat](https://huggingface.co/datasets/team-hatakeyama-phase2/LLMChat) - 📥 279 / ⭐ 4 / LLMChatシステムからの2,139件の人間評価済みQ&Aペアのリポジトリ。各ユーザー質問には、13の参加モデルからランダムに選ばれた2つの回答が付添えられ、レビューアは優れた返答を選択 (1 = 最初、2 = 2番目、0 = どちらも劣悪、3 = どちらも優秀)。エントリには質問、両回答、評価、必要に応じて訂正された回答、モデル名、タイムスタンプ、CC0ライセンスのテキストとモデル固有の出力ライセンスが含まれる。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 269 / ⭐ 7 / JHumanEval は HumanEval benchmark の手翻訳版で、164 の Python programming problems を提供し、並行した英語と日本語のコメント付きで、日本語‑LLM のコード生成を評価しつつ、元の英語のエラーを保持します。
 * [dataset-for-annotation-v2-annotated](https://huggingface.co/datasets/preference-team/dataset-for-annotation-v2-annotated) - 📥 260 / ⭐ 3 / 多くのジャンルにわたり、ネイティブスピーカーが好みと強度（−3〜3）で注釈付けした合成質問−回答ペアの日本語データセットは、限定的な多様性、一般的なLLMフレーズパターン、実世界のシナリオの欠落、そしてより深い専門知識の機会を示しています。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 259 / ⭐ 9 / llm‑book/wrime‑sentiment のデータセットカードは、WRIME から派生した二項式日本語感情分析セットを提供し、Avg. Readers_Sentiment に基づいて「positive」または「negative」とラベル付けされます（中立ケースを含めるオプション付き）。このセットは、“Introduction to Large Language Models” のサンプルデータとして意図されています。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 258 / ⭐ 2 / JCommonsenseQA は、日本語の複数選択データセットで、CommonsenseQA の適応版として共通認識推論を対象にしています。CC BY‑SA 4.0 のライセンスの下で公開され、doi:10.5715/jnlp.30.63 として引用されています。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 249 / ⭐ 15 / Hachi-Alpacaは、Stanford Alpacaから派生した日本語合成データを提供し、mistralai/Mixtral‑8x22B‑Instruct‑v0.1で洗練・検証され、Deepinfraを通じて利用されるとともに、モデルベースの品質チェックを通過した「_cleaned」バージョンを備えています。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 248 / ⭐ 3 / 日本語版Wikipediaの文はさまざまな埋め込みとFAISSインデックスに変換され、Hugging Face Spaceデモ、変換スクリプト、検索・Q&A・OpenAI text‑embedding‑3‑smallを用いたRAGの評価が提供されます。埋め込みはOpenAIライセンス対象で、その他はCC‑BY‑SA‑4.0です。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 245 / ⭐ 14 / OpenMathInstruct‑1 から取得され、GSM8K と MATH ベンチマークの質問と検証済みの Mixtral‑8x7B で生成された合成解答がペアになった 1.8 百万件の日本語翻訳項目が、NVIDIA のライセンスに基づき商業的に利用可能となっています。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 234 / ⭐ 5 / JSNLI は、黒橋-徐-村脇研究室が公開した SNLI 自然言語推論ベンチマークの日本語訳です。TSV 形式で提供され、JUMAN++ でセグメント化された前提と仮説を含み、約 533,000 ペアと 548,000 ペアのフィルタリング済み、未フィルタリング済みトレーニングセットと、3,916 ペアの検証セットを提供します。CC BY‑SA 4.0 ライセンスの下で配布されています。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 233 / ⭐ 15 / Zundamonキャラクター設定のシンプルなデータセット—オンラインソースおよび管理データから編纂された—は、character‑LLMsのテスト用に、指定されたライセンスの下でzmnjp.jsonlおよびzmn.jsonl形式で提供されます。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 233 / ⭐ 2 / AWS Open Data RegistryからのABEJA‑CC‑JAデータセットのHugging Faceミラーで、詳細はABEJAのtech‑blog entryにあります。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 232 / ⭐ 11 / JaQuADは2022年作成の日本語QAデータセットで、Wikipediaから抽出した39,696ペアのSQuAD‑style抽出クエリで構成され、総サイズは73.2 MBです。BERT‑Japaneseでファインチューニングすると78.92 % F1（63.38 % EM）を達成します。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 215 / ⭐ 3 / 2010年の日本語ウェブコーパスは、HuggingFace にアップロードされ、2009年の著作権改革に基づき研究利用のライセンスが付与されており、形態素ベースの解析と変換スクリプトによる自動句読点付加テキストを含んでいます。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 214 / ⭐ 6 / Range3のwikipedia‑ja‑20230101リポジトリは、完全なWikipediaデータセットから抽出され、Pythonコードで生成された日本語Wikipediaテキストのみを含むParquetファイルを提供しています。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 214 / ⭐ 80 / 文章対照済みの日本語ウェブ小説の章と英語ファン翻訳（106 K+ エントリ、バージョン 2）は、翻訳研究のために設計され、更新されたアラインメント、追加されたシリーズメタデータ、品質フィルタリングなしでフェアユースと Apache 2.0 の下で配布され、Hugging Face を通じた削除リクエストの対象となります。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 206 / ⭐ 51 / AnswerCarefully Datasetは、商業利用または非商業利用のLLM安全向上のために日本語および多言語データを提供し、他の使用（安全迂回を含む）を禁止し、帰属を伴う派生作品を許可し、害やサービス変更に対する非責任の創作者免責事項を付帯しています。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 203 / ⭐ 9 / JSICKはSICKから翻訳された日本語NLI/STSデータセットで、語順と格助詞の取り扱いを検証するストレステストを提供し、複数の変換された文対サブセットを通じて多言語合成推論の研究を支援します。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 202 / ⭐ 6 / Dataset card for “oscar2301-ja-filter-ja-normal”、現在詳細情報が不足しています。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 201 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) は、Integration、Reasoning、Logical、Table、Abstention を網羅したマルチカテゴリ QA dataset を提供し、日本語 RAG ジェネレーターの評価を目的としています。このデータセットは人手と GPT‑4.1 によって構築され、CC BY‑SA 4.0 の下でリリースされています。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 200 / ⭐ 16 / 日本語の仮名から漢字への変換のための1億9千万ペアのJSONLデータセットで、zenz‑v2.5 medium、small、xsmall モデルを支え、AJIMEE‑Bench 評価コーパスを含む。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 198 / ⭐ 11 / Range3/wiki40b‑ja は、日本語サブセットの wiki40b データセットをホストし、Python データ処理パイプラインで生成された 3 つの Parquet ファイルとして提供します。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 197 / ⭐ 8 / JMMMU‑Pro は、Vibe Construction を通じて構築された日本語のマルチモーダルベンチマークであり、生成型モデリングと人間による検証を組み合わせて、低コストかつ高品質な画像‑QA データを生成し、オープンソース LMMs の欠点を明らかにし、将来の VQA 研究を導くものです。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 185 / ⭐ 4 / JFWIRは、fine‑web教育クローラから構築された64 百万ペアの日本語情報検索データセットで、文書ごとに7種類のクエリを提供し、ハードネガティブを含み、以前のベースラインよりも実証的に優れたベンチマーク性能を示します。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 185 / ⭐ 2 / オープンで CC-BY-4.0 ライセンスの日本語証券表データセットで、画像、バウンディングボックス付き OCR テキスト、および直接セル値 Q&A を提供し、マルチモーダル vision‑language model training に使用。NTCIR‑U4 と EDINET をベースにしています。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 184 / ⭐ 16 / Galgame_Speech_SER_16kHzは、Galgame_Speech_ASR_16kHzから派生した3.7 百万ファイル（5,353時間、104 GB）の感情音声データセットで、ローカルLLMによって注釈付けされ、GNU GPL v3.0に基づき商業利用が禁止されています。このデータセットを使って訓練されたモデルはオープンソースでなければならず、必須の引用は不要です。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 182 / ⭐ 15 / 『Large Language Model Introduction』で使われるJGLUE datasetのデータセットカード。元のリポジトリ (original repo) から取得し、コードはCC BY‑SA 4.0でライセンス、データは配布者のライセンスに基づく。Kurihara & Kawahara（日本語）を引用し、Shunsuke Kitada’s repository をベースに構築。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 182 / ⭐ 18 / Databricks‑dolly‑15k‑ja dataset は、instruction tuning 用に作られた databricks‑dolly‑15k の日本語版で、DeepL で翻訳されました。日本の LLM‑jp プロジェクトが作成し、著者は Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama、Takumi Okamoto です。
 * [relaion2B-en-research-safe-japanese-translation](https://huggingface.co/datasets/llm-jp/relaion2B-en-research-safe-japanese-translation) - 📥 176 / ⭐ 4 / text2dataset、Gemma-2-9b-it、vLLMを使用して構築された高速な英語→日本語翻訳パイプラインで、concise, open-weight LLM promptを介して大規模なrelaion2B-en-research-safeコーパスを変換します。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 175 / ⭐ 12 / LLM‑jpは、英語サブセット oasst2（kunishou/oasst2‑135k‑ja から派生）の DeepL 翻訳による日本語指示チューニングデータセットを提供し、Kiyomaru と Kodama によってコンパイルされています。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 168 / ⭐ 5 / J‑HARD‑TTS‑Evalは、日本語のオートレグレッシブTTSモデルにおける短シーケンス安定性、繰り返し、韻、継続などの失敗をベンチマークし、プロンプト音声とテキストを含むデータセットを提供し、Hugging Face経由で読み込むことができる。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 167 / ⭐ 16 / oasst1‑21k‑ja は、DeepL によって英語版 OASST1 サブセットから派生した日本語の instruction‑tuning データセットであり、LLM‑jp コラボレーティブプロジェクトにより日本で作成されました。お問い合わせは llm‑jp@nii.ac.jp、著者には Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama、Okamoto が含まれます。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 160 / ⭐ 10 / 検証済みのchain‑of‑thought 推論を備えた高品質な合成日本語数学問題データセット。PRM800K と GSM8K を Qwen2‑7B‑Instruct で翻訳し、正確性をフィルタリングして作成。Hugging Face datasets ライブラリ経由で利用可能。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 157 / ⭐ 33 / Allganize RAG Leaderboard は、財務・通信・製造・公共部門・小売りという5つの業界分野にわたる日本語 RAG パフォーマンスデータと自動化されたエンドツーエンド評価結果を公開し、包括的な日本語ベンチマークがまだ存在しない状況で、パーサー・リトリーバル・生成コンポーネントのベンチマーク作成を企業が支援できるようにしています。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 155 / ⭐ 24 / AutoWikiQAは、日本最大の無料QAデータセット（2 ,377 ,503ペア）で、Swallow‑MXとvLLMを使用してWikipediaテキストから生成され、知識注入と検索補強生成のために多様でテンプレートフリーな質問と回答を提供します。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 145 / ⭐ 26 / 失敗フラグ付きの日本語翻訳済み OpenAssistant/oasst1 データ、約2,000件の手動で修正されたコード翻訳エラー、リリース済みのチャットフォーマットサブセット (oasst1‑chat‑44k‑ja)、およびファインチューニング用にエントリをインストラクション–アウトプットペアに変換するスクリプト。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 141 / ⭐ 19 / Retrieval‑Augmented Generation (RAG) を評価するための日本語 QA データセットで、JAQKET 質問と Wikipedia パッセージから構築され、金ラベル付きの検索関連性ラベルを持つ。HuggingFace と GitHub でリリースされ、主に nDCG@10 で評価される。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 141 / ⭐ 3 / 『Introduction to Large‑Scale LLM II』で使用され、llm‑jp‑eval によって作成されたクロスデータセットの日本語LLM評価用のja‑vicuna‑qa‑benchmarkのデータセットカード（Apache 2.0）。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 136 / ⭐ 10 / JA‑Multi‑Image‑VQAは、39枚の画像と55問の質問からなるデータセットで、マニュアルで作成された日本語のQ&Aが含まれ、マルチイメージVQA用に設計されています。load_dataset経由でアクセスでき、テキストはApache 2.0ライセンスで提供されます（画像の使用は制限されています）。
 * [jawiki-bullet-points](https://huggingface.co/datasets/hpprc/jawiki-bullet-points) - 📥 136 / ⭐ 4 / CC‑BY‑SA‑4.0 ライセンスの日本語Wikipediaテキストのデータセットを、Apache‑2.0 ライセンスの DeepSeek R1 Distill Qwen 32B モデルで箇条書きに変換。重複を許容するランダムサンプリングで生成されましたが、改行が Hugging Face 上で必ずしも明確に表示されるとは限りません。
 * [nagisa_stopwords](https://huggingface.co/datasets/taishi-i/nagisa_stopwords) - 📥 130 / ⭐ 2 / 147語の日本語ストップワードリストは、CC-100 Wikipedia から取得し、MIT ライセンスで提供され、nagisaトークナイザに nagisa.stopwords として組み込まれているため、簡単に利用できます。
 * [EliteVoiceProject](https://huggingface.co/datasets/Elite35P-Server/EliteVoiceProject) - 📥 119 / ⭐ 12 / Elite Voice Project は、Sakura Miko の音声録音を Hololive‑準拠のデータセットへまとめ、音声認識研究のために提供し、協力者に train/test 分割の下にある構造化された `audio_raw` フォルダー（twitch、twitter、youtube）経由で新しいクリップを追加するよう呼び掛けます。ただし、Hololive の派生作品に関するガイドラインに従う必要があります。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 119 / ⭐ 2 / WAONは、ビジョン‑ランゲージモデル向けの大規模で高品質な日本語画像―テキストペアデータセットです。サイズとSigLIP‑scoreフィルタリングとURL、キャプション、パーセプチュアルハッシュ上での重複排除によって構築され、Apache 2.0のライセンスの下で提供され、日本法に基づく情報分析用途に限定されます。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 118 / ⭐ 4 / Loonwit が提供した livedoor news corpus を対象とした Dataset Card。『Introduction to Large Language Models』で使用され、Creative Commons ライセンス（CC BY‑ND 2.1 JP）付きのニュース記事を含み、HTML タグが除去されています。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 115 / ⭐ 5 / JetCopper‑10B は、CC‑100、OSCAR‑2301、HPLT v1.2、wiki40b‑ja のクリーンアップ済みサブセットから派生した、4.7 B 日本語トークンと 0.9 B 英語コードトークンを含む日本語―英語データセットであり、LOCAL AI HACKATHON #000 用に Contrail‑200m‑64k を事前学習するために使用されましたが、文境界やパープレキシティフィルタリングは実施されていません。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 112 / ⭐ 2 / Japanese Common Voice 17.0 のサブセットを提供します。649 人の話者（各 30〜300 サンプル）を対象に、45,668 の発話を話者別に 80/20 に分割し、1,000 サンプル単位の Parquet ファイルにバッチ化しています。すべて CC0 ライセンスです。
 * [oasst1-chat-44k-ja](https://huggingface.co/datasets/kunishou/oasst1-chat-44k-ja) - 📥 111 / ⭐ 10 / ShareGPT フォーマットのマルチターンチャットデータセットで、oasst1‑89k‑ja から派生し、ファインチューニングに使用されます。膨大な計算リソースを必要とし、関連する記事と GitHub/HuggingFace のリンクをご覧ください。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 110 / ⭐ 11 / Japanese Roleplay Dialogues データセットは、投稿者が1人以下または投稿数が10以下のレコードを除外し、投稿者名を正規化・匿名化し、上位2投稿者が投稿の90%以上を占め、各投稿者が少なくとも40%を寄与する会話のみを保持するようにフィルタリングされます。機械学習用途向けです。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 107 / ⭐ 7 / Livedoor News Corpus は、日本語ニュース記事データセットを提供し、5,894件のトレーニング、737件の検証、736件のテストのインスタンスに分割され、HTMLタグを除去して Creative Commons Attribution‑NoDerivs ライセンスの下で公開されています。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 107 / ⭐ 2 / 64,139件の日本人名を生物学的性別でラベル付けしたデータセット―漢字、ひらがな、ローマ字で表記―は、トレーニング44.9k、検証6.41k、テスト12.8kに分割され、ISDA'23で採択されました。
 * [japanese-stackexchange](https://huggingface.co/datasets/p1atdev/japanese-stackexchange) - 📥 106 / ⭐ 3 / 英語で書かれた日本語のStack Exchange QAデータセットで、サイトのダンプから抽出・処理され、デフォルトサブセットとフラット化されたサブセットを提供し、Hugging Face datasets経由でロード可能、CC BY‑SA 4.0でライセンスされています。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 106 / ⭐ 41 / VNTL リーダーボードは、256件のサンプルにわたるコサイン類似度スコアの平均を算出し、日本語のビジュアルノベルを英語に翻訳する際に大規模言語モデルを評価し、予備結果をランキング化し、Sugoi Translator、Google Translate、Naver Papago などのツールとベンチマークします。
 * [Swallow-Instruct-v0.1](https://huggingface.co/datasets/tokyotech-llm/Swallow-Instruct-v0.1) - 📥 105 / ⭐ 11 / Swallow Instruct v0.1 データセット—OpenAssistant2 および Japanese‑translated variants から採取された 26,479 件の会話で、特定のサンプリング設定で構築され—は、Swallow v0.1 Llama‑3 と OpenAI GPT モデル（8B‑70B）のファインチューニングのために編纂され、東京工科大学 YOKOTA Laboratory および AIST の研究者によって作成された。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 103 / ⭐ 29 / CC‑BY‑4.0 ライセンスの、日本政府 FAQ Q‑A ペア（ソースURL付き）を手作業で抽出したデータセットで、インストラクションチューニングおよびRAGテスト用に設計されており、高品質と称賛される一方で、時折フォーマットエラーや強い公式政策表現を含むことが指摘されている。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 101 / ⭐ 13 / 日本語の固有表現抽出用に、Wikipediaから派生したCC‑BY‑SA 3.0 ライセンスのデータセット。 https://github.com/stockmarkteam/ner-wikipedia-dataset/ にホストされ、Stockmark Inc. によって開発されています。
