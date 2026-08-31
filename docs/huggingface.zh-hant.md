# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專門收錄日語NLP相關的Python函式庫、LLM、詞典和語料庫資源的精選列表。
本頁面列出了Hugging Face上可用的日語NLP專用模型和資料集。目前包含221個模型和155個資料集。

_更新於2026年8月31日_

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
   * [audio-to-audio](#audio-to-audio)
   * [image-text-to-text](#image-text-to-text)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | 模型名稱 | Downloads | Likes | 類別 |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 12M | ⭐ 62 | automatic-speech-recognition |
| 2 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 788k | ⭐ 179 | image-to-text |
| 3 | [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) | 📥 547k | ⭐ 11 | automatic-speech-recognition |
| 4 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 542k | ⭐ 15 | text-generation |
| 5 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 497k | ⭐ 9 | fill-mask |
| 6 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 430k | ⭐ 82 | sentence-similarity |
| 7 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 340k | ⭐ 10 | sentence-similarity |
| 8 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 337k | ⭐ 76 | fill-mask |
| 9 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 327k | ⭐ 17 | translation |
| 10 | [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) | 📥 317k | ⭐ 15 | text-ranking |
| 11 | [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) | 📥 282k | ⭐ 38 | sentence-similarity |
| 12 | [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) | 📥 198k | ⭐ 24 | sentence-similarity |
| 13 | [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) | 📥 192k | ⭐ 5 | feature-extraction |
| 14 | [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) | 📥 188k | ⭐ 56 | feature-extraction |
| 15 | [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) | 📥 168k | ⭐ 6 | text-ranking |
| 16 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 150k | ⭐ 42 | fill-mask |
| 17 | [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) | 📥 139k | ⭐ 64 | others |
| 18 | [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) | 📥 132k | ⭐ 51 | fill-mask |
| 19 | [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) | 📥 130k | ⭐ 51 | feature-extraction |
| 20 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 128k | ⭐ 11 | others |

### Datasets-ranking

| # | 資料集名稱 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 4M | ⭐ 80 |
| 2 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 5k | ⭐ 34 |
| 3 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 4k | ⭐ 7 |
| 4 | [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) | 📥 4k | ⭐ 92 |
| 5 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 4k | ⭐ 127 |
| 6 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 4k | ⭐ 36 |
| 7 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 3k | ⭐ 9 |
| 8 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 3k | ⭐ 19 |
| 9 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 2k | ⭐ 48 |
| 10 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 101 |
| 11 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 2k | ⭐ 7 |
| 12 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 2k | ⭐ 47 |
| 13 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 2k | ⭐ 12 |
| 14 | [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) | 📥 1k | ⭐ 5 |
| 15 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 1k | ⭐ 6 |
| 16 | [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) | 📥 1k | ⭐ 5 |
| 17 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 1k | ⭐ 147 |
| 18 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 1k | ⭐ 49 |
| 19 | [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) | 📥 1k | ⭐ 3 |
| 20 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 1k | ⭐ 20 |

## Models
### text-generation
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 542k / ⭐ 15 / 一個 12 層、768 隱藏層的日本 GPT‑NeoX 模型，訓練於 CC‑100、C4 和 Wikipedia，兼容 Huggingface，並可選擇使用一個玩具前綴調優權重，使每句結尾強制出現笑臉表情符號。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 105k / ⭐ 19 / Llama 3.1 Swallow 是一組 8‑B 和 70‑B 模型，繼續對 Meta 的 Llama 3.1 進行預訓練以提升日語表現，然後在合成日語數據上進行 instruction‑fine‑tune，提供多個已發佈的變體，具有與 gemma‑3‑27b‑it 相當的對話行為改進。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 89k / ⭐ 8 / LLM‑jp‑3‑150m — 來自日本情報學研究院 LLM 研發中心的 150M 參數日語語言模型，已以 Hugging Face Transformers 格式發佈，需安裝 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，並以日語維基百科、Common Crawl、WARP/PDF、WARP/HTML 以及 Kaken 數據，使用 unigram byte‑fallback tokenizer 進行預訓練。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 81k / ⭐ 16 / SB Intuitions 的 Sarashina2.2‑0.5B instruct v0.1 是一個 5 億參數的日語自回歸模型，在日語和英語 MT 基準上表現優秀，並可透過 torch-transformers 載入。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 80k / ⭐ 59 / 一個 2.7‑B 參數的日語 GPT‑NeoX 模型，由 ABEJA Inc 在日語 CC‑100 與 OSCAR 上訓練，可透過 Hugging Face Transformers pipelines 或 PyTorch 使用，並以 MIT 授權釋出。
 * [Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4) - 📥 73k / ⭐ 2 / 在 Qwen3‑Swallow v0.2 中，這些雙語日英大型語言模型（30B‑A3B / 32B）被通過 CPT、SFT 與 RLVR 訓練，以保持數學和編碼性能、提升推理能力，並已在 Hugging Face 上釋出多個量化版本。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 45k / ⭐ 21 / OpenCALM 是由 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 之下發佈的一套僅解碼器的日語 transformer 語言模型（160 M–6.8 B 參數），經日本維基百科與 Common Crawl 訓練，可透過 Hugging Face 的 torch‑transformers 使用。
 * [LFM2.5-1.2B-JP-202606](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606) - 📥 20k / ⭐ 76 / LFM 2.5‑1.2B‑JP‑202606 是一款高效能、通用的日語聊天模型，在知識、指令遵循、數學、程式碼與工具使用方面優於同類 200 億參數以下的模型，適合開發者打造具有文化細膩度的日語應用。
 * [llm-jp-4-33b-thinking](https://huggingface.co/llm-jp/llm-jp-4-33b-thinking) - 📥 13k / ⭐ 39 / 存放 NII 的 LLM 研究中心所開發的 llm‑jp‑4‑33b‑thinking 33 B‑parameter transformer 模型的倉庫，經由監督式與偏好優化進行微調，並提供實務使用指南。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 9k / ⭐ 21 / Llama3 Swallow 是一款日本增強版 Meta Llama 3 系列，於 2024 年 7 月 1 日發布，提供 8B 與 70B 兩種版本，包含 Instruct 與 chat 形式，並使用 SFT 與 Chat Vector 在 Megatron‑LM 上微調，並在關鍵的日本 NLP 任務上進行基準測試。
 * [LFM2.5-1.2B-JP-202606-ONNX](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-ONNX) - 📥 9k / ⭐ 6 / 將日本 LFM2.5‑1.2B 模型匯出為 ONNX，以便於在 ONNX Runtime、Transformers.js 與 WebGPU 上進行跨平台推論，提供多種精度變體（FP32、FP16、INT4/FP16 混合）以及建議的 WebGPU 友好 INT4+FP16 格式。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 實驗性日本模型，透過採用 chat‑vector 方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 與 Meta‑Llama‑3‑8B‑Instruct 之間的差異，升樣後應用於 Meta‑Llama‑3‑70B‑Instruct，顯示變化不大，並計畫未來擴充。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 8k / ⭐ 18 / 以 Shisa 7B 數據微調了 Japanese Stable LM Base Gamma 7B，並在 JA MT‑Bench 上取得優異成績。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 8k / ⭐ 3 / Qwen3‑Swallow v0.2 提供 30‑B 和 32‑B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，提升日語準確度、翻譯、數學與編碼能力，以達到或超越原始 Qwen3，提供九種模型（CPT、SFT、RL）以及 AWQ‑quantized 版本，並同時發布 GPT‑OSS‑Swallow。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 8k / ⭐ 17 / 一套日本大型語言模型（1.8 b 至 172 b beta1，含 instruct 變體）來自 NII 研究發展中心，以 Hugging Face Transformers 格式打包，並在混合的日文、英文以及網路語料上預訓練，總 token 數量超過 1 trillion，需至少 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 7k / ⭐ 12 / llm‑jp‑4‑8b‑instruct 是 NII 的 LLM‑jp‑4 系列 4.1 B 參數的日語 LLM，先在大規模語料庫上進行預訓練，接著僅用監督式指令資料微調（不使用 DPO/REINFORCE），並附有類似食譜風格的使用指引與 byte‑fallback unigram tokenizer。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 6k / ⭐ 151 / Llama‑3‑ELYZA‑JP‑8B 是 ELYZA 推出的日語改良版，8 億參數的 Llama 3 模型，已在 Meta‑Llama‑3‑8B‑Instruct 上為日語進行微調。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 6k / ⭐ 39 / 提供由 SB Intuitions 推出的自回歸日語語言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已與其他模型進行基準測試，且附帶示例使用腳本，並註明安全訓練有限。
 * [asmr-qwen3.5-9b-zh-cn-echo-mtp-gguf-v0.1](https://huggingface.co/mmis1000/asmr-qwen3.5-9b-zh-cn-echo-mtp-gguf-v0.1) - 📥 6k / ⭐ 2 / Fine‑tuned Qwen3.5 MTP in GGUF format that translates Japanese ASMR transcriptions into Simplified Chinese while echoing the source text, applying domain glossaries, and preserving emotion with several quantized versions (q4_k_m, q6_k, q8_0, bf16).
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 5k / ⭐ 10 / 此存儲庫提供 GGUF 格式、量化的模型檔，適用於 Stability AI 的日文 StableLM Instruct Gamma 7B，該模型由 Massed Compute 硬體製成，並屬於 TheBloke 的 a16z 資金支持的 LLM 專案的一部分。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 5k / ⭐ 48 / 提供 NII 的 8B 參數 LLM‑jp‑4‑8b‑thinking 日文語言模型，已經以 pre/​mid‑training 訓練並通過 SFT/DPO 對齊，已準備好與 torch‑transformers 一起使用，並附有詳細的 cookbook 指南。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 5k / ⭐ 85 / Rinna 的 24 層、1024 隱藏單元的日本 GPT‑2‑medium 模型，使用 CC‑100 和 Wikipedia 進行訓練，採用 SentencePiece 分詞，已在 rinna/japanese‑pretrained‑models repo 中提供（MIT‑licensed，於 2021 年 4 月 7 日發布，於 2021 年 8 月 25 日更新）。
 * [llm-jp-4-33b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-33b-thinking-gguf) - 📥 5k / ⭐ 9 / LLM‑jp‑4‑33b‑thinking‑gguf 是來自日本情報院（National Institute of Informatics）的 33 B 日語模型，已使用 SFT 和 DPO（無 RL）進行預訓練，可透過 llama.cpp 的 LLM‑jp fork 使用，並在其食譜中包含詳細的使用說明。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking-gguf) - 📥 4k / ⭐ 8 / 大型語言模型 llm-jp-4‑32b‑a3b‑thinking‑gguf 來自 NII 的 LLM R&D Center，提供 32 B 個參數，使用預訓練/中階訓練加上 SFT/DPO（或僅 SFT 用於指令版本），並透過食譜提供使用指南。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 4k / ⭐ 13 / Qwen3‑Swallow v0.2 提供日英語 LLM（30B‑A3B 和 32B），採用 CPT、SFT 與 RLVR 訓練，保持強大的數學、程式編寫與推理能力，已發布九個模型及 AWQ‑quantized 變體。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 4k / ⭐ 24 / Llama 3.1 Swallow 是一系列經過日本優化的 8B/70B Llama 3.1 模型，透過持續預訓練和日本專用說明微調進行訓練，最新的 8B‑Instruct‑v0.3 在日本 MT‑Bench 上取得了最先進的成果。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 4k / ⭐ 141 / 一個九十億參數的日文優化 LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，於 2024 年 9 月以前的資料進行訓練，採用混合的 Mamba‑2/MLP/4‑layer‑attention 架構，並在 Nemotron‑Personas‑Japan 工具呼叫資料集中進行微調，可選擇在產生最終答案前生成可控的推理回溯，且可商業使用。
 * [Qwen3-Swallow-8B-CPT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2) - 📥 4k / ⭐ 1 / 雙語 30 B 及 32 B 參數 LLM——Qwen3‑Swallow v0.2，以 CPT、SFT 與 RLVR 構建，能在日文、日英翻譯、數學與程式編寫上表現卓越，與 Qwen3 相當或更優，並以 AWQ 量化形式於 Hugging Face 發佈。
 * [llm-jp-3-440m](https://huggingface.co/llm-jp/llm-jp-3-440m) - 📥 4k / ⭐ 1 / LLM‑jp‑3‑440m 是一個符合 Hugging Face 標準的日語 transformer 模型（0.44 billion 參數），屬於 NII 的 LLM‑jp‑3 系列，已在約 1 trillion tokens 上預訓練，且需要 torch ≥2.3.0、transformers ≥4.40.1、accelerate ≥0.29.3 與 flash‑attn ≥2.5.8。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 4k / ⭐ 153 / LFM2.5‑1.2B‑JP 是一款為日語優化的聊天模型，在日語知識和指令遵循方面優於 LFM2，支援 LoRA 的微調、使用 Transformers、vLLM、llama.cpp 進行推論，並達到 50.7 JMMLU、58.1 M‑IFEval 和 56.0 GSM8K 分數。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking-gguf) - 📥 4k / ⭐ 15 / LLM‑jp‑4‑8b‑thinking‑gguf 是由國立情報學研究所（National Institute of Informatics）開發的日本大型語言模型（≈8 B 參數），在中途訓練階段完成預訓練，並透過監督式學習與直接偏好優化進行微調，以產生「思考」變體。此模型以 GGUF 格式提供，附有詳細使用說明的食譜（cookbook）。
 * [japanese-stablelm-instruct-beta-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-7B-GGUF) - 📥 3k / ⭐ 1 / 倉庫提供使用Massed Compute硬體量化的GGUF格式7B日語StableLM Instruct Beta模型，已準備好可與llama.cpp及熱門AI UI框架一起使用。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 3k / ⭐ 7 / 一個存儲庫托管國立情報學研究院 LLM 研發中心的 8.6 B‑parameter llm‑jp‑4‑8b‑base transformer，該模型經由預訓練與中訓練，隨後進行監督式微調與直接優先權優化（未使用強化學習），並提供 PyTorch‑transformers 使用指南。
 * [Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF) - 📥 3k / ⭐ 2 / 以日語為主的低位元 GGUF 量化，針對 Qwen 3.5‑35B‑A3B 模型使用在日文文本上校準的 Importance Matrix，降低安全過濾器並建議使用提供的 .GGUF 檔案。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 3k / ⭐ 37 / 一個32十億參數的日語 transformer LLM (llm‑jp‑4‑32b‑a3b‑thinking)，來自國立情報學研究所 (National Institute of Informatics)，預訓練並通過有監督微調與直接偏好優化進行調整——未使用強化學習——採用 unigram byte‑fallback tokenizer。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 3k / ⭐ 28 / rinna 的日語 GPT‑2 small 為 12 層、768 隱藏單元的 transformer，訓練於日語 CC‑100 和 Wikipedia，使用 SentencePiece 進行分詞，於 2021 年 8 月 25 日以 MIT 版發布（Hugging Face：rinna/japanese‑gpt2‑small，詳見 https://arxiv.org/abs/2404.01657）。
 * [Llama-3.1-Swallow-8B-Instruct-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2) - 📥 3k / ⭐ 16 / 由持續預訓練和指令微調於 Meta 基礎模型上建構的日本語增強 Llama 3.1 語言模型（8B 和 70B），以 Llama‑3.1‑Swallow‑v0.x 與 Instruct 變體形式釋出，並使用以日文為中心的資料。
 * [aibuncho-japanese-novel-gpt-j-6b-gguf](https://huggingface.co/mmnga/aibuncho-japanese-novel-gpt-j-6b-gguf) - 📥 3k / ⭐ 4 / 已將日本小說 GPT‑J‑6B 轉換為 GGUF，供 llama.cpp（分支 mmnga‑dev）使用，並提供了使用範例，但請注意當 llama.cpp 採用原生 gptneox 或 gpt2 支援時可能會失效。
 * [DeepSeek-R1-Distill-Qwen-32B-Japanese](https://huggingface.co/cyberagent/DeepSeek-R1-Distill-Qwen-32B-Japanese) - 📥 3k / ⭐ 254 / 一個經日語微調的 DeepSeek‑R1‑Distill‑Qwen‑32B 模型（MIT 授權），用於透過 transformer 生成文本，使用自訂提示格式並支援串流輸出。
 * [japanese-stablelm-instruct-beta-70B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-70B-GGUF) - 📥 3k / ⭐ 12 / 提供 GGUF 格式、硬體量化的模型檔案，用於 Stability AI 的 70‑billion‑parameter 日本版 StableLM Instruct Beta，準備好與 LLaMA‑cpp‑based 工具一起使用。
 * [jinen-v1.1-beta.gguf](https://huggingface.co/togatogah/jinen-v1.1-beta.gguf) - 📥 3k / ⭐ 1 / 一個 GGUF 格式的「jinen」日語假名-漢字轉換模型原型（v1.1‑beta），針對 NFKC 正規化提示進行優化，在 AJIMEE‑Bench 上測試，Accuracy@1 80%，並提供各種量化版本（f16、Q8_0、Q5_K_M、Q4_K_M）。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 2k / ⭐ 35 / LFM2.5‑1.2B‑JP 是一個 1.2B 參數的日語文本生成模型，基於 LFM2.5 混合架構構建，優化用於生成和完成任務，托管於 Hugging Face 並可通過 llama.cpp 運行。
 * [LFM2.5-1.2B-JP-202606-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-GGUF) - 📥 2k / ⭐ 27 / Hybrid LFM2 模型來自 Liquid AI，例如 1.2 B 的日語 GGUF 版本，提供高品質、快速且記憶體效率高的邊緣 AI，可在裝置上部署並透過 Hugging Face repo 使用 llama.cpp 本地執行。
 * [Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF) - 📥 2k / ⭐ 2 / 針對日語的 imatrix GGUF 量化的已消融 Qwen3.6‑35B‑A3B‑uncensored‑heretic 模型，以日語文本校準以提升日語生成品質，但安全過濾器已被顯著削弱。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 2k / ⭐ 17 / TokyoTech‑LLM 倉庫提供了 Swallow Llama‑2 系列的 LLaMA‑2 模型，這些模型已加入日文資料，涵蓋 7B、13B 與 70B 變體，並包含 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以來發佈的 7B Plus 版本。
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 2k / ⭐ 12 / 東京Tech-LLM 的大型語言模型，基於 LLaMA‑2 並以日文資料（SFT）微調，包括 Swallow‑7b/13b/70b 變體及其 instruct、NVE 和「plus」版本，自 2023 年 12 月至 2024 年 4 月發布。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 2k / ⭐ 25 / 來自國立情報學研究所的 Hugging Face 兼容的以日語為中心的 transformer 模型（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct），已在多樣化的日語和英語語料庫（包括 Wikipedia、Common Crawl、WARP、Kaken、Dolma）上預訓練，並且需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate 與 flash‑attn。
 * [ELYZA-japanese-Llama-2-13b-fast-instruct-GGUF](https://huggingface.co/second-state/ELYZA-japanese-Llama-2-13b-fast-instruct-GGUF) - 📥 2k / ⭐ 1 / 量化的日本版 LLaMA‑2‑13B Fast Instruct 模型（各種 GGUF 格式）供 LlamaEdge v0.2.8+ 使用，提供多種尺寸-品質折衷方案以及命令列或 wasm API 範例。
 * [Lumi-v2-llm-jp-4-8b](https://huggingface.co/SousiOmine/Lumi-v2-llm-jp-4-8b) - 📥 2k / ⭐ 2 / Lumi‑v2‑llm‑jp‑4‑8b 是 llm‑jp/llm‑jp‑4‑8b‑base 的 ChatML 模板化 SFT，訓練資料約 1.7 B tokens，來源於公共與自訂資料集，例如 NVIDIA 的 Nemotron SFT collections、Open‑SWE Traces、NRI‑AI financial reasoning，以及 OpenResearcher data。
 * [japanese-stablelm-base-beta-70B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-base-beta-70B-GGUF) - 📥 2k / ⭐ 2 / 提供由 Stability AI 生成的 GGUF‑量化 70 B 日語 StableLM Base Beta 模型檔案（使用 Massed Compute 硬體），並附上 a16z 補助、TheBloke Discord、Patreon 的連結，以及兼容的 UI 和庫，如 text‑generation‑webui、KoboldCpp、LM Studio、LoLLMS、Faraday.dev、ctransformers 與 llama‑cpp‑python。
 * [Wanabi-Gemma4-31B-GGUF](https://huggingface.co/kawaimasa/Wanabi-Gemma4-31B-GGUF) - 📥 2k / ⭐ 9 / 一個針對 Google 的 Gemma 4 31B 進行微調的 GGUF 版本，已為 Project Wannabe 的結構化提示格式與日文創作寫作進行優化，同時保留一般對話與推理功能，可用於各種聊天 UI。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 2k / ⭐ 20 / GPT‑OSS‑Swallow v0.1 提供 20B 及 120B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，能在數學與編程任務上匹敵或超越 GPT‑OSS，於 2026 年 2 月發布，包含四種 SFT/RL 變體與即將推出的量化版本。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 58 / TinySwallow‑1.5B‑Instruct 是一個 1.5 B 日語指令調校的自回歸語言模型，經由 TAID 從 Qwen2.5‑32B‑Instruct 蒸餾，僅供研究使用。
 * [zenz-v2.5-medium](https://huggingface.co/Miwa-Keita/zenz-v2.5-medium) - 📥 2k / ⭐ 10 / 一個基於 GPT‑2 的條件語言模型（zenz‑v2.5），專門用於假名-漢字轉換，發布了三種尺寸（310 M、91 M、26 M），使用字符+位元組 BPE 分詞器並在 zenz‑v2.5‑dataset 上訓練，以實現高效且具備上下文感知的轉換。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 1k / ⭐ 49 / 一個日語持續預訓練的 Mistral‑Nemo 模型（Mistral‑Nemo‑Japanese‑Instruct‑2408），基於 mistralai/Mistral‑Nemo‑Instruct‑2407 建構，可透過 transformers 使用裝置映射與 ChatML 版面提示，並由 Ryosuke Ishigami 以 Apache‑2.0 授權發布。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 1k / ⭐ 21 / OpenCALM 是 CyberAgent 發布的一系列日語僅解碼器 Transformer 語言模型（參數 160 M–6.8 B），訓練於日語維基百科和 Common Crawl，並以 CC BY‑SA 4.0 授權發行。
 * [ABEJA-Qwen2.5-32b-Japanese-v1.0](https://huggingface.co/abeja/ABEJA-Qwen2.5-32b-Japanese-v1.0) - 📥 1k / ⭐ 6 / 一個以日語為主的 Qwen 2.5‑32B 模型，從 abeja/ABEJA‑Qwen2.5-32b-Japanese‑v0.1 進行 SFT 與 DPO 微調後發布為 ABEJA‑Qwen2.5‑32b‑Japanese‑v1.0。
 * [llm-jp-3-13b-instruct](https://huggingface.co/llm-jp/llm-jp-3-13b-instruct) - 📥 1k / ⭐ 30 / 來自國立情報學研究所 LLM 研發中心的 Large language models（llm‑jp‑3‑1.8b、3‑3.7b、3‑13b 與 beta 3‑172b）已以 Hugging Face Transformers 檢查點形式發布，需使用 torch≥2.3.0、transformers≥4.40.1、accelerate≥0.29.3、flash‑attn≥2.5.8，並在日本維基百科、Common Crawl、WARP/PDF/HTML、Kaken、英文維基百科及 Dolma 資料集混合上訓練。
 * [GPT-OSS-Swallow-120B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1) - 📥 1k / ⭐ 16 / GPT‑OSS‑Swallow v0.1 提供 20 B 與 120 B 參數的日英雙語 LLM，透過 CPT、SFT 和 RLVR 訓練，以保留數學與程式碼表現，同時在推理和翻譯方面匹配或超越 GPT‑OSS。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 1k / ⭐ 21 / 提供由 NII 出品的 1.8 B 參數 llm‑jp‑3.1‑1.8b‑instruct4 日語指令調校模型，兼容 Hugging Face Transformers 及 Torch ≥ 2.3.0，包含預訓練與微調檢查點及使用示例。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 1k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一個 13‑B 的、已經進行指令預訓練的日語語言模型，由 NII 的 R&D Center 開發，並以 Hugging‑Face Transformers 的 checkpoint 形式發布，使用 UNIGRAM‑byte‑fallback tokenizer。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 1k / ⭐ 22 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter 日本語擴展版本，進一步針對日本語語言任務進行預訓練，並提供 base、instruct、fast 和 fast‑instruct 變體，由 ELYZA 團隊在 Llama 2 Community License 下維護。
 * [llm-jp-3-7.2b-instruct3](https://huggingface.co/llm-jp/llm-jp-3-7.2b-instruct3) - 📥 1k / ⭐ 4 / 承載 LLM‑jp‑3‑7.2b‑instruct3 7.2 B‑parameter 的日語語言模型，該模型來自信息學國立研究院，已在日語維基百科和 Common Crawl 上進行預訓練，採用 Hugging Face Transformers 格式，並且需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29 以及 flash‑attn ≥ 2.5。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 1k / ⭐ 108 / 一個 1.3‑B‑parameter、24‑layer transformer GPT‑1B，在 Japanese C4、CC‑100 以及 Wikipedia 上訓練，於 2022 年 1 月 26 日由 rinna Co. 發布，並以 MIT license 供使用。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 1k / ⭐ 1 / 日語增強、指令微調的 Gemma‑2 模型，建構於 Llama（2b/9b/27b pre‑train 和 instruction 版本），於 2025 年 5 月 19 日發布，並可於 HuggingFace 與 Swallow team 的網站上取得。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 12M / ⭐ 62 / 日語 wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 與 JSUT 上微調，需要 16 kHz 音訊，並可透過 HuggingSound 或 HuggingFace pipelines 使用。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 547k / ⭐ 11 / 一個經由 facebook/wav2vec2‑large‑xlsr‑53 在 Common Voice 與 JSUT corpus 微調的日語語音辨識模型，已優化為 16 kHz 音訊輸入。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 69k / ⭐ 155 / Anime Whisper 是一個輕量級的日語 ASR 模型，已在約 5,300 小時的動漫式對白上微調，提供低幻覺、節奏對齊的標點符號，並能準確轉錄非語音聲音和 NSFW 內容，必須在沒有初始提示的情況下運行。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 17k / ⭐ 127 / Kotoba‑Whisper‑v2.2 是一款日語 ASR 模型，擴展了 kotoba‑whisper‑v2.0，整合了 integrated diarization 與 automatic punctuation，透過 HuggingFace‑Transformers pipeline 實現，並與 Asahi Ushio 和 Kotoba Technologies 合作開發。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 12k / ⭐ 95 / Kotoba‑Whisper v2.0 是一款從 OpenAI Whisper large‑v3 提煉的日語ASR模型，使用 7.2 million ReazonSpeech 片段訓練，速度比原版快 6.3×，同時在領域測試中匹配教師模型的 CER/WER，並包含 stable‑ts/punctuation 支援及完整訓練程式碼於 GitHub。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 11k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供 6.3 倍更快的蒸餾 Whisper 模型，支援日本語與英語的 ASR 以及雙向語音轉文字翻譯，這些模型由 OpenAI 的 Whisper large‑v3 透過 knowledge distillation 與 cross‑entropy 及 KL‑divergence loss 建構。
 * [Qwen3-ASR-1.7B-JA](https://huggingface.co/neosophie/Qwen3-ASR-1.7B-JA) - 📥 10k / ⭐ 9 / Fine‑tuned Qwen3‑ASR‑1.7B for Japanese ASR，優化以準確轉錄專有名詞、組織及產品名稱、漢字濃厚以及日英混合技術術語。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 4k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一個擁有 **96.7 M** 參數的 **wav2vec 2.0** Base 模型，已在 **ReazonSpeech v2.0 Japanese ASR corpus** 上微調，達到 **13.22 % CER**，可透過 **Hugging Face transformers** 部署，並以 **Apache 2.0 license** 發布。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 4k / ⭐ 59 / NVIDIA NeMo 的 0.6 B‑參數 Hybrid FastConformer‑TDT‑CTC ASR 模型能帶標點符號轉錄日語語音，並且可在 NeMo 框架內進行推論或微調。
 * [qwen3-asr-1.7b-ja-anime-GGUF](https://huggingface.co/cstr/qwen3-asr-1.7b-ja-anime-GGUF) - 📥 3k / ⭐ 3 / GGUF‑量化的 Qwen3‑ASR‑1.7B，針對日語動漫/美少女遊戲語音進行微調，支援 30+ 程式語言以及 CrispASR，提供兩種尺寸（約 1.3 GB Q4_K 與 約 2.5 GB Q8_0），採用 Apache 2.0 授權。
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 3k / ⭐ 25 / Kotoba Whisper v2.0 已轉換為 CTranslate2 格式，可與 CTranslate2 與 faster‑whisper 一同使用，並提供安裝、推理範例、Apple M2 基準測試以及轉換說明。
 * [japanese-hubert-base-phoneme-ctc-v3](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v3) - 📥 3k / ⭐ 5 / Fine‑tuned Japanese HuBERT‑base for CTC phoneme recognition (v3)，加入 MeCab N‑best 與 pyopenjtalk‑plus 後處理，使用結合 CTC 和 MeCab 成本的加權損失、更新排除規則，以及新增「ty」音素。
 * [mms-300m-ForcedAligner-karaoke-ja-Latn](https://huggingface.co/NextFire/mms-300m-ForcedAligner-karaoke-ja-Latn) - 📥 2k / ⭐ 2 / 一個針對日語羅馬字卡拉OK 歌詞的微調對齊模型（MMS-300M），附帶筆記本和 TrackIO 工具。
 * [japanese-hubert-base-phoneme-ctc-v4](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v4) - 📥 2k / ⭐ 5 / 已微調日本 Hubert‑Base 的 CTC 音素辨識 (v4)，包含更新的句子過濾規則、發音調整，以及將 GPU 切換至 A6000，訓練停止於 110k 步。
 * [parakeet-tdt-0.6b-ja-GGUF](https://huggingface.co/cstr/parakeet-tdt-0.6b-ja-GGUF) - 📥 2k / ⭐ 1 / 一個已轉換為 GGUF 的 0.6 B 日語 Parakeet TDT‑CTC 模型，可與 CrispASR 的 CLI 一起使用進行 TDT 解碼（CTC 回退），在 JSUT 上達到 6.4 % CER，並提供單詞級時間戳。它有完整的 1.24 GB 精確位元構建版本，以及約 470 MB 的 Q4_K 定量化變體（該變體在大約 8 個 token 後會退化，因此推薦使用 F16）。
 * [japanese-wav2vec2-large-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-large-rs35kh) - 📥 2k / ⭐ 4 / 使用了 ReazonSpeech v2.0 微調的日本語 wav2vec 2.0 Large (319 M 參數) 在日本語 ASR 上提供了平均 16.25 % CER，勝過其他 wav2vec 2.0 系列。
 * [japanese-hubert-base-phoneme-ctc](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc) - 📥 2k / ⭐ 5 / 基於 rinna/japanese‑hubert‑base 的微調日語音素 CTC 模型，使用 ReazonSpeech v2 數據與 pyopenjtalk‑plus 標籤訓練，在新版 v2 釋出（prj-beatrice/japanese-hubert-base-phoneme-ctc-v2）中達到更佳準確度。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 2k / ⭐ 18 / Kotoba‑Whisper‑v2.1 是一款日語 ASR 模型，繼承了 kotoba‑whisper‑v2.0，並整合了標點符號後處理流程，能保持相當的 CER 性能，同時實現無縫、能感知標點符號的轉錄。
 * [Qwen3-ASR-1.7B-JA-Anime-Galgame-hf](https://huggingface.co/jaykwok/Qwen3-ASR-1.7B-JA-Anime-Galgame-hf) - 📥 1k / ⭐ 3 / 一個符合 Hugging Face 的 Qwen3‑ASR‑1.7B‑JA‑Anime‑Galgame checkpoint 轉換，保留微調權重，同時調整其佈局以便原生 Transformers 載入並支援日語動畫/美少女遊戲語音生成。
 * [kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) - 📥 1k / ⭐ 34 / Kotoba‑Whisper v1.1 是一款日文 ASR 模型，擴充了 kotoba‑whisper‑v1.0，加入無縫的標點符號添加後處理流程，提升轉錄準確率並減少延遲，與多個 Whisper 基線相較更為優秀。
 * [wavlm-base-plus-hiragana-ctc-v2](https://huggingface.co/TylorShine/wavlm-base-plus-hiragana-ctc-v2) - 📥 1k / ⭐ 3 / 一款輕量級的日語 ASR 模型，基於 WavLM‑Base‑Plus，具備雙重 CTC 頭（平假名與音素）以及 MLP 頭，不含自回歸解碼器，並可透過 `trust_remote_code=True` 以 Hugging Face 原生方式載入。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 1k / ⭐ 38 / reazonspeech-nemo-v2 是一款擁有 619‑M參數的日語長文語音識別模型，基於改進版 Fast‑Conformer 與 Linearly Scalable Attention 架構構建，訓練於 ReazonSpeech v2.0 資料集，透過 subword RNN‑T decoder（3000‑token SentencePiece）提供多小時推理，並以 Apache 2.0 授權方式分發。

### fill-mask
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 497k / ⭐ 9 / Japanese DeBERTa V2 大型模型已在 171 GB 的日語維基百科、CC‑100、與 OSCAR 上訓練，採用字符級 sentencepiece tokenization 與 whole‑word masking，已準備好通過 Hugging Face Transformers 進行下游微調。
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 337k / ⭐ 76 / Japanese BERT‑base 預訓練於 2019 年日本維基百科，使用 IPA 字典與整詞掩碼，12 層、768 維，32,000 詞表，512 令牌序列，1 百萬步；可於 cl‑tohoku/bert‑japanese 在 CC‑BY‑SA 條款下取得。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 150k / ⭐ 42 / 一個基於 BERT base 的模型，預訓練於約 17 M 日文 Wikipedia 句子（2.6 GB），採用 IPA dictionary 與 WordPiece 進行 tokenization，擁有 12 layers／768‑dim hidden states／12 heads，32 000‑token 詞彙表，於 Cloud TPUs 上訓練 1 M steps，並以 CC‑BY‑SA 3.0 發布。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 132k / ⭐ 51 / 一個 132 百萬參數的 Japanese ModernBERT 模型，結合 local‑global 與 RoPE attention，在 4.39 T tokens（日語/英語）上訓練，含有 102‑k‑size 的 vocab，最大 token 長度 8,192，並優化為 Flash Attention 2。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 64k / ⭐ 6 / 一個 BERT‑base 日語模型（12 層，768 維隱藏狀態，12 頭）在 30 M 句子（約 4 GB）上訓練，使用 Unidic 2.1.2 詞級分詞，隨後進行字級分詞和整詞遮蔽，使用 512 令牌序列、256 批次及 1 M 訓練步驟。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 21k / ⭐ 28 / ModernBERT‑Ja‑310M 是一款日語 BERT 變體，結合了 local‑global attention 與 RoPE，已在 4.09 T 個日語/英語文本 token 上訓練，支持 102 400 個詞彙、8 192 token 序列，並被優化以配合 Flash Attention 2。
 * [bigbird-base-japanese](https://huggingface.co/nlp-waseda/bigbird-base-japanese) - 📥 18k / ⭐ 5 / 日文 BigBird‑Base 模型預訓練於日本維基百科、CC‑100 以及 OSCAR，使用 Juman++ 與 SentencePiece 分詞，可微調以應用於下游任務，並在 JGLUE 基準上報告效能。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 12k / ⭐ 8 / 一個 BERT‑base 日語模型（12 層，768‑維隱藏，12 頭），在約 1700 萬句來自日語維基百科（2.6 GB）的資料上進行預訓練，使用 MeCab IPA 單詞級分詞，隨後進行字符級分詞，建立一個 4000 單詞詞彙表。訓練程式碼位於 cl‑tohoku/bert‑japanese，並以 CC BY‑SA 3.0 釋出。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 9k / ⭐ 40 / Japanese‑Roberta‑Base 是由 rinna Co., Ltd. 推出的預訓練遮罩語言模型，含正確載入、token 預處理、position‑id 處理的指引，以及強調需放置於首位的 `[CLS]` token 和一致 tokenization 的使用範例。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 8k / ⭐ 50 / LINE DistilBERT Japanese 是一個 66‑million‑parameter 的 DistilBERT 模型，使用內部 BERT‑base 教師在 131 GB 的日本網路文本上進行預訓練，並於 JGLUE 上評估，採用 MeCab Unidic 與 SentencePiece 進行分詞，於 Apache 2.0 授權下釋出。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 8k / ⭐ 5 / Japanese DeBERTa V2 tiny，預訓練於約 171 GB 的日語 Wikipedia、CC‑100 與 OSCAR 資料庫，需要 Juman++ 詞彙分割，已在 8 顆 NVIDIA A100 GPU 上訓練 33 小時，可進一步微調以應用於下游任務。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 8k / ⭐ 26 / Japanese BERT‑base (12 層, 768 hidden, 12 heads) 以 4 GB 的日本 Wikipedia（約 30 M 句）為預訓練資料，使用 Unidic 2.1.2 文字級別分詞、WordPiece 子分詞，與整詞掩碼。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 5k / ⭐ 1 / 一個以 171 GB 日本維基百科、CC‑100 與 OSCAR 文本預訓練的日語 DeBERTa‑V2 基礎模型，採用字元級分詞、全詞遮罩模式，已在 8 台 A100 GPU 上訓練 20 天，並準備好進行下游微調。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 5k / ⭐ 30 / 日文 DeBERTa V2 基礎模型，已在 171 GB 日文維基百科、CC‑100 與 OSCAR 資料上使用 Juman++ 斷詞與 SentencePiece Tokenization 進行預訓練，訓練時間三週，使用八台 NVIDIA A100 GPU，已準備好進行微調。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 4k / ⭐ 5 / DeBERTaV2 基礎模型在日本語語料庫（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上進行訓練，並採用 FP‑16 微調以應對 NLU 任務（JSTS、JNLI、JCommonsenseQA）。本模型以 CC BY‑SA 4.0 授權發佈，並獲得日本研究撥款資助。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 4k / ⭐ 32 / Japanese RoBERTa‑base，於日本維基百科與日本 CC‑100 上進行預訓練，使用 Juman++ 詞彙分割與 SentencePiece 標記化，於一週內於 8 台 NVIDIA A100 GPU 上使用 Adam（lr = 1e‑4，native AMP）進行訓練，並可微調，且於 JGLUE 上報告結果。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 3k / ⭐ 8 / ModernBERT‑Ja‑30M 是一款日語 BERT 變體，它將局部與全局注意力與 RoPE 混合起來，並在 4.39 TB 的日英文本上訓練，支援 8,192‑token 序列，參數規模從 30 M 至 130 M，並在使用 Flash Attention 2 時表現最佳。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 2k / ⭐ 9 / ModernBERT‑Ja‑70M 是一款輕量級的日語 BERT 變體，結合局部與全局注意力與 RoPE，使用 4.39 T 混合語言令牌（詞彙表 102 400，最大 8 192 令牌）訓練，支援 Flash Attention 2，並提供 30 M 至 310 M 參數的多種規格。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 一個 12 層、768 維的 BERT-Base 日語模型，使用 2.6 GB 的維基百科（≈17 M 句子）進行訓練，採用 IPA-dictionary 字元分詞與整詞遮罩（whole‑word masking），並以 CC‑BY‑SA 3.0 版權授權釋出。
 * [jmedroberta-base-sentencepiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece-vocab50000) - 📥 1k / ⭐ 1 / 日本語 RoBERTa‑base 模型，預訓練於約 10 M 的 JST 醫學文章摘要，使用 50k SentencePiece（Unigram）詞彙表，並以 CC‑BY‑4.0 授權發布，附帶全形文字輸入說明及透過 Hugging Face pipelines 進行微調的指示。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 430k / ⭐ 82 / Ruri v3 是一個尖端的日本語文本嵌入模型，建立於 ModernBERT‑Ja，支援最多 8,192‑token 輸入、100K‑token 詞彙表、FlashAttention‑加速推論，以及多種尺寸變體，方便快速使用 sentence‑transformer。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 340k / ⭐ 10 / Ruri v3 是一款最先進的日文文本嵌入模型，構建於 ModernBERT‑Ja，支持高達 8,192 tokens、一個 100k‑token 詞彙表、FlashAttention 加速，並提供從 37 M 到 315 M 參數的多種規模。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 282k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B 是一個 1.2 B‑參數的日文文本嵌入模型，建立於 Sarashina2.1‑1B 上，採用多階段對比學習訓練，以在 JMTEB 上達成最先進的分數，同時產生 1,792 維的密集向量，用於語意相似度、搜尋與分類，並在非商業授權下使用。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 198k / ⭐ 24 / GLuCoSE v2 是一款適合 CPU 的日語文本嵌入模型，透過蒸餾與多階段對比學習進行微調，提供優越的語義相似度與檢索性能—在 MIRACL 以及相關基準上超越同等規模模型。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 66k / ⭐ 7 / Ruri v3 是一款最先進的日本語文本嵌入模型，基於 ModernBERT‑Ja 建構，支援長達 8192‑token 序列、10 萬詞彙、FlashAttention，並以 30 M 到 310 M 參數大小提供，以供 sentence‑transformers 使用。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 44k / ⭐ 5 / Ruri v3 提供高性能的日語文本嵌入，最多可達 8192 個 token，擁有 100k token 詞彙表，支援 FlashAttention，並提供多種模型尺寸 (30 m–310 m) 以供透過 sentence‑transformers 進行高效推理與微調。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 27k / ⭐ 34 / GLuCoSE 是一個基於 LUKE 的日語句子嵌入模型，輸出 768 維均值池化向量（最多 512 個 tokens），在網路及 NLI/搜尋資料上訓練，於相似度基準上達成 0.864 Spearman 與 0.818 Pearson。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 14k / ⭐ 45 / 一組可釋出的 Ruri v3 日文文本嵌入模型（30m–310m），包含 SentenceTransformer 使用技巧、查詢/段落前綴，以及 JMTEB 基準測試結果，展示它們與其他日文及多語言嵌入模型的比較。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 12k / ⭐ 48 / PLaMo‑Embedding‑1B 是 Preferred Networks 開發的日本文本嵌入模型，能將日文文本轉換為向量，用於資訊檢索、分類與聚類，在 JMTEB 基準測試上表現優異，且以 Apache v2.0 license 免費提供。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 10k / ⭐ 13 / 日文通用文本嵌入模型 (Ruri‑v3, 30‑310 M 參數, 8192‑token 上限, 高 JMTEB 分數) 以 Sentence‑Transformers 使用範例提供，並與其他日文嵌入進行基準比較。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 7k / ⭐ 17 / JaColBERTv2 是一個僅限日文的 ColBERT 基於檢索模型，使用 MMarco（31 個負樣本對每個正樣本、250k 步驟、批次 32）進行知識蒸餾訓練，目前表現優於 multilingual‑e5‑large、BGE‑M3 以及 JaColBERT，完整評估仍待進行。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 5k / ⭐ 9 / 包含 Ruri v3 日文文字嵌入（30 M–310 M 參數、8192‑token 限制、JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前綴的 Sentence Transformers 指令，以及幾個日文模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基準結果。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 2k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一個 768 維的句子轉換器，建立於 studio‑ousia/luke‑japanese‑base‑lite 上，已在 shunk031/jsnli 培訓一個 epoch，並包含聚類、語意搜尋以及同時適用於 Sentence‑Transformers 與 HuggingFace 的範例。

### feature-extraction
 * [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) - 📥 192k / ⭐ 5 / 日本語 HuBERT Base，12 層 transformer 版本與 rinna 原始模型相同，訓練於約19,000 小時的 ReazonSpeech v1 日本語語音資料，並以 Apache 2.0 授權發佈。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 188k / ⭐ 56 / 一個日語 T5 模型，預訓練於約 100 GB 的 Wikipedia 與 OSCAR 數據，使用 SentencePiece 分詞，超越了 Google 的多語言 T5，在新聞分類基準上表現更佳，但仍需要微調，且可能產生偏見輸出。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 130k / ⭐ 51 / 一個日本語的 Sentence‑BERT v2，經過在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上微調，並採用 MultipleNegativesRankingLoss，與 v1 相比提升了約 1.5–2 % 的準確率，並以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 形式釋出。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 34k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一個授權為 Apache‑2.0 的日語 CLIP 模型，基於 ViT‑B/16，訓練於翻譯成日語的 CC12M 標題，並於 2022 年 5 月 12 日發布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 25k / ⭐ 30 / LY Corporation 的 clip‑japanese‑base 是一個訓練於約 1 B 影像‑文字配對的日文 CLIP 模型，使用 Eva02‑B Transformer 影像編碼器並配備 12 層 BERT 文字編碼器，於 STAIR 的 R@1 成績為 0.30，於 Recruit 的準確度為 0.89，以及於 ImageNet‑1K 的準確度為 0.58，並支援零樣本影像分類與檢索。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 13k / ⭐ 11 / Japanese Sentence‑BERT (v1) 模型，用於生成句子嵌入，並提供改進版 v2，並可透過 Hugging Face Transformers 與自訂的 `SentenceBertJapanese` 類別示範使用。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 6k / ⭐ 14 / Japanese Sentence‑LUKE 模型在與 Sentence‑BERT 相同的資料集上進行訓練，表現優於或相當於 Sentence‑BERT，基於 studio‑ousia/luke‑japanese‑base‑lite 建立，並透過 Hugging Face Transformers 的 MLukeTokenizer 與 LukeModel 使用。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 6k / ⭐ 18 / Japanese CLIP 模型 clip‑japanese‑base‑v2，升級至約 2 B 影像‑文字配對並 distillation，將 Eva02‑B 影像編碼器與 12 層 BERT 文本編碼器結合，以達到比其前身更高的 ImageNet‑1k 準確度 (0.708)。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 5k / ⭐ 2 / ja_ginza_electra 是一個 spaCy v3 Python 套件，提供已在 mC4 和 UD_Japanese_BCCWJ r2.8 上微調的日語 ELECTRA 模型（基於 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator），並具備自訂 bunsetu‑phrase detection，依照 MIT license 發佈。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 2k / ⭐ 27 / Sarashina‑Embedding‑v2‑1B 是一個 1,792 維的日語句子變換器，透過多階段對比學習訓練，達到先進的 JMTEB 分數，可用於語義相似度、搜尋、同義句挖掘、分類和聚類，透過 Sentence‑Transformers 並可加上可選的指令前綴。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 2k / ⭐ 3 / 一款在 JSNLI 上使用監督式 SimCSE 微調的日語 BERT‑base 模型，透過 Sentence‑Transformers 或 HuggingFace 以 CLS pooling 方式公開，訓練於 1 M 範例，batch size 512，學習率 5 × 10⁻⁵，溫度 5 × 10⁻⁵，64‑token 限制，以及 BFloat16 精度。
 * [japanese-hubert-large](https://huggingface.co/yky-h/japanese-hubert-large) - 📥 1k / ⭐ 2 / 日語 HuBERT Large 是由 rinna Co., Ltd. 所開發的 24 層、16 頭 Transformer 模型，使用約 19,000 小時的 ReazonSpeech v1 日語音訊進行訓練，並於 2024 年 3 月 7 日以 Apache 2.0 許可發布。

### text-ranking
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 317k / ⭐ 15 / Ruri‑v3 Reranker 是一款以 ModernBERT‑Ja 為基礎的強大日語文本重排序器，支援多達 8,192 令牌序列、100k 令牌詞彙表、FlashAttention 以及 SentencePiece tokenizer，並可透過 sentence‑transformers 使用。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 168k / ⭐ 6 / 快速、輕量級的日語 Reranker v2 模型（tiny、xsmall、small、base）具有基準分數和 GPU 速度，可通過 sentence_transformers CrossEncoder 和 transformers ≥ v4.48 （可選使用 flash‑attn 加速）使用，並且亦提供 ONNX/量化版本以供 CPU/ARM 使用。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 62k / ⭐ 7 / 日本 CrossEncoder 重排序模型 覆蓋 xsmall 到 large（含 BGE），已於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 進行評估，並附上可直接使用的 sentence_transformers 與 HuggingFace 整合範例。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 26k / ⭐ 5 / 以日語訓練的 CrossEncoder 重新排序模型，規模從 xsmall（384）到 large（1024），並包含 BGE‑v2‑m3‑v1 模型，附有微調、推理的範例程式碼，以及在 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上的基準分數。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 5k / ⭐ 2 / 使用 Sentence Transformers（交叉編碼器）構建的日語重排序模型，可透過 `trust_remote_code` 加載，在 JQaRA、JaCWIR 和 MIRACL 數據集上進行基準測試，並由 hotchpotch 組織提供小到大尺寸版本。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 4k / ⭐ 8 / 一套日本 Reranker v2，發布從 tiny 到 large 的 CrossEncoder 與基礎模型，每個模型皆附有基準分數與 GPU 推論時間，且需要 HuggingFace Transformers ≥ 4.48（可選 flash‑attn 以加速推論）。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / 日文 CrossEncoder Reranker 模型（xsmall、small、base、large、BGE‑v2 m3）隱藏層大小 384–1024，示例推理通過 sentence_transformers 和 Hugging Face，在 JQaRA、JaCWIR、MIRACL 和 JSQuAD 上獲得 0.71–0.97+ 的分數。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 2k / ⭐ 16 / 由 xsmall 到 large 的日文 CrossEncoder 排序模型，使用日語文本訓練，透過 sentence_transformers 提供，並於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上進行評估。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 1k / ⭐ 15 / 一套日本 CrossEncoder 重複器（reranker）套件——包括 xsmall、small、base、large 以及 japanese‑bge‑reranker‑v2‑m3‑v1——搭配示例使用、在多個基準上的評估指標與輔助文件。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 1k / ⭐ 6 / 一個小型、高速的日語 re‑ranker 函式庫（v2），提供 tiny‑through‑base 與 cross‑encoder 模型，具有詳細的延遲與準確率統計資訊，需 Transformers ≥ 4.48（可選 Flash‑Attention 2）並支援 ONNX/quantization 用於 CPU/ARM 部署。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 1k / ⭐ 3 / Japanese‑reranker‑small‑v2 是一款輕量、快速的日語重排序模型系列（v2），提供從 tiny 到 base 的各種變體，最高可達平均 0.89 分，且 GPU 推論時間為 2–15 秒，亦包含 cross‑encoder 選項，並要求 Hugging Face Transformers v4.48+；可選擇 Flash Attention 2 以加速。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 327k / ⭐ 17 / 一個以新 VNTL 數據集為基礎的 LLaMA 3 Youko qlora 微調模型，優化為準確、逐字的日語視覺小說到英文翻譯，不使用聊天模式，使用預設的 LLaMA 3 提示，並建議採用中性取樣（temperature 0，無重複懲罰）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 90k / ⭐ 16 / Sugoi LLM 14B Ultra (GGUF) 是一個日語轉英語的翻譯模型，BLEU 分數為 21.38——幾乎是其先前分數 13.67 的兩倍——在 RPG‑Maker 方括號文本上擅長，提示遵從性強，並為交互式聊天 UI 生成 JSON 輸出。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 35k / ⭐ 75 / 來自 Opus corpus 的日文-英語 Transformer‑Align MT 模型，使用 normalization 與 SentencePiece 先行處理，在 Tatoeba 測試集上達到 41.7 BLEU 與 0.589 chr‑F。
 * [aihub-ja-ko-translator](https://huggingface.co/sappho192/aihub-ja-ko-translator) - 📥 4k / ⭐ 5 / 使用 bert‑japanese 編碼器與 kogpt‑2 解碼器的日語至韓語翻譯模型，在 HuggingFace 上進行示範，建立於需要與韓國 NIA 獨立簽署匯出協議的 Aihub 數據集上。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 4k / ⭐ 33 / FuguMT 是一個由 transformers 與 SentencePiece 建構的日文對英語 Marian‑NMT 翻譯模型，在 Tatoeba 上取得 39.1 BLEU 分數。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 3k / ⭐ 54 / FuguMT 是一個基於 Marian‑NMT 的英日翻譯模型，使用 Hugging Face Transformers 和 SentencePiece 構建，於 Tatoeba 上達成 32.7 的 BLEU 分數。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 2k / ⭐ 42 / 微調、GGUF‑量化後的 LFM2‑350M checkpoint，適用於近即時雙向日英短至中篇文本翻譯，可透過 llama.cpp 使用。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 1k / ⭐ 122 / PLaMo Translation Model 是 Preferred Networks 為翻譯任務所創建的大規模語言模型，可供 base、post‑trained 以及 evaluation 版本使用，並以 PLaMo community license 釋出，未對聊天或其他下游用途進行 instruction‑tuned。
 * [sugoi-v4-ja-en-ctranslate2](https://huggingface.co/entai2965/sugoi-v4-ja-en-ctranslate2) - 📥 1k / ⭐ 3 / Sugoi v4 是 MingShiba 開發的日語至英語 NMT 模型，可從 Hugging Face 下載，並使用 CTranslate2 進行批次翻譯。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 788k / ⭐ 179 / Manga OCR 是一個 Vision Encoder‑Decoder OCR 工具，能閱讀垂直與水平的日語漫畫文字（包含振假名），適用於多種字體與低品質圖像，且源碼免費提供。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 100k / ⭐ 7 / Meikiocr的 `meiki.text.recognition.v0`——一個基於 D‑FINE 的 MobileNetV4 模型，在日語視訊遊戲文字上微調——為水平文字提供最先進的準確性和延遲，能從 960×32 的輸入中偵測多達 48 個字符，並輸出每個字符的外框與置信度分數。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 51k / ⭐ 3 / meikiocr 提供一款基於 D‑FINE 的開源權重文字偵測模型，適用於遊戲視訊（v0.1 版，採用 MobileNet‑v4 主幹，提供兩種解析度變體與 64 框限制），以及實驗性低延遲 tiny 與 small 變體，已在日本遊戲及漫畫上訓練。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 3k / ⭐ 4 / Manga OCR 是一個 Vision Encoder‑Decoder 系統，能在各種字體與低品質影像中提供高品質的日本漫畫 OCR，包括帶有假名覆蓋的垂直與水平文字，亦可用於一般印刷日語 OCR。
 * [manga-ocr-2025-onnx](https://huggingface.co/l0wgear/manga-ocr-2025-onnx) - 📥 3k / ⭐ 9 / 一款基於 kha‑white 的 manga‑ocr 與 jzhang533 2025 基線構建的 ONNX Vision‑Encoder‑Decoder Manga OCR 模型，支援垂直/水平日文文字、振假名、疊加與低品質影像，訓練資料包含 manga109‑s 與合成數據，可透過 Hugging Face Optimum 使用 TrOCRProcessor 與 ORTModelForVision2Seq 部署。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 2k / ⭐ 32 / Sarashina2.2‑OCR 是一款 3‑B 參數、端到端的 OCR 模型，經過人類偏好優化後，能將日文與英文文件解析為 Markdown，並將表格轉換為 HTML，數學轉換為 LaTeX，圖形轉換為 bounding‑box 註釋；它透過將 SigLIP2 為基礎的視覺編碼器與 Sarashina2.2‑3B‑Instruct LLM 整合，實現高解析度視覺‑語言理解。

### text-classification
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 52k / ⭐ 6 / 一個針對 WRIME 數據集微調的日本 BERT BASE 模型，為作者和讀者預測八種情感（喜悅、悲傷、期待、驚訝、憤怒、恐懼、厭惡、信任）的 0‑4 強度分數；代碼可用，訓練耗時 3 小時於 K80 上，對作者達到約 0.6 MSE，對讀者達到約 0.2 MSE。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 4k / ⭐ 16 / 在 Amazon 商品評論上微調日本 BERT（cl‑tohoku/bert‑base‑japanese‑v2）以進行情感分類，達到約 81% 的準確率與 0.73 的 F1 分數，在 6 個 epoch 之後，學習率為 2 × 10⁻⁵。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 3k / ⭐ 2 / 在《Large Language Model Introduction》第5章中介紹的日本 BERT‑based 模型，已於 JGLUE JSTS 資料集上進行微調，用於語義相似度評分。此模型包含 Colab notebooks、transformers‑pipeline 使用說明，以及 Apache 2.0 授權。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 2k / ⭐ 15 / 在 chABSA 數據集上訓練的日文情感分析模型，達到 loss 0.0001、accuracy 1.0、以及 F1 1.0。使用 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 構建，使用 Adam 進行優化（learning rate 2e‑05，10 epochs，batch size 16），並通過 `model(**inputs)` 評估。

### token-classification
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 11k / ⭐ 11 / Fine‑tuned Japanese BERT‑Base 用於在維基百科資料集上的命名實體識別，已在《Large Language Model Introduction》一書第六章展示，可透過 Hugging Face transformers pipeline 部署（Apache 2.0 授權）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 7k / ⭐ 27 / 使用 5 週期 Adam (lr 5e‑5, batch 12) 微調 XLM‑RoBERTa‑base，針對日語 NER 資料集（tags PER, ORG, LOC, INS, PRD, EVT）以達成 0.0173 的驗證損失，已於 Transformers 4.23.1 與 PyTorch 1.12.1 發佈。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 3k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日語 NER，可提取八種實體類型（公司、政治/其他組織、設施、產品、事件），透過 `BertForTokenClassification`，在 Stockmark Wikipedia 數據集上訓練，並可透過 `transformers`、`unidic_lite`、`fugashi` 安裝，採用 CC BY‑SA 3.0 許可證。

### text-to-speech
 * [sarashina2.2-tts](https://huggingface.co/sbintuitions/sarashina2.2-tts) - 📥 7k / ⭐ 71 / sarashina2.2-tts 是一個基於 SB Intuitions LLM 的日語中心化 TTS 系統，提供高精度的日語和英語合成、自然表達聲音、零樣本克隆、跨語言一致性以及無縫代碼切換。
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 4k / ⭐ 11 / 一個名為 **tsukuyomi‑wavlm** 的日語 TTS 模型—在 tsukuyomi 語料庫 100 條語句上 fine‑tuned 300 epochs，使用 WavLM discriminator 和 A1/A2/A3 prosody features 於 VITS architecture，匯出為 61 MB 的 ONNX file，能生成 22.05 kHz syntheses。

### any-to-any
 * [gemma-4-12B-it-qat-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-12B-it-qat-UD-japanese-imatrix) - 📥 5k / ⭐ 14 / 一個 1/4 大小、CPU 友善的日語優化量化 Gemma 4 模型（Apache 2.0），完全在本機運行，提供可選開發者支援和穩健基準。

### audio-to-audio
 * [LFM2.5-Audio-1.5B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF) - 📥 2k / ⭐ 31 / 量化 GGUF 版本的 LiquidAI LFM 2.5‑Audio 1.5B JP 模型，包括語言、音訊編碼器和聲碼器權重（F32/F16/Q8_0/Q4_0），以及使用 llama.cpp 的 ASR 與 TTS CLI/Server 運行器。

### image-text-to-text
 * [Stockmark-Nemotron-3-Nano-Omni-JapanDocReader](https://huggingface.co/stockmark/Stockmark-Nemotron-3-Nano-Omni-JapanDocReader) - 📥 2k / ⭐ 8 / Stockmark‑Nemotron‑3‑Nano‑Omni‑JapanDocReader 是一個基於 NVIDIA 的 Nemotron‑3‑Nano‑Omni 的日語多模態文件閱讀模型，使用混合 VQA 與結構化解析數據進行微調，並透過 DAPO 強化，以保留 VQA 推理能力，同時提升文件解析品質。

### others
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 139k / ⭐ 64 / Japanese BERT‑base (12 層, 768‑維度隱藏, 12 頭, 32k 詞彙) 以完整詞遮蔽在 CC‑100 與 2023‑Jan Wikipedia 上預訓練，使用 Unidic 2.1.2 詞級分詞加 WordPiece，訓練 200 萬步。
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 128k / ⭐ 11 / Japanese‑language BERT‑Base（12層，768‑次元，12頭）以 Unidic 為基礎的單詞層級加字符層級標記化以及整詞遮蔽，在 CC‑100 和 2023 Wikipedia 上進行預訓練，產生了 7,027‑token 詞彙。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 78k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上訓練，使用 Unidic‑lite 詞級分詞，結合 WordPiece 子詞與全詞遮蔽，模型為 24 層、1024 維隱藏、16 頭、32k 詞表；預訓練程式碼位於 cl‑tohoku/bert‑japanese。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 39k / ⭐ 13 / 一個 gguf 格式的 moonshotai 的 Moonlight‑16B‑A3B‑Instruct，已經在 TFMC 的 imatrix 日語資料集上訓練，準備好可與 llama.cpp (CUDA‑enabled) 一同使用，並可透過執行 recipe‑request 提示來展示。
 * [kana-whisper](https://huggingface.co/sbintuitions/kana-whisper) - 📥 18k / ⭐ 12 / 一個經過微調的 Whisper large-v3-turbo 模型，能將日語語音轉錄成片假名，作為 Sarashina2.2-TTS 專案內 Joyo Kanji Yomi Benchmark 的 ASR 組件，同時驅動 Kana CER Usage With Transformers 管道。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 17k / ⭐ 11 / 一個以約 100 GB 的 Wikipedia 與 OSCAR CC‑100 數據（混合 10:1、Byte‑fallback 的 SentencePiece）預訓練的日本 T5‑v1.1 模型，需對下游任務進行微調，包含遷移學習範例程式碼，提示輸出可能存在偏差，且採用 CC‑BY‑SA 4.0 授權。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 6k / ⭐ 17 / 高效能日文 SPLADE v2 透過 WebUI demo 可進行稀疏向量轉換與推理，使用 YAST 訓練，提供 YASEM 嵌入，並報告 JMTEB 基準結果。
 * [umiyuki-Umievo-itr012-Gleipnir-7B-gguf](https://huggingface.co/mmnga/umiyuki-Umievo-itr012-Gleipnir-7B-gguf) - 📥 4k / ⭐ 9 / 一個以 gguf 格式的 Umievo‑itr012‑Gleipnir‑7B 版本（在 TFMC/imatrix‑dataset‑for‑japanese‑llm 上訓練），已準備好在 llama.cpp 執行。
 * [tokyotech-llm-Swallow-13b-instruct-v0.1-gguf](https://huggingface.co/mmnga/tokyotech-llm-Swallow-13b-instruct-v0.1-gguf) - 📥 4k / ⭐ 1 / 一個由 TokyoTech‑LLM 提供的 GGUF 格式 13B 語言指令模型，已在 TFMC 的日語資料集上進行微調，可使用 llama.cpp 處理日文提示。
 * [YuisekinAIEvol-Mistral-7B-ja-math-v0.1.1-gguf](https://huggingface.co/mmnga/YuisekinAIEvol-Mistral-7B-ja-math-v0.1.1-gguf) - 📥 4k / ⭐ 2 / GGUF 格式的 YuisekinAIEvol‑Mistral‑7B‑ja‑math‑v0.1.1（基於 TFMC/imatrix‑dataset），已準備好供 llama.cpp 使用。
 * [umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf](https://huggingface.co/mmnga/umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf) - 📥 4k / ⭐ 3 / 一個已轉換為 GGUF 的日本語聊天模型「Japanese-Chat-Umievo-itr001-7b」，由 TFMC/imatrix 數據集構建，可透過 llama.cpp 使用單檔命令列執行。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 3k / ⭐ 19 / 日文 DeBERTa V3 基礎版本，預訓練於 LLM‑jp v1.0 的 540 B 個 token，使用已調整的 DeBERTa V3 設定，採用 unigram byte‑fallback tokenizer（無形態學分析器），並進行 fine‑tuned 於 JGLUE NLU 任務。
 * [DataPilot-ArrowPro-7B-KUJIRA-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-KUJIRA-gguf) - 📥 3k / ⭐ 10 / ArrowPro‑7B‑KUJIRA 以 GGUF 格式發布，由 DataPilot 製作，來源於 TFMC/imatrix-dataset-for-japanese-LLM，可使用 llama.cpp 在日本語 LLM 推理中使用。
 * [Fugaku-LLM-13B-instruct-gguf](https://huggingface.co/mmnga/Fugaku-LLM-13B-instruct-gguf) - 📥 3k / ⭐ 6 / Fugaku‑LLM‑13B‑instruct‑gguf 是 Fugaku‑LLM‑13B‑instruct 的 gguf 格式轉換，使用來自 TFMC/imatrix-dataset-for-japanese-llm 的 imatrix 數據構建，用戶需同意其使用條款。
 * [karakuri-lm-8x7b-instruct-v0.1-gguf](https://huggingface.co/mmnga/karakuri-lm-8x7b-instruct-v0.1-gguf) - 📥 3k / ⭐ 2 / 由 karakuri‑ai 發佈的 GGUF 格式版本 karakuri‑lm‑8x7b‑instruct‑v0.1，訓練於 TFMC/imatrix‑dataset‑for‑japanese‑llm，可透過提供的命令列與 llama.cpp 一同使用。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 3k / ⭐ 3 / A T5 v1.1 日語模型，預訓練於 mC4/ja 與 Wikipedia，採用 GEGLU 激活函式，在預訓練期間無 dropout，具有獨立的 embedding / classifier 層，以及較大的 d_model 但頭數更少，授權為 CC‑BY‑SA 4.0，可商業使用。
 * [ArrowPro-7B-KillerWhale-gguf](https://huggingface.co/mmnga/ArrowPro-7B-KillerWhale-gguf) - 📥 3k / ⭐ 1 / 一個已轉換為 gguf 的 ArrowPro‑7B‑KillerWhale 模型（使用 TFMC/imatrix‑dataset-for-japanese‑LLM 訓練），準備好供 llama.cpp 使用。
 * [lightblue-suzume-llama-3-8B-japanese-gguf](https://huggingface.co/mmnga/lightblue-suzume-llama-3-8B-japanese-gguf) - 📥 3k / ⭐ 2 / 日語優化版的 GGUF 版本，為 Lightblue 的 suzume‑Llama‑3‑8B，使用 TFMC/imatrix 資料構建，可與 llama.cpp 進行推論。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 3k / ⭐ 2 / 一個已轉換為 GGUF 的 DataPilot ArrowPro‑7B‑RobinHood 模型版本，基於 TFMC/imatrix 數據集構建，可與 llama.cpp 一起使用於日語 LLM 任務。
 * [gemma-4-E2B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E2B-it-UD-japanese-imatrix) - 📥 3k / ⭐ 2 / 一個已轉換為 GGUF 的 Gemma‑4‑E2B‑it 模型，經過針對日語能力的微調，使用 Unsloth® Dynamic Quantization 2.0 構建，加入社群錯誤修復與日語校正資料，可在 CPU（≥8 GB RAM、≥4 GB 硬碟）上執行 via llama.cpp。
 * [tokyotech-llm-Swallow-70b-instruct-v0.1-gguf](https://huggingface.co/mmnga/tokyotech-llm-Swallow-70b-instruct-v0.1-gguf) - 📥 3k / ⭐ 1 / 一個從 TokyoTech LLM 轉換成 GGUF 的 70 B Swallow‑instruct 模型，使用 imatrix Japanese dataset 訓練，可與 llama.cpp 進行推論。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一個擁有 80 億參數的 LLM，透過持續預訓練以及在合成日語數據上進行指令調整微調，提升了 Meta 的 Llama 3.1 在日語語言以及程式碼／數學推理方面的表現，同時保持英語流暢度。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 75 / Llama‑3‑ELYZA‑JP‑8B 是一款日本優化的 8‑B Llama 3 模型，採用 GGUF (Q4_K_M) 與 AWQ 量化，能以 llama.cpp、LM Studio 或 OpenAI‑相容 API 執行。
 * [pfnet-nekomata-14b-pfn-qfin-gguf](https://huggingface.co/mmnga/pfnet-nekomata-14b-pfn-qfin-gguf) - 📥 2k / ⭐ 1 / 一個已轉換為 GGUF 的 pfnet nekomata‑14b‑pfn‑qfin 模型版本，使用 TFMC/imatrix 資料構建並依照 Tongyi Qianwen 許可證授權，準備與 llama.cpp 一起使用。
 * [Llama-3-Swallow-70B-Instruct-v0.1-gguf](https://huggingface.co/mmnga/Llama-3-Swallow-70B-Instruct-v0.1-gguf) - 📥 2k / ⭐ 8 / 一份由 tokyotech‑llm 發佈的 Llama‑3‑Swallow‑70B‑Instruct‑v0.1 的 gguf 格式轉換，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 訓練，可透過 llama.cpp 使用（例如 `./main -m 'Llama-3-Swallow-70B-Instruct-v0.1-Q4_0.gguf'`）。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 2k / ⭐ 1 / 一個高度優化的 GGUF 版本，基於 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 與廣泛修復，調校以擅長日語，並可在 llama.cpp 上運行，至少需要 16 GB RAM 與 6 GB 硬碟空間（GPU 為選用）。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 2k / ⭐ 22 / 一個 GGUF‑格式的 pfnet 的 plamo‑2‑translate 發行版，基於 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 數據構建，並附有使用 llama.cpp 在支援 CUDA 的硬體上編譯與執行的說明。
 * [Llama-3-Swallow-8B-Instruct-v0.1-gguf](https://huggingface.co/mmnga/Llama-3-Swallow-8B-Instruct-v0.1-gguf) - 📥 2k / ⭐ 3 / 一個 gguf‑format 轉換版本的 tokyotech‑llm 的 Llama‑3‑Swallow‑8B‑Instruct‑v0.1，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 資料構建，可透過 llama.cpp 執行（例如：`./main -m 'Llama-3-Swallow-8B-Instruct-v0.1-Q4_0.gguf'`）。
 * [rinna-llama-3-youko-70b-instruct-gguf](https://huggingface.co/mmnga/rinna-llama-3-youko-70b-instruct-gguf) - 📥 2k / ⭐ 1 / 一個 GGUF 格式的轉換版本，針對 rinna 的 Llama 3 Youko 70B Instruct 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 資料構建，可透過 llama.cpp 使用（例如 `./llama-cli -m rinna-…-Q4_0.gguf`）。
 * [llama-3-youko-8b-instruct-i1-GGUF](https://huggingface.co/mradermacher/llama-3-youko-8b-instruct-i1-GGUF) - 📥 2k / ⭐ 1 / GGUF 量化版本的 rinna/llama‑3‑youko‑8b‑instruct 集合，列出其大小/品質折衷，並提供使用指引、比較圖表及 FAQ／模型請求連結。
 * [Llama-3.1-8B-EZO-1.1-it-gguf](https://huggingface.co/mmnga/Llama-3.1-8B-EZO-1.1-it-gguf) - 📥 2k / ⭐ 7 / HODACHI 的 GGUF 轉換版 Llama 3.1 8B “EZO‑1.1‑it” 模型（在 TFMC/imatrix‑dataset-for-japanese‑LLM 上訓練）已準備好可使用 llama.cpp 命令列介面。
 * [aixsatoshi-Honyaku-13b-gguf](https://huggingface.co/mmnga/aixsatoshi-Honyaku-13b-gguf) - 📥 2k / ⭐ 1 / 一個由 aixsatoshi 的 Honyaku‑13B 模型轉換成 GGUF 版本，使用 TFMC/imatrix-dataset-for-japanese-llm 中的 imatrix 數據構建，可通過 llama.cpp 使用（例如 `./main -m 'aixsatoshi-Honyaku-13b-Q4_0.gguf'`）。
 * [SakanaAI-EvoLLM-JP-v1-7B-gguf](https://huggingface.co/mmnga/SakanaAI-EvoLLM-JP-v1-7B-gguf) - 📥 2k / ⭐ 4 / EvoLLM‑JP‑v1‑7B 在 gguf 格式，為 Shisa Gamma 7B、WizardMath 7B V1.1 與 Abel 7B 002 合併的基礎模型，可使用 llama.cpp 進行日語相關任務。
 * [Llama-3.1-70B-Japanese-Instruct-2407-gguf](https://huggingface.co/mmnga/Llama-3.1-70B-Japanese-Instruct-2407-gguf) - 📥 2k / ⭐ 8 / 一個 gguf‑格式的 cyberagent’s Llama‑3.1‑70B‑Japanese‑Instruct‑2407，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 資料構建，並以 llama.cpp 的 CLI 執行。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct-gguf](https://huggingface.co/mmnga/ELYZA-japanese-Llama-2-7b-fast-instruct-gguf) - 📥 2k / ⭐ 45 / 已將 ELYZA 的 7 b 日文 Llama‑2 instruct 模型轉成 GGUF，加入日文詞彙以提升 1.8× 速度，並可在 llama.cpp 上執行，符合 Llama 2 license。
 * [japanese-stablelm-2-instruct-1_6b-gguf](https://huggingface.co/mmnga/japanese-stablelm-2-instruct-1_6b-gguf) - 📥 2k / ⭐ 3 / GGUF 格式版本的 stabilityai 的 japanese-stablelm-2-instruct-1_6b，使用 TFMC 的 imatrix-dataset 建置，需要授權協議（商業用途需會員），並包含使用 llama.cpp 的轉換腳本。
 * [karakuri-lm-8x7b-chat-v0.1-gguf](https://huggingface.co/mmnga/karakuri-lm-8x7b-chat-v0.1-gguf) - 📥 1k / ⭐ 4 / 一個已轉換為 GGUF 的 karakuri‑lm‑8x7b‑chat‑v0.1 版本，基於 TFMC/imatrix 資料集建置，用於日語 LLM 並可與 llama.cpp 一同使用（例如：`./main -m karakuri-lm-8x7b-chat-v0.1-Q4_0.gguf`）。
 * [llm-jp-4-33b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-33b-thinking-gguf) - 📥 1k / ⭐ 4 / 一個 GGUF 格式的 llm-jp「llm‑jp‑4‑33b‑thinking」模型版本，從 TFMC/imatrix 數據集構建並使用支持 CUDA、flash‑attn 及可調 GPU 記憶體設定的自訂 llama.cpp 構建執行。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 1k / ⭐ 6 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一款頂級、以日文為焦點的 GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，具備廣泛的日文校準和社區修正的缺陷，即使沒有 GPU 也能在 llama.cpp 上運行，最低需要 8 GB RAM 及 3 GB 磁碟空間。
 * [Ninja-v1-NSFW-128k-gguf](https://huggingface.co/mmnga/Ninja-v1-NSFW-128k-gguf) - 📥 1k / ⭐ 11 / 一個倉庫提供 Ninja‑v1‑NSFW‑128k 模型的 GGUF 格式轉換，該模型由 TFMC/imatrix‑dataset‑for‑japanese‑LLM 構建，並附帶在 llama.cpp 中運行以生成日文小說文本的使用說明。
 * [Qwen3-8B-JP-Uncensored-GGUF](https://huggingface.co/ryo559/Qwen3-8B-JP-Uncensored-GGUF) - 📥 1k / ⭐ 1 / 一個 GGUF‑量化的 Qwen3‑8B 日語無審查模型（約 5 GB 用 Q4_K_M、約 8.5 GB 用 Q8_0），可在本地透過 Ollama 或 llama.cpp 運行，並釋出供研究使用，但用戶須對生成內容負責。
 * [nekomata-7b-instruction-i1-GGUF](https://huggingface.co/mradermacher/nekomata-7b-instruction-i1-GGUF) - 📥 1k / ⭐ 1 / 加權/矩陣量化的 7B “nekomata‑instruction” 模型可作為 GGUF 檔案提供（不同 IQ 和 Q 等級，大小 2.1–6.4 GB），並附有使用說明連結至 TheBloke README、比較圖表，以及 HuggingFace 模型請求頁面以供進一步支援。
 * [HODACHI-EZO-Common-T2-2B-gemma-2-it-gguf](https://huggingface.co/mmnga/HODACHI-EZO-Common-T2-2B-gemma-2-it-gguf) - 📥 1k / ⭐ 5 / 一個 gguf‑格式轉換的 HODACHI 的 EZO‑Common‑T2‑2B‑gemma‑2‑it 模型，基於 TFMC/imatrix‑dataset-for-japanese‑llm 構建，已準備好與 llama.cpp 一起使用（例如 `-m HODACHI-EZO-Common-T2-2B-gemma-2-it-Q4_0.gguf`）。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5-gguf](https://huggingface.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf) - 📥 1k / ⭐ 2 / GGUF 轉換 Llama‑3.1‑Swallow‑8B‑Instruct‑v0.5 由 tokyotech‑llm，結合 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附帶 Build/Run 指令 for llama.cpp.
 * [HODACHI-Borea-Phi-3.5-mini-Instruct-Jp-gguf](https://huggingface.co/mmnga/HODACHI-Borea-Phi-3.5-mini-Instruct-Jp-gguf) - 📥 1k / ⭐ 4 / 一個以 gguf 格式呈現的 HODACHI 的 Borea‑Phi‑3.5‑mini‑Instruct‑Jp 模型，使用 TFMC/imatrix-dataset-for-japanese-llm 的 imatrix 數據構建，可通過 llama.cpp 的命令列介面使用。
 * [rinna-llama-3-youko-8b-gguf](https://huggingface.co/mmnga/rinna-llama-3-youko-8b-gguf) - 📥 1k / ⭐ 6 / 一個 GGUF 格式的 rinna’s llama‑3‑youko‑8b 模型轉換，使用來自 TFMC/imatrix‑dataset-for-japanese‑llm 的 imatrix 資料構建，可通過 llama.cpp 使用。
 * [ELYZA-japanese-Llama-2-13b-fast-instruct-gguf](https://huggingface.co/mmnga/ELYZA-japanese-Llama-2-13b-fast-instruct-gguf) - 📥 1k / ⭐ 24 / Repo 主機包含了 ELYZA 的 GGUF 版 13‑B 日語 Llama‑2 fast‑instruct 模型，已準備好供 llama.cpp 使用，並提供其他 ELYZA Llama‑2 與 CodeLlama 變體的連結。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 1k / ⭐ 7 / 一個為日語微調的 Qwen 3.5‑9B GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，進行了廣泛的錯誤修復、大規模日語校準，並可在 CPU 上運行，需 16 GB RAM 及 6 GB 磁碟空間，透過 llama.cpp。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 16 / Sarashina2.2 提供 0.5‑B、1‑B、和 3‑B 的語言模型，這些模型由 SB Intuitions 透過三階段流程及合成資料進行訓練，達成優異的日文 QA、數學及編碼分數，同時提供未經指令微調的預訓練權重，可能產生有偏差的輸出。
 * [Qwen2.5-7B-Instruct-gguf-japanese-imatrix-128K](https://huggingface.co/dahara1/Qwen2.5-7B-Instruct-gguf-japanese-imatrix-128K) - 📥 1k / ⭐ 2 / Qwen 2.5 3B 模型的 Japanese‑instruct 版本，以 GGUF 格式發布，使用 128 KB 矩陣，由 dahara1 發布。
 * [Llama-3-ELYZA-JP-8B-gguf](https://huggingface.co/mmnga/Llama-3-ELYZA-JP-8B-gguf) - 📥 1k / ⭐ 4 / 由 elyza 提供的 GGUF‑converted Llama‑3‑ELYZA‑JP‑8B，使用 TFMC/imatrix‑dataset‑for‑japanese‑LLM 構建，已準備好供 llama.cpp 使用。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 4M / ⭐ 80 / 聚合自 2009‑2024 年的 NicoNico Live 評論日誌超過 150 GB，包括轉換前、轉換後及實時 NX‑Jikkyo 捕獲，並提供 API 以方便檢索歷史 TV‑broadcast 討論。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 5k / ⭐ 34 / FineWeb2 Edu Japanese 交付約 120 million 高品質教育用日語文本（≈89.3 billion tokens）來自 FineWeb2，經 DeepSeek‑API classifier（score ≥ 2.5）過濾，使用 ModernBERT‑Ja‑130M 分詞，並包含小型 token 子集（≤512 tokens）。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 4k / ⭐ 7 / Japanese Medical VQA 12M 是一個大型多模態資料集（約 12 M 個樣本），包含日語醫學影像及其原始和擴充的說明文字，說明文字同時以源語言與日語呈現，並附帶生成的 VQA 問答對。此資料集以 Parquet/Webdataset 格式發布，來源為 Open‑PMC‑18M，使用 InternVL3.5 進行擴充、Qwen3‑30B‑A3B 進行翻譯，以及 GPT‑OSS 120B 生成 VQA。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 4k / ⭐ 92 / AnswerCarefully Dataset 提供日語及多語言資料，用於商業或非商業 LLM 安全增強；禁止任何其他用途——包括安全繞過；允許帶歸屬的衍生作品；並附帶創作者對損害或服務變更之非責任免責聲明。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 4k / ⭐ 127 / Nemotron‑Personas‑Japan是一個開源、CC BY 4.0資料集，提供高品質的合成生成日本人格資料——包含姓名、性別、年齡、背景、婚姻狀況、教育、職業和地理位置——基於真實世界的人口、地理和個性分佈設計，使用概率圖形模型和GPT‑OSS‑120B進行優化，以提升多樣性、減少偏見、避免模型崩潰，協助主權AI發展並支持商業使用。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 4k / ⭐ 36 / 重構後重新上傳 Galgame VisualNovel 資料集 (OOPPEENN/5669736E6F76656C5F44617461736574)，為了提高 Hugging Face 資料集載入效率，保留所有原始音訊 / 文字，並提供一段提取腳本，支援多種遊戲子集選項。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 3k / ⭐ 9 / Cauldron‑JA 是一套日本視覺‑語言資料集，包含 44 個子資料集，這些子資料集是使用 DeepL API 將 The Cauldron 翻譯而成，通過 HuggingFace’s datasets library 可取得，授權條件與原始資料集完全相同，提示（prompts）則以 CC‑BY‑4.0 授權釋出。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 3k / ⭐ 19 / JMTEB 是一套日語文本嵌入基準，包含 5 個任務（聚類、分類、STS、檢索、重排序）與 28 個資料集，提供一行式評估腳本並邀請社群貢獻。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 2k / ⭐ 48 / 使用者友善、去重的 CSV 資料集，包含來自 Aozora Bunko 的公有領域日語文本，已使用 globis‑org/aozorabunko‑extractor 處理並為現代日語機器學習用途做過清理。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 101 / 一個包含 100 筆樣本的日本語 instruction‑tuning 評估資料集，內含標註任務——從摘要校正、數學推理到翻譯、創意生成及使用者意圖理解——設計用於手動或自動 5‑point rating 的 fine‑tuned models 評估。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 2k / ⭐ 7 / JMedBench 是一個日本醫學領域 LLM 基準，包含 20 個資料集，涵蓋五個任務（MCQA、NER、STS 等），資料來源於 MedMCQA、PubMedQA、MMLU 及其他，每個資料集都有自己的授權，並附有註記指出翻譯可能存在偏差，需人工審核。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 2k / ⭐ 47 / 更新了 JGLUE 數據集卡和載入腳本，適用於由 Yahoo Japan 和 Waseda University 創建的日本 NLP 基準，涵蓋文本分類（MARC‑ja、JCoLA）、句子對分類（JNLI）和 QA（JSQuAD、JCommonsenseQA），發布版本已在 GitHub 和 Hugging Face 上連結。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 2k / ⭐ 12 / 一份托管於 Hugging Face 的 Reazon Speech v2 Japanese dataset 的鏡像，採用 CDLA‑Sharing‑1.0 發行，使用僅限於《Japanese Copyright Act Article 30‑4》，包含 4,096 個 16 kHz FLAC 音訊檔案以及對應的 TSV/CSV format 文字稿。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 1k / ⭐ 5 / 來自 Fate/Stay Night 角色「Emilia」的對話與傳說資料集，格式化用於訓練與評估對話語言模型。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 6 / JamC‑QA 是一個涵蓋八個日本文化與知識類別的雙語多選題基準測試，並以排行榜指標對比最先進模型。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 1k / ⭐ 5 / Japanese JaQuAD（QG‑Bench 的子集）提供句子級和段落級資料，並以高亮顯示答案 token，用於訓練日語提問生成模型，評估指標包括 BLEU4、METEOR、ROUGE‑L、BERTScore 與 MoverScore。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 1k / ⭐ 147 / Japanese Anime Speech Dataset V2 提供 292,637 對乾淨的音頻-文本對，約 397.5 小時為 SFW，52.4 小時為 NSFW，存於 128‑kbps MP3 檔案中按安全性分割，專為訓練自動語音識別模型而設。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 1k / ⭐ 49 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小時的匿名化 1,033,142 對 eroge 音訊–轉錄配對 (大多為女性，NSFW)，MIT授權，用於學術研究。
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 1k / ⭐ 3 / 從 Hugging Face（if001/oscar_2023_filtered）載入 Oscar 2023 資料集的 312,396 行篩選子集，並在 GitHub 上的 if001/HojiChar_OSCAR_sample 儲存庫提供範例程式碼。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 1k / ⭐ 20 / JMMMU 是一個日語多模態基準，已擴充十倍至 1,320 個文化多樣化問題 (720 個文化中立，600 個文化特定)，由母語專家翻譯，現在擁有公開排行榜。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 1k / ⭐ 2 / 18,612個將Python指令–回應對日文翻譯—使用 GPT‑4o‑mini 生成，保留原始英文提示、程式碼與範例—為訓練、微調、聊天機器人、研究與教育提供多樣的編程任務，全部以 MIT 許可證發布。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 1k / ⭐ 122 / ReazonSpeech 是一個免費的 FLAC‑encoded 日語語音語料庫，附帶文字稿，提供五種規模，從 8.5 小時到 35,000 小時，可透過 Hugging Face 下載，採用 CDLA‑Sharing‑1.0 授權，並受限於日本版權法第 30‑4 條使用。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 982 / ⭐ 5 / 一個受限、非商業性的衍生資料集，基於 EDINET XBRL 財務資料，禁止再散佈、AI 訓練及商業使用，存取需手動批准。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 970 / ⭐ 6 / 日文 MC4 資料集卡片 (mc4-ja)
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 884 / ⭐ 15 / EDINET‑Bench 是一個日本金融基準，評估 LLM 在會計欺詐檢測、盈餘預測以及產業預測等任務，使用十年的 EDINET‑API 公開報告。提供構建與評估代碼，資料集已重新授權為 PDL 1.0。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 803 / ⭐ 15 / Dataset 卡片（針對 “wikipedia-ja-20230720” 日文維基百科快照）
 * [Wiki-JA-Pair](https://huggingface.co/datasets/llm-jp/Wiki-JA-Pair) - 📥 792 / ⭐ 2 / 一個由 jawiki-20250501 文章構建的日本維基百科圖片說明文字資料集，包含 1,054,434 個獨特（圖像、說明）對，以及 1,047,565 張已下載圖像，並附帶尺寸、hash、頁面資訊等元資料，下載成功率為 99.35%。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 760 / ⭐ 16 / 日語及多語系 QA、NLI 與同義句資料集的目錄，說明各資料集的檢索或 QA 任務以及其授權規範（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [Hadou-Voice-Dataset](https://huggingface.co/datasets/hadou1225/Hadou-Voice-Dataset) - 📥 740 / ⭐ 2 / 一個日語語音資料集，包含 966 個「Calm Voice」片段（約 114 分鐘）和 424 個「ITA Corpus」片段（約 39 分鐘），由 Hadou 提供，可用於 AI 訓練、TTS、聲音轉換、LoRA 創建或直接納入任何專案，並可選擇給予署名。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 732 / ⭐ 89 / 一個自動翻譯的日語版 databricks‑dolly‑15k dataset，採用 CC‑BY‑SA‑3.0 授權，最後更新於 2023‑05‑11。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 682 / ⭐ 14 / JMMLU 是一個日本大型多任務語言理解基準，包含 7,536 個由教師精心編寫的問題，涵蓋 56 個科目，包含專業醫學、心理學、會計、哲學，以及多種高中學科。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 666 / ⭐ 5 / STAIR‑Captions 在 2017 年發布，提供 820,310 條日語字幕，用於字幕生成、多模態檢索和圖像生成，並帶有詳細標註、元資料以及 Creative Commons BY‑4.0 license。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 657 / ⭐ 5 / JAMMEval 是七個日本 VQA 數據集的蒸餾基準，經過兩輪人工註釋以消除歧義和非視覺問題，提供對多模態日本任務的視覺‑語言模型可靠評估。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 608 / ⭐ 8 / Rakuda 提供 40 個日文問題—針對歷史、社會與政府的開放式題目，以及針對地理的專門題目—作為基準測試日本 AI 助手的資料，與 vicuna‑eval 相似，並可透過 `datasets.load_dataset` 載入。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 596 / ⭐ 24 / cc100-ja 是 cc100 資料集的日本語部分，提供為分片 Parquet 檔案。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 582 / ⭐ 3 / 日本語指令資料集，含 632,636 個多回合樣本（約 6.35 億 tokens）以及 GPT‑OSS‑120b 理由痕跡，針對開放式、數學、寫作與多選題 (MCQA) 任務，在 135 個財務主題及 20 個一般主題中使用，旨在微調 LLM 在財務領域的推理能力。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 579 / ⭐ 159 / Japanese Anime Speech Dataset 提供 73,004 對音頻-文字對（共 110 小時，從 V1 演進至 V5），用於提升 ASR 模型（如 OpenAI 的 Whisper），在開放授權下可供任何使用，若能標明來源將不勝感激。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 554 / ⭐ 5 / 資料集卡片詳述日語變體 “mc4‑ja‑filter‑ja‑normal”，附加資訊待補充。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 552 / ⭐ 12 / JaQuAD 是 2022 年的日本 QA 資料集，包含 39,696 對 SQuAD‑style 抽取式問答對，來源於 Wikipedia，總量 73.2 MB，當使用 BERT‑Japanese 微調時，F1 分數達 78.92 %（EM 63.38 %）。
 * [honkoku-lines](https://huggingface.co/datasets/yuta1984/honkoku-lines) - 📥 541 / ⭐ 2 / 一份公民科學資料集，包含 1,169,304 行經過轉錄的日本歷史文本，來源於 79,086 張 IIIF 頁面影像。該資料集以約 1 GB 的 WebDataset 分片形式提供，其中包括高度為 256 px 的 JPEG 行圖裁剪以及相應的元數據，已準備好進行訓練/驗證/測試分割。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 521 / ⭐ 7 / JHumanEval 是手工翻譯的日本版 HumanEval benchmark，提供 164 個 Python 程式設計問題，並提供對應的英文與日文註解，旨在評估 Japanese-LLM 程式產生，同時保留原始英文錯誤。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 512 / ⭐ 5 / 一組日文與英文網路語料庫，包括 9 B‑token 日文集（JA‑WEB‑9B）、63 B‑token 英文及日文集（EN‑WEB‑63B、JA‑WEB‑63B）以及合成版本，如改寫版 JA‑PARAPHRASE‑63B、指令式 JA‑INSTRUCT‑63B 與翻譯版 JA‑TRANSLATE‑63B，供在資料受限情境下研究對日文 LLM 進行預訓練的資料增強。
 * [joyo-kanji-yomi-benchmark-parakeet](https://huggingface.co/datasets/Parakeet-Inc/joyo-kanji-yomi-benchmark-parakeet) - 📥 512 / ⭐ 5 / 一套基準資料集與評估工具包，用於測量日本語 G2P、形態素分析器和 TTS 系統在朗讀文化省「常用漢字」列表時的準確度，包含 4,512 個漢字-閱讀對，每個對應三句帶標註的範例句，以及多重讀音的詳細註解。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 511 / ⭐ 3 / 2010 年的日本網路語料庫已上傳至 HuggingFace，並按 2009 年版權改革為研究授權，包含自動帶標點的文本，這些文本來自形態學解析和轉換腳本。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 510 / ⭐ 20 / 一個日語 QA 數據集，用於評估 Retrieval‑Augmented Generation (RAG)，由 JAQKET 題目與 Wikipedia 文章構建，帶有金鑰檢索相關性標簽，已於 HuggingFace 和 GitHub 發布，主要以 nDCG@10 作為評分指標。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 501 / ⭐ 35 / Syosetu711K 是一個日本資料集，於 2023 年 3 月 26‑27 日從小説家になろう抓取約 711,700 本小說，提供全文和元資料（標題、作者、NCode、簡介等）供無監督文本生成和分類任務使用。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 499 / ⭐ 6 / Dataset card for “oscar2301‑ja‑filter‑ja‑normal”，為 Oscar 資料庫中日語過濾與正常子集。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 498 / ⭐ 2 / Hugging Face 的 ABEJA‑CC‑JA 資料集鏡像，存放於 OpenData AWS 註冊庫，並附有連結至 Abeja 技術部落格的說明文件。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 493 / ⭐ 143 / 日語說明式對話資料集，用於微調 LLM（例如 LoRA），9M+ 範例，最近更新為去除授權的 Alpaca 數據，清理 Wikipedia 和 ALT 輸出，並以 CC‑BY‑SA 4.0 發佈。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 489 / ⭐ 13 / LLM‑jp 提供一個日語指令調校數據集，來自 oasst2 的英語子集經 DeepL 翻譯（源自 kunishou/oasst2‑135k‑ja）並由 Kiyomaru 與 Kodama 編譯。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 477 / ⭐ 3 / 日文維基百科句子被轉換為各種嵌入，並建立 FAISS 索引，提供 Hugging Face Space 的演示、轉換腳本，以及對搜尋、問答和 OpenAI text‑embedding‑3‑small 在 RAG 中的評估；嵌入採用 OpenAI 授權，其他則採用 CC‑BY‑SA‑4.0。
 * [EliteVoiceProject](https://huggingface.co/datasets/Elite35P-Server/EliteVoiceProject) - 📥 476 / ⭐ 13 / 一個非官方的 Hololive VTuber 樱井みこ（Sakura Miko）語音資料集，用於語音辨識研究，按來源平台整理並分為訓練/測試資料夾；使用受 Hololive 的粉絲創作指引所管制，版權屬於 Cover Corp。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 474 / ⭐ 15 / JGLUE 資料集卡片，使用於《Large Language Model Introduction》一書，來源自原始倉庫，程式碼採用 CC BY‑SA 4.0 許可，資料受發行者授權，引用 Kurihara & Kawahara（以日文）並建立於 Shunsuke Kitada 的倉庫。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 422 / ⭐ 6 / Range3 的 wikipedia-ja-20230101 存儲庫提供只包含日文維基百科文本的 Parquet 檔案，這些文本是從完整的維基百科資料集提取並使用 Python 程式碼生成。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 422 / ⭐ 7 / 一個經過重新格式化以符合 SentenceTransformers 友好列與結構的日本資料集，透過 RelRank 分數篩選為正向（≥0.7）和負向（≤0.3）對，來自多個 HuggingFace 資源，用於對比學習。
 * [oscor-2301-ja-text-content](https://huggingface.co/datasets/ayousanz/oscor-2301-ja-text-content) - 📥 417 / ⭐ 2 / 從 OSCOR-2301-ja JSON 文件的「content」欄位提取出的文字檔，透過一個解析每行 JSON 並將內容值寫入輸出檔案的 Python 腳本產生。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 410 / ⭐ 5 / 一個日語開放領域問答資料集 JAQKET，提供測驗式多選題（v1.0）與自由文字答案生成（v2.0），其中 v1.0 具有 13 061 個訓練範例和 271 個驗證範例，而 v2.0 擁有 2 154 個訓練範例和 1 164 個驗證範例。
 * [Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k) - 📥 408 / ⭐ 8 / 39,600 個樣本的日語小說寫作任務資料集，由 deepseek-ai/DeepSeek-V3-0324 生成，包含兩回合 OpenAI 風格對話（包括可選的 NSFW 內容），並以 MIT 授權發佈。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 385 / ⭐ 18 / 一個適合 NLP 的 Wikipedia 文章資料集，來源自 2024 年 1 月的 HTML 資料快照，保留段落結構、元資料（如消歧、性、暴力旗標、模板、時間戳）以及在 GitHub 上托管的相關抽取腳本。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 378 / ⭐ 4 / 提供一個日文搜尋/問答資料集，包含每個查詢的分數，這些分數由五個多語言／日文再排序器計算（如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base），並包括每個查詢大約 200 篇正面與負面範例文件的平均分數。
 * [Umamusume-voice-transcription](https://huggingface.co/datasets/TLME/Umamusume-voice-transcription) - 📥 374 / ⭐ 8 / 一個針對遊戲 Umamusume 的轉錄資料集，包含 77 個角色的語音與相應的音訊剪輯，其總時長約為 12,000 秒，涵蓋 50 匹命名馬匹。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 367 / ⭐ 5 / 可下載的81 歲日本女性聲音語料庫（含原始與降噪 wav 檔、音素／假名＋韻律標籤）可免費供學術使用，並須署名「Fusic Saoyoshi Voice Corpus」。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 329 / ⭐ 25 / 使用英文提示生成的 AI 動漫插圖，以及來自 Phi‑3 Vision 的字幕（英文與日文），已釋出至公共領域供免費使用。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 323 / ⭐ 3 / 資料集卡為「Introduction to Large‑Scale LLM II」一書中使用的 ja‑vicuna‑qa‑benchmark，並由 llm‑jp‑eval 為跨資料集的日語 LLM 評估所創建（Apache 2.0）。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 319 / ⭐ 2 / JCommonsenseQA 是一個日語多選題常識推理資料集——CommonsenseQA 的改編版——授權為 CC BY‑SA 4.0，並以 doi:10.5715/jnlp.30.63 引用。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 312 / ⭐ 4 / 一個可透過 `ass` Python 函式庫或字幕編輯器（如 Aegisub）使用的日語動畫字幕資料集，採用 Advanced SubStation Alpha (SSA/ASS) 格式，授權為 ODC‑BY。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 305 / ⭐ 6 / Japanese XL‑Sum 子集經 PaLM‑2 15‑gram 重疊過濾，包含 4,215 個訓練、758 個驗證以及 766 個測試範例。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 291 / ⭐ 48 / Galgame_Speech_ASR_16kHz 是一個 16 kHz ASR 資料集，包含 3.75 百萬對（≈5,354 h），由 Galgame_Dataset 派生，採 GPL v3.0 授權，禁止商業使用，且任何訓練出來的模型必須開源（引用可選）。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 281 / ⭐ 2 / 一個多模態日語表格問答資料集，用於直接從年度證券報告表格中提取單元格值，提供圖像、帶有邊界框的 OCR 文本、問題和答案，並採用 CC‑BY‑4.0 許可。
 * [japanese-math-synthetic-108k](https://huggingface.co/datasets/yamaTK/japanese-math-synthetic-108k) - 📥 281 / ⭐ 2 / 一份已清理、無重複的日本數學題目資料集，用於 LLM‑JP 2026 調教競賽，覆蓋中學至高中IIIC等級，由 GPT‑OSS 120B 生成並驗證，包含詳細提示、逐步推理、解題者解答，以及跨年級和主題類別的結構化 JSON 架構。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 277 / ⭐ 17 / 一個 104 GB、包含 370 萬檔案的 Galgame 語音資料集，採用 16 kHz 壓縮並帶有情感標籤（由 LLM 自動註記，準確度未經保證），需要符合 GNU GPL v3 條款，禁止商業使用，且必須開源模型基於此資料集進行訓練。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 273 / ⭐ 22 / 一個日本網路文件與影像資料集（約5600萬頁、1100億字元、2.49億張圖像），名為MOMIJI，設計用於訓練視覺‑語言模型，並附帶互動式可視化工具及生成文字欄位的實用腳本。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 267 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 資料集的一個 500 個樣本子集，授權為 CC BY 4.0，用於基準測試 EvoVLM‑JP‑v1‑7B。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 267 / ⭐ 3 / WildGuardTestJP 是一份包含 1,725 個樣本的日文評估資料集，透過多階段精煉流程（Seed‑X‑PPO‑7B、gpt‑oss‑120b、Qwen2.5‑72B‑Instruct、gemma‑3‑27b‑it）忠實翻譯自 WildGuardTest，並於 Hugging Face 上以 ODC‑BY 許可發布。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 264 / ⭐ 36 / 一個 409 小時的日本 eroge 語音資料集，經 2-pass loudnorm 處理（‑23 LUFS、‑1 dB peak、11 LRA），由 litagin/anime-whisper 轉錄，已匿名化，存儲為 WebDataset（FLAC、JSON、TXT），主要包含女性聲音，可能存在 AI 轉錄錯誤，並以 MIT‑licensed 供學術研究。
 * [cc100-ja-documents](https://huggingface.co/datasets/hotchpotch/cc100-ja-documents) - 📥 262 / ⭐ 4 / 一個日文文件級別的 cc100 資料集版本，從 HuggingFace 上的逐行拆分資料合併而來，並依照原始 cc100 條款授權。
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 251 / ⭐ 5 / 使用 Whisper Large‑V2 從影片中轉錄 Makise Kurisu VN 對話，並以 pydub 分割成片段；未經清理的文字僅供 TTS 模型訓練之用，並非作者作品。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 245 / ⭐ 6 / JetCopper‑10B 是一個約 4.7 億詞彙（外加 0.9 億英文程式碼）的日本文本語料庫，來源於 CC‑100、OSCAR‑2301、HPLT v1.2 和 wiki40b‑ja，在清理和去重後使用，以預訓練 Contrail‑200m‑64k 用於 LOCAL AI HACKATHON #000 calm2‑chat，但缺乏句子邊界和困惑度過濾。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 244 / ⭐ 26 / 此倉庫存放了 OpenAssistant/oasst1 資料集的日文翻譯版本，包括帶有錯誤標記的自動翻譯條目、約 2,000 筆人工更正、以聊天格式擷取的子集，以及將資料轉換為指令‑輸出對以便微調的腳本。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 244 / ⭐ 16 / 僅包含足夠長度的多發佈者記錄、已標準化發佈者名稱及平衡主要發言者的日本角色扮演對話資料集，供機器學習應用。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 241 / ⭐ 3 / 一個經過清理的日語網路語料庫（例如 mc4‑ja），透過非監督式學習聚類成約 10,000 組，可用於合法分析；在 “out” 資料夾中僅列出部分文件為 Parquet 格式，並可透過 Git LFS 下載。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 240 / ⭐ 10 / llm‑jp‑instructions 是一個手動編輯的日語指示資料集 (v1.0)，提供 train、dev 和 test 分割，可透過 load_dataset 存取。
 * [Japanese-wiki-dump-sentence-dataset](https://huggingface.co/datasets/AhmedSSabir/Japanese-wiki-dump-sentence-dataset) - 📥 239 / ⭐ 7 / 清潔的日語資料集，包含 500 萬句完整句子並附有上下文，適用於訓練無監督語義相似度模型。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 236 / ⭐ 17 / Jagle 是一個約 920 萬筆的日本多模態後訓練資料集，由圖像–文字配對和 PDF 文本庫構成，用於訓練 LLM‑jp‑4‑VL 9B beta，並證明能提升日語視覺-語言任務的表現。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 233 / ⭐ 7 / VOICEVOX‑generated synthetic voice dataset comprising 445,793 .wav files (totaling 577 h 51 m 23 s) built from the ITA, つくよみちゃん, and ROHAN corpora.
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 232 / ⭐ 33 / 一份去除 izumi-lab 的 llm-japanese-dataset 中英日翻譯資料的日本聊天數據集，旨在通過 LoRA 進行指令回應任務的日語 LLM 微調，並以 CC‑BY‑SA 4.0 授權公開。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 220 / ⭐ 8 / Livedoor News Corpus 提供一套日語新聞文章數據集，分為 5 894 個訓練、737 個驗證和 736 個測試實例，已去除 HTML 標籤並以 Creative Commons Attribution‑NoDerivs 授權釋出。
 * [CABankSakuraCHJP](https://huggingface.co/datasets/Fhrozen/CABankSakuraCHJP) - 📥 218 / ⭐ 2 / 日語 CallHome 語料庫：120 位講者，200 條電話錄音（每條最多 30 分鐘），來自美國，透過免付費 LDC 機器人操作員錄製，每通話支付 $20，並以 80/20/100 的比例分為訓練集／驗證集／測試集。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 212 / ⭐ 2 / 日本 Common Voice 17.0 子集已過濾至 649 個客戶 ID，每個包含 30–300 個樣本，按 8:2 分成訓練/驗證，分批成 1,000 個樣本的 Parquet 檔，總計 45,668 個樣本 (CC0 授權)。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 210 / ⭐ 18 / 一個 190 M‑pair 的 JSONL 資料集，用於日語假名到漢字的轉換，包含「左側上下文 – 輸入 – 輸出」三元組，以及預訓練模型（medium、small、xsmall）和 AJIMEE-Bench 基準測試，採用 CC BY‑SA 4.0 授權發布，其子集來源於 Wikipedia 和 Common Crawl。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 208 / ⭐ 4 / JFWIR 是一個大型的日語資訊檢索資料集，包含超過 6400 萬個文件–查詢對 — 由高品質教育網頁內容生成，具備七種查詢類型與難題負例，以提升對比學習並在 JQaRA、MIRACL(ja)、jsquad 與 JaCWIR 等任務上進行基準測試。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 199 / ⭐ 3 / 一個大規模、基於時間戳的 JSONL 資料集，包含來自 2ch.sc 的日本匿名論壇主題，詳細列出主題 ID、標題、區域、版面名稱、回覆數，以及貼文陣列（含使用者、郵件、日期、ID、內容以及可選的標題欄位）。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 198 / ⭐ 27 / WRIME 數據集是一個日本語收藏，包含 42,200 篇文章，已用 Plutchik 的八種情緒為作者、三位讀者以及他們的平均值進行標註，並結構為 40k‑train、1.2k‑validation、2k‑test 的分割，供情感分析任務使用。
 * [swallow-magpie-ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1) - 📥 198 / ⭐ 5 / 一個日英對照指令調教資料集（各 42k 對），作為 Swallow‑Magpie‑Ultra‑v0.1 的一部分發布，用於訓練 tokyotech‑llm 模型，從 magpie‑ultra‑v0.1 中提取，平均品質良好。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 191 / ⭐ 24 / AutoWikiQA 是最大的免費日語問答資料集，提供超過230萬個手工篩選的問答對，這些問答對自維基百科自動生成，使用 Swallow‑MX 和 LLMs（無規則基模板），以支援知識傳授與檢索增強生成應用。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 191 / ⭐ 43 / 一個排行榜，根據大型語言模型在將日文視覺小說翻譯成英文時的語義準確度進行排名，使用 256 個樣本的餘弦相似度並報告 chrF 分數，以便與 Sugoi Translator、Google Translate、Naver Papago 和 Alibaba Translate 等工具比較。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 186 / ⭐ 21 / 這是一份 SNOW T15/T23 Japanese simplification corpus 的資料集卡片，包含 50 k 手動對齊的原始簡化日語 (≤2 k‑word vocab) 與 English translation records，以及 35 k 擴充集，供日英文本簡化與翻譯使用。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 179 / ⭐ 5 / SNLI 自然語言推理基準（JSNLI）的日文翻譯，提供 TSV 格式的詞形分割前提與假設，並包含篩選與未篩選的訓練拆分，以及 3,916 對驗證集，採用 CC BY‑SA 4.0 授權。
 * [DEJIMA-dataset](https://huggingface.co/datasets/MIL-UT/DEJIMA-dataset) - 📥 179 / ⭐ 5 / DEJIMA 是一個日本規模的網路資料集，包含 3.88 M 張圖像與 LLM 生成的說明文字及 VQA 答案。此資料集透過嚴格篩選、重複移除、偵測驅動的證據提取以及基礎對齊限制製作，並提供多種標題化與 VQA 變體以供分析。
 * [ogiri-bokete](https://huggingface.co/datasets/YANS-official/ogiri-bokete) - 📥 178 / ⭐ 4 / 一個僅包含日文的數據集，來自 Bokete crowdsourced joke 網站，分為三項任務——文字到文字、圖像到文字以及圖像中的文字完成，每項各有 100 個提示（約 900 答案），圖像到文字則有 500 個提示（2355 答案）。資料經過 OCR 處理並篩除不當內容。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 177 / ⭐ 2 / COVID‑19 日本 Twitter 數據集提供日本推文 ID 與評估碼 (63–68)，指出 COVID‑19 的相關性以及事實／意見狀態，從而促進文本分類研究。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 176 / ⭐ 2 / 一份日本線上廣告資料集，用於五個 NLP 任務——廣告可接受性、一致性、性能估算、A3 認識與相似度，並以 TSV 格式提供 train/dev/test 拆分。
 * [joyo-kanji-yomi-benchmark](https://huggingface.co/datasets/sbintuitions/joyo-kanji-yomi-benchmark) - 📥 176 / ⭐ 10 / 一個日本 TTS 基準，評估所有 2,136 個常用漢字的發音，共有 4,378 種讀法，使用 13,095 條由母語者驗證的句子，每條句子針對單一讀法並標註自動 CER 計算，採 MIT 授權。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 169 / ⭐ 17 / oasst1‑21k‑ja 是一個由 DeepL 從英文 OASST1 子集衍生而來的日語指令調整資料集，通過日本的 LLM‑jp 合作項目創建；如需聯繫，請發送電子郵件至 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 以及 Okamoto。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 167 / ⭐ 82 / 一個日本網路小說章節資料集，配有英文粉絲翻譯，在第 2 版擴展到 106K 對齊句子，包含系列元資料，未進行品質篩選，並以公平使用/Apache 2.0 發佈，附帶下架條款。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 166 / ⭐ 16 / 一個日語 Alpaca 風格的合成資料集，使用 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 建立並透過 Deepinfra 精煉，其中「_cleaned」條目已經驗證其指令清晰度、語言一致性與相關性，並以 Apache 2.0 授權發佈。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 165 / ⭐ 4 / 「Japanese RAG Generator Benchmark (J‑RAGBench)」供應一份多分類 QA 數據集—涵蓋 Integration、Reasoning、Logical、Table 與 Abstention—旨在評估日文 RAG 生成器，並由人力與 GPT‑4.1 建構，且以 CC BY‑SA 4.0 授權發布。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 161 / ⭐ 9 / JSICK 是一個日英 NLI 與 STS 數據集，透過翻譯 SICK 語料庫而創建，包含一組壓力測試資料，用於探討詞序與格助詞處理，分別有 1,666、797 和 1,006 對句子對應不同的語法關係。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 160 / ⭐ 6 / 這份 20,800 檔案的 WAV 數據集包含 195 位日本 AItuber 人格──其中包括參考、原始、描述性和情感語句──並附帶詳細的人格與聲音元資料，準備好透過數據科學 API 進行檢索。
 * [JA_audio_JA_text_180k_samples](https://huggingface.co/datasets/Sin2pi/JA_audio_JA_text_180k_samples) - 📥 155 / ⭐ 9 / 一個 GitHub wiki 頁面，詳細說明了在日語處理中使用的 neologd MeCab 字典所採用的正則表達式規則。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 154 / ⭐ 16 / 一個簡易的 Zundamon 角色設定資料集—由線上來源及管理數據編輯—用於測試 character‑LLMs，提供於 zmnjp.jsonl 與 zmn.jsonl 格式，並依指定授權提供。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 154 / ⭐ 2 / WAON 是一個大型、高品質的日語圖像-文字配對資料集，透過規模、SigLIP‑score 過濾以及去重（按 URL、標題和 pHash）建立，並以 Apache 2.0 於 HuggingFace 釋出，用於資訊分析。
 * [OpenSakura-DS-260220-LN-ja-zh-COT-Lilith](https://huggingface.co/datasets/OpenSakura/OpenSakura-DS-260220-LN-ja-zh-COT-Lilith) - 📥 153 / ⭐ 2 / OpenSakura‑DS‑260220‑LN‑ja‑zh‑COT‑Lilith 是一個 1.64 百萬行的日文到中文輕小說翻譯資料集（約 18 GB），採用映射式 5 路切分，保留推理內容與結構化欄位，如 uuid、episode 與 segment 索引。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 150 / ⭐ 4 / 由 Guo, Mandy、Dai, Zihang 與 Vrandečić, Denny 撰寫的 Wiki40B 數據集日本語子集重新排版。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 148 / ⭐ 7 / 量化語音輸入與文字輸入（針對語音語言模型）的智力差距的一個資料集，由從 Elyza‑tasks‑100、M‑IFEval 和 JamC‑QA 基準中合成的音訊組成，分為四個子集；文字使用 CC‑BY‑SA 4.0 授權，音訊僅允許非營利、非再分發使用。
 * [Japanese-Heron-Bench](https://huggingface.co/datasets/turing-motors/Japanese-Heron-Bench) - 📥 146 / ⭐ 11 / Japanese‑Heron‑Bench 是一個日本 VLM 基準測試，包含七個子分類的 21 張圖像，每張圖像配有三類問題（對話、細節、複雜），共計 102 個查詢，並採用 CC BY 授權。
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 145 / ⭐ 6 / 一組去重、已清理（NFKC‑標準化）的 mQA 數據集中的查詢–段落對集合，`pos_ids` 和 `neg_ids` 指向相應的集合以便於檢索，並遵守原始數據的授權條款。
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 145 / ⭐ 4 / JP Voice‑Text Dataset for Arknights Waifus：10,905 個日語聲音片段（總計 26.3 小時）來自單一演員角色，適合微調或評估 ASR/ASV 模型。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 145 / ⭐ 26 / 收集自個人資料的 2,300 萬條日本 web‑novel 紀錄（約 800 億字元）資料集；請求後僅限於正當機器學習用途。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 144 / ⭐ 11 / 三個 Parquet 檔案，包含 Wiki40B 數據集的日語子集，由提供的 Python 腳本產生。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 144 / ⭐ 18 / Databricks‑dolly‑15k‑ja 數據集是一個 DeepL 翻譯的日文版本，為指令微調而由日本 LLM‑jp 專案創建，作者為 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 與 Takumi Okamoto。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 144 / ⭐ 9 / JMMMU‑Pro 是一個基於圖像的日語多模態基準，透過現實模型生成視覺問題並經由人工驗證而創建，顯示目前開源 LMM 在此任務表現不佳，同時提供一種成本效益高的方法供未來 VQA 基準發展使用。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 140 / ⭐ 3 / 一個包含 64,139 項日文姓名的資料集，已按生物性別標記——採用漢字、平假名與羅馬拼音——其 44.9k 訓練集、6.41k 驗證集與 12.8k 測試集的分割方式獲得 ISDA’23 的接受。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 140 / ⭐ 2 / KokoroChat 是最大的日本心理諮詢對話資料集—由 480 位受訓顧問進行了 6,589 次角色扮演會談，平均每次 91 則發言—包含豐富且長篇的對話、詳細的 20 維客戶回饋，並支援同理心回應生成、對話評估以及心理健康語言模型的研究，並已於 ACL 2025 接受。
 * [KokushiMD-10](https://huggingface.co/datasets/humanalysis-square/KokushiMD-10) - 📥 140 / ⭐ 7 / KokushiMD‑10 是一個多語言基準，涵蓋十種日本醫療保健職業，提供純文字與圖像的單選、多選、計算以及填空題，並附有思考鏈解釋，可分別以日文、英文或混合拆分方式使用。
 * [Furigana-Aozora-Speech](https://huggingface.co/datasets/Calvin-Xu/Furigana-Aozora-Speech) - 📥 139 / ⭐ 2 / 已處理所有原始文本文件，產出一個經過清洗的語料庫共 3,361,443 條條目，剔除了重複項目以及缺乏漢字的任何條目。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 135 / ⭐ 11 / 日本語テキスト（kaken サブセットの llm-jp-corpus-v3 から）を Qwen/Qwen2.5-32B-Instruct で英訳し、CC-BY 4.0 ライセンスのもとでオープンな日本語–英語パラレルコーパスとして公開。元データセットの利用規約は継承されます。
 * [michiyomi-tokyo-streetscape](https://huggingface.co/datasets/finalvent/michiyomi-tokyo-streetscape) - 📥 134 / ⭐ 2 / 一份東京街景語音化資料集，將 1,009,250 張 Mapillary 圖像與全市 23 個區域內可見特徵的日文文字描述配對，該資料集透過視覺‑語言模型生成，未使用外部知識。
 * [hh-rlhf-12k-ja](https://huggingface.co/datasets/llm-jp/hh-rlhf-12k-ja) - 📥 133 / ⭐ 14 / 由 LLM‑jp 使用 DeepL 產生的 hh‑rlhf 數據集子集之日文翻譯，作者按字母順序列出，聯絡方式為 llm-jp(at)nii.ac.jp。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 129 / ⭐ 14 / 一個商業用途的 180 萬例日語翻譯版本，屬於 OpenMathInstruct‑1 數學指令微調資料集——由 GSM8K 和 MATH 基準問題生成，使用 Mixtral‑8x7B 解答並經過正確性驗證；並以 NVIDIA 許可發佈，重新分發時需承襲該許可。
 * [danbooru-ja-tag-pair-20241015](https://huggingface.co/datasets/p1atdev/danbooru-ja-tag-pair-20241015) - 📥 128 / ⭐ 10 / 一個 150 K 條目資料集，包含 Danbooru 標籤及其日文翻譯（於 2024‑10‑15 更新），由擴充的 wiki 資源構建，經 FastText 過濾以移除非日語標籤，並使用 Calam Chat 的少量示例翻譯補全缺失項目。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 128 / ⭐ 11 / 一個高品質的合成日語數學題目資料集，具有已驗證的鏈式思考推理，透過 Qwen2‑7B‑Instruct 將 PRM800K 和 GSM8K 進行翻譯並篩選正確性後構建，可透過 Hugging Face datasets library 獲取。
 * [jmultiwoz](https://huggingface.co/datasets/nu-dialogue/jmultiwoz) - 📥 127 / ⭐ 8 / JMultiWOZ 是一個大型日語多領域任務導向對話資料集，包含 4,246 條 Wizard‑of‑Oz 收集的對話，跨六個領域（restaurant、hotel、attraction、shopping、taxi、weather），提供使用者目標、對話狀態和發言，用於訓練對話狀態追蹤與生成模型。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 127 / ⭐ 33 / 提供日文 RAG 基準，涵蓋金融、電訊、製造、公共、零售五大產業領域，透過發布資料集、自動評估框架，以及比較結果，例如 Claude 3.5‑Sonnet、GPT‑4o 等模型。
 * [Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k) - 📥 123 / ⭐ 4 / 一份包含39.6k條目之合成日語角色扮演資料集，由 gpt‑4o‑mini 生成，對話每個互動含5–10回合，並帶有元資料鍵如類型、年齡標籤、世界/場景/使用者/助手設定、語氣及 OpenAI 訊息格式，採用 CC‑BY‑NC‑SA 4.0 授權。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 123 / ⭐ 2 / 由 LLM 生成的日語查詢與答案資料集，來源於改寫的 Wikipedia 文字，並以 CC‑BY‑SA 4.0 釋出。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 120 / ⭐ 14 / 日本語 NER 數據集，來源自維基百科，採用 CC‑BY‑SA 3.0 授權，由 Stockmark Inc. 所創建
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 119 / ⭐ 17 / 資料集「japanese_alpaca_data」在 masa3141 的 Japanese‑Alpaca‑LORA 工作基礎上，提供了一個精心策劃的日本 Alpaca 資料集，用於研究與應用。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 119 / ⭐ 2 / JA CallHome 資料集已轉換為 WAV，並附有 JSON 結構化的元資料與 RTTM 口述檔供評估。
 * [azurlane_voices_jp](https://huggingface.co/datasets/deepghs/azurlane_voices_jp) - 📥 118 / ⭐ 10 / 一份日語聲音文字資料集，涵蓋 30,160 條錄音（≈75.8 小時），來源於單一演員的聲音，可用於微調或評估 ASR/ASV 模型。
 * [liz-nojaloli-ja-ds](https://huggingface.co/datasets/ebisuke/liz-nojaloli-ja-ds) - 📥 117 / ⭐ 3 / MIT 授權的手工製作日文資料集，用於訓練「liz‑nojaloli‑ja」，並附帶透過 Qiita 連結的 Python 程式碼，旨在為未來的 RLHF 準備。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 117 / ⭐ 6 / 日本動畫語音資料集，原始 joujiboi/japanese‑anime‑speech‑v2 集合的分割版本。
 * [fgo_voices_jp](https://huggingface.co/datasets/deepghs/fgo_voices_jp) - 📥 116 / ⭐ 16 / FGO Waifu 的 JP Voice‑Text 資料集：包含 30,800 條記錄、66.4 小時的日語音訊集合，涵蓋單一配音員角色台詞（每條約 7.76 秒），適用於 ASR/ASV 微調與評估。
 * [Magpie-Tanuki-8B-97k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-97k) - 📥 116 / ⭐ 12 / 一個由將 Magpie 方法應用於 weblab‑GENIAC/Tanuki‑8B‑dpo‑v1.0 所創建的 97,269 條日本對話資料集，可能包含因未進行後續過濾而產生的低品質記錄。
 * [japan-law](https://huggingface.co/datasets/y2lan/japan-law) - 📥 115 / ⭐ 22 / 日本法律電子政務提供一份去重的法規資料集，包含編號、標題、ID、生效日期與全文，以截至 2023 年 8 月 1 日為止最新生效版本。
 * [llmjp-kaken](https://huggingface.co/datasets/hpprc/llmjp-kaken) - 📥 114 / ⭐ 6 / 已將 llm‑jp‑corpus‑v3 的 kaken 子集轉換為 Hugging Face 格式，並從每個 URL 擷取原始文章標題，授權於 CC‑BY 4.0。
 * [modern_haiku](https://huggingface.co/datasets/p1atdev/modern_haiku) - 📥 112 / ⭐ 4 / 一份精選的 37,158 條現代日語俳句資料集，來自 Modern Haiku Association，每條俳句包含 ID、文本、作者、可選評論者備註、季節標籤，以及連結的季語「kigo」詞彙（含發音與別名）。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 111 / ⭐ 9 / 此為 llm-book/wrime‑sentiment 的資料集卡，提供一個由 WRIME 衍生的二元日語情感分析集合，根據 Avg. Readers_Sentiment 標記為正向或負向（可選擇包含中性案例），並作為《Introduction to Large Language Models》一書的樣本資料。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 111 / ⭐ 29 / 一份由手工從日本政府網站提取的 FAQ 數據集，採用 CC‑BY‑4.0 授權，旨在供大型語言模型進行指令微調與 RAG 測試使用，提供高品質問答對及來源網址。
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 110 / ⭐ 24 / RealPersonaChat 是一個約 14,000 條對話的日本語對話語料庫，包含說話者的人格特質與角色設定，提供發言資料（含評分）以及詳細的說話者檔案（persona、Big Five 分數、人口統計）。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 109 / ⭐ 3 / 一份日語 BIG‑Bench Hard 資料集 (bbh‑ja)，提供評估問題與 Chain‑of‑Thought 提示，分別以 JSON Lines 與 YAML 格式呈現，翻譯由 PLaMo 模型生成。
 * [wikidata-parallel-descriptions-en-ja](https://huggingface.co/datasets/Mitsua/wikidata-parallel-descriptions-en-ja) - 📥 107 / ⭐ 9 / 一個即時可訓練的英日機器翻譯語料庫，來源於 Wikidata 描述，已清理並去重成 JSONL 檔案，用於 Hugging Face transformers，可在 CC0 1.0 取得。
 * [Magpie-Tanuki-8B-annotated-96k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-annotated-96k) - 📥 107 / ⭐ 6 / 對一個 96k 樣本資料集進行註解，應用 Magpie 方法學於 Tanuki‑8B，使用 calm3 為基礎的提示評估每條指令的難度、品質和類別。
 * [J-ResearchCorpus](https://huggingface.co/datasets/kunishou/J-ResearchCorpus) - 📥 105 / ⭐ 32 / 一個高品質的日文文本資料集（約 3900 萬字符），由 CC‑BY‑4.0 學術論文與會議紀錄（例如 ACL 2024、*NLP* 期刊、東京女子醫學大學等）編譯而成，用於語言模型或 RAG 系統的預訓練，並計畫新增更多 CC‑BY 授權內容。
 * [amenokaku-code-instruct](https://huggingface.co/datasets/kunishou/amenokaku-code-instruct) - 📥 102 / ⭐ 17 / 一個日語指令資料集，共5,200個程式碼生成任務—1,050 用於程式碼生成、150 用於行為檢查、4,000 用於錯誤修復—增強了180個 JaxTon/Java 範例，並來自商業授權的程式設計內容，全部以明確許可證發佈。
