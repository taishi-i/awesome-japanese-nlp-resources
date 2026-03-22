# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專門收錄日語NLP相關的Python函式庫、LLM、詞典和語料庫資源的精選列表。
本頁面列出了Hugging Face上可用的日語NLP專用模型和資料集。目前包含164個模型和109個資料集。

_更新於2026年3月22日_

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

| # | 模型名稱 | Downloads | Likes | 類別 |
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

| # | 資料集名稱 | Downloads | Likes |
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
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 480k / ⭐ 15 / 一個 12 層、768 隱藏層的日本 GPT‑NeoX 模型，訓練於 CC‑100、C4 和 Wikipedia，兼容 Huggingface，並可選擇使用一個玩具前綴調優權重，使每句結尾強制出現笑臉表情符號。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 444k / ⭐ 131 / 一個九十億參數的日文優化 LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，於 2024 年 9 月以前的資料進行訓練，採用混合的 Mamba‑2/MLP/4‑layer‑attention 架構，並在 Nemotron‑Personas‑Japan 工具呼叫資料集中進行微調，可選擇在產生最終答案前生成可控的推理回溯，且可商業使用。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 219k / ⭐ 20 / OpenCALM 是由 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 之下發佈的一套僅解碼器的日語 transformer 語言模型（160 M–6.8 B 參數），經日本維基百科與 Common Crawl 訓練，可透過 Hugging Face 的 torch‑transformers 使用。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 118k / ⭐ 58 / 一個 2.7‑B 參數的日語 GPT‑NeoX 模型，由 ABEJA Inc 在日語 CC‑100 與 OSCAR 上訓練，可透過 Hugging Face Transformers pipelines 或 PyTorch 使用，並以 MIT 授權釋出。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 40k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一個 13‑B 的、已經進行指令預訓練的日語語言模型，由 NII 的 R&D Center 開發，並以 Hugging‑Face Transformers 的 checkpoint 形式發布，使用 UNIGRAM‑byte‑fallback tokenizer。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 39k / ⭐ 28 / LFM2.5‑1.2B‑JP 是一個 1.2B 參數的日語文本生成模型，基於 LFM2.5 混合架構構建，優化用於生成和完成任務，托管於 Hugging Face 並可通過 llama.cpp 運行。
 * [llm-jp-3.1-13b](https://huggingface.co/llm-jp/llm-jp-3.1-13b) - 📥 24k / ⭐ 2 / llm‑jp‑3.1‑13b 是來自 NII R&D Center 的 13 B‑parameter transformer LLM，已在日文文本上預訓練，並以 Hugging Face 格式提供，要求 torch ≥2.3、transformers ≥4.40，另外還提供微調檢查點及 unigram byte‑fallback tokenizer。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 17k / ⭐ 18 / 以 Shisa 7B 數據微調了 Japanese Stable LM Base Gamma 7B，並在 JA MT‑Bench 上取得優異成績。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 14k / ⭐ 146 / Llama‑3‑ELYZA‑JP‑8B 是 ELYZA 推出的日語改良版，8 億參數的 Llama 3 模型，已在 Meta‑Llama‑3‑8B‑Instruct 上為日語進行微調。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 13k / ⭐ 56 / TinySwallow‑1.5B‑Instruct 是一個 1.5 B 日語指令調校的自回歸語言模型，經由 TAID 從 Qwen2.5‑32B‑Instruct 蒸餾，僅供研究使用。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 11k / ⭐ 21 / Llama3 Swallow 是一款日本增強版 Meta Llama 3 系列，於 2024 年 7 月 1 日發布，提供 8B 與 70B 兩種版本，包含 Instruct 與 chat 形式，並使用 SFT 與 Chat Vector 在 Megatron‑LM 上微調，並在關鍵的日本 NLP 任務上進行基準測試。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 11k / ⭐ 18 / Llama 3.1 Swallow 是一組 8‑B 和 70‑B 模型，繼續對 Meta 的 Llama 3.1 進行預訓練以提升日語表現，然後在合成日語數據上進行 instruction‑fine‑tune，提供多個已發佈的變體，具有與 gemma‑3‑27b‑it 相當的對話行為改進。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 10k / ⭐ 25 / rinna 的日語 GPT‑2 small 為 12 層、768 隱藏單元的 transformer，訓練於日語 CC‑100 和 Wikipedia，使用 SentencePiece 進行分詞，於 2021 年 8 月 25 日以 MIT 版發布（Hugging Face：rinna/japanese‑gpt2‑small，詳見 https://arxiv.org/abs/2404.01657）。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 10k / ⭐ 50 / GGUF‑格式的 NVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese，從imatrix數據集重建，已準備好使用 llama.cpp 在 CUDA 上運行。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 9k / ⭐ 24 / Llama 3.1 Swallow 是一系列經過日本優化的 8B/70B Llama 3.1 模型，透過持續預訓練和日本專用說明微調進行訓練，最新的 8B‑Instruct‑v0.3 在日本 MT‑Bench 上取得了最先進的成果。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 9k / ⭐ 4 / 實驗性日本模型，透過採用 chat‑vector 方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 與 Meta‑Llama‑3‑8B‑Instruct 之間的差異，升樣後應用於 Meta‑Llama‑3‑70B‑Instruct，顯示變化不大，並計畫未來擴充。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 7k / ⭐ 18 / GPT‑OSS‑Swallow v0.1 提供 20B 及 120B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，能在數學與編程任務上匹敵或超越 GPT‑OSS，於 2026 年 2 月發布，包含四種 SFT/RL 變體與即將推出的量化版本。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 7k / ⭐ 19 / 提供由 NII 出品的 1.8 B 參數 llm‑jp‑3.1‑1.8b‑instruct4 日語指令調校模型，兼容 Hugging Face Transformers 及 Torch ≥ 2.3.0，包含預訓練與微調檢查點及使用示例。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 5k / ⭐ 8 / Qwen3‑Swallow v0.2 提供日英語 LLM（30B‑A3B 和 32B），採用 CPT、SFT 與 RLVR 訓練，保持強大的數學、程式編寫與推理能力，已發布九個模型及 AWQ‑quantized 變體。
 * [Qwen3-Swallow-8B-CPT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2) - 📥 4k / ⭐ 1 / 雙語 30 B 及 32 B 參數 LLM——Qwen3‑Swallow v0.2，以 CPT、SFT 與 RLVR 構建，能在日文、日英翻譯、數學與程式編寫上表現卓越，與 Qwen3 相當或更優，並以 AWQ 量化形式於 Hugging Face 發佈。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 3k / ⭐ 20 / OpenCALM 是 CyberAgent 發布的一系列日語僅解碼器 Transformer 語言模型（參數 160 M–6.8 B），訓練於日語維基百科和 Common Crawl，並以 CC BY‑SA 4.0 授權發行。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 3k / ⭐ 107 / 一個 1.3‑B‑parameter、24‑layer transformer GPT‑1B，在 Japanese C4、CC‑100 以及 Wikipedia 上訓練，於 2022 年 1 月 26 日由 rinna Co. 發布，並以 MIT license 供使用。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 3k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27‑B 參數擴充，已在包含 instruct 與 fast 變體的日文資料上進行預訓練，可透過 Hugging Face Transformers 使用。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 3k / ⭐ 85 / Rinna 的 24 層、1024 隱藏單元的日本 GPT‑2‑medium 模型，使用 CC‑100 和 Wikipedia 進行訓練，採用 SentencePiece 分詞，已在 rinna/japanese‑pretrained‑models repo 中提供（MIT‑licensed，於 2021 年 4 月 7 日發布，於 2021 年 8 月 25 日更新）。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 3k / ⭐ 26 / 日本語 3.6B 參數 GPT‑NeoX 模型經過調校以符合指令追蹤 (SFT‑v2)，在 100 個提示上與先前的 SFT 針對 ChatGPT 進行測試，於 2023 年 3 月 31 日發布。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 3k / ⭐ 7 / 已預訓練的 TinyLlama，日語版本（≈50k 步），建立於約3B OSCAR/mC4 代幣上，可透過 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 與 Renju Aoki 製作。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 3k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 與 Swallow Team 所開發的一款緊湊型日語指令跟隨語言模型，採用 Qwen2.5‑32B‑Instruct 的 TAID 蒸餾，並進一步於日語文本上進行預訓練，僅以 Apache 2.0 授權釋出，僅供研究用途。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 3k / ⭐ 36 / 提供由 SB Intuitions 推出的自回歸日語語言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已與其他模型進行基準測試，且附帶示例使用腳本，並註明安全訓練有限。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 2k / ⭐ 10 / 此存儲庫提供 GGUF 格式、量化的模型檔，適用於 Stability AI 的日文 StableLM Instruct Gamma 7B，該模型由 Massed Compute 硬體製成，並屬於 TheBloke 的 a16z 資金支持的 LLM 專案的一部分。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 140 / LFM2.5‑1.2B‑JP 是一款為日語優化的聊天模型，在日語知識和指令遵循方面優於 LFM2，支援 LoRA 的微調、使用 Transformers、vLLM、llama.cpp 進行推論，並達到 50.7 JMMLU、58.1 M‑IFEval 和 56.0 GSM8K 分數。
 * [GPT-OSS-Swallow-20B-SFT-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-SFT-v0.1) - 📥 2k / ⭐ 5 / GPT‑OSS‑Swallow v0.1 是一個雙語日英模型家族 (20B & 120B)，透過連續預訓練、監督式微調與可驗證獎勵的強化學習進行訓練，以保持數學與程式碼性能，現已發布 SFT 與 RL 變體，並規劃量化版本。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 2k / ⭐ 21 / youri‑7b 是一個 32 層、4096 隱藏層的 transformer，來源於 Llama2‑7b，持續預訓練於約 40 B 個日語 token（CC‑100、C4、OSCAR、Pile、Wikipedia）並於 2023‑10‑31 發布，並在 AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA 與 Winogrande 上取得競爭性分數。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 1k / ⭐ 1 / Qwen3‑Swallow v0.2 提供 30‑B 和 32‑B 雙語日英 LLM，透過 CPT、SFT 與 RLVR 訓練，提升日語準確度、翻譯、數學與編碼能力，以達到或超越原始 Qwen3，提供九種模型（CPT、SFT、RL）以及 AWQ‑quantized 版本，並同時發布 GPT‑OSS‑Swallow。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 1k / ⭐ 3 / LLM‑jp‑3‑150m — 來自日本情報學研究院 LLM 研發中心的 150M 參數日語語言模型，已以 Hugging Face Transformers 格式發佈，需安裝 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，並以日語維基百科、Common Crawl、WARP/PDF、WARP/HTML 以及 Kaken 數據，使用 unigram byte‑fallback tokenizer 進行預訓練。
 * [japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) - 📥 1k / ⭐ 75 / 一個擁有 3.6 億參數的日語 GPT‑NeoX 模型，使用約 650 GB 的日語文本（C4、CC‑100、Oscar、網絡爬取）進行訓練，於內部 C4 驗證集上取得 7.50 的困惑度，並以 Apache 2.0 授權發布。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ](https://huggingface.co/dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ) - 📥 1k / ⭐ 3 / 提供 Meta 的 Llama‑2 7B（ELYZA‑japanese‑Llama‑2‑7b‑fast‑instruct）的 4‑bit、4.11 GB 量化版本，其可縮減記憶體但會降低指令跟隨，需 GPU 及 autoGPTQ，並包含對替代 AWQ、llama.cpp 及 gguf 量化方法與基準測試結果的參考。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 1k / ⭐ 16 / 一個 6 層、512 隱藏單元的 transformer，名為 Japanese GPT‑2 xSmall，訓練於日本 CC‑100 與 Wikipedia 並使用 SentencePiece tokenization；於 2021 年 8 月 25 日以 MIT 授權發布，並託管於 Hugging Face（rinna/japanese‑gpt2‑xsmall），在 arXiv 2404.01657 中被引用。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 82 / 由 ELYZA 開發的日文增強版 Llama‑2‑7B，預訓練以擴展日語能力，包含標準、指導、快速三種變體，附帶詳細使用範例、開發者貢獻，並採用 Meta 的 Llama‑2 Community License 授權。
 * [Murasaki-4B-v0.3-GGUF](https://huggingface.co/Murasaki-Project/Murasaki-4B-v0.3-GGUF) - 📥 1k / ⭐ 1 / Murasaki‑4B‑v0.3 是一個 40 億參數的 GGUF System 2 推理模型，已針對 ACGN 日英翻譯進行優化，特色包括提示控制的 CoT 切換、增強的 Non‑think 模式、BF16 基準以及多種量化，全部採用 CC BY‑NC‑SA 4.0 授權。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 1k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter 日本語擴展版本，進一步針對日本語語言任務進行預訓練，並提供 base、instruct、fast 和 fast‑instruct 變體，由 ELYZA 團隊在 Llama 2 Community License 下維護。
 * [japanese-stablelm-instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b) - 📥 1k / ⭐ 26 / Japanese‑StableLM‑Instruct‑Beta‑70B 是一個 70 億參數的日本解碼僅 Llama2 為基礎的語言模型，經 Dolly‑15k、Anthropic HH 以及其他公共資料微調，亦提供 7 億參數的變體，並以 Llama2 Community License 釋出。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 1k / ⭐ 96 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 7 B 的日語優化版本，提供 instruct 與 fast 兩種變體，具有 6.27–6.37 B 個參數，可通過 Hugging‑Face Transformers 庫進行存取。
 * [stockmark-13b](https://huggingface.co/stockmark/stockmark-13b) - 📥 1k / ⭐ 39 / Stockmark‑13b 是一個 13B 參數的日語大型語言模型，訓練於大約 2200 億個 token，並配有一個指令微調版本，建置於 AWS Trainium，使用 neuronx‑nemo‑megatron，並以 MIT 授權由 Stockmark Inc. 發佈。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 1k / ⭐ 15 / LLM‑jp 提供 13B 與 1.3B 的 transformer 語言模型，包括多個 instruction‑tuned 變體，使用 Megatron‑DeepSpeed 與 Hugging Face Transformers 生態系統構建。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 1k / ⭐ 16 / 一套日本大型語言模型（1.8 b 至 172 b beta1，含 instruct 變體）來自 NII 研究發展中心，以 Hugging Face Transformers 格式打包，並在混合的日文、英文以及網路語料上預訓練，總 token 數量超過 1 trillion，需至少 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 470k / ⭐ 76 / Japanese BERT‑base 預訓練於 2019 年日本維基百科，使用 IPA 字典與整詞掩碼，12 層、768 維，32,000 詞表，512 令牌序列，1 百萬步；可於 cl‑tohoku/bert‑japanese 在 CC‑BY‑SA 條款下取得。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 234k / ⭐ 41 / 一個基於 BERT base 的模型，預訓練於約 17 M 日文 Wikipedia 句子（2.6 GB），採用 IPA dictionary 與 WordPiece 進行 tokenization，擁有 12 layers／768‑dim hidden states／12 heads，32 000‑token 詞彙表，於 Cloud TPUs 上訓練 1 M steps，並以 CC‑BY‑SA 3.0 發布。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 177k / ⭐ 9 / Japanese DeBERTa V2 大型模型已在 171 GB 的日語維基百科、CC‑100、與 OSCAR 上訓練，採用字符級 sentencepiece tokenization 與 whole‑word masking，已準備好通過 Hugging Face Transformers 進行下游微調。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 89k / ⭐ 8 / 一個 BERT‑base 日語模型（12 層，768‑維隱藏，12 頭），在約 1700 萬句來自日語維基百科（2.6 GB）的資料上進行預訓練，使用 MeCab IPA 單詞級分詞，隨後進行字符級分詞，建立一個 4000 單詞詞彙表。訓練程式碼位於 cl‑tohoku/bert‑japanese，並以 CC BY‑SA 3.0 釋出。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 44k / ⭐ 6 / 一個 BERT‑base 日語模型（12 層，768 維隱藏狀態，12 頭）在 30 M 句子（約 4 GB）上訓練，使用 Unidic 2.1.2 詞級分詞，隨後進行字級分詞和整詞遮蔽，使用 512 令牌序列、256 批次及 1 M 訓練步驟。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 28k / ⭐ 5 / ModernBERT‑Ja‑30M 是一款日語 BERT 變體，它將局部與全局注意力與 RoPE 混合起來，並在 4.39 TB 的日英文本上訓練，支援 8,192‑token 序列，參數規模從 30 M 至 130 M，並在使用 Flash Attention 2 時表現最佳。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 16k / ⭐ 48 / LINE DistilBERT Japanese 是一個 66‑million‑parameter 的 DistilBERT 模型，使用內部 BERT‑base 教師在 131 GB 的日本網路文本上進行預訓練，並於 JGLUE 上評估，採用 MeCab Unidic 與 SentencePiece 進行分詞，於 Apache 2.0 授權下釋出。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 13k / ⭐ 27 / Japanese BERT‑base (12 層, 768 hidden, 12 heads) 以 4 GB 的日本 Wikipedia（約 30 M 句）為預訓練資料，使用 Unidic 2.1.2 文字級別分詞、WordPiece 子分詞，與整詞掩碼。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 11k / ⭐ 39 / Japanese‑Roberta‑Base 是由 rinna Co., Ltd. 推出的預訓練遮罩語言模型，含正確載入、token 預處理、position‑id 處理的指引，以及強調需放置於首位的 `[CLS]` token 和一致 tokenization 的使用範例。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 6k / ⭐ 3 / 日文 RoBERTa‑base 模型，預訓練於約 10 M 篇日文醫學摘要與 1.4 M 篇來自 JST 的主體文本，使用 30 k‑token 的 SentencePiece 進行分詞，於 CC BY‑4.0 授權下釋出，可透過 Hugging Face pipelines 使用。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 6k / ⭐ 47 / 一個 132 百萬參數的 Japanese ModernBERT 模型，結合 local‑global 與 RoPE attention，在 4.39 T tokens（日語/英語）上訓練，含有 102‑k‑size 的 vocab，最大 token 長度 8,192，並優化為 Flash Attention 2。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 5k / ⭐ 30 / 日文 DeBERTa V2 基礎模型，已在 171 GB 日文維基百科、CC‑100 與 OSCAR 資料上使用 Juman++ 斷詞與 SentencePiece Tokenization 進行預訓練，訓練時間三週，使用八台 NVIDIA A100 GPU，已準備好進行微調。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 5k / ⭐ 2 / Japanese DeBERTa V2 tiny，預訓練於約 171 GB 的日語 Wikipedia、CC‑100 與 OSCAR 資料庫，需要 Juman++ 詞彙分割，已在 8 顆 NVIDIA A100 GPU 上訓練 33 小時，可進一步微調以應用於下游任務。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 5k / ⭐ 20 / ModernBERT‑Ja‑310M 是一款日語 BERT 變體，結合了 local‑global attention 與 RoPE，已在 4.09 T 個日語/英語文本 token 上訓練，支持 102 400 個詞彙、8 192 token 序列，並被優化以配合 Flash Attention 2。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 2k / ⭐ 4 / DeBERTaV2 基礎模型在日本語語料庫（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上進行訓練，並採用 FP‑16 微調以應對 NLU 任務（JSTS、JNLI、JCommonsenseQA）。本模型以 CC BY‑SA 4.0 授權發佈，並獲得日本研究撥款資助。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 一個 12 層、768 維的 BERT-Base 日語模型，使用 2.6 GB 的維基百科（≈17 M 句子）進行訓練，採用 IPA-dictionary 字元分詞與整詞遮罩（whole‑word masking），並以 CC‑BY‑SA 3.0 版權授權釋出。
 * [deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 📥 1k / ⭐ 9 / Japanese DeBERTa‑V2 大型模型，預先訓練於 171 GB 日本語文本（Wikipedia、CC‑100、OSCAR），採用 Juman++ 分詞，於 8 顆 A100 GPU 上訓練 36 天，可針對下游任務進行微調。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 52k / ⭐ 11 / Japanese Sentence‑BERT (v1) 模型，用於生成句子嵌入，並提供改進版 v2，並可透過 Hugging Face Transformers 與自訂的 `SentenceBertJapanese` 類別示範使用。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 48k / ⭐ 51 / 一個日本語的 Sentence‑BERT v2，經過在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上微調，並採用 MultipleNegativesRankingLoss，與 v1 相比提升了約 1.5–2 % 的準確率，並以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 形式釋出。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 44k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一個授權為 Apache‑2.0 的日語 CLIP 模型，基於 ViT‑B/16，訓練於翻譯成日語的 CC12M 標題，並於 2022 年 5 月 12 日發布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 22k / ⭐ 29 / LY Corporation 的 clip‑japanese‑base 是一個訓練於約 1 B 影像‑文字配對的日文 CLIP 模型，使用 Eva02‑B Transformer 影像編碼器並配備 12 層 BERT 文字編碼器，於 STAIR 的 R@1 成績為 0.30，於 Recruit 的準確度為 0.89，以及於 ImageNet‑1K 的準確度為 0.58，並支援零樣本影像分類與檢索。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 13k / ⭐ 22 / Sarashina‑Embedding‑v2‑1B 是一個 1,792 維的日語句子變換器，透過多階段對比學習訓練，達到先進的 JMTEB 分數，可用於語義相似度、搜尋、同義句挖掘、分類和聚類，透過 Sentence‑Transformers 並可加上可選的指令前綴。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 12k / ⭐ 2 / ja_ginza_electra 是一個 spaCy v3 Python 套件，提供已在 mC4 和 UD_Japanese_BCCWJ r2.8 上微調的日語 ELECTRA 模型（基於 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator），並具備自訂 bunsetu‑phrase detection，依照 MIT license 發佈。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 10k / ⭐ 14 / Japanese Sentence‑LUKE 模型在與 Sentence‑BERT 相同的資料集上進行訓練，表現優於或相當於 Sentence‑BERT，基於 studio‑ousia/luke‑japanese‑base‑lite 建立，並透過 Hugging Face Transformers 的 MLukeTokenizer 與 LukeModel 使用。
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 9k / ⭐ 4 / fastText 是一個輕量級、開源函式庫，可在標準 CPU 上快速學習文字與句子嵌入及分類器，能在數分鐘內以數十億字進行訓練，可被壓縮以供行動裝置使用，並提供分類與語言識別的預訓練向量。
 * [japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16) - 📥 7k / ⭐ 13 / Japanese CLOOB‑VIT-B-16，為基於 vit‑base‑patch16‑224 的 Vision‑Language 模型，已在翻譯後的 CC12M 說明書上進行訓練，並於 2022 年 5 月 12 日由 rinna Co., Ltd. 以 Apache 2.0 發布。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 5k / ⭐ 17 / Japanese CLIP 模型 clip‑japanese‑base‑v2，升級至約 2 B 影像‑文字配對並 distillation，將 Eva02‑B 影像編碼器與 12 層 BERT 文本編碼器結合，以達到比其前身更高的 ImageNet‑1k 準確度 (0.708)。
 * [japanese-avhubert-base_noise_pt](https://huggingface.co/enactic/japanese-avhubert-base_noise_pt) - 📥 4k / ⭐ 1 / 日本語 AVHuBERT AV‑SR 模型的倉庫，已在約 ~2,250 h 的視聽資料上預訓練，並進行大量噪聲增強，以實現強健的語音識別。
 * [japanese-avhubert-large_noise_pt](https://huggingface.co/enactic/japanese-avhubert-large_noise_pt) - 📥 2k / ⭐ 1 / 一個已預訓練的 2,250 小時 AVHuBERT Large 自監督式模型，使用噪音增強於日語音視覺數據上訓練，以強健地支持音視覺語音辨識。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 2k / ⭐ 55 / 一個日語 T5 模型，預訓練於約 100 GB 的 Wikipedia 與 OSCAR 數據，使用 SentencePiece 分詞，超越了 Google 的多語言 T5，在新聞分類基準上表現更佳，但仍需要微調，且可能產生偏見輸出。
 * [amber-large](https://huggingface.co/retrieva-jp/amber-large) - 📥 2k / ⭐ 7 / AMBER 是 Retrieva Inc. 的一個 3.15 億參數嵌入模型，擴充了 sbintuitions/modernbert‑ja‑310m 用於日語（可選英語支持），提供 768 維、以提示為驅動的嵌入，並以 Apache 2.0 許可發布。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 2k / ⭐ 3 / 一款在 JSNLI 上使用監督式 SimCSE 微調的日語 BERT‑base 模型，透過 Sentence‑Transformers 或 HuggingFace 以 CLS pooling 方式公開，訓練於 1 M 範例，batch size 512，學習率 5 × 10⁻⁵，溫度 5 × 10⁻⁵，64‑token 限制，以及 BFloat16 精度。

### sentence-similarity
 * [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) - 📥 633k / ⭐ 22 / 最終 JaColBERTv2.5 檢查點的權重，在新配方下僅使用 JaColBERTv2 數據的 40% 進行訓練，已超越所有先前模型——包括 JaColBERTV2 的多語言變體，例如 BGE‑M3——在所有資料集上的表現。
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 448k / ⭐ 67 / Ruri v3 是一個尖端的日本語文本嵌入模型，建立於 ModernBERT‑Ja，支援最多 8,192‑token 輸入、100K‑token 詞彙表、FlashAttention‑加速推論，以及多種尺寸變體，方便快速使用 sentence‑transformer。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 395k / ⭐ 11 / 日文通用文本嵌入模型 (Ruri‑v3, 30‑310 M 參數, 8192‑token 上限, 高 JMTEB 分數) 以 Sentence‑Transformers 使用範例提供，並與其他日文嵌入進行基準比較。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 179k / ⭐ 8 / Ruri v3 是一款最先進的日文文本嵌入模型，構建於 ModernBERT‑Ja，支持高達 8,192 tokens、一個 100k‑token 詞彙表、FlashAttention 加速，並提供從 37 M 到 315 M 參數的多種規模。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 129k / ⭐ 9 / 包含 Ruri v3 日文文字嵌入（30 M–310 M 參數、8192‑token 限制、JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前綴的 Sentence Transformers 指令，以及幾個日文模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基準結果。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 32k / ⭐ 44 / PLaMo‑Embedding‑1B 是 Preferred Networks 開發的日本文本嵌入模型，能將日文文本轉換為向量，用於資訊檢索、分類與聚類，在 JMTEB 基準測試上表現優異，且以 Apache v2.0 license 免費提供。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 30k / ⭐ 34 / GLuCoSE 是一個基於 LUKE 的日語句子嵌入模型，輸出 768 維均值池化向量（最多 512 個 tokens），在網路及 NLI/搜尋資料上訓練，於相似度基準上達成 0.864 Spearman 與 0.818 Pearson。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 28k / ⭐ 4 / Ruri v3 是一款最先進的日本語文本嵌入模型，基於 ModernBERT‑Ja 建構，支援長達 8192‑token 序列、10 萬詞彙、FlashAttention，並以 30 M 到 310 M 參數大小提供，以供 sentence‑transformers 使用。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 28k / ⭐ 16 / JaColBERTv2 是一個僅限日文的 ColBERT 基於檢索模型，使用 MMarco（31 個負樣本對每個正樣本、250k 步驟、批次 32）進行知識蒸餾訓練，目前表現優於 multilingual‑e5‑large、BGE‑M3 以及 JaColBERT，完整評估仍待進行。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 21k / ⭐ 22 / GLuCoSE v2 是一款適合 CPU 的日語文本嵌入模型，透過蒸餾與多階段對比學習進行微調，提供優越的語義相似度與檢索性能—在 MIRACL 以及相關基準上超越同等規模模型。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 21k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一個 768 維的句子轉換器，建立於 studio‑ousia/luke‑japanese‑base‑lite 上，已在 shunk031/jsnli 培訓一個 epoch，並包含聚類、語意搜尋以及同時適用於 Sentence‑Transformers 與 HuggingFace 的範例。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 11k / ⭐ 44 / 一組可釋出的 Ruri v3 日文文本嵌入模型（30m–310m），包含 SentenceTransformer 使用技巧、查詢/段落前綴，以及 JMTEB 基準測試結果，展示它們與其他日文及多語言嵌入模型的比較。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 10k / ⭐ 2 / Ruri v3 提供高性能的日語文本嵌入，最多可達 8192 個 token，擁有 100k token 詞彙表，支援 FlashAttention，並提供多種模型尺寸 (30 m–310 m) 以供透過 sentence‑transformers 進行高效推理與微調。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 3M / ⭐ 53 / 日語 wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 與 JSUT 上微調，需要 16 kHz 音訊，並可透過 HuggingSound 或 HuggingFace pipelines 使用。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 18k / ⭐ 89 / Kotoba‑Whisper v2.0 是一款從 OpenAI Whisper large‑v3 提煉的日語ASR模型，使用 7.2 million ReazonSpeech 片段訓練，速度比原版快 6.3×，同時在領域測試中匹配教師模型的 CER/WER，並包含 stable‑ts/punctuation 支援及完整訓練程式碼於 GitHub。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 15k / ⭐ 96 / Kotoba‑Whisper‑v2.2 是一款日語 ASR 模型，擴展了 kotoba‑whisper‑v2.0，整合了 integrated diarization 與 automatic punctuation，透過 HuggingFace‑Transformers pipeline 實現，並與 Asahi Ushio 和 Kotoba Technologies 合作開發。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 9k / ⭐ 128 / Anime Whisper 是一個輕量級的日語 ASR 模型，已在約 5,300 小時的動漫式對白上微調，提供低幻覺、節奏對齊的標點符號，並能準確轉錄非語音聲音和 NSFW 內容，必須在沒有初始提示的情況下運行。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 8k / ⭐ 46 / NVIDIA NeMo 的 0.6 B‑參數 Hybrid FastConformer‑TDT‑CTC ASR 模型能帶標點符號轉錄日語語音，並且可在 NeMo 框架內進行推論或微調。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 8k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供 6.3 倍更快的蒸餾 Whisper 模型，支援日本語與英語的 ASR 以及雙向語音轉文字翻譯，這些模型由 OpenAI 的 Whisper large‑v3 透過 knowledge distillation 與 cross‑entropy 及 KL‑divergence loss 建構。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 3k / ⭐ 19 / Kotoba‑Whisper‑v2.1 是一款日語 ASR 模型，繼承了 kotoba‑whisper‑v2.0，並整合了標點符號後處理流程，能保持相當的 CER 性能，同時實現無縫、能感知標點符號的轉錄。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 2k / ⭐ 37 / reazonspeech-nemo-v2 是一款擁有 619‑M參數的日語長文語音識別模型，基於改進版 Fast‑Conformer 與 Linearly Scalable Attention 架構構建，訓練於 ReazonSpeech v2.0 資料集，透過 subword RNN‑T decoder（3000‑token SentencePiece）提供多小時推理，並以 Apache 2.0 授權方式分發。
 * [moonshine-tiny-ja](https://huggingface.co/UsefulSensors/moonshine-tiny-ja) - 📥 2k / ⭐ 11 / 小型、edge‑ready 的 ASR 模型由 Moonshine AI 開發，能即時轉錄日語語音，並在低資源 deployment 的 model card 中詳細說明。
 * [kotoba-whisper-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0) - 📥 2k / ⭐ 58 / Kotoba‑Whisper v1.0，為從 OpenAI 的 Whisper large‑v3 擠壓而成的日語 ASR 模型，提供 6.3 倍速度提升且準確度相當，可在 1,253 小時的 ReazonSpeech 上訓練，其程式碼（以及在 Hugging Face 上更新的 v2.0 版本）已公開可用。

### text-ranking
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 46k / ⭐ 7 / 日本 CrossEncoder 重排序模型 覆蓋 xsmall 到 large（含 BGE），已於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 進行評估，並附上可直接使用的 sentence_transformers 與 HuggingFace 整合範例。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 19k / ⭐ 6 / 快速、輕量級的日語 Reranker v2 模型（tiny、xsmall、small、base）具有基準分數和 GPU 速度，可通過 sentence_transformers CrossEncoder 和 transformers ≥ v4.48 （可選使用 flash‑attn 加速）使用，並且亦提供 ONNX/量化版本以供 CPU/ARM 使用。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 8k / ⭐ 13 / Ruri‑v3 Reranker 是一款以 ModernBERT‑Ja 為基礎的強大日語文本重排序器，支援多達 8,192 令牌序列、100k 令牌詞彙表、FlashAttention 以及 SentencePiece tokenizer，並可透過 sentence‑transformers 使用。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 3k / ⭐ 2 / Japanese‑reranker‑small‑v2 是一款輕量、快速的日語重排序模型系列（v2），提供從 tiny 到 base 的各種變體，最高可達平均 0.89 分，且 GPU 推論時間為 2–15 秒，亦包含 cross‑encoder 選項，並要求 Hugging Face Transformers v4.48+；可選擇 Flash Attention 2 以加速。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 3k / ⭐ 2 / 一個基於 Sentence Transformers 的 CrossEncoder 所構建的日語句子重排序器，提供推理代碼、基準測試結果以及多種模型尺寸，用於排序日語文本。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 2k / ⭐ 15 / 一套日本 CrossEncoder 重複器（reranker）套件——包括 xsmall、small、base、large 以及 japanese‑bge‑reranker‑v2‑m3‑v1——搭配示例使用、在多個基準上的評估指標與輔助文件。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 2k / ⭐ 16 / 由 xsmall 到 large 的日文 CrossEncoder 排序模型，使用日語文本訓練，透過 sentence_transformers 提供，並於 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上進行評估。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 1k / ⭐ 4 / 以日語訓練的 CrossEncoder 重新排序模型，規模從 xsmall（384）到 large（1024），並包含 BGE‑v2‑m3‑v1 模型，附有微調、推理的範例程式碼，以及在 JQaRA、JaCWIR、MIRACL 與 JSQuAD 上的基準分數。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 1k / ⭐ 12 / 一個使用 Sentence Transformers 構建的日本交叉編碼器重排序器，展示了對各種尺寸的 Ruri‑Reranker 模型的推理使用和基準結果。

### text-classification
 * [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) - 📥 777k / ⭐ 3 / Finance Sentiment JA (base) 是一個基於 BERT 的日語情緒模型，訓練於翻譯後的 Financial PhraseBank，能將日本財經新聞分類為正面、負面或中性，macro f1 為 0.959、accuracy 0.967、每秒 134.9 samples per second。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 238k / ⭐ 15 / 在 Amazon 商品評論上微調日本 BERT（cl‑tohoku/bert‑base‑japanese‑v2）以進行情感分類，達到約 81% 的準確率與 0.73 的 F1 分數，在 6 個 epoch 之後，學習率為 2 × 10⁻⁵。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 11k / ⭐ 15 / 在 chABSA 數據集上訓練的日文情感分析模型，達到 loss 0.0001、accuracy 1.0、以及 F1 1.0。使用 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 構建，使用 Adam 進行優化（learning rate 2e‑05，10 epochs，batch size 16），並通過 `model(**inputs)` 評估。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 4k / ⭐ 2 / 在《Large Language Model Introduction》第5章中介紹的日本 BERT‑based 模型，已於 JGLUE JSTS 資料集上進行微調，用於語義相似度評分。此模型包含 Colab notebooks、transformers‑pipeline 使用說明，以及 Apache 2.0 授權。
 * [luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 📥 3k / ⭐ 43 / 一個日語版本的 LUKE 模型，在 WRIME 數據集上微調，能夠分類一句話中表達的八種情緒——快樂、悲傷、期待、驚訝、憤怒、恐懼、厭惡、信任。
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 1k / ⭐ 6 / 一個針對 WRIME 數據集微調的日本 BERT BASE 模型，為作者和讀者預測八種情感（喜悅、悲傷、期待、驚訝、憤怒、恐懼、厭惡、信任）的 0‑4 強度分數；代碼可用，訓練耗時 3 小時於 K80 上，對作者達到約 0.6 MSE，對讀者達到約 0.2 MSE。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 338k / ⭐ 12 / 一個以新 VNTL 數據集為基礎的 LLaMA 3 Youko qlora 微調模型，優化為準確、逐字的日語視覺小說到英文翻譯，不使用聊天模式，使用預設的 LLaMA 3 提示，並建議採用中性取樣（temperature 0，無重複懲罰）。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 54k / ⭐ 73 / 來自 Opus corpus 的日文-英語 Transformer‑Align MT 模型，使用 normalization 與 SentencePiece 先行處理，在 Tatoeba 測試集上達到 41.7 BLEU 與 0.589 chr‑F。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 47k / ⭐ 28 / 微調、GGUF‑量化後的 LFM2‑350M checkpoint，適用於近即時雙向日英短至中篇文本翻譯，可透過 llama.cpp 使用。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 12k / ⭐ 118 / PLaMo Translation Model 是 Preferred Networks 為翻譯任務所創建的大規模語言模型，可供 base、post‑trained 以及 evaluation 版本使用，並以 PLaMo community license 釋出，未對聊天或其他下游用途進行 instruction‑tuned。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 2k / ⭐ 8 / Sugoi LLM 14B Ultra (GGUF) 是一個日語轉英語的翻譯模型，BLEU 分數為 21.38——幾乎是其先前分數 13.67 的兩倍——在 RPG‑Maker 方括號文本上擅長，提示遵從性強，並為交互式聊天 UI 生成 JSON 輸出。

### token-classification
 * [MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - 📥 57k / ⭐ 12 / 日文醫學文件 NER 模型（下載這五個檔案，執行 **predict.py** – 輸出疾病、藥物、日期等標籤）用於 NAISTSOC 2022 NTCIR‑16 Real‑MedNLP 任務。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 17k / ⭐ 10 / Fine‑tuned Japanese BERT‑Base 用於在維基百科資料集上的命名實體識別，已在《Large Language Model Introduction》一書第六章展示，可透過 Hugging Face transformers pipeline 部署（Apache 2.0 授權）。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 15k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日語 NER，可提取八種實體類型（公司、政治/其他組織、設施、產品、事件），透過 `BertForTokenClassification`，在 Stockmark Wikipedia 數據集上訓練，並可透過 `transformers`、`unidic_lite`、`fugashi` 安裝，採用 CC BY‑SA 3.0 許可證。
 * [bert-base-japanese-v3-crf-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset) - 📥 2k / ⭐ 2 / CRF‑增強的 BERT‑base‑japanese‑v3，針對日本 NER 在 Wikipedia 數據上微調，正如《Large‑Language‑Model Intro》一書所示（Apache 2.0 授權）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 使用 5 週期 Adam (lr 5e‑5, batch 12) 微調 XLM‑RoBERTa‑base，針對日語 NER 資料集（tags PER, ORG, LOC, INS, PRD, EVT）以達成 0.0173 的驗證損失，已於 Transformers 4.23.1 與 PyTorch 1.12.1 發佈。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 312k / ⭐ 169 / Manga OCR 是一個 Vision Encoder‑Decoder OCR 工具，能閱讀垂直與水平的日語漫畫文字（包含振假名），適用於多種字體與低品質圖像，且源碼免費提供。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 111k / ⭐ 5 / Meikiocr的 `meiki.text.recognition.v0`——一個基於 D‑FINE 的 MobileNetV4 模型，在日語視訊遊戲文字上微調——為水平文字提供最先進的準確性和延遲，能從 960×32 的輸入中偵測多達 48 個字符，並輸出每個字符的外框與置信度分數。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 102k / ⭐ 3 / meikiocr 提供一款基於 D‑FINE 的開源權重文字偵測模型，適用於遊戲視訊（v0.1 版，採用 MobileNet‑v4 主幹，提供兩種解析度變體與 64 框限制），以及實驗性低延遲 tiny 與 small 變體，已在日本遊戲及漫畫上訓練。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 1k / ⭐ 16 / Sarashina2.2‑Vision‑3B 是一個 3‑B 參數的日本大型視覺－語言模型，建立於 Sarashina2.2‑3B‑Instruct 和 SigLIP 圖像編碼器之上，並在日本 VQA 基準上達到強勁表現。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 2k / ⭐ 121 / PaddleOCR‑VL‑For‑Manga 由 PaddleOCR‑VL 微調，於 Manga109 的對話框裁切圖像上達成 70％完整句子準確率——高於 27％基準的三倍以上——使用多語系資料集，並提供訓練程式碼與開發人員指南。
 * [Heron-NVILA-Lite-15B](https://huggingface.co/turing-motors/Heron-NVILA-Lite-15B) - 📥 1k / ⭐ 14 / Heron‑NVILA‑Lite‑15B‑hf 是一種以日本為中心的視覺‑語言模型，基於 NVILA‑Lite 架構構建，具備 PALIGEMMA‑SIGLIP 視覺編碼器、一個 MLP‑downsample 投影器，以及 Qwen2.5‑14B‑Instruct LLM，支援日語和英語，並可直接與 Hugging Face 進行整合。

### text-to-speech
 * [Anime-Llasa-3B](https://huggingface.co/NandemoGHS/Anime-Llasa-3B) - 📥 1k / ⭐ 26 / Anime‑Llasa‑3B 是一款建立於 HKUSTAudio/Llasa‑3B 上的日語 TTS 模型，透過更多訓練資料進行增強，以提升其表達力與穩定性，並授權為 CC‑BY‑NC‑4.0。
 * [japanese-parler-tts-mini](https://huggingface.co/2121-8/japanese-parler-tts-mini) - 📥 1k / ⭐ 26 / Japanese Parler‑TTS Mini 是一個輕量級、高品質的日語 TTS 模型，從 parler‑tts‑mini‑v1 微調而成，提供高效的語音生成。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 2k / ⭐ 14 / Anime‑XCodec2‑44.1kHz‑v2 將 16 kHz 的日語語音升頻至 44.1 kHz 高保真音訊，並使用僅解碼器的 RMS‑loss 微調，保持編碼器/代碼簿凍結並保留相同的語音標記。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 90k / ⭐ 11 / Japanese‑language BERT‑Base（12層，768‑次元，12頭）以 Unidic 為基礎的單詞層級加字符層級標記化以及整詞遮蔽，在 CC‑100 和 2023 Wikipedia 上進行預訓練，產生了 7,027‑token 詞彙。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 81k / ⭐ 61 / Japanese BERT‑base (12 層, 768‑維度隱藏, 12 頭, 32k 詞彙) 以完整詞遮蔽在 CC‑100 與 2023‑Jan Wikipedia 上預訓練，使用 Unidic 2.1.2 詞級分詞加 WordPiece，訓練 200 萬步。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 67k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上訓練，使用 Unidic‑lite 詞級分詞，結合 WordPiece 子詞與全詞遮蔽，模型為 24 層、1024 維隱藏、16 頭、32k 詞表；預訓練程式碼位於 cl‑tohoku/bert‑japanese。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / 一個以約 100 GB 的 Wikipedia 與 OSCAR CC‑100 數據（混合 10:1、Byte‑fallback 的 SentencePiece）預訓練的日本 T5‑v1.1 模型，需對下游任務進行微調，包含遷移學習範例程式碼，提示輸出可能存在偏差，且採用 CC‑BY‑SA 4.0 授權。
 * [GPT-OSS-Swallow-20B-SFT-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-SFT-v0.1-gguf) - 📥 12k / ⭐ 1 / GPT‑OSS‑Swallow‑20B‑SFT‑v0.1‑gguf 是一個經 gguf 轉換的 tokyotech‑llm GPT‑OSS‑Swallow 20B SFT 模型版本，訓練於 TFMC/imatrix‑dataset‑for‑japanese‑LLM，並為 CUDA‑enabled llama.cpp 構建，已可透過 llama‑cli 執行（例如：專業廚師食譜提示）。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 9k / ⭐ 1 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一款頂級、以日文為焦點的 GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，具備廣泛的日文校準和社區修正的缺陷，即使沒有 GPU 也能在 llama.cpp 上運行，最低需要 8 GB RAM 及 3 GB 磁碟空間。
 * [GPT-OSS-Swallow-20B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-RL-v0.1-gguf) - 📥 9k / ⭐ 4 / 一個 gguf‑format 轉換的 GPT‑OSS‑Swallow 20B RL v0.1 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 數據構建，已準備好透過 llama.cpp 以 CUDA 支持執行。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 6k / ⭐ 4 / 一個為日語微調的 Qwen 3.5‑9B GGUF 模型，採用 Unsloth Dynamic Quantization 2.0，進行了廣泛的錯誤修復、大規模日語校準，並可在 CPU 上運行，需 16 GB RAM 及 6 GB 磁碟空間，透過 llama.cpp。
 * [Qwen3.5-0.8B-JP-gguf](https://huggingface.co/tatsuyaaaaaaa/Qwen3.5-0.8B-JP-gguf) - 📥 5k / ⭐ 1 / 一個從 Holy‑fox 轉成 gguf 的 Qwen3.5‑0.8B‑JP，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 數據集進行量化。
 * [GPT-OSS-Swallow-120B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-120B-RL-v0.1-gguf) - 📥 5k / ⭐ 5 / gguf-format 轉換 120 B GPT‑OSS‑Swallow RL 模型，使用 TFMC/imatrix 日語資料集構建，並附有編譯帶 CUDA 支援的 llama.cpp 及透過 llama‑cli 執行模型的說明。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 3k / ⭐ 17 / 日文 DeBERTa V3 基礎版本，預訓練於 LLM‑jp v1.0 的 540 B 個 token，使用已調整的 DeBERTa V3 設定，採用 unigram byte‑fallback tokenizer（無形態學分析器），並進行 fine‑tuned 於 JGLUE NLU 任務。
 * [Qwen3-8B-JP-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/Qwen3-8B-JP-Uncensored-i1-GGUF) - 📥 3k / ⭐ 1 / 提供一系列加權與 imatrix GGUF 量化版本，適用於 Qwen3‑8B‑JP‑Uncensored 模型，從 2.2 GB 的 IQ1 變體到 6.8 GB 的 IQ6，並附有使用說明、static‑quant links 與支援資源。
 * [GPT-OSS-Swallow-20B-RL-v0.1-MXFP4](https://huggingface.co/dahara1/GPT-OSS-Swallow-20B-RL-v0.1-MXFP4) - 📥 3k / ⭐ 2 / GPT‑OSS‑Swallow‑20B‑RL‑v0.1‑MXFP4 是一個免費且不需要 GPU 的 GPT‑4o‑mini‑level AI，以 gguf file 方式發布，已優化為日語版本，並結合社群發現的 bug 修復、基於基準測試的設定，且僅使用預設 MXFP4 format（不包含 dynamic quantization 或 large imatrix）。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 3k / ⭐ 72 / Llama‑3‑ELYZA‑JP‑8B 是一款日本優化的 8‑B Llama 3 模型，採用 GGUF (Q4_K_M) 與 AWQ 量化，能以 llama.cpp、LM Studio 或 OpenAI‑相容 API 執行。
 * [SIP-jmed-llm-3-13b-OP-4k-base](https://huggingface.co/SIP-med-LLM/SIP-jmed-llm-3-13b-OP-4k-base) - 📥 3k / ⭐ 1 / SIP‑jmed‑llm‑3‑13b‑OP‑4k‑base 是一個 Apache‑2.0 授權、域適應的日英醫療大語言模型，基於 llm‑jp‑3.1‑13b 建立，由 SIP’s third‑term program for medical knowledge 研發的研究原型，但並非臨床使用。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一個擁有 80 億參數的 LLM，透過持續預訓練以及在合成日語數據上進行指令調整微調，提升了 Meta 的 Llama 3.1 在日語語言以及程式碼／數學推理方面的表現，同時保持英語流暢度。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 2k / ⭐ 22 / 一個 GGUF‑格式的 pfnet 的 plamo‑2‑translate 發行版，基於 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 數據構建，並附有使用 llama.cpp 在支援 CUDA 的硬體上編譯與執行的說明。
 * [Holy-fox-Qwen3.5-0.8B-JP-gguf](https://huggingface.co/mmnga-o/Holy-fox-Qwen3.5-0.8B-JP-gguf) - 📥 2k / ⭐ 1 / 提供 Holy‑fox 的 Qwen3.5‑0.8B‑JP 模型（由 TFMC/imatrix‑dataset-for-japanese‑LLM 建構）之 GGUF 格式轉換，並附帶編譯與執行 llama.cpp（含 CUDA 支援）的說明。
 * [gemma-2-2b-it-gguf](https://huggingface.co/mmnga/gemma-2-2b-it-gguf) - 📥 2k / ⭐ 1 / 使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix data 進行 Google 的 gemma‑2‑2b‑it 模型的 GGUF‑formatted conversion，附帶 llama.cpp usage instructions。
 * [Qwen3.5-REAP-212B-A17B-gguf](https://huggingface.co/mmnga-o/Qwen3.5-REAP-212B-A17B-gguf) - 📥 2k / ⭐ 5 / GGUF 轉換的 OpenMOSE Qwen3.5‑REAP‑212B‑A17B，從 TFMC/imatrix 日本 LLM 資料集重新建構，並已準備好透過 llama.cpp 的標準 CLI 進行啟用 CUDA 的推理。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 2k / ⭐ 17 / 高效能日文 SPLADE v2 透過 WebUI demo 可進行稀疏向量轉換與推理，使用 YAST 訓練，提供 YASEM 嵌入，並報告 JMTEB 基準結果。
 * [Qwen3-Swallow-8B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-8B-SFT-v0.2-gguf) - 📥 1k / ⭐ 1 / 一個已轉換為 gguf 的 Qwen3‑Swallow‑8B‑SFT‑v0.2 模型，用於日語 LLM，使用 imatrix 數據構建，並附帶 llama.cpp 推理指令。
 * [llm-jp-moshi-v1](https://huggingface.co/llm-jp/llm-jp-moshi-v1) - 📥 1k / ⭐ 35 / LLM‑jp‑Moshi‑v1 是一個基於 7‑B‑parameter Moshi 架構的實驗性日語全雙工語音聊天模型，經 J‑CHAT 和 Zoom 對話資料微調，並以 Apache 2.0 許可證釋出，附帶適用於 Linux GPU 系統的 web‑UI 示範。
 * [Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf) - 📥 1k / ⭐ 2 / GGUF格式的 Qwen3‑Swallow‑30B‑A3B‑SFT‑v0.2 模型版本，由 tokyotech‑llm 發佈，並使用 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 數據構建，已準備好供 llama.cpp CUDA 使用。
 * [SIP-jmed-llm-3-8x13b-OP-32k-R0.1-GGUF](https://huggingface.co/hiratagoh/SIP-jmed-llm-3-8x13b-OP-32k-R0.1-GGUF) - 📥 1k / ⭐ 3 / 一個經 GGUF 轉換、量化、僅供研究使用版本的日本 SIP‑jmed‑llm‑3‑8x13b‑OP‑32k‑R0.1 主權醫療推論模型，於日本 SIP 計畫之下開發，致力於安全、開放醫療 LLM，適用於研究與示範用途（例如在 Ollama + Dify 上），但不適合臨床決策。
 * [RakutenAI-3.0-gguf](https://huggingface.co/mmnga-o/RakutenAI-3.0-gguf) - 📥 1k / ⭐ 5 / GGUF 轉換版本的 RakutenAI-3.0，使用 imatrix dataset 構建，已準備好與 llama.cpp 配合使用，以運行日語 LLMs.
 * [cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf](https://huggingface.co/mmnga/cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf) - 📥 1k / ⭐ 55 / Cyberagent 的 gguf‑converted DeepSeek‑R1‑Distill‑Qwen‑14B‑Japanese 模型（基於 TFMC imatrix 數據集構建）已在 mmnga 可用，並且可使用 llama.cpp 在帶 CUDA 支持的環境中運行。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 1k / ⭐ 3 / 一個 T5 v1.1 模型，預訓練於日本 Wikipedia 以及 mC4/ja，採用 GEGLU 激活；預訓練期間不使用 dropout；不共享 embedding‑classifier；在 CC‑BY‑SA 4.0 協議下發佈（商業使用須事先聯繫）。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 1k / ⭐ 2 / DataPilot-ArrowPro-7B-RobinHood‑gguf 是 DataPilot 的 ArrowPro‑7B‑RobinHood 模型使用 imatrix 日本 LLM 數據集進行 gguf 格式轉換，已準備好與 llama.cpp 一起執行推理。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 12 / Sarashina2.2 提供 0.5‑B、1‑B、和 3‑B 的語言模型，這些模型由 SB Intuitions 透過三階段流程及合成資料進行訓練，達成優異的日文 QA、數學及編碼分數，同時提供未經指令微調的預訓練權重，可能產生有偏差的輸出。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 3M / ⭐ 23 / 聚合自 2009‑2024 年的 NicoNico Live 評論日誌超過 150 GB，包括轉換前、轉換後及實時 NX‑Jikkyo 捕獲，並提供 API 以方便檢索歷史 TV‑broadcast 討論。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 158k / ⭐ 7 / 由 VOICEVOX 與 ITA、Tsukuyomi‑chan、ROHAN 資料庫所建立的人工語音資料集，包含 445,793 個 WAV 檔案，總計 577 小時 51 分鐘 23 秒。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 17k / ⭐ 16 / 日語及多語系 QA、NLI 與同義句資料集的目錄，說明各資料集的檢索或 QA 任務以及其授權規範（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 11k / ⭐ 9 / Cauldron‑JA 是一套日本視覺‑語言資料集，包含 44 個子資料集，這些子資料集是使用 DeepL API 將 The Cauldron 翻譯而成，通過 HuggingFace’s datasets library 可取得，授權條件與原始資料集完全相同，提示（prompts）則以 CC‑BY‑4.0 授權釋出。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 9k / ⭐ 109 / Nemotron‑Personas‑Japan是一個開源、CC BY 4.0資料集，提供高品質的合成生成日本人格資料——包含姓名、性別、年齡、背景、婚姻狀況、教育、職業和地理位置——基於真實世界的人口、地理和個性分佈設計，使用概率圖形模型和GPT‑OSS‑120B進行優化，以提升多樣性、減少偏見、避免模型崩潰，協助主權AI發展並支持商業使用。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 5k / ⭐ 28 / FineWeb2 Edu Japanese 交付約 120 million 高品質教育用日語文本（≈89.3 billion tokens）來自 FineWeb2，經 DeepSeek‑API classifier（score ≥ 2.5）過濾，使用 ModernBERT‑Ja‑130M 分詞，並包含小型 token 子集（≤512 tokens）。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 5k / ⭐ 4 / Japanese Medical VQA 12M 是一個可商業使用的多模態資料集，包含超過1200萬張日文醫學影像及說明文字，來源自 Open‑PMC‑18M，採用 Parquet/Webdataset 格式，並包含原始及日文翻譯的影像、豐富的說明文字，以及使用 InternVL3.5、Qwen3‑30B 與 GPT‑oss 120B 產生的 VQA‑風格問答對。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 3k / ⭐ 110 / ReazonSpeech 是一個免費的 FLAC‑encoded 日語語音語料庫，附帶文字稿，提供五種規模，從 8.5 小時到 35,000 小時，可透過 Hugging Face 下載，採用 CDLA‑Sharing‑1.0 授權，並受限於日本版權法第 30‑4 條使用。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 3k / ⭐ 39 / 使用者友善、去重的 CSV 資料集，包含來自 Aozora Bunko 的公有領域日語文本，已使用 globis‑org/aozorabunko‑extractor 處理並為現代日語機器學習用途做過清理。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 3k / ⭐ 16 / Reazon Speech v2 數據集的鏡像：3,674 個去噪語音檔經 UVR 於 8 台 A800 GPU 上處理，耗時 10 天，由 Stardust‑minus 完成，並以 CDLA‑Sharing‑1.0 釋出且未附文字稿。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 3k / ⭐ 99 / 一個包含 100 筆樣本的日本語 instruction‑tuning 評估資料集，內含標註任務——從摘要校正、數學推理到翻譯、創意生成及使用者意圖理解——設計用於手動或自動 5‑point rating 的 fine‑tuned models 評估。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 2k / ⭐ 5 / JAQKET 是一個來自 Wikipedia 的日語開放域問答資料集，提供版本 1.0，包含多選測驗題（13,061 個訓練例子，271 個驗證例子）以及版本 2.0，只包含需要抽取答案的提問提示（2,154 個訓練例子，1,164 個驗證例子），旨在促進問答系統研究。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 2k / ⭐ 36 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小時的匿名化 1,033,142 對 eroge 音訊–轉錄配對 (大多為女性，NSFW)，MIT授權，用於學術研究。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 2k / ⭐ 4 / JamC‑QA 是一個涵蓋八個日本文化與知識類別的雙語多選題基準測試，並以排行榜指標對比最先進模型。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 2k / ⭐ 19 / JMMMU 是一個日語多模態基準，已擴充十倍至 1,320 個文化多樣化問題 (720 個文化中立，600 個文化特定)，由母語專家翻譯，現在擁有公開排行榜。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEB 是一套日語文本嵌入基準，包含 5 個任務（聚類、分類、STS、檢索、重排序）與 28 個資料集，提供一行式評估腳本並邀請社群貢獻。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 2k / ⭐ 47 / 更新了 JGLUE 數據集卡和載入腳本，適用於由 Yahoo Japan 和 Waseda University 創建的日本 NLP 基準，涵蓋文本分類（MARC‑ja、JCoLA）、句子對分類（JNLI）和 QA（JSQuAD、JCommonsenseQA），發布版本已在 GitHub 和 Hugging Face 上連結。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 1k / ⭐ 89 / 一個自動翻譯的日語版 databricks‑dolly‑15k dataset，採用 CC‑BY‑SA‑3.0 授權，最後更新於 2023‑05‑11。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 1k / ⭐ 4 / 提供一個日文搜尋/問答資料集，包含每個查詢的分數，這些分數由五個多語言／日文再排序器計算（如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base），並包括每個查詢大約 200 篇正面與負面範例文件的平均分數。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 1k / ⭐ 6 / Japanese XL‑Sum 子集經 PaLM‑2 15‑gram 重疊過濾，包含 4,215 個訓練、758 個驗證以及 766 個測試範例。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 978 / ⭐ 23 / cc100-ja 是 cc100 資料集的日本語部分，提供為分片 Parquet 檔案。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 919 / ⭐ 7 / JMedBench 是一個日本醫學領域 LLM 基準，包含 20 個資料集，涵蓋五個任務（MCQA、NER、STS 等），資料來源於 MedMCQA、PubMedQA、MMLU 及其他，每個資料集都有自己的授權，並附有註記指出翻譯可能存在偏差，需人工審核。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 918 / ⭐ 133 / Japanese Anime Speech Dataset V2 提供 292,637 對乾淨的音頻-文本對，約 397.5 小時為 SFW，52.4 小時為 NSFW，存於 128‑kbps MP3 檔案中按安全性分割，專為訓練自動語音識別模型而設。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 827 / ⭐ 2 / LLM 生成的查詢與答案資料集，採自日本維基百科文字的改寫，未使用授權受限模型構建，並以 CC‑BY‑SA 4.0 版本發布。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 798 / ⭐ 2 / 大型壓縮的 JSON‑Lines 數據集，包含匿名 2ch.sc/2ch.net 論壇討論串，包含討論串 ID、標題、版面與區域資訊、回覆數量，以及完整的貼文元資料（作者、郵件、日期、內容）。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 787 / ⭐ 32 / 一個 409 小時的日本 eroge 語音資料集，經 2-pass loudnorm 處理（‑23 LUFS、‑1 dB peak、11 LRA），由 litagin/anime-whisper 轉錄，已匿名化，存儲為 WebDataset（FLAC、JSON、TXT），主要包含女性聲音，可能存在 AI 轉錄錯誤，並以 MIT‑licensed 供學術研究。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 731 / ⭐ 11 / JMMLU 是一個日本大型多任務語言理解基準，包含 7,536 個由教師精心編寫的問題，涵蓋 56 個科目，包含專業醫學、心理學、會計、哲學，以及多種高中學科。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 706 / ⭐ 148 / Japanese Anime Speech Dataset 提供 73,004 對音頻-文字對（共 110 小時，從 V1 演進至 V5），用於提升 ASR 模型（如 OpenAI 的 Whisper），在開放授權下可供任何使用，若能標明來源將不勝感激。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 690 / ⭐ 4 / 來自 Fate/Stay Night 角色「Emilia」的對話與傳說資料集，格式化用於訓練與評估對話語言模型。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 681 / ⭐ 8 / Rakuda 提供 40 個日文問題—針對歷史、社會與政府的開放式題目，以及針對地理的專門題目—作為基準測試日本 AI 助手的資料，與 vicuna‑eval 相似，並可透過 `datasets.load_dataset` 載入。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 665 / ⭐ 32 / 重構後重新上傳 Galgame VisualNovel 資料集 (OOPPEENN/5669736E6F76656C5F44617461736574)，為了提高 Hugging Face 資料集載入效率，保留所有原始音訊 / 文字，並提供一段提取腳本，支援多種遊戲子集選項。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 592 / ⭐ 12 / EDINET‑Bench 是一個日本金融基準，評估 LLM 在會計欺詐檢測、盈餘預測以及產業預測等任務，使用十年的 EDINET‑API 公開報告。提供構建與評估代碼，資料集已重新授權為 PDL 1.0。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 563 / ⭐ 33 / Syosetu711K 是一個日本資料集，於 2023 年 3 月 26‑27 日從小説家になろう抓取約 711,700 本小說，提供全文和元資料（標題、作者、NCode、簡介等）供無監督文本生成和分類任務使用。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 553 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 資料集的一個 500 個樣本子集，授權為 CC BY 4.0，用於基準測試 EvoVLM‑JP‑v1‑7B。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 549 / ⭐ 6 / 日文 MC4 資料集卡片 (mc4-ja)
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 545 / ⭐ 44 / Galgame_Speech_ASR_16kHz 是一個 16 kHz ASR 資料集，包含 3.75 百萬對（≈5,354 h），由 Galgame_Dataset 派生，採 GPL v3.0 授權，禁止商業使用，且任何訓練出來的模型必須開源（引用可選）。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 536 / ⭐ 141 / 日語說明式對話資料集，用於微調 LLM（例如 LoRA），9M+ 範例，最近更新為去除授權的 Alpaca 數據，清理 Wikipedia 和 ALT 輸出，並以 CC‑BY‑SA 4.0 發佈。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 474 / ⭐ 22 / 一個日本網路集合，包含56 million文件、110 B字元以及249 million圖像，這些資料被用於訓練大型視覺語言模型——提供momiji_generator進行資料填充、OBELICS‑style視覺化，以及一個範例模型（Heron‑NVILA‑Lite）。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 439 / ⭐ 3 / Japanese Guardrail model evaluation dataset (1,725 samples)、WildGuardTest 的高品質多階段翻譯、以 ODC‑BY license 釋出且可於 Hugging Face 獲取。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 418 / ⭐ 5 / Japanese JaQuAD（QG‑Bench 的子集）提供句子級和段落級資料，並以高亮顯示答案 token，用於訓練日語提問生成模型，評估指標包括 BLEU4、METEOR、ROUGE‑L、BERTScore 與 MoverScore。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 404 / ⭐ 10 / 一個日文對英文平行語料庫，將 llm‑jp‑corpus‑v3 的 kaken 子集翻譯成英文，使用 Qwen/Qwen2.5‑32B‑Instruct，特點為自訂翻譯欄位，並以 CC‑BY‑4.0 授權。
 * [jhle](https://huggingface.co/datasets/llm-jp/jhle) - 📥 396 / ⭐ 96 / 由 LLM‑jp 策劃的日文翻譯版 Humanity’s Last Exam dataset，該數據集省略了圖像問題，每個 raw_subject 抽取五筆樣本，已機器翻譯並由專家審核，並且由 Yuji Tamakoshi、Kouta Nakayama 和 Yusuke Miyao 撰寫，絕不能用於訓練語料庫。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 388 / ⭐ 6 / 將日文資料集轉換為 SentenceTransformers 友好的欄位，並根據 Rerank 分數（≥0.7 為正面，≤0.3 為負面）篩選範例，從多個 HuggingFace 來源擷取，以支援對比學習，同時遵守原始授權。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 378 / ⭐ 5 / STAIR‑Captions 在 2017 年發布，提供 820,310 條日語字幕，用於字幕生成、多模態檢索和圖像生成，並帶有詳細標註、元資料以及 Creative Commons BY‑4.0 license。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 361 / ⭐ 11 / JDocQA 是一個以日文 PDF 為基礎的問答資料集，包含 5,504 篇文件和 11,600 個問答對，測試是/否、事實、數值、開放式、無法回答的理解，並同時使用視覺和文字資訊。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 340 / ⭐ 27 / WRIME 數據集是一個日本語收藏，包含 42,200 篇文章，已用 Plutchik 的八種情緒為作者、三位讀者以及他們的平均值進行標註，並結構為 40k‑train、1.2k‑validation、2k‑test 的分割，供情感分析任務使用。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 340 / ⭐ 16 / 日本語 Alpaca 資料，來源於 masa3141 的日本語 Alpaca‑LoRA 工作，並引用原始倉庫以供進一步細節參考。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 338 / ⭐ 2 / 日語 Callhome 語音檔已轉換為 WAV，並附帶 JSON 格式的元資料陣列與 RTMM 旁白標籤檔，供評估使用。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 323 / ⭐ 13 / Dataset 卡片（針對 “wikipedia-ja-20230720” 日文維基百科快照）
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 322 / ⭐ 6 / 已去重、NFKC‑正規化的 mQA 查詢–段落對，pos_ids/neg_ids 對應於集合索引，便於直接通過 collection[pos_id] 進行檢索，並遵循原始數據集的授權條款。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 319 / ⭐ 3 / Japanese Explainable Multi‑hop Question Answering dataset 特色為問題、答案與逐步推導，連結 Wikipedia 文章，並更新推導格式及多個版本發布。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 318 / ⭐ 18 / 部分 *Project Sekai* 聲樂曲目資料集，專為草薙寧々（來源 CV Machico）設計，包含 nene_org.txt 標籤檔，計畫擴充並標準化資料，並呼籲收藏此 repo、分享想法及加入 QQ 群，以取得完整收藏。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 306 / ⭐ 21 / 使用英文提示生成的 AI 動漫插圖，以及來自 Phi‑3 Vision 的字幕（英文與日文），已釋出至公共領域供免費使用。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 293 / ⭐ 3 / BBH‑ja 提供 BIG‑Bench Hard 資料集的日文翻譯，提供 JSON‑L（輸入、正確目標）格式的評估問題，以及 YAML（輸入、目標）格式的 Chain‑of‑Thought 提示，翻譯使用 PLaMo 模型。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 283 / ⭐ 3 / 已清理的日語網頁語料庫 (mc4‑ja, etc.) 經無監督學習分群為約10,000篇文本，其中僅部分文件為 Parquet；檔案清單位於 out 資料夾，可使用 Git LFS 下載，供合法允許的資訊分析使用。
 * [LLMChat](https://huggingface.co/datasets/team-hatakeyama-phase2/LLMChat) - 📥 279 / ⭐ 4 / 來自 LLMChat 系統的 2,139 條人工評分 Q&A 配對的資料庫，每個使用者問題會隨機收到 13 個參與模型中的兩個答案，審閱者會挑選較佳回覆（1 = 第一，2 = 第二，0 = 兩個皆差，3 = 兩個皆良好），並包含問題、兩個答案、評估、可選的修正答案、模型名稱、時間戳，以及 CC0 授權文本和模型專屬輸出許可證。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 269 / ⭐ 7 / JHumanEval 是手工翻譯的日本版 HumanEval benchmark，提供 164 個 Python 程式設計問題，並提供對應的英文與日文註解，旨在評估 Japanese-LLM 程式產生，同時保留原始英文錯誤。
 * [dataset-for-annotation-v2-annotated](https://huggingface.co/datasets/preference-team/dataset-for-annotation-v2-annotated) - 📥 260 / ⭐ 3 / 一個日語合成問答對數據集，由母語者標註偏好及強度（−3到3），涵蓋多種體裁，說明有限的變化、常見的 LLM 詞句模式、缺失的實際場景，以及深化專業知識的機會。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 259 / ⭐ 9 / 此為 llm-book/wrime‑sentiment 的資料集卡，提供一個由 WRIME 衍生的二元日語情感分析集合，根據 Avg. Readers_Sentiment 標記為正向或負向（可選擇包含中性案例），並作為《Introduction to Large Language Models》一書的樣本資料。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 258 / ⭐ 2 / JCommonsenseQA 是一個日語多選題常識推理資料集——CommonsenseQA 的改編版——授權為 CC BY‑SA 4.0，並以 doi:10.5715/jnlp.30.63 引用。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 249 / ⭐ 15 / Hachi-Alpaca 傳遞的日本語合成資料源自 Stanford Alpaca，經 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 之精煉與驗證，並透過 Deepinfra 使用，附帶已通過 model‑based quality checks 的 “_cleaned” 版本。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 248 / ⭐ 3 / 日文維基百科句子被轉換為各種嵌入，並建立 FAISS 索引，提供 Hugging Face Space 的演示、轉換腳本，以及對搜尋、問答和 OpenAI text‑embedding‑3‑small 在 RAG 中的評估；嵌入採用 OpenAI 授權，其他則採用 CC‑BY‑SA‑4.0。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 245 / ⭐ 14 / 1.8 百萬個日文翻譯條目，來源於 OpenMathInstruct‑1，並由 GSM8K 與 MATH benchmark 題目配合經驗證的 Mixtral‑8x7B 產生的合成解答組成，已在 NVIDIA 的授權下商業可用。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 234 / ⭐ 5 / JSNLI 是 Kurohashi‑Chu‑Murawaki Lab 發布的 SNLI 自然語言推理基準的日語翻譯，以 TSV 格式提供，前提和假設已使用 JUMAN++ 斷詞，提供約 533,000 和 548,000 對的篩選與未篩選訓練集，以及 3,916 對的驗證集，採用 CC BY‑SA 4.0 授權。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 233 / ⭐ 15 / 一個簡易的 Zundamon 角色設定資料集—由線上來源及管理數據編輯—用於測試 character‑LLMs，提供於 zmnjp.jsonl 與 zmn.jsonl 格式，並依指定授權提供。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 233 / ⭐ 2 / 來自 AWS Open Data 註冊庫的 ABEJA‑CC‑JA 數據集的 Hugging Face 鏡像，詳情請參考 ABEJA 的技術部落格文章。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 232 / ⭐ 11 / JaQuAD 是 2022 年的日本 QA 資料集，包含 39,696 對 SQuAD‑style 抽取式問答對，來源於 Wikipedia，總量 73.2 MB，當使用 BERT‑Japanese 微調時，F1 分數達 78.92 %（EM 63.38 %）。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 215 / ⭐ 3 / 2010 年的日本網路語料庫已上傳至 HuggingFace，並按 2009 年版權改革為研究授權，包含自動帶標點的文本，這些文本來自形態學解析和轉換腳本。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 214 / ⭐ 6 / Range3 的 wikipedia-ja-20230101 存儲庫提供只包含日文維基百科文本的 Parquet 檔案，這些文本是從完整的維基百科資料集提取並使用 Python 程式碼生成。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 214 / ⭐ 80 / 句對齊的日本網路小說章節與英語粉絲翻譯（106K+ 條目，版本 2），設計用於翻譯研究，更新對齊、增加系列元資料、未做品質篩選，依 fair‑use 及 Apache 2.0 分發，受 Hugging Face 的下架請求約束。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 206 / ⭐ 51 / AnswerCarefully Dataset 提供日語及多語言資料，用於商業或非商業 LLM 安全增強；禁止任何其他用途——包括安全繞過；允許帶歸屬的衍生作品；並附帶創作者對損害或服務變更之非責任免責聲明。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 203 / ⭐ 9 / JSICK 是一個從 SICK 翻譯而成的日本 NLI/STS 數據集，提供了一項壓力測試，透過多個變換後的句子對子集探測 word‑order 與 case‑particle 處理，以支援多語言組合推理的研究。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 202 / ⭐ 6 / Dataset card for “oscar2301‑ja‑filter‑ja‑normal”，目前缺少詳細資訊。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 201 / ⭐ 4 / 「Japanese RAG Generator Benchmark (J‑RAGBench)」供應一份多分類 QA 數據集—涵蓋 Integration、Reasoning、Logical、Table 與 Abstention—旨在評估日文 RAG 生成器，並由人力與 GPT‑4.1 建構，且以 CC BY‑SA 4.0 授權發布。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 200 / ⭐ 16 / 一個 1.9 億對 JSONL 資料集，用於日語假名至漢字轉換，為 zenz‑v2.5 medium、small 與 xsmall 模型提供基礎，並包含 AJIMEE‑Bench 評估語料庫。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 198 / ⭐ 11 / Range3/wiki40b‑ja 是 wiki40b 數據集的日文子集，作為由 Python 數據處理流程產生的三個 Parquet 檔案。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 197 / ⭐ 8 / JMMMU‑Pro 是一個日本的多模態基準，通過 Vibe Construction 建立——結合生成式建模和人工驗證——以產生低成本、高品質的 image‑QA 數據，揭示開源 LMMs 的缺陷並指引未來 VQA 研究。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 185 / ⭐ 4 / JFWIR 是一個 64‑million‑pair 的日文資訊檢索資料集，由 fine‑web educational crawls 構建而成，提供每份文件七種查詢類型、hard negatives，並在 benchmark performance 上明顯優於此前的 prior baselines。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 185 / ⭐ 2 / 一個開放、CC‑BY‑4.0 的日本證券表格資料集，提供圖像、帶邊界框的 OCR 文本，以及直接的單元格值 Q&A，用於多模態視覺‑語言模型訓練，基於 NTCIR‑U4 和 EDINET。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 184 / ⭐ 16 / Galgame_Speech_SER_16kHz 是一個 3.7 百萬檔（5,353 小時、104 GB）情感語音資料集，來源於 Galgame_Speech_ASR_16kHz，經本地 LLM 標註，依 GNU GPL v3.0 發佈，禁止商業使用，且訓練於此的模型必須開源，且不強制要求引用。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 182 / ⭐ 15 / JGLUE 資料集卡片，使用於《Large Language Model Introduction》一書，來源自原始倉庫，程式碼採用 CC BY‑SA 4.0 許可，資料受發行者授權，引用 Kurihara & Kawahara（以日文）並建立於 Shunsuke Kitada 的倉庫。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 182 / ⭐ 18 / Databricks‑dolly‑15k‑ja 數據集是一個 DeepL 翻譯的日文版本，為指令微調而由日本 LLM‑jp 專案創建，作者為 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 與 Takumi Okamoto。
 * [relaion2B-en-research-safe-japanese-translation](https://huggingface.co/datasets/llm-jp/relaion2B-en-research-safe-japanese-translation) - 📥 176 / ⭐ 4 / 一個快速的英譯日文翻譯管道，採用 text2dataset、Gemma‑2‑9b‑it 和 vLLM 建構，透過簡潔、開放權重 LLM 提示，將大型 relaion2B‑en‑research‑safe 版語料轉換。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 175 / ⭐ 12 / LLM‑jp 提供一個日語指令調校數據集，來自 oasst2 的英語子集經 DeepL 翻譯（源自 kunishou/oasst2‑135k‑ja）並由 Kiyomaru 與 Kodama 編譯。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 168 / ⭐ 5 / J‑HARD‑TTS‑Eval 對日本語自回歸 TTS 模型進行評估，測試短序列穩定性、重複、押韻和延續等失敗情況，並提供帶有提示音頻和文本的數據集，透過 Hugging Face 可載入。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 167 / ⭐ 16 / oasst1‑21k‑ja 是一個由 DeepL 從英文 OASST1 子集衍生而來的日語指令調整資料集，通過日本的 LLM‑jp 合作項目創建；如需聯繫，請發送電子郵件至 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 以及 Okamoto。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 160 / ⭐ 10 / 一個高品質的合成日語數學題目資料集，具有已驗證的鏈式思考推理，透過 Qwen2‑7B‑Instruct 將 PRM800K 和 GSM8K 進行翻譯並篩選正確性後構建，可透過 Hugging Face datasets library 獲取。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 157 / ⭐ 33 / Allganize RAG Leaderboard 發佈日本 RAG 性能資料以及涵蓋金融、電信、製造、公共部門與零售五個行業領域的自動端到端評估結果，協助企業在尚未出現全面日本基準的情況下，對解析器、檢索與生成組件進行基準測試。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 155 / ⭐ 24 / AutoWikiQA 是日本最大的免費 QA 數據集（2,377,503 對），由 Wikipedia 文字使用 Swallow‑MX 與 vLLM 生成，提供多樣、無模板的問題與答案，用於知識注入及檢索增強生成。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 145 / ⭐ 26 / 日本語翻譯的 OpenAssistant/oasst1 資料，含失敗旗標；約 2,000 個手動修正的程式碼翻譯錯誤；已發佈的聊天格式子集 (oasst1-chat-44k-ja)；以及將條目轉換為指令-輸出對的腳本，用於微調。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 141 / ⭐ 19 / 一個日語 QA 數據集，用於評估 Retrieval‑Augmented Generation (RAG)，由 JAQKET 題目與 Wikipedia 文章構建，帶有金鑰檢索相關性標簽，已於 HuggingFace 和 GitHub 發布，主要以 nDCG@10 作為評分指標。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 141 / ⭐ 3 / 資料集卡為「Introduction to Large‑Scale LLM II」一書中使用的 ja‑vicuna‑qa‑benchmark，並由 llm‑jp‑eval 為跨資料集的日語 LLM 評估所創建（Apache 2.0）。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 136 / ⭐ 10 / JA‑Multi‑Image‑VQA 是包含 39 張圖片、55 個題目的資料集，擁有手工製作的日語 Q&A 用於多圖像 VQA，透過 load_dataset 訪問，文本授權為 Apache 2.0（圖片受限）。
 * [jawiki-bullet-points](https://huggingface.co/datasets/hpprc/jawiki-bullet-points) - 📥 136 / ⭐ 4 / 一個 CC‑BY‑SA‑4.0 的日語維基百科文字資料集，已轉成項目符號，使用 Apache‑2.0 授權的 DeepSeek R1 Distill Qwen 32B model 透過 random sampling 產生，允許重複項目——但在 Hugging Face 上可能不總能清楚顯示行分隔符。
 * [nagisa_stopwords](https://huggingface.co/datasets/taishi-i/nagisa_stopwords) - 📥 130 / ⭐ 2 / 一個 147 個單詞的日語停用詞清單，來源於 CC‑100 Wikipedia，MIT 授權，並以 nagisa.stopwords 的方式內置於 nagisa tokenizer，方便使用。
 * [EliteVoiceProject](https://huggingface.co/datasets/Elite35P-Server/EliteVoiceProject) - 📥 119 / ⭐ 12 / Elite Voice Project 將 Sakura Miko 的語音錄音編製為符合 Hololive 的語音辨識研究資料集，並邀請協作者透過結構化的 `audio_raw` 資料夾（twitch、twitter、youtube）在 train/test 分割下新增新片段，同時遵守 Hololive 的衍生作品指引。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 119 / ⭐ 2 / WAON 是一套用於視覺‑語言模型的大規模、優質日文圖像-文本配對資料集，透過尺寸和 SigLIP 分數過濾及 URL、標題、感知雜湊去重生成，並以 Apache 2.0 版權授權，使用限制於根據日本法規僅用於資訊性分析。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 118 / ⭐ 4 / 資料集卡片：用於《Introduction to Large Language Models》一書的 Loonwit 提供的 livedoor 新聞語料庫，包含已去除 HTML 標籤的 Creative Commons 授權新聞文章（CC BY‑ND 2.1 JP）。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 115 / ⭐ 5 / JetCopper‑10B 是一個日英資料集，包含 4.7 億日文 token 與 0.9 億英文‑code token，來源於經過清理的 CC‑100、OSCAR‑2301、HPLT v1.2 與 wiki40b‑ja 子集，用於預訓練 Contrail‑200m‑64k，以參與 LOCAL AI HACKATHON #000，但尚未進行句界限或困惑度篩選。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 112 / ⭐ 2 / 提供日本 Common Voice 17.0 子集，含 649 位講者（每位 30–300 個樣本）、45,668 個語句，按講者分成 80/20，批次為 1,000‑sample Parquet 檔案，全部採用 CC0 許可。
 * [oasst1-chat-44k-ja](https://huggingface.co/datasets/kunishou/oasst1-chat-44k-ja) - 📥 111 / ⭐ 10 / 一個基於 oasst1‑89k‑ja 的 ShareGPT 格式多輪對話數據集，用於微調，需大量計算資源；請參見隨附的文章以及 GitHub/HuggingFace 連結。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 110 / ⭐ 11 / Japanese Roleplay Dialogues dataset 按照以下規則進行過濾：移除 ≤1 名投稿者或 ≤10 則貼文的記錄，標準化並匿名化投稿者名稱，只保留前兩名投稿者佔貼文 ≥90% 且各自貢獻至少 40% 的對話，供機器學習應用。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 107 / ⭐ 7 / Livedoor News Corpus 提供一套日語新聞文章數據集，分為 5 894 個訓練、737 個驗證和 736 個測試實例，已去除 HTML 標籤並以 Creative Commons Attribution‑NoDerivs 授權釋出。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 107 / ⭐ 2 / 一個包含 64,139 項日文姓名的資料集，已按生物性別標記——採用漢字、平假名與羅馬拼音——其 44.9k 訓練集、6.41k 驗證集與 12.8k 測試集的分割方式獲得 ISDA’23 的接受。
 * [japanese-stackexchange](https://huggingface.co/datasets/p1atdev/japanese-stackexchange) - 📥 106 / ⭐ 3 / 一個以英語為語言的日語 Stack Exchange 問答資料集，從網站的匯出資料中提取並處理，提供預設與扁平化子集，可透過 Hugging Face datasets 載入，授權為 CC BY‑SA 4.0。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 106 / ⭐ 41 / VNTL 排行榜通過在 256 個樣本上平均余弦相似度分數，來評估大型語言模型在將日語視覺小說翻譯成英語方面的表現，並對初步結果進行排名，同時與 Sugoi Translator、Google Translate、Naver Papago 等工具進行基準比較。
 * [Swallow-Instruct-v0.1](https://huggingface.co/datasets/tokyotech-llm/Swallow-Instruct-v0.1) - 📥 105 / ⭐ 11 / Swallow Instruct v0.1 資料集 — 來自 OpenAssistant2 與日語翻譯變體的 26,479 條對話，採用特定抽樣設定構建 — 旨在精調 Swallow v0.1 Llama‑3 與 OpenAI GPT 模型（8B‑70B），由東京科技大學、YOKOTA Laboratory 與 AIST 的研究人員製作。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 103 / ⭐ 29 / 一個採用 CC‑BY‑4.0 授權的資料集，手動提取自日本政府 FAQ 的 Q‑A 配對（附帶來源網址），旨在用於指令微調與 RAG 測試，因高品質而受到讚譽，但亦被指出偶有格式錯誤與強烈的官方政策語氣。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 101 / ⭐ 13 / 一份採用 CC‑BY‑SA 3.0 授權的日文實體抽取資料集，來源自維基百科，存放於 https://github.com/stockmarkteam/ner-wikipedia-dataset/，並由 Stockmark Inc. 開發。
