# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專門收錄日語NLP相關的Python函式庫、LLM、詞典和語料庫資源的精選列表。
本頁面列出了Hugging Face上可用的日語NLP專用模型和資料集。目前包含203個模型和199個資料集。

_更新於2026年5月19日_

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
   * [text-classification](#text-classification)
   * [token-classification](#token-classification)
   * [audio-to-audio](#audio-to-audio)
   * [text-to-speech](#text-to-speech)
   * [image-text-to-text](#image-text-to-text)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | 模型名稱 | Downloads | Likes | 類別 |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 1M | ⭐ 57 | automatic-speech-recognition |
| 2 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 981k | ⭐ 14 | translation |
| 3 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 394k | ⭐ 74 | sentence-similarity |
| 4 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 346k | ⭐ 76 | fill-mask |
| 5 | [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) | 📥 317k | ⭐ 11 | feature-extraction |
| 6 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 281k | ⭐ 171 | image-to-text |
| 7 | [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) | 📥 231k | ⭐ 5 | text-ranking |
| 8 | [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 📥 229k | ⭐ 21 | text-generation |
| 9 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 225k | ⭐ 11 | translation |
| 10 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 200k | ⭐ 41 | fill-mask |
| 11 | [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) | 📥 189k | ⭐ 100 | automatic-speech-recognition |
| 12 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 153k | ⭐ 15 | text-generation |
| 13 | [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) | 📥 142k | ⭐ 39 | fill-mask |
| 14 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 142k | ⭐ 9 | sentence-similarity |
| 15 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 129k | ⭐ 11 | others |
| 16 | [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) | 📥 119k | ⭐ 8 | fill-mask |
| 17 | [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) | 📥 112k | ⭐ 136 | text-generation |
| 18 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 91k | ⭐ 59 | text-generation |
| 19 | [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) | 📥 73k | ⭐ 14 | others |
| 20 | [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) | 📥 65k | ⭐ 63 | others |

### Datasets-ranking

| # | 資料集名稱 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 3M | ⭐ 44 |
| 2 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 19k | ⭐ 9 |
| 3 | [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) | 📥 13k | ⭐ 4 |
| 4 | [WAON](https://huggingface.co/datasets/speed/WAON) | 📥 6k | ⭐ 2 |
| 5 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 6k | ⭐ 16 |
| 6 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 5k | ⭐ 7 |
| 7 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 4k | ⭐ 6 |
| 8 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 4k | ⭐ 18 |
| 9 | [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) | 📥 4k | ⭐ 6 |
| 10 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 4k | ⭐ 117 |
| 11 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 3k | ⭐ 139 |
| 12 | [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) | 📥 3k | ⭐ 5 |
| 13 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 3k | ⭐ 99 |
| 14 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 3k | ⭐ 11 |
| 15 | [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) | 📥 2k | ⭐ 10 |
| 16 | [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) | 📥 2k | ⭐ 4 |
| 17 | [jawiki](https://huggingface.co/datasets/hpprc/jawiki) | 📥 2k | ⭐ 18 |
| 18 | [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) | 📥 2k | ⭐ 2 |
| 19 | [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) | 📥 2k | ⭐ 5 |
| 20 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 2k | ⭐ 43 |

## Models
### text-generation
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 229k / ⭐ 21 / OpenCALM 是由 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 之下發佈的一套僅解碼器的日語 transformer 語言模型（160 M–6.8 B 參數），經日本維基百科與 Common Crawl 訓練，可透過 Hugging Face 的 torch‑transformers 使用。
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 153k / ⭐ 15 / 一個 12 層、768 隱藏層的日本 GPT‑NeoX 模型，訓練於 CC‑100、C4 和 Wikipedia，兼容 Huggingface，並可選擇使用一個玩具前綴調優權重，使每句結尾強制出現笑臉表情符號。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 112k / ⭐ 136 / 一個九十億參數的日文優化 LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，於 2024 年 9 月以前的資料進行訓練，採用混合的 Mamba‑2/MLP/4‑layer‑attention 架構，並在 Nemotron‑Personas‑Japan 工具呼叫資料集中進行微調，可選擇在產生最終答案前生成可控的推理回溯，且可商業使用。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 91k / ⭐ 59 / 一個 2.7‑B 參數的日語 GPT‑NeoX 模型，由 ABEJA Inc 在日語 CC‑100 與 OSCAR 上訓練，可透過 Hugging Face Transformers pipelines 或 PyTorch 使用，並以 MIT 授權釋出。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 46k / ⭐ 7 / 已預訓練的 TinyLlama，日語版本（≈50k 步），建立於約3B OSCAR/mC4 代幣上，可透過 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 與 Renju Aoki 製作。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 38k / ⭐ 5 / LLM‑jp‑3‑150m — 來自日本情報學研究院 LLM 研發中心的 150M 參數日語語言模型，已以 Hugging Face Transformers 格式發佈，需安裝 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，並以日語維基百科、Common Crawl、WARP/PDF、WARP/HTML 以及 Kaken 數據，使用 unigram byte‑fallback tokenizer 進行預訓練。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 23k / ⭐ 18 / 以 Shisa 7B 數據微調了 Japanese Stable LM Base Gamma 7B，並在 JA MT‑Bench 上取得優異成績。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 23k / ⭐ 37 / 提供 NII 的 8B 參數 LLM‑jp‑4‑8b‑thinking 日文語言模型，已經以 pre/​mid‑training 訓練並通過 SFT/DPO 對齊，已準備好與 torch‑transformers 一起使用，並附有詳細的 cookbook 指南。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 13k / ⭐ 7 / llm‑jp‑4‑8b‑instruct 是 NII 的 LLM‑jp‑4 系列 4.1 B 參數的日語 LLM，先在大規模語料庫上進行預訓練，接著僅用監督式指令資料微調（不使用 DPO/REINFORCE），並附有類似食譜風格的使用指引與 byte‑fallback unigram tokenizer。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 10k / ⭐ 48 / 一個日語持續預訓練的 Mistral‑Nemo 模型（Mistral‑Nemo‑Japanese‑Instruct‑2408），基於 mistralai/Mistral‑Nemo‑Instruct‑2407 建構，可透過 transformers 使用裝置映射與 ChatML 版面提示，並由 Ryosuke Ishigami 以 Apache‑2.0 授權發布。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 9k / ⭐ 21 / Llama3 Swallow 是一款日本增強版 Meta Llama 3 系列，於 2024 年 7 月 1 日發布，提供 8B 與 70B 兩種版本，包含 Instruct 與 chat 形式，並使用 SFT 與 Chat Vector 在 Megatron‑LM 上微調，並在關鍵的日本 NLP 任務上進行基準測試。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 實驗性日本模型，透過採用 chat‑vector 方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 與 Meta‑Llama‑3‑8B‑Instruct 之間的差異，升樣後應用於 Meta‑Llama‑3‑70B‑Instruct，顯示變化不大，並計畫未來擴充。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 8k / ⭐ 10 / 此存儲庫提供 GGUF 格式、量化的模型檔，適用於 Stability AI 的日文 StableLM Instruct Gamma 7B，該模型由 Massed Compute 硬體製成，並屬於 TheBloke 的 a16z 資金支持的 LLM 專案的一部分。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 8k / ⭐ 85 / Rinna 的 24 層、1024 隱藏單元的日本 GPT‑2‑medium 模型，使用 CC‑100 和 Wikipedia 進行訓練，採用 SentencePiece 分詞，已在 rinna/japanese‑pretrained‑models repo 中提供（MIT‑licensed，於 2021 年 4 月 7 日發布，於 2021 年 8 月 25 日更新）。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 6k / ⭐ 1 / 日語增強、指令微調的 Gemma‑2 模型，建構於 Llama（2b/9b/27b pre‑train 和 instruction 版本），於 2025 年 5 月 19 日發布，並可於 HuggingFace 與 Swallow team 的網站上取得。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 6k / ⭐ 24 / Llama 3.1 Swallow 是一系列經過日本優化的 8B/70B Llama 3.1 模型，透過持續預訓練和日本專用說明微調進行訓練，最新的 8B‑Instruct‑v0.3 在日本 MT‑Bench 上取得了最先進的成果。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 6k / ⭐ 148 / Llama‑3‑ELYZA‑JP‑8B 是 ELYZA 推出的日語改良版，8 億參數的 Llama 3 模型，已在 Meta‑Llama‑3‑8B‑Instruct 上為日語進行微調。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 6k / ⭐ 6 / 一個存儲庫托管國立情報學研究院 LLM 研發中心的 8.6 B‑parameter llm‑jp‑4‑8b‑base transformer，該模型經由預訓練與中訓練，隨後進行監督式微調與直接優先權優化（未使用強化學習），並提供 PyTorch‑transformers 使用指南。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 5k / ⭐ 27 / rinna 的日語 GPT‑2 small 為 12 層、768 隱藏單元的 transformer，訓練於日語 CC‑100 和 Wikipedia，使用 SentencePiece 進行分詞，於 2021 年 8 月 25 日以 MIT 版發布（Hugging Face：rinna/japanese‑gpt2‑small，詳見 https://arxiv.org/abs/2404.01657）。
 * [Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF) - 📥 5k / ⭐ 1 / 針對日語的 imatrix GGUF 量化的已消融 Qwen3.6‑35B‑A3B‑uncensored‑heretic 模型，以日語文本校準以提升日語生成品質，但安全過濾器已被顯著削弱。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 4k / ⭐ 108 / 一個 1.3‑B‑parameter、24‑layer transformer GPT‑1B，在 Japanese C4、CC‑100 以及 Wikipedia 上訓練，於 2022 年 1 月 26 日由 rinna Co. 發布，並以 MIT license 供使用。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 4k / ⭐ 20 / 提供由 NII 出品的 1.8 B 參數 llm‑jp‑3.1‑1.8b‑instruct4 日語指令調校模型，兼容 Hugging Face Transformers 及 Torch ≥ 2.3.0，包含預訓練與微調檢查點及使用示例。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 3k / ⭐ 37 / 提供由 SB Intuitions 推出的自回歸日語語言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已與其他模型進行基準測試，且附帶示例使用腳本，並註明安全訓練有限。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 3k / ⭐ 29 / 一個32十億參數的日語 transformer LLM (llm‑jp‑4‑32b‑a3b‑thinking)，來自國立情報學研究所 (National Institute of Informatics)，預訓練並通過有監督微調與直接偏好優化進行調整——未使用強化學習——採用 unigram byte‑fallback tokenizer。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 3k / ⭐ 16 / 一個 6 層、512 隱藏單元的 transformer，名為 Japanese GPT‑2 xSmall，訓練於日本 CC‑100 與 Wikipedia 並使用 SentencePiece tokenization；於 2021 年 8 月 25 日以 MIT 授權發布，並託管於 Hugging Face（rinna/japanese‑gpt2‑xsmall），在 arXiv 2404.01657 中被引用。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 3k / ⭐ 20 / GPT‑OSS‑Swallow v0.1 提供 20B 及 120B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，能在數學與編程任務上匹敵或超越 GPT‑OSS，於 2026 年 2 月發布，包含四種 SFT/RL 變體與即將推出的量化版本。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 3k / ⭐ 16 / 一套日本大型語言模型（1.8 b 至 172 b beta1，含 instruct 變體）來自 NII 研究發展中心，以 Hugging Face Transformers 格式打包，並在混合的日文、英文以及網路語料上預訓練，總 token 數量超過 1 trillion，需至少 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 3k / ⭐ 146 / LFM2.5‑1.2B‑JP 是一款為日語優化的聊天模型，在日語知識和指令遵循方面優於 LFM2，支援 LoRA 的微調、使用 Transformers、vLLM、llama.cpp 進行推論，並達到 50.7 JMMLU、58.1 M‑IFEval 和 56.0 GSM8K 分數。
 * [shisa-v2.1-qwen3-8b](https://huggingface.co/shisa-ai/shisa-v2.1-qwen3-8b) - 📥 3k / ⭐ 8 / Shisa V2.1推出升級的日英雙語聊天模型——擴建自更新的資料集，並進行強化的指令、翻譯與禮貌微調——涵蓋 Llama 3.2、Qwen 3‑8B、UnPhi‑4 14B 等變體，帶來顯著的性能提升。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 3k / ⭐ 15 / SB Intuitions 的 Sarashina2.2‑0.5B instruct v0.1 是一個 5 億參數的日語自回歸模型，在日語和英語 MT 基準上表現優秀，並可透過 torch-transformers 載入。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 3k / ⭐ 57 / TinySwallow‑1.5B‑Instruct 是一個 1.5 B 日語指令調校的自回歸語言模型，經由 TAID 從 Qwen2.5‑32B‑Instruct 蒸餾，僅供研究使用。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 2k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 與 Swallow Team 所開發的一款緊湊型日語指令跟隨語言模型，採用 Qwen2.5‑32B‑Instruct 的 TAID 蒸餾，並進一步於日語文本上進行預訓練，僅以 Apache 2.0 授權釋出，僅供研究用途。
 * [llm-jp-3.1-1.8b](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b) - 📥 2k / ⭐ 13 / llm‑jp‑3.1‑1.8b 是來自 NII 的大型語言模型研發中心的 1.8 億參數日語 LLM，作為 Hugging Face 檢查點發佈（torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5），在倉庫中提供完整模型規格、分詞器和預訓練細節。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 2k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter 日本語擴展版本，進一步針對日本語語言任務進行預訓練，並提供 base、instruct、fast 和 fast‑instruct 變體，由 ELYZA 團隊在 Llama 2 Community License 下維護。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 2k / ⭐ 9 / Qwen3‑Swallow v0.2 提供日英語 LLM（30B‑A3B 和 32B），採用 CPT、SFT 與 RLVR 訓練，保持強大的數學、程式編寫與推理能力，已發布九個模型及 AWQ‑quantized 變體。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 2k / ⭐ 19 / Llama 3.1 Swallow 是一組 8‑B 和 70‑B 模型，繼續對 Meta 的 Llama 3.1 進行預訓練以提升日語表現，然後在合成日語數據上進行 instruction‑fine‑tune，提供多個已發佈的變體，具有與 gemma‑3‑27b‑it 相當的對話行為改進。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 2k / ⭐ 20 / OpenCALM 是 CyberAgent 發布的一系列日語僅解碼器 Transformer 語言模型（參數 160 M–6.8 B），訓練於日語維基百科和 Common Crawl，並以 CC BY‑SA 4.0 授權發行。
 * [gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - 📥 2k / ⭐ 18 / 由 ABEJA, Inc. 在日本 CC‑100、Wikipedia、OSCAR 上訓練的大型日語 GPT‑2 模型，使用 sentencepiece 進行分詞，可透過 Hugging Face transformers 在 PyTorch 或 TensorFlow 使用，並採用 MIT 授權。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 2k / ⭐ 17 / TokyoTech‑LLM 倉庫提供了 Swallow Llama‑2 系列的 LLaMA‑2 模型，這些模型已加入日文資料，涵蓋 7B、13B 與 70B 變體，並包含 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以來發佈的 7B Plus 版本。
 * [sarashina2.2-1b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1) - 📥 2k / ⭐ 16 / 本倉庫托管 SB Intuitions 的 1 B‑參數自回歸式日本指令模型 sarashina2.2‑1b‑instruct‑v0.1，與其他日本‑BERT 進行日本與英語 MT 及指令任務的基準測試，提供一段 torch‑transformer 使用範例，並警告安全訓練有限。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 2k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27‑B 參數擴充，已在包含 instruct 與 fast 變體的日文資料上進行預訓練，可透過 Hugging Face Transformers 使用。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 2k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一個 13‑B 的、已經進行指令預訓練的日語語言模型，由 NII 的 R&D Center 開發，並以 Hugging‑Face Transformers 的 checkpoint 形式發布，使用 UNIGRAM‑byte‑fallback tokenizer。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 2k / ⭐ 1 / Qwen3‑Swallow v0.2 提供 30‑B 和 32‑B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，提升日語準確度、翻譯、數學與編碼能力，以達到或超越原始 Qwen3，提供九種模型（CPT、SFT、RL）以及 AWQ‑quantized 版本，並同時發布 GPT‑OSS‑Swallow。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 2k / ⭐ 29 / LFM2.5‑1.2B‑JP 是一個 1.2B 參數的日語文本生成模型，基於 LFM2.5 混合架構構建，優化用於生成和完成任務，托管於 Hugging Face 並可通過 llama.cpp 運行。
 * [gpt2-large-japanese-char](https://huggingface.co/ku-nlp/gpt2-large-japanese-char) - 📥 2k / ⭐ 5 / 日文字符級 GPT‑2 Large（717 M參數）在約171 GB的日本維基百科、CC‑100和OSCAR資料上預訓練，使用NVIDIA A100以AdamW優化器與線性學習率計畫訓練了約8個月，可透過Hugging Face pipelines 進行文字生成或特徵提取。
 * [gpt2-japanese-lyric-small](https://huggingface.co/skytnt/gpt2-japanese-lyric-small) - 📥 1k / ⭐ 3 / 日本 GPT‑2 歌詞生成模型，訓練於 143,587 首 uta‑net 歌曲，並透過網頁 Demo 與 Torch/Transformers 使用範例提供。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 1k / ⭐ 26 / 日本語 3.6B 參數 GPT‑NeoX 模型經過調校以符合指令追蹤 (SFT‑v2)，在 100 個提示上與先前的 SFT 針對 ChatGPT 進行測試，於 2023 年 3 月 31 日發布。
 * [RakutenAI-7B-chat](https://huggingface.co/Rakuten/RakutenAI-7B-chat) - 📥 1k / ⭐ 67 / RakutenAI‑7B‑chat 是一個以 Mistral‑7B‑v0.1 架構為基礎的日語 LLM，提供日語理解的頂尖基準結果，英語表現亦具競爭力，包含基礎模型 (RakutenAI‑7B) 與指令微調版本 (RakutenAI‑7B‑instruct)。
 * [RakutenAI-7B-instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) - 📥 1k / ⭐ 50 / RakutenAI‑7B‑instruct，建立於 Mistral‑7B‑v0.1 上，是一款以日語為重點的LLM，在日語基準測試中名列前茅，同時保持英語表現相當；同時也發佈了聊天調校版本。
 * [llm-jp-13b-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0) - 📥 1k / ⭐ 41 / 來自 LLM‑jp 的大型語言模型 – 13B 和 1.3B Japanese‑English transformers，具備多種 instruction 和 LoRA 變體，使用 Megatron‑DeepSpeed 預訓練，並以 Hugging Face 格式發布（torch ≥ 2.0，transformers ≥ 4.34）。
 * [japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - 📥 1k / ⭐ 75 / 一個 3.6‑B 參數的日本 GPT‑NeoX 模型——36 層、2816 維隱藏層 Transformer——透過基於 PPO 的 RLHF 在翻譯後的 Anthropic 數據上進行訓練，遵循指令式對話，與 SFT 相比，基於 PPO 的勝率分別為人類約 30% 和 ChatGPT 約 34%，但傾向於產生重複文本。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 1k / ⭐ 21 / youri‑7b 是一個 32 層、4096 隱藏層的 transformer，來源於 Llama2‑7b，持續預訓練於約 40 B 個日語 token（CC‑100、C4、OSCAR、Pile、Wikipedia）並於 2023‑10‑31 發布，並在 AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA 與 Winogrande 上取得競爭性分數。
 * [Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4) - 📥 1k / ⭐ 2 / 在 Qwen3‑Swallow v0.2 中，這些雙語日英大型語言模型（30B‑A3B / 32B）被通過 CPT、SFT 與 RLVR 訓練，以保持數學和編碼性能、提升推理能力，並已在 Hugging Face 上釋出多個量化版本。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 1k / ⭐ 15 / LLM‑jp 提供 13B 與 1.3B 的 transformer 語言模型，包括多個 instruction‑tuned 變體，使用 Megatron‑DeepSpeed 與 Hugging Face Transformers 生態系統構建。
 * [sarashina2-7b](https://huggingface.co/sbintuitions/sarashina2-7b) - 📥 1k / ⭐ 28 / Sarashina2‑7B 是一個擁有 7 B 參數的 Llama‑2 模型，訓練於約 1 T 的 Japanese Common Crawl tokens 與 SlimPajama English data，採用 RoPE‑based architecture，然而它仍未進行 instruction‑unfined，可能產生偏見或不準確的 outputs。
 * [t5-base-long-livedoor-news-corpus](https://huggingface.co/llm-book/t5-base-long-livedoor-news-corpus) - 📥 1k / ⭐ 1 / 一個在日本 Livedoor 新聞語料庫上微調的 T5‑base 摘要模型，展示於《Large‑Scale Language Model Introduction guide》第七章。
 * [open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - 📥 1k / ⭐ 4 / OpenCALM 是 CyberAgent 旗下的日本語 decoder‑only Transformer 語言模型套件，參數範圍從 160 M 到 6.8 B，訓練資料來源於日語維基百科及 Common Crawl，並以 CC BY‑SA 4.0 版權發布。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 82 / 由 ELYZA 開發的日文增強版 Llama‑2‑7B，預訓練以擴展日語能力，包含標準、指導、快速三種變體，附帶詳細使用範例、開發者貢獻，並採用 Meta 的 Llama‑2 Community License 授權。
 * [Qwen3-Swallow-30B-A3B-SFT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-30B-A3B-SFT-v0.2) - 📥 1k / ⭐ 1 / Qwen3‑Swallow v0.2 提供了30至32億參數的日英雙語大型語言模型，透過 CPT、SFT 與 RLVR 訓練，保留數學及程式碼執行表現，優於 Qwen3 在推理任務中的表現，並提供九種公開（AWQ‑quantized）模型變體，同時將 GPTQ‑quantized 版本保持私有。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 1k / ⭐ 96 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 7 B 的日語優化版本，提供 instruct 與 fast 兩種變體，具有 6.27–6.37 B 個參數，可通過 Hugging‑Face Transformers 庫進行存取。
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 1k / ⭐ 12 / 東京Tech-LLM 的大型語言模型，基於 LLaMA‑2 並以日文資料（SFT）微調，包括 Swallow‑7b/13b/70b 變體及其 instruct、NVE 和「plus」版本，自 2023 年 12 月至 2024 年 4 月發布。
 * [japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) - 📥 1k / ⭐ 121 / Japanese‑StableLM‑Base‑Alpha‑7B 是一個 7‑B‑parameter decoder-only 語言模型，已在混合日語/英語資料集上預訓練，以在日語語言建模和下游任務中提供強勁表現。
 * [open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - 📥 1k / ⭐ 205 / OpenCALM 是 CyberAgent, Inc. 推出的日本式解碼器專用 Transformer 語言模型套件，參數量從 160 M 到 6.8 B 不等，已在 Wikipedia 和 Common Crawl 上進行預訓練，可透過 Transformers library 以 CC BY‑SA 4.0 授權取得。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 1k / ⭐ 50 / GGUF‑格式的 NVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese，從imatrix數據集重建，已準備好使用 llama.cpp 在 CUDA 上運行。
 * [open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) - 📥 1k / ⭐ 17 / OpenCALM 是由 CyberAgent 出品的一套日語僅解碼器語言模型，參數規模從 160 M 到 6.8 B，基於 GPT‑NeoX，並以 CC BY‑SA 4.0 授權發佈。
 * [open-calm-large](https://huggingface.co/cyberagent/open-calm-large) - 📥 1k / ⭐ 10 / OpenCALM 是 CyberAgent 推出的僅解碼器日語 Transformer 家族 (參數量從 160 M 到 6.8 B，包含 open‑calm‑small 至 open‑calm‑7b)，由日語 Wikipedia 與 Common‑Crawl 訓練，採用 CC BY‑SA 4.0 授權，並可透過 Hugging Face transformers 使用。
 * [llm-jp-3-150m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-150m-instruct3) - 📥 1k / ⭐ 4 / 日本資訊學國立研究所推出的 150 M 參數教學 LLM，可作為符合 Hugging Face 的 Transformer 模型使用，需使用 torch ≥ 2.3.0 與 transformers ≥ 4.40.1。
 * [ELYZA-japanese-Llama-2-13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct) - 📥 1k / ⭐ 43 / ELYZA‑japanese‑Llama‑2‑13b 延伸了 Meta 的 Llama 2，加入額外針對日文的預訓練，提供 13 B‑參數模型（包含 instruct 與 fast 變體），可在 PyTorch 與 🤗 Transformers 之下以 Llama 2 Community License 載入。
 * [japanese-stablelm-instruct-beta-70B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-70B-GGUF) - 📥 1k / ⭐ 12 / 提供 GGUF 格式、硬體量化的模型檔案，用於 Stability AI 的 70‑billion‑parameter 日本版 StableLM Instruct Beta，準備好與 LLaMA‑cpp‑based 工具一起使用。
 * [ALMA-7B-Ja-V2](https://huggingface.co/webbigdata/ALMA-7B-Ja-V2) - 📥 1k / ⭐ 20 / C3TR‑Adapter 將 4‑bit QLoRA 應用於 gemma‑7b，允許在免費 Colab 上使用 8.1 GB GPU，而 ALMA‑7B‑Ja‑V2 提供日英翻譯（亦支援德語、中文、冰島語、捷克語），使用 BLEU 與 chrF++ 指標評估。
 * [llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0) - 📥 1k / ⭐ 8 / 提供 LLM‑jp 的 13 B 與 1.3 B 日文-英文指令集與預訓練模型，提供多種變體檢查點，供 Hugging Face Transformers 使用，需搭配 torch ≥ 2.0、transformers ≥ 4.34、accelerate 0.23 且支援 DeepSpeed。
 * [ELYZA-japanese-Llama-2-13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b) - 📥 1k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑13b 擴充 Meta 的 Llama 2，透過額外的預訓練提升日語語言能力，提供數個 13 B 參數變體（包括 instruct 和 fast），由研究團隊以 LLAMA 2 Community License 發佈。
 * [ELYZA-japanese-Llama-2-13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct) - 📥 1k / ⭐ 24 / 一個日語版本的 Llama 2 13B‑參數模型，ELYZA‑Japanese‑Llama‑2‑13B‑Fast‑Instruct，提供快速分詞、使用範例、開發者署名，並符合 Llama 2 Community License。
 * [llm-jp-13b-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0) - 📥 1k / ⭐ 15 / 13‑B 與 1.3‑B 參數 LLM‑jp instruction‑fine‑tuned 模型（包括 LoRA 變體）的倉庫，已封裝為 Hugging Face Transformers 格式，並需要 torch ≥ 2.0、transformers ≥ 4.34 以及 accelerate 0.23，使用 Megatron‑DeepSpeed 與 PEFT 在約 5 萬個混合日英/程式碼範例上訓練。
 * [llm-jp-13b-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0) - 📥 1k / ⭐ 4 / LLM‑jp 提供 instruction‑style 與 pretrained 13B/1.3B Transformer 模型，並以 Hugging Face 與 DeepSpeed 格式供應，已在 50 k+ 混合日本/英語/原始碼資料上進行訓練，需符合 torch ≥ 2.0、transformers ≥ 4.34 與 accelerate 0.23。
 * [ELYZA-japanese-Llama-2-13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast) - 📥 1k / ⭐ 7 / 此倉庫提供 ELYZA‑Japanese‑Llama‑2‑13B‑Fast 模型——一個加入日語預訓練的 Llama‑2‑13B 基礎模型——包括 instr‑styled 與 fast‑vocab 版本（約13.1 億參數，詞彙 44,581 個），並附帶示範 PyTorch 使用方法，由 Akira Sasaki、Masato Hirakawa、Shintaro Horie、Tomoaki Nakamura、Sam Passaglia 與 Daisuke Oba 共同開發，並於 Meta’s Llama 2 Community License 之下釋出。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 346k / ⭐ 76 / Japanese BERT‑base 預訓練於 2019 年日本維基百科，使用 IPA 字典與整詞掩碼，12 層、768 維，32,000 詞表，512 令牌序列，1 百萬步；可於 cl‑tohoku/bert‑japanese 在 CC‑BY‑SA 條款下取得。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 200k / ⭐ 41 / 一個基於 BERT base 的模型，預訓練於約 17 M 日文 Wikipedia 句子（2.6 GB），採用 IPA dictionary 與 WordPiece 進行 tokenization，擁有 12 layers／768‑dim hidden states／12 heads，32 000‑token 詞彙表，於 Cloud TPUs 上訓練 1 M steps，並以 CC‑BY‑SA 3.0 發布。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 142k / ⭐ 39 / Japanese‑Roberta‑Base 是由 rinna Co., Ltd. 推出的預訓練遮罩語言模型，含正確載入、token 預處理、position‑id 處理的指引，以及強調需放置於首位的 `[CLS]` token 和一致 tokenization 的使用範例。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 119k / ⭐ 8 / 一個 BERT‑base 日語模型（12 層，768‑維隱藏，12 頭），在約 1700 萬句來自日語維基百科（2.6 GB）的資料上進行預訓練，使用 MeCab IPA 單詞級分詞，隨後進行字符級分詞，建立一個 4000 單詞詞彙表。訓練程式碼位於 cl‑tohoku/bert‑japanese，並以 CC BY‑SA 3.0 釋出。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 61k / ⭐ 6 / 一個 BERT‑base 日語模型（12 層，768 維隱藏狀態，12 頭）在 30 M 句子（約 4 GB）上訓練，使用 Unidic 2.1.2 詞級分詞，隨後進行字級分詞和整詞遮蔽，使用 512 令牌序列、256 批次及 1 M 訓練步驟。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 33k / ⭐ 9 / Japanese DeBERTa V2 大型模型已在 171 GB 的日語維基百科、CC‑100、與 OSCAR 上訓練，採用字符級 sentencepiece tokenization 與 whole‑word masking，已準備好通過 Hugging Face Transformers 進行下游微調。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 17k / ⭐ 48 / 一個 132 百萬參數的 Japanese ModernBERT 模型，結合 local‑global 與 RoPE attention，在 4.39 T tokens（日語/英語）上訓練，含有 102‑k‑size 的 vocab，最大 token 長度 8,192，並優化為 Flash Attention 2。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 10k / ⭐ 24 / ModernBERT‑Ja‑310M 是一款日語 BERT 變體，結合了 local‑global attention 與 RoPE，已在 4.09 T 個日語/英語文本 token 上訓練，支持 102 400 個詞彙、8 192 token 序列，並被優化以配合 Flash Attention 2。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 8k / ⭐ 2 / Japanese DeBERTa V2 tiny，預訓練於約 171 GB 的日語 Wikipedia、CC‑100 與 OSCAR 資料庫，需要 Juman++ 詞彙分割，已在 8 顆 NVIDIA A100 GPU 上訓練 33 小時，可進一步微調以應用於下游任務。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 6k / ⭐ 49 / LINE DistilBERT Japanese 是一個 66‑million‑parameter 的 DistilBERT 模型，使用內部 BERT‑base 教師在 131 GB 的日本網路文本上進行預訓練，並於 JGLUE 上評估，採用 MeCab Unidic 與 SentencePiece 進行分詞，於 Apache 2.0 授權下釋出。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 6k / ⭐ 26 / Japanese BERT‑base (12 層, 768 hidden, 12 heads) 以 4 GB 的日本 Wikipedia（約 30 M 句）為預訓練資料，使用 Unidic 2.1.2 文字級別分詞、WordPiece 子分詞，與整詞掩碼。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 5k / ⭐ 5 / DeBERTaV2 基礎模型在日本語語料庫（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上進行訓練，並採用 FP‑16 微調以應對 NLU 任務（JSTS、JNLI、JCommonsenseQA）。本模型以 CC BY‑SA 4.0 授權發佈，並獲得日本研究撥款資助。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 3k / ⭐ 1 / 一個以 171 GB 日本維基百科、CC‑100 與 OSCAR 文本預訓練的日語 DeBERTa‑V2 基礎模型，採用字元級分詞、全詞遮罩模式，已在 8 台 A100 GPU 上訓練 20 天，並準備好進行下游微調。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 3k / ⭐ 30 / 日文 DeBERTa V2 基礎模型，已在 171 GB 日文維基百科、CC‑100 與 OSCAR 資料上使用 Juman++ 斷詞與 SentencePiece Tokenization 進行預訓練，訓練時間三週，使用八台 NVIDIA A100 GPU，已準備好進行微調。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 2k / ⭐ 32 / Japanese RoBERTa‑base，於日本維基百科與日本 CC‑100 上進行預訓練，使用 Juman++ 詞彙分割與 SentencePiece 標記化，於一週內於 8 台 NVIDIA A100 GPU 上使用 Adam（lr = 1e‑4，native AMP）進行訓練，並可微調，且於 JGLUE 上報告結果。
 * [luke-japanese-large](https://huggingface.co/studio-ousia/luke-japanese-large) - 📥 2k / ⭐ 9 / Japanese‑language LUKE，為一種知識增強型 Transformer，將單詞與 Wikipedia 實體視為獨立 token——提供語境化表示並在 JGLUE 上（例如 MARC‑ja 96.5 % 準確率）超越基準，同時針對無實體任務提供輕量版。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 一個 12 層、768 維的 BERT-Base 日語模型，使用 2.6 GB 的維基百科（≈17 M 句子）進行訓練，採用 IPA-dictionary 字元分詞與整詞遮罩（whole‑word masking），並以 CC‑BY‑SA 3.0 版權授權釋出。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 1k / ⭐ 7 / ModernBERT‑Ja‑30M 是一款日語 BERT 變體，它將局部與全局注意力與 RoPE 混合起來，並在 4.39 TB 的日英文本上訓練，支援 8,192‑token 序列，參數規模從 30 M 至 130 M，並在使用 Flash Attention 2 時表現最佳。
 * [deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 📥 1k / ⭐ 9 / Japanese DeBERTa‑V2 大型模型，預先訓練於 171 GB 日本語文本（Wikipedia、CC‑100、OSCAR），採用 Juman++ 分詞，於 8 顆 A100 GPU 上訓練 36 天，可針對下游任務進行微調。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 394k / ⭐ 74 / Ruri v3 是一個尖端的日本語文本嵌入模型，建立於 ModernBERT‑Ja，支援最多 8,192‑token 輸入、100K‑token 詞彙表、FlashAttention‑加速推論，以及多種尺寸變體，方便快速使用 sentence‑transformer。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 142k / ⭐ 9 / Ruri v3 是一款最先進的日文文本嵌入模型，構建於 ModernBERT‑Ja，支持高達 8,192 tokens、一個 100k‑token 詞彙表、FlashAttention 加速，並提供從 37 M 到 315 M 參數的多種規模。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 40k / ⭐ 6 / Ruri v3 是一款最先進的日本語文本嵌入模型，基於 ModernBERT‑Ja 建構，支援長達 8192‑token 序列、10 萬詞彙、FlashAttention，並以 30 M 到 310 M 參數大小提供，以供 sentence‑transformers 使用。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 22k / ⭐ 24 / GLuCoSE v2 是一款適合 CPU 的日語文本嵌入模型，透過蒸餾與多階段對比學習進行微調，提供優越的語義相似度與檢索性能—在 MIRACL 以及相關基準上超越同等規模模型。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 18k / ⭐ 34 / GLuCoSE 是一個基於 LUKE 的日語句子嵌入模型，輸出 768 維均值池化向量（最多 512 個 tokens），在網路及 NLI/搜尋資料上訓練，於相似度基準上達成 0.864 Spearman 與 0.818 Pearson。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 15k / ⭐ 12 / 日文通用文本嵌入模型 (Ruri‑v3, 30‑310 M 參數, 8192‑token 上限, 高 JMTEB 分數) 以 Sentence‑Transformers 使用範例提供，並與其他日文嵌入進行基準比較。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 12k / ⭐ 3 / Ruri v3 提供高性能的日語文本嵌入，最多可達 8192 個 token，擁有 100k token 詞彙表，支援 FlashAttention，並提供多種模型尺寸 (30 m–310 m) 以供透過 sentence‑transformers 進行高效推理與微調。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 11k / ⭐ 16 / JaColBERTv2 是一個僅限日文的 ColBERT 基於檢索模型，使用 MMarco（31 個負樣本對每個正樣本、250k 步驟、批次 32）進行知識蒸餾訓練，目前表現優於 multilingual‑e5‑large、BGE‑M3 以及 JaColBERT，完整評估仍待進行。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 10k / ⭐ 45 / 一組可釋出的 Ruri v3 日文文本嵌入模型（30m–310m），包含 SentenceTransformer 使用技巧、查詢/段落前綴，以及 JMTEB 基準測試結果，展示它們與其他日文及多語言嵌入模型的比較。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 7k / ⭐ 44 / PLaMo‑Embedding‑1B 是 Preferred Networks 開發的日本文本嵌入模型，能將日文文本轉換為向量，用於資訊檢索、分類與聚類，在 JMTEB 基準測試上表現優異，且以 Apache v2.0 license 免費提供。
 * [ruri-base-v2](https://huggingface.co/cl-nagoya/ruri-base-v2) - 📥 6k / ⭐ 5 / 此倉庫提供新的日文文字嵌入 v3 模型（30M‑310M 參數，最高 8k 令牌，JMTEB 74‑77），可使用 sentence_transformers（使用 query/passage 前綴）載入，並包含與有監督/無監督 SimCSE、LaBSE、E5 及其他模型的基準比較。
 * [ruri-small-v2](https://huggingface.co/cl-nagoya/ruri-small-v2) - 📥 2k / ⭐ 4 / Ruri 發布了日文通用文本嵌入模型 v3（30 M–310 M 參數，最大長度 8192 token），並取得 JMTEB 的最高分數，提供簡易的 sentence_transformers 使用方法（以「クエリ: 」或「文章: 」作前綴），以及檢索、STS、分類、重排序、聚類及成對分類任務的基準結果。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 2k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一個 768 維的句子轉換器，建立於 studio‑ousia/luke‑japanese‑base‑lite 上，已在 shunk031/jsnli 培訓一個 epoch，並包含聚類、語意搜尋以及同時適用於 Sentence‑Transformers 與 HuggingFace 的範例。
 * [fio-base-japanese-v0.1](https://huggingface.co/bclavie/fio-base-japanese-v0.1) - 📥 2k / ⭐ 7 / fio‑base‑japanese‑v0.1 是一個概念驗證的日文嵌入模型，從 cl‑tohoku/bert‑base‑japanese‑v3 在有限資料上以單一 GPU 微調，釋出用於文本蕴含與檢索任務。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 1k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B 是一個 1.2 B‑參數的日文文本嵌入模型，建立於 Sarashina2.1‑1B 上，採用多階段對比學習訓練，以在 JMTEB 上達成最先進的分數，同時產生 1,792 維的密集向量，用於語意相似度、搜尋與分類，並在非商業授權下使用。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 1M / ⭐ 57 / 日語 wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 與 JSUT 上微調，需要 16 kHz 音訊，並可透過 HuggingSound 或 HuggingFace pipelines 使用。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 189k / ⭐ 100 / Kotoba‑Whisper‑v2.2 是一款日語 ASR 模型，擴展了 kotoba‑whisper‑v2.0，整合了 integrated diarization 與 automatic punctuation，透過 HuggingFace‑Transformers pipeline 實現，並與 Asahi Ushio 和 Kotoba Technologies 合作開發。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 33k / ⭐ 19 / Kotoba‑Whisper‑v2.1 是一款日語 ASR 模型，繼承了 kotoba‑whisper‑v2.0，並整合了標點符號後處理流程，能保持相當的 CER 性能，同時實現無縫、能感知標點符號的轉錄。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 31k / ⭐ 136 / Anime Whisper 是一個輕量級的日語 ASR 模型，已在約 5,300 小時的動漫式對白上微調，提供低幻覺、節奏對齊的標點符號，並能準確轉錄非語音聲音和 NSFW 內容，必須在沒有初始提示的情況下運行。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 18k / ⭐ 10 / 一個經由 facebook/wav2vec2‑large‑xlsr‑53 在 Common Voice 與 JSUT corpus 微調的日語語音辨識模型，已優化為 16 kHz 音訊輸入。
 * [whisper-ja-1.5B](https://huggingface.co/efwkjn/whisper-ja-1.5B) - 📥 13k / ⭐ 3 / 經精細調校的 Whisper‑Large‑v3 基線在 KitsuneX07、TEDxJP、kotoba‑tech、Saruwatari‑lab 與 grider‑without‑ai 測試集上提供競爭性的 SOTA CER，訓練於 OOPPEENN、Reazon、小虫哥_、Common Voice 20 與 deepghs，且表現出較此前模型更小的檢查點與偶爾重複。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 11k / ⭐ 90 / Kotoba‑Whisper v2.0 是一款從 OpenAI Whisper large‑v3 提煉的日語ASR模型，使用 7.2 million ReazonSpeech 片段訓練，速度比原版快 6.3×，同時在領域測試中匹配教師模型的 CER/WER，並包含 stable‑ts/punctuation 支援及完整訓練程式碼於 GitHub。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 10k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供 6.3 倍更快的蒸餾 Whisper 模型，支援日本語與英語的 ASR 以及雙向語音轉文字翻譯，這些模型由 OpenAI 的 Whisper large‑v3 透過 knowledge distillation 與 cross‑entropy 及 KL‑divergence loss 建構。
 * [japanese-wav2vec2-large-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-large-rs35kh) - 📥 8k / ⭐ 3 / 使用了 ReazonSpeech v2.0 微調的日本語 wav2vec 2.0 Large (319 M 參數) 在日本語 ASR 上提供了平均 16.25 % CER，勝過其他 wav2vec 2.0 系列。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 5k / ⭐ 52 / NVIDIA NeMo 的 0.6 B‑參數 Hybrid FastConformer‑TDT‑CTC ASR 模型能帶標點符號轉錄日語語音，並且可在 NeMo 框架內進行推論或微調。
 * [japanese-hubert-base-phoneme-ctc-v4](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v4) - 📥 3k / ⭐ 4 / 已微調日本 Hubert‑Base 的 CTC 音素辨識 (v4)，包含更新的句子過濾規則、發音調整，以及將 GPU 切換至 A6000，訓練停止於 110k 步。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 2k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一個擁有 **96.7 M** 參數的 **wav2vec 2.0** Base 模型，已在 **ReazonSpeech v2.0 Japanese ASR corpus** 上微調，達到 **13.22 % CER**，可透過 **Hugging Face transformers** 部署，並以 **Apache 2.0 license** 發布。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 1k / ⭐ 38 / reazonspeech-nemo-v2 是一款擁有 619‑M參數的日語長文語音識別模型，基於改進版 Fast‑Conformer 與 Linearly Scalable Attention 架構構建，訓練於 ReazonSpeech v2.0 資料集，透過 subword RNN‑T decoder（3000‑token SentencePiece）提供多小時推理，並以 Apache 2.0 授權方式分發。
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 1k / ⭐ 24 / Kotoba Whisper v2.0 已轉換為 CTranslate2 格式，可與 CTranslate2 與 faster‑whisper 一同使用，並提供安裝、推理範例、Apple M2 基準測試以及轉換說明。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 317k / ⭐ 11 / Japanese Sentence‑BERT (v1) 模型，用於生成句子嵌入，並提供改進版 v2，並可透過 Hugging Face Transformers 與自訂的 `SentenceBertJapanese` 類別示範使用。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 52k / ⭐ 51 / 一個日本語的 Sentence‑BERT v2，經過在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上微調，並採用 MultipleNegativesRankingLoss，與 v1 相比提升了約 1.5–2 % 的準確率，並以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 形式釋出。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 28k / ⭐ 2 / ja_ginza_electra 是一個 spaCy v3 Python 套件，提供已在 mC4 和 UD_Japanese_BCCWJ r2.8 上微調的日語 ELECTRA 模型（基於 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator），並具備自訂 bunsetu‑phrase detection，依照 MIT license 發佈。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 24k / ⭐ 29 / LY Corporation 的 clip‑japanese‑base 是一個訓練於約 1 B 影像‑文字配對的日文 CLIP 模型，使用 Eva02‑B Transformer 影像編碼器並配備 12 層 BERT 文字編碼器，於 STAIR 的 R@1 成績為 0.30，於 Recruit 的準確度為 0.89，以及於 ImageNet‑1K 的準確度為 0.58，並支援零樣本影像分類與檢索。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 24k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一個授權為 Apache‑2.0 的日語 CLIP 模型，基於 ViT‑B/16，訓練於翻譯成日語的 CC12M 標題，並於 2022 年 5 月 12 日發布。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 22k / ⭐ 14 / Japanese Sentence‑LUKE 模型在與 Sentence‑BERT 相同的資料集上進行訓練，表現優於或相當於 Sentence‑BERT，基於 studio‑ousia/luke‑japanese‑base‑lite 建立，並透過 Hugging Face Transformers 的 MLukeTokenizer 與 LukeModel 使用。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 4k / ⭐ 56 / 一個日語 T5 模型，預訓練於約 100 GB 的 Wikipedia 與 OSCAR 數據，使用 SentencePiece 分詞，超越了 Google 的多語言 T5，在新聞分類基準上表現更佳，但仍需要微調，且可能產生偏見輸出。
 * [japanese-avhubert-large_noise_pt](https://huggingface.co/enactic/japanese-avhubert-large_noise_pt) - 📥 3k / ⭐ 2 / 一個已預訓練的 2,250 小時 AVHuBERT Large 自監督式模型，使用噪音增強於日語音視覺數據上訓練，以強健地支持音視覺語音辨識。
 * [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) - 📥 3k / ⭐ 4 / 日本語 HuBERT Base，12 層 transformer 版本與 rinna 原始模型相同，訓練於約19,000 小時的 ReazonSpeech v1 日本語語音資料，並以 Apache 2.0 授權發佈。
 * [llm-jp-4-vl-9b-beta](https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta) - 📥 3k / ⭐ 12 / LLM‑jp‑4‑VL 9B beta 是一個以 llm‑jp‑4‑8b‑instruct 和 SigLIP‑2 為基礎構建的 90 億參數日語視覺‑語言模型，採用 InternVL3.0‑style 動態切片以及輕量化 MLP 投影器，在 FineVision 與 Jagle 上進行訓練後，於日語基準測試中達到具競爭力的表現。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 2k / ⭐ 18 / Japanese CLIP 模型 clip‑japanese‑base‑v2，升級至約 2 B 影像‑文字配對並 distillation，將 Eva02‑B 影像編碼器與 12 層 BERT 文本編碼器結合，以達到比其前身更高的 ImageNet‑1k 準確度 (0.708)。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 1k / ⭐ 3 / 一款在 JSNLI 上使用監督式 SimCSE 微調的日語 BERT‑base 模型，透過 Sentence‑Transformers 或 HuggingFace 以 CLS pooling 方式公開，訓練於 1 M 範例，batch size 512，學習率 5 × 10⁻⁵，溫度 5 × 10⁻⁵，64‑token 限制，以及 BFloat16 精度。
 * [japanese-hubert-large](https://huggingface.co/yky-h/japanese-hubert-large) - 📥 1k / ⭐ 2 / Japanese‑HuBERT‑Large 是一個 Apache 2.0 授權的鏡像，為 rinna 原始 24 層、16 頭 transformer 模型，在約 19,000 小時的 ReazonSpeech v1 日本語音訊上訓練完成，於 2024 年 3 月 7 日發布。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 1k / ⭐ 25 / Sarashina‑Embedding‑v2‑1B 是一個 1,792 維的日語句子變換器，透過多階段對比學習訓練，達到先進的 JMTEB 分數，可用於語義相似度、搜尋、同義句挖掘、分類和聚類，透過 Sentence‑Transformers 並可加上可選的指令前綴。

### text-ranking
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 231k / ⭐ 5 / 以日語訓練的 CrossEncoder 重新排序模型，規模從 xsmall（384）到 large（1024），並包含 BGE‑v2‑m3‑v1 模型，附有微調、推理的範例程式碼，以及在 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上的基準分數。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 52k / ⭐ 14 / Ruri‑v3 Reranker 是一款以 ModernBERT‑Ja 為基礎的強大日語文本重排序器，支援多達 8,192 令牌序列、100k 令牌詞彙表、FlashAttention 以及 SentencePiece tokenizer，並可透過 sentence‑transformers 使用。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 50k / ⭐ 7 / 日本 CrossEncoder 重排序模型 覆蓋 xsmall 到 large（含 BGE），已於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 進行評估，並附上可直接使用的 sentence_transformers 與 HuggingFace 整合範例。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 14k / ⭐ 6 / 快速、輕量級的日語 Reranker v2 模型（tiny、xsmall、small、base）具有基準分數和 GPU 速度，可通過 sentence_transformers CrossEncoder 和 transformers ≥ v4.48 （可選使用 flash‑attn 加速）使用，並且亦提供 ONNX/量化版本以供 CPU/ARM 使用。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / 日文 CrossEncoder Reranker 模型（xsmall、small、base、large、BGE‑v2 m3）隱藏層大小 384–1024，示例推理通過 sentence_transformers 和 Hugging Face，在 JQaRA、JaCWIR、MIRACL 和 JSQuAD 上獲得 0.71–0.97+ 的分數。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 2k / ⭐ 16 / 由 xsmall 到 large 的日文 CrossEncoder 排序模型，使用日語文本訓練，透過 sentence_transformers 提供，並於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上進行評估。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 2k / ⭐ 15 / 一套日本 CrossEncoder 重複器（reranker）套件——包括 xsmall、small、base、large 以及 japanese‑bge‑reranker‑v2‑m3‑v1——搭配示例使用、在多個基準上的評估指標與輔助文件。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 2k / ⭐ 6 / 一個小型、高速的日語 re‑ranker 函式庫（v2），提供 tiny‑through‑base 與 cross‑encoder 模型，具有詳細的延遲與準確率統計資訊，需 Transformers ≥ 4.48（可選 Flash‑Attention 2）並支援 ONNX/quantization 用於 CPU/ARM 部署。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 1k / ⭐ 2 / Japanese‑reranker‑small‑v2 是一款輕量、快速的日語重排序模型系列（v2），提供從 tiny 到 base 的各種變體，最高可達平均 0.89 分，且 GPU 推論時間為 2–15 秒，亦包含 cross‑encoder 選項，並要求 Hugging Face Transformers v4.48+；可選擇 Flash Attention 2 以加速。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 1k / ⭐ 7 / 一套日本 Reranker v2，發布從 tiny 到 large 的 CrossEncoder 與基礎模型，每個模型皆附有基準分數與 GPU 推論時間，且需要 HuggingFace Transformers ≥ 4.48（可選 flash‑attn 以加速推論）。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 981k / ⭐ 14 / 一個以新 VNTL 數據集為基礎的 LLaMA 3 Youko qlora 微調模型，優化為準確、逐字的日語視覺小說到英文翻譯，不使用聊天模式，使用預設的 LLaMA 3 提示，並建議採用中性取樣（temperature 0，無重複懲罰）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 225k / ⭐ 11 / Sugoi LLM 14B Ultra (GGUF) 是一個日語轉英語的翻譯模型，BLEU 分數為 21.38——幾乎是其先前分數 13.67 的兩倍——在 RPG‑Maker 方括號文本上擅長，提示遵從性強，並為交互式聊天 UI 生成 JSON 輸出。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 42k / ⭐ 74 / 來自 Opus corpus 的日文-英語 Transformer‑Align MT 模型，使用 normalization 與 SentencePiece 先行處理，在 Tatoeba 測試集上達到 41.7 BLEU 與 0.589 chr‑F。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 3k / ⭐ 33 / FuguMT 是一個由 transformers 與 SentencePiece 建構的日文對英語 Marian‑NMT 翻譯模型，在 Tatoeba 上取得 39.1 BLEU 分數。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 3k / ⭐ 32 / 微調、GGUF‑量化後的 LFM2‑350M checkpoint，適用於近即時雙向日英短至中篇文本翻譯，可透過 llama.cpp 使用。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 2k / ⭐ 120 / PLaMo Translation Model 是 Preferred Networks 為翻譯任務所創建的大規模語言模型，可供 base、post‑trained 以及 evaluation 版本使用，並以 PLaMo community license 釋出，未對聊天或其他下游用途進行 instruction‑tuned。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 2k / ⭐ 55 / FuguMT 是一個基於 Marian‑NMT 的英日翻譯模型，使用 Hugging Face Transformers 和 SentencePiece 構建，於 Tatoeba 上達成 32.7 的 BLEU 分數。
 * [LFM2-350M-ENJP-MT](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT) - 📥 1k / ⭐ 88 / LFM2‑350M‑ENJP‑MT 是一個經過微調的 LFM2‑350M checkpoint，能為短到中等長度輸入提供近乎即時、雙向日英翻譯，品質可與大十倍規模的模型媲美，示例涵蓋日常、技術、商業及新聞領域，並強調人工‑AI 協作使用。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 281k / ⭐ 171 / Manga OCR 是一個 Vision Encoder‑Decoder OCR 工具，能閱讀垂直與水平的日語漫畫文字（包含振假名），適用於多種字體與低品質圖像，且源碼免費提供。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 43k / ⭐ 6 / Meikiocr的 `meiki.text.recognition.v0`——一個基於 D‑FINE 的 MobileNetV4 模型，在日語視訊遊戲文字上微調——為水平文字提供最先進的準確性和延遲，能從 960×32 的輸入中偵測多達 48 個字符，並輸出每個字符的外框與置信度分數。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 27k / ⭐ 3 / meikiocr 提供一款基於 D‑FINE 的開源權重文字偵測模型，適用於遊戲視訊（v0.1 版，採用 MobileNet‑v4 主幹，提供兩種解析度變體與 64 框限制），以及實驗性低延遲 tiny 與 small 變體，已在日本遊戲及漫畫上訓練。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 4k / ⭐ 17 / Sarashina2.2‑Vision‑3B 是一個 3‑B 參數的日本大型視覺－語言模型，建立於 Sarashina2.2‑3B‑Instruct 和 SigLIP 圖像編碼器之上，並在日本 VQA 基準上達到強勁表現。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 3k / ⭐ 2 / Manga OCR 是一個 Vision Encoder‑Decoder 系統，能在各種字體與低品質影像中提供高品質的日本漫畫 OCR，包括帶有假名覆蓋的垂直與水平文字，亦可用於一般印刷日語 OCR。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 1k / ⭐ 29 / Sarashina2.2‑OCR 是一款 3‑B 參數、端到端的 OCR 模型，經過人類偏好優化後，能將日文與英文文件解析為 Markdown，並將表格轉換為 HTML，數學轉換為 LaTeX，圖形轉換為 bounding‑box 註釋；它透過將 SigLIP2 為基礎的視覺編碼器與 Sarashina2.2‑3B‑Instruct LLM 整合，實現高解析度視覺‑語言理解。

### text-classification
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 17k / ⭐ 15 / 在 chABSA 數據集上訓練的日文情感分析模型，達到 loss 0.0001、accuracy 1.0、以及 F1 1.0。使用 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 構建，使用 Adam 進行優化（learning rate 2e‑05，10 epochs，batch size 16），並通過 `model(**inputs)` 評估。
 * [bert-for-japanese-twitter-sentiment](https://huggingface.co/LoneWolfgang/bert-for-japanese-twitter-sentiment) - 📥 8k / ⭐ 2 / Fine‑tuned BERT 適用於日文推文情感分析，使用 JTS1k dataset，將推文分類為 negative (0)、neutral (1) 與 positive (2) 標籤，已準備好可與 transformers pipeline 一同使用。
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 8k / ⭐ 6 / 一個針對 WRIME 數據集微調的日本 BERT BASE 模型，為作者和讀者預測八種情感（喜悅、悲傷、期待、驚訝、憤怒、恐懼、厭惡、信任）的 0‑4 強度分數；代碼可用，訓練耗時 3 小時於 K80 上，對作者達到約 0.6 MSE，對讀者達到約 0.2 MSE。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 5k / ⭐ 2 / 在《Large Language Model Introduction》第5章中介紹的日本 BERT‑based 模型，已於 JGLUE JSTS 資料集上進行微調，用於語義相似度評分。此模型包含 Colab notebooks、transformers‑pipeline 使用說明，以及 Apache 2.0 授權。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 3k / ⭐ 16 / 在 Amazon 商品評論上微調日本 BERT（cl‑tohoku/bert‑base‑japanese‑v2）以進行情感分類，達到約 81% 的準確率與 0.73 的 F1 分數，在 6 個 epoch 之後，學習率為 2 × 10⁻⁵。
 * [bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - 📥 1k / ⭐ 9 / Japanese BERT‑Base v3 微調整於 MARC‑ja JGLUE 整體分析資料集，來源自 cl‑tohoku/bert‑base‑japanese‑v3，可與 Hugging Face `pipeline` 一同使用，並以 Apache License 2.0 發佈。

### token-classification
 * [MedNERN-CR-JA](https://huggingface.co/sociocom/MedNERN-CR-JA) - 📥 35k / ⭐ 4 / 一個以 MedTxt-CR-JA 訓練的日本醫療命名實體識別模型，附帶可與 HuggingFace 兼容的預測腳本，可輸出 XML 標籤文本並對實體進行正規化，以及可選的再訓練工具。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 18k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日語 NER，可提取八種實體類型（公司、政治/其他組織、設施、產品、事件），透過 `BertForTokenClassification`，在 Stockmark Wikipedia 數據集上訓練，並可透過 `transformers`、`unidic_lite`、`fugashi` 安裝，採用 CC BY‑SA 3.0 許可證。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 2k / ⭐ 10 / Fine‑tuned Japanese BERT‑Base 用於在維基百科資料集上的命名實體識別，已在《Large Language Model Introduction》一書第六章展示，可透過 Hugging Face transformers pipeline 部署（Apache 2.0 授權）。
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 2k / ⭐ 4 / 一個日語專注的 DeBERTa V3 模型，具有 xsmall、base 和 large 三種變體，推理時不使用形態分析器，尊重詞界，使用縮減的詞彙表（僅在 large 型號中使用 BPE），並且與 Hugging Face 兼容。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 使用 5 週期 Adam (lr 5e‑5, batch 12) 微調 XLM‑RoBERTa‑base，針對日語 NER 資料集（tags PER, ORG, LOC, INS, PRD, EVT）以達成 0.0173 的驗證損失，已於 Transformers 4.23.1 與 PyTorch 1.12.1 發佈。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 4k / ⭐ 14 / Anime‑XCodec2‑44.1kHz‑v2 將 16 kHz 的日語語音升頻至 44.1 kHz 高保真音訊，並使用僅解碼器的 RMS‑loss 微調，保持編碼器/代碼簿凍結並保留相同的語音標記。

### text-to-speech
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 3k / ⭐ 11 / 一個名為 **tsukuyomi‑wavlm** 的日語 TTS 模型—在 tsukuyomi 語料庫 100 條語句上 fine‑tuned 300 epochs，使用 WavLM discriminator 和 A1/A2/A3 prosody features 於 VITS architecture，匯出為 61 MB 的 ONNX file，能生成 22.05 kHz syntheses。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 2k / ⭐ 127 / PaddleOCR‑VL‑For‑Manga 由 PaddleOCR‑VL 微調，於 Manga109 的對話框裁切圖像上達成 70％完整句子準確率——高於 27％基準的三倍以上——使用多語系資料集，並提供訓練程式碼與開發人員指南。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 129k / ⭐ 11 / Japanese‑language BERT‑Base（12層，768‑次元，12頭）以 Unidic 為基礎的單詞層級加字符層級標記化以及整詞遮蔽，在 CC‑100 和 2023 Wikipedia 上進行預訓練，產生了 7,027‑token 詞彙。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 73k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上訓練，使用 Unidic‑lite 詞級分詞，結合 WordPiece 子詞與全詞遮蔽，模型為 24 層、1024 維隱藏、16 頭、32k 詞表；預訓練程式碼位於 cl‑tohoku/bert‑japanese。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 65k / ⭐ 63 / Japanese BERT‑base (12 層, 768‑維度隱藏, 12 頭, 32k 詞彙) 以完整詞遮蔽在 CC‑100 與 2023‑Jan Wikipedia 上預訓練，使用 Unidic 2.1.2 詞級分詞加 WordPiece，訓練 200 萬步。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / 一個以約 100 GB 的 Wikipedia 與 OSCAR CC‑100 數據（混合 10:1、Byte‑fallback 的 SentencePiece）預訓練的日本 T5‑v1.1 模型，需對下游任務進行微調，包含遷移學習範例程式碼，提示輸出可能存在偏差，且採用 CC‑BY‑SA 4.0 授權。
 * [gemma-4-E2B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E2B-it-UD-japanese-imatrix) - 📥 12k / ⭐ 1 / 一個已轉換為 GGUF 的 Gemma‑4‑E2B‑it 模型，經過針對日語能力的微調，使用 Unsloth® Dynamic Quantization 2.0 構建，加入社群錯誤修復與日語校正資料，可在 CPU（≥8 GB RAM、≥4 GB 硬碟）上執行 via llama.cpp。
 * [llm-jp-moshi-v1](https://huggingface.co/llm-jp/llm-jp-moshi-v1) - 📥 7k / ⭐ 39 / LLM‑jp‑Moshi‑v1 是一個基於 7‑B‑parameter Moshi 架構的實驗性日語全雙工語音聊天模型，經 J‑CHAT 和 Zoom 對話資料微調，並以 Apache 2.0 許可證釋出，附帶適用於 Linux GPU 系統的 web‑UI 示範。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 5k / ⭐ 1 / 一個高度優化的 GGUF 版本，基於 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 與廣泛修復，調校以擅長日語，並可在 llama.cpp 上運行，至少需要 16 GB RAM 與 6 GB 硬碟空間（GPU 為選用）。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 4k / ⭐ 6 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一款頂級、以日文為焦點的 GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，具備廣泛的日文校準和社區修正的缺陷，即使沒有 GPU 也能在 llama.cpp 上運行，最低需要 8 GB RAM 及 3 GB 磁碟空間。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 4k / ⭐ 17 / 高效能日文 SPLADE v2 透過 WebUI demo 可進行稀疏向量轉換與推理，使用 YAST 訓練，提供 YASEM 嵌入，並報告 JMTEB 基準結果。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 3k / ⭐ 3 / 一個 T5 v1.1 模型，預訓練於日本 Wikipedia 以及 mC4/ja，採用 GEGLU 激活；預訓練期間不使用 dropout；不共享 embedding‑classifier；在 CC‑BY‑SA 4.0 協議下發佈（商業使用須事先聯繫）。
 * [Llama-3.1-70B-Japanese-Instruct-2407-gguf](https://huggingface.co/mmnga/Llama-3.1-70B-Japanese-Instruct-2407-gguf) - 📥 3k / ⭐ 8 / 一個 gguf‑格式的 cyberagent’s Llama‑3.1‑70B‑Japanese‑Instruct‑2407，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 資料構建，並以 llama.cpp 的 CLI 執行。
 * [Qwen3-Swallow-8B-RL-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-8B-RL-v0.2-gguf) - 📥 3k / ⭐ 1 / GGUF‑formatted 版的 Qwen3‑Swallow‑8B‑RL‑v0.2，以 imatrix Japanese LLM 資料構建，已準備好供支援 CUDA 的 llama.cpp 使用。
 * [Aurora-SCE-12B-v2-i1-GGUF](https://huggingface.co/mradermacher/Aurora-SCE-12B-v2-i1-GGUF) - 📥 3k / ⭐ 2 / Aurora‑SCE‑12B‑v2 模型的加權-/imatrix 與靜態 GGUF 量化集合，包含下載連結、尺寸／品質排名及使用說明。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 3k / ⭐ 18 / 日文 DeBERTa V3 基礎版本，預訓練於 LLM‑jp v1.0 的 540 B 個 token，使用已調整的 DeBERTa V3 設定，採用 unigram byte‑fallback tokenizer（無形態學分析器），並進行 fine‑tuned 於 JGLUE NLU 任務。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-thinking-gguf) - 📥 3k / ⭐ 12 / 一個使用 imatrix 數據集和自訂聊天模板，用 llama.cpp 編譯而成的 GGUF 版本 LLM‑JP 的 4.8‑b “thinking” 模型。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 73 / Llama‑3‑ELYZA‑JP‑8B 是一款日本優化的 8‑B Llama 3 模型，採用 GGUF (Q4_K_M) 與 AWQ 量化，能以 llama.cpp、LM Studio 或 OpenAI‑相容 API 執行。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 2k / ⭐ 13 / 一個 gguf 格式的 moonshotai 的 Moonlight‑16B‑A3B‑Instruct，已經在 TFMC 的 imatrix 日語資料集上訓練，準備好可與 llama.cpp (CUDA‑enabled) 一同使用，並可透過執行 recipe‑request 提示來展示。
 * [Anime-Speech-Japanese-Refiner-i1-GGUF](https://huggingface.co/mradermacher/Anime-Speech-Japanese-Refiner-i1-GGUF) - 📥 2k / ⭐ 1 / 提供了 Anime‑Speech‑Japanese‑Refiner 模型的加權/矩陣 GGUF 量化版本，列出量化類型與尺寸、比較圖表，以及對視覺模型檔案的使用指引。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 2k / ⭐ 7 / 一個為日語微調的 Qwen 3.5‑9B GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，進行了廣泛的錯誤修復、大規模日語校準，並可在 CPU 上運行，需 16 GB RAM 及 6 GB 磁碟空間，透過 llama.cpp。
 * [qwen2.5-bakeneko-32b-instruct-v2-gguf](https://huggingface.co/mmnga/qwen2.5-bakeneko-32b-instruct-v2-gguf) - 📥 2k / ⭐ 1 / GGUF格式轉換 rinna 的 qwen2.5‑bakeneko‑32b‑instruct‑v2 模型，該模型基於 TFMC/imatrix‑dataset‑for‑japanese‑LLM 構建，並附帶使用 llama.cpp 的使用說明以及可選的 CUDA 支持。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-32b-a3b-thinking-gguf) - 📥 2k / ⭐ 11 / llm‑jp‑4‑32b‑a3b‑thinking 的 GGUF‑格式轉換，使用 TFMC 的 imatrix 數據集構建，通過 llama.cpp 進行 CUDA 啟用推理。
 * [llm-jp-4-8b-instruct-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-instruct-gguf) - 📥 2k / ⭐ 6 / gguf 格式轉換的 llm‑jp‑4‑8b‑instruct 容器，使用 imatrix 資料構建，含 LMStudio 設定及範例 llama.cpp CUDA 命令。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 22 / 一個 GGUF‑格式的 pfnet 的 plamo‑2‑translate 發行版，基於 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 數據構建，並附有使用 llama.cpp 在支援 CUDA 的硬體上編譯與執行的說明。
 * [Anime-Speech-Japanese-Refiner](https://huggingface.co/NandemoGHS/Anime-Speech-Japanese-Refiner) - 📥 1k / ⭐ 9 / Anime‑Speech‑Japanese‑Refiner 是一個經過微調的 Qwen3‑Omni 30B 模型，處理日本動漫/遊戲語音音訊以生成詳細描述 (情感、角色概況等) 以及帶有非語音事件的精緻轉錄，訓練於 Galgame Gemini Captions 資料集，並在 vLLM 上表現最佳。
 * [Qwen3-Swallow-8B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-8B-SFT-v0.2-gguf) - 📥 1k / ⭐ 1 / 一個已轉換為 gguf 的 Qwen3‑Swallow‑8B‑SFT‑v0.2 模型，用於日語 LLM，使用 imatrix 數據構建，並附帶 llama.cpp 推理指令。
 * [Llama-3-ELYZA-JP-8B-gguf](https://huggingface.co/mmnga/Llama-3-ELYZA-JP-8B-gguf) - 📥 1k / ⭐ 4 / 由 elyza 提供的 GGUF‑converted Llama‑3‑ELYZA‑JP‑8B，使用 TFMC/imatrix‑dataset‑for‑japanese‑LLM 構建，已準備好供 llama.cpp 使用。
 * [sarashina2.2-3b-instruct-v0.1-gguf](https://huggingface.co/mmnga/sarashina2.2-3b-instruct-v0.1-gguf) - 📥 1k / ⭐ 8 / 一個以 GGUF 格式轉換的 sbintuitions 的 sarashina2.2‑3b‑instruct‑v0.1 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 建構，已準備好通過 llama.cpp 進行 CUDA 啟用推理。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 3M / ⭐ 44 / 聚合自 2009‑2024 年的 NicoNico Live 評論日誌超過 150 GB，包括轉換前、轉換後及實時 NX‑Jikkyo 捕獲，並提供 API 以方便檢索歷史 TV‑broadcast 討論。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 19k / ⭐ 9 / Cauldron‑JA 是一套日本視覺‑語言資料集，包含 44 個子資料集，這些子資料集是使用 DeepL API 將 The Cauldron 翻譯而成，通過 HuggingFace’s datasets library 可取得，授權條件與原始資料集完全相同，提示（prompts）則以 CC‑BY‑4.0 授權釋出。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 13k / ⭐ 4 / 一個受限、非商業性的衍生資料集，基於 EDINET XBRL 財務資料，禁止再散佈、AI 訓練及商業使用，存取需手動批准。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 6k / ⭐ 2 / WAON 是一個大型、高品質的日語圖像-文字配對資料集，透過規模、SigLIP‑score 過濾以及去重（按 URL、標題和 pHash）建立，並以 Apache 2.0 於 HuggingFace 釋出，用於資訊分析。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 6k / ⭐ 16 / 日語及多語系 QA、NLI 與同義句資料集的目錄，說明各資料集的檢索或 QA 任務以及其授權規範（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 5k / ⭐ 7 / JMedBench 是一個日本醫學領域 LLM 基準，包含 20 個資料集，涵蓋五個任務（MCQA、NER、STS 等），資料來源於 MedMCQA、PubMedQA、MMLU 及其他，每個資料集都有自己的授權，並附有註記指出翻譯可能存在偏差，需人工審核。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 4k / ⭐ 6 / Japanese Medical VQA 12M 是一個可商業使用的多模態資料集，包含超過1200萬張日文醫學影像及說明文字，來源自 Open‑PMC‑18M，採用 Parquet/Webdataset 格式，並包含原始及日文翻譯的影像、豐富的說明文字，以及使用 InternVL3.5、Qwen3‑30B 與 GPT‑oss 120B 產生的 VQA‑風格問答對。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 4k / ⭐ 18 / JMTEB 是一套日語文本嵌入基準，包含 5 個任務（聚類、分類、STS、檢索、重排序）與 28 個資料集，提供一行式評估腳本並邀請社群貢獻。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 4k / ⭐ 6 / 日文 MC4 資料集卡片 (mc4-ja)
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 4k / ⭐ 117 / Nemotron‑Personas‑Japan是一個開源、CC BY 4.0資料集，提供高品質的合成生成日本人格資料——包含姓名、性別、年齡、背景、婚姻狀況、教育、職業和地理位置——基於真實世界的人口、地理和個性分佈設計，使用概率圖形模型和GPT‑OSS‑120B進行優化，以提升多樣性、減少偏見、避免模型崩潰，協助主權AI發展並支持商業使用。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 3k / ⭐ 139 / Japanese Anime Speech Dataset V2 提供 292,637 對乾淨的音頻-文本對，約 397.5 小時為 SFW，52.4 小時為 NSFW，存於 128‑kbps MP3 檔案中按安全性分割，專為訓練自動語音識別模型而設。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 3k / ⭐ 5 / 來自 Fate/Stay Night 角色「Emilia」的對話與傳說資料集，格式化用於訓練與評估對話語言模型。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 3k / ⭐ 99 / 一個包含 100 筆樣本的日本語 instruction‑tuning 評估資料集，內含標註任務——從摘要校正、數學推理到翻譯、創意生成及使用者意圖理解——設計用於手動或自動 5‑point rating 的 fine‑tuned models 評估。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 3k / ⭐ 11 / 一份托管於 Hugging Face 的 Reazon Speech v2 Japanese dataset 的鏡像，採用 CDLA‑Sharing‑1.0 發行，使用僅限於《Japanese Copyright Act Article 30‑4》，包含 4,096 個 16 kHz FLAC 音訊檔案以及對應的 TSV/CSV format 文字稿。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 2k / ⭐ 10 / 一個日文對英文平行語料庫，將 llm‑jp‑corpus‑v3 的 kaken 子集翻譯成英文，使用 Qwen/Qwen2.5‑32B‑Instruct，特點為自訂翻譯欄位，並以 CC‑BY‑4.0 授權。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 2k / ⭐ 4 / 提供一個日文搜尋/問答資料集，包含每個查詢的分數，這些分數由五個多語言／日文再排序器計算（如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base），並包括每個查詢大約 200 篇正面與負面範例文件的平均分數。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 2k / ⭐ 18 / 一個適合 NLP 的 Wikipedia 文章資料集，來源自 2024 年 1 月的 HTML 資料快照，保留段落結構、元資料（如消歧、性、暴力旗標、模板、時間戳）以及在 GitHub 上托管的相關抽取腳本。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 2k / ⭐ 2 / 由 LLM 生成的日語查詢與答案資料集，來源於改寫的 Wikipedia 文字，並以 CC‑BY‑SA 4.0 釋出。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 2k / ⭐ 5 / Japanese JaQuAD（QG‑Bench 的子集）提供句子級和段落級資料，並以高亮顯示答案 token，用於訓練日語提問生成模型，評估指標包括 BLEU4、METEOR、ROUGE‑L、BERTScore 與 MoverScore。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 2k / ⭐ 43 / 使用者友善、去重的 CSV 資料集，包含來自 Aozora Bunko 的公有領域日語文本，已使用 globis‑org/aozorabunko‑extractor 處理並為現代日語機器學習用途做過清理。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 2k / ⭐ 48 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小時的匿名化 1,033,142 對 eroge 音訊–轉錄配對 (大多為女性，NSFW)，MIT授權，用於學術研究。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 2k / ⭐ 28 / FineWeb2 Edu Japanese 交付約 120 million 高品質教育用日語文本（≈89.3 billion tokens）來自 FineWeb2，經 DeepSeek‑API classifier（score ≥ 2.5）過濾，使用 ModernBERT‑Ja‑130M 分詞，並包含小型 token 子集（≤512 tokens）。
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 2k / ⭐ 3 / 從 Hugging Face（if001/oscar_2023_filtered）載入 Oscar 2023 資料集的 312,396 行篩選子集，並在 GitHub 上的 if001/HojiChar_OSCAR_sample 儲存庫提供範例程式碼。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 1k / ⭐ 18 / 部分 *Project Sekai* 聲樂曲目資料集，專為草薙寧々（來源 CV Machico）設計，包含 nene_org.txt 標籤檔，計畫擴充並標準化資料，並呼籲收藏此 repo、分享想法及加入 QQ 群，以取得完整收藏。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 1k / ⭐ 148 / Japanese Anime Speech Dataset 提供 73,004 對音頻-文字對（共 110 小時，從 V1 演進至 V5），用於提升 ASR 模型（如 OpenAI 的 Whisper），在開放授權下可供任何使用，若能標明來源將不勝感激。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 1k / ⭐ 2 / 擴大資料受限日語 LLM 的預訓練語料庫，包含天然日語/英語網路資料集（9B‑token JA‑WEB‑9B、63B‑token EN‑WEB‑63B/JA‑WEB‑63B）以及合成資料集（Qwen3‑14B、JA‑PARAPHRASE‑63B、JA‑INSTRUCT‑63B、JA‑TRANSLATE‑63B），用於 EACL 2026 研究。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 4 / JamC‑QA 是一個涵蓋八個日本文化與知識類別的雙語多選題基準測試，並以排行榜指標對比最先進模型。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 1k / ⭐ 89 / 一個自動翻譯的日語版 databricks‑dolly‑15k dataset，採用 CC‑BY‑SA‑3.0 授權，最後更新於 2023‑05‑11。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 1k / ⭐ 11 / 一個由 23,000,000 件個人收集的日本網路小說組成的資料集，總字數為 80,850,000,000 個字元，只允許合法機器學習用途，需提交詳細存取申請。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 1k / ⭐ 47 / 更新了 JGLUE 數據集卡和載入腳本，適用於由 Yahoo Japan 和 Waseda University 創建的日本 NLP 基準，涵蓋文本分類（MARC‑ja、JCoLA）、句子對分類（JNLI）和 QA（JSQuAD、JCommonsenseQA），發布版本已在 GitHub 和 Hugging Face 上連結。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 1k / ⭐ 33 / 一個 409 小時的日本 eroge 語音資料集，經 2-pass loudnorm 處理（‑23 LUFS、‑1 dB peak、11 LRA），由 litagin/anime-whisper 轉錄，已匿名化，存儲為 WebDataset（FLAC、JSON、TXT），主要包含女性聲音，可能存在 AI 轉錄錯誤，並以 MIT‑licensed 供學術研究。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 923 / ⭐ 6 / Range3 的 wikipedia-ja-20230101 存儲庫提供只包含日文維基百科文本的 Parquet 檔案，這些文本是從完整的維基百科資料集提取並使用 Python 程式碼生成。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 891 / ⭐ 19 / JMMMU 是一個日語多模態基準，已擴充十倍至 1,320 個文化多樣化問題 (720 個文化中立，600 個文化特定)，由母語專家翻譯，現在擁有公開排行榜。
 * [ApolloCorpus-ja](https://huggingface.co/datasets/kunishou/ApolloCorpus-ja) - 📥 881 / ⭐ 4 / 一套包含 525k 條日語指令微調集，自動從 ApolloCorpus 的英文醫學文件「medicalPaper_en_qa.json」翻譯而來，提供高品質但不完美的醫學數據集，供日語 LLM 謹慎使用。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 843 / ⭐ 14 / Jagle 是一個約 920 萬筆的日本多模態後訓練資料集，由圖像–文字配對和 PDF 文本庫構成，用於訓練 LLM‑jp‑4‑VL 9B beta，並證明能提升日語視覺-語言任務的表現。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 837 / ⭐ 13 / JMMLU 是一個日本大型多任務語言理解基準，包含 7,536 個由教師精心編寫的問題，涵蓋 56 個科目，包含專業醫學、心理學、會計、哲學，以及多種高中學科。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 796 / ⭐ 22 / 使用英文提示生成的 AI 動漫插圖，以及來自 Phi‑3 Vision 的字幕（英文與日文），已釋出至公共領域供免費使用。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 777 / ⭐ 5 / STAIR‑Captions 在 2017 年發布，提供 820,310 條日語字幕，用於字幕生成、多模態檢索和圖像生成，並帶有詳細標註、元資料以及 Creative Commons BY‑4.0 license。
 * [Synthetic-JP-Conversations-Magpie-Nemotron-4-10k](https://huggingface.co/datasets/Aratako/Synthetic-JP-Conversations-Magpie-Nemotron-4-10k) - 📥 772 / ⭐ 11 / 約 10,000 範例的日語指令微調資料集，透過 DeepInfra 將 Magpie 的方法應用於 nvidia/Nemotron‑4‑340B‑Instruct 產生，包含創建程式碼但未做後置過濾，因此可能存在一些低品質紀錄。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 740 / ⭐ 5 / JAMMEval 是七個日本 VQA 數據集的蒸餾基準，經過兩輪人工註釋以消除歧義和非視覺問題，提供對多模態日本任務的視覺‑語言模型可靠評估。
 * [EliteVoiceProject](https://huggingface.co/datasets/Elite35P-Server/EliteVoiceProject) - 📥 730 / ⭐ 13 / 非官方的 Hololive VTuber Sakura Miko 語音資料集，用於語音辨識研究，按來源平台整理並分為訓練/測試資料夾，依照 Hololive 的粉絲創作指引授權，所有權歸 Cover Corporation 所有。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 712 / ⭐ 117 / ReazonSpeech 是一個免費的 FLAC‑encoded 日語語音語料庫，附帶文字稿，提供五種規模，從 8.5 小時到 35,000 小時，可透過 Hugging Face 下載，採用 CDLA‑Sharing‑1.0 授權，並受限於日本版權法第 30‑4 條使用。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 712 / ⭐ 24 / cc100-ja 是 cc100 資料集的日本語部分，提供為分片 Parquet 檔案。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 682 / ⭐ 15 / Hachi‑Alpaca 是一個由 Stanford Alpaca 以 ‑mistralai/Mixtral‑8x22B‑Instruct‑v0.1 創建的日本合成資料集，由該模型清理，部署於 Deepinfra，並以 Apache‑2.0 license 釋出給 Alpaca‑jp research。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 667 / ⭐ 3 / 日文維基百科句子被轉換為各種嵌入，並建立 FAISS 索引，提供 Hugging Face Space 的演示、轉換腳本，以及對搜尋、問答和 OpenAI text‑embedding‑3‑small 在 RAG 中的評估；嵌入採用 OpenAI 授權，其他則採用 CC‑BY‑SA‑4.0。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 661 / ⭐ 11 / Range3/wiki40b‑ja 是 wiki40b 數據集的日文子集，作為由 Python 數據處理流程產生的三個 Parquet 檔案。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 628 / ⭐ 17 / Galgame_Speech_SER_16kHz 是一個 3.7 百萬檔（5,353 小時、104 GB）情感語音資料集，來源於 Galgame_Speech_ASR_16kHz，經本地 LLM 標註，依 GNU GPL v3.0 發佈，禁止商業使用，且訓練於此的模型必須開源，且不強制要求引用。
 * [alpaca_jp_python](https://huggingface.co/datasets/HachiML/alpaca_jp_python) - 📥 605 / ⭐ 8 / alpaca_jp_python 是一個由 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 創建的日本合成 Alpaca 數據集，使用同一模型進行清理，托管於 Deepinfra，並以 HachiML Japanese Apache 2.0 license 發佈。
 * [KokushiMD-10](https://huggingface.co/datasets/humanalysis-square/KokushiMD-10) - 📥 588 / ⭐ 7 / KokushiMD‑10 是一個多語言基準，涵蓋日本十項國家醫療保健執照考試，提供日語、英語及混合語言版本的文本與圖像多選題、計算題與填空題，覆蓋十個職業，每題皆附有專家推理說明。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 586 / ⭐ 5 / 這份 20,800 檔案的 WAV 數據集包含 195 位日本 AItuber 人格──其中包括參考、原始、描述性和情感語句──並附帶詳細的人格與聲音元資料，準備好透過數據科學 API 進行檢索。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 581 / ⭐ 5 / 資料集卡片詳述日語變體 “mc4‑ja‑filter‑ja‑normal”，附加資訊待補充。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 561 / ⭐ 11 / 一個高品質的合成日語數學題目資料集，具有已驗證的鏈式思考推理，透過 Qwen2‑7B‑Instruct 將 PRM800K 和 GSM8K 進行翻譯並篩選正確性後構建，可透過 Hugging Face datasets library 獲取。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 561 / ⭐ 34 / 重構後重新上傳 Galgame VisualNovel 資料集 (OOPPEENN/5669736E6F76656C5F44617461736574)，為了提高 Hugging Face 資料集載入效率，保留所有原始音訊 / 文字，並提供一段提取腳本，支援多種遊戲子集選項。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 542 / ⭐ 3 / 日本語指令資料集，含 632,636 個多回合樣本（約 6.35 億 tokens）以及 GPT‑OSS‑120b 理由痕跡，針對開放式、數學、寫作與多選題 (MCQA) 任務，在 135 個財務主題及 20 個一般主題中使用，旨在微調 LLM 在財務領域的推理能力。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 533 / ⭐ 12 / JaQuAD 是 2022 年的日本 QA 資料集，包含 39,696 對 SQuAD‑style 抽取式問答對，來源於 Wikipedia，總量 73.2 MB，當使用 BERT‑Japanese 微調時，F1 分數達 78.92 %（EM 63.38 %）。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 506 / ⭐ 43 / 在評估 LLMs 將日語視覺小說準確翻譯成英文的表現時，VNTL 領域排行榜以 256 個參考翻譯的餘弦相似度評估（同時報告 chrF 但未排名），並公布初步結果，該結果優於 Sugoi Translator、Google Translate、Papago 與 Alibaba Translate 等工具。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 499 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 資料集的一個 500 個樣本子集，授權為 CC BY 4.0，用於基準測試 EvoVLM‑JP‑v1‑7B。
 * [jawiki-bullet-points](https://huggingface.co/datasets/hpprc/jawiki-bullet-points) - 📥 486 / ⭐ 4 / 一個基於日語維基百科的項目式資料集，使用 Apache 2.0 授權的 rinna/deepseek‑r1‑distill‑qwen2.5‑bakeneko‑32b 模型生成，並以 CC‑BY‑SA 4.0 方式發佈。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 484 / ⭐ 6 / 將日文資料集轉換為 SentenceTransformers 友好的欄位，並根據 Rerank 分數（≥0.7 為正面，≤0.3 為負面）篩選範例，從多個 HuggingFace 來源擷取，以支援對比學習，同時遵守原始授權。
 * [CC-news-2024-July-October-cleaned](https://huggingface.co/datasets/kajuma/CC-news-2024-July-October-cleaned) - 📥 473 / ⭐ 15 / 一個從 2024 年七月至十月抽取的日本新聞語料庫，使用 Uzushio 以 pipeline_03a.conf 過濾設定從 Common Crawl 的新聞子集提取。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 466 / ⭐ 45 / Galgame_Speech_ASR_16kHz 是一個 16 kHz ASR 資料集，包含 3.75 百萬對（≈5,354 h），由 Galgame_Dataset 派生，採 GPL v3.0 授權，禁止商業使用，且任何訓練出來的模型必須開源（引用可選）。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 459 / ⭐ 8 / Rakuda 提供 40 個日文問題—針對歷史、社會與政府的開放式題目，以及針對地理的專門題目—作為基準測試日本 AI 助手的資料，與 vicuna‑eval 相似，並可透過 `datasets.load_dataset` 載入。
 * [HelpSteer2-20k-ja](https://huggingface.co/datasets/kunishou/HelpSteer2-20k-ja) - 📥 459 / ⭐ 7 / 日文翻譯的 HelpSteer2，NVIDIA 在 Nemotron‑4‑430B‑Reward 中使用的 SteerLM 試用資料集，並附上對齊與訓練資源的連結。
 * [image-text-pairs-ja-cc0-2](https://huggingface.co/datasets/alfredplpl/image-text-pairs-ja-cc0-2) - 📥 446 / ⭐ 2 / 一個 CC‑0 的日語文字‑圖像資料集，透過 GPT‑OSS‑20B 從約 80,000 個單詞/短句建立，使用 Pillow/Python 與 Noto Sans JP 字體渲染成 1 M 與 100 k 張圖像。
 * [r1-distill-qwen-pseudo-qa](https://huggingface.co/datasets/hpprc/r1-distill-qwen-pseudo-qa) - 📥 427 / ⭐ 5 / 日本語 Wikipedia Q&A 資料集，LLM 生成的問題與答案來自 DeepSeek‑R1‑Distill‑Qwen‑32B‑Japanese，並於 CC‑BY‑SA 4.0 條款下發布。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 416 / ⭐ 142 / 日語說明式對話資料集，用於微調 LLM（例如 LoRA），9M+ 範例，最近更新為去除授權的 Alpaca 數據，清理 Wikipedia 和 ALT 輸出，並以 CC‑BY‑SA 4.0 發佈。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 413 / ⭐ 2 / 18,612個將Python指令–回應對日文翻譯—使用 GPT‑4o‑mini 生成，保留原始英文提示、程式碼與範例—為訓練、微調、聊天機器人、研究與教育提供多樣的編程任務，全部以 MIT 許可證發布。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 412 / ⭐ 13 / EDINET‑Bench 是一個日本金融基準，評估 LLM 在會計欺詐檢測、盈餘預測以及產業預測等任務，使用十年的 EDINET‑API 公開報告。提供構建與評估代碼，資料集已重新授權為 PDL 1.0。
 * [MangaOCR](https://huggingface.co/datasets/hal-utokyo/MangaOCR) - 📥 404 / ⭐ 2 / 一個由大約 209 K 個敘事文字實例組成的 MangaOCR 資料集，來自 Manga109 與漫畫擬聲詞收藏，特色為多樣化的視覺風格與版式。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 400 / ⭐ 20 / 一個日語 QA 數據集，用於評估 Retrieval‑Augmented Generation (RAG)，由 JAQKET 題目與 Wikipedia 文章構建，帶有金鑰檢索相關性標簽，已於 HuggingFace 和 GitHub 發布，主要以 nDCG@10 作為評分指標。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 398 / ⭐ 15 / JGLUE 資料集卡片，使用於《Large Language Model Introduction》一書，來源自原始倉庫，程式碼採用 CC BY‑SA 4.0 許可，資料受發行者授權，引用 Kurihara & Kawahara（以日文）並建立於 Shunsuke Kitada 的倉庫。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 398 / ⭐ 34 / Syosetu711K 是一個日本資料集，於 2023 年 3 月 26‑27 日從小説家になろう抓取約 711,700 本小說，提供全文和元資料（標題、作者、NCode、簡介等）供無監督文本生成和分類任務使用。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 385 / ⭐ 9 / JSICK 是一個從 SICK 語料庫翻譯而來的日本 NLI 和 STS 數據集，包含一個 stress‑test set，將句對混淆並改寫，以評估模型對 word order 和 case particles 的敏感度，適用於 advanced multilingual compositional inference。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 384 / ⭐ 26 / 此倉庫存放了 OpenAssistant/oasst1 資料集的日文翻譯版本，包括帶有錯誤標記的自動翻譯條目、約 2,000 筆人工更正、以聊天格式擷取的子集，以及將資料轉換為指令‑輸出對以便微調的腳本。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 383 / ⭐ 5 / 日本動畫語音資料集，從原始的 `joujiboi/japanese-anime-speech-v2` 集合拆分而來。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 381 / ⭐ 7 / JHumanEval 是手工翻譯的日本版 HumanEval benchmark，提供 164 個 Python 程式設計問題，並提供對應的英文與日文註解，旨在評估 Japanese-LLM 程式產生，同時保留原始英文錯誤。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 370 / ⭐ 2 / JCommonsenseQA 是一個日語多選題常識推理資料集——CommonsenseQA 的改編版——授權為 CC BY‑SA 4.0，並以 doi:10.5715/jnlp.30.63 引用。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 365 / ⭐ 7 / Livedoor News Corpus 提供一套日語新聞文章數據集，分為 5 894 個訓練、737 個驗證和 736 個測試實例，已去除 HTML 標籤並以 Creative Commons Attribution‑NoDerivs 授權釋出。
 * [japanese-text-difficulty](https://huggingface.co/datasets/ronantakizawa/japanese-text-difficulty) - 📥 363 / ⭐ 5 / 一份 5,000 篇來自 Aozora Bunko 的日語文本資料集，使用 jReadability 評估難度，提供整體、漢字、詞彙及詳細可讀性指標，用於課程設計與適應式學習。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 354 / ⭐ 22 / 一個日本網路集合，包含56 million文件、110 B字元以及249 million圖像，這些資料被用於訓練大型視覺語言模型——提供momiji_generator進行資料填充、OBELICS‑style視覺化，以及一個範例模型（Heron‑NVILA‑Lite）。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 352 / ⭐ 18 / Databricks‑dolly‑15k‑ja 數據集是一個 DeepL 翻譯的日文版本，為指令微調而由日本 LLM‑jp 專案創建，作者為 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 與 Takumi Okamoto。
 * [jimba-instuction-1k-beta](https://huggingface.co/datasets/Kendamarron/jimba-instuction-1k-beta) - 📥 348 / ⭐ 6 / 一個由人工審閱並編輯 cyberagent/calm2-7b-chat 的輸出而構建的日語指令數據集（詳見連結文章）。
 * [Magpie-Tanuki-8B-97k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-97k) - 📥 344 / ⭐ 12 / 一個 97,269 條日語對話數據集，由於將 Magpie 的方法應用於 weblab‑GENIAC/Tanuki‑8B‑dpo‑v1.0 生成，未進行後期過濾，可能包含低質量條目。
 * [JA_audio_JA_text_180k_samples](https://huggingface.co/datasets/Sin2pi/JA_audio_JA_text_180k_samples) - 📥 341 / ⭐ 9 / MeCab‑IPADIC‑Neologd 儲存庫中的「Regexp.ja」Wiki 頁面說明了用於去除不必要標點並正規化文字的日文正則表達式規則。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 335 / ⭐ 3 / BBH‑ja 提供 BIG‑Bench Hard 資料集的日文翻譯，提供 JSON‑L（輸入、正確目標）格式的評估問題，以及 YAML（輸入、目標）格式的 Chain‑of‑Thought 提示，翻譯使用 PLaMo 模型。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 334 / ⭐ 33 / 一個用於指令‑回覆微調（例如通過 LoRA）的日語聊天數據集，來源於 llm‑japanese‑dataset，剔除日英翻譯示例，提供 1.8–2.5 million 條目，跨版本發布，並以 CC‑BY‑SA 4.0 授權，引用 DOI 10.1109/BigData59044.2023.10386605。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 327 / ⭐ 4 / 本書「Introduction to Large Language Models」所用的 livedoor news corpus 的一個經過清理的子集（授權 CC BY‑ND 2.1 JP），已由 llm‑book/ner‑wikinews‑dataset 卡所描述。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 326 / ⭐ 3 / 2010 年的日本網路語料庫已上傳至 HuggingFace，並按 2009 年版權改革為研究授權，包含自動帶標點的文本，這些文本來自形態學解析和轉換腳本。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 323 / ⭐ 2 / 大型壓縮的 JSON‑Lines 數據集，包含匿名 2ch.sc/2ch.net 論壇討論串，包含討論串 ID、標題、版面與區域資訊、回覆數量，以及完整的貼文元資料（作者、郵件、日期、內容）。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 322 / ⭐ 16 / 日本語 Alpaca 資料，來源於 masa3141 的日本語 Alpaca‑LoRA 工作，並引用原始倉庫以供進一步細節參考。
 * [ScreenTalk_JA2ZH-XS](https://huggingface.co/datasets/Itbanque/ScreenTalk_JA2ZH-XS) - 📥 321 / ⭐ 3 / 一個10,000樣本的配對資料集，約30小時的日語音訊與對應的簡體中文文字，採 Parquet 格式（CC BY 4.0），設計用於語音轉文字翻譯以及多語言ASR+MT研究。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 312 / ⭐ 5 / JAQKET 是一個來自 Wikipedia 的日語開放域問答資料集，提供版本 1.0，包含多選測驗題（13,061 個訓練例子，271 個驗證例子）以及版本 2.0，只包含需要抽取答案的提問提示（2,154 個訓練例子，1,164 個驗證例子），旨在促進問答系統研究。
 * [Zero_SFT_Ja_v3.5](https://huggingface.co/datasets/DataPilot/Zero_SFT_Ja_v3.5) - 📥 308 / ⭐ 5 / 108k 日語指令-回覆對以 BARE 方法製作，結合 Sarashina2‑70B 處理查詢、Qwen3‑235B‑A22B 處理回答，並以 Multilingual‑E5‑Large 與 Phi‑4 進行篩選，輸出格式為 JSON Lines。
 * [AKU-d_ms-0.5B-v0.1_dataset](https://huggingface.co/datasets/YukiTomita-CC/AKU-d_ms-0.5B-v0.1_dataset) - 📥 304 / ⭐ 4 / 提供 1.56 B‑token 預訓練資料集（來自各種授權公共語料庫）的倉庫，該資料集被用於在 AKU 系列中訓練 AKU‑d_ms‑0.5B‑chat‑v0.1 模型，並附帶處理腳本。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 300 / ⭐ 12 / LLM‑jp 提供一個日語指令調校數據集，來自 oasst2 的英語子集經 DeepL 翻譯（源自 kunishou/oasst2‑135k‑ja）並由 Kiyomaru 與 Kodama 編譯。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 292 / ⭐ 6 / J‑HARD‑TTS‑Eval 將短序列穩定性、重複處理和上下文完成作為基準，評估自回歸式日文 TTS 模型的魯棒性，相關資料集可通過 Hugging Face 取得（short, repetition, rhyme, continuation）。
 * [japan-law](https://huggingface.co/datasets/y2lan/japan-law) - 📥 290 / ⭐ 22 / 日本 e‑Gov 法律資料集，每筆條目包含編號、標題、唯一 ID、有效日期及全文，已去重至截至 2023 年 8 月 1 日之最新有效版本。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 284 / ⭐ 9 / 此為 llm-book/wrime‑sentiment 的資料集卡，提供一個由 WRIME 衍生的二元日語情感分析集合，根據 Avg. Readers_Sentiment 標記為正向或負向（可選擇包含中性案例），並作為《Introduction to Large Language Models》一書的樣本資料。
 * [nekopara-speech](https://huggingface.co/datasets/grider-transwithai/nekopara-speech) - 📥 282 / ⭐ 16 / 一個 Nekopara 音訊資料集，提供 44.1 kHz 的錄音，並以角色名稱、音量、原始檔名、轉錄文字以及 is_adult 標記進行標註，需要謹慎使用此成人內容標誌來做 NSFW 篩選。
 * [msmarco-ja-hard-negatives](https://huggingface.co/datasets/hotchpotch/msmarco-ja-hard-negatives) - 📥 280 / ⭐ 3 / 一個由 MS MARCO 翻譯衍生的日本硬負樣本挖掘資料集，經過 BAAI/bge‑reranker‑v2‑m3 過濾與重新排序並以 japanese‑splade‑base‑v1‑mmarco‑only 進行評分，在 0.7/0.8 門檻下，其正向率統計上顯著高於 mMARCO(ja)，提升約 1.3–1.7 %。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 271 / ⭐ 15 / 一個簡易的 Zundamon 角色設定資料集—由線上來源及管理數據編輯—用於測試 character‑LLMs，提供於 zmnjp.jsonl 與 zmn.jsonl 格式，並依指定授權提供。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 269 / ⭐ 81 / 正字對齊的日文網路小說章節與英文粉絲翻譯（106 K章節，V2），具備更新的對齊、加入系列元資料、保留標題、無質量篩選，採用 Apache 2.0 授權（合理使用），並使用 HuggingFace 基礎的下架程序。
 * [japanese-reasoning-dataset-sample](https://huggingface.co/datasets/APTO-001/japanese-reasoning-dataset-sample) - 📥 265 / ⭐ 3 / 一個高品質的合成推理 Q&A 對資料集，每個對話都包含 <think> 包裝的推理過程與最終答案，採用 JSON 格式提供，並含有題型、答案格式及對話類型的標籤，旨在微調推理模型。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 260 / ⭐ 4 / Japanese Explainable Multi‑hop Question Answering dataset 特色為問題、答案與逐步推導，連結 Wikipedia 文章，並更新推導格式及多個版本發布。
 * [monster-girl-encyclopedia-stories](https://huggingface.co/datasets/lemonilia/monster-girl-encyclopedia-stories) - 📥 256 / ⭐ 3 / 僅限日文的 MGE-universe 故事已預先批准並按時間順序排列，每條故事附帶以下元資料：(chapter, title, author, summary, tags, views, votes, update date, byte/token lengths)，並且包含最高 500k 個原始文字字符，準備進一步處理。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 255 / ⭐ 3 / 量化語音輸入與文字輸入（針對語音語言模型）的智力差距的一個資料集，由從 Elyza‑tasks‑100、M‑IFEval 和 JamC‑QA 基準中合成的音訊組成，分為四個子集；文字使用 CC‑BY‑SA 4.0 授權，音訊僅允許非營利、非再分發使用。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 251 / ⭐ 3 / 一個包含 64,139 項日文姓名的資料集，已按生物性別標記——採用漢字、平假名與羅馬拼音——其 44.9k 訓練集、6.41k 驗證集與 12.8k 測試集的分割方式獲得 ISDA’23 的接受。
 * [Aya_ja](https://huggingface.co/datasets/ryota39/Aya_ja) - 📥 245 / ⭐ 4 / 由 CohereForAI/aya_dataset 提取的 6,259 個手動標註的指令–回應對，屬於日文說明資料集，可透過 Python 的 datasets.load_dataset() 使用。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 245 / ⭐ 4 / JFWIR 是一個 64‑million‑pair 的日文資訊檢索資料集，由 fine‑web educational crawls 構建而成，提供每份文件七種查詢類型、hard negatives，並在 benchmark performance 上明顯優於此前的 prior baselines。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 240 / ⭐ 17 / oasst1‑21k‑ja 是一個由 DeepL 從英文 OASST1 子集衍生而來的日語指令調整資料集，通過日本的 LLM‑jp 合作項目創建；如需聯繫，請發送電子郵件至 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 以及 Okamoto。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 231 / ⭐ 5 / JSNLI 是 SNLI 自然語言推理基準的日語翻譯，提供為 TSV 文件，內容為在過濾與未過濾的訓練與驗證拆分中，由形態素切分過的前提–假設–標籤三元組，授權採用 CC BY‑SA 4.0。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 225 / ⭐ 21 / 這是一份 SNOW T15/T23 Japanese simplification corpus 的資料集卡片，包含 50 k 手動對齊的原始簡化日語 (≤2 k‑word vocab) 與 English translation records，以及 35 k 擴充集，供日英文本簡化與翻譯使用。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 224 / ⭐ 2 / 一份日本線上廣告資料集，用於五個 NLP 任務——廣告可接受性、一致性、性能估算、A3 認識與相似度，並以 TSV 格式提供 train/dev/test 拆分。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 223 / ⭐ 6 / Dataset card for “oscar2301‑ja‑filter‑ja‑normal”，為 Oscar 資料庫中日語過濾與正常子集。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 223 / ⭐ 5 / 這個儲存庫包含一位81歲日本女性的語音資料庫——原始與降噪的WAV檔案、音素及假名標籤——可透過 Google Drive 連結取得，免費供研究與商業語音合成使用，需署名；但禁止直接檔案連結或色情用途。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 221 / ⭐ 17 / 一個鏡像版本的 Reazon Speech v2 數據集，包含已經通過 UVR 去噪並去除背景音樂的音訊檔案（在大約十天內使用八顆 A800 GPU 處理了 4096 個檔案中的 3674 個）。
 * [amenokaku-code-instruct](https://huggingface.co/datasets/kunishou/amenokaku-code-instruct) - 📥 220 / ⭐ 17 / A 5.2k項目聚焦於程式碼的指令資料集，現在新增了 180 個 JaxTon 與 professional‑Java 項目，內容包含 1,050 條 code‑generation、150 條 code‑behavior‑check 以及 4,000 條 code‑fix 記錄，這些資料是從已翻譯成日文且完全授權商業使用的商業授權學習內容組成的。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 218 / ⭐ 3 / 一個經過清理的日語網路語料庫（例如 mc4‑ja），透過非監督式學習聚類成約 10,000 組，可用於合法分析；在 “out” 資料夾中僅列出部分文件為 Parquet 格式，並可透過 Git LFS 下載。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 217 / ⭐ 13 / Dataset 卡片（針對 “wikipedia-ja-20230720” 日文維基百科快照）
 * [japanese-image-classification-evaluation-dataset](https://huggingface.co/datasets/recruit-jp/japanese-image-classification-evaluation-dataset) - 📥 216 / ⭐ 7 / 四項以日本為中心的圖像分類任務—jafood101（101道菜）、jaflower30（30朵花）、jafacility20（20種設施）與 jalandmark10（10座地標）—由 Recruit Co. 以 CC‑BY‑4.0 授權彙編成一個資料集。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 216 / ⭐ 2 / 日本 Common Voice 17.0 子集已過濾至 649 個客戶 ID，每個包含 30–300 個樣本，按 8:2 分成訓練/驗證，分批成 1,000 個樣本的 Parquet 檔，總計 45,668 個樣本 (CC0 授權)。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 214 / ⭐ 10 / JA‑Multi‑Image‑VQA 是包含 39 張圖片、55 個題目的資料集，擁有手工製作的日語 Q&A 用於多圖像 VQA，透過 load_dataset 訪問，文本授權為 Apache 2.0（圖片受限）。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 212 / ⭐ 9 / JMMMU‑Pro 是一個日本的多模態基準，通過 Vibe Construction 建立——結合生成式建模和人工驗證——以產生低成本、高品質的 image‑QA 數據，揭示開源 LMMs 的缺陷並指引未來 VQA 研究。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 210 / ⭐ 2 / COVID‑19 日本 Twitter 數據集提供日本推文 ID 與評估碼 (63–68)，指出 COVID‑19 的相關性以及事實／意見狀態，從而促進文本分類研究。
 * [HelpSteer-35k-ja](https://huggingface.co/datasets/kunishou/HelpSteer-35k-ja) - 📥 210 / ⭐ 3 / NVIDIA 的 HelpSteer 試用資料集的日文翻譯，用於測試及對齊 SteerLM，並附有 SteerLM 訓練資源的連結。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 210 / ⭐ 12 / 僅包含足夠長度的多發佈者記錄、已標準化發佈者名稱及平衡主要發言者的日本角色扮演對話資料集，供機器學習應用。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 197 / ⭐ 4 / AnimuSubtitle‑JP 是一個使用 Advanced SubStation Alpha 格式的日語字幕資料集，可透過 Python ‘ass’ library 或像 Aegisub 這類編輯器使用，並採用 ODC‑By 授權。
 * [azurlane_voices_jp](https://huggingface.co/datasets/deepghs/azurlane_voices_jp) - 📥 193 / ⭐ 9 / 一個日文語音文字資料集，收錄 Azur Lane 角色的 30,160 條錄音（75.8 小時），來自單一演員聲音，用於 ASR/ASV 微調與評估。
 * [Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k-formatted](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k-formatted) - 📥 191 / ⭐ 11 / 日語角色扮演資料集已經從約 19,800 範例擴增至約 39,600 範例，使用 GPT‑4o‑mini，並以新增的系統訊息進行格式化。此資料集授權為 CC‑BY‑NC‑SA 4.0，且禁止用於構建與 OpenAI 服務競爭的模型。
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 191 / ⭐ 3 / JP Voice‑Text Dataset for Arknights Waifus：10,905 個日語聲音片段（總計 26.3 小時）來自單一演員角色，適合微調或評估 ASR/ASV 模型。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 190 / ⭐ 4 / 經重新格式化的日語子集 Wiki40B 資料集，作者為 Mandy Guo、Zihang Dai 以及 Denny Vrandečić.
 * [Japanese-wiki-dump-sentence-dataset](https://huggingface.co/datasets/AhmedSSabir/Japanese-wiki-dump-sentence-dataset) - 📥 188 / ⭐ 7 / 一個包含 500 萬句清晰日語完整句子上下文的資料集，適合用於無監督的語義相似度學習。
 * [CCMatrix-v1-Ja_Zh-filtered](https://huggingface.co/datasets/larryvrh/CCMatrix-v1-Ja_Zh-filtered) - 📥 188 / ⭐ 11 / 從 CCMatrix v1 過濾的日文/中文雙語資料，透過 regex 與長度檢查去除異常配對，削減到 LaBSE 語義相似度 0.6，並使用 zhconv 將所有繁體中文轉為簡體中文。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 188 / ⭐ 53 / AnswerCarefully Dataset 提供日語及多語言資料，用於商業或非商業 LLM 安全增強；禁止任何其他用途——包括安全繞過；允許帶歸屬的衍生作品；並附帶創作者對損害或服務變更之非責任免責聲明。
 * [Malum-230](https://huggingface.co/datasets/Manual-Dataset-Creation-Project/Malum-230) - 📥 187 / ⭐ 8 / Malum‑230 是一個由人手製作的日語多輪對話與段落資料集，設計用於邏輯推理，適合於預訓練與後訓練，並以 Qwen2.5‑7B 在 Japanese MT‑Bench 上進行評估。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 186 / ⭐ 24 / AutoWikiQA 是最大的免費日語問答資料集，提供超過230萬個手工篩選的問答對，這些問答對自維基百科自動生成，使用 Swallow‑MX 和 LLMs（無規則基模板），以支援知識傳授與檢索增強生成應用。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 182 / ⭐ 6 / Japanese XL‑Sum 子集經 PaLM‑2 15‑gram 重疊過濾，包含 4,215 個訓練、758 個驗證以及 766 個測試範例。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 181 / ⭐ 14 / 一份採用 CC‑BY‑SA 3.0 授權的日文實體抽取資料集，來源自維基百科，存放於 https://github.com/stockmarkteam/ner-wikipedia-dataset/，並由 Stockmark Inc. 開發。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 177 / ⭐ 2 / KokoroChat 是最大的日本心理諮詢對話資料集—由 480 位受訓顧問進行了 6,589 次角色扮演會談，平均每次 91 則發言—包含豐富且長篇的對話、詳細的 20 維客戶回饋，並支援同理心回應生成、對話評估以及心理健康語言模型的研究，並已於 ACL 2025 接受。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 176 / ⭐ 17 / 一個 1.9 億對 JSONL 資料集，用於日語假名至漢字轉換，為 zenz‑v2.5 medium、small 與 xsmall 模型提供基礎，並包含 AJIMEE‑Bench 評估語料庫。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 174 / ⭐ 7 / llm‑jp‑instructions 是一個手動編輯的日語指示資料集 (v1.0)，提供 train、dev 和 test 分割，可透過 load_dataset 存取。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 172 / ⭐ 2 / 預處理過的日語 Callhome 音訊被轉換成 WAV，並附帶 JSON 元資料陣列和 RTTM 檔案以供評估，包含發話者如 callhome_jpn_0。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 171 / ⭐ 27 / WRIME 數據集是一個日本語收藏，包含 42,200 篇文章，已用 Plutchik 的八種情緒為作者、三位讀者以及他們的平均值進行標註，並結構為 40k‑train、1.2k‑validation、2k‑test 的分割，供情感分析任務使用。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 170 / ⭐ 2 / 來自AWS的ABEJA‑CC‑JA開放資料集（https://registry.opendata.aws/abeja-cc-ja/）在Hugging Face上的鏡像，詳情請參閱Abeja的技術博客。
 * [girlsfrontline_voices_jp](https://huggingface.co/datasets/deepghs/girlsfrontline_voices_jp) - 📥 169 / ⭐ 9 / JP Voice‑Text Dataset for Girls Front Line Waifus：12,508 條單一演員女性角色錄音（20.9 小時），適合 ASR/ASV 微調與評估。
 * [ja-rag-cot](https://huggingface.co/datasets/jaeyong2/ja-rag-cot) - 📥 168 / ⭐ 2 / 一個日語維基百科資料集（209,496 項）使用 Qwen/Qwen2‑72B‑Instruct 透過思考鏈生成進行處理，採用 CC‑BY‑SA‑3.0/GNU Free Documentation 授權，由 TPU Research Cloud 支持。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 166 / ⭐ 2 / 266 小時日本語音訊資料集，來自 Emilia collection，已由 Facebook Audio Aesthetics 前置篩選，並藉 Scribe v1/ElevenLabs STT 進行分類，資料已托管於 Hugging Face，並可於 Discord 進行協作。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 165 / ⭐ 11 / Japanese Document Question Answering (JDocQA) 是一個大型 PDF 為基礎的 QA 資料集，包含 5,504 篇文件與 11,600 個已標註的日文問答對，涵蓋是/否、事實、數值及開放式問題，包括無法回答的實例，旨在評估對視覺與文字內容的複雜理解。
 * [oasst1-chat-44k-ja](https://huggingface.co/datasets/kunishou/oasst1-chat-44k-ja) - 📥 163 / ⭐ 10 / Chat 格式的 ShareGPT 數據集，來源為 oasst1‑89k‑ja，適合多輪微調，但包含長範圍的 token 序列，需要大量計算資源，已在 GitHub 和 HuggingFace 上提供。
 * [Tengentoppa-sft-v1.0](https://huggingface.co/datasets/DeL-TaiseiOzaki/Tengentoppa-sft-v1.0) - 📥 163 / ⭐ 21 / Tengentoppa corpus 是一個大型、JSON 格式的日語指令遵循資料集，來源於 16 個多樣化的公開資料集，與一個處理腳本相連，並衍生自多個開源來源。
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 162 / ⭐ 24 / RealPersonaChat 是一個包含 14,000 次發言的日本對話語料庫，將對話記錄與說話者個性、BigFive 人格分數、人口統計資料以及評分（1–5）相關聯，透過 Hugging Face 的 `load_dataset` 可存取，但須嚴格遵守隱私與非冒名作業合規。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 162 / ⭐ 3 / 資料集卡為「Introduction to Large‑Scale LLM II」一書中使用的 ja‑vicuna‑qa‑benchmark，並由 llm‑jp‑eval 為跨資料集的日語 LLM 評估所創建（Apache 2.0）。
 * [Japanese-Heron-Bench](https://huggingface.co/datasets/turing-motors/Japanese-Heron-Bench) - 📥 157 / ⭐ 11 / Japanese‑Heron‑Bench 提供 21 張具有文化標籤的日語圖片，含 102 組問答，分別涵蓋 Conversation、Detail、Complex 三個類別，並為日本視覺‑語言模型建立基準。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 153 / ⭐ 3 / WildGuardTestJP 是一份包含 1,725 個樣本的日文評估資料集，透過多階段精煉流程（Seed‑X‑PPO‑7B、gpt‑oss‑120b、Qwen2.5‑72B‑Instruct、gemma‑3‑27b‑it）忠實翻譯自 WildGuardTest，並於 Hugging Face 上以 ODC‑BY 許可發布。
 * [fgo_voices_jp](https://huggingface.co/datasets/deepghs/fgo_voices_jp) - 📥 151 / ⭐ 15 / 日語配音文字資料集，適用於《Fate／Grand Order》角色，總共 30,800 個片段（約 66.4 小時），包含單一演員錄製的內容，非常適合 ASR/ASV 的微調與評估。
 * [Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k) - 📥 150 / ⭐ 2 / 39,600 份合成的日語角色扮演對話，每份包含 5–10 回合，由 gpt‑4o‑mini 生成，並以類型、年齡標籤、世界/場景/使用者/助手設定和語氣進行標註，採用 OpenAI 訊息格式提供，並以 CC‑BY‑NC‑SA 4.0 授權，禁止任何與 OpenAI 競爭的模型使用。
 * [wikipedia-human-retrieval-ja](https://huggingface.co/datasets/baobab-trees/wikipedia-human-retrieval-ja) - 📥 149 / ⭐ 34 / 「Japanese Wikipedia Human Retrieval dataset」紀錄了受訓工人對 838 答題及 433 未答題的日本問答對進行手動基於維基百科的檢索。由 Yusuke Oda 定義，並由 Baobab Inc. 收集、核查與格式化。
 * [aozorabunko-clean-sin](https://huggingface.co/datasets/if001/aozorabunko-clean-sin) - 📥 147 / ⭐ 4 / AozoRABunko‑clean 資料集的 Fork，已過濾僅包含 meta['文字遣い種別'] 等於 '新字新仮名' 的行。
 * [LLaVA-Pretrain-JA](https://huggingface.co/datasets/turing-motors/LLaVA-Pretrain-JA) - 📥 147 / ⭐ 4 / Japanese LLaVA Pretrain 是 DeepL 轉移後的本地化版本，基於原始 LLaVA Pretrain 數據集，保持 CC‑3M 及 BLIP 許可，目標針對從事日語多模態模型與聊天機器人構建的研究人員和業餘者。
 * [AItuber-Personas-Japan](https://huggingface.co/datasets/DataPilot/AItuber-Personas-Japan) - 📥 146 / ⭐ 28 / 一個由 Kimi‑K2.5 透過 SDG‑LOOM 管線生成的合成 195 條 AI‑VTuber 人格資料集，提供概念文件、系統提示及主題清單，針對以六個種子參數（類型、個性、年齡、性別表達、視覺主題、語言風格）定義的角色，跨約 25 種類型和 20 種個性類型，授權為 ODC‑BY。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 145 / ⭐ 29 / 從日本政府機構網站手動提取並經 QC‑checked 的 FAQ 資料集，授權為 CC‑BY‑4.0，以 QA 形式呈現並附有來源 URL，用於 LLM instruction‑tuning 和 RAG testing，然而仍受 PDF‑to‑text conversion 雜訊以及強烈的政府觀點所影響。
 * [cosmopedia-japanese-100k](https://huggingface.co/datasets/aixsatoshi/cosmopedia-japanese-100k) - 📥 144 / ⭐ 7 / Cosmopedia 日本語資料已擴充至 100k 條目（含提示翻譯），並可作為 Hugging Face 資料集取得，亦存於儲存庫中。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 143 / ⭐ 2 / 一個多模態日語表格問答資料集，用於直接從年度證券報告表格中提取單元格值，提供圖像、帶有邊界框的 OCR 文本、問題和答案，並採用 CC‑BY‑4.0 許可。
 * [shisa-pretrain-en-ja-v1](https://huggingface.co/datasets/augmxnt/shisa-pretrain-en-ja-v1) - 📥 142 / ⭐ 7 / shisa‑base‑7b‑v1 的預訓練資料集，構建自 DSIR 樣本中的 MADLAD‑400 日語/英語 tokens，比例為 90%/10%。
 * [Magpie-Tanuki-8B-annotated-96k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-annotated-96k) - 📥 141 / ⭐ 6 / 一個 96k 樣本資料集，將 Magpie 應用於 Tanuki‑8B，並由 cyberagent/calm3‑22b‑chat 標註難度、品質與任務類別標籤。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 140 / ⭐ 33 / 提供日文 RAG 基準，涵蓋金融、電訊、製造、公共、零售五大產業領域，透過發布資料集、自動評估框架，以及比較結果，例如 Claude 3.5‑Sonnet、GPT‑4o 等模型。
 * [JParaCrawl-Filtered-English-Japanese-Parallel-Corpus](https://huggingface.co/datasets/Verah/JParaCrawl-Filtered-English-Japanese-Parallel-Corpus) - 📥 139 / ⭐ 3 / 提供了一份已清理的日文對英文翻譯語料庫，並配備了經過微調的 Mistral/Stable‑LM 模型，用於評估每一對翻譯，只接受高品質的翻譯，拒絕任何不完整、不準確或寫作差的翻譯。
 * [hh-rlhf-12k-ja](https://huggingface.co/datasets/llm-jp/hh-rlhf-12k-ja) - 📥 138 / ⭐ 14 / 日文翻譯，屬於 hh‑rlhf human preference dataset 的子集，由日本本土的 LLM‑jp 合作項目使用 DeepL 產出。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 138 / ⭐ 7 / 一個由 Voicevox 生成的人工聲音資料集，包含來自 ITA、つくよみちゃん 和 ROHAN 語料庫的 445,793 個 .wav 檔案，總計 577 小時 51 分 23 秒音訊。
 * [guanaco_ja](https://huggingface.co/datasets/fn-aka-mur/guanaco_ja) - 📥 135 / ⭐ 6 / 日本語子集的Guanaco資料集，可比作如 inu‑ai/alpaca‑guanaco‑japanese‑gpt‑1b 等儲存庫。
 * [Synthetic-JP-EN-Translation-Dataset-Magpie-Nemotron-4-20k](https://huggingface.co/datasets/Aratako/Synthetic-JP-EN-Translation-Dataset-Magpie-Nemotron-4-20k) - 📥 135 / ⭐ 6 / 一個 20 k 的日英與英日翻譯資料集，使用 Magpie 方法在 nvidia/Nemotron‑4‑340B‑Instruct 上透過 DeepInfra 生成，公開發布程式碼但未做後續篩選，因此可能包含一些低品質記錄。
 * [alpaca_jp_math](https://huggingface.co/datasets/HachiML/alpaca_jp_math) - 📥 134 / ⭐ 6 / alpaca_jp_math 是一個由 Stanford Alpaca 與 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 產生的日本合成數學資料集，經由一個提示清理，該提示驗證程式計算與文字輸出在小數點第三位相符，並以 HachiML Apache 2.0 授權發布。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 134 / ⭐ 4 / 「Japanese RAG Generator Benchmark (J‑RAGBench)」供應一份多分類 QA 數據集—涵蓋 Integration、Reasoning、Logical、Table 與 Abstention—旨在評估日文 RAG 生成器，並由人力與 GPT‑4.1 建構，且以 CC BY‑SA 4.0 授權發布。
 * [AutoMultiTurnByCalm3-22B](https://huggingface.co/datasets/kanhatakeyama/AutoMultiTurnByCalm3-22B) - 📥 133 / ⭐ 2 / 自動生成的多回合問答數據集：最初的問題取自開放來源，所有後續回覆由 Calm3‑22b 合成，使用 Tokyo Tech’s TSUBAME4.0 構建，並以列出的授權釋出.
 * [oscor-2301-ja-text-content](https://huggingface.co/datasets/ayousanz/oscor-2301-ja-text-content) - 📥 131 / ⭐ 2 / 從 OSCOR‑2301‑ja JSON 檔案中擷取「content」欄位文字，並附上一段 Python 腳本，將這些值從指定資料夾中的每一個 JSON 拉取。
 * [J-ResearchCorpus](https://huggingface.co/datasets/kunishou/J-ResearchCorpus) - 📥 130 / ⭐ 32 / J‑ResearchCorpus 提供約 3900 萬個高品質日本研究論文文本，來自 1,343 個 CC‑BY‑4.0 來源—包括 NLP2024 會議論文和期刊文章—，準備好供語言模型預訓練與 RAG 使用。
 * [Synthetic-JP-Roleplay-Instruction-Nemotron-4-1k](https://huggingface.co/datasets/Aratako/Synthetic-JP-Roleplay-Instruction-Nemotron-4-1k) - 📥 129 / ⭐ 6 / 約1,000項日語角色扮演指令集，經由將 Synthetic‑JP‑Roleplay‑Instruction‑Nemotron‑4 Magpie 方法應用於 NVIDIA/Nemotron‑4‑340B‑Instruct，使用 DeepInfra 產生，包含未經過濾的資料，可能包含低質量條目。
 * [japanese_hh-rlhf-49k](https://huggingface.co/datasets/fn-aka-mur/japanese_hh-rlhf-49k) - 📥 126 / ⭐ 12 / 一個修改過的 kunishou/hh‑rlhf‑49k‑ja 版本，排除 ng_translation=1 的條目，參考原始資料集。
 * [arxiver_ja](https://huggingface.co/datasets/speed/arxiver_ja) - 📥 124 / ⭐ 3 / 由 gemma‑2‑2b‑it 生成的 neuralwork/arXiv 摘要欄位的日文翻譯，授權為 CC BY‑NC‑SA 4.0。
 * [CABankSakuraCHJP](https://huggingface.co/datasets/Fhrozen/CABankSakuraCHJP) - 📥 123 / ⭐ 2 / 日語 CallHome 語料庫：在美國錄製了 120 位說話者的 200 條電話通話（每條最多 30 分鐘），並將其轉寫為 80 個訓練集、20 個開發測試集和 100 個評估測試集，錄音可透過免費 LDC 機器人操作員取得。
 * [japanese-stackexchange](https://huggingface.co/datasets/p1atdev/japanese-stackexchange) - 📥 122 / ⭐ 3 / 一個已處理的日本 Stack Exchange QA 資料集，包含 28,428 篇英日問答對，提供預設與簡易子集合，並附上貼文及答案的元資料（IDs、已接受/熱門答案、分數、標籤、標題、內容），可透過 Hugging Face `datasets` library 閱讀，並採用 CC BY‑SA 4.0 許可。
 * [Longcontext-aozora-summary](https://huggingface.co/datasets/aixsatoshi/Longcontext-aozora-summary) - 📥 122 / ⭐ 6 / 由長篇文本衍生的摘要對資料集，來源於 Aozora Bunko 语料库（globis‑university/aozorabunko-clean），採用 CC BY 4.0 授權。
 * [oasst2-chat-68k-ja](https://huggingface.co/datasets/kunishou/oasst2-chat-68k-ja) - 📥 121 / ⭐ 8 / 一個類似於 ChatGPT 的「ShareGPT」格式化資料集（oasst2‑135k‑ja），準備進行多輪微調，雖然每筆紀錄的長 token 長度需要大量運算資源，但已透過 OpenAssistant Hugging Face 倉庫提供指引。
 * [Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k-formatted](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k-formatted) - 📥 121 / ⭐ 2 / 一份日語角色扮演資料集（20 k 個樣本），由 deepseek‑ai/DeepSeek‑V3‑0324 生成，重新格式化為系統訊息並以 MIT 許可證發布。
 * [oasst2-135k-ja](https://huggingface.co/datasets/kunishou/oasst2-135k-ja) - 📥 119 / ⭐ 13 / 一個日語聊天格式資料集，**oasst2-chat-68k-ja**，源自 DeepL 翻譯的 OpenAssistant/oasst2，附帶程式碼將其轉換為 Instruction/Output 對件以進行微調。
 * [MGSM_ja](https://huggingface.co/datasets/sbintuitions/MGSM_ja) - 📥 118 / ⭐ 2 / 一個僅限日文的 Hugging Face 複製版 MGSM，這是一個於 2021 年推出的多語言「思維鏈」語言模型，確保可重現的評估分數並包含 SB Intuitions 修訂。
 * [japanese-photos-conversation](https://huggingface.co/datasets/llm-jp/japanese-photos-conversation) - 📥 117 / ⭐ 7 / 一份包含 11,808 個樣本的多輪對話資料集，內容為關於日本圖像的對話，來源於 ThePioneer/japanese-photos，部分使用 Azure OpenAI 進行過濾，授權遵循 CC‑BY‑4.0 條款，並受 OpenAI 條款限制。
 * [cosmopedia-100k-ja-preview](https://huggingface.co/datasets/kunishou/cosmopedia-100k-ja-preview) - 📥 111 / ⭐ 4 / 日文自動翻譯的 cosmopedia‑100k 條目，索引為 20k–100k（長文本記錄已省略），將來會與 0–20k 翻譯集合併並被移除，但資料集仍保留在檔案中。
 * [JaCWIR](https://huggingface.co/datasets/hotchpotch/JaCWIR) - 📥 111 / ⭐ 6 / JaCWIR 是一個日語休閒網路資訊檢索資料集，包含 5,000 個由 ChatGPT 生成的查詢，並連結至約 500k 篇來自 Hatena Bookmark 的標題與描述，可透過 BM25/embedding 再排序及 MAP@10 指標進行非商業性搜尋模型評估。
 * [abc-multiple-choice](https://huggingface.co/datasets/tohoku-nlp/abc-multiple-choice) - 📥 108 / ⭐ 4 / 一個由日本多項選擇題組成的 QA 數據集，來源於 abc 比賽中使用的 4 選項測驗問題，評估腳本托管在 GitHub 上，只授權用於研究。
 * [Japanese_Wikipedia_Conversation](https://huggingface.co/datasets/shi3z/Japanese_Wikipedia_Conversation) - 📥 107 / ⭐ 7 / 使用 GPT‑3.5‑Turbo 從 Wikipedia 日文版（izumi‑lab/wikipedia‑ja‑20230720）生成的對話文本資料集，不適用於商業用途。
 * [llmjp-kaken](https://huggingface.co/datasets/hpprc/llmjp-kaken) - 📥 106 / ⭐ 6 / 將 llm-jp-corpus-v3 的 kaken 子集轉換為 Hugging Face 格式，並在可能的情況下從每個網址附加檢索到的文章標題，授權 CC‑BY 4.0。
 * [Umamusume-voice-transcription](https://huggingface.co/datasets/TLME/Umamusume-voice-transcription) - 📥 105 / ⭐ 8 / 一份包含 77 個角色的《ウマ娘》語音轉錄音頻資料集，並為倉庫中列出的每首曲目提供詳細的播放時間統計（≈799–1563 s）。
 * [wikidata-parallel-descriptions-en-ja](https://huggingface.co/datasets/Mitsua/wikidata-parallel-descriptions-en-ja) - 📥 104 / ⭐ 9 / 一個雙語英日平行語料庫，用於機器翻譯，已從 Wikidata dump 提取並過濾成 JSONL 格式，準備好供 Hugging Face 訓練使用，進行了去重但仍包含一些噪聲，採用 CC0 1.0 發佈。
 * [jmultiwoz](https://huggingface.co/datasets/nu-dialogue/jmultiwoz) - 📥 103 / ⭐ 8 / JMultiWOZ 是一個大型的日本多域任務導向對話資料集，包含 4,246 個由 WoZ 生成的對話，涵蓋餐廳、酒店、景點、購物、計程車和天氣領域，並為使用者目標、對話狀態（belief、book、DB results）以及發言進行註解，可用於對話狀態追蹤與生成等任務。
 * [Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k) - 📥 103 / ⭐ 9 / 約 2 萬項合成日語角色扮演資料集，由 DeepSeek V3 生成，包含 10–20 回合對話，並以類型、年齡標籤、世界/場景/使用者/助手設定、語氣以及 OpenAI 訊息格式進行註釋；採 MIT 授權，方便模型訓練。
 * [Ideal-TSUNDERE-Loli-Girl-Japanese-v1](https://huggingface.co/datasets/Rikunarita-ORG/Ideal-TSUNDERE-Loli-Girl-Japanese-v1) - 📥 103 / ⭐ 2 / 高品質、手工製作的日語對話資料集，聚焦於傲嬌小女孩（tsundere loli）主題，包含簡短且情感豐富的交流，採用 JSONL 格式，用於微調 Gemma、Qwen、Llama、Mistral 與 OpenHermes 等聊天模型，在 MIT 授權下發布。
 * [databricks-qa-ja](https://huggingface.co/datasets/yulanfmy/databricks-qa-ja) - 📥 101 / ⭐ 5 / 一個大約 1,300 條手動創建的關於 Databricks 的問題-答案對，來自其 HP blog、FAQ 和員工在 Qitta 上的貼文，用於展示。
 * [iterative-dpo-data-for-ORPO-iter3](https://huggingface.co/datasets/Aratako/iterative-dpo-data-for-ORPO-iter3) - 📥 101 / ⭐ 3 / 日語偏好資料集由 Aratako/Self‑Instruct‑Qwen2.5‑72B‑Instruct‑60k 建構，使用開發模型為每個指令產生五個回覆，並以 Qwen/Qwen2.5‑72B‑Instruct‑GPTQ‑Int8 進行 0–5 分數評估，選取最高分作為「選中」且最低分作為「拒絕」，排除平手或分數 ≤2 的情形，並受 Meta LLama 3.1 Community License、Gemma Terms of Use 與 Qwen 授權條款約束。
