# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專門收錄日語NLP相關的Python函式庫、LLM、詞典和語料庫資源的精選列表。
本頁面列出了Hugging Face上可用的日語NLP專用模型和資料集。目前包含174個模型和137個資料集。

_更新於2026年6月29日_

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)

## Contents
 * [Ranking](#Ranking)
   * [Models](#models-ranking)
   * [Datasets](#datasets-ranking)
 * [Models](#Models)
   * [text-generation](#text-generation)
   * [fill-mask](#fill-mask)
   * [automatic-speech-recognition](#automatic-speech-recognition)
   * [sentence-similarity](#sentence-similarity)
   * [feature-extraction](#feature-extraction)
   * [text-ranking](#text-ranking)
   * [translation](#translation)
   * [image-to-text](#image-to-text)
   * [text-classification](#text-classification)
   * [token-classification](#token-classification)
   * [text-to-speech](#text-to-speech)
   * [audio-to-audio](#audio-to-audio)
   * [any-to-any](#any-to-any)
   * [image-text-to-text](#image-text-to-text)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | 模型名稱 | Downloads | Likes | 類別 |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 6M | ⭐ 61 | automatic-speech-recognition |
| 2 | [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) | 📥 2M | ⭐ 39 | fill-mask |
| 3 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 756k | ⭐ 14 | translation |
| 4 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 610k | ⭐ 80 | sentence-similarity |
| 5 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 387k | ⭐ 76 | fill-mask |
| 6 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 373k | ⭐ 9 | fill-mask |
| 7 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 368k | ⭐ 176 | image-to-text |
| 8 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 367k | ⭐ 15 | text-generation |
| 9 | [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) | 📥 348k | ⭐ 5 | text-ranking |
| 10 | [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) | 📥 266k | ⭐ 14 | text-ranking |
| 11 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 250k | ⭐ 41 | fill-mask |
| 12 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 224k | ⭐ 10 | sentence-similarity |
| 13 | [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) | 📥 217k | ⭐ 108 | automatic-speech-recognition |
| 14 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 182k | ⭐ 12 | translation |
| 15 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 124k | ⭐ 11 | others |
| 16 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 116k | ⭐ 59 | text-generation |
| 17 | [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) | 📥 108k | ⭐ 138 | text-generation |
| 18 | [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) | 📥 83k | ⭐ 24 | sentence-similarity |
| 19 | [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) | 📥 81k | ⭐ 56 | feature-extraction |
| 20 | [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) | 📥 75k | ⭐ 42 | text-generation |

### Datasets-ranking

| # | 資料集名稱 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 2M | ⭐ 58 |
| 2 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 15k | ⭐ 9 |
| 3 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 12k | ⭐ 32 |
| 4 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 8k | ⭐ 7 |
| 5 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 5k | ⭐ 11 |
| 6 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 5k | ⭐ 120 |
| 7 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 3k | ⭐ 7 |
| 8 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 3k | ⭐ 35 |
| 9 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 3k | ⭐ 46 |
| 10 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 99 |
| 11 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 2k | ⭐ 7 |
| 12 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 2k | ⭐ 49 |
| 13 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 2k | ⭐ 141 |
| 14 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 2k | ⭐ 18 |
| 15 | [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) | 📥 2k | ⭐ 24 |
| 16 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 1k | ⭐ 19 |
| 17 | [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) | 📥 1k | ⭐ 6 |
| 18 | [WAON](https://huggingface.co/datasets/speed/WAON) | 📥 1k | ⭐ 2 |
| 19 | [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) | 📥 1k | ⭐ 4 |
| 20 | [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) | 📥 1k | ⭐ 18 |

## Models
### text-generation
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 367k / ⭐ 15 / 一個 12 層、768 隱藏層的日本 GPT‑NeoX 模型，訓練於 CC‑100、C4 和 Wikipedia，兼容 Huggingface，並可選擇使用一個玩具前綴調優權重，使每句結尾強制出現笑臉表情符號。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 116k / ⭐ 59 / 一個 2.7‑B 參數的日語 GPT‑NeoX 模型，由 ABEJA Inc 在日語 CC‑100 與 OSCAR 上訓練，可透過 Hugging Face Transformers pipelines 或 PyTorch 使用，並以 MIT 授權釋出。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 108k / ⭐ 138 / 一個九十億參數的日文優化 LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，於 2024 年 9 月以前的資料進行訓練，採用混合的 Mamba‑2/MLP/4‑layer‑attention 架構，並在 Nemotron‑Personas‑Japan 工具呼叫資料集中進行微調，可選擇在產生最終答案前生成可控的推理回溯，且可商業使用。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 75k / ⭐ 42 / 提供 NII 的 8B 參數 LLM‑jp‑4‑8b‑thinking 日文語言模型，已經以 pre/​mid‑training 訓練並通過 SFT/DPO 對齊，已準備好與 torch‑transformers 一起使用，並附有詳細的 cookbook 指南。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 74k / ⭐ 21 / OpenCALM 是由 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 之下發佈的一套僅解碼器的日語 transformer 語言模型（160 M–6.8 B 參數），經日本維基百科與 Common Crawl 訓練，可透過 Hugging Face 的 torch‑transformers 使用。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 50k / ⭐ 8 / LLM‑jp‑3‑150m — 來自日本情報學研究院 LLM 研發中心的 150M 參數日語語言模型，已以 Hugging Face Transformers 格式發佈，需安裝 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，並以日語維基百科、Common Crawl、WARP/PDF、WARP/HTML 以及 Kaken 數據，使用 unigram byte‑fallback tokenizer 進行預訓練。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 36k / ⭐ 36 / 一個32十億參數的日語 transformer LLM (llm‑jp‑4‑32b‑a3b‑thinking)，來自國立情報學研究所 (National Institute of Informatics)，預訓練並通過有監督微調與直接偏好優化進行調整——未使用強化學習——採用 unigram byte‑fallback tokenizer。
 * [Llama-3.3-Swallow-70B-Instruct-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-Instruct-v0.4) - 📥 24k / ⭐ 13 / Llama 3.3 Swallow 是一個擁有 70 億參數的日文增強大型語言模型，透過對 Meta 的 Llama 3.3 進行持續預訓練和指令微調而構建。它提供多種已發布變體（例如 v0.4），可在 Hugging Face 與 Swallow 官方網站下載。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 20k / ⭐ 10 / llm‑jp‑4‑8b‑instruct 是 NII 的 LLM‑jp‑4 系列 4.1 B 參數的日語 LLM，先在大規模語料庫上進行預訓練，接著僅用監督式指令資料微調（不使用 DPO/REINFORCE），並附有類似食譜風格的使用指引與 byte‑fallback unigram tokenizer。
 * [LFM2.5-1.2B-JP-202606](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606) - 📥 15k / ⭐ 63 / LFM 2.5‑1.2B‑JP‑202606 是一款高效能、通用的日語聊天模型，在知識、指令遵循、數學、程式碼與工具使用方面優於同類 200 億參數以下的模型，適合開發者打造具有文化細膩度的日語應用。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 11k / ⭐ 39 / 提供由 SB Intuitions 推出的自回歸日語語言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已與其他模型進行基準測試，且附帶示例使用腳本，並註明安全訓練有限。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 10k / ⭐ 7 / 已預訓練的 TinyLlama，日語版本（≈50k 步），建立於約3B OSCAR/mC4 代幣上，可透過 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 與 Renju Aoki 製作。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 10k / ⭐ 17 / 一套日本大型語言模型（1.8 b 至 172 b beta1，含 instruct 變體）來自 NII 研究發展中心，以 Hugging Face Transformers 格式打包，並在混合的日文、英文以及網路語料上預訓練，總 token 數量超過 1 trillion，需至少 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 9k / ⭐ 21 / Llama3 Swallow 是一款日本增強版 Meta Llama 3 系列，於 2024 年 7 月 1 日發布，提供 8B 與 70B 兩種版本，包含 Instruct 與 chat 形式，並使用 SFT 與 Chat Vector 在 Megatron‑LM 上微調，並在關鍵的日本 NLP 任務上進行基準測試。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 9k / ⭐ 24 / Llama 3.1 Swallow 是一系列經過日本優化的 8B/70B Llama 3.1 模型，透過持續預訓練和日本專用說明微調進行訓練，最新的 8B‑Instruct‑v0.3 在日本 MT‑Bench 上取得了最先進的成果。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 實驗性日本模型，透過採用 chat‑vector 方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 與 Meta‑Llama‑3‑8B‑Instruct 之間的差異，升樣後應用於 Meta‑Llama‑3‑70B‑Instruct，顯示變化不大，並計畫未來擴充。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 7k / ⭐ 148 / Llama‑3‑ELYZA‑JP‑8B 是 ELYZA 推出的日語改良版，8 億參數的 Llama 3 模型，已在 Meta‑Llama‑3‑8B‑Instruct 上為日語進行微調。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 7k / ⭐ 10 / 此存儲庫提供 GGUF 格式、量化的模型檔，適用於 Stability AI 的日文 StableLM Instruct Gamma 7B，該模型由 Massed Compute 硬體製成，並屬於 TheBloke 的 a16z 資金支持的 LLM 專案的一部分。
 * [LFM2.5-1.2B-JP-202606-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-GGUF) - 📥 7k / ⭐ 21 / Hybrid LFM2 模型來自 Liquid AI，例如 1.2 B 的日語 GGUF 版本，提供高品質、快速且記憶體效率高的邊緣 AI，可在裝置上部署並透過 Hugging Face repo 使用 llama.cpp 本地執行。
 * [Wanabi-Gemma4-31B-GGUF](https://huggingface.co/kawaimasa/Wanabi-Gemma4-31B-GGUF) - 📥 6k / ⭐ 4 / 一個針對 Google 的 Gemma 4 31B 進行微調的 GGUF 版本，已為 Project Wannabe 的結構化提示格式與日文創作寫作進行優化，同時保留一般對話與推理功能，可用於各種聊天 UI。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 6k / ⭐ 85 / Rinna 的 24 層、1024 隱藏單元的日本 GPT‑2‑medium 模型，使用 CC‑100 和 Wikipedia 進行訓練，採用 SentencePiece 分詞，已在 rinna/japanese‑pretrained‑models repo 中提供（MIT‑licensed，於 2021 年 4 月 7 日發布，於 2021 年 8 月 25 日更新）。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 6k / ⭐ 2 / Qwen3‑Swallow v0.2 提供 30‑B 和 32‑B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，提升日語準確度、翻譯、數學與編碼能力，以達到或超越原始 Qwen3，提供九種模型（CPT、SFT、RL）以及 AWQ‑quantized 版本，並同時發布 GPT‑OSS‑Swallow。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 6k / ⭐ 19 / Llama 3.1 Swallow 是一組 8‑B 和 70‑B 模型，繼續對 Meta 的 Llama 3.1 進行預訓練以提升日語表現，然後在合成日語數據上進行 instruction‑fine‑tune，提供多個已發佈的變體，具有與 gemma‑3‑27b‑it 相當的對話行為改進。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 5k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 與 Swallow Team 所開發的一款緊湊型日語指令跟隨語言模型，採用 Qwen2.5‑32B‑Instruct 的 TAID 蒸餾，並進一步於日語文本上進行預訓練，僅以 Apache 2.0 授權釋出，僅供研究用途。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 5k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27‑B 參數擴充，已在包含 instruct 與 fast 變體的日文資料上進行預訓練，可透過 Hugging Face Transformers 使用。
 * [Qwen3-Swallow-8B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2-AWQ-INT4) - 📥 5k / ⭐ 1 / Qwen3‑Swallow v0.2 提供雙語日英 30B‑A3B 與 32B 模型，基於 Qwen3 經由 Continual Pre‑Training、Supervised Fine‑Tuning 與 Reinforcement Learning with Verifiable Rewards 建構，以提升日文能力、翻譯、數學與程式推理，同時保持核心 Qwen3 性能，並提供多種量化變體。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 4k / ⭐ 27 / rinna 的日語 GPT‑2 small 為 12 層、768 隱藏單元的 transformer，訓練於日語 CC‑100 和 Wikipedia，使用 SentencePiece 進行分詞，於 2021 年 8 月 25 日以 MIT 版發布（Hugging Face：rinna/japanese‑gpt2‑small，詳見 https://arxiv.org/abs/2404.01657）。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 4k / ⭐ 6 / 一個存儲庫托管國立情報學研究院 LLM 研發中心的 8.6 B‑parameter llm‑jp‑4‑8b‑base transformer，該模型經由預訓練與中訓練，隨後進行監督式微調與直接優先權優化（未使用強化學習），並提供 PyTorch‑transformers 使用指南。
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 3k / ⭐ 12 / 東京Tech-LLM 的大型語言模型，基於 LLaMA‑2 並以日文資料（SFT）微調，包括 Swallow‑7b/13b/70b 變體及其 instruct、NVE 和「plus」版本，自 2023 年 12 月至 2024 年 4 月發布。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 3k / ⭐ 15 / SB Intuitions 的 Sarashina2.2‑0.5B instruct v0.1 是一個 5 億參數的日語自回歸模型，在日語和英語 MT 基準上表現優秀，並可透過 torch-transformers 載入。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 3k / ⭐ 49 / 一個日語持續預訓練的 Mistral‑Nemo 模型（Mistral‑Nemo‑Japanese‑Instruct‑2408），基於 mistralai/Mistral‑Nemo‑Instruct‑2407 建構，可透過 transformers 使用裝置映射與 ChatML 版面提示，並由 Ryosuke Ishigami 以 Apache‑2.0 授權發布。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 3k / ⭐ 11 / Qwen3‑Swallow v0.2 提供日英語 LLM（30B‑A3B 和 32B），採用 CPT、SFT 與 RLVR 訓練，保持強大的數學、程式編寫與推理能力，已發布九個模型及 AWQ‑quantized 變體。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 3k / ⭐ 17 / TokyoTech‑LLM 倉庫提供了 Swallow Llama‑2 系列的 LLaMA‑2 模型，這些模型已加入日文資料，涵蓋 7B、13B 與 70B 變體，並包含 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以來發佈的 7B Plus 版本。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 3k / ⭐ 58 / TinySwallow‑1.5B‑Instruct 是一個 1.5 B 日語指令調校的自回歸語言模型，經由 TAID 從 Qwen2.5‑32B‑Instruct 蒸餾，僅供研究使用。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 148 / LFM2.5‑1.2B‑JP 是一款為日語優化的聊天模型，在日語知識和指令遵循方面優於 LFM2，支援 LoRA 的微調、使用 Transformers、vLLM、llama.cpp 進行推論，並達到 50.7 JMMLU、58.1 M‑IFEval 和 56.0 GSM8K 分數。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 2k / ⭐ 20 / OpenCALM 是 CyberAgent 發布的一系列日語僅解碼器 Transformer 語言模型（參數 160 M–6.8 B），訓練於日語維基百科和 Common Crawl，並以 CC BY‑SA 4.0 授權發行。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 2k / ⭐ 16 / 一個 6 層、512 隱藏單元的 transformer，名為 Japanese GPT‑2 xSmall，訓練於日本 CC‑100 與 Wikipedia 並使用 SentencePiece tokenization；於 2021 年 8 月 25 日以 MIT 授權發布，並託管於 Hugging Face（rinna/japanese‑gpt2‑xsmall），在 arXiv 2404.01657 中被引用。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 2k / ⭐ 21 / 提供由 NII 出品的 1.8 B 參數 llm‑jp‑3.1‑1.8b‑instruct4 日語指令調校模型，兼容 Hugging Face Transformers 及 Torch ≥ 2.3.0，包含預訓練與微調檢查點及使用示例。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 2k / ⭐ 15 / LLM‑jp 提供 13B 與 1.3B 的 transformer 語言模型，包括多個 instruction‑tuned 變體，使用 Megatron‑DeepSpeed 與 Hugging Face Transformers 生態系統構建。
 * [sarashina2.2-1b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1) - 📥 2k / ⭐ 16 / 本倉庫托管 SB Intuitions 的 1 B‑參數自回歸式日本指令模型 sarashina2.2‑1b‑instruct‑v0.1，與其他日本‑BERT 進行日本與英語 MT 及指令任務的基準測試，提供一段 torch‑transformer 使用範例，並警告安全訓練有限。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 1k / ⭐ 25 / 來自國立情報學研究所的 Hugging Face 兼容的以日語為中心的 transformer 模型（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct），已在多樣化的日語和英語語料庫（包括 Wikipedia、Common Crawl、WARP、Kaken、Dolma）上預訓練，並且需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate 與 flash‑attn。
 * [gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - 📥 1k / ⭐ 18 / 由 ABEJA, Inc. 在日本 CC‑100、Wikipedia、OSCAR 上訓練的大型日語 GPT‑2 模型，使用 sentencepiece 進行分詞，可透過 Hugging Face transformers 在 PyTorch 或 TensorFlow 使用，並採用 MIT 授權。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 1k / ⭐ 29 / LFM2.5‑1.2B‑JP 是一個 1.2B 參數的日語文本生成模型，基於 LFM2.5 混合架構構建，優化用於生成和完成任務，托管於 Hugging Face 並可通過 llama.cpp 運行。
 * [llm-jp-3-150m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-150m-instruct3) - 📥 1k / ⭐ 4 / 日本資訊學國立研究所推出的 150 M 參數教學 LLM，可作為符合 Hugging Face 的 Transformer 模型使用，需使用 torch ≥ 2.3.0 與 transformers ≥ 4.40.1。
 * [Sakura-13B-Galgame-GGUF](https://huggingface.co/QuantFactory/Sakura-13B-Galgame-GGUF) - 📥 1k / ⭐ 2 / 一個已量化、可離線使用的 Galgame/輕小說翻譯模型（Sakura-13B-Galgame-GGUF），以 llama.cpp 構建，提供 GPT‑3.5 級別表現、OpenAI‑API 兼容性，以及基於 Qwen/Qwen2 主幹的多種 GGUF 變體，採用 CC BY‑NC‑SA 4.0 授權並附帶非商業使用警告。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 1k / ⭐ 108 / 一個 1.3‑B‑parameter、24‑layer transformer GPT‑1B，在 Japanese C4、CC‑100 以及 Wikipedia 上訓練，於 2022 年 1 月 26 日由 rinna Co. 發布，並以 MIT license 供使用。
 * [llm-jp-3-1.8b-instruct3](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct3) - 📥 1k / ⭐ 2 / Repository hosts the llm‑jp‑3‑1.8b‑instruct3，這是一個由國立資訊研究所開發的 1.8 B 參數日語 LLM，已在日本維基百科與 Common Crawl 上進行預訓練，可直接用於 Hugging Face Transformers（torch ≥ 2.3, transformers ≥ 4.40）。
 * [Gemma-2-Llama-Swallow-2b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-2b-it-v0.1) - 📥 1k / ⭐ 4 / 日語增強的 Gemma‑2 “Swallow” 語言模型，採用持續預訓練和指令微調技術構建，可在 Hugging Face 上下載 2 b、9 b 與 27 b 三種變體。
 * [open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - 📥 1k / ⭐ 4 / OpenCALM 是 CyberAgent 旗下的日本語 decoder‑only Transformer 語言模型套件，參數範圍從 160 M 到 6.8 B，訓練資料來源於日語維基百科及 Common Crawl，並以 CC BY‑SA 4.0 版權發布。
 * [LFM2-350M-PII-Extract-JP](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP) - 📥 1k / ⭐ 56 / LFM2‑350M‑PII‑Extract‑JP 是一個在裝置上執行的 3.5 億參數日文 PII‑擷取模型，匹配 GPT‑5 的表現，允許在合約、電子郵件和醫療報告中對敏感數據進行遮蔽。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 1k / ⭐ 20 / GPT‑OSS‑Swallow v0.1 提供 20B 及 120B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，能在數學與編程任務上匹敵或超越 GPT‑OSS，於 2026 年 2 月發布，包含四種 SFT/RL 變體與即將推出的量化版本。

### fill-mask
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 2M / ⭐ 39 / Japanese‑Roberta‑Base 是由 rinna Co., Ltd. 推出的預訓練遮罩語言模型，含正確載入、token 預處理、position‑id 處理的指引，以及強調需放置於首位的 `[CLS]` token 和一致 tokenization 的使用範例。
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 387k / ⭐ 76 / Japanese BERT‑base 預訓練於 2019 年日本維基百科，使用 IPA 字典與整詞掩碼，12 層、768 維，32,000 詞表，512 令牌序列，1 百萬步；可於 cl‑tohoku/bert‑japanese 在 CC‑BY‑SA 條款下取得。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 373k / ⭐ 9 / Japanese DeBERTa V2 大型模型已在 171 GB 的日語維基百科、CC‑100、與 OSCAR 上訓練，採用字符級 sentencepiece tokenization 與 whole‑word masking，已準備好通過 Hugging Face Transformers 進行下游微調。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 250k / ⭐ 41 / 一個基於 BERT base 的模型，預訓練於約 17 M 日文 Wikipedia 句子（2.6 GB），採用 IPA dictionary 與 WordPiece 進行 tokenization，擁有 12 layers／768‑dim hidden states／12 heads，32 000‑token 詞彙表，於 Cloud TPUs 上訓練 1 M steps，並以 CC‑BY‑SA 3.0 發布。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 67k / ⭐ 6 / 一個 BERT‑base 日語模型（12 層，768 維隱藏狀態，12 頭）在 30 M 句子（約 4 GB）上訓練，使用 Unidic 2.1.2 詞級分詞，隨後進行字級分詞和整詞遮蔽，使用 512 令牌序列、256 批次及 1 M 訓練步驟。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 17k / ⭐ 8 / 一個 BERT‑base 日語模型（12 層，768‑維隱藏，12 頭），在約 1700 萬句來自日語維基百科（2.6 GB）的資料上進行預訓練，使用 MeCab IPA 單詞級分詞，隨後進行字符級分詞，建立一個 4000 單詞詞彙表。訓練程式碼位於 cl‑tohoku/bert‑japanese，並以 CC BY‑SA 3.0 釋出。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 16k / ⭐ 49 / 一個 132 百萬參數的 Japanese ModernBERT 模型，結合 local‑global 與 RoPE attention，在 4.39 T tokens（日語/英語）上訓練，含有 102‑k‑size 的 vocab，最大 token 長度 8,192，並優化為 Flash Attention 2。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 16k / ⭐ 49 / LINE DistilBERT Japanese 是一個 66‑million‑parameter 的 DistilBERT 模型，使用內部 BERT‑base 教師在 131 GB 的日本網路文本上進行預訓練，並於 JGLUE 上評估，採用 MeCab Unidic 與 SentencePiece 進行分詞，於 Apache 2.0 授權下釋出。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 14k / ⭐ 25 / ModernBERT‑Ja‑310M 是一款日語 BERT 變體，結合了 local‑global attention 與 RoPE，已在 4.09 T 個日語/英語文本 token 上訓練，支持 102 400 個詞彙、8 192 token 序列，並被優化以配合 Flash Attention 2。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 8k / ⭐ 26 / Japanese BERT‑base (12 層, 768 hidden, 12 heads) 以 4 GB 的日本 Wikipedia（約 30 M 句）為預訓練資料，使用 Unidic 2.1.2 文字級別分詞、WordPiece 子分詞，與整詞掩碼。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 4k / ⭐ 5 / DeBERTaV2 基礎模型在日本語語料庫（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上進行訓練，並採用 FP‑16 微調以應對 NLU 任務（JSTS、JNLI、JCommonsenseQA）。本模型以 CC BY‑SA 4.0 授權發佈，並獲得日本研究撥款資助。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 3k / ⭐ 30 / 日文 DeBERTa V2 基礎模型，已在 171 GB 日文維基百科、CC‑100 與 OSCAR 資料上使用 Juman++ 斷詞與 SentencePiece Tokenization 進行預訓練，訓練時間三週，使用八台 NVIDIA A100 GPU，已準備好進行微調。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 3k / ⭐ 1 / 一個以 171 GB 日本維基百科、CC‑100 與 OSCAR 文本預訓練的日語 DeBERTa‑V2 基礎模型，採用字元級分詞、全詞遮罩模式，已在 8 台 A100 GPU 上訓練 20 天，並準備好進行下游微調。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 3k / ⭐ 2 / Japanese DeBERTa V2 tiny，預訓練於約 171 GB 的日語 Wikipedia、CC‑100 與 OSCAR 資料庫，需要 Juman++ 詞彙分割，已在 8 顆 NVIDIA A100 GPU 上訓練 33 小時，可進一步微調以應用於下游任務。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 2k / ⭐ 4 / 日本語 RoBERTa‑base 模型，預訓練於 JST 約 10 M 節點醫學科學摘要（約 1.6 GB），使用 SentencePiece Unigram (30k vocab) 分詞，採用 CC‑BY‑4.0 授權，可透過 Hugging Face pipelines 進行微調。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 2k / ⭐ 7 / ModernBERT‑Ja‑30M 是一款日語 BERT 變體，它將局部與全局注意力與 RoPE 混合起來，並在 4.39 TB 的日英文本上訓練，支援 8,192‑token 序列，參數規模從 30 M 至 130 M，並在使用 Flash Attention 2 時表現最佳。
 * [luke-japanese-large](https://huggingface.co/studio-ousia/luke-japanese-large) - 📥 2k / ⭐ 9 / Japanese‑language LUKE，為一種知識增強型 Transformer，將單詞與 Wikipedia 實體視為獨立 token——提供語境化表示並在 JGLUE 上（例如 MARC‑ja 96.5 % 準確率）超越基準，同時針對無實體任務提供輕量版。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 1k / ⭐ 7 / ModernBERT‑Ja‑70M 是一款輕量級的日語 BERT 變體，結合局部與全局注意力與 RoPE，使用 4.39 T 混合語言令牌（詞彙表 102 400，最大 8 192 令牌）訓練，支援 Flash Attention 2，並提供 30 M 至 310 M 參數的多種規格。
 * [llm-jp-modernbert-base](https://huggingface.co/llm-jp/llm-jp-modernbert-base) - 📥 1k / ⭐ 12 / 一個 ModernBERT‑base 模型在 3.4 TB 的日本 llm‑jp‑corpus v4 上訓練，並在兩個階段進行微調（max_seq_len 1024 → 8192），獲得 0.92 JSTS、0.91 JNLI 與 0.88 JCoLA。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 6M / ⭐ 61 / 日語 wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 與 JSUT 上微調，需要 16 kHz 音訊，並可透過 HuggingSound 或 HuggingFace pipelines 使用。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 217k / ⭐ 108 / Kotoba‑Whisper‑v2.2 是一款日語 ASR 模型，擴展了 kotoba‑whisper‑v2.0，整合了 integrated diarization 與 automatic punctuation，透過 HuggingFace‑Transformers pipeline 實現，並與 Asahi Ushio 和 Kotoba Technologies 合作開發。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 36k / ⭐ 141 / Anime Whisper 是一個輕量級的日語 ASR 模型，已在約 5,300 小時的動漫式對白上微調，提供低幻覺、節奏對齊的標點符號，並能準確轉錄非語音聲音和 NSFW 內容，必須在沒有初始提示的情況下運行。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 19k / ⭐ 92 / Kotoba‑Whisper v2.0 是一款從 OpenAI Whisper large‑v3 提煉的日語ASR模型，使用 7.2 million ReazonSpeech 片段訓練，速度比原版快 6.3×，同時在領域測試中匹配教師模型的 CER/WER，並包含 stable‑ts/punctuation 支援及完整訓練程式碼於 GitHub。
 * [japanese-hubert-base-phoneme-ctc](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc) - 📥 11k / ⭐ 5 / 基於 rinna/japanese‑hubert‑base 的微調日語音素 CTC 模型，使用 ReazonSpeech v2 數據與 pyopenjtalk‑plus 標籤訓練，在新版 v2 釋出（prj-beatrice/japanese-hubert-base-phoneme-ctc-v2）中達到更佳準確度。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 9k / ⭐ 56 / NVIDIA NeMo 的 0.6 B‑參數 Hybrid FastConformer‑TDT‑CTC ASR 模型能帶標點符號轉錄日語語音，並且可在 NeMo 框架內進行推論或微調。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 8k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供 6.3 倍更快的蒸餾 Whisper 模型，支援日本語與英語的 ASR 以及雙向語音轉文字翻譯，這些模型由 OpenAI 的 Whisper large‑v3 透過 knowledge distillation 與 cross‑entropy 及 KL‑divergence loss 建構。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 7k / ⭐ 11 / 一個經由 facebook/wav2vec2‑large‑xlsr‑53 在 Common Voice 與 JSUT corpus 微調的日語語音辨識模型，已優化為 16 kHz 音訊輸入。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 3k / ⭐ 18 / Kotoba‑Whisper‑v2.1 是一款日語 ASR 模型，繼承了 kotoba‑whisper‑v2.0，並整合了標點符號後處理流程，能保持相當的 CER 性能，同時實現無縫、能感知標點符號的轉錄。
 * [Qwen3-ASR-1.7B-JA](https://huggingface.co/neosophie/Qwen3-ASR-1.7B-JA) - 📥 3k / ⭐ 5 / Fine‑tuned Qwen3‑ASR‑1.7B for Japanese ASR，優化以準確轉錄專有名詞、組織及產品名稱、漢字濃厚以及日英混合技術術語。
 * [japanese-hubert-base-phoneme-ctc-v3](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v3) - 📥 2k / ⭐ 5 / Fine‑tuned Japanese HuBERT‑base for CTC phoneme recognition (v3)，加入 MeCab N‑best 與 pyopenjtalk‑plus 後處理，使用結合 CTC 和 MeCab 成本的加權損失、更新排除規則，以及新增「ty」音素。
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 2k / ⭐ 25 / Kotoba Whisper v2.0 已轉換為 CTranslate2 格式，可與 CTranslate2 與 faster‑whisper 一同使用，並提供安裝、推理範例、Apple M2 基準測試以及轉換說明。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 1k / ⭐ 38 / reazonspeech-nemo-v2 是一款擁有 619‑M參數的日語長文語音識別模型，基於改進版 Fast‑Conformer 與 Linearly Scalable Attention 架構構建，訓練於 ReazonSpeech v2.0 資料集，透過 subword RNN‑T decoder（3000‑token SentencePiece）提供多小時推理，並以 Apache 2.0 授權方式分發。
 * [avista-large](https://huggingface.co/enactic/avista-large) - 📥 1k / ⭐ 1 / AVHuBERT‑Large 是一個針對日本 AVSR 微調的 Audio‑Visual BERT 模型，基於約 1,300 小時資料構建，可透過 Hugging Face Transformers 或 reazonspeech.avsr 套件取得，並支援可選的口部提取與波束搜尋生成。
 * [japanese-hubert-base-phoneme-ctc-v4](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v4) - 📥 1k / ⭐ 4 / 已微調日本 Hubert‑Base 的 CTC 音素辨識 (v4)，包含更新的句子過濾規則、發音調整，以及將 GPU 切換至 A6000，訓練停止於 110k 步。
 * [parakeet-tdt-0.6b-ja-GGUF](https://huggingface.co/cstr/parakeet-tdt-0.6b-ja-GGUF) - 📥 1k / ⭐ 1 / 一個已轉換為 GGUF 的 0.6 B 日語 Parakeet TDT‑CTC 模型，可與 CrispASR 的 CLI 一起使用進行 TDT 解碼（CTC 回退），在 JSUT 上達到 6.4 % CER，並提供單詞級時間戳。它有完整的 1.24 GB 精確位元構建版本，以及約 470 MB 的 Q4_K 定量化變體（該變體在大約 8 個 token 後會退化，因此推薦使用 F16）。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 1k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一個擁有 **96.7 M** 參數的 **wav2vec 2.0** Base 模型，已在 **ReazonSpeech v2.0 Japanese ASR corpus** 上微調，達到 **13.22 % CER**，可透過 **Hugging Face transformers** 部署，並以 **Apache 2.0 license** 發布。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 610k / ⭐ 80 / Ruri v3 是一個尖端的日本語文本嵌入模型，建立於 ModernBERT‑Ja，支援最多 8,192‑token 輸入、100K‑token 詞彙表、FlashAttention‑加速推論，以及多種尺寸變體，方便快速使用 sentence‑transformer。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 224k / ⭐ 10 / Ruri v3 是一款最先進的日文文本嵌入模型，構建於 ModernBERT‑Ja，支持高達 8,192 tokens、一個 100k‑token 詞彙表、FlashAttention 加速，並提供從 37 M 到 315 M 參數的多種規模。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 83k / ⭐ 24 / GLuCoSE v2 是一款適合 CPU 的日語文本嵌入模型，透過蒸餾與多階段對比學習進行微調，提供優越的語義相似度與檢索性能—在 MIRACL 以及相關基準上超越同等規模模型。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 53k / ⭐ 3 / Ruri v3 提供高性能的日語文本嵌入，最多可達 8192 個 token，擁有 100k token 詞彙表，支援 FlashAttention，並提供多種模型尺寸 (30 m–310 m) 以供透過 sentence‑transformers 進行高效推理與微調。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 40k / ⭐ 47 / PLaMo‑Embedding‑1B 是 Preferred Networks 開發的日本文本嵌入模型，能將日文文本轉換為向量，用於資訊檢索、分類與聚類，在 JMTEB 基準測試上表現優異，且以 Apache v2.0 license 免費提供。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 34k / ⭐ 6 / Ruri v3 是一款最先進的日本語文本嵌入模型，基於 ModernBERT‑Ja 建構，支援長達 8192‑token 序列、10 萬詞彙、FlashAttention，並以 30 M 到 310 M 參數大小提供，以供 sentence‑transformers 使用。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 19k / ⭐ 34 / GLuCoSE 是一個基於 LUKE 的日語句子嵌入模型，輸出 768 維均值池化向量（最多 512 個 tokens），在網路及 NLI/搜尋資料上訓練，於相似度基準上達成 0.864 Spearman 與 0.818 Pearson。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 17k / ⭐ 9 / 包含 Ruri v3 日文文字嵌入（30 M–310 M 參數、8192‑token 限制、JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前綴的 Sentence Transformers 指令，以及幾個日文模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基準結果。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 14k / ⭐ 45 / 一組可釋出的 Ruri v3 日文文本嵌入模型（30m–310m），包含 SentenceTransformer 使用技巧、查詢/段落前綴，以及 JMTEB 基準測試結果，展示它們與其他日文及多語言嵌入模型的比較。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 12k / ⭐ 12 / 日文通用文本嵌入模型 (Ruri‑v3, 30‑310 M 參數, 8192‑token 上限, 高 JMTEB 分數) 以 Sentence‑Transformers 使用範例提供，並與其他日文嵌入進行基準比較。
 * [ruri-large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2) - 📥 10k / ⭐ 10 / Japanese general‑text embeddings repository Ruri 提供 v3 模型，參數範圍從 30 M 到 310 M，並附帶 JMTEB 分數；展示如何使用 sentence_transformers（使用 “クエリ: ” / “文章: ” 前綴）載入它們；並提供多個日本嵌入模型的基準比較結果。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 7k / ⭐ 16 / JaColBERTv2 是一個僅限日文的 ColBERT 基於檢索模型，使用 MMarco（31 個負樣本對每個正樣本、250k 步驟、批次 32）進行知識蒸餾訓練，目前表現優於 multilingual‑e5‑large、BGE‑M3 以及 JaColBERT，完整評估仍待進行。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 3k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一個 768 維的句子轉換器，建立於 studio‑ousia/luke‑japanese‑base‑lite 上，已在 shunk031/jsnli 培訓一個 epoch，並包含聚類、語意搜尋以及同時適用於 Sentence‑Transformers 與 HuggingFace 的範例。
 * [ruri-base-v2](https://huggingface.co/cl-nagoya/ruri-base-v2) - 📥 2k / ⭐ 5 / 此倉庫提供新的日文文字嵌入 v3 模型（30M‑310M 參數，最高 8k 令牌，JMTEB 74‑77），可使用 sentence_transformers（使用 query/passage 前綴）載入，並包含與有監督/無監督 SimCSE、LaBSE、E5 及其他模型的基準比較。
 * [simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) - 📥 1k / ⭐ 15 / 一個從 tohok u/bert‑base‑japanese‑v2 在 JSNLI 數據集上微調的日本 SimCSE 模型，採用 CC‑BY‑SA 4.0 釋出，並可使用 fugashi/unidic‑lite 分詞在 sentence‑transformers 中直接使用。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 1k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B 是一個 1.2 B‑參數的日文文本嵌入模型，建立於 Sarashina2.1‑1B 上，採用多階段對比學習訓練，以在 JMTEB 上達成最先進的分數，同時產生 1,792 維的密集向量，用於語意相似度、搜尋與分類，並在非商業授權下使用。

### feature-extraction
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 81k / ⭐ 56 / 一個日語 T5 模型，預訓練於約 100 GB 的 Wikipedia 與 OSCAR 數據，使用 SentencePiece 分詞，超越了 Google 的多語言 T5，在新聞分類基準上表現更佳，但仍需要微調，且可能產生偏見輸出。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 40k / ⭐ 51 / 一個日本語的 Sentence‑BERT v2，經過在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上微調，並採用 MultipleNegativesRankingLoss，與 v1 相比提升了約 1.5–2 % 的準確率，並以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 形式釋出。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 33k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一個授權為 Apache‑2.0 的日語 CLIP 模型，基於 ViT‑B/16，訓練於翻譯成日語的 CC12M 標題，並於 2022 年 5 月 12 日發布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 24k / ⭐ 30 / LY Corporation 的 clip‑japanese‑base 是一個訓練於約 1 B 影像‑文字配對的日文 CLIP 模型，使用 Eva02‑B Transformer 影像編碼器並配備 12 層 BERT 文字編碼器，於 STAIR 的 R@1 成績為 0.30，於 Recruit 的準確度為 0.89，以及於 ImageNet‑1K 的準確度為 0.58，並支援零樣本影像分類與檢索。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 23k / ⭐ 11 / Japanese Sentence‑BERT (v1) 模型，用於生成句子嵌入，並提供改進版 v2，並可透過 Hugging Face Transformers 與自訂的 `SentenceBertJapanese` 類別示範使用。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 23k / ⭐ 18 / Japanese CLIP 模型 clip‑japanese‑base‑v2，升級至約 2 B 影像‑文字配對並 distillation，將 Eva02‑B 影像編碼器與 12 層 BERT 文本編碼器結合，以達到比其前身更高的 ImageNet‑1k 準確度 (0.708)。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 9k / ⭐ 2 / ja_ginza_electra 是一個 spaCy v3 Python 套件，提供已在 mC4 和 UD_Japanese_BCCWJ r2.8 上微調的日語 ELECTRA 模型（基於 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator），並具備自訂 bunsetu‑phrase detection，依照 MIT license 發佈。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 9k / ⭐ 14 / Japanese Sentence‑LUKE 模型在與 Sentence‑BERT 相同的資料集上進行訓練，表現優於或相當於 Sentence‑BERT，基於 studio‑ousia/luke‑japanese‑base‑lite 建立，並透過 Hugging Face Transformers 的 MLukeTokenizer 與 LukeModel 使用。
 * [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) - 📥 2k / ⭐ 5 / 日本語 HuBERT Base，12 層 transformer 版本與 rinna 原始模型相同，訓練於約19,000 小時的 ReazonSpeech v1 日本語語音資料，並以 Apache 2.0 授權發佈。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 1k / ⭐ 3 / 一款在 JSNLI 上使用監督式 SimCSE 微調的日語 BERT‑base 模型，透過 Sentence‑Transformers 或 HuggingFace 以 CLS pooling 方式公開，訓練於 1 M 範例，batch size 512，學習率 5 × 10⁻⁵，溫度 5 × 10⁻⁵，64‑token 限制，以及 BFloat16 精度。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 1k / ⭐ 25 / Sarashina‑Embedding‑v2‑1B 是一個 1,792 維的日語句子變換器，透過多階段對比學習訓練，達到先進的 JMTEB 分數，可用於語義相似度、搜尋、同義句挖掘、分類和聚類，透過 Sentence‑Transformers 並可加上可選的指令前綴。
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 1k / ⭐ 4 / fastText 是一個輕量級、開源函式庫，可在標準 CPU 上快速學習文字與句子嵌入及分類器，能在數分鐘內以數十億字進行訓練，可被壓縮以供行動裝置使用，並提供分類與語言識別的預訓練向量。

### text-ranking
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 348k / ⭐ 5 / 以日語訓練的 CrossEncoder 重新排序模型，規模從 xsmall（384）到 large（1024），並包含 BGE‑v2‑m3‑v1 模型，附有微調、推理的範例程式碼，以及在 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上的基準分數。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 266k / ⭐ 14 / Ruri‑v3 Reranker 是一款以 ModernBERT‑Ja 為基礎的強大日語文本重排序器，支援多達 8,192 令牌序列、100k 令牌詞彙表、FlashAttention 以及 SentencePiece tokenizer，並可透過 sentence‑transformers 使用。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 55k / ⭐ 7 / 日本 CrossEncoder 重排序模型 覆蓋 xsmall 到 large（含 BGE），已於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 進行評估，並附上可直接使用的 sentence_transformers 與 HuggingFace 整合範例。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 44k / ⭐ 6 / 快速、輕量級的日語 Reranker v2 模型（tiny、xsmall、small、base）具有基準分數和 GPU 速度，可通過 sentence_transformers CrossEncoder 和 transformers ≥ v4.48 （可選使用 flash‑attn 加速）使用，並且亦提供 ONNX/量化版本以供 CPU/ARM 使用。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 5k / ⭐ 2 / 使用 Sentence Transformers（交叉編碼器）構建的日語重排序模型，可透過 `trust_remote_code` 加載，在 JQaRA、JaCWIR 和 MIRACL 數據集上進行基準測試，並由 hotchpotch 組織提供小到大尺寸版本。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 3k / ⭐ 12 / 一個使用 Sentence Transformers 構建的日本交叉編碼器重排序器，展示了對各種尺寸的 Ruri‑Reranker 模型的推理使用和基準結果。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 2k / ⭐ 8 / 一套日本 Reranker v2，發布從 tiny 到 large 的 CrossEncoder 與基礎模型，每個模型皆附有基準分數與 GPU 推論時間，且需要 HuggingFace Transformers ≥ 4.48（可選 flash‑attn 以加速推論）。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / 日文 CrossEncoder Reranker 模型（xsmall、small、base、large、BGE‑v2 m3）隱藏層大小 384–1024，示例推理通過 sentence_transformers 和 Hugging Face，在 JQaRA、JaCWIR、MIRACL 和 JSQuAD 上獲得 0.71–0.97+ 的分數。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 2k / ⭐ 15 / 一套日本 CrossEncoder 重複器（reranker）套件——包括 xsmall、small、base、large 以及 japanese‑bge‑reranker‑v2‑m3‑v1——搭配示例使用、在多個基準上的評估指標與輔助文件。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 1k / ⭐ 6 / 一個小型、高速的日語 re‑ranker 函式庫（v2），提供 tiny‑through‑base 與 cross‑encoder 模型，具有詳細的延遲與準確率統計資訊，需 Transformers ≥ 4.48（可選 Flash‑Attention 2）並支援 ONNX/quantization 用於 CPU/ARM 部署。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 1k / ⭐ 16 / 由 xsmall 到 large 的日文 CrossEncoder 排序模型，使用日語文本訓練，透過 sentence_transformers 提供，並於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上進行評估。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 756k / ⭐ 14 / 一個以新 VNTL 數據集為基礎的 LLaMA 3 Youko qlora 微調模型，優化為準確、逐字的日語視覺小說到英文翻譯，不使用聊天模式，使用預設的 LLaMA 3 提示，並建議採用中性取樣（temperature 0，無重複懲罰）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 182k / ⭐ 12 / Sugoi LLM 14B Ultra (GGUF) 是一個日語轉英語的翻譯模型，BLEU 分數為 21.38——幾乎是其先前分數 13.67 的兩倍——在 RPG‑Maker 方括號文本上擅長，提示遵從性強，並為交互式聊天 UI 生成 JSON 輸出。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 36k / ⭐ 75 / 來自 Opus corpus 的日文-英語 Transformer‑Align MT 模型，使用 normalization 與 SentencePiece 先行處理，在 Tatoeba 測試集上達到 41.7 BLEU 與 0.589 chr‑F。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 7k / ⭐ 123 / PLaMo Translation Model 是 Preferred Networks 為翻譯任務所創建的大規模語言模型，可供 base、post‑trained 以及 evaluation 版本使用，並以 PLaMo community license 釋出，未對聊天或其他下游用途進行 instruction‑tuned。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 3k / ⭐ 33 / FuguMT 是一個由 transformers 與 SentencePiece 建構的日文對英語 Marian‑NMT 翻譯模型，在 Tatoeba 上取得 39.1 BLEU 分數。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 2k / ⭐ 35 / 微調、GGUF‑量化後的 LFM2‑350M checkpoint，適用於近即時雙向日英短至中篇文本翻譯，可透過 llama.cpp 使用。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 1k / ⭐ 55 / FuguMT 是一個基於 Marian‑NMT 的英日翻譯模型，使用 Hugging Face Transformers 和 SentencePiece 構建，於 Tatoeba 上達成 32.7 的 BLEU 分數。
 * [opus-tatoeba-en-ja](https://huggingface.co/Helsinki-NLP/opus-tatoeba-en-ja) - 📥 1k / ⭐ 15 / 英日 Transformer‑Align 機器翻譯模型，15.2 BLEU，基於 opus+bt‑2021‑04‑10 建立，使用 normalization + SentencePiece，托管於 Tatoeba Challenge。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 368k / ⭐ 176 / Manga OCR 是一個 Vision Encoder‑Decoder OCR 工具，能閱讀垂直與水平的日語漫畫文字（包含振假名），適用於多種字體與低品質圖像，且源碼免費提供。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 69k / ⭐ 6 / Meikiocr的 `meiki.text.recognition.v0`——一個基於 D‑FINE 的 MobileNetV4 模型，在日語視訊遊戲文字上微調——為水平文字提供最先進的準確性和延遲，能從 960×32 的輸入中偵測多達 48 個字符，並輸出每個字符的外框與置信度分數。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 51k / ⭐ 3 / meikiocr 提供一款基於 D‑FINE 的開源權重文字偵測模型，適用於遊戲視訊（v0.1 版，採用 MobileNet‑v4 主幹，提供兩種解析度變體與 64 框限制），以及實驗性低延遲 tiny 與 small 變體，已在日本遊戲及漫畫上訓練。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 3k / ⭐ 19 / Sarashina2.2‑Vision‑3B 是一個 3‑B 參數的日本大型視覺－語言模型，建立於 Sarashina2.2‑3B‑Instruct 和 SigLIP 圖像編碼器之上，並在日本 VQA 基準上達到強勁表現。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 2k / ⭐ 3 / Manga OCR 是一個 Vision Encoder‑Decoder 系統，能在各種字體與低品質影像中提供高品質的日本漫畫 OCR，包括帶有假名覆蓋的垂直與水平文字，亦可用於一般印刷日語 OCR。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 1k / ⭐ 30 / Sarashina2.2‑OCR 是一款 3‑B 參數、端到端的 OCR 模型，經過人類偏好優化後，能將日文與英文文件解析為 Markdown，並將表格轉換為 HTML，數學轉換為 LaTeX，圖形轉換為 bounding‑box 註釋；它透過將 SigLIP2 為基礎的視覺編碼器與 Sarashina2.2‑3B‑Instruct LLM 整合，實現高解析度視覺‑語言理解。

### text-classification
 * [bert-for-japanese-twitter-sentiment](https://huggingface.co/LoneWolfgang/bert-for-japanese-twitter-sentiment) - 📥 14k / ⭐ 2 / Fine‑tuned BERT 適用於日文推文情感分析，使用 JTS1k dataset，將推文分類為 negative (0)、neutral (1) 與 positive (2) 標籤，已準備好可與 transformers pipeline 一同使用。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 7k / ⭐ 16 / 在 Amazon 商品評論上微調日本 BERT（cl‑tohoku/bert‑base‑japanese‑v2）以進行情感分類，達到約 81% 的準確率與 0.73 的 F1 分數，在 6 個 epoch 之後，學習率為 2 × 10⁻⁵。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 4k / ⭐ 2 / 在《Large Language Model Introduction》第5章中介紹的日本 BERT‑based 模型，已於 JGLUE JSTS 資料集上進行微調，用於語義相似度評分。此模型包含 Colab notebooks、transformers‑pipeline 使用說明，以及 Apache 2.0 授權。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 2k / ⭐ 15 / 在 chABSA 數據集上訓練的日文情感分析模型，達到 loss 0.0001、accuracy 1.0、以及 F1 1.0。使用 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 構建，使用 Adam 進行優化（learning rate 2e‑05，10 epochs，batch size 16），並通過 `model(**inputs)` 評估。
 * [bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - 📥 2k / ⭐ 9 / Japanese BERT‑Base v3 微調整於 MARC‑ja JGLUE 整體分析資料集，來源自 cl‑tohoku/bert‑base‑japanese‑v3，可與 Hugging Face `pipeline` 一同使用，並以 Apache License 2.0 發佈。

### token-classification
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 15k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日語 NER，可提取八種實體類型（公司、政治/其他組織、設施、產品、事件），透過 `BertForTokenClassification`，在 Stockmark Wikipedia 數據集上訓練，並可透過 `transformers`、`unidic_lite`、`fugashi` 安裝，採用 CC BY‑SA 3.0 許可證。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 9k / ⭐ 26 / 使用 5 週期 Adam (lr 5e‑5, batch 12) 微調 XLM‑RoBERTa‑base，針對日語 NER 資料集（tags PER, ORG, LOC, INS, PRD, EVT）以達成 0.0173 的驗證損失，已於 Transformers 4.23.1 與 PyTorch 1.12.1 發佈。
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 7k / ⭐ 4 / 一個日語專注的 DeBERTa V3 模型，具有 xsmall、base 和 large 三種變體，推理時不使用形態分析器，尊重詞界，使用縮減的詞彙表（僅在 large 型號中使用 BPE），並且與 Hugging Face 兼容。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 3k / ⭐ 11 / Fine‑tuned Japanese BERT‑Base 用於在維基百科資料集上的命名實體識別，已在《Large Language Model Introduction》一書第六章展示，可透過 Hugging Face transformers pipeline 部署（Apache 2.0 授權）。

### text-to-speech
 * [sarashina2.2-tts](https://huggingface.co/sbintuitions/sarashina2.2-tts) - 📥 64k / ⭐ 56 / sarashina2.2-tts 是一個基於 SB Intuitions LLM 的日語中心化 TTS 系統，提供高精度的日語和英語合成、自然表達聲音、零樣本克隆、跨語言一致性以及無縫代碼切換。
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 2k / ⭐ 11 / 一個名為 **tsukuyomi‑wavlm** 的日語 TTS 模型—在 tsukuyomi 語料庫 100 條語句上 fine‑tuned 300 epochs，使用 WavLM discriminator 和 A1/A2/A3 prosody features 於 VITS architecture，匯出為 61 MB 的 ONNX file，能生成 22.05 kHz syntheses。

### audio-to-audio
 * [LFM2.5-Audio-1.5B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF) - 📥 5k / ⭐ 22 / 量化 GGUF 版本的 LiquidAI LFM 2.5‑Audio 1.5B JP 模型，包括語言、音訊編碼器和聲碼器權重（F32/F16/Q8_0/Q4_0），以及使用 llama.cpp 的 ASR 與 TTS CLI/Server 運行器。
 * [LFM2.5-Audio-1.5B-JP](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP) - 📥 1k / ⭐ 65 / 一款輕量化的 1.5 B‑參數、端到端多模態日語語音‑文字模型，能實現即時低延遲的語音轉語音聊天機器人，以及通過交錯或順序生成進行非對話式 ASR/TTS。

### any-to-any
 * [gemma-4-12B-it-qat-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-12B-it-qat-UD-japanese-imatrix) - 📥 19k / ⭐ 9 / 一個 1/4 大小、CPU 友善的日語優化量化 Gemma 4 模型（Apache 2.0），完全在本機運行，提供可選開發者支援和穩健基準。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 1k / ⭐ 133 / PaddleOCR‑VL‑For‑Manga 由 PaddleOCR‑VL 微調，於 Manga109 的對話框裁切圖像上達成 70％完整句子準確率——高於 27％基準的三倍以上——使用多語系資料集，並提供訓練程式碼與開發人員指南。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 124k / ⭐ 11 / Japanese‑language BERT‑Base（12層，768‑次元，12頭）以 Unidic 為基礎的單詞層級加字符層級標記化以及整詞遮蔽，在 CC‑100 和 2023 Wikipedia 上進行預訓練，產生了 7,027‑token 詞彙。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 72k / ⭐ 63 / Japanese BERT‑base (12 層, 768‑維度隱藏, 12 頭, 32k 詞彙) 以完整詞遮蔽在 CC‑100 與 2023‑Jan Wikipedia 上預訓練，使用 Unidic 2.1.2 詞級分詞加 WordPiece，訓練 200 萬步。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 68k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上訓練，使用 Unidic‑lite 詞級分詞，結合 WordPiece 子詞與全詞遮蔽，模型為 24 層、1024 維隱藏、16 頭、32k 詞表；預訓練程式碼位於 cl‑tohoku/bert‑japanese。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 16k / ⭐ 11 / 一個以約 100 GB 的 Wikipedia 與 OSCAR CC‑100 數據（混合 10:1、Byte‑fallback 的 SentencePiece）預訓練的日本 T5‑v1.1 模型，需對下游任務進行微調，包含遷移學習範例程式碼，提示輸出可能存在偏差，且採用 CC‑BY‑SA 4.0 授權。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 9k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一個擁有 80 億參數的 LLM，透過持續預訓練以及在合成日語數據上進行指令調整微調，提升了 Meta 的 Llama 3.1 在日語語言以及程式碼／數學推理方面的表現，同時保持英語流暢度。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 7k / ⭐ 13 / 一個 gguf 格式的 moonshotai 的 Moonlight‑16B‑A3B‑Instruct，已經在 TFMC 的 imatrix 日語資料集上訓練，準備好可與 llama.cpp (CUDA‑enabled) 一同使用，並可透過執行 recipe‑request 提示來展示。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 5k / ⭐ 19 / 日文 DeBERTa V3 基礎版本，預訓練於 LLM‑jp v1.0 的 540 B 個 token，使用已調整的 DeBERTa V3 設定，採用 unigram byte‑fallback tokenizer（無形態學分析器），並進行 fine‑tuned 於 JGLUE NLU 任務。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 4k / ⭐ 17 / 高效能日文 SPLADE v2 透過 WebUI demo 可進行稀疏向量轉換與推理，使用 YAST 訓練，提供 YASEM 嵌入，並報告 JMTEB 基準結果。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 3k / ⭐ 15 / Sarashina2.2 提供 0.5‑B、1‑B、和 3‑B 的語言模型，這些模型由 SB Intuitions 透過三階段流程及合成資料進行訓練，達成優異的日文 QA、數學及編碼分數，同時提供未經指令微調的預訓練權重，可能產生有偏差的輸出。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 75 / Llama‑3‑ELYZA‑JP‑8B 是一款日本優化的 8‑B Llama 3 模型，採用 GGUF (Q4_K_M) 與 AWQ 量化，能以 llama.cpp、LM Studio 或 OpenAI‑相容 API 執行。
 * [kana-whisper](https://huggingface.co/sbintuitions/kana-whisper) - 📥 2k / ⭐ 1 / 一個經過微調的 Whisper large-v3-turbo 模型，能將日語語音轉錄成片假名，作為 Sarashina2.2-TTS 專案內 Joyo Kanji Yomi Benchmark 的 ASR 組件，同時驅動 Kana CER Usage With Transformers 管道。
 * [gemma-4-E2B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E2B-it-UD-japanese-imatrix) - 📥 2k / ⭐ 2 / 一個已轉換為 GGUF 的 Gemma‑4‑E2B‑it 模型，經過針對日語能力的微調，使用 Unsloth® Dynamic Quantization 2.0 構建，加入社群錯誤修復與日語校正資料，可在 CPU（≥8 GB RAM、≥4 GB 硬碟）上執行 via llama.cpp。
 * [Qwen3.5-0.8B-JP-Tuned-v1.0](https://huggingface.co/CloudGoat/Qwen3.5-0.8B-JP-Tuned-v1.0) - 📥 2k / ⭐ 1 / Fine‑tuned Qwen3.5‑0.8B 在 3.72 M 日語 tokens 上，達成 JCommonsenseQA 61.39%、JNLI 49.88%、JSQuAD 54.01% 與 MARC‑ja 70.43%，整體回應率提升 3.53%。
 * [llm-jp-4-kappa-32b-a3b-v0.1-gguf](https://huggingface.co/mmnga-o/llm-jp-4-kappa-32b-a3b-v0.1-gguf) - 📥 2k / ⭐ 2 / 一個 GGUF 轉換版本的 third‑intelligence 的 llm‑jp‑4‑kappa‑32b‑a3b‑v0.1，使用 TFMC/imatrix-dataset-for-japanese-llm 的 imatrix 數據構建，可通過帶 CUDA 支援的 llama.cpp 使用。
 * [sarashina2.2-1b](https://huggingface.co/sbintuitions/sarashina2.2-1b) - 📥 1k / ⭐ 12 / 一款擁有 10 億參數的日語 LLM，名為 Sarashina2.2‑1B，在三個階段訓練：基礎訓練、針對數學/編碼的合成資料微調，以及少量資料任務微調。它在 QA、數學和編碼基準測試上優於先前模型，但仍未進行指令跟隨微調，且可能產生偏見或不準確的輸出。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 22 / 一個 GGUF‑格式的 pfnet 的 plamo‑2‑translate 發行版，基於 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 數據構建，並附有使用 llama.cpp 在支援 CUDA 的硬體上編譯與執行的說明。
 * [llm-jp-moshi-v1](https://huggingface.co/llm-jp/llm-jp-moshi-v1) - 📥 1k / ⭐ 40 / LLM‑jp‑Moshi‑v1 是一個基於 7‑B‑parameter Moshi 架構的實驗性日語全雙工語音聊天模型，經 J‑CHAT 和 Zoom 對話資料微調，並以 Apache 2.0 許可證釋出，附帶適用於 Linux GPU 系統的 web‑UI 示範。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 1k / ⭐ 1 / 一個高度優化的 GGUF 版本，基於 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 與廣泛修復，調校以擅長日語，並可在 llama.cpp 上運行，至少需要 16 GB RAM 與 6 GB 硬碟空間（GPU 為選用）。
 * [t5-base-japanese-web](https://huggingface.co/megagonlabs/t5-base-japanese-web) - 📥 1k / ⭐ 21 / 32K 語彙的 T5 模型，預訓練於日文網路文本（mC4 + Wikipedia），採用字節回退機制，在 TPU v3‑8 上訓練 100 萬步，並以 Apache 2.0 授權發布。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 2M / ⭐ 58 / 聚合自 2009‑2024 年的 NicoNico Live 評論日誌超過 150 GB，包括轉換前、轉換後及實時 NX‑Jikkyo 捕獲，並提供 API 以方便檢索歷史 TV‑broadcast 討論。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 15k / ⭐ 9 / Cauldron‑JA 是一套日本視覺‑語言資料集，包含 44 個子資料集，這些子資料集是使用 DeepL API 將 The Cauldron 翻譯而成，通過 HuggingFace’s datasets library 可取得，授權條件與原始資料集完全相同，提示（prompts）則以 CC‑BY‑4.0 授權釋出。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 12k / ⭐ 32 / FineWeb2 Edu Japanese 交付約 120 million 高品質教育用日語文本（≈89.3 billion tokens）來自 FineWeb2，經 DeepSeek‑API classifier（score ≥ 2.5）過濾，使用 ModernBERT‑Ja‑130M 分詞，並包含小型 token 子集（≤512 tokens）。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 8k / ⭐ 7 / VOICEVOX‑generated synthetic voice dataset comprising 445,793 .wav files (totaling 577 h 51 m 23 s) built from the ITA, つくよみちゃん, and ROHAN corpora.
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 5k / ⭐ 11 / 一份托管於 Hugging Face 的 Reazon Speech v2 Japanese dataset 的鏡像，採用 CDLA‑Sharing‑1.0 發行，使用僅限於《Japanese Copyright Act Article 30‑4》，包含 4,096 個 16 kHz FLAC 音訊檔案以及對應的 TSV/CSV format 文字稿。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 5k / ⭐ 120 / Nemotron‑Personas‑Japan是一個開源、CC BY 4.0資料集，提供高品質的合成生成日本人格資料——包含姓名、性別、年齡、背景、婚姻狀況、教育、職業和地理位置——基於真實世界的人口、地理和個性分佈設計，使用概率圖形模型和GPT‑OSS‑120B進行優化，以提升多樣性、減少偏見、避免模型崩潰，協助主權AI發展並支持商業使用。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 3k / ⭐ 7 / JMedBench 是一個日本醫學領域 LLM 基準，包含 20 個資料集，涵蓋五個任務（MCQA、NER、STS 等），資料來源於 MedMCQA、PubMedQA、MMLU 及其他，每個資料集都有自己的授權，並附有註記指出翻譯可能存在偏差，需人工審核。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 3k / ⭐ 35 / 重構後重新上傳 Galgame VisualNovel 資料集 (OOPPEENN/5669736E6F76656C5F44617461736574)，為了提高 Hugging Face 資料集載入效率，保留所有原始音訊 / 文字，並提供一段提取腳本，支援多種遊戲子集選項。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 3k / ⭐ 46 / 使用者友善、去重的 CSV 資料集，包含來自 Aozora Bunko 的公有領域日語文本，已使用 globis‑org/aozorabunko‑extractor 處理並為現代日語機器學習用途做過清理。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 99 / 一個包含 100 筆樣本的日本語 instruction‑tuning 評估資料集，內含標註任務——從摘要校正、數學推理到翻譯、創意生成及使用者意圖理解——設計用於手動或自動 5‑point rating 的 fine‑tuned models 評估。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 2k / ⭐ 7 / Japanese Medical VQA 12M 是一個可商業使用的多模態資料集，包含超過1200萬張日文醫學影像及說明文字，來源自 Open‑PMC‑18M，採用 Parquet/Webdataset 格式，並包含原始及日文翻譯的影像、豐富的說明文字，以及使用 InternVL3.5、Qwen3‑30B 與 GPT‑oss 120B 產生的 VQA‑風格問答對。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 2k / ⭐ 49 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小時的匿名化 1,033,142 對 eroge 音訊–轉錄配對 (大多為女性，NSFW)，MIT授權，用於學術研究。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 2k / ⭐ 141 / Japanese Anime Speech Dataset V2 提供 292,637 對乾淨的音頻-文本對，約 397.5 小時為 SFW，52.4 小時為 NSFW，存於 128‑kbps MP3 檔案中按安全性分割，專為訓練自動語音識別模型而設。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEB 是一套日語文本嵌入基準，包含 5 個任務（聚類、分類、STS、檢索、重排序）與 28 個資料集，提供一行式評估腳本並邀請社群貢獻。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 2k / ⭐ 24 / 一個由 23,000,000 件個人收集的日本網路小說組成的資料集，總字數為 80,850,000,000 個字元，只允許合法機器學習用途，需提交詳細存取申請。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 1k / ⭐ 19 / JMMMU 是一個日語多模態基準，已擴充十倍至 1,320 個文化多樣化問題 (720 個文化中立，600 個文化特定)，由母語專家翻譯，現在擁有公開排行榜。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 1k / ⭐ 6 / 日文 MC4 資料集卡片 (mc4-ja)
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 1k / ⭐ 2 / WAON 是一個大型、高品質的日語圖像-文字配對資料集，透過規模、SigLIP‑score 過濾以及去重（按 URL、標題和 pHash）建立，並以 Apache 2.0 於 HuggingFace 釋出，用於資訊分析。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 1k / ⭐ 4 / 提供一個日文搜尋/問答資料集，包含每個查詢的分數，這些分數由五個多語言／日文再排序器計算（如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base），並包括每個查詢大約 200 篇正面與負面範例文件的平均分數。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 1k / ⭐ 18 / Databricks‑dolly‑15k‑ja 數據集是一個 DeepL 翻譯的日文版本，為指令微調而由日本 LLM‑jp 專案創建，作者為 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 與 Takumi Okamoto。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 1k / ⭐ 2 / 由 LLM 生成的日語查詢與答案資料集，來源於改寫的 Wikipedia 文字，並以 CC‑BY‑SA 4.0 釋出。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 1k / ⭐ 118 / ReazonSpeech 是一個免費的 FLAC‑encoded 日語語音語料庫，附帶文字稿，提供五種規模，從 8.5 小時到 35,000 小時，可透過 Hugging Face 下載，採用 CDLA‑Sharing‑1.0 授權，並受限於日本版權法第 30‑4 條使用。
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 1k / ⭐ 3 / 從 Hugging Face（if001/oscar_2023_filtered）載入 Oscar 2023 資料集的 312,396 行篩選子集，並在 GitHub 上的 if001/HojiChar_OSCAR_sample 儲存庫提供範例程式碼。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 1k / ⭐ 8 / llm‑jp‑instructions 是一個手動編輯的日語指示資料集 (v1.0)，提供 train、dev 和 test 分割，可透過 load_dataset 存取。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 1k / ⭐ 13 / LLM‑jp 提供一個日語指令調校數據集，來自 oasst2 的英語子集經 DeepL 翻譯（源自 kunishou/oasst2‑135k‑ja）並由 Kiyomaru 與 Kodama 編譯。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 1k / ⭐ 3 / 2010 年的日本網路語料庫已上傳至 HuggingFace，並按 2009 年版權改革為研究授權，包含自動帶標點的文本，這些文本來自形態學解析和轉換腳本。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 1k / ⭐ 2 / 18,612個將Python指令–回應對日文翻譯—使用 GPT‑4o‑mini 生成，保留原始英文提示、程式碼與範例—為訓練、微調、聊天機器人、研究與教育提供多樣的編程任務，全部以 MIT 許可證發布。
 * [Lux-Japanese-Speech-Corpus](https://huggingface.co/datasets/Lami/Lux-Japanese-Speech-Corpus) - 📥 995 / ⭐ 5 / 一個包含原創角色「Lux」的日本語音資料集，提供 96 kHz/16‑bit 原始與已清理的 WAV 檔案、`metadata.csv` 中的逐字稿元資料，以及 `dataset_infos.json` 中的整體資料集資訊，並以 CC BY 4.0 授權供 TTS 研究與應用使用。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 967 / ⭐ 4 / 一個受限、非商業性的衍生資料集，基於 EDINET XBRL 財務資料，禁止再散佈、AI 訓練及商業使用，存取需手動批准。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 934 / ⭐ 6 / JamC‑QA 是一個涵蓋八個日本文化與知識類別的雙語多選題基準測試，並以排行榜指標對比最先進模型。
 * [japanese-qa-reasoning-100k](https://huggingface.co/datasets/hotchpotch/japanese-qa-reasoning-100k) - 📥 912 / ⭐ 3 / 由 fineweb2‑edu‑japanese 文本使用 DeepSeek‑R1 生成的日文問題、關鍵字和答案資料集，包括推理，並包含原始測試集中的測試樣本，授權為 ODC‑BY。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 854 / ⭐ 55 / AnswerCarefully Dataset 提供日語及多語言資料，用於商業或非商業 LLM 安全增強；禁止任何其他用途——包括安全繞過；允許帶歸屬的衍生作品；並附帶創作者對損害或服務變更之非責任免責聲明。
 * [Medical-o1-Reasoning-SFT-Japanese](https://huggingface.co/datasets/ronantakizawa/Medical-o1-Reasoning-SFT-Japanese) - 📥 841 / ⭐ 3 / FreedomIntelligence 的 medical‑o1‑reasoning‑SFT 資料集（19,688 條項目）的日文翻譯，該資料集由 GPT‑4o‑mini 透過 OpenAI Batch API 產生，包含已翻譯的問題、思考鏈推理與答案，以及原始英文文本。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 813 / ⭐ 6 / 量化語音輸入與文字輸入（針對語音語言模型）的智力差距的一個資料集，由從 Elyza‑tasks‑100、M‑IFEval 和 JamC‑QA 基準中合成的音訊組成，分為四個子集；文字使用 CC‑BY‑SA 4.0 授權，音訊僅允許非營利、非再分發使用。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 772 / ⭐ 17 / oasst1‑21k‑ja 是一個由 DeepL 從英文 OASST1 子集衍生而來的日語指令調整資料集，通過日本的 LLM‑jp 合作項目創建；如需聯繫，請發送電子郵件至 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 以及 Okamoto。
 * [japan-law](https://huggingface.co/datasets/y2lan/japan-law) - 📥 760 / ⭐ 22 / 一份包含日本電子政府法規的資料集，包含編號、標題、ID、施行日期、全文，並於2023年8月1日已去除重複項目，只保留最新有效版本。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 743 / ⭐ 47 / 更新了 JGLUE 數據集卡和載入腳本，適用於由 Yahoo Japan 和 Waseda University 創建的日本 NLP 基準，涵蓋文本分類（MARC‑ja、JCoLA）、句子對分類（JNLI）和 QA（JSQuAD、JCommonsenseQA），發布版本已在 GitHub 和 Hugging Face 上連結。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 739 / ⭐ 5 / 來自 Fate/Stay Night 角色「Emilia」的對話與傳說資料集，格式化用於訓練與評估對話語言模型。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 735 / ⭐ 89 / 一個自動翻譯的日語版 databricks‑dolly‑15k dataset，採用 CC‑BY‑SA‑3.0 授權，最後更新於 2023‑05‑11。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 697 / ⭐ 14 / EDINET‑Bench 是一個日本金融基準，評估 LLM 在會計欺詐檢測、盈餘預測以及產業預測等任務，使用十年的 EDINET‑API 公開報告。提供構建與評估代碼，資料集已重新授權為 PDL 1.0。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 663 / ⭐ 155 / Japanese Anime Speech Dataset 提供 73,004 對音頻-文字對（共 110 小時，從 V1 演進至 V5），用於提升 ASR 模型（如 OpenAI 的 Whisper），在開放授權下可供任何使用，若能標明來源將不勝感激。
 * [OpenSakura-DS-260220-LN-ja-zh-COT-Lilith](https://huggingface.co/datasets/OpenSakura/OpenSakura-DS-260220-LN-ja-zh-COT-Lilith) - 📥 661 / ⭐ 2 / OpenSakura‑DS‑260220‑LN‑ja‑zh‑COT‑Lilith 是一個 1.64 百萬行的日文到中文輕小說翻譯資料集（約 18 GB），採用映射式 5 路切分，保留推理內容與結構化欄位，如 uuid、episode 與 segment 索引。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 644 / ⭐ 8 / Rakuda 提供 40 個日文問題—針對歷史、社會與政府的開放式題目，以及針對地理的專門題目—作為基準測試日本 AI 助手的資料，與 vicuna‑eval 相似，並可透過 `datasets.load_dataset` 載入。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 606 / ⭐ 17 / Galgame_Speech_SER_16kHz 是一個 3.7 百萬檔（5,353 小時、104 GB）情感語音資料集，來源於 Galgame_Speech_ASR_16kHz，經本地 LLM 標註，依 GNU GPL v3.0 發佈，禁止商業使用，且訓練於此的模型必須開源，且不強制要求引用。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 604 / ⭐ 5 / Japanese JaQuAD（QG‑Bench 的子集）提供句子級和段落級資料，並以高亮顯示答案 token，用於訓練日語提問生成模型，評估指標包括 BLEU4、METEOR、ROUGE‑L、BERTScore 與 MoverScore。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 604 / ⭐ 3 / 日本語指令資料集，含 632,636 個多回合樣本（約 6.35 億 tokens）以及 GPT‑OSS‑120b 理由痕跡，針對開放式、數學、寫作與多選題 (MCQA) 任務，在 135 個財務主題及 20 個一般主題中使用，旨在微調 LLM 在財務領域的推理能力。
 * [Synthetic-JP-Preference-Dataset-Qwen2.5_72B-191k](https://huggingface.co/datasets/Aratako/Synthetic-JP-Preference-Dataset-Qwen2.5_72B-191k) - 📥 581 / ⭐ 6 / 一個包含 190,854 個項目的日本合成偏好資料集，使用五種開源模型以及 Qwen/Qwen2.5‑72B‑Instruct‑GPTQ‑Int8 構建。透過雙向判定（並反轉順序）選取僅一致的對子，採用 Apache 2.0 授權，但在模型訓練時仍受 Qwen 版權限制。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 573 / ⭐ 16 / 日語及多語系 QA、NLI 與同義句資料集的目錄，說明各資料集的檢索或 QA 任務以及其授權規範（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 559 / ⭐ 46 / Galgame_Speech_ASR_16kHz 是一個 16 kHz ASR 資料集，包含 3.75 百萬對（≈5,354 h），由 Galgame_Dataset 派生，採 GPL v3.0 授權，禁止商業使用，且任何訓練出來的模型必須開源（引用可選）。
 * [JParaCrawl-Filtered-English-Japanese-Parallel-Corpus](https://huggingface.co/datasets/Verah/JParaCrawl-Filtered-English-Japanese-Parallel-Corpus) - 📥 499 / ⭐ 3 / 提供了一份已清理的日文對英文翻譯語料庫，並配備了經過微調的 Mistral/Stable‑LM 模型，用於評估每一對翻譯，只接受高品質的翻譯，拒絕任何不完整、不準確或寫作差的翻譯。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 487 / ⭐ 27 / WRIME 數據集是一個日本語收藏，包含 42,200 篇文章，已用 Plutchik 的八種情緒為作者、三位讀者以及他們的平均值進行標註，並結構為 40k‑train、1.2k‑validation、2k‑test 的分割，供情感分析任務使用。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 487 / ⭐ 3 / WildGuardTestJP 是一份包含 1,725 個樣本的日文評估資料集，透過多階段精煉流程（Seed‑X‑PPO‑7B、gpt‑oss‑120b、Qwen2.5‑72B‑Instruct、gemma‑3‑27b‑it）忠實翻譯自 WildGuardTest，並於 Hugging Face 上以 ODC‑BY 許可發布。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 484 / ⭐ 142 / 日語說明式對話資料集，用於微調 LLM（例如 LoRA），9M+ 範例，最近更新為去除授權的 Alpaca 數據，清理 Wikipedia 和 ALT 輸出，並以 CC‑BY‑SA 4.0 發佈。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 480 / ⭐ 13 / JMMLU 是一個日本大型多任務語言理解基準，包含 7,536 個由教師精心編寫的問題，涵蓋 56 個科目，包含專業醫學、心理學、會計、哲學，以及多種高中學科。
 * [CC-news-2024-July-October-cleaned](https://huggingface.co/datasets/kajuma/CC-news-2024-July-October-cleaned) - 📥 478 / ⭐ 15 / 一個從 2024 年七月至十月抽取的日本新聞語料庫，使用 Uzushio 以 pipeline_03a.conf 過濾設定從 Common Crawl 的新聞子集提取。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 475 / ⭐ 5 / 資料集卡片詳述日語變體 “mc4‑ja‑filter‑ja‑normal”，附加資訊待補充。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 473 / ⭐ 3 / 日文維基百科句子被轉換為各種嵌入，並建立 FAISS 索引，提供 Hugging Face Space 的演示、轉換腳本，以及對搜尋、問答和 OpenAI text‑embedding‑3‑small 在 RAG 中的評估；嵌入採用 OpenAI 授權，其他則採用 CC‑BY‑SA‑4.0。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 473 / ⭐ 6 / J‑HARD‑TTS‑Eval 將短序列穩定性、重複處理和上下文完成作為基準，評估自回歸式日文 TTS 模型的魯棒性，相關資料集可通過 Hugging Face 取得（short, repetition, rhyme, continuation）。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 439 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 資料集的一個 500 個樣本子集，授權為 CC BY 4.0，用於基準測試 EvoVLM‑JP‑v1‑7B。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 427 / ⭐ 22 / 使用英文提示生成的 AI 動漫插圖，以及來自 Phi‑3 Vision 的字幕（英文與日文），已釋出至公共領域供免費使用。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 419 / ⭐ 24 / cc100-ja 是 cc100 資料集的日本語部分，提供為分片 Parquet 檔案。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 411 / ⭐ 7 / JHumanEval 是手工翻譯的日本版 HumanEval benchmark，提供 164 個 Python 程式設計問題，並提供對應的英文與日文註解，旨在評估 Japanese-LLM 程式產生，同時保留原始英文錯誤。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 409 / ⭐ 17 / 一個鏡像版本的 Reazon Speech v2 數據集，包含已經通過 UVR 去噪並去除背景音樂的音訊檔案（在大約十天內使用八顆 A800 GPU 處理了 4096 個檔案中的 3674 個）。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 408 / ⭐ 34 / 一個 409 小時的日本 eroge 語音資料集，經 2-pass loudnorm 處理（‑23 LUFS、‑1 dB peak、11 LRA），由 litagin/anime-whisper 轉錄，已匿名化，存儲為 WebDataset（FLAC、JSON、TXT），主要包含女性聲音，可能存在 AI 轉錄錯誤，並以 MIT‑licensed 供學術研究。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 403 / ⭐ 9 / JMMMU‑Pro 是一個日本的多模態基準，通過 Vibe Construction 建立——結合生成式建模和人工驗證——以產生低成本、高品質的 image‑QA 數據，揭示開源 LMMs 的缺陷並指引未來 VQA 研究。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 375 / ⭐ 6 / Dataset card for “oscar2301‑ja‑filter‑ja‑normal”，為 Oscar 資料庫中日語過濾與正常子集。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 366 / ⭐ 5 / STAIR‑Captions 在 2017 年發布，提供 820,310 條日語字幕，用於字幕生成、多模態檢索和圖像生成，並帶有詳細標註、元資料以及 Creative Commons BY‑4.0 license。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 362 / ⭐ 17 / 一個大規模的 JSONL 資料集，包含約 190 M 個日語「左側上下文–輸入–輸出」三元組，用於平假名到漢字轉換，支援訓練 zenz‑v2.5 系列（medium、small、xsmall），並提供 AJIMEE‑Bench 評估基準，授權為 CC BY‑SA 4.0 或 Common Crawl。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 345 / ⭐ 15 / Jagle 是一個約 920 萬筆的日本多模態後訓練資料集，由圖像–文字配對和 PDF 文本庫構成，用於訓練 LLM‑jp‑4‑VL 9B beta，並證明能提升日語視覺-語言任務的表現。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 328 / ⭐ 10 / 一個日文對英文平行語料庫，將 llm‑jp‑corpus‑v3 的 kaken 子集翻譯成英文，使用 Qwen/Qwen2.5‑32B‑Instruct，特點為自訂翻譯欄位，並以 CC‑BY‑4.0 授權。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 320 / ⭐ 9 / 此為 llm-book/wrime‑sentiment 的資料集卡，提供一個由 WRIME 衍生的二元日語情感分析集合，根據 Avg. Readers_Sentiment 標記為正向或負向（可選擇包含中性案例），並作為《Introduction to Large Language Models》一書的樣本資料。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 312 / ⭐ 7 / Livedoor News Corpus 提供一套日語新聞文章數據集，分為 5 894 個訓練、737 個驗證和 736 個測試實例，已去除 HTML 標籤並以 Creative Commons Attribution‑NoDerivs 授權釋出。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 309 / ⭐ 13 / Dataset 卡片（針對 “wikipedia-ja-20230720” 日文維基百科快照）
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 308 / ⭐ 15 / JGLUE 資料集卡片，使用於《Large Language Model Introduction》一書，來源自原始倉庫，程式碼採用 CC BY‑SA 4.0 許可，資料受發行者授權，引用 Kurihara & Kawahara（以日文）並建立於 Shunsuke Kitada 的倉庫。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 294 / ⭐ 5 / 這份 20,800 檔案的 WAV 數據集包含 195 位日本 AItuber 人格──其中包括參考、原始、描述性和情感語句──並附帶詳細的人格與聲音元資料，準備好透過數據科學 API 進行檢索。
 * [DEJIMA-dataset](https://huggingface.co/datasets/MIL-UT/DEJIMA-dataset) - 📥 292 / ⭐ 4 / 一個日本規模的網路資料集，包含 3.88 M 張圖片、LLM 產生的標題與開放式 QA 對，已經過重複刪除篩選並加入檢測標籤，可供多種變體（simple、refined、detection、all）下載，並托管於 Hugging Face。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 292 / ⭐ 5 / JAMMEval 是七個日本 VQA 數據集的蒸餾基準，經過兩輪人工註釋以消除歧義和非視覺問題，提供對多模態日本任務的視覺‑語言模型可靠評估。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 284 / ⭐ 4 / 一個 266 小時的日語音訊資料集，來源於 Emilia 資料集並透過 Scribe v1（ElevenLabs STT/ASR）分類，配合 Facebook audio aesthetics prefiltering，已在 HuggingFace 與 Discord 上提供以供協作。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 274 / ⭐ 4 / 一組日文與英文網路語料庫，包括 9 B‑token 日文集（JA‑WEB‑9B）、63 B‑token 英文及日文集（EN‑WEB‑63B、JA‑WEB‑63B）以及合成版本，如改寫版 JA‑PARAPHRASE‑63B、指令式 JA‑INSTRUCT‑63B 與翻譯版 JA‑TRANSLATE‑63B，供在資料受限情境下研究對日文 LLM 進行預訓練的資料增強。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 273 / ⭐ 26 / 此倉庫存放了 OpenAssistant/oasst1 資料集的日文翻譯版本，包括帶有錯誤標記的自動翻譯條目、約 2,000 筆人工更正、以聊天格式擷取的子集，以及將資料轉換為指令‑輸出對以便微調的腳本。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/llm-book/ner-wikipedia-dataset) - 📥 272 / ⭐ 4 / 日文 NER 數據集「Wikipedia-based Named Entity Extraction」(v2.0)，用於《Large Language Models: An Introduction》一書，由 Stockmark 創建，並以 CC‑BY‑SA 3.0 釋出。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 271 / ⭐ 3 / 一個經過清理的日語網路語料庫（例如 mc4‑ja），透過非監督式學習聚類成約 10,000 組，可用於合法分析；在 “out” 資料夾中僅列出部分文件為 Parquet 格式，並可透過 Git LFS 下載。
 * [JDocQA-Reasoning](https://huggingface.co/datasets/ricoh-ai/JDocQA-Reasoning) - 📥 271 / ⭐ 5 / 日本 Ricoh 在 GENIAC 專案中發布的「JDocQA Reasoning Bench」基準測試，評估大型多模態語言模型在 1,286 題關於解讀圖表、表格、圖示以及來自實際文件影像中的複雜文字的推理問題上的能力，並透過 LLM‑as‑Judge 系統進行自動打分。
 * [ScreenTalk_JA2ZH-XS](https://huggingface.co/datasets/Itbanque/ScreenTalk_JA2ZH-XS) - 📥 262 / ⭐ 3 / 一個10,000樣本的配對資料集，約30小時的日語音訊與對應的簡體中文文字，採 Parquet 格式（CC BY 4.0），設計用於語音轉文字翻譯以及多語言ASR+MT研究。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 248 / ⭐ 20 / 一個日語 QA 數據集，用於評估 Retrieval‑Augmented Generation (RAG)，由 JAQKET 題目與 Wikipedia 文章構建，帶有金鑰檢索相關性標簽，已於 HuggingFace 和 GitHub 發布，主要以 nDCG@10 作為評分指標。
 * [OpenAI-MRCR-Translation-JPN](https://huggingface.co/datasets/abeja/OpenAI-MRCR-Translation-JPN) - 📥 238 / ⭐ 2 / 一個由LLMs從OpenAI的長篇語境MRCR翻譯而成的日語評估資料集，保留原始結構，同時生成新的助手回應並維持MIT授權。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 233 / ⭐ 18 / 一個適合 NLP 的 Wikipedia 文章資料集，來源自 2024 年 1 月的 HTML 資料快照，保留段落結構、元資料（如消歧、性、暴力旗標、模板、時間戳）以及在 GitHub 上托管的相關抽取腳本。
 * [Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k) - 📥 231 / ⭐ 7 / 一個 39,600 個樣本的日語創意寫作資料集，使用 deepseek-ai/DeepSeek-V3-0324 建構，每條記錄包含兩個 OpenAI‑style 消息回合（instruction_1/output_1 和 instruction_2/output_2），其中有部分 NSFW 內容，並以 MIT 授權釋出。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 222 / ⭐ 5 / 一個 5.6 B‑token 的日英程式碼資料集，來源於 CC‑100、OSCAR‑2301、HPLT v1.2 與 wiki40b‑ja，用於預訓練 Contrail‑200m‑64k，為 LOCAL AI HACKATHON #000 “calm2-chat” 服務，但缺乏句子邊界與困惑度篩選。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 220 / ⭐ 12 / JaQuAD 是 2022 年的日本 QA 資料集，包含 39,696 對 SQuAD‑style 抽取式問答對，來源於 Wikipedia，總量 73.2 MB，當使用 BERT‑Japanese 微調時，F1 分數達 78.92 %（EM 63.38 %）。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 212 / ⭐ 3 / BBH‑ja 提供 BIG‑Bench Hard 資料集的日文翻譯，提供 JSON‑L（輸入、正確目標）格式的評估問題，以及 YAML（輸入、目標）格式的 Chain‑of‑Thought 提示，翻譯使用 PLaMo 模型。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 211 / ⭐ 2 / JCommonsenseQA 是一個日語多選題常識推理資料集——CommonsenseQA 的改編版——授權為 CC BY‑SA 4.0，並以 doi:10.5715/jnlp.30.63 引用。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 211 / ⭐ 2 / 一個多模態日語表格問答資料集，用於直接從年度證券報告表格中提取單元格值，提供圖像、帶有邊界框的 OCR 文本、問題和答案，並採用 CC‑BY‑4.0 許可。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 209 / ⭐ 2 / 日本 Common Voice 17.0 子集已過濾至 649 個客戶 ID，每個包含 30–300 個樣本，按 8:2 分成訓練/驗證，分批成 1,000 個樣本的 Parquet 檔，總計 45,668 個樣本 (CC0 授權)。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 207 / ⭐ 4 / Japanese Explainable Multi‑hop Question Answering dataset 特色為問題、答案與逐步推導，連結 Wikipedia 文章，並更新推導格式及多個版本發布。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 198 / ⭐ 2 / 大型壓縮的 JSON‑Lines 數據集，包含匿名 2ch.sc/2ch.net 論壇討論串，包含討論串 ID、標題、版面與區域資訊、回覆數量，以及完整的貼文元資料（作者、郵件、日期、內容）。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 195 / ⭐ 3 / 一個包含 64,139 項日文姓名的資料集，已按生物性別標記——採用漢字、平假名與羅馬拼音——其 44.9k 訓練集、6.41k 驗證集與 12.8k 測試集的分割方式獲得 ISDA’23 的接受。
 * [swallow-magpie-ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1) - 📥 189 / ⭐ 5 / 一個日英對照指令調教資料集（各 42k 對），作為 Swallow‑Magpie‑Ultra‑v0.1 的一部分發布，用於訓練 tokyotech‑llm 模型，從 magpie‑ultra‑v0.1 中提取，平均品質良好。
 * [abc-multiple-choice](https://huggingface.co/datasets/tohoku-nlp/abc-multiple-choice) - 📥 188 / ⭐ 4 / 一份來自「abc」競賽四選項題目的日語多選擇問答資料集，於非商業授權下釋出供研究使用。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 172 / ⭐ 33 / 一個用於指令‑回覆微調（例如通過 LoRA）的日語聊天數據集，來源於 llm‑japanese‑dataset，剔除日英翻譯示例，提供 1.8–2.5 million 條目，跨版本發布，並以 CC‑BY‑SA 4.0 授權，引用 DOI 10.1109/BigData59044.2023.10386605。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 164 / ⭐ 3 / 資料集卡為「Introduction to Large‑Scale LLM II」一書中使用的 ja‑vicuna‑qa‑benchmark，並由 llm‑jp‑eval 為跨資料集的日語 LLM 評估所創建（Apache 2.0）。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 163 / ⭐ 24 / AutoWikiQA 是最大的免費日語問答資料集，提供超過230萬個手工篩選的問答對，這些問答對自維基百科自動生成，使用 Swallow‑MX 和 LLMs（無規則基模板），以支援知識傳授與檢索增強生成應用。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 162 / ⭐ 6 / Range3 的 wikipedia-ja-20230101 存儲庫提供只包含日文維基百科文本的 Parquet 檔案，這些文本是從完整的維基百科資料集提取並使用 Python 程式碼生成。
 * [jawiki-bullet-points](https://huggingface.co/datasets/hpprc/jawiki-bullet-points) - 📥 158 / ⭐ 4 / 一個基於日語維基百科的項目式資料集，使用 Apache 2.0 授權的 rinna/deepseek‑r1‑distill‑qwen2.5‑bakeneko‑32b 模型生成，並以 CC‑BY‑SA 4.0 方式發佈。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 153 / ⭐ 21 / 這是一份 SNOW T15/T23 Japanese simplification corpus 的資料集卡片，包含 50 k 手動對齊的原始簡化日語 (≤2 k‑word vocab) 與 English translation records，以及 35 k 擴充集，供日英文本簡化與翻譯使用。
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 152 / ⭐ 4 / JP Voice‑Text Dataset for Arknights Waifus：10,905 個日語聲音片段（總計 26.3 小時）來自單一演員角色，適合微調或評估 ASR/ASV 模型。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 147 / ⭐ 34 / Syosetu711K 是一個日本資料集，於 2023 年 3 月 26‑27 日從小説家になろう抓取約 711,700 本小說，提供全文和元資料（標題、作者、NCode、簡介等）供無監督文本生成和分類任務使用。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 147 / ⭐ 33 / 提供日文 RAG 基準，涵蓋金融、電訊、製造、公共、零售五大產業領域，透過發布資料集、自動評估框架，以及比較結果，例如 Claude 3.5‑Sonnet、GPT‑4o 等模型。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 147 / ⭐ 4 / 「Japanese RAG Generator Benchmark (J‑RAGBench)」供應一份多分類 QA 數據集—涵蓋 Integration、Reasoning、Logical、Table 與 Abstention—旨在評估日文 RAG 生成器，並由人力與 GPT‑4.1 建構，且以 CC BY‑SA 4.0 授權發布。
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 146 / ⭐ 3 / 使用 Whisper Large‑V2 從影片中轉錄了麥基爾·庫里蘇（Makise Kurisu）VN 對白，並以 pydub 進行分割；未經清理的文本用於 TTS 模型訓練（版權不屬於本方）。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 145 / ⭐ 2 / COVID‑19 日本 Twitter 數據集提供日本推文 ID 與評估碼 (63–68)，指出 COVID‑19 的相關性以及事實／意見狀態，從而促進文本分類研究。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 144 / ⭐ 4 / 由 Guo 等人重新格式化 Wiki40B 資料集的日語部分
 * [Umamusume-voice-transcription](https://huggingface.co/datasets/TLME/Umamusume-voice-transcription) - 📥 143 / ⭐ 8 / Umamusume‑voice‑transcription 是一個包含 77 個字符的資料集，為每位賽馬角色提供逐字稿檔案，列出其總音訊時長（例如，“東商變革” 799 秒，「北部玄驹」 1128 秒）。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 143 / ⭐ 15 / 一個簡易的 Zundamon 角色設定資料集—由線上來源及管理數據編輯—用於測試 character‑LLMs，提供於 zmnjp.jsonl 與 zmn.jsonl 格式，並依指定授權提供。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 143 / ⭐ 16 / Hachi‑Alpaca 是一個由 Stanford Alpaca 以 ‑mistralai/Mixtral‑8x22B‑Instruct‑v0.1 創建的日本合成資料集，由該模型清理，部署於 Deepinfra，並以 Apache‑2.0 license 釋出給 Alpaca‑jp research。
 * [cc100-ja-documents](https://huggingface.co/datasets/hotchpotch/cc100-ja-documents) - 📥 143 / ⭐ 4 / 將已合併的 line‑split cc100‑ja 資料整合進 HuggingFace 的文件單位，同時保留原始 CC100 license。
 * [japanese-confidential-information-extraction-sft](https://huggingface.co/datasets/akiFQC/japanese-confidential-information-extraction-sft) - 📥 143 / ⭐ 2 / 一個日本SFT資料集，用於從文本中提取11類機密實體，設計為LFM2模型的LoRA微調使用，包含40,897個樣本，分為訓練/驗證集合，輸出JSON且所有鍵皆存在（若缺失則為空列表）。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 136 / ⭐ 10 / JA‑Multi‑Image‑VQA 是包含 39 張圖片、55 個題目的資料集，擁有手工製作的日語 Q&A 用於多圖像 VQA，透過 load_dataset 訪問，文本授權為 Apache 2.0（圖片受限）。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 132 / ⭐ 5 / JAQKET 是一個來自 Wikipedia 的日語開放域問答資料集，提供版本 1.0，包含多選測驗題（13,061 個訓練例子，271 個驗證例子）以及版本 2.0，只包含需要抽取答案的提問提示（2,154 個訓練例子，1,164 個驗證例子），旨在促進問答系統研究。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 130 / ⭐ 6 / Japanese XL‑Sum 子集經 PaLM‑2 15‑gram 重疊過濾，包含 4,215 個訓練、758 個驗證以及 766 個測試範例。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 130 / ⭐ 2 / 一份日本線上廣告資料集，用於五個 NLP 任務——廣告可接受性、一致性、性能估算、A3 認識與相似度，並以 TSV 格式提供 train/dev/test 拆分。
 * [pjsk-emu-dataset](https://huggingface.co/datasets/chitsanfei/pjsk-emu-dataset) - 📥 127 / ⭐ 11 / 一個包含 2735 個檔案的 WAV 語音資料集，用於 so‑vits‑svc 4.0，採用 CC‑BY‑NC 4.0 授權（需署名且禁止商業使用），僅可透過電子郵件申請取得，供研究用途。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 124 / ⭐ 9 / JSICK 是一個日英 NLI 與 STS 數據集，透過翻譯 SICK 語料庫而創建，包含一組壓力測試資料，用於探討詞序與格助詞處理，分別有 1,666、797 和 1,006 對句子對應不同的語法關係。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 118 / ⭐ 4 / AnimuSubtitle‑JP 是一個使用 Advanced SubStation Alpha 格式的日語字幕資料集，可透過 Python ‘ass’ library 或像 Aegisub 這類編輯器使用，並採用 ODC‑By 授權。
 * [sakura_japanese_dataset](https://huggingface.co/datasets/saldra/sakura_japanese_dataset) - 📥 117 / ⭐ 20 / Sakura_dataset 是一個商業級、超小型、高品質的日語資料集，涵蓋常識 QA、數學問題（Calc‑ape210k）以及自訂日語常識題目，採用 DbCL v1.0 授權，可與 rinna/japanese‑gpt‑neox‑3.6b 等模型進行 LoRA 微調使用。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 116 / ⭐ 13 / 僅包含足夠長度的多發佈者記錄、已標準化發佈者名稱及平衡主要發言者的日本角色扮演對話資料集，供機器學習應用。
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 115 / ⭐ 24 / RealPersonaChat 是一個約 14,000 條項目的日語對話語料庫，將會話資料與說話者的人格特質（Big Five）及其評估分數和人口統計屬性配對，同時警告不要進行再識別或冒充。
 * [llmjp-kaken](https://huggingface.co/datasets/hpprc/llmjp-kaken) - 📥 113 / ⭐ 6 / 將 llm-jp-corpus-v3 的 kaken 子集轉換為 Hugging Face 格式，並在可能的情況下從每個網址附加檢索到的文章標題，授權 CC‑BY 4.0。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 111 / ⭐ 16 / 日本語 Alpaca 資料，來源於 masa3141 的日本語 Alpaca‑LoRA 工作，並引用原始倉庫以供進一步細節參考。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 111 / ⭐ 7 / 一個經過重新格式化以符合 SentenceTransformers 友好列與結構的日本資料集，透過 RelRank 分數篩選為正向（≥0.7）和負向（≤0.3）對，來自多個 HuggingFace 資源，用於對比學習。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 110 / ⭐ 2 / KokoroChat 是最大的日本心理諮詢對話資料集—由 480 位受訓顧問進行了 6,589 次角色扮演會談，平均每次 91 則發言—包含豐富且長篇的對話、詳細的 20 維客戶回饋，並支援同理心回應生成、對話評估以及心理健康語言模型的研究，並已於 ACL 2025 接受。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 107 / ⭐ 14 / 一份採用 CC‑BY‑SA 3.0 授權的日文實體抽取資料集，來源自維基百科，存放於 https://github.com/stockmarkteam/ner-wikipedia-dataset/，並由 Stockmark Inc. 開發。
 * [JA_audio_JA_text_180k_samples](https://huggingface.co/datasets/Sin2pi/JA_audio_JA_text_180k_samples) - 📥 106 / ⭐ 9 / 一組正則表達式規則，用於在 MeCab‑IPADIC Neologd 字典中篩選並處理日語術語。
 * [WAON](https://huggingface.co/datasets/llm-jp/WAON) - 📥 106 / ⭐ 8 / WAON 是一個大型且高品質的日語影像-文字配對資料集，專為視覺語言模型設計。其採用嚴格過濾（影像尺寸、SigLIP 分數）和去重（URL、說明文字、感知雜湊），並以 Apache 2.0 授權釋出，供「資訊分析」用途使用。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 104 / ⭐ 11 / 一個高品質的合成日語數學題目資料集，具有已驗證的鏈式思考推理，透過 Qwen2‑7B‑Instruct 將 PRM800K 和 GSM8K 進行翻譯並篩選正確性後構建，可透過 Hugging Face datasets library 獲取。
 * [alpaca_jp_python](https://huggingface.co/datasets/HachiML/alpaca_jp_python) - 📥 103 / ⭐ 8 / 使用 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 生成的合成日語 Alpaca 數據集，並通過 Deepinfra 精煉，在 HachiML 專案下以 Apache 2.0 授權發布。
 * [danbooru-ja-tag-pair-20241015](https://huggingface.co/datasets/p1atdev/danbooru-ja-tag-pair-20241015) - 📥 101 / ⭐ 9 / 一個 150 K 條目資料集，包含 Danbooru 標籤及其日文翻譯（於 2024‑10‑15 更新），由擴充的 wiki 資源構建，經 FastText 過濾以移除非日語標籤，並使用 Calam Chat 的少量示例翻譯補全缺失項目。
