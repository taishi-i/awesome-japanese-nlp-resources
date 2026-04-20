# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專門收錄日語NLP相關的Python函式庫、LLM、詞典和語料庫資源的精選列表。
本頁面列出了Hugging Face上可用的日語NLP專用模型和資料集。目前包含204個模型和100個資料集。

_更新於2026年4月20日_

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
   * [text-classification](#text-classification)
   * [image-to-text](#image-to-text)
   * [token-classification](#token-classification)
   * [text-to-speech](#text-to-speech)
   * [image-text-to-text](#image-text-to-text)
   * [audio-to-audio](#audio-to-audio)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | 模型名稱 | Downloads | Likes | 類別 |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 2M | ⭐ 54 | automatic-speech-recognition |
| 2 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 2M | ⭐ 13 | translation |
| 3 | [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) | 📥 633k | ⭐ 5 | text-ranking |
| 4 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 400k | ⭐ 70 | sentence-similarity |
| 5 | [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) | 📥 352k | ⭐ 134 | text-generation |
| 6 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 316k | ⭐ 170 | image-to-text |
| 7 | [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) | 📥 313k | ⭐ 12 | sentence-similarity |
| 8 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 297k | ⭐ 76 | fill-mask |
| 9 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 283k | ⭐ 8 | sentence-similarity |
| 10 | [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 📥 217k | ⭐ 20 | text-generation |
| 11 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 211k | ⭐ 9 | fill-mask |
| 12 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 192k | ⭐ 41 | fill-mask |
| 13 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 186k | ⭐ 10 | translation |
| 14 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 118k | ⭐ 15 | text-generation |
| 15 | [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) | 📥 113k | ⭐ 8 | fill-mask |
| 16 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 113k | ⭐ 11 | others |
| 17 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 92k | ⭐ 58 | text-generation |
| 18 | [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) | 📥 74k | ⭐ 63 | others |
| 19 | [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) | 📥 66k | ⭐ 11 | feature-extraction |
| 20 | [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) | 📥 65k | ⭐ 14 | others |

### Datasets-ranking

| # | 資料集名稱 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 311k | ⭐ 37 |
| 2 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 6k | ⭐ 9 |
| 3 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 4k | ⭐ 6 |
| 4 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 3k | ⭐ 112 |
| 5 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 3k | ⭐ 19 |
| 6 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 2k | ⭐ 10 |
| 7 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 99 |
| 8 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 2k | ⭐ 28 |
| 9 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 2k | ⭐ 16 |
| 10 | [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) | 📥 2k | ⭐ 112 |
| 11 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 2k | ⭐ 45 |
| 12 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 2k | ⭐ 18 |
| 13 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 2k | ⭐ 7 |
| 14 | [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) | 📥 1k | ⭐ 89 |
| 15 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 1k | ⭐ 4 |
| 16 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 1k | ⭐ 34 |
| 17 | [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) | 📥 1k | ⭐ 3 |
| 18 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 941 | ⭐ 47 |
| 19 | [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) | 📥 913 | ⭐ 5 |
| 20 | [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) | 📥 878 | ⭐ 11 |

## Models
### text-generation
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 352k / ⭐ 134 / 一個九十億參數的日文優化 LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，於 2024 年 9 月以前的資料進行訓練，採用混合的 Mamba‑2/MLP/4‑layer‑attention 架構，並在 Nemotron‑Personas‑Japan 工具呼叫資料集中進行微調，可選擇在產生最終答案前生成可控的推理回溯，且可商業使用。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 217k / ⭐ 20 / OpenCALM 是由 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 之下發佈的一套僅解碼器的日語 transformer 語言模型（160 M–6.8 B 參數），經日本維基百科與 Common Crawl 訓練，可透過 Hugging Face 的 torch‑transformers 使用。
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 118k / ⭐ 15 / 一個 12 層、768 隱藏層的日本 GPT‑NeoX 模型，訓練於 CC‑100、C4 和 Wikipedia，兼容 Huggingface，並可選擇使用一個玩具前綴調優權重，使每句結尾強制出現笑臉表情符號。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 92k / ⭐ 58 / 一個 2.7‑B 參數的日語 GPT‑NeoX 模型，由 ABEJA Inc 在日語 CC‑100 與 OSCAR 上訓練，可透過 Hugging Face Transformers pipelines 或 PyTorch 使用，並以 MIT 授權釋出。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 35k / ⭐ 30 / 提供 NII 的 8B 參數 LLM‑jp‑4‑8b‑thinking 日文語言模型，已經以 pre/​mid‑training 訓練並通過 SFT/DPO 對齊，已準備好與 torch‑transformers 一起使用，並附有詳細的 cookbook 指南。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 32k / ⭐ 29 / LFM2.5‑1.2B‑JP 是一個 1.2B 參數的日語文本生成模型，基於 LFM2.5 混合架構構建，優化用於生成和完成任務，托管於 Hugging Face 並可通過 llama.cpp 運行。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 22k / ⭐ 18 / 以 Shisa 7B 數據微調了 Japanese Stable LM Base Gamma 7B，並在 JA MT‑Bench 上取得優異成績。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 22k / ⭐ 5 / LLM‑jp‑3‑150m — 來自日本情報學研究院 LLM 研發中心的 150M 參數日語語言模型，已以 Hugging Face Transformers 格式發佈，需安裝 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，並以日語維基百科、Common Crawl、WARP/PDF、WARP/HTML 以及 Kaken 數據，使用 unigram byte‑fallback tokenizer 進行預訓練。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 14k / ⭐ 20 / 提供由 NII 出品的 1.8 B 參數 llm‑jp‑3.1‑1.8b‑instruct4 日語指令調校模型，兼容 Hugging Face Transformers 及 Torch ≥ 2.3.0，包含預訓練與微調檢查點及使用示例。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 12k / ⭐ 10 / 此存儲庫提供 GGUF 格式、量化的模型檔，適用於 Stability AI 的日文 StableLM Instruct Gamma 7B，該模型由 Massed Compute 硬體製成，並屬於 TheBloke 的 a16z 資金支持的 LLM 專案的一部分。
 * [Wanabi-Novelist-12B-i1-GGUF](https://huggingface.co/mradermacher/Wanabi-Novelist-12B-i1-GGUF) - 📥 10k / ⭐ 1 / Wanabi‑Novelist‑12B 的 GGUF 量化集合（imatrix 和 static），列出多個精度級別和尺寸，提供使用說明、下載連結和額外資源。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 9k / ⭐ 21 / Llama3 Swallow 是一款日本增強版 Meta Llama 3 系列，於 2024 年 7 月 1 日發布，提供 8B 與 70B 兩種版本，包含 Instruct 與 chat 形式，並使用 SFT 與 Chat Vector 在 Megatron‑LM 上微調，並在關鍵的日本 NLP 任務上進行基準測試。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 9k / ⭐ 147 / Llama‑3‑ELYZA‑JP‑8B 是 ELYZA 推出的日語改良版，8 億參數的 Llama 3 模型，已在 Meta‑Llama‑3‑8B‑Instruct 上為日語進行微調。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 8k / ⭐ 25 / 來自國立情報學研究所的 Hugging Face 兼容的以日語為中心的 transformer 模型（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct），已在多樣化的日語和英語語料庫（包括 Wikipedia、Common Crawl、WARP、Kaken、Dolma）上預訓練，並且需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate 與 flash‑attn。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 8k / ⭐ 22 / 一個32十億參數的日語 transformer LLM (llm‑jp‑4‑32b‑a3b‑thinking)，來自國立情報學研究所 (National Institute of Informatics)，預訓練並通過有監督微調與直接偏好優化進行調整——未使用強化學習——採用 unigram byte‑fallback tokenizer。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 實驗性日本模型，透過採用 chat‑vector 方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 與 Meta‑Llama‑3‑8B‑Instruct 之間的差異，升樣後應用於 Meta‑Llama‑3‑70B‑Instruct，顯示變化不大，並計畫未來擴充。
 * [shisa-v2.1-qwen3-8b](https://huggingface.co/shisa-ai/shisa-v2.1-qwen3-8b) - 📥 8k / ⭐ 8 / Shisa V2.1推出升級的日英雙語聊天模型——擴建自更新的資料集，並進行強化的指令、翻譯與禮貌微調——涵蓋 Llama 3.2、Qwen 3‑8B、UnPhi‑4 14B 等變體，帶來顯著的性能提升。
 * [Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF) - 📥 6k / ⭐ 2 / 日本語校準的重要性矩陣 GGUF 量化（IQ3/IQ4）已在 Qwen3.5‑35B‑A3B‑heretic‑v2 模型中發布，旨在在大幅降低安全過濾器的同時維持日語生成品質，並以使用者責任免責聲明作為發布條件。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 5k / ⭐ 7 / 已預訓練的 TinyLlama，日語版本（≈50k 步），建立於約3B OSCAR/mC4 代幣上，可透過 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 與 Renju Aoki 製作。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 5k / ⭐ 18 / Llama 3.1 Swallow 是一組 8‑B 和 70‑B 模型，繼續對 Meta 的 Llama 3.1 進行預訓練以提升日語表現，然後在合成日語數據上進行 instruction‑fine‑tune，提供多個已發佈的變體，具有與 gemma‑3‑27b‑it 相當的對話行為改進。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 5k / ⭐ 85 / Rinna 的 24 層、1024 隱藏單元的日本 GPT‑2‑medium 模型，使用 CC‑100 和 Wikipedia 進行訓練，採用 SentencePiece 分詞，已在 rinna/japanese‑pretrained‑models repo 中提供（MIT‑licensed，於 2021 年 4 月 7 日發布，於 2021 年 8 月 25 日更新）。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 5k / ⭐ 16 / 一個 6 層、512 隱藏單元的 transformer，名為 Japanese GPT‑2 xSmall，訓練於日本 CC‑100 與 Wikipedia 並使用 SentencePiece tokenization；於 2021 年 8 月 25 日以 MIT 授權發布，並託管於 Hugging Face（rinna/japanese‑gpt2‑xsmall），在 arXiv 2404.01657 中被引用。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 5k / ⭐ 20 / OpenCALM 是 CyberAgent 發布的一系列日語僅解碼器 Transformer 語言模型（參數 160 M–6.8 B），訓練於日語維基百科和 Common Crawl，並以 CC BY‑SA 4.0 授權發行。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 5k / ⭐ 26 / rinna 的日語 GPT‑2 small 為 12 層、768 隱藏單元的 transformer，訓練於日語 CC‑100 和 Wikipedia，使用 SentencePiece 進行分詞，於 2021 年 8 月 25 日以 MIT 版發布（Hugging Face：rinna/japanese‑gpt2‑small，詳見 https://arxiv.org/abs/2404.01657）。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 5k / ⭐ 24 / Llama 3.1 Swallow 是一系列經過日本優化的 8B/70B Llama 3.1 模型，透過持續預訓練和日本專用說明微調進行訓練，最新的 8B‑Instruct‑v0.3 在日本 MT‑Bench 上取得了最先進的成果。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 4k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 與 Swallow Team 所開發的一款緊湊型日語指令跟隨語言模型，採用 Qwen2.5‑32B‑Instruct 的 TAID 蒸餾，並進一步於日語文本上進行預訓練，僅以 Apache 2.0 授權釋出，僅供研究用途。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 4k / ⭐ 9 / Qwen3‑Swallow v0.2 提供日英語 LLM（30B‑A3B 和 32B），採用 CPT、SFT 與 RLVR 訓練，保持強大的數學、程式編寫與推理能力，已發布九個模型及 AWQ‑quantized 變體。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 4k / ⭐ 20 / GPT‑OSS‑Swallow v0.1 提供 20B 及 120B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，能在數學與編程任務上匹敵或超越 GPT‑OSS，於 2026 年 2 月發布，包含四種 SFT/RL 變體與即將推出的量化版本。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 4k / ⭐ 107 / 一個 1.3‑B‑parameter、24‑layer transformer GPT‑1B，在 Japanese C4、CC‑100 以及 Wikipedia 上訓練，於 2022 年 1 月 26 日由 rinna Co. 發布，並以 MIT license 供使用。
 * [japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - 📥 4k / ⭐ 75 / 一個 3.6‑B 參數的日本 GPT‑NeoX 模型——36 層、2816 維隱藏層 Transformer——透過基於 PPO 的 RLHF 在翻譯後的 Anthropic 數據上進行訓練，遵循指令式對話，與 SFT 相比，基於 PPO 的勝率分別為人類約 30% 和 ChatGPT 約 34%，但傾向於產生重複文本。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 3k / ⭐ 36 / 提供由 SB Intuitions 推出的自回歸日語語言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已與其他模型進行基準測試，且附帶示例使用腳本，並註明安全訓練有限。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 3k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27‑B 參數擴充，已在包含 instruct 與 fast 變體的日文資料上進行預訓練，可透過 Hugging Face Transformers 使用。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 3k / ⭐ 5 / 一個存儲庫托管國立情報學研究院 LLM 研發中心的 8.6 B‑parameter llm‑jp‑4‑8b‑base transformer，該模型經由預訓練與中訓練，隨後進行監督式微調與直接優先權優化（未使用強化學習），並提供 PyTorch‑transformers 使用指南。
 * [gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - 📥 3k / ⭐ 18 / 由 ABEJA, Inc. 在日本 CC‑100、Wikipedia、OSCAR 上訓練的大型日語 GPT‑2 模型，使用 sentencepiece 進行分詞，可透過 Hugging Face transformers 在 PyTorch 或 TensorFlow 使用，並採用 MIT 授權。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 3k / ⭐ 26 / 日本語 3.6B 參數 GPT‑NeoX 模型經過調校以符合指令追蹤 (SFT‑v2)，在 100 個提示上與先前的 SFT 針對 ChatGPT 進行測試，於 2023 年 3 月 31 日發布。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 3k / ⭐ 21 / youri‑7b 是一個 32 層、4096 隱藏層的 transformer，來源於 Llama2‑7b，持續預訓練於約 40 B 個日語 token（CC‑100、C4、OSCAR、Pile、Wikipedia）並於 2023‑10‑31 發布，並在 AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA 與 Winogrande 上取得競爭性分數。
 * [gpt2-japanese-lyric-small](https://huggingface.co/skytnt/gpt2-japanese-lyric-small) - 📥 3k / ⭐ 3 / 日本 GPT‑2 歌詞生成模型，訓練於 143,587 首 uta‑net 歌曲，並透過網頁 Demo 與 Torch/Transformers 使用範例提供。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 143 / LFM2.5‑1.2B‑JP 是一款為日語優化的聊天模型，在日語知識和指令遵循方面優於 LFM2，支援 LoRA 的微調、使用 Transformers、vLLM、llama.cpp 進行推論，並達到 50.7 JMMLU、58.1 M‑IFEval 和 56.0 GSM8K 分數。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 2k / ⭐ 3 / llm‑jp‑4‑8b‑instruct 是 NII 的 LLM‑jp‑4 系列 4.1 B 參數的日語 LLM，先在大規模語料庫上進行預訓練，接著僅用監督式指令資料微調（不使用 DPO/REINFORCE），並附有類似食譜風格的使用指引與 byte‑fallback unigram tokenizer。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 2k / ⭐ 50 / GGUF‑格式的 NVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese，從imatrix數據集重建，已準備好使用 llama.cpp 在 CUDA 上運行。
 * [gpt2-small-japanese-char](https://huggingface.co/ku-nlp/gpt2-small-japanese-char) - 📥 2k / ⭐ 3 / 日文字符層級 GPT‑2 Small (90 M 參數) 已於 171 GB 日文維基百科、CC‑100 與 OSCAR 資料上進行預訓練，並於 A100 GPU 上訓練約 3 個月，現在可透過 Hugging Face pipeline 執行文本生成。
 * [diafill-sarashina2.2-3b-instruct](https://huggingface.co/sbintuitions/diafill-sarashina2.2-3b-instruct) - 📥 2k / ⭐ 1 / DiaFill 是一個經過微調的日語雙說話者對話腳本生成器，能從種子提示生成自然且充滿填充詞的口語對話，訓練於專有 GENIAC 數據。
 * [RakutenAI-7B-instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) - 📥 2k / ⭐ 50 / RakutenAI‑7B‑instruct，建立於 Mistral‑7B‑v0.1 上，是一款以日語為重點的LLM，在日語基準測試中名列前茅，同時保持英語表現相當；同時也發佈了聊天調校版本。
 * [llm-jp-3.1-1.8b](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b) - 📥 2k / ⭐ 12 / llm‑jp‑3.1‑1.8b 是來自 NII 的大型語言模型研發中心的 1.8 億參數日語 LLM，作為 Hugging Face 檢查點發佈（torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5），在倉庫中提供完整模型規格、分詞器和預訓練細節。
 * [RakutenAI-7B-chat](https://huggingface.co/Rakuten/RakutenAI-7B-chat) - 📥 2k / ⭐ 66 / RakutenAI‑7B‑chat 是一個以 Mistral‑7B‑v0.1 架構為基礎的日語 LLM，提供日語理解的頂尖基準結果，英語表現亦具競爭力，包含基礎模型 (RakutenAI‑7B) 與指令微調版本 (RakutenAI‑7B‑instruct)。
 * [youri-7b-instruction](https://huggingface.co/rinna/youri-7b-instruction) - 📥 2k / ⭐ 15 / 一個 7 億參數的日語指令調校 Transformer（32 層，4096 隱藏），基於 rinna/youri‑7b 構建，並以 Alpaca‑format 對 Dolly、FLAN 與 Izumi 資料集的日語子集進行微調，於 2023 年 10 月 31 日發布。
 * [RakutenAI-7B](https://huggingface.co/Rakuten/RakutenAI-7B) - 📥 2k / ⭐ 52 / RakutenAI‑7B 是一款基於 Mistral‑7B‑v0.1 的日語 LLM，在日語基準測試中領先，同時在英語任務上亦保持競爭力，提供指令調校及聊天調校版本，並於 arXiv 發表技術報告。
 * [youri-7b-chat](https://huggingface.co/rinna/youri-7b-chat) - 📥 2k / ⭐ 14 / rinna/youri‑7b‑chat 是一個 32 層、4096 隱藏單元的 transformer，從 rinna/youri‑7b 進行 instruction‑tuned，採用對話式輸入格式，使用 Dolly、Anthropic、FLAN、Izumi 以及日本語料庫的精心挑選子集，並於 2023 年 10 月 31 日發布。
 * [nekomata-7b-instruction](https://huggingface.co/rinna/nekomata-7b-instruction) - 📥 2k / ⭐ 10 / rinna/nekomata‑7b‑instruction 是一個 32 層、隱藏層大小為 4096 的日語指令微調 Transformer（基於 nekomata‑7b/Qwen 架構），遵循 Alpaca 輸入格式，並在精心挑選的 Dolly、FLAN、Izumi lab 與其他日語資料集子集上進行訓練。
 * [ALMA-7B-Ja-V2](https://huggingface.co/webbigdata/ALMA-7B-Ja-V2) - 📥 2k / ⭐ 20 / C3TR‑Adapter 將 4‑bit QLoRA 應用於 gemma‑7b，允許在免費 Colab 上使用 8.1 GB GPU，而 ALMA‑7B‑Ja‑V2 提供日英翻譯（亦支援德語、中文、冰島語、捷克語），使用 BLEU 與 chrF++ 指標評估。
 * [nekomata-14b](https://huggingface.co/rinna/nekomata-14b) - 📥 2k / ⭐ 19 / nekomata‑14B 是一個 40 層、5120 隱藏層的 Transformer，使用 Qwen‑14B 為初始化，並在 66 B 個日語 token（CC‑100、Japanese C4、OSCAR、The Pile、Wikipedia 以及 rinna 數據集）上持續預訓練，採用包含超過 150 k 的 Qwen 詞彙，在 16 台 Amazon Trainium 節點上訓練，耗時約 7 天，並於 2023 年 12 月 21 日發布。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 2k / ⭐ 1 / 日語增強、指令微調的 Gemma‑2 模型，建構於 Llama（2b/9b/27b pre‑train 和 instruction 版本），於 2025 年 5 月 19 日發布，並可於 HuggingFace 與 Swallow team 的網站上取得。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 57 / TinySwallow‑1.5B‑Instruct 是一個 1.5 B 日語指令調校的自回歸語言模型，經由 TAID 從 Qwen2.5‑32B‑Instruct 蒸餾，僅供研究使用。
 * [Sakura-13B-Galgame](https://huggingface.co/sakuraumi/Sakura-13B-Galgame) - 📥 2k / ⭐ 125 / SakuraLLM 提供非商業、RLHF 微調的日中翻譯模型，為輕小說與 galgame 領域服務，基於開源 LLM 與領域特定資料構建，提供多種尺寸、離線部署，以及明確的授權與使用指引。
 * [GPT-OSS-Swallow-20B-SFT-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-SFT-v0.1) - 📥 2k / ⭐ 5 / GPT‑OSS‑Swallow v0.1 是一個雙語日英模型家族 (20B & 120B)，透過連續預訓練、監督式微調與可驗證獎勵的強化學習進行訓練，以保持數學與程式碼性能，現已發布 SFT 與 RL 變體，並規劃量化版本。
 * [shukatsu-gemma4](https://huggingface.co/careerbot/shukatsu-gemma4) - 📥 2k / ⭐ 2 / shukatsu‑gemma4‑26b‑v1 是一個針對日本求職支援微調的 Gemma 4 26B 模型，提供在履歷表、自我推銷與職業建議上的邏輯與同理式回饋，並以 GGUF 格式提供本地推論使用。
 * [open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - 📥 2k / ⭐ 205 / OpenCALM 是 CyberAgent, Inc. 推出的日本式解碼器專用 Transformer 語言模型套件，參數量從 160 M 到 6.8 B 不等，已在 Wikipedia 和 Common Crawl 上進行預訓練，可透過 Transformers library 以 CC BY‑SA 4.0 授權取得。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 2k / ⭐ 96 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 7 B 的日語優化版本，提供 instruct 與 fast 兩種變體，具有 6.27–6.37 B 個參數，可通過 Hugging‑Face Transformers 庫進行存取。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 2k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter 日本語擴展版本，進一步針對日本語語言任務進行預訓練，並提供 base、instruct、fast 和 fast‑instruct 變體，由 ELYZA 團隊在 Llama 2 Community License 下維護。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 1k / ⭐ 17 / TokyoTech‑LLM 倉庫提供了 Swallow Llama‑2 系列的 LLaMA‑2 模型，這些模型已加入日文資料，涵蓋 7B、13B 與 70B 變體，並包含 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以來發佈的 7B Plus 版本。
 * [open-calm-large](https://huggingface.co/cyberagent/open-calm-large) - 📥 1k / ⭐ 10 / OpenCALM 是 CyberAgent 推出的僅解碼器日語 Transformer 家族 (參數量從 160 M 到 6.8 B，包含 open‑calm‑small 至 open‑calm‑7b)，由日語 Wikipedia 與 Common‑Crawl 訓練，採用 CC BY‑SA 4.0 授權，並可透過 Hugging Face transformers 使用。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 1k / ⭐ 16 / 一套日本大型語言模型（1.8 b 至 172 b beta1，含 instruct 變體）來自 NII 研究發展中心，以 Hugging Face Transformers 格式打包，並在混合的日文、英文以及網路語料上預訓練，總 token 數量超過 1 trillion，需至少 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 1k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一個 13‑B 的、已經進行指令預訓練的日語語言模型，由 NII 的 R&D Center 開發，並以 Hugging‑Face Transformers 的 checkpoint 形式發布，使用 UNIGRAM‑byte‑fallback tokenizer。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 1k / ⭐ 1 / Qwen3‑Swallow v0.2 提供 30‑B 和 32‑B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，提升日語準確度、翻譯、數學與編碼能力，以達到或超越原始 Qwen3，提供九種模型（CPT、SFT、RL）以及 AWQ‑quantized 版本，並同時發布 GPT‑OSS‑Swallow。
 * [LFM2-350M-PII-Extract-JP](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP) - 📥 1k / ⭐ 54 / LFM2‑350M‑PII‑Extract‑JP 是一個在裝置上執行的 3.5 億參數日文 PII‑擷取模型，匹配 GPT‑5 的表現，允許在合約、電子郵件和醫療報告中對敏感數據進行遮蔽。
 * [ArrowCanaria-Llama-8B-SFT-v0.1](https://huggingface.co/DataPilot/ArrowCanaria-Llama-8B-SFT-v0.1) - 📥 1k / ⭐ 23 / ArrowCanaria‑Llama‑8B‑SFT‑v0.1 是一個 8‑B 參數的日本語 LLM，在 175k 合成對話上進行微調，以提供自然閒聊、角色扮演、推理及工具使用，適用於 AI‑VTuber 環境，基於 Llama 3.1‑Swallow 8B‑Instruct 構建。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 82 / 由 ELYZA 開發的日文增強版 Llama‑2‑7B，預訓練以擴展日語能力，包含標準、指導、快速三種變體，附帶詳細使用範例、開發者貢獻，並採用 Meta 的 Llama‑2 Community License 授權。
 * [open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - 📥 1k / ⭐ 4 / OpenCALM 是 CyberAgent 旗下的日本語 decoder‑only Transformer 語言模型套件，參數範圍從 160 M 到 6.8 B，訓練資料來源於日語維基百科及 Common Crawl，並以 CC BY‑SA 4.0 版權發布。
 * [t5-base-long-livedoor-news-corpus](https://huggingface.co/llm-book/t5-base-long-livedoor-news-corpus) - 📥 1k / ⭐ 1 / 一個在日本 Livedoor 新聞語料庫上微調的 T5‑base 摘要模型，展示於《Large‑Scale Language Model Introduction guide》第七章。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 1k / ⭐ 15 / LLM‑jp 提供 13B 與 1.3B 的 transformer 語言模型，包括多個 instruction‑tuned 變體，使用 Megatron‑DeepSpeed 與 Hugging Face Transformers 生態系統構建。
 * [open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) - 📥 1k / ⭐ 17 / OpenCALM 是由 CyberAgent 出品的一套日語僅解碼器語言模型，參數規模從 160 M 到 6.8 B，基於 GPT‑NeoX，並以 CC BY‑SA 4.0 授權發佈。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 297k / ⭐ 76 / Japanese BERT‑base 預訓練於 2019 年日本維基百科，使用 IPA 字典與整詞掩碼，12 層、768 維，32,000 詞表，512 令牌序列，1 百萬步；可於 cl‑tohoku/bert‑japanese 在 CC‑BY‑SA 條款下取得。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 211k / ⭐ 9 / Japanese DeBERTa V2 大型模型已在 171 GB 的日語維基百科、CC‑100、與 OSCAR 上訓練，採用字符級 sentencepiece tokenization 與 whole‑word masking，已準備好通過 Hugging Face Transformers 進行下游微調。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 192k / ⭐ 41 / 一個基於 BERT base 的模型，預訓練於約 17 M 日文 Wikipedia 句子（2.6 GB），採用 IPA dictionary 與 WordPiece 進行 tokenization，擁有 12 layers／768‑dim hidden states／12 heads，32 000‑token 詞彙表，於 Cloud TPUs 上訓練 1 M steps，並以 CC‑BY‑SA 3.0 發布。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 113k / ⭐ 8 / 一個 BERT‑base 日語模型（12 層，768‑維隱藏，12 頭），在約 1700 萬句來自日語維基百科（2.6 GB）的資料上進行預訓練，使用 MeCab IPA 單詞級分詞，隨後進行字符級分詞，建立一個 4000 單詞詞彙表。訓練程式碼位於 cl‑tohoku/bert‑japanese，並以 CC BY‑SA 3.0 釋出。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 51k / ⭐ 6 / 一個 BERT‑base 日語模型（12 層，768 維隱藏狀態，12 頭）在 30 M 句子（約 4 GB）上訓練，使用 Unidic 2.1.2 詞級分詞，隨後進行字級分詞和整詞遮蔽，使用 512 令牌序列、256 批次及 1 M 訓練步驟。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 19k / ⭐ 48 / LINE DistilBERT Japanese 是一個 66‑million‑parameter 的 DistilBERT 模型，使用內部 BERT‑base 教師在 131 GB 的日本網路文本上進行預訓練，並於 JGLUE 上評估，採用 MeCab Unidic 與 SentencePiece 進行分詞，於 Apache 2.0 授權下釋出。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 18k / ⭐ 5 / ModernBERT‑Ja‑30M 是一款日語 BERT 變體，它將局部與全局注意力與 RoPE 混合起來，並在 4.39 TB 的日英文本上訓練，支援 8,192‑token 序列，參數規模從 30 M 至 130 M，並在使用 Flash Attention 2 時表現最佳。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 9k / ⭐ 2 / Japanese DeBERTa V2 tiny，預訓練於約 171 GB 的日語 Wikipedia、CC‑100 與 OSCAR 資料庫，需要 Juman++ 詞彙分割，已在 8 顆 NVIDIA A100 GPU 上訓練 33 小時，可進一步微調以應用於下游任務。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 9k / ⭐ 39 / Japanese‑Roberta‑Base 是由 rinna Co., Ltd. 推出的預訓練遮罩語言模型，含正確載入、token 預處理、position‑id 處理的指引，以及強調需放置於首位的 `[CLS]` token 和一致 tokenization 的使用範例。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 9k / ⭐ 47 / 一個 132 百萬參數的 Japanese ModernBERT 模型，結合 local‑global 與 RoPE attention，在 4.39 T tokens（日語/英語）上訓練，含有 102‑k‑size 的 vocab，最大 token 長度 8,192，並優化為 Flash Attention 2。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 5k / ⭐ 27 / Japanese BERT‑base (12 層, 768 hidden, 12 heads) 以 4 GB 的日本 Wikipedia（約 30 M 句）為預訓練資料，使用 Unidic 2.1.2 文字級別分詞、WordPiece 子分詞，與整詞掩碼。
 * [roberta-base-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) - 📥 5k / ⭐ 8 / Japanese RoBERTa 基礎模型，已在 Japanese Wikipedia 與 CC‑100 上進行預訓練，使用 Juman++ 分詞，於八顆 NVIDIA A100 GPU 上以 1e‑4 學習率訓練 700k 步驟。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 5k / ⭐ 21 / ModernBERT‑Ja‑310M 是一款日語 BERT 變體，結合了 local‑global attention 與 RoPE，已在 4.09 T 個日語/英語文本 token 上訓練，支持 102 400 個詞彙、8 192 token 序列，並被優化以配合 Flash Attention 2。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 4k / ⭐ 4 / DeBERTaV2 基礎模型在日本語語料庫（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上進行訓練，並採用 FP‑16 微調以應對 NLU 任務（JSTS、JNLI、JCommonsenseQA）。本模型以 CC BY‑SA 4.0 授權發佈，並獲得日本研究撥款資助。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 3k / ⭐ 32 / Japanese RoBERTa‑base，於日本維基百科與日本 CC‑100 上進行預訓練，使用 Juman++ 詞彙分割與 SentencePiece 標記化，於一週內於 8 台 NVIDIA A100 GPU 上使用 Adam（lr = 1e‑4，native AMP）進行訓練，並可微調，且於 JGLUE 上報告結果。
 * [deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 📥 3k / ⭐ 9 / Japanese DeBERTa‑V2 大型模型，預先訓練於 171 GB 日本語文本（Wikipedia、CC‑100、OSCAR），採用 Juman++ 分詞，於 8 顆 A100 GPU 上訓練 36 天，可針對下游任務進行微調。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 3k / ⭐ 30 / 日文 DeBERTa V2 基礎模型，已在 171 GB 日文維基百科、CC‑100 與 OSCAR 資料上使用 Juman++ 斷詞與 SentencePiece Tokenization 進行預訓練，訓練時間三週，使用八台 NVIDIA A100 GPU，已準備好進行微調。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 一個 12 層、768 維的 BERT-Base 日語模型，使用 2.6 GB 的維基百科（≈17 M 句子）進行訓練，採用 IPA-dictionary 字元分詞與整詞遮罩（whole‑word masking），並以 CC‑BY‑SA 3.0 版權授權釋出。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 1k / ⭐ 6 / ModernBERT‑Ja‑70M 是一款輕量級的日語 BERT 變體，結合局部與全局注意力與 RoPE，使用 4.39 T 混合語言令牌（詞彙表 102 400，最大 8 192 令牌）訓練，支援 Flash Attention 2，並提供 30 M 至 310 M 參數的多種規格。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 400k / ⭐ 70 / Ruri v3 是一個尖端的日本語文本嵌入模型，建立於 ModernBERT‑Ja，支援最多 8,192‑token 輸入、100K‑token 詞彙表、FlashAttention‑加速推論，以及多種尺寸變體，方便快速使用 sentence‑transformer。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 313k / ⭐ 12 / 日文通用文本嵌入模型 (Ruri‑v3, 30‑310 M 參數, 8192‑token 上限, 高 JMTEB 分數) 以 Sentence‑Transformers 使用範例提供，並與其他日文嵌入進行基準比較。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 283k / ⭐ 8 / Ruri v3 是一款最先進的日文文本嵌入模型，構建於 ModernBERT‑Ja，支持高達 8,192 tokens、一個 100k‑token 詞彙表、FlashAttention 加速，並提供從 37 M 到 315 M 參數的多種規模。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 29k / ⭐ 4 / Ruri v3 是一款最先進的日本語文本嵌入模型，基於 ModernBERT‑Ja 建構，支援長達 8192‑token 序列、10 萬詞彙、FlashAttention，並以 30 M 到 310 M 參數大小提供，以供 sentence‑transformers 使用。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 16k / ⭐ 44 / 一組可釋出的 Ruri v3 日文文本嵌入模型（30m–310m），包含 SentenceTransformer 使用技巧、查詢/段落前綴，以及 JMTEB 基準測試結果，展示它們與其他日文及多語言嵌入模型的比較。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 16k / ⭐ 2 / Ruri v3 提供高性能的日語文本嵌入，最多可達 8192 個 token，擁有 100k token 詞彙表，支援 FlashAttention，並提供多種模型尺寸 (30 m–310 m) 以供透過 sentence‑transformers 進行高效推理與微調。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 15k / ⭐ 9 / 包含 Ruri v3 日文文字嵌入（30 M–310 M 參數、8192‑token 限制、JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前綴的 Sentence Transformers 指令，以及幾個日文模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基準結果。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 15k / ⭐ 16 / JaColBERTv2 是一個僅限日文的 ColBERT 基於檢索模型，使用 MMarco（31 個負樣本對每個正樣本、250k 步驟、批次 32）進行知識蒸餾訓練，目前表現優於 multilingual‑e5‑large、BGE‑M3 以及 JaColBERT，完整評估仍待進行。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 14k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一個 768 維的句子轉換器，建立於 studio‑ousia/luke‑japanese‑base‑lite 上，已在 shunk031/jsnli 培訓一個 epoch，並包含聚類、語意搜尋以及同時適用於 Sentence‑Transformers 與 HuggingFace 的範例。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 14k / ⭐ 34 / GLuCoSE 是一個基於 LUKE 的日語句子嵌入模型，輸出 768 維均值池化向量（最多 512 個 tokens），在網路及 NLI/搜尋資料上訓練，於相似度基準上達成 0.864 Spearman 與 0.818 Pearson。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 10k / ⭐ 44 / PLaMo‑Embedding‑1B 是 Preferred Networks 開發的日本文本嵌入模型，能將日文文本轉換為向量，用於資訊檢索、分類與聚類，在 JMTEB 基準測試上表現優異，且以 Apache v2.0 license 免費提供。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 6k / ⭐ 23 / GLuCoSE v2 是一款適合 CPU 的日語文本嵌入模型，透過蒸餾與多階段對比學習進行微調，提供優越的語義相似度與檢索性能—在 MIRACL 以及相關基準上超越同等規模模型。
 * [ruri-small-v2](https://huggingface.co/cl-nagoya/ruri-small-v2) - 📥 2k / ⭐ 4 / Ruri 發布了日文通用文本嵌入模型 v3（30 M–310 M 參數，最大長度 8192 token），並取得 JMTEB 的最高分數，提供簡易的 sentence_transformers 使用方法（以「クエリ: 」或「文章: 」作前綴），以及檢索、STS、分類、重排序、聚類及成對分類任務的基準結果。
 * [ruri-v3-pt-310m](https://huggingface.co/cl-nagoya/ruri-v3-pt-310m) - 📥 2k / ⭐ 1 / Ruri v3 是一個預訓練的日文文字嵌入模型，基於 ModernBERT‑Ja，提供 30 M 至 310 M 參數版（含微調的 310 M 版本），可透過 sentence‑transformers 使用，並可選擇搭載 Flash‑Attention 2，並以 Apache 2.0 授權發布。
 * [ruri-v3-pt-30m](https://huggingface.co/cl-nagoya/ruri-v3-pt-30m) - 📥 1k / ⭐ 1 / Ruri‑v3 是一款基於 ModernBERT‑Ja 的日語文本嵌入模型，提供四種預訓練大小（30 M–310 M 參數），可與 sentence‑transformer 前綴一起使用，用於語義、主題、查詢和文件編碼，支持 Flash Attention 2，並在 Apache 2.0 授權下提供。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 2M / ⭐ 54 / 日語 wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 與 JSUT 上微調，需要 16 kHz 音訊，並可透過 HuggingSound 或 HuggingFace pipelines 使用。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 42k / ⭐ 97 / Kotoba‑Whisper‑v2.2 是一款日語 ASR 模型，擴展了 kotoba‑whisper‑v2.0，整合了 integrated diarization 與 automatic punctuation，透過 HuggingFace‑Transformers pipeline 實現，並與 Asahi Ushio 和 Kotoba Technologies 合作開發。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 30k / ⭐ 38 / reazonspeech-nemo-v2 是一款擁有 619‑M參數的日語長文語音識別模型，基於改進版 Fast‑Conformer 與 Linearly Scalable Attention 架構構建，訓練於 ReazonSpeech v2.0 資料集，透過 subword RNN‑T decoder（3000‑token SentencePiece）提供多小時推理，並以 Apache 2.0 授權方式分發。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 28k / ⭐ 134 / Anime Whisper 是一個輕量級的日語 ASR 模型，已在約 5,300 小時的動漫式對白上微調，提供低幻覺、節奏對齊的標點符號，並能準確轉錄非語音聲音和 NSFW 內容，必須在沒有初始提示的情況下運行。
 * [whisper-ja-1.5B](https://huggingface.co/efwkjn/whisper-ja-1.5B) - 📥 26k / ⭐ 2 / 經精細調校的 Whisper‑Large‑v3 基線在 KitsuneX07、TEDxJP、kotoba‑tech、Saruwatari‑lab 與 grider‑without‑ai 測試集上提供競爭性的 SOTA CER，訓練於 OOPPEENN、Reazon、小虫哥_、Common Voice 20 與 deepghs，且表現出較此前模型更小的檢查點與偶爾重複。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 10k / ⭐ 52 / NVIDIA NeMo 的 0.6 B‑參數 Hybrid FastConformer‑TDT‑CTC ASR 模型能帶標點符號轉錄日語語音，並且可在 NeMo 框架內進行推論或微調。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 8k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供 6.3 倍更快的蒸餾 Whisper 模型，支援日本語與英語的 ASR 以及雙向語音轉文字翻譯，這些模型由 OpenAI 的 Whisper large‑v3 透過 knowledge distillation 與 cross‑entropy 及 KL‑divergence loss 建構。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 4k / ⭐ 90 / Kotoba‑Whisper v2.0 是一款從 OpenAI Whisper large‑v3 提煉的日語ASR模型，使用 7.2 million ReazonSpeech 片段訓練，速度比原版快 6.3×，同時在領域測試中匹配教師模型的 CER/WER，並包含 stable‑ts/punctuation 支援及完整訓練程式碼於 GitHub。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 3k / ⭐ 19 / Kotoba‑Whisper‑v2.1 是一款日語 ASR 模型，繼承了 kotoba‑whisper‑v2.0，並整合了標點符號後處理流程，能保持相當的 CER 性能，同時實現無縫、能感知標點符號的轉錄。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 2k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一個擁有 **96.7 M** 參數的 **wav2vec 2.0** Base 模型，已在 **ReazonSpeech v2.0 Japanese ASR corpus** 上微調，達到 **13.22 % CER**，可透過 **Hugging Face transformers** 部署，並以 **Apache 2.0 license** 發布。
 * [kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) - 📥 2k / ⭐ 34 / Kotoba‑Whisper v1.1 是一款日文 ASR 模型，擴充了 kotoba‑whisper‑v1.0，加入無縫的標點符號添加後處理流程，提升轉錄準確率並減少延遲，與多個 Whisper 基線相較更為優秀。
 * [wav2vec2-large-xlsr-japanese](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese) - 📥 2k / ⭐ 5 / Fine‑tuned Wav2Vec2‑Large‑XLSR‑53 用於日語，已在 Common Voice 與 JSUT 數據集上以 16kHz 音訊訓練，準備好進行 16kHz 粵語使用與評估。
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 1k / ⭐ 24 / Kotoba Whisper v2.0 已轉換為 CTranslate2 格式，可與 CTranslate2 與 faster‑whisper 一同使用，並提供安裝、推理範例、Apple M2 基準測試以及轉換說明。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 66k / ⭐ 11 / Japanese Sentence‑BERT (v1) 模型，用於生成句子嵌入，並提供改進版 v2，並可透過 Hugging Face Transformers 與自訂的 `SentenceBertJapanese` 類別示範使用。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 46k / ⭐ 51 / 一個日本語的 Sentence‑BERT v2，經過在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上微調，並採用 MultipleNegativesRankingLoss，與 v1 相比提升了約 1.5–2 % 的準確率，並以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 形式釋出。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 42k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一個授權為 Apache‑2.0 的日語 CLIP 模型，基於 ViT‑B/16，訓練於翻譯成日語的 CC12M 標題，並於 2022 年 5 月 12 日發布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 21k / ⭐ 29 / LY Corporation 的 clip‑japanese‑base 是一個訓練於約 1 B 影像‑文字配對的日文 CLIP 模型，使用 Eva02‑B Transformer 影像編碼器並配備 12 層 BERT 文字編碼器，於 STAIR 的 R@1 成績為 0.30，於 Recruit 的準確度為 0.89，以及於 ImageNet‑1K 的準確度為 0.58，並支援零樣本影像分類與檢索。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 14k / ⭐ 17 / Japanese CLIP 模型 clip‑japanese‑base‑v2，升級至約 2 B 影像‑文字配對並 distillation，將 Eva02‑B 影像編碼器與 12 層 BERT 文本編碼器結合，以達到比其前身更高的 ImageNet‑1k 準確度 (0.708)。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 12k / ⭐ 2 / ja_ginza_electra 是一個 spaCy v3 Python 套件，提供已在 mC4 和 UD_Japanese_BCCWJ r2.8 上微調的日語 ELECTRA 模型（基於 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator），並具備自訂 bunsetu‑phrase detection，依照 MIT license 發佈。
 * [japanese-avhubert-large_noise_pt](https://huggingface.co/enactic/japanese-avhubert-large_noise_pt) - 📥 12k / ⭐ 1 / 一個已預訓練的 2,250 小時 AVHuBERT Large 自監督式模型，使用噪音增強於日語音視覺數據上訓練，以強健地支持音視覺語音辨識。
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 4k / ⭐ 4 / fastText 是一個輕量級、開源函式庫，可在標準 CPU 上快速學習文字與句子嵌入及分類器，能在數分鐘內以數十億字進行訓練，可被壓縮以供行動裝置使用，並提供分類與語言識別的預訓練向量。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 2k / ⭐ 14 / Japanese Sentence‑LUKE 模型在與 Sentence‑BERT 相同的資料集上進行訓練，表現優於或相當於 Sentence‑BERT，基於 studio‑ousia/luke‑japanese‑base‑lite 建立，並透過 Hugging Face Transformers 的 MLukeTokenizer 與 LukeModel 使用。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 2k / ⭐ 55 / 一個日語 T5 模型，預訓練於約 100 GB 的 Wikipedia 與 OSCAR 數據，使用 SentencePiece 分詞，超越了 Google 的多語言 T5，在新聞分類基準上表現更佳，但仍需要微調，且可能產生偏見輸出。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 2k / ⭐ 3 / 一款在 JSNLI 上使用監督式 SimCSE 微調的日語 BERT‑base 模型，透過 Sentence‑Transformers 或 HuggingFace 以 CLS pooling 方式公開，訓練於 1 M 範例，batch size 512，學習率 5 × 10⁻⁵，溫度 5 × 10⁻⁵，64‑token 限制，以及 BFloat16 精度。
 * [llm-jp-4-vl-9b-beta](https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta) - 📥 1k / ⭐ 11 / LLM‑jp‑4‑VL 9B beta 是一個以 llm‑jp‑4‑8b‑instruct 和 SigLIP‑2 為基礎構建的 90 億參數日語視覺‑語言模型，採用 InternVL3.0‑style 動態切片以及輕量化 MLP 投影器，在 FineVision 與 Jagle 上進行訓練後，於日語基準測試中達到具競爭力的表現。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 1k / ⭐ 24 / Sarashina‑Embedding‑v2‑1B 是一個 1,792 維的日語句子變換器，透過多階段對比學習訓練，達到先進的 JMTEB 分數，可用於語義相似度、搜尋、同義句挖掘、分類和聚類，透過 Sentence‑Transformers 並可加上可選的指令前綴。

### text-ranking
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 633k / ⭐ 5 / 以日語訓練的 CrossEncoder 重新排序模型，規模從 xsmall（384）到 large（1024），並包含 BGE‑v2‑m3‑v1 模型，附有微調、推理的範例程式碼，以及在 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上的基準分數。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 45k / ⭐ 7 / 日本 CrossEncoder 重排序模型 覆蓋 xsmall 到 large（含 BGE），已於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 進行評估，並附上可直接使用的 sentence_transformers 與 HuggingFace 整合範例。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 30k / ⭐ 13 / Ruri‑v3 Reranker 是一款以 ModernBERT‑Ja 為基礎的強大日語文本重排序器，支援多達 8,192 令牌序列、100k 令牌詞彙表、FlashAttention 以及 SentencePiece tokenizer，並可透過 sentence‑transformers 使用。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 8k / ⭐ 6 / 快速、輕量級的日語 Reranker v2 模型（tiny、xsmall、small、base）具有基準分數和 GPU 速度，可通過 sentence_transformers CrossEncoder 和 transformers ≥ v4.48 （可選使用 flash‑attn 加速）使用，並且亦提供 ONNX/量化版本以供 CPU/ARM 使用。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 7k / ⭐ 2 / Japanese‑reranker‑small‑v2 是一款輕量、快速的日語重排序模型系列（v2），提供從 tiny 到 base 的各種變體，最高可達平均 0.89 分，且 GPU 推論時間為 2–15 秒，亦包含 cross‑encoder 選項，並要求 Hugging Face Transformers v4.48+；可選擇 Flash Attention 2 以加速。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 6k / ⭐ 7 / 一套日本 Reranker v2，發布從 tiny 到 large 的 CrossEncoder 與基礎模型，每個模型皆附有基準分數與 GPU 推論時間，且需要 HuggingFace Transformers ≥ 4.48（可選 flash‑attn 以加速推論）。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 3k / ⭐ 16 / 由 xsmall 到 large 的日文 CrossEncoder 排序模型，使用日語文本訓練，透過 sentence_transformers 提供，並於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上進行評估。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 2k / ⭐ 15 / 一套日本 CrossEncoder 重複器（reranker）套件——包括 xsmall、small、base、large 以及 japanese‑bge‑reranker‑v2‑m3‑v1——搭配示例使用、在多個基準上的評估指標與輔助文件。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 1k / ⭐ 6 / 一個小型、高速的日語 re‑ranker 函式庫（v2），提供 tiny‑through‑base 與 cross‑encoder 模型，具有詳細的延遲與準確率統計資訊，需 Transformers ≥ 4.48（可選 Flash‑Attention 2）並支援 ONNX/quantization 用於 CPU/ARM 部署。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 1k / ⭐ 12 / 一個使用 Sentence Transformers 構建的日本交叉編碼器重排序器，展示了對各種尺寸的 Ruri‑Reranker 模型的推理使用和基準結果。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 1k / ⭐ 2 / 日文 CrossEncoder Reranker 模型（xsmall、small、base、large、BGE‑v2 m3）隱藏層大小 384–1024，示例推理通過 sentence_transformers 和 Hugging Face，在 JQaRA、JaCWIR、MIRACL 和 JSQuAD 上獲得 0.71–0.97+ 的分數。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 2M / ⭐ 13 / 一個以新 VNTL 數據集為基礎的 LLaMA 3 Youko qlora 微調模型，優化為準確、逐字的日語視覺小說到英文翻譯，不使用聊天模式，使用預設的 LLaMA 3 提示，並建議採用中性取樣（temperature 0，無重複懲罰）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 186k / ⭐ 10 / Sugoi LLM 14B Ultra (GGUF) 是一個日語轉英語的翻譯模型，BLEU 分數為 21.38——幾乎是其先前分數 13.67 的兩倍——在 RPG‑Maker 方括號文本上擅長，提示遵從性強，並為交互式聊天 UI 生成 JSON 輸出。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 41k / ⭐ 31 / 微調、GGUF‑量化後的 LFM2‑350M checkpoint，適用於近即時雙向日英短至中篇文本翻譯，可透過 llama.cpp 使用。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 28k / ⭐ 73 / 來自 Opus corpus 的日文-英語 Transformer‑Align MT 模型，使用 normalization 與 SentencePiece 先行處理，在 Tatoeba 測試集上達到 41.7 BLEU 與 0.589 chr‑F。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 5k / ⭐ 118 / PLaMo Translation Model 是 Preferred Networks 為翻譯任務所創建的大規模語言模型，可供 base、post‑trained 以及 evaluation 版本使用，並以 PLaMo community license 釋出，未對聊天或其他下游用途進行 instruction‑tuned。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 2k / ⭐ 32 / FuguMT 是一個由 transformers 與 SentencePiece 建構的日文對英語 Marian‑NMT 翻譯模型，在 Tatoeba 上取得 39.1 BLEU 分數。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 1k / ⭐ 54 / FuguMT 是一個基於 Marian‑NMT 的英日翻譯模型，使用 Hugging Face Transformers 和 SentencePiece 構建，於 Tatoeba 上達成 32.7 的 BLEU 分數。
 * [LFM2-350M-ENJP-MT](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT) - 📥 1k / ⭐ 87 / LFM2‑350M‑ENJP‑MT 是一個經過微調的 LFM2‑350M checkpoint，能為短到中等長度輸入提供近乎即時、雙向日英翻譯，品質可與大十倍規模的模型媲美，示例涵蓋日常、技術、商業及新聞領域，並強調人工‑AI 協作使用。

### text-classification
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 10k / ⭐ 15 / 在 chABSA 數據集上訓練的日文情感分析模型，達到 loss 0.0001、accuracy 1.0、以及 F1 1.0。使用 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 構建，使用 Adam 進行優化（learning rate 2e‑05，10 epochs，batch size 16），並通過 `model(**inputs)` 評估。
 * [bert-for-japanese-twitter-sentiment](https://huggingface.co/LoneWolfgang/bert-for-japanese-twitter-sentiment) - 📥 4k / ⭐ 2 / Fine‑tuned BERT 適用於日文推文情感分析，使用 JTS1k dataset，將推文分類為 negative (0)、neutral (1) 與 positive (2) 標籤，已準備好可與 transformers pipeline 一同使用。
 * [luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 📥 3k / ⭐ 43 / 一個日語版本的 LUKE 模型，在 WRIME 數據集上微調，能夠分類一句話中表達的八種情緒——快樂、悲傷、期待、驚訝、憤怒、恐懼、厭惡、信任。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 3k / ⭐ 2 / 在《Large Language Model Introduction》第5章中介紹的日本 BERT‑based 模型，已於 JGLUE JSTS 資料集上進行微調，用於語義相似度評分。此模型包含 Colab notebooks、transformers‑pipeline 使用說明，以及 Apache 2.0 授權。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 2k / ⭐ 16 / 在 Amazon 商品評論上微調日本 BERT（cl‑tohoku/bert‑base‑japanese‑v2）以進行情感分類，達到約 81% 的準確率與 0.73 的 F1 分數，在 6 個 epoch 之後，學習率為 2 × 10⁻⁵。
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 1k / ⭐ 6 / 一個針對 WRIME 數據集微調的日本 BERT BASE 模型，為作者和讀者預測八種情感（喜悅、悲傷、期待、驚訝、憤怒、恐懼、厭惡、信任）的 0‑4 強度分數；代碼可用，訓練耗時 3 小時於 K80 上，對作者達到約 0.6 MSE，對讀者達到約 0.2 MSE。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 316k / ⭐ 170 / Manga OCR 是一個 Vision Encoder‑Decoder OCR 工具，能閱讀垂直與水平的日語漫畫文字（包含振假名），適用於多種字體與低品質圖像，且源碼免費提供。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 64k / ⭐ 6 / Meikiocr的 `meiki.text.recognition.v0`——一個基於 D‑FINE 的 MobileNetV4 模型，在日語視訊遊戲文字上微調——為水平文字提供最先進的準確性和延遲，能從 960×32 的輸入中偵測多達 48 個字符，並輸出每個字符的外框與置信度分數。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 52k / ⭐ 3 / meikiocr 提供一款基於 D‑FINE 的開源權重文字偵測模型，適用於遊戲視訊（v0.1 版，採用 MobileNet‑v4 主幹，提供兩種解析度變體與 64 框限制），以及實驗性低延遲 tiny 與 small 變體，已在日本遊戲及漫畫上訓練。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 1k / ⭐ 25 / Sarashina2.2‑OCR 是一款 3‑B 參數、端到端的 OCR 模型，經過人類偏好優化後，能將日文與英文文件解析為 Markdown，並將表格轉換為 HTML，數學轉換為 LaTeX，圖形轉換為 bounding‑box 註釋；它透過將 SigLIP2 為基礎的視覺編碼器與 Sarashina2.2‑3B‑Instruct LLM 整合，實現高解析度視覺‑語言理解。

### token-classification
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 16k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日語 NER，可提取八種實體類型（公司、政治/其他組織、設施、產品、事件），透過 `BertForTokenClassification`，在 Stockmark Wikipedia 數據集上訓練，並可透過 `transformers`、`unidic_lite`、`fugashi` 安裝，採用 CC BY‑SA 3.0 許可證。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 11k / ⭐ 10 / Fine‑tuned Japanese BERT‑Base 用於在維基百科資料集上的命名實體識別，已在《Large Language Model Introduction》一書第六章展示，可透過 Hugging Face transformers pipeline 部署（Apache 2.0 授權）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 使用 5 週期 Adam (lr 5e‑5, batch 12) 微調 XLM‑RoBERTa‑base，針對日語 NER 資料集（tags PER, ORG, LOC, INS, PRD, EVT）以達成 0.0173 的驗證損失，已於 Transformers 4.23.1 與 PyTorch 1.12.1 發佈。

### text-to-speech
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 2k / ⭐ 9 / 一個名為 **tsukuyomi‑wavlm** 的日語 TTS 模型—在 tsukuyomi 語料庫 100 條語句上 fine‑tuned 300 epochs，使用 WavLM discriminator 和 A1/A2/A3 prosody features 於 VITS architecture，匯出為 61 MB 的 ONNX file，能生成 22.05 kHz syntheses。
 * [Anime-Llasa-3B](https://huggingface.co/NandemoGHS/Anime-Llasa-3B) - 📥 1k / ⭐ 26 / Anime‑Llasa‑3B 是一款建立於 HKUSTAudio/Llasa‑3B 上的日語 TTS 模型，透過更多訓練資料進行增強，以提升其表達力與穩定性，並授權為 CC‑BY‑NC‑4.0。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 3k / ⭐ 123 / PaddleOCR‑VL‑For‑Manga 由 PaddleOCR‑VL 微調，於 Manga109 的對話框裁切圖像上達成 70％完整句子準確率——高於 27％基準的三倍以上——使用多語系資料集，並提供訓練程式碼與開發人員指南。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 2k / ⭐ 14 / Anime‑XCodec2‑44.1kHz‑v2 將 16 kHz 的日語語音升頻至 44.1 kHz 高保真音訊，並使用僅解碼器的 RMS‑loss 微調，保持編碼器/代碼簿凍結並保留相同的語音標記。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 113k / ⭐ 11 / Japanese‑language BERT‑Base（12層，768‑次元，12頭）以 Unidic 為基礎的單詞層級加字符層級標記化以及整詞遮蔽，在 CC‑100 和 2023 Wikipedia 上進行預訓練，產生了 7,027‑token 詞彙。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 74k / ⭐ 63 / Japanese BERT‑base (12 層, 768‑維度隱藏, 12 頭, 32k 詞彙) 以完整詞遮蔽在 CC‑100 與 2023‑Jan Wikipedia 上預訓練，使用 Unidic 2.1.2 詞級分詞加 WordPiece，訓練 200 萬步。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 65k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上訓練，使用 Unidic‑lite 詞級分詞，結合 WordPiece 子詞與全詞遮蔽，模型為 24 層、1024 維隱藏、16 頭、32k 詞表；預訓練程式碼位於 cl‑tohoku/bert‑japanese。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 21k / ⭐ 16 / 日文 DeBERTa V3 基礎版本，預訓練於 LLM‑jp v1.0 的 540 B 個 token，使用已調整的 DeBERTa V3 設定，採用 unigram byte‑fallback tokenizer（無形態學分析器），並進行 fine‑tuned 於 JGLUE NLU 任務。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 19k / ⭐ 1 / 一個高度優化的 GGUF 版本，基於 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 與廣泛修復，調校以擅長日語，並可在 llama.cpp 上運行，至少需要 16 GB RAM 與 6 GB 硬碟空間（GPU 為選用）。
 * [SIP-jmed-llm-3-13b-OP-4k-base](https://huggingface.co/SIP-med-LLM/SIP-jmed-llm-3-13b-OP-4k-base) - 📥 18k / ⭐ 1 / SIP‑jmed‑llm‑3‑13b‑OP‑4k‑base 是一個 Apache‑2.0 授權、域適應的日英醫療大語言模型，基於 llm‑jp‑3.1‑13b 建立，由 SIP’s third‑term program for medical knowledge 研發的研究原型，但並非臨床使用。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / 一個以約 100 GB 的 Wikipedia 與 OSCAR CC‑100 數據（混合 10:1、Byte‑fallback 的 SentencePiece）預訓練的日本 T5‑v1.1 模型，需對下游任務進行微調，包含遷移學習範例程式碼，提示輸出可能存在偏差，且採用 CC‑BY‑SA 4.0 授權。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 15k / ⭐ 5 / 一個為日語微調的 Qwen 3.5‑9B GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，進行了廣泛的錯誤修復、大規模日語校準，並可在 CPU 上運行，需 16 GB RAM 及 6 GB 磁碟空間，透過 llama.cpp。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 7k / ⭐ 3 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一款頂級、以日文為焦點的 GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，具備廣泛的日文校準和社區修正的缺陷，即使沒有 GPU 也能在 llama.cpp 上運行，最低需要 8 GB RAM 及 3 GB 磁碟空間。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-thinking-gguf) - 📥 7k / ⭐ 8 / 一個使用 imatrix 數據集和自訂聊天模板，用 llama.cpp 編譯而成的 GGUF 版本 LLM‑JP 的 4.8‑b “thinking” 模型。
 * [Llama-3-ELYZA-JP-8B-gguf](https://huggingface.co/mmnga/Llama-3-ELYZA-JP-8B-gguf) - 📥 5k / ⭐ 4 / 由 elyza 提供的 GGUF‑converted Llama‑3‑ELYZA‑JP‑8B，使用 TFMC/imatrix‑dataset‑for‑japanese‑LLM 構建，已準備好供 llama.cpp 使用。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/alfredplpl/llm-jp-4-8b-thinking-gguf) - 📥 3k / ⭐ 5 / 一個已 GGUF 量化的 llm‑jp‑4‑8b‑thinking 模型版本，保留了最小聊天模板，可通過 llama‑cpp 的 llama‑completion 或 LM Studio 使用，但不支援 llama‑cli/llama‑server.
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 3k / ⭐ 3 / 一個 T5 v1.1 模型，預訓練於日本 Wikipedia 以及 mC4/ja，採用 GEGLU 激活；預訓練期間不使用 dropout；不共享 embedding‑classifier；在 CC‑BY‑SA 4.0 協議下發佈（商業使用須事先聯繫）。
 * [Qwen3.5-9B-Japanese-awy](https://huggingface.co/Aikimi/Qwen3.5-9B-Japanese-awy) - 📥 3k / ⭐ 5 / 一個 9‑B Qwen3.5 日語模型經過微調並使用 Unsloth 轉換為 GGUF，提供多種量化權重（Q4_K_M、Q5_K_M、Q3_K_M、F16、BF16‑mmproj），並且在 TFMC/imatrix‑Japanese‑LLM 數據集上訓練速度是原來的兩倍。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 3k / ⭐ 17 / 高效能日文 SPLADE v2 透過 WebUI demo 可進行稀疏向量轉換與推理，使用 YAST 訓練，提供 YASEM 嵌入，並報告 JMTEB 基準結果。
 * [NeonMaid-12B-v2-i1-GGUF](https://huggingface.co/mradermacher/NeonMaid-12B-v2-i1-GGUF) - 📥 3k / ⭐ 6 / 提供 NeonMaid‑12B‑v2 模型的多種 GGUF 量化選項，包含下載連結、尺寸/品質表格、使用指導以及 FAQ。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-32b-a3b-thinking-gguf) - 📥 3k / ⭐ 7 / llm‑jp‑4‑32b‑a3b‑thinking 的 GGUF‑格式轉換，使用 TFMC 的 imatrix 數據集構建，通過 llama.cpp 進行 CUDA 啟用推理。
 * [Llama-3.1-Nemotron-Nano-8B-v1-gguf](https://huggingface.co/mmnga/Llama-3.1-Nemotron-Nano-8B-v1-gguf) - 📥 2k / ⭐ 1 / 一個已轉換成 gguf 的 Llama‑3.1‑Nemotron‑Nano‑8B‑v1 模型，該模型基於 imatrix 數據集構建，附帶使用 CUDA 編譯 llama.cpp 以及通過 llama‑cli 運行該模型的說明，並包含一個示例烹飪提示。
 * [ArrowCanaria-Llama-8B-SFT-v0.1-gguf](https://huggingface.co/mmnga-o/ArrowCanaria-Llama-8B-SFT-v0.1-gguf) - 📥 2k / ⭐ 4 / DataPilot 的 gguf 轉換版本 ArrowCanaria‑Llama‑8B‑SFT‑v0.1，在 TFMC/imatrix‑dataset‑for‑japanese‑LLM 數據上訓練，可用於 CUDA 版的 llama.cpp 並透過提供的 llama‑cli 命令執行。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 73 / Llama‑3‑ELYZA‑JP‑8B 是一款日本優化的 8‑B Llama 3 模型，採用 GGUF (Q4_K_M) 與 AWQ 量化，能以 llama.cpp、LM Studio 或 OpenAI‑相容 API 執行。
 * [japanese-llama-3-8b-instruct-v2-i1-GGUF](https://huggingface.co/mradermacher/japanese-llama-3-8b-instruct-v2-i1-GGUF) - 📥 2k / ⭐ 1 / 提供日本 Llama‑3 8B Instruct v2 模型的 weighted/IMatrix GGUF 量化版本（2.1–6.7 GB），包含 HuggingFace 上的靜態量化連結、使用說明以及模型請求 FAQ。
 * [t5-base-long](https://huggingface.co/retrieva-jp/t5-base-long) - 📥 2k / ⭐ 2 / 一個 T5 v1.1 日語編碼器‑解碼器模型，已在日語維基百科和 mC4/ja 上訓練，使用 GEGLU 激活函數，無 dropout，d_model 更大但 heads 更少，512‑token 輸入，114‑token 輸出，256‑batch fp32，CC‑BY‑SA 4.0 授權，商業使用請聯絡。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/alfredplpl/llm-jp-4-32b-a3b-thinking-gguf) - 📥 2k / ⭐ 2 / 一個40億參數的日本 LLM 已轉換為 GGUF，並保留最小聊天模板，可在 llama‑cpp 的 llama‑completion 或 LM Studio 中使用（原始為 llm‑jp/llm‑jp‑4‑32b‑a3b‑thinking）。
 * [cyberagent-Mistral-Nemo-Japanese-Instruct-2408-gguf](https://huggingface.co/mmnga/cyberagent-Mistral-Nemo-Japanese-Instruct-2408-gguf) - 📥 2k / ⭐ 4 / 提供一個已轉為 gguf 的 cyberagent 的 Mistral‑Nemo‑Japanese‑Instruct‑2408 模型（使用 imatrix 數據構建），並包括 llama.cpp CUDA 啟用建置與使用說明以及範例 prompt。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 2k / ⭐ 22 / 一個 GGUF‑格式的 pfnet 的 plamo‑2‑translate 發行版，基於 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 數據構建，並附有使用 llama.cpp 在支援 CUDA 的硬體上編譯與執行的說明。
 * [ABEJA-Qwen3-14B-Agentic-256k-v0.1-gguf](https://huggingface.co/mmnga-o/ABEJA-Qwen3-14B-Agentic-256k-v0.1-gguf) - 📥 2k / ⭐ 2 / 已將 ABEJA‑Qwen3‑14B‑Agentic‑256k‑v0.1 轉換為 GGUF 格式，使用 TFMC/imatrix‑dataset‑for‑Japanese‑LLM，準備好在支援 CUDA 的 llama.cpp 上進行推理，並附上示例日語料理提示。
 * [AXCXEPT-phi-4-open-R1-Distill-EZOv1-gguf](https://huggingface.co/mmnga/AXCXEPT-phi-4-open-R1-Distill-EZOv1-gguf) - 📥 2k / ⭐ 3 / AXCXEPT 的 gguf 格式化 phi‑4‑open‑R1‑Distill‑EZOv1 模型，基於 TFMC/imatrix‑dataset 為日本 LLM 構建，可按提供的建置與啟動指令使用 CUDA‑enabled llama.cpp 執行。
 * [GPT-OSS-Swallow-20B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-RL-v0.1-gguf) - 📥 1k / ⭐ 4 / 一個 gguf‑format 轉換的 GPT‑OSS‑Swallow 20B RL v0.1 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 數據構建，已準備好透過 llama.cpp 以 CUDA 支持執行。
 * [Gemma-2-Llama-Swallow-9b-it-v0.1-gguf](https://huggingface.co/mmnga/Gemma-2-Llama-Swallow-9b-it-v0.1-gguf) - 📥 1k / ⭐ 1 / Gemma‑2‑Llama‑Swallow‑9b‑it‑v0.1 以 GGUF 格式發布，由 tokyotech‑llm 發布，並從 TFMC/imatrix‑dataset‑for‑japanese‑llm 構建，使用 llama.cpp (CUDA‑enabled) 執行，提示示例為 “You are a professional chef, teach me a recipe.”
 * [Ninja-v1-NSFW-gguf](https://huggingface.co/mmnga/Ninja-v1-NSFW-gguf) - 📥 1k / ⭐ 5 / Local‑Novel‑LLM 專案中 Ninja‑v1‑NSFW 模型的 gguf‑格式轉換，使用 imatrix 資料集訓練，並準備部署至 llama.cpp。
 * [llm-jp-4-8b-instruct-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-instruct-gguf) - 📥 1k / ⭐ 2 / gguf 格式轉換的 llm‑jp‑4‑8b‑instruct 容器，使用 imatrix 資料構建，含 LMStudio 設定及範例 llama.cpp CUDA 命令。
 * [Llama-3-ELYZA-JP-8B-Heretic-i1-GGUF](https://huggingface.co/mradermacher/Llama-3-ELYZA-JP-8B-Heretic-i1-GGUF) - 📥 1k / ⭐ 1 / 存儲庫提供了針對 Llama‑3‑ELYZA‑JP‑8B‑Heretic 的完整 weighted/imatrix GGUF 定量化集合，涵蓋不同品質與大小等級（例如：i1‑IQ1_S、i1‑IQ2_M、i1‑Q4_K_M），可從 HuggingFace 下載，並附有指向 TheBloke 的 README 的使用說明。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5-gguf](https://huggingface.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf) - 📥 1k / ⭐ 2 / GGUF 轉換 Llama‑3.1‑Swallow‑8B‑Instruct‑v0.5 由 tokyotech‑llm，結合 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附帶 Build/Run 指令 for llama.cpp.
 * [shisa-v2.1-qwen3-8b-UD-japanese-imatrix](https://huggingface.co/dahara1/shisa-v2.1-qwen3-8b-UD-japanese-imatrix) - 📥 1k / ⭐ 4 / 一個已經 GGUF‑量化的 shisa‑v2.1‑qwen3‑8b 模型，使用 Unsloth Dynamic 2.0 構建，社群修補了 Qwen3 設定以減少故障，採用更大的 imatrix 以提升日語表現，並具 40K 的最大上下文長度。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 12 / Sarashina2.2 提供 0.5‑B、1‑B、和 3‑B 的語言模型，這些模型由 SB Intuitions 透過三階段流程及合成資料進行訓練，達成優異的日文 QA、數學及編碼分數，同時提供未經指令微調的預訓練權重，可能產生有偏差的輸出。
 * [umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf](https://huggingface.co/mmnga/umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf) - 📥 1k / ⭐ 3 / GGUF‑converted Japanese‑Chat‑Umievo‑itr001‑7b 模型，使用來自 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 資料構建，通過 llama.cpp 執行。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 1k / ⭐ 2 / DataPilot-ArrowPro-7B-RobinHood‑gguf 是 DataPilot 的 ArrowPro‑7B‑RobinHood 模型使用 imatrix 日本 LLM 數據集進行 gguf 格式轉換，已準備好與 llama.cpp 一起執行推理。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 311k / ⭐ 37 / 聚合自 2009‑2024 年的 NicoNico Live 評論日誌超過 150 GB，包括轉換前、轉換後及實時 NX‑Jikkyo 捕獲，並提供 API 以方便檢索歷史 TV‑broadcast 討論。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 6k / ⭐ 9 / Cauldron‑JA 是一套日本視覺‑語言資料集，包含 44 個子資料集，這些子資料集是使用 DeepL API 將 The Cauldron 翻譯而成，通過 HuggingFace’s datasets library 可取得，授權條件與原始資料集完全相同，提示（prompts）則以 CC‑BY‑4.0 授權釋出。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 4k / ⭐ 6 / Japanese Medical VQA 12M 是一個可商業使用的多模態資料集，包含超過1200萬張日文醫學影像及說明文字，來源自 Open‑PMC‑18M，採用 Parquet/Webdataset 格式，並包含原始及日文翻譯的影像、豐富的說明文字，以及使用 InternVL3.5、Qwen3‑30B 與 GPT‑oss 120B 產生的 VQA‑風格問答對。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 3k / ⭐ 112 / Nemotron‑Personas‑Japan是一個開源、CC BY 4.0資料集，提供高品質的合成生成日本人格資料——包含姓名、性別、年齡、背景、婚姻狀況、教育、職業和地理位置——基於真實世界的人口、地理和個性分佈設計，使用概率圖形模型和GPT‑OSS‑120B進行優化，以提升多樣性、減少偏見、避免模型崩潰，協助主權AI發展並支持商業使用。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 3k / ⭐ 19 / JMMMU 是一個日語多模態基準，已擴充十倍至 1,320 個文化多樣化問題 (720 個文化中立，600 個文化特定)，由母語專家翻譯，現在擁有公開排行榜。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 2k / ⭐ 10 / 一份托管於 Hugging Face 的 Reazon Speech v2 Japanese dataset 的鏡像，採用 CDLA‑Sharing‑1.0 發行，使用僅限於《Japanese Copyright Act Article 30‑4》，包含 4,096 個 16 kHz FLAC 音訊檔案以及對應的 TSV/CSV format 文字稿。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 99 / 一個包含 100 筆樣本的日本語 instruction‑tuning 評估資料集，內含標註任務——從摘要校正、數學推理到翻譯、創意生成及使用者意圖理解——設計用於手動或自動 5‑point rating 的 fine‑tuned models 評估。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 2k / ⭐ 28 / FineWeb2 Edu Japanese 交付約 120 million 高品質教育用日語文本（≈89.3 billion tokens）來自 FineWeb2，經 DeepSeek‑API classifier（score ≥ 2.5）過濾，使用 ModernBERT‑Ja‑130M 分詞，並包含小型 token 子集（≤512 tokens）。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 2k / ⭐ 16 / 日語及多語系 QA、NLI 與同義句資料集的目錄，說明各資料集的檢索或 QA 任務以及其授權規範（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 2k / ⭐ 112 / ReazonSpeech 是一個免費的 FLAC‑encoded 日語語音語料庫，附帶文字稿，提供五種規模，從 8.5 小時到 35,000 小時，可透過 Hugging Face 下載，採用 CDLA‑Sharing‑1.0 授權，並受限於日本版權法第 30‑4 條使用。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 2k / ⭐ 45 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小時的匿名化 1,033,142 對 eroge 音訊–轉錄配對 (大多為女性，NSFW)，MIT授權，用於學術研究。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEB 是一套日語文本嵌入基準，包含 5 個任務（聚類、分類、STS、檢索、重排序）與 28 個資料集，提供一行式評估腳本並邀請社群貢獻。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 2k / ⭐ 7 / JMedBench 是一個日本醫學領域 LLM 基準，包含 20 個資料集，涵蓋五個任務（MCQA、NER、STS 等），資料來源於 MedMCQA、PubMedQA、MMLU 及其他，每個資料集都有自己的授權，並附有註記指出翻譯可能存在偏差，需人工審核。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 1k / ⭐ 89 / 一個自動翻譯的日語版 databricks‑dolly‑15k dataset，採用 CC‑BY‑SA‑3.0 授權，最後更新於 2023‑05‑11。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 4 / JamC‑QA 是一個涵蓋八個日本文化與知識類別的雙語多選題基準測試，並以排行榜指標對比最先進模型。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 1k / ⭐ 34 / 重構後重新上傳 Galgame VisualNovel 資料集 (OOPPEENN/5669736E6F76656C5F44617461736574)，為了提高 Hugging Face 資料集載入效率，保留所有原始音訊 / 文字，並提供一段提取腳本，支援多種遊戲子集選項。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 1k / ⭐ 3 / 日本語指令資料集，含 632,636 個多回合樣本（約 6.35 億 tokens）以及 GPT‑OSS‑120b 理由痕跡，針對開放式、數學、寫作與多選題 (MCQA) 任務，在 135 個財務主題及 20 個一般主題中使用，旨在微調 LLM 在財務領域的推理能力。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 941 / ⭐ 47 / 更新了 JGLUE 數據集卡和載入腳本，適用於由 Yahoo Japan 和 Waseda University 創建的日本 NLP 基準，涵蓋文本分類（MARC‑ja、JCoLA）、句子對分類（JNLI）和 QA（JSQuAD、JCommonsenseQA），發布版本已在 GitHub 和 Hugging Face 上連結。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 913 / ⭐ 5 / Japanese JaQuAD（QG‑Bench 的子集）提供句子級和段落級資料，並以高亮顯示答案 token，用於訓練日語提問生成模型，評估指標包括 BLEU4、METEOR、ROUGE‑L、BERTScore 與 MoverScore。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 878 / ⭐ 11 / Range3/wiki40b‑ja 是 wiki40b 數據集的日文子集，作為由 Python 數據處理流程產生的三個 Parquet 檔案。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 809 / ⭐ 12 / JMMLU 是一個日本大型多任務語言理解基準，包含 7,536 個由教師精心編寫的問題，涵蓋 56 個科目，包含專業醫學、心理學、會計、哲學，以及多種高中學科。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 790 / ⭐ 40 / 使用者友善、去重的 CSV 資料集，包含來自 Aozora Bunko 的公有領域日語文本，已使用 globis‑org/aozorabunko‑extractor 處理並為現代日語機器學習用途做過清理。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 755 / ⭐ 24 / cc100-ja 是 cc100 資料集的日本語部分，提供為分片 Parquet 檔案。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 751 / ⭐ 135 / Japanese Anime Speech Dataset V2 提供 292,637 對乾淨的音頻-文本對，約 397.5 小時為 SFW，52.4 小時為 NSFW，存於 128‑kbps MP3 檔案中按安全性分割，專為訓練自動語音識別模型而設。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 686 / ⭐ 4 / JFWIR 是一個 64‑million‑pair 的日文資訊檢索資料集，由 fine‑web educational crawls 構建而成，提供每份文件七種查詢類型、hard negatives，並在 benchmark performance 上明顯優於此前的 prior baselines。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 673 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 資料集的一個 500 個樣本子集，授權為 CC BY 4.0，用於基準測試 EvoVLM‑JP‑v1‑7B。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 628 / ⭐ 16 / 日本語 Alpaca 資料，來源於 masa3141 的日本語 Alpaca‑LoRA 工作，並引用原始倉庫以供進一步細節參考。
 * [KokushiMD-10](https://huggingface.co/datasets/humanalysis-square/KokushiMD-10) - 📥 599 / ⭐ 7 / KokushiMD‑10 是一個多語言基準，涵蓋日本十項國家醫療保健執照考試，提供日語、英語及混合語言版本的文本與圖像多選題、計算題與填空題，覆蓋十個職業，每題皆附有專家推理說明。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 584 / ⭐ 5 / JAMMEval 是七個日本 VQA 數據集的蒸餾基準，經過兩輪人工註釋以消除歧義和非視覺問題，提供對多模態日本任務的視覺‑語言模型可靠評估。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 556 / ⭐ 2 / 大型壓縮的 JSON‑Lines 數據集，包含匿名 2ch.sc/2ch.net 論壇討論串，包含討論串 ID、標題、版面與區域資訊、回覆數量，以及完整的貼文元資料（作者、郵件、日期、內容）。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 556 / ⭐ 2 / 擴大資料受限日語 LLM 的預訓練語料庫，包含天然日語/英語網路資料集（9B‑token JA‑WEB‑9B、63B‑token EN‑WEB‑63B/JA‑WEB‑63B）以及合成資料集（Qwen3‑14B、JA‑PARAPHRASE‑63B、JA‑INSTRUCT‑63B、JA‑TRANSLATE‑63B），用於 EACL 2026 研究。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 538 / ⭐ 13 / EDINET‑Bench 是一個日本金融基準，評估 LLM 在會計欺詐檢測、盈餘預測以及產業預測等任務，使用十年的 EDINET‑API 公開報告。提供構建與評估代碼，資料集已重新授權為 PDL 1.0。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 528 / ⭐ 142 / 日語說明式對話資料集，用於微調 LLM（例如 LoRA），9M+ 範例，最近更新為去除授權的 Alpaca 數據，清理 Wikipedia 和 ALT 輸出，並以 CC‑BY‑SA 4.0 發佈。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 516 / ⭐ 5 / STAIR‑Captions 在 2017 年發布，提供 820,310 條日語字幕，用於字幕生成、多模態檢索和圖像生成，並帶有詳細標註、元資料以及 Creative Commons BY‑4.0 license。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 492 / ⭐ 11 / 一個高品質的合成日語數學題目資料集，具有已驗證的鏈式思考推理，透過 Qwen2‑7B‑Instruct 將 PRM800K 和 GSM8K 進行翻譯並篩選正確性後構建，可透過 Hugging Face datasets library 獲取。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 477 / ⭐ 16 / Reazon Speech v2 數據集的鏡像：3,674 個去噪語音檔經 UVR 於 8 台 A800 GPU 上處理，耗時 10 天，由 Stardust‑minus 完成，並以 CDLA‑Sharing‑1.0 釋出且未附文字稿。
 * [AItuber-Personas-Japan](https://huggingface.co/datasets/DataPilot/AItuber-Personas-Japan) - 📥 472 / ⭐ 28 / 一個由 Kimi‑K2.5 透過 SDG‑LOOM 管線生成的合成 195 條 AI‑VTuber 人格資料集，提供概念文件、系統提示及主題清單，針對以六個種子參數（類型、個性、年齡、性別表達、視覺主題、語言風格）定義的角色，跨約 25 種類型和 20 種個性類型，授權為 ODC‑BY。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 467 / ⭐ 22 / 一個日本網路集合，包含56 million文件、110 B字元以及249 million圖像，這些資料被用於訓練大型視覺語言模型——提供momiji_generator進行資料填充、OBELICS‑style視覺化，以及一個範例模型（Heron‑NVILA‑Lite）。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 429 / ⭐ 9 / JMMMU‑Pro 是一個日本的多模態基準，通過 Vibe Construction 建立——結合生成式建模和人工驗證——以產生低成本、高品質的 image‑QA 數據，揭示開源 LMMs 的缺陷並指引未來 VQA 研究。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 411 / ⭐ 6 / 日文 MC4 資料集卡片 (mc4-ja)
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 400 / ⭐ 8 / Rakuda 提供 40 個日文問題—針對歷史、社會與政府的開放式題目，以及針對地理的專門題目—作為基準測試日本 AI 助手的資料，與 vicuna‑eval 相似，並可透過 `datasets.load_dataset` 載入。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 393 / ⭐ 6 / Range3 的 wikipedia-ja-20230101 存儲庫提供只包含日文維基百科文本的 Parquet 檔案，這些文本是從完整的維基百科資料集提取並使用 Python 程式碼生成。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 355 / ⭐ 32 / 一個 409 小時的日本 eroge 語音資料集，經 2-pass loudnorm 處理（‑23 LUFS、‑1 dB peak、11 LRA），由 litagin/anime-whisper 轉錄，已匿名化，存儲為 WebDataset（FLAC、JSON、TXT），主要包含女性聲音，可能存在 AI 轉錄錯誤，並以 MIT‑licensed 供學術研究。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 353 / ⭐ 44 / Galgame_Speech_ASR_16kHz 是一個 16 kHz ASR 資料集，包含 3.75 百萬對（≈5,354 h），由 Galgame_Dataset 派生，採 GPL v3.0 授權，禁止商業使用，且任何訓練出來的模型必須開源（引用可選）。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 352 / ⭐ 13 / Dataset 卡片（針對 “wikipedia-ja-20230720” 日文維基百科快照）
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 347 / ⭐ 5 / JAQKET 是一個來自 Wikipedia 的日語開放域問答資料集，提供版本 1.0，包含多選測驗題（13,061 個訓練例子，271 個驗證例子）以及版本 2.0，只包含需要抽取答案的提問提示（2,154 個訓練例子，1,164 個驗證例子），旨在促進問答系統研究。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 341 / ⭐ 6 / Japanese XL‑Sum 子集經 PaLM‑2 15‑gram 重疊過濾，包含 4,215 個訓練、758 個驗證以及 766 個測試範例。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 336 / ⭐ 10 / JA‑Multi‑Image‑VQA 是包含 39 張圖片、55 個題目的資料集，擁有手工製作的日語 Q&A 用於多圖像 VQA，透過 load_dataset 訪問，文本授權為 Apache 2.0（圖片受限）。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 312 / ⭐ 17 / Galgame_Speech_SER_16kHz 是一個 3.7 百萬檔（5,353 小時、104 GB）情感語音資料集，來源於 Galgame_Speech_ASR_16kHz，經本地 LLM 標註，依 GNU GPL v3.0 發佈，禁止商業使用，且訓練於此的模型必須開源，且不強制要求引用。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 312 / ⭐ 2 / 266 小時日本語音訊資料集，來自 Emilia collection，已由 Facebook Audio Aesthetics 前置篩選，並藉 Scribe v1/ElevenLabs STT 進行分類，資料已托管於 Hugging Face，並可於 Discord 進行協作。
 * [image-text-pairs-ja-cc0-2](https://huggingface.co/datasets/alfredplpl/image-text-pairs-ja-cc0-2) - 📥 289 / ⭐ 2 / 一個 CC‑0 的日語文字‑圖像資料集，透過 GPT‑OSS‑20B 從約 80,000 個單詞/短句建立，使用 Pillow/Python 與 Noto Sans JP 字體渲染成 1 M 與 100 k 張圖像。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 284 / ⭐ 3 / Japanese Explainable Multi‑hop Question Answering dataset 特色為問題、答案與逐步推導，連結 Wikipedia 文章，並更新推導格式及多個版本發布。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 284 / ⭐ 4 / 提供一個日文搜尋/問答資料集，包含每個查詢的分數，這些分數由五個多語言／日文再排序器計算（如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base），並包括每個查詢大約 200 篇正面與負面範例文件的平均分數。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 278 / ⭐ 148 / Japanese Anime Speech Dataset 提供 73,004 對音頻-文字對（共 110 小時，從 V1 演進至 V5），用於提升 ASR 模型（如 OpenAI 的 Whisper），在開放授權下可供任何使用，若能標明來源將不勝感激。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 271 / ⭐ 14 / 一份採用 CC‑BY‑SA 3.0 授權的日文實體抽取資料集，來源自維基百科，存放於 https://github.com/stockmarkteam/ner-wikipedia-dataset/，並由 Stockmark Inc. 開發。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 269 / ⭐ 15 / 一個簡易的 Zundamon 角色設定資料集—由線上來源及管理數據編輯—用於測試 character‑LLMs，提供於 zmnjp.jsonl 與 zmn.jsonl 格式，並依指定授權提供。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 269 / ⭐ 4 / 這份 20,800 檔案的 WAV 數據集包含 195 位日本 AItuber 人格──其中包括參考、原始、描述性和情感語句──並附帶詳細的人格與聲音元資料，準備好透過數據科學 API 進行檢索。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 260 / ⭐ 5 / 這個儲存庫包含一位81歲日本女性的語音資料庫——原始與降噪的WAV檔案、音素及假名標籤——可透過 Google Drive 連結取得，免費供研究與商業語音合成使用，需署名；但禁止直接檔案連結或色情用途。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 259 / ⭐ 51 / AnswerCarefully Dataset 提供日語及多語言資料，用於商業或非商業 LLM 安全增強；禁止任何其他用途——包括安全繞過；允許帶歸屬的衍生作品；並附帶創作者對損害或服務變更之非責任免責聲明。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 251 / ⭐ 7 / JHumanEval 是手工翻譯的日本版 HumanEval benchmark，提供 164 個 Python 程式設計問題，並提供對應的英文與日文註解，旨在評估 Japanese-LLM 程式產生，同時保留原始英文錯誤。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 251 / ⭐ 12 / LLM‑jp 提供一個日語指令調校數據集，來自 oasst2 的英語子集經 DeepL 翻譯（源自 kunishou/oasst2‑135k‑ja）並由 Kiyomaru 與 Kodama 編譯。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 250 / ⭐ 3 / 2010 年的日本網路語料庫已上傳至 HuggingFace，並按 2009 年版權改革為研究授權，包含自動帶標點的文本，這些文本來自形態學解析和轉換腳本。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 239 / ⭐ 16 / 一個 1.9 億對 JSONL 資料集，用於日語假名至漢字轉換，為 zenz‑v2.5 medium、small 與 xsmall 模型提供基礎，並包含 AJIMEE‑Bench 評估語料庫。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 236 / ⭐ 17 / oasst1‑21k‑ja 是一個由 DeepL 從英文 OASST1 子集衍生而來的日語指令調整資料集，通過日本的 LLM‑jp 合作項目創建；如需聯繫，請發送電子郵件至 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 以及 Okamoto。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 228 / ⭐ 2 / JCommonsenseQA 是一個日語多選題常識推理資料集——CommonsenseQA 的改編版——授權為 CC BY‑SA 4.0，並以 doi:10.5715/jnlp.30.63 引用。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 225 / ⭐ 3 / BBH‑ja 提供 BIG‑Bench Hard 資料集的日文翻譯，提供 JSON‑L（輸入、正確目標）格式的評估問題，以及 YAML（輸入、目標）格式的 Chain‑of‑Thought 提示，翻譯使用 PLaMo 模型。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 192 / ⭐ 12 / JaQuAD 是 2022 年的日本 QA 資料集，包含 39,696 對 SQuAD‑style 抽取式問答對，來源於 Wikipedia，總量 73.2 MB，當使用 BERT‑Japanese 微調時，F1 分數達 78.92 %（EM 63.38 %）。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 187 / ⭐ 27 / WRIME 數據集是一個日本語收藏，包含 42,200 篇文章，已用 Plutchik 的八種情緒為作者、三位讀者以及他們的平均值進行標註，並結構為 40k‑train、1.2k‑validation、2k‑test 的分割，供情感分析任務使用。
 * [MGSM_ja](https://huggingface.co/datasets/sbintuitions/MGSM_ja) - 📥 185 / ⭐ 2 / 一個可公開重現的日本子集，屬於 MGSM 多語言思考鏈數據集，在 Hugging Face 上克隆，採用 Creative Commons BY‑SA 4.0 許可證，包含問題、答案、答案編號和等式求解欄位。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 185 / ⭐ 4 / 來自 Fate/Stay Night 角色「Emilia」的對話與傳說資料集，格式化用於訓練與評估對話語言模型。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 181 / ⭐ 33 / Syosetu711K 是一個日本資料集，於 2023 年 3 月 26‑27 日從小説家になろう抓取約 711,700 本小說，提供全文和元資料（標題、作者、NCode、簡介等）供無監督文本生成和分類任務使用。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 181 / ⭐ 7 / llm‑jp‑instructions 是一個手動編輯的日語指示資料集 (v1.0)，提供 train、dev 和 test 分割，可透過 load_dataset 存取。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 166 / ⭐ 21 / 使用英文提示生成的 AI 動漫插圖，以及來自 Phi‑3 Vision 的字幕（英文與日文），已釋出至公共領域供免費使用。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 158 / ⭐ 42 / 在評估 LLMs 將日語視覺小說準確翻譯成英文的表現時，VNTL 領域排行榜以 256 個參考翻譯的餘弦相似度評估（同時報告 chrF 但未排名），並公布初步結果，該結果優於 Sugoi Translator、Google Translate、Papago 與 Alibaba Translate 等工具。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 154 / ⭐ 3 / 資料集卡為「Introduction to Large‑Scale LLM II」一書中使用的 ja‑vicuna‑qa‑benchmark，並由 llm‑jp‑eval 為跨資料集的日語 LLM 評估所創建（Apache 2.0）。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 150 / ⭐ 21 / 這是一份 SNOW T15/T23 Japanese simplification corpus 的資料集卡片，包含 50 k 手動對齊的原始簡化日語 (≤2 k‑word vocab) 與 English translation records，以及 35 k 擴充集，供日英文本簡化與翻譯使用。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 150 / ⭐ 7 / Livedoor News Corpus 提供一套日語新聞文章數據集，分為 5 894 個訓練、737 個驗證和 736 個測試實例，已去除 HTML 標籤並以 Creative Commons Attribution‑NoDerivs 授權釋出。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 148 / ⭐ 6 / 將日文資料集轉換為 SentenceTransformers 友好的欄位，並根據 Rerank 分數（≥0.7 為正面，≤0.3 為負面）篩選範例，從多個 HuggingFace 來源擷取，以支援對比學習，同時遵守原始授權。
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 148 / ⭐ 2 / Makise Kurisu VN 的對話，使用 Whisper Large‑V2 從影片轉錄，並以 pydub 分割成片段，尚未清理且可能包含錯誤，旨在用於 TTS 模型訓練，並非作者擁有。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 146 / ⭐ 9 / 一個由 23,000,000 件個人收集的日本網路小說組成的資料集，總字數為 80,850,000,000 個字元，只允許合法機器學習用途，需提交詳細存取申請。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 142 / ⭐ 3 / 一個包含 64,139 項日文姓名的資料集，已按生物性別標記——採用漢字、平假名與羅馬拼音——其 44.9k 訓練集、6.41k 驗證集與 12.8k 測試集的分割方式獲得 ISDA’23 的接受。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 142 / ⭐ 7 / 由 VOICEVOX 與 ITA、Tsukuyomi‑chan、ROHAN 資料庫所建立的人工語音資料集，包含 445,793 個 WAV 檔案，總計 577 小時 51 分鐘 23 秒。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 141 / ⭐ 15 / JGLUE 資料集卡片，使用於《Large Language Model Introduction》一書，來源自原始倉庫，程式碼採用 CC BY‑SA 4.0 許可，資料受發行者授權，引用 Kurihara & Kawahara（以日文）並建立於 Shunsuke Kitada 的倉庫。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 140 / ⭐ 18 / Databricks‑dolly‑15k‑ja 數據集是一個 DeepL 翻譯的日文版本，為指令微調而由日本 LLM‑jp 專案創建，作者為 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 與 Takumi Okamoto。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 139 / ⭐ 18 / 部分 *Project Sekai* 聲樂曲目資料集，專為草薙寧々（來源 CV Machico）設計，包含 nene_org.txt 標籤檔，計畫擴充並標準化資料，並呼籲收藏此 repo、分享想法及加入 QQ 群，以取得完整收藏。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 139 / ⭐ 3 / 量化語音輸入與文字輸入（針對語音語言模型）的智力差距的一個資料集，由從 Elyza‑tasks‑100、M‑IFEval 和 JamC‑QA 基準中合成的音訊組成，分為四個子集；文字使用 CC‑BY‑SA 4.0 授權，音訊僅允許非營利、非再分發使用。
 * [japanese-stackexchange](https://huggingface.co/datasets/p1atdev/japanese-stackexchange) - 📥 135 / ⭐ 3 / 一個以英語為語言的日語 Stack Exchange 問答資料集，從網站的匯出資料中提取並處理，提供預設與扁平化子集，可透過 Hugging Face datasets 載入，授權為 CC BY‑SA 4.0。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 135 / ⭐ 20 / 一個日語 QA 數據集，用於評估 Retrieval‑Augmented Generation (RAG)，由 JAQKET 題目與 Wikipedia 文章構建，帶有金鑰檢索相關性標簽，已於 HuggingFace 和 GitHub 發布，主要以 nDCG@10 作為評分指標。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 132 / ⭐ 9 / 此為 llm-book/wrime‑sentiment 的資料集卡，提供一個由 WRIME 衍生的二元日語情感分析集合，根據 Avg. Readers_Sentiment 標記為正向或負向（可選擇包含中性案例），並作為《Introduction to Large Language Models》一書的樣本資料。
 * [oscor-2301-ja-text-content](https://huggingface.co/datasets/ayousanz/oscor-2301-ja-text-content) - 📥 132 / ⭐ 2 / 從 OSCOR‑2301‑ja JSON 檔案中擷取「content」欄位文字，並附上一段 Python 腳本，將這些值從指定資料夾中的每一個 JSON 拉取。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 126 / ⭐ 3 / 日文維基百科句子被轉換為各種嵌入，並建立 FAISS 索引，提供 Hugging Face Space 的演示、轉換腳本，以及對搜尋、問答和 OpenAI text‑embedding‑3‑small 在 RAG 中的評估；嵌入採用 OpenAI 授權，其他則採用 CC‑BY‑SA‑4.0。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 124 / ⭐ 10 / 一個日文對英文平行語料庫，將 llm‑jp‑corpus‑v3 的 kaken 子集翻譯成英文，使用 Qwen/Qwen2.5‑32B‑Instruct，特點為自訂翻譯欄位，並以 CC‑BY‑4.0 授權。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 122 / ⭐ 4 / 「Japanese RAG Generator Benchmark (J‑RAGBench)」供應一份多分類 QA 數據集—涵蓋 Integration、Reasoning、Logical、Table 與 Abstention—旨在評估日文 RAG 生成器，並由人力與 GPT‑4.1 建構，且以 CC BY‑SA 4.0 授權發布。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 120 / ⭐ 2 / COVID‑19 日本 Twitter 數據集提供日本推文 ID 與評估碼 (63–68)，指出 COVID‑19 的相關性以及事實／意見狀態，從而促進文本分類研究。
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 112 / ⭐ 23 / RealPersonaChat 是一個包含 14,000 次發言的日本對話語料庫，將對話記錄與說話者個性、BigFive 人格分數、人口統計資料以及評分（1–5）相關聯，透過 Hugging Face 的 `load_dataset` 可存取，但須嚴格遵守隱私與非冒名作業合規。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 111 / ⭐ 5 / 來自 joujiboi/japanese‑anime‑speech‑v2 數據集的一個子集。
 * [JA_audio_JA_text_180k_samples](https://huggingface.co/datasets/Sin2pi/JA_audio_JA_text_180k_samples) - 📥 110 / ⭐ 9 / MeCab‑IPADIC‑Neologd 儲存庫中的「Regexp.ja」Wiki 頁面說明了用於去除不必要標點並正規化文字的日文正則表達式規則。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 109 / ⭐ 32 / 一個用於指令‑回覆微調（例如通過 LoRA）的日語聊天數據集，來源於 llm‑japanese‑dataset，剔除日英翻譯示例，提供 1.8–2.5 million 條目，跨版本發布，並以 CC‑BY‑SA 4.0 授權，引用 DOI 10.1109/BigData59044.2023.10386605。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 108 / ⭐ 33 / 提供日文 RAG 基準，涵蓋金融、電訊、製造、公共、零售五大產業領域，透過發布資料集、自動評估框架，以及比較結果，例如 Claude 3.5‑Sonnet、GPT‑4o 等模型。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 101 / ⭐ 5 / J‑HARD‑TTS‑Eval 對日本語自回歸 TTS 模型進行評估，測試短序列穩定性、重複、押韻和延續等失敗情況，並提供帶有提示音頻和文本的數據集，透過 Hugging Face 可載入。
