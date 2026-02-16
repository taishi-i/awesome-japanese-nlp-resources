# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語向けのNLPに関する、Pythonライブラリ、LLM、辞書、コーパスに特化したリソースを厳選してまとめた一覧です。
このページでは、Hugging Faceで利用可能な日本語NLP特化のモデルとデータセットを掲載しています。現在、144件のモデルと93件のデータセットが含まれています。

_2026年2月16日更新_

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
   * [token-classification](#token-classification)
   * [image-to-text](#image-to-text)
   * [translation](#translation)
   * [text-ranking](#text-ranking)
   * [text-classification](#text-classification)
   * [image-text-to-text](#image-text-to-text)
   * [audio-to-audio](#audio-to-audio)
   * [text-to-speech](#text-to-speech)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | モデル名 | Downloads | Likes | カテゴリ |
|---|-------|-----------|-------|----------|
| 1 | [llm-jp-3-3.7b-instruct](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct) | 📥 2M | ⭐ 13 | text-generation |
| 2 | [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) | 📥 2M | ⭐ 22 | sentence-similarity |
| 3 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 1M | ⭐ 52 | automatic-speech-recognition |
| 4 | [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) | 📥 993k | ⭐ 3 | text-classification |
| 5 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 491k | ⭐ 74 | fill-mask |
| 6 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 387k | ⭐ 66 | sentence-similarity |
| 7 | [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) | 📥 331k | ⭐ 11 | sentence-similarity |
| 8 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 241k | ⭐ 165 | image-to-text |
| 9 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 188k | ⭐ 10 | translation |
| 10 | [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 📥 170k | ⭐ 20 | text-generation |
| 11 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 164k | ⭐ 15 | text-generation |
| 12 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 159k | ⭐ 39 | fill-mask |
| 13 | [MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) | 📥 152k | ⭐ 12 | token-classification |
| 14 | [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) | 📥 145k | ⭐ 9 | sentence-similarity |
| 15 | [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) | 📥 142k | ⭐ 4 | token-classification |
| 16 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 102k | ⭐ 7 | sentence-similarity |
| 17 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 101k | ⭐ 10 | others |
| 18 | [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) | 📥 99k | ⭐ 3 | fill-mask |
| 19 | [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) | 📥 99k | ⭐ 8 | fill-mask |
| 20 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 73k | ⭐ 58 | text-generation |

### Datasets-ranking

| # | データセット名 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 2M | ⭐ 21 |
| 2 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 5k | ⭐ 13 |
| 3 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 5k | ⭐ 33 |
| 4 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 3k | ⭐ 100 |
| 5 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 3k | ⭐ 8 |
| 6 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 3k | ⭐ 99 |
| 7 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 3k | ⭐ 10 |
| 8 | [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) | 📥 2k | ⭐ 16 |
| 9 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 2k | ⭐ 24 |
| 10 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 2k | ⭐ 19 |
| 11 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 1k | ⭐ 47 |
| 12 | [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) | 📥 1k | ⭐ 8 |
| 13 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 1k | ⭐ 130 |
| 14 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 1k | ⭐ 18 |
| 15 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 1k | ⭐ 31 |
| 16 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 1k | ⭐ 4 |
| 17 | [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) | 📥 1k | ⭐ 10 |
| 18 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 1k | ⭐ 7 |
| 19 | [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) | 📥 1k | ⭐ 108 |
| 20 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 895 | ⭐ 6 |

## Models
### text-generation
 * [llm-jp-3-3.7b-instruct](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct) - 📥 2M / ⭐ 13 / NIIのLarge Language Models R&D Centerがリリースした、日本語・多言語言語モデル（1.8 bn〜13 bnパラメータ、base・instructバリアント）は、Hugging Face Transformers向けにパッケージ化され、Japanese Wikipedia、Common Crawl、WARP/PDF/HTML、Kaken、English Wikipedia、Dolmaデータセットで事前学習されています。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 170k / ⭐ 20 / OpenCALM は、decoder‑only 日本語 Transformer 言語モデル（160 M〜6.8 B パラメータ）のスイートで、CyberAgent, Inc. によって CC‑BY‑SA 4.0 の下でリリースされました。日本語 Wikipedia と Common Crawl でトレーニングされ、Hugging Face の torch‑transformers を通じて利用可能です。
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 164k / ⭐ 15 / CC‑100、C4、Wikipedia で学習された12‑layer、768‑hidden の日本語 GPT‑NeoX モデル。Huggingface と互換性があり、各文の末尾に必ず笑顔の絵文字を付けるオプションのトイプレフィックス調整ウェイトが付属しています。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 73k / ⭐ 58 / 2.7Bパラメータの日本語 GPT‑NeoX モデルは、ABEJA Inc. が日本語 CC‑100 と OSCAR で学習し、Hugging Face Transformers パイプラインまたは PyTorch で利用可能で、MIT license の下で公開されています。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 34k / ⭐ 35 / TinySwallow‑1.5Bは、Sakana AIとSwallow Teamによるコンパクトな日本語指示‑フォロー型言語モデルで、Qwen2.5‑32B‑InstructからのTAID蒸留を利用し、さらに日本語テキストで事前学習が追加され、研究利用のみを目的としてApache 2.0でリリースされています。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 34k / ⭐ 28 / LFM2.5‑1.2B‑JPは、LFM2.5ハイブリッドアーキテクチャ上に構築された1.2 Bパラメータの日本語テキスト生成モデルで、生成と完了タスク向けに最適化され、Hugging Faceにホストされ、llama.cpp経由で実行可能です。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 20k / ⭐ 21 / Llama3 Swallowは、2024年7月1日にリリースされた、日本語拡張のMeta Llama 3ファミリーで、Instructとchat形式の8Bおよび70Bバリアントを提供し、SFTとChat VectorでMegatron‑LM上で微調整され、主要な日本語NLPタスクでベンチマークされている。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 19k / ⭐ 142 / Llama‑3‑ELYZA‑JP‑8B は、ELYZA によって開発された日本語強化版で、8 billion パラメータ（80億）を持つ Llama 3 モデルで、Meta‑Llama‑3‑8B‑Instruct 上で日本語用に微調整されています。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 13k / ⭐ 18 / Japanese Stable LM Base Gamma 7BをShisa 7B dataでFine‑tunedし、JA MT‑Benchで強い結果を得ました。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 11k / ⭐ 18 / Llama 3.1 Swallowは、MetaのLlama 3.1の事前学習を継続して日本語性能を向上させ、合成日本語データで指示ファインチューニングを行う8‑Bおよび70‑Bモデルのセットです。これにより、gemma‑3‑27b‑itと同等の会話挙動を備えた複数のリリースバリアントが提供されます。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 10k / ⭐ 25 / rinnaの日本語GPT‑2 smallは、12層、768ユニットの隠れ層を持つtransformerで、日本語CC‑100とWikipediaをデータとして学習され、SentencePieceでトークナイズされ、MITライセンスのもとで2021年8月25日にリリースされました（Hugging Face: rinna/japanese‑gpt2‑small、詳細は https://arxiv.org/abs/2404.01657 を参照）。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 8k / ⭐ 85 / Rinnaの24層、1024ユニットの日本語GPT‑2‑mediumモデルは、CC‑100とWikipediaをSentencePieceトークナイゼーションで学習され、rinna/japanese‑pretrained‑modelsリポジトリで入手できます（MITライセンス、2021年4月7日リリース、2021年8月25日更新）。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 実験的な日本語モデルは、lightblue/suzume‑llama‑3‑8B‑japanese と Meta‑Llama‑3‑8B‑Instruct の違いを chat‑vector approach を使って抽出し、upsampled して Meta‑Llama‑3‑70B‑Instruct に適用した結果、ほとんど変更がなく、将来のスケーリング計画を立てている。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 8k / ⭐ 135 / LFM2.5‑1.2B‑JPは日本語最適化されたチャットモデルで、LFM2より日本語知識と指示に従う能力で優れ、LoRAによるファインチューニング、Transformers、vLLM、llama.cppを使った推論をサポートし、50.7 JMMLU、58.1 M‑IFEval、56.0 GSM8Kのスコアを達成しています。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 5k / ⭐ 24 / Llama 3.1 Swallowは、継続的なプレトレーニングと日本語特有のインストラクションファインチューニングで訓練された8B / 70B Llama 3.1モデルの日本語強化シリーズです。最新の8B‑Instruct‑v0.3は、日本語MT‑Benchで最先端の結果を示しています。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 4k / ⭐ 26 / 日本語用 3.6 B‑parameter GPT‑NeoX モデルで、指示に従うことを目的として fine‑tuned（SFT‑v2）。ChatGPT での以前の SFT と比較して 100 件のプロンプトで評価され、2023年3月31日にリリース。
 * [shisa-v2.1-unphi4-14b](https://huggingface.co/shisa-ai/shisa-v2.1-unphi4-14b) - 📥 3k / ⭐ 4 / Shisa V2.1 は、再サンプリングされたデータと新しい instruction‑following、translation、politeness など、日本語特有の機能を追加して、Shisa V2 バイリンガル日本語―英語チャットモデルを改良し、1.2 B から 70 B までのバージョン（Llama 3.2/3.3 や Qwen 3 バリアントを含む）を Apache 2.0、MIT、LLM ライセンスの下で提供し、競争力のある JA/EN ベンチマークを実現しています。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 3k / ⭐ 74 / ELYZA‑japanese‑Llama‑2‑7b は、Meta の Llama‑2 モデルの 6.27B パラメータ拡張で、インストラクトとファストバリアントで日本語データ上で事前学習され、Hugging Face Transformers を通じて利用できるものです。
 * [Swallow-7b-instruct-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-instruct-hf) - 📥 3k / ⭐ 44 / TokyoTech‑LLMは、Swallow Llama 2 ファミリーを提供しています。7 B、13 B、70 Bモデル向けの日本語強化、教師付き微調整済み、語彙拡張なしのバリアントで、最近のリリースには Swallow‑7b‑instruct‑v0.1 と Swallow‑70b‑NVE‑hf が含まれます。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 2k / ⭐ 16 / NIIから提供される1.8 Bパラメータのllm‑jp‑3.1‑1.8b‑instruct4日本語指示‑調整モデルは、Hugging Face TransformersおよびTorch ≥ 2.3.0に互換性があり、事前学習済みと微調整済みのチェックポイント、ならびに使用例を含みます。
 * [Murasaki-8B-v0.1-GGUF](https://huggingface.co/Murasaki-Project/Murasaki-8B-v0.1-GGUF) - 📥 2k / ⭐ 4 / Murasaki‑8B‑v0.1 は 8‑billion パラメータを持ち、CoT 対応の System 2 翻訳モデルで、ACGN コンテンツ向けに設計されています。複数の GGUF‑quantized 形式でリリースされ、Murasaki‑ACGN ベンチマークで競合 LLM を上回ります。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 2k / ⭐ 48 / 日本語で継続的にプレトレーニングされたMistral‑Nemoモデル（Mistral‑Nemo‑Japanese‑Instruct‑2408）は、mistralai/Mistral‑Nemo‑Instruct‑2407 を基に構築され、device mapping と ChatML プロンプトを備えた transformers で利用可能で、Apache‑2.0 ライセンスの下で Ryo Ishigami により公開されました。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 2k / ⭐ 1 / 日本語対応・指示調整済みのGemma‑2モデルは、Llama（2b/9b/27b 事前学習版と指示版）に基づいて構築され、2025年5月19日にリリースされ、HuggingFaceとSwallowチームのウェブサイトから入手できます。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 2k / ⭐ 17 / LLM‑jp‑3.1‑13b‑instruct4 は、13‑B の指示事前学習済み日本語言語モデルで、NII の R&D Center によって開発され、Hugging‑Face Transformers のチェックポイントとして UNIGRAM‑byte‑fallback トークナイザー付きで公開されました。
 * [Llama-3.3-Swallow-70B-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-v0.4) - 📥 2k / ⭐ 4 / Llama 3.3 Swallow は 70 billionパラメータ（＝700億パラメータ）のモデルで、Meta の Llama 3.3 を拡張し、英語の性能を保ちながら日本語機能を強化しています。このモデルは継続的な事前学習と指示ファインチューニングを経て構築され、2024年12月以降に複数の Instruct バリアントがリリースされ、HuggingFace で利用可能です。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 2k / ⭐ 20 / OpenCALMは、CyberAgentが開発した日本語専用のデコーダオンリートランスフォーマー言語モデル（160 M〜6.8 Bパラメータ）のファミリーです。日本語のWikipediaとCommon Crawlで学習され、CC BY‑SA 4.0の下でリリースされています。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 2k / ⭐ 10 / リポジトリは、Massed Compute ハードウェアで作成され、TheBloke の a16z ファンド付き LLM 仕事の一部として、Stability AI の日本語 StableLM Instruct Gamma 7B の GGUF 形式で量子化されたモデルファイルを提供します。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 57 / TinySwallow‑1.5B‑Instruct は、TAID を用いて Qwen2.5‑32B‑Instruct から蒸留された 1.5 B の日本語インストラクション調整済みオートレグレッシブ言語モデルであり、研究目的のみに利用されることを想定しています。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 2k / ⭐ 7 / 日本語で事前学習済み TinyLlama (≈50 k ステップ) は、約3 B OSCAR/mC4トークンで構築され、HuggingFace Transformers または VLLM で使用可能です。Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru、Renju Aoki が作成しました。
 * [Mistral-Nemo-Japanese-Instruct-2408-GGUF](https://huggingface.co/QuantFactory/Mistral-Nemo-Japanese-Instruct-2408-GGUF) - 📥 2k / ⭐ 18 / gguf‑quantized U‑Lens リリースの cyberagent の Mistral‑Nemo‑Japanese‑Instruct‑2408 は llama.cpp で構築され、mistralai の Mistral‑Nemo‑Instruct‑2407 をベースにし、Apache‑2.0 の下で配布され、更新された transformers インターフェースを通じて使用されます。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 2k / ⭐ 96 / ELYZA-japanese-Llama-2-7bは、MetaのLlama-2 7 Bの日本語最適化拡張で、インストラクトバリアントとファストバリアントを提供し、6.27–6.37 Bパラメータを有し、Hugging‑Face Transformers libraryを通じてアクセスできます。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 1k / ⭐ 34 / SB Intuitionsから提供される自己回帰型日本語モデル（sarashina2.2‑3B‑instruct‑v0.1）を、他のモデルとベンチマークし、使用例スクリプト付きで提供。安全性トレーニングは限定的である旨の注意書きが付いています。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 1k / ⭐ 21 / youri‑7bは、Llama2‑7bをベースに構築された32層、4096ユニットの隠れ層を持つトランスフォーマーです。CC‑100、C4、OSCAR、Pile、Wikipediaから約40 Bの日本語トークンで継続的に事前学習され、2023年10月31日にリリースされました。AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA、Winograndeで競合力のあるスコアを達成しています。
 * [llm-jp-3-13b-instruct](https://huggingface.co/llm-jp/llm-jp-3-13b-instruct) - 📥 1k / ⭐ 31 / 日本語大型言語モデル（llm‑jp‑3‑13b‑instruct 及びそのバリエーション） は NII から提供され、Hugging Face Transformers をベースに構築され、2.1 T パラメータを持ち、ユニグラムバイトフォールバックトークナイザーを使用し、混合日本語/英語コーパスで訓練され、GENIAC の一部資金提供を受けています。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 1k / ⭐ 16 / 6層、512ユニットの隠れ層を持つトランスフォーマーで、Japanese GPT‑2 xSmall と呼ばれ、Japanese CC‑100 および Wikipedia を SentencePiece でトークナイズして学習された。2021年8月25日に MIT ライセンスで公開され、Hugging Face（rinna/japanese‑gpt2‑xsmall）にホストされ、arXiv 2404.01657 で引用されている。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 1k / ⭐ 25 / Hugging Face‑互換の日本語中心のトランスフォーマーモデル（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct）は情報学研究所から提供され、Wikipedia、Common Crawl、WARP、Kaken、Dolma を含む多様な日本語・英語コーパスで事前学習されており、torch ≥ 2.3、transformers ≥ 4.40、accelerate、flash‑attn を必要とします。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 81 / ELYZA の Japanese‑enhanced Llama‑2‑7B は、standard、instruct、fast バリアントで拡張日本語対応を実現するよう事前学習され、詳細な使用例、開発者クレジットが付随し、Meta の Llama‑2 Community License の下でライセンスされています。
 * [open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - 📥 1k / ⭐ 205 / OpenCALMは、CyberAgent, Inc.が提供する日本語のデコーダーのみのトランスフォーマー言語モデルスイートです。160 M〜6.8 Bパラメータのバージョンがあり、Wikipedia と Common Crawl で事前学習されています。Transformers ライブラリ経由で CC BY‑SA 4.0 ライセンスの下で利用できます。
 * [llm-jp-3-980m](https://huggingface.co/llm-jp/llm-jp-3-980m) - 📥 1k / ⭐ 3 / リポジトリは NII からの 980 M パラメータを持つ LLM‑jp‑3 モデルをホストし、日本語 Wikipedia、Common Crawl、WARP、Kaken で事前学習済みの Hugging‑Face チェックポイントとして提供しています。このモデルは torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8 を必要とします。
 * [sarashina2.2-1b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1) - 📥 1k / ⭐ 15 / このリポジトリは、SB Intuitions の 1 B‑パラメータ自動回帰日本語指示モデル sarashina2.2‑1b‑instruct‑v0.1 をホストし、他の日本語‑BERT と比較して日本語と英語の MT と指示タスクでベンチマークを行っています。さらに、torch‑transformer の使用例と安全性トレーニングが限定的である旨の警告も付録として含まれています。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 491k / ⭐ 74 / 2019年の日本語Wikipediaを対象に、IPA辞書と全単語マスキングを用いて事前学習されたJapanese BERT‑base、12層、768次元、32,000語語彙、512トークンシーケンス、1Mステップ、CC‑BY‑SAの下でcl‑tohoku/bert‑japaneseから入手可能。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 159k / ⭐ 39 / 約17 Mの日本語Wikipedia文（2.6 GB）で事前学習済みのBERT base modelで、IPA dictionaryとWordPieceでトークナイズし、12層／768-dim hidden states／12 headsを有し、32 000-token vocabularyを備え、1 MステップでCloud TPUs上で訓練され、CC‑BY‑SA 3.0でリリースされています。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 99k / ⭐ 3 / 日本語RoBERTa‑baseモデルは、約10 M件の日本語医学要旨と1.4 M件のJST本文で事前学習され、30 kトークンのSentencePieceでトークナイズされ、CC BY‑4.0で公開され、Hugging Face pipelinesで利用可能です。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 99k / ⭐ 8 / 日本語のBERT‑baseモデル（12層、768次元の隠れレイヤー、12ヘッド）は、MeCab IPA単語レベルトークン化を経て文字レベルトークン化で4000語語彙に変換し、約1700万文（2.6 GB）の日本語Wikipediaで事前学習されました。学習コードはcl‑tohoku/bert‑japaneseにあり、CC BY‑SA 3.0 でリリースされています。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 54k / ⭐ 6 / BERT‑base Japanese model（12層、768‑次元の hidden states、12ヘッド）を、30 M Wikipedia 文（約4 GB）で Unidic 2.1.2 を用いた単語レベルトークン化の後、文字レベルトークン化と全単語マスクを行い、512トークンのシーケンス、256バッチ、1 M トレーニングステップで訓練しました。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 43k / ⭐ 48 / LINE DistilBERT Japanese は、インハウスの BERT‑base 先生を用いて 131 GB の日本語ウェブテキストで事前学習された 66 百万パラメータの DistilBERT モデルであり、JGLUE で評価され、MeCab Unidic と SentencePiece でトークナイズされ、Apache 2.0 ライセンスの下でリリースされました。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 21k / ⭐ 8 / 171 GBの日本語Wikipedia、CC‑100、OSCARでトレーニングされた日本語DeBERTa V2 large modelは、文字レベルのsentencepieceトークナイズと全単語マスキングを使用し、Hugging Face Transformersを通じて下流でのファインチューニングに準備できています。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 10k / ⭐ 39 / Japanese‑Roberta‑Base は rinna Co., Ltd. が開発した事前学習済みのマスク言語モデルで、正しいロード方法、トークン前処理、位置ID処理、および使用例に関するガイドラインがあり、先頭に `[CLS]` トークンが必要であることと、一貫したトークン化を強調しています。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 7k / ⭐ 27 / Japanese BERT‑base (12 layers, 768 hidden, 12 heads) は、Unidic 2.1.2 単語レベルトークナイゼーション、WordPiece サブトークナイズ、および whole‑word マスクリングを使用し、4 GBの日本語Wikipedia（約30 M文）で事前学習されています。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 7k / ⭐ 47 / 132 Mパラメータの日本語 ModernBERT モデルで、ローカルグローバルとRoPE注意を組み合わせ、4.39 T トークン（日本語/英語）で訓練され、102 kサイズの語彙、最大8,192トークン長、Flash Attention 2 に最適化されています
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 4k / ⭐ 30 / 日本語 DeBERTa V2 ベースモデルは、171 GBの日本語 Wikipedia、CC‑100、OSCAR データを用いて Juman++ セグメンテーションと SentencePiece トークン化で事前学習され、8枚の NVIDIA A100 GPU を 3週間使用してトレーニングされ、ファインチューニングに向けて準備ができています。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 3k / ⭐ 32 / Japanese RoBERTa‑baseはJapanese WikipediaとJapanese CC‑100で事前学習され、Juman++の単語分割とSentencePieceのトークナイズを使用し、1週間で8台のNVIDIA A100 GPU上でAdam（lr = 1e‑4、native AMP）で訓練され、微調整可能で、JGLUEにおける結果が報告されている。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 3k / ⭐ 20 / ModernBERT‑Ja‑310M は local‑global attention と RoPE を組み合わせた日本語 BERT 変種で、4.09 T tokens の日本語／英語テキストで訓練され、102 400語の語彙、8 192トークンのシーケンスをサポートし、Flash Attention 2 用に最適化されています。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 3k / ⭐ 2 / Japanese DeBERTa V2 tinyは、約171 GBの日本語Wikipedia、CC‑100、およびOSCARコーパスで事前学習され、Juman++による形態素解析が必要です。8台のNVIDIA A100 GPUを使用して33時間で訓練され、下流タスクに微調整できます。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 2k / ⭐ 5 / ModernBERT‑Ja‑30Mは、ローカルおよびグローバル注意機構をRoPEと組み合わせた日本語BERTバリアントです。4.39 TBの日本語／英語テキストで訓練され、8,192トークンのシーケンスをサポートし、30 Mから130 Mパラメータのサイズで提供され、Flash Attention 2との組み合わせで最も効果的です。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 2k / ⭐ 4 / DeBERTaV2 base は日本語コーパス（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）でトレーニングされ、FP‑16 ファインチューニングで NLU タスク（JSTS、JNLI、JCommonsenseQA）に適用され、CC BY‑SA 4.0 の下でリリースされ、日本の研究助成金で資金提供されました。
 * [llm-jp-modernbert-base](https://huggingface.co/llm-jp/llm-jp-modernbert-base) - 📥 1k / ⭐ 11 / ModernBERT‑base モデルは 3.4 TB 日本語 llm‑jp‑corpus v4 で学習され、2 段階（max_seq_len 1024 → 8192）で微調整され、0.92 JSTS、0.91 JNLI、0.88 JCoLA を達成します。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 1k / ⭐ 6 / ModernBERT‑Ja‑70M は、ローカルとグローバル注意を RoPE と組み合わせた軽量な日本語 BERT 変種です。4.39 T の混合言語トークンでトレーニングされ、語彙数 102 400、最大 8 192 トークンをサポートし、Flash Attention 2 に対応しています。パラメータ数は 30 M から 310 M の複数サイズで提供されます。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 2.6 GBのWikipedia（約1700万文）で訓練された12層、768次元のBERT‑Base日本語モデルで、IPA‑dictionary文字トークナイズとwhole‑word maskingを使用し、CC‑BY‑SA 3.0でリリースされた。

### sentence-similarity
 * [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) - 📥 2M / ⭐ 22 / 最終 JaColBERTv2.5 チェックポイントの重みは、新しいレシピで JaColBERTv2 データのわずか 40 % でトレーニングされ、すべてのデータセットにおいて、以前のモデルすべて（BGE‑M3 などの JaColBERTV2 多言語バリアントを含む）を上回っています。
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 387k / ⭐ 66 / Ruri v3 は、ModernBERT‑Ja をベースとした最先端の日本語テキスト埋め込みモデルで、最大8,192トークンの入力、100Kトークンの語彙、FlashAttention で加速された推論、および高速な sentence‑transformer での使用のための複数サイズバリアントをサポートします。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 331k / ⭐ 11 / 日本語一般テキスト埋め込みモデル（Ruri‑v3、30‑310 Mパラメータ、8192‑token最大、JMTEBスコアが高い）は、Sentence‑Transformers使用例と他の日本語埋め込みとのベンチマーク比較とともに提供されています。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 145k / ⭐ 9 / Ruri v3 Japanese text embeddings（30 M–310 M parameters, 8192‑token limit, JMTEB 74.5–77.2）を含み、Sentence Transformers 用の「クエリ:」または「文章:」prefixes での指示、および Sup/Unsup SimCSE、GLuCoSE、LaBSE など複数の日本語モデルのベンチマーク結果を含みます。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 102k / ⭐ 7 / Ruri v3 は、ModernBERT‑Ja をベースに構築された最先端の日本語テキスト埋め込みモデルで、最大 8,192 トークン、100 k‑トークン語彙、FlashAttention 加速、37 M から 315 M の複数サイズに対応しています。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 27k / ⭐ 22 / GLuCoSE v2 は CPU‑フレンドリーな日本語テキスト埋め込みモデルで、蒸留とマルチステージ対照学習によって微調整され、MIRACL や関連ベンチマークで同規模のモデルを上回る優れた意味的類似度と検索性能を提供します。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 23k / ⭐ 34 / GLuCoSEは、LUKEをベースに構築された日本語文埋め込みモデルであり、ウェブおよびNLI／検索データで訓練され、最大512トークンまでの768次元平均プールベクトルを出力します。類似度ベンチマークで0.864のSpearmanと0.818のPearsonを達成しています。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 20k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite は 768 次元の sentence‑transformer で、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、shunk031/jsnli 上で 1 エポックでトレーニングされ、クラスタリング、セマンティック検索、さらに Sentence‑Transformers と HuggingFace の両方の使用例を含んでいます。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 15k / ⭐ 16 / JaColBERTv2は、日本語専用のColBERTベースの検索モデルで、MMarcoで知識蒸留（31）ノルゲート／1件の正例、250kステップ、バッチ32）を使って訓練されており、現在はmultilingual‑e5‑large、BGE‑M3、JaColBERTを上回っています。完全な評価は保留中です。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 11k / ⭐ 44 / リリース準備済みのRuri v3日本語テキスト埋め込みモデル（30m–310m）のコレクションで、SentenceTransformerの使用ヒント、クエリ/パッセージプレフィックス、JMTEBベンチマーク結果を含み、他の日本語および多言語埋め込みと比較しています。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 8k / ⭐ 44 / PLaMo‑Embedding‑1B は、Preferred Networks が提供する日本語テキスト埋め込みモデルで、情報検索、分類、クラスタリングのために日本語テキストをベクトルに変換します。JMTEB ベンチマークで高い性能を示し、Apache v2.0 license の下で無料で利用できます。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 8k / ⭐ 4 / Ruri v3は、ModernBERT‑Jaをベースに構築された最先端の日本語テキスト埋め込みモデルで、8192トークンまでのシーケンス、10万語の語彙、FlashAttentionに対応し、sentence‑transformers用に30 M〜310 Mパラメータのサイズでリリースされます。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 3k / ⭐ 2 / Ruri v3は、8192トークンまでの高性能日本語テキスト埋め込み、100kトークン語彙、FlashAttentionサポート、および30 m–310 mの複数モデルサイズを備え、sentence‑transformersを介した効率的な推論とファインチューニングを可能にします。
 * [ruri-small-v2](https://huggingface.co/cl-nagoya/ruri-small-v2) - 📥 2k / ⭐ 4 / Ruri は、日本語汎用テキスト埋め込みモデル v3（30 M–310 M パラメータ、8192‑token 最大長）をリリースし、JMTEB でトップスコアを獲得しています。 sentence_transformers を簡単に使用できるように「クエリ:」または「文章:」でプレフィックスする方法を提供し、検索、STS、分類、再ランキング、クラスタリング、およびペア分類タスクのベンチマーク結果も掲載しています。
 * [ruri-large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2) - 📥 1k / ⭐ 10 / 日本語一般テキスト埋め込みリポジトリ Ruri は、30 M から 310 M パラメータまでの v3 モデルを提供し、JMTEB スコアを提示しています。sentence_transformers で（「クエリ: 」／「文章: 」接頭辞を使用）ロードする方法を示し、複数の日本語埋め込みモデルを比較したベンチマーク結果を提供します。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 1k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B は、1.2 B パラメータを持つ日本語テキスト埋め込みモデルで、Sarashina2.1‑1B をベースに構築され、多段階対照学習で訓練され、JMTEB で最先端のスコアを達成しつつ、非商用ライセンス下で意味的類似性、検索、分類のために1,792 次元の密ベクトルを生成します。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 1M / ⭐ 52 / Japanese wav2vec‑2 XLSR‑53 は Common Voice 6.1、CSS10、JSUT で微調整され、16 kHz オーディオを必要とし、HuggingSound または HuggingFace パイプラインで使用できます。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 32k / ⭐ 93 / Kotoba‑Whisper‑v2.2 は、HuggingFace‑Transformers パイプラインを通じて統合された話者分離と自動句読点機能を備えた kotoba‑whisper‑v2.0 を拡張した日本語 ASR モデルであり、Asahi Ushio と Kotoba Technologies と協力して構築されました。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 11k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh は、ReazonSpeech v2.0 Japanese ASR corpus でファインチューニングされた 96.7 M‑パラメータの wav2vec 2.0 Base モデルで、13.22 % の CER を達成し、Hugging Face transformers でデプロイ可能、Apache 2.0 ライセンスで公開されています。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 11k / ⭐ 18 / Kotoba‑Whisper‑Bilingual v1.0 は、日本語と英語の ASR 用に 6.3 倍速化された distilled Whisper モデルを提供し、さらに双方向音声からテキストへの翻訳機能を備えています。これらは、OpenAI の Whisper large‑v3 をベースに、knowledge distillation を用いて構築され、クロスエントロピーと KL‑divergence loss を利用しています。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 7k / ⭐ 35 / reazonspeech‑nemo‑v2は、619 Mパラメータの日本語長文ASRモデルで、改良版Fast‑Conformerと線形スケーラブル注意機構を採用し、ReazonSpeech v2.0コーパスで訓練されました。3000トークンSentencePieceを用いたsubword RNN‑Tデコーダにより、多時間推論を提供し、Apache 2.0で配布されています。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 6k / ⭐ 118 / Anime Whisperは、約5,300時間のanime‑style dialogueで微調整された軽量の日本語ASRモデルで、低 hallucination、リズムに合わせた句読点、非言語音声およびNSFW contentの正確な文字起こしを実現し、初期プロンプトなしで実行する必要があります。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 5k / ⭐ 45 / NVIDIA NeMo の 0.6 B‑parameter Hybrid FastConformer‑TDT‑CTC ASR model は、日本語音声を句読点付きで文字起こしし、NeMo フレームワーク内で推論またはファインチューニングに利用可能です。
 * [japanese-wav2vec2-large-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-large-rs35kh) - 📥 4k / ⭐ 3 / Japanese wav2vec 2.0 Large (319 Mパラメータ) を ReazonSpeech v2.0 でファインチューニングしたモデルは、Japanese ASR で平均 CER 16.25 % を達成し、他の wav2vec 2.0 ファミリーを上回っています。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 3k / ⭐ 86 / Kotoba‑Whisper v2.0 は、OpenAI Whisper large‑v3 から蒸留された日本語 ASR モデルで、7.2 million ReazonSpeech クリップで訓練され、ドメイン内テストで教師の CER/WER と同等の性能を維持しつつ 6.3 倍速で動作します。stable‑ts/punctuation のサポートと完全なトレーニングコードが GitHub にあります。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 2k / ⭐ 19 / Kotoba‑Whisper‑v2.1は、日本語のASRモデルであり、統合されたpunctuation‑postprocessing pipelinesを備えてkotoba‑whisper‑v2.0を拡張しています。これにより、同等のCER性能を保持しながら、シームレスでpunctuation‑aware transcriptionが可能になります。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 51k / ⭐ 51 / 日本語 Sentence‑BERT v2 は、cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking を MultipleNegativesRankingLoss でファインチューニングし、v1 に比べて約1.5〜2 % の精度向上を実現。sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 としてリリースされました。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 31k / ⭐ 11 / 文埋め込みを生成するJapanese Sentence‑BERT (v1) モデルで、改良版v2が利用可能で、Hugging Face Transformers とカスタム `SentenceBertJapanese` クラスを使用したサンプル使用例があります。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 29k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 は、ViT‑B/16 をベースにした Apache‑2.0 ライセンスの日本語 CLIP モデルで、CC12M のキャプションを日本語に翻訳して訓練され、2022 年 5 月 12 日にリリースされました。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 21k / ⭐ 21 / Sarashina‑Embedding‑v2‑1B は、1,792 次元の日本語文変換器であり、マルチステージ対照学習 (multi‑stage contrastive learning) によって訓練され、最先端の JMTEB スコアを達成しています。また、意味的類似度、検索、パラフレーズ・マイニング、分類、クラスタリングに利用でき、Sentence‑Transformers を通じてオプションの instruction prefixes 付きで使用可能です。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 19k / ⭐ 29 / LY Corporation の clip‑japanese‑base は、約 1 B の画像‑テキストペアで学習された日本語 CLIP モデルで、Eva02‑B トランスフォーマー画像エンコーダーと12層の BERT テキストエンコーダーを使用し、STAIR で R@1 0.30、Recruit で 0.89 の精度、ImageNet‑1K で 0.58 の精度を達成し、ゼロショット画像分類と検索をサポートしています。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 10k / ⭐ 2 / ja_ginza_electra は、mC4 と UD_Japanese_BCCWJ r2.8（megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator をベースにしたもの）でファインチューニングされた日本語 ELECTRA モデルを提供する spaCy v3 の Python パッケージです。カスタム bunsetu‑phrase 検出機能を備え、MIT ライセンスで配布されています。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 3k / ⭐ 14 / 日本語Sentence‑LUKEモデルは、Sentence‑BERTと同じデータセットで訓練され、同等にするかそれを上回る性能を有し、studio‑ousia/luke‑japanese‑base‑lite をベースに構築され、Hugging Face Transformers の MLukeTokenizer と LukeModel を介して使用される。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 3k / ⭐ 17 / Japanese CLIP モデル clip‑japanese‑base‑v2 は、約20億画像‑テキストペアと蒸留でアップグレードされ、Eva02‑B 画像エンコーダと12層 BERT テキストエンコーダをペアリングし、前モデルよりも高い ImageNet‑1k 精度（0.708）を達成します。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 2k / ⭐ 55 / 日本語対応の T5 モデルは、Wikipedia と OSCAR データ約100 GB を SentencePiece トークナイズで事前学習し、ニュース分類ベンチマークで Google’s multilingual T5 を上回るが、ファインチューニングが必要で、バイアスのある出力が生成される可能性がある。

### token-classification
 * [MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - 📥 152k / ⭐ 12 / 日本語医療文書 NER モデル（5 つのファイルをダウンロードし、**predict.py** を実行すると、病気、薬、日付などのタグが出力されます。）NAISTSOC 2022 NTCIR‑16 Real‑MedNLP タスクで使用された。
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 142k / ⭐ 4 / 日本語に特化した DeBERTa V3 は、Kudoトークナイゼーションでファインチューニングされ、推論時には形態素解析器を使用せず、効率的な埋め込みのために語彙を削減しています。また、Hugging Face のリリース（xsmall、base、large、large は BPE でトレーニング済み）が含まれます。
 * [MedNERN-CR-JA](https://huggingface.co/sociocom/MedNERN-CR-JA) - 📥 51k / ⭐ 4 / MedTxt‑CR‑JA 日本語医療データセットで学習された Hugging‑Face 互換 NER モデルで、エンティティ出力を正規化し、XMLタグ付きテキストを生成し、外部の `id_to_tags.pkl` を使用してラベルIDを実際のタグにマッピングする予測スクリプトが付属しています。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 10k / ⭐ 11 / cl‑tohoku/bert‑base‑japanese‑v2 を使用した日本語 NER は、`BertForTokenClassification` を介して 8 つのエンティティタイプ（企業、政治・その他組織、施設、製品、イベント）を抽出し、Stockmark Wikipedia データセットで学習済みです。CC BY‑SA 3.0 ライセンスの下で `transformers`、`unidic_lite`、`fugashi` でインストール可能です。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 6k / ⭐ 10 / Wikipediaデータセット上の固有表現認識用に微調整された日本語 BERT‑Base は、*Large Language Model Introduction* の第6章で紹介され、Hugging Face transformers パイプライン（Apache 2.0 ライセンス）でデプロイできるものです。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 日本語NERコーパス（タグ PER, ORG, LOC, INS, PRD, EVT）上で、5エポックのAdam（lr 5e‑5、バッチ12）を使用してFine‑tuneしたXLM‑RoBERTa‑baseは、0.0173の検証ロスを達成し、Transformers 4.23.1とPyTorch 1.12.1でリリースされました。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 241k / ⭐ 165 / Manga OCR は、縦書きと横書きの日本語漫画テキスト（フリガナを含む）を、さまざまなフォントと低品質画像でも読み取る Vision Encoder-Decoder OCR ツールで、ソースコードは無料で入手可能です。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 14k / ⭐ 3 / meikiocr は、ビデオゲーム向けに D‑FINE ベースのオープンウェイトテキスト検出モデル（v0.1、MobileNet‑v4 バックボーン、2種類の解像度バリアント、64 ボックス制限）と、実験的低遅延 tiny および small バリアント（日本のビデオゲームと漫画で訓練済み）を提供します。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 14k / ⭐ 4 / Meikiocrの `meiki.text.recognition.v0`――D‑FINEベースのMobileNetV4モデルで、日本語ビデオゲームテキストに特化して微調整されたもので――は、960×32入力から最大48文字まで検出し、それぞれの文字をバウンディングボックスと信頼度スコアとともに出力することで、水平テキストに対して最先端の精度と遅延を実現します。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 2k / ⭐ 14 / Sarashina2.2‑Vision‑3B は、Sarashina2.2‑3B‑Instruct と SigLIP 画像エンコーダーをベースに構築された 3 B パラメータを持つ日本語大規模ビジョン‑ラングエージングモデルであり、日本語 VQA ベンチマークで高い性能を達成しています。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 1k / ⭐ 2 / Manga OCRは、さまざまなフォントと低品質画像に対して縦書き・横書きテキストとふりがなオーバーレイを含む日本漫画の高品質なOCRを提供するVision Encoder‑Decoder systemです。また、一般的な印刷された日本語OCRにも使用できます。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 188k / ⭐ 10 / 新しい VNTL データセットに基づく LLaMA 3 Youko qlora ファインチューニング。日本のビジュアルノベルを英語へ正確かつ文字通りに翻訳することに最適化されており、チャットモードは使用せず、デフォルトの LLaMA 3 プロンプトを使用し、ニュートラルサンプリング（温度 0、繰り返しペナルティ無し）を推奨する。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 45k / ⭐ 28 / Fine‑tuned, GGUF‑quantized LFM2‑350M checkpoint は、短〜中長テキストに対するほぼリアルタイムの bi‑directional Japanese‑English 翻訳に使用でき、llama.cpp で利用可能です。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 41k / ⭐ 68 / OpusコーパスからのJapanese‑to‑English Transformer‑Align MT modelは、正規化とSentencePiece前処理を使用して、Tatoebaテストセットで41.7 BLEUと0.589 chr‑Fを達成します。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 7k / ⭐ 115 / PLaMo Translation Model は Preferred Networks が開発した翻訳タスク向けの大規模言語モデルで、ベース、ポストトレーニング、評価バリアントが用意されています。PLaMo community license の下で公開され、チャットやその他のダウンストリーム用途向けにインストラクションチューンは行われていません。
 * [opus-tatoeba-en-ja](https://huggingface.co/Helsinki-NLP/opus-tatoeba-en-ja) - 📥 4k / ⭐ 14 / 15.2 BLEUを持つ英語‑日本語の transformer‑align MTモデルは、opus+bt‑2021‑04‑10 をベースに正規化 + SentencePiece を使用して構築され、Tatoeba Challenge にてホストされています。

### text-ranking
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 39k / ⭐ 7 / Japanese CrossEncoderリランカーモデルは、xsmall から large（BGE を含む）まであり、JQaRA、JaCWIR、MIRACL、JSQuAD で評価済み。sentence_transformers と HuggingFace 用の、すぐに利用可能な統合例も用意されています。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 11k / ⭐ 13 / Ruri‑v3 Reranker は、ModernBERT‑Ja をベースにした堅牢な日本語テキストリランカーで、最大 8,192 トークンのシーケンス、100k トークンの語彙、FlashAttention および SentencePiece tokenizer をサポートし、sentence‑transformers 経由で使用できます。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 7k / ⭐ 6 / 高速で軽量な日本語 Reranker v2 モデル（tiny、xsmall、small、base）は、ベンチマークスコアと GPU スピードを備え、sentence_transformers CrossEncoder と transformers ≥ v4.48 で使用でき、flash‑attn で高速化も可能です。また、CPU/ARM 用に ONNX/quantized フォーマットでも利用可能です。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 3k / ⭐ 4 / 日本語でトレーニングされた CrossEncoder リランクラーは xsmall (384) から large (1024) まであり、さらに BGE‑v2‑m3‑v1 モデルも含まれます。ファインチューニング、推論、JQaRA、JaCWIR、MIRACL、JSQuAD のベンチマークスコアの例コードが付属しています。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 1k / ⭐ 16 / 日本語向け CrossEncoder リランカー モデル（xsmall から large まで）は、日本語テキストで学習され、sentence_transformers を通じて公開され、JQaRA、JaCWIR、MIRACL、JSQuAD で評価されます。

### text-classification
 * [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) - 📥 993k / ⭐ 3 / Finance Sentiment JA (base) は、翻訳された Financial PhraseBank で訓練された BERT‑ベースの日本語感情モデルで、金融ニュースを positive、negative、neutral に分類し、macro f1 0.959、accuracy 0.967、134.9 samples per second で動作します。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 11k / ⭐ 15 / 日本語感情分析モデルは、chABSAデータセットで学習され、損失0.0001、精度1.0、F1スコア1.0を達成しました。Transformers 4.24.0およびPyTorch 1.12.1+cu113で構築され、Adam（学習率2e‑05、10エポック、バッチサイズ16）で最適化され、`model(**inputs)`で評価されました。
 * [luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 📥 8k / ⭐ 43 / 日本語のLUKEモデルで、WRIMEデータセットで微調整され、文章内で表現されている8つの感情（喜び、悲しみ、期待、驚き、怒り、恐怖、嫌悪、信頼）のうちどれかを分類する。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 4k / ⭐ 2 / 「Large Language Model Introduction」の第5章で紹介された、日本語 BERT‑based モデル。JGLUE JSTS データセットで意味的類似度スコアリングのためにファインチューニングされ、Colab ノートブック、transformers‑pipeline の使用方法、Apache 2.0 ライセンス付き。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 2k / ⭐ 119 / PaddleOCR‑VL からファインチューニングされた PaddleOCR‑VL‑For‑Manga は、Manga109 の吹き出し切り抜きで 70 % の全文正確性を達成し、27 % のベースラインを 3 倍以上上回ります。多言語データセットを使用し、トレーニングコードと開発者ガイドが含まれます。
 * [llm-jp-3-vila-14b](https://huggingface.co/llm-jp/llm-jp-3-vila-14b) - 📥 1k / ⭐ 11 / LLM‑jp VILA 14B は、国立情報学研究所（日本）が開発した 14‑B‑パラメータの vision‑language モデルで、Python 3.10.12 用にクローン―インストール―ランのワークフローを通じて必要なライブラリ（flash‑attention を含む）をインストールし、画像入力とテキストクエリを受け付けるように設計されています。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 3k / ⭐ 13 / Anime‑XCodec2‑44.1kHz‑v2は、16 kHzの日本語音声を44.1 kHzの高音質オーディオにアップサンプリングし、デコーダー専用RMS‑lossファインチューニングを行い、encoder/codebookをフリーズしたまま、同一の音声トークンを保持します。

### text-to-speech
 * [Anime-Llasa-3B](https://huggingface.co/NandemoGHS/Anime-Llasa-3B) - 📥 2k / ⭐ 26 / Anime‑Llasa‑3B は、HKUSTAudio/Llasa‑3B に基づく日本語 TTS モデルで、より多くのトレーニングデータで表現力と安定性を向上させ、CC‑BY‑NC‑4.0 のライセンスが適用されています。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 101k / ⭐ 10 / Japanese‑language BERT‑Base (12 layers, 768‑dim, 12 heads)は、Unidic‑based word‑level plus character‑level tokenizationとwhole‑word maskingをCC‑100と2023 Wikipediaで事前学習し、7,027‑token vocabularyを生成する。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 67k / ⭐ 14 / Japanese‑BERT‑Large は CC‑100 と Wikipedia に対して訓練され、Unidic‑lite のワードレベルトークナイゼーションを使用し、WordPiece サブワードとホールワードマスクリングを採用しています（24 層、隠れ層 1024 次元、16 ヘッド、32k 語彙）。プリトレーニングコードは cl‑tohoku/bert‑japanese にあります。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 40k / ⭐ 59 / Japanese BERT‑base（12層、768次元の隠れ層、12ヘッド、32k語彙）は、CC‑100と2023‑Jan Wikipediaで全単語マスキングを用いて事前学習され、Unidic 2.1.2の単語レベルトークナイゼーション＋WordPieceを併用し、200万ステップで学習しました。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / ≈100 GB の Wikipedia と OSCAR CC‑100 データ（SentencePiece で 10:1 の混合、byte‑fallback を有する）で事前学習された日本語 T5‑v1.1 モデルで、下流タスクの微調整が必要です。転移学習サンプルコードが含まれ、出力に潜在的なバイアスを示唆しています。ライセンスは CC‑BY‑SA 4.0 です。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 6k / ⭐ 17 / Japanese DeBERTa V3 base は、LLM‑jp v1.0 から 540 B トークンで事前学習され、修正された DeBERTa V3 セットアップで訓練され、形態素解析器を使用しないユニグラム・バイトフォールバックトークナイザーを使用し、JGLUE NLUタスク用に微調整済みです。
 * [tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf](https://huggingface.co/mmnga/tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf) - 📥 3k / ⭐ 4 / Repository は、tokyotech‑llm の Llama‑3.1‑Swallow‑8B‑Instruct‑v0.3 モデルの gguf-format 変換をホストしており、imatrix データセットで構築され、llama.cpp で実行可能です。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 3k / ⭐ 17 / 高性能日本語 SPLADE v2 は、WebUI demo を通じてスパース‑ベクトル変換と推論を可能にし、YAST でトレーニングを行い、YASEM 埋め込みを提供し、JMTEB ベンチマーク結果を報告します。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 3k / ⭐ 9 / Llama 3.1 Swallow v0.5 は、8 billion パラメータを持つ LLM で、Meta の Llama 3.1 を日本語とコード／数式推論で改善しつつ英語の流暢さを保持し、継続的なプリトレーニングと指示調整ファインチューニングを合成日本語データで実現したものです。
 * [llama-3-youko-8b-instruct-i1-GGUF](https://huggingface.co/mradermacher/llama-3-youko-8b-instruct-i1-GGUF) - 📥 3k / ⭐ 1 / GGUF 量子化された rinna/llama‑3‑youko‑8b‑instruct のコレクションで、サイズ/品質のトレードオフをリストし、使用ガイダンス、比較グラフ、および FAQ/model-request link を付添する。
 * [tokyotech-llm-Llama-3.1-Swallow-70B-Instruct-v0.3-gguf](https://huggingface.co/mmnga/tokyotech-llm-Llama-3.1-Swallow-70B-Instruct-v0.3-gguf) - 📥 3k / ⭐ 2 / TokyoTech-LLMのLlama-3.1-Swallow-70B-Instruct-v0.3モデルをgguf形式にしたバリアントで、TFMC/imatrix-dataset-for-japanese-LLMから構築され、CUDA上でllama.cppを通じて実行するための使用手順が含まれています。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 71 / Llama‑3‑ELYZA‑JP‑8B は、日本語向けに強化された 8‑B Llama 3 モデルで、GGUF（Q4_K_M）と AWQ 量子化を備え、llama.cpp、LM Studio、または OpenAI‑compatible API で実行できます。
 * [Qwen2.5-7B-ja-struct-tooled-base-i1-GGUF](https://huggingface.co/mradermacher/Qwen2.5-7B-ja-struct-tooled-base-i1-GGUF) - 📥 2k / ⭐ 1 / Weighted/imatrix GGUF quantizations of the Qwen2.5‑7B‑ja‑struct‑tooled‑base model are provided, with static quants hosted on Hugging Face, a table of file names, sizes, and quality notes ranging from low‑quality i1‑IQ2_XXS to high‑quality i1‑IQ4_K_M, and usage guidance via TheBloke READMEs for concatenating multi‑part files.
 * [gemma-3-12b-it-qat-japanese-imatrix](https://huggingface.co/dahara1/gemma-3-12b-it-qat-japanese-imatrix) - 📥 2k / ⭐ 6 / Google Gemma 3‑12bの日本語重視のimatrix‑quantized版で、llama.cpp用に準備済み。llama‑mtmd‑cli/mmproj.ggufで画像読み込みが可能で、Hugging Faceにホストされています。
 * [pfnet-nekomata-14b-pfn-qfin-gguf](https://huggingface.co/mmnga/pfnet-nekomata-14b-pfn-qfin-gguf) - 📥 2k / ⭐ 1 / GGUF‑converted pfnet nekomata‑14b‑pfn‑qfin、TFMC/imatrix 日本語LLM データセットから構築され、Tongyi‑Qianwen ライセンスの下でリリースされました。
 * [shisa-v2.1-qwen3-8b-UD-japanese-imatrix](https://huggingface.co/dahara1/shisa-v2.1-qwen3-8b-UD-japanese-imatrix) - 📥 2k / ⭐ 3 / Unsloth Dynamic 2.0で構築されたGGUF‑quantized shisa‑v2.1‑qwen3‑8bモデルは、コミュニティパッチ適用済みのQwen3設定で不具合を減らし、より大きなimatrixを備えて日本語性能を強化し、最大コンテキスト長40Kを備えています。
 * [Qwen3-30B-A3B-gguf](https://huggingface.co/mmnga/Qwen3-30B-A3B-gguf) - 📥 2k / ⭐ 3 / GGUF‐formatted Qwen3‑30B‑A3B は TFMC/imatrix‑dataset‑for‑Japanese‑LLM から変換され、CUDA‑enabled llama.cpp で実行可能です。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 20 / pfnet の plamo‑2‑translate を imatrix データから構築し、TFMC/imatrix‑dataset‑for‑japanese‑LLM に基づく GGUF‑format リリースで、CUDA 対応ハードウェア上で llama.cpp を通じてコンパイル・実行する手順を含む。
 * [DataPilot-ArrowPro-7B-KUJIRA-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-KUJIRA-gguf) - 📥 1k / ⭐ 10 / DataPilot の ArrowPro‑7B‑KUJIRA モデルの gguf フォーマット変換、TFMC の imatrix Japanese LLM データセットで構築され、llama.cpp で実行される。
 * [cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf](https://huggingface.co/mmnga/cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf) - 📥 1k / ⭐ 55 / Cyberagent の gguf‑converted DeepSeek‑R1‑Distill‑Qwen‑14B‑Japanese モデル（TFMC imatrix dataset から構築）は mmnga の下で利用可能で、CUDA サポートを使用して llama.cpp で実行できます。
 * [ELYZA-Diffusion-Instruct-1.0-Dream-7B-gguf](https://huggingface.co/mmnga-o/ELYZA-Diffusion-Instruct-1.0-Dream-7B-gguf) - 📥 1k / ⭐ 1 / elyza の ELYZA‑Diffusion‑Instruct‑1.0‑Dream‑7B を gguf‑フォーマットへ変換し、CUDA サポート付きで llama.cpp で構築・実行し、カスタム diffusion パラメーターを使用しています。
 * [ELYZA-Shortcut-1.0-Qwen-7B-gguf](https://huggingface.co/mmnga/ELYZA-Shortcut-1.0-Qwen-7B-gguf) - 📥 1k / ⭐ 3 / TFMC/imatrix‑dataset‑for‑japanese‑LLM データで構築された ELYZA‑Shortcut‑1.0‑Qwen‑7B モデルの gguf‑format conversion で、CUDA でコンパイルされた llama.cpp で実行可能な状態です。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 2M / ⭐ 21 / 2009年から2024年までのNicoNico Liveのコメントログ（150GB超）を集約し、転換前・転換後・リアルタイムNX‑Jikkyoのキャプチャも含む、歴史的なTV‑broadcastディスカッションを簡単に取得できるAPIを提供します。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 5k / ⭐ 13 / 日本語および多言語のQA、NLI、パラフレーズデータセットのカタログで、各データセットの検索またはQAタスクとライセンス（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）を詳細に記載。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 5k / ⭐ 33 / Japanese‑Eroge‑Voice‑V2は、匿名化された1,033,142件のエロゲ音声–文字起こしペア（主に女性、NSFW）を2,657時間提供し、学術研究向けにMITライセンスで配布します。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 3k / ⭐ 100 / Nemotron‑Personas‑Japan は、CC BY 4.0 のオープンソースデータセットであり、高品質の合成生成された日本人ペルソナ（名前、性別、年齢、背景、婚姻状況、学歴、職業、所在地を含む）で、実際の人口統計・地理・人格分布に基づいており、確率的グラフィカルモデルと GPT‑OSS‑120B を用いて多様性を高め、バイアスを減らし、モデル崩壊を防ぎ、主権 AI の開発を支援し、商業利用をサポートするよう設計されています。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 3k / ⭐ 8 / Cauldron‑JAは、DeepL APIを使ってThe Cauldronから翻訳された44個のサブデータセットからなる日本語ビジョン‑ランゲージデータセットです。HuggingFace’s datasets library を通じて入手可能で、オリジナルセットと同一のライセンスで提供され、プロンプトはCC‑BY‑4.0でリリースされています。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 3k / ⭐ 99 / 注釈付きタスク（要約訂正、数学推論、翻訳、創造的生成、ユーザー意図理解など）を網羅した100サンプルの日本語インストラクション・チューニング評価データセット。微調整モデルを手動または自動で5点評価できるよう設計されている。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 3k / ⭐ 10 / 🤗 上の Reazon Speech v2 データセットのミラー。CDLA‑Sharing‑1.0 ライセンスで提供され、日本の著作権法第30‑4条に制限される。16 kHz FLAC オーディオと付随するメタデータを含む。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 2k / ⭐ 16 / Reazon Speech v2 dataset のミラー: Stardust‑minus によって 10 日間にわたり 8 枚の A800 GPU で UVR を使用して処理された 3,674 本のノイズ除去された音声ファイル、CDLA‑Sharing‑1.0 でリリースされ、トランスクリプトなし。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 2k / ⭐ 24 / FineWeb2 Edu Japanese は FineWeb2 からの約1億2000万の高品質教育用日本語テキスト（約893億トークン）を提供し、DeepSeek‑API クラスフィケーター（スコア ≥ 2.5）でフィルタリングし、ModernBERT‑Ja‑130M でトークナイズされ、512 トークン以下の小規模サブセットを含みます。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 2k / ⭐ 19 / JMMMUは、日本語のマルチモーダルベンチマークで、ネイティブ専門家が翻訳した1,320の文化的に多様な質問（720は文化に依存しない、600は文化固有）に拡張され、現在は公開リーダーボードを備えています。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 1k / ⭐ 47 / 日本語 NLP ベンチマーク（Yahoo Japan と早稲田大学が作成）に対する JGLUE データセットカードとロードスクリプトを更新しました。テキスト分類（MARC‑ja、JCoLA）、文対分類（JNLI）、QA（JSQuAD、JCommonsenseQA）をカバーし、リリースは GitHub と Hugging Face にリンクされています。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 1k / ⭐ 8 / Rakuda は 40 件の日本語質問—歴史・社会・政府に関する自由回答形式と地理に特化した質問—を提供し、日本語 AI アシスタントのベンチマークに使用でき、vicuna‑eval と比較可能で、`datasets.load_dataset` で読み込むことができます。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 1k / ⭐ 130 / Japanese Anime Speech Dataset V2は、292,637件の整理済みオーディオ‑テキストペア（約397.5時間のSFW、および52.4時間のNSFWコンテンツ）を、セーフティ別に分割された128‑kbps MP3ファイルとして提供し、特に自動音声認識モデルのトレーニング用に設計されています。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 1k / ⭐ 18 / JMTEBは日本語テキスト埋め込みベンチマークで、5つのタスク（クラスタリング、分類、STS、検索、リランキング）と28のデータセットを特徴とし、1行で評価できるスクリプトを提供し、コミュニティの貢献を歓迎する。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 1k / ⭐ 31 / Galgame VisualNovelデータセット (OOPPEENN/566973746F6F6372656164656C65746572) の再構成された再アップロード。Hugging Face datasets の効率的な読み込みのため、すべてのオリジナル音声/テキストを保持し、複数のゲームサブセットオプションを備えた抽出スクリプトを提供します。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 4 / JamC‑QA は、8つの日本文化・知識カテゴリにわたる多肢選択問題のバイリンガルベンチマークで、リーダーボードメトリクスで最先端モデルを比較します。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 1k / ⭐ 10 / JDocQAは、日本語PDFベースのQAデータセットで、5,504件のドキュメントと11,600件の質問回答ペアを含み、視覚情報とテキスト情報の両方を用いて、はい／いいえ、事実・数値・オープンエンド・不可回答の理解をテストする。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 1k / ⭐ 7 / JMedBenchは日本語医療・生物医学用LLMベンチマークであり、20のデータセットをMCQA、NER、STSなどを含む5つのタスクにまたがって構成しています。データセットはMedMCQA、PubMedQA、MMLUなどから取得されており、それぞれに独自のライセンスが付属しています。また、翻訳にバイアスが含まれる可能性があるため、人間によるレビューが必要であるという注意事項が記載されています。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 1k / ⭐ 108 / ReazonSpeech は、FLAC エンコードされた日本語音声コーパスで、文字起こし付きです。8.5 h から 35,000 h までの 5 つのサイズで提供され、Hugging Face 経由で CDLA‑Sharing‑1.0 ライセンスの下でダウンロードでき、日本著作権法第 30‑4 条の規定により使用が制限されています。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 895 / ⭐ 6 / VOICEVOXで作成された人工音声データセットで、ITA、Tsukuyomi‑chan、ROHANコーパスから構成され、445,793個のWAVファイルを含み、総再生時間が577時間51分23秒です。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 766 / ⭐ 32 / 409時間の日本語エロゲ音声データセットで、2パス loudnorm（‑23 LUFS、‑1 dB peak、11 LRA）で処理され、litagin/anime-whisper により文字起こしされ、匿名化され、WebDataset（FLAC、JSON、TXT）として保存されています。主に女性の声が収録されており、AI文字起こしのエラーが存在する可能性があります。MIT‑licensed for academic research.
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 715 / ⭐ 87 / databricks‑dolly‑15k データセットの自動翻訳された日本語版、CC‑BY‑SA‑3.0 ライセンス、2023‑05‑11に最終更新。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 684 / ⭐ 6 / 日本語のMC4データセット (mc4-ja) のデータセットカード
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 674 / ⭐ 147 / Japanese Anime Speech Dataset は、73,004 の音声‑テキストペア（合計110時間、V1 から V5 へと進化）を提供し、OpenAI’s Whisper などの ASR モデルを強化します。すべての利用に対してオープンライセンスが適用され、クレジットの表記があれば感謝します。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 667 / ⭐ 6 / Japanese XL‑Sum subset は PaLM‑2 15‑gram overlap を通じてフィルタリングされ、4,215件のトレーニング例、758件の検証例、766件のテスト例を含みます。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 591 / ⭐ 10 / EDINET‑Bench は、10 年分の EDINET‑API 公開レポートを使用して、会計不正検出、収益予測、業界予測などのタスクで LLM を評価する日本の金融ベンチマークです。構築・評価コードが提供され、データセットは PDL 1.0 に再ライセンスされています。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 585 / ⭐ 38 / Aozora Bunkoから取得したパブリックドメイン日本語テキストのユーザーフレンドリーで重複除去済みCSVデータセット。globis-org/aozorabunko‑extractorで処理され、現代日本語機械学習用途に合わせてクリーニング済み。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 554 / ⭐ 5 / 日本語データセットをSentenceTransformers対応のカラムに変換し、複数のHuggingFaceソースから取得したRerankスコア（≥0.7 を正例、≤0.3 を負例）で例をフィルタリングし、オリジナルのライセンスを尊重しつつ対照学習をサポートしました。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 524 / ⭐ 5 / JAQKET は、Wikipedia から派生した日本語のオープンドメイン QA データセットであり、複数選択式のクイズ質問を含むバージョン 1.0（13,061 件の学習データ、271 件の検証データ）と、質問プロンプトのみで抽出された回答を要求するバージョン 2.0（2,154 件の学習データ、1,164 件の検証データ）を提供し、QA システムの研究を促進するように設計されています。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 466 / ⭐ 2 / 匿名の 2ch.sc/2ch.net スレッドの大規模圧縮 JSON‑Lines データセット。スレッド ID、タイトル、掲示板と地域情報、返信数、完全な投稿メタデータ（投稿者、メール、日付、本文）を含む。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 464 / ⭐ 4 / 日本語の検索/QAデータセットを提供し、5つの多言語/日本語リランカー（例：BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）によって算出されたクエリごとのスコアを含む。各クエリごとに約200件の正例と負例ドキュメントの平均スコアも含まれる。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 459 / ⭐ 13 / 104 GBのデータセットで、3,746,131のGalgameオーディオファイル（5,353 時間）を含み、既存の16 kHz ASRセットにLLM生成の感情ラベル（不正確である可能性あり）を追加。GPL v3.0でリリースされ、商業利用は禁止され、訓練済みモデルはすべてオープンソースである必要があります。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 433 / ⭐ 142 / 日本語インストラクション・チャットデータセット（LLMのファインチューニング用（例：LoRA）、9 M+サンプル）。最近更新され、ライセンス付きAlpacaデータを除外し、クリーンなWikipediaとALT出力を含め、CC‑BY‑SA 4.0でリリース。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 431 / ⭐ 11 / JMMLUは、56科目に跨る7,536問の教師作成質問を収録した、日本語のマルチタスク言語理解ベンチマークです。含まれる科目は、専門医学・心理学・会計学・哲学、及び多様な高校科目です。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 370 / ⭐ 23 / cc100-jaは、cc100データセットの日本語部分を集めたもので、シャーディングされたParquetファイルとして提供されています。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 359 / ⭐ 33 / Allganize RAG Leaderboard は、財務・通信・製造・公共部門・小売りという5つの業界分野にわたる日本語 RAG パフォーマンスデータと自動化されたエンドツーエンド評価結果を公開し、包括的な日本語ベンチマークがまだ存在しない状況で、パーサー・リトリーバル・生成コンポーネントのベンチマーク作成を企業が支援できるようにしています。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 359 / ⭐ 2 / 日本語ウィキペディアテキストのパラフレーズから生成されたLLM生成クエリと回答のデータセット。ライセンス制限付きモデルを使用せずに構築され、CC‑BY‑SA 4.0で公開されています。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 339 / ⭐ 13 / 「wikipedia-ja-20230720」日本語ウィキペディアスナップショットのデータセットカード。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 333 / ⭐ 15 / 日本語の仮名から漢字への変換のための1億9千万ペアのJSONLデータセットで、zenz‑v2.5 medium、small、xsmall モデルを支え、AJIMEE‑Bench 評価コーパスを含む。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 306 / ⭐ 11 / JaQuADは2022年作成の日本語QAデータセットで、Wikipediaから抽出した39,696ペアのSQuAD‑style抽出クエリで構成され、総サイズは73.2 MBです。BERT‑Japaneseでファインチューニングすると78.92 % F1（63.38 % EM）を達成します。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 303 / ⭐ 17 / JA‑VG‑VQA‑500 は、日本語 Visual Genome VQA データセットの 500 サンプルのサブセットで、CC BY 4.0 ライセンスが付与され、EvoVLM‑JP‑v1‑7B のベンチマークに使用されます。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 301 / ⭐ 3 / Japanese Guardrail モデル評価データセット（1,725サンプル）で、WildGuardTest の高品質なマルチステージ翻訳で、ODC-BY ライセンスで公開され、Hugging Face で入手可能です。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 286 / ⭐ 3 / 日本語版のExplainable Multi-hop Question Answering dataset は、質問、回答、Wikipedia記事を結びつけるステップバイステップの導出を特徴とし、導出フォーマットが更新され、複数のバージョンがリリースされています。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 284 / ⭐ 3 / BBH‑jaはBIG‑Bench Hardデータセットの日本語訳を提供し、JSON‑L（入力・正解ターゲット）とYAML（入力・ターゲット）のChain‑of‑Thoughtプロンプトを含む評価問題を提供し、PLaMoモデルで翻訳しています。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 280 / ⭐ 19 / Retrieval‑Augmented Generation (RAG) を評価するための日本語 QA データセットで、JAQKET 質問と Wikipedia パッセージから構築され、金ラベル付きの検索関連性ラベルを持つ。HuggingFace と GitHub でリリースされ、主に nDCG@10 で評価される。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 275 / ⭐ 10 / 日本語から英語への並列コーパスで、kakenサブセットの llm‑jp‑corpus‑v3 を Qwen/Qwen2.5‑32B‑Instruct で翻訳し、独自の翻訳列を備え、CC‑BY‑4.0 の下でライセンスされています。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 270 / ⭐ 31 / Syosetu711Kは、2023年3月26日〜27日に小説家になろうからスクレイピングされた約711,700本の小説で構成される日本語データセットです。全テキストとメタデータ（タイトル、著者、NCode、あらすじ等）を提供し、教師なしテキスト生成および分類タスクに利用されます。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 270 / ⭐ 10 / 検証済みのchain‑of‑thought 推論を備えた高品質な合成日本語数学問題データセット。PRM800K と GSM8K を Qwen2‑7B‑Instruct で翻訳し、正確性をフィルタリングして作成。Hugging Face datasets ライブラリ経由で利用可能。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 269 / ⭐ 3 / クリーンされた日本語ウェブコーパス（mc4‑ja など）は、教師なし学習で約10 k 文書にクラスター化され、一部のファイルのみが Parquet 形式です。ファイルリストは out フォルダーにあり、法的に許可された情報分析用途のために Git LFS でダウンロードできます。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 263 / ⭐ 21 / 日本語ウェブコレクションの56百万件の文書、110 B文字、249百万枚の画像は、大規模なビジョン-言語モデルのトレーニングに使用されます。momiji_generatorによるデータポピュレーション、OBELICS‑style visualization、サンプルモデル（Heron‑NVILA‑Lite）を提供します。
 * [jhle](https://huggingface.co/datasets/llm-jp/jhle) - 📥 260 / ⭐ 96 / LLM‑jp によってキュレーションされた日本語訳の “Humanity’s Last Exam” データセット。画像質問は省略され、raw_subject ごとに5件をサンプリングし、機械翻訳・専門家レビュー済みです。著者は Yuji Tamakoshi、Kouta Nakayama、Yusuke Miyao で、トレーニングコーパスとして決して使用してはならない。
 * [wiki40b_ja](https://huggingface.co/datasets/fujiki/wiki40b_ja) - 📥 249 / ⭐ 4 / Mandy Guo、Zihang Dai、Denny Vrandečić によってコンパイルされた Wiki40B データセットの書式変更済み日本語サブセット
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 249 / ⭐ 15 / 『Large Language Model Introduction』で使われるJGLUE datasetのデータセットカード。元のリポジトリ (original repo) から取得し、コードはCC BY‑SA 4.0でライセンス、データは配布者のライセンスに基づく。Kurihara & Kawahara（日本語）を引用し、Shunsuke Kitada’s repository をベースに構築。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 249 / ⭐ 7 / JHumanEval は HumanEval benchmark の手翻訳版で、164 の Python programming problems を提供し、並行した英語と日本語のコメント付きで、日本語‑LLM のコード生成を評価しつつ、元の英語のエラーを保持します。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 248 / ⭐ 6 / Range3のwikipedia‑ja‑20230101リポジトリは、完全なWikipediaデータセットから抽出され、Pythonコードで生成された日本語Wikipediaテキストのみを含むParquetファイルを提供しています。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 236 / ⭐ 24 / AutoWikiQAは、日本最大の無料QAデータセット（2 ,377 ,503ペア）で、Swallow‑MXとvLLMを使用してWikipediaテキストから生成され、知識注入と検索補強生成のために多様でテンプレートフリーな質問と回答を提供します。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 232 / ⭐ 9 / llm‑book/wrime‑sentiment のデータセットカードは、WRIME から派生した二項式日本語感情分析セットを提供し、Avg. Readers_Sentiment に基づいて「positive」または「negative」とラベル付けされます（中立ケースを含めるオプション付き）。このセットは、“Introduction to Large Language Models” のサンプルデータとして意図されています。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 228 / ⭐ 41 / Galgame_Speech_ASR_16kHz は 16 kHz の ASR データセットで、3.75 百万ペア（≈5,354 時間）が含まれ、Galgame_Dataset から派生しており、GPL v3.0 の下で公開され、商用利用は禁止され、訓練済みモデルはオープンソースであることが求められます（引用は任意）。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 221 / ⭐ 40 / VNTL リーダーボードは、256件のサンプルにわたるコサイン類似度スコアの平均を算出し、日本語のビジュアルノベルを英語に翻訳する際に大規模言語モデルを評価し、予備結果をランキング化し、Sugoi Translator、Google Translate、Naver Papago などのツールとベンチマークします。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 218 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) は、Integration、Reasoning、Logical、Table、Abstention を網羅したマルチカテゴリ QA dataset を提供し、日本語 RAG ジェネレーターの評価を目的としています。このデータセットは人手と GPT‑4.1 によって構築され、CC BY‑SA 4.0 の下でリリースされています。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 215 / ⭐ 3 / 日本語版Wikipediaの文はさまざまな埋め込みとFAISSインデックスに変換され、Hugging Face Spaceデモ、変換スクリプト、検索・Q&A・OpenAI text‑embedding‑3‑smallを用いたRAGの評価が提供されます。埋め込みはOpenAIライセンス対象で、その他はCC‑BY‑SA‑4.0です。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 214 / ⭐ 4 / Loonwit が提供した livedoor news corpus を対象とした Dataset Card。『Introduction to Large Language Models』で使用され、Creative Commons ライセンス（CC BY‑ND 2.1 JP）付きのニュース記事を含み、HTML タグが除去されています。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 212 / ⭐ 2 / WAONは、ビジョン‑ランゲージモデル向けの大規模で高品質な日本語画像―テキストペアデータセットです。サイズとSigLIP‑scoreフィルタリングとURL、キャプション、パーセプチュアルハッシュ上での重複排除によって構築され、Apache 2.0のライセンスの下で提供され、日本法に基づく情報分析用途に限定されます。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 210 / ⭐ 26 / 失敗フラグ付きの日本語翻訳済み OpenAssistant/oasst1 データ、約2,000件の手動で修正されたコード翻訳エラー、リリース済みのチャットフォーマットサブセット (oasst1‑chat‑44k‑ja)、およびファインチューニング用にエントリをインストラクション–アウトプットペアに変換するスクリプト。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 209 / ⭐ 32 / izumi‑lab/llm‑japanese‑dataset から英語翻訳データを除去した日本語チャットボットデータセットで、2.5 million+ のエントリ（v1.0.0）を提供し、CC‑BY‑SA 4.0 の下で指示‑応答タスク向けに日本語 LLM をファインチューニングするために利用できます。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 203 / ⭐ 2 / 日本語 Callhome 音声ファイルを WAV に変換し、JSON 形式のメタデータ配列と RTMM 話者ラベルファイルを評価用に付随させる。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 195 / ⭐ 49 / AnswerCarefully Datasetは、商業利用または非商業利用のLLM安全向上のために日本語および多言語データを提供し、他の使用（安全迂回を含む）を禁止し、帰属を伴う派生作品を許可し、害やサービス変更に対する非責任の創作者免責事項を付帯しています。
 * [relaion2B-en-research-safe-japanese-translation](https://huggingface.co/datasets/llm-jp/relaion2B-en-research-safe-japanese-translation) - 📥 194 / ⭐ 4 / text2dataset、Gemma-2-9b-it、vLLMを使用して構築された高速な英語→日本語翻訳パイプラインで、concise, open-weight LLM promptを介して大規模なrelaion2B-en-research-safeコーパスを変換します。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 187 / ⭐ 11 / Range3/wiki40b‑ja は、日本語サブセットの wiki40b データセットをホストし、Python データ処理パイプラインで生成された 3 つの Parquet ファイルとして提供します。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 181 / ⭐ 4 / Fate/Stay Nightのキャラクター「Emilia」の対話とロアのデータセットで、会話型言語モデルのトレーニングと評価のためにフォーマットされています。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 172 / ⭐ 3 / 『Introduction to Large‑Scale LLM II』で使用され、llm‑jp‑eval によって作成されたクロスデータセットの日本語LLM評価用のja‑vicuna‑qa‑benchmarkのデータセットカード（Apache 2.0）。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 172 / ⭐ 5 / STAIR‑Captionsは2017年にリリースされ、キャプション生成、マルチモーダル検索、画像生成に利用できる820,310の日本語キャプションを提供します。詳細なアノテーション、メタデータ、Creative Commons BY‑4.0 ライセンス付きです。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 167 / ⭐ 2 / 64,139件の日本人名を生物学的性別でラベル付けしたデータセット―漢字、ひらがな、ローマ字で表記―は、トレーニング44.9k、検証6.41k、テスト12.8kに分割され、ISDA'23で採択されました。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 162 / ⭐ 21 / AI生成されたアニメイラストには英語のプロンプトとPhi‑3 Vision由来のキャプション（英語と日本語）が付いており、パブリックドメインで無料利用が可能です。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 158 / ⭐ 9 / JSICKはSICKから翻訳された日本語NLI/STSデータセットで、語順と格助詞の取り扱いを検証するストレステストを提供し、複数の変換された文対サブセットを通じて多言語合成推論の研究を支援します。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 158 / ⭐ 14 / Zundamonキャラクター設定のシンプルなデータセット—オンラインソースおよび管理データから編纂された—は、character‑LLMsのテスト用に、指定されたライセンスの下でzmnjp.jsonlおよびzmn.jsonl形式で提供されます。
 * [cc100-ja-documents](https://huggingface.co/datasets/hotchpotch/cc100-ja-documents) - 📥 157 / ⭐ 3 / 行単位で分割された cc100‑ja データセットを、文書レベルのチャンクに集約し、元の cc100 ライセンスを保持する。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 144 / ⭐ 27 / WRIMEデータセットは、日本語の投稿42,200件からなるコレクションで、筆者、3名の読者、およびその平均に対してPlutchikの8つの感情でアノテーションされています。感情分析タスク向けに、40kトレーニング、1.2kバリデーション、2kテストのスプリットで構成されています。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 137 / ⭐ 2 / 日本語のCOVID‑19 Twitter データセット：tweet IDs を含む CSV で、一般事実、個人事実、意見、曖昧な COVID 関連、不関連、未定の6つの評価オプションでアノテーションされ、tweet の関連性と事実性のテキスト分類のために作成された。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 137 / ⭐ 5 / Japanese JaQuAD、QG‑Bench のサブセットは、文レベルおよび段落レベルのデータを提供し、ハイライトされた回答トークンを用いて日本語の質問生成モデルの学習に利用でき、BLEU4、METEOR、ROUGE‑L、BERTScore、MoverScore で評価されます。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 135 / ⭐ 3 / AnimuSubtitle‑JP は、Python の ass ライブラリで解析できる、または Aegisub で編集できる日本語の ASS/SSA 字幕データセット（data_ass、data_TS）をホストしており、ODC‑By ライセンスでリリースされています。
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 132 / ⭐ 6 / 重複除外済み、NFKC正規化済みの mQA クエリ–パッセージペアで、pos_ids/neg_ids は collection のインデックスにマッピングされ、collection[pos_id] による直接取得が可能であり、元データセットの利用規約に基づきライセンスされています。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 130 / ⭐ 3 / 2010年の日本語ウェブコーパスは、HuggingFace にアップロードされ、2009年の著作権改革に基づき研究利用のライセンスが付与されており、形態素ベースの解析と変換スクリプトによる自動句読点付加テキストを含んでいます。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fujiki/japanese_alpaca_data) - 📥 129 / ⭐ 16 / **japanese_alpaca_data** のデータセットカードは、masa3141 の Japanese‑Alpaca‑LoRA 作業に基づいて構築され、参照リポジトリに追加詳細が記載されています。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 126 / ⭐ 3 / J‑HARD‑TTS‑Evalは、日本語のオートレグレッシブTTSモデルにおける短シーケンス安定性、繰り返し、韻、継続などの失敗をベンチマークし、プロンプト音声とテキストを含むデータセットを提供し、Hugging Face経由で読み込むことができる。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 125 / ⭐ 15 / Hachi-Alpacaは、Stanford Alpacaから派生した日本語合成データを提供し、mistralai/Mixtral‑8x22B‑Instruct‑v0.1で洗練・検証され、Deepinfraを通じて利用されるとともに、モデルベースの品質チェックを通過した「_cleaned」バージョンを備えています。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 120 / ⭐ 5 / llm‑jp‑instructions は、手動で整理された日本語の指示データセットで、言語モデルの微調整のために train、dev、test の分割を提供します。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 119 / ⭐ 13 / 日本語の固有表現抽出用に、Wikipediaから派生したCC‑BY‑SA 3.0 ライセンスのデータセット。 https://github.com/stockmarkteam/ner-wikipedia-dataset/ にホストされ、Stockmark Inc. によって開発されています。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 116 / ⭐ 7 / livedoor news からクリーンアップされた日本語ニュースコーパスで、CC ライセンス付き。5,894 用例のトレーニング、737 用例のバリデーション、736 用例のテストに分割されています。
 * [oscor-2301-ja-text-content](https://huggingface.co/datasets/ayousanz/oscor-2301-ja-text-content) - 📥 112 / ⭐ 2 / リポジトリは、OSCOR‑2301‑ja JSONファイルの「content」フィールドから抽出したテキストを提供し、各 content 値を変換して表示する Python スクリプトも用意しています。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 111 / ⭐ 79 / 文章対照済みの日本語ウェブ小説の章と英語ファン翻訳（106 K+ エントリ、バージョン 2）は、翻訳研究のために設計され、更新されたアラインメント、追加されたシリーズメタデータ、品質フィルタリングなしでフェアユースと Apache 2.0 の下で配布され、Hugging Face を通じた削除リクエストの対象となります。
 * [Longcontext-aozora-summary](https://huggingface.co/datasets/aixsatoshi/Longcontext-aozora-summary) - 📥 106 / ⭐ 6 / 長文から派生した要約のデータセットで、globis‑university/aozorabunko‑clean Aozora Bunko collection に由来し、CC BY 4.0 でライセンスされている。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 103 / ⭐ 2 / Japanese Common Voice 17.0 のサブセットを提供します。649 人の話者（各 30〜300 サンプル）を対象に、45,668 の発話を話者別に 80/20 に分割し、1,000 サンプル単位の Parquet ファイルにバッチ化しています。すべて CC0 ライセンスです。
