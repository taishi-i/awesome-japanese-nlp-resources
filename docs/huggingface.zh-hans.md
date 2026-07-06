# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专门收录日语NLP相关的Python库、LLM、词典和语料库资源的精选列表。
本页面列出了Hugging Face上可用的日语NLP专用模型和数据集。目前包含171个模型和133个数据集。

_更新于2026年7月6日_

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

| # | 模型名称 | Downloads | Likes | 类别 |
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

| # | 数据集名称 | Downloads | Likes |
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
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 299k / ⭐ 15 / 一个 12 层、768 隐藏层的日语 GPT‑NeoX 模型，训练数据为 CC‑100、C4 以及 Wikipedia，兼容 Huggingface，并配备可选的玩具前缀调优权重，能强制每个句子末尾以笑脸表情符号结束。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 98k / ⭐ 59 / 一款由 ABEJA Inc. 使用日语 CC‑100 和 OSCAR 训练的 2.7B 参数日语 GPT‑NeoX 模型，可通过 Hugging Face Transformers 管道或 PyTorch 使用，按 MIT 许可证发布。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 51k / ⭐ 42 / 提供来自 NII 的 8 B 参数 LLM‑jp‑4‑8b‑thinking 日语语言模型，使用 pre‑/mid‑training 训练并通过 SFT/DPO 对齐，已准备好与 torch‑transformers 一起使用，并附有详细的教程说明。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 50k / ⭐ 8 / LLM‑jp‑3‑150m——来自国立信息学研究所LLM研发中心的150 M参数日语语言模型——以 Hugging Face Transformers 格式发布，需要 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，并且在日本维基百科、Common Crawl、WARP/PDF、WARP/HTML 和 Kaken 数据上使用 unigram byte‑fallback tokenizer 进行预训练。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 45k / ⭐ 36 / 32亿参数的日语 Transformer LLM（llm‑jp‑4‑32b‑a3b‑thinking）来自国立信息学研究所，预训练和校准通过有监督微调和直接偏好优化完成——不使用强化学习——使用unigram byte‑fallback tokenizer。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 32k / ⭐ 139 / 9亿参数的日语优化LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，训练数据截至2024年9月，采用混合 Mamba‑2/MLP/4‑层注意力架构，已在 Nemotron‑Personas‑Japan 工具调用数据集上微调，可选地在生成最终答案前生成可控的推理轨迹，且可商用。
 * [Llama-3.3-Swallow-70B-Instruct-v0.4](https://huggingface.co/tokyotech-llm/Llama-3.3-Swallow-70B-Instruct-v0.4) - 📥 24k / ⭐ 13 / Llama 3.3 Swallow 是一个 70 Billion 参数的日语增强大型语言模型，基于 Meta 的 Llama 3.3 通过持续预训练和指令调优微调构建，已在 Hugging Face 和 Swallow 网站上发布多个版本（如 v0.4）。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 20k / ⭐ 21 / OpenCALM 是 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 许可证下发布的一套仅解码的日本 transformer 语言模型（160 M–6.8 B 参数），训练于 Japanese Wikipedia 和 Common Crawl，并可通过 Hugging Face’s torch‑transformers 使用。
 * [LFM2.5-1.2B-JP-202606](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606) - 📥 18k / ⭐ 63 / LFM 2.5-1.2B-JP-202606 是一款高性能、通用的日语聊天模型，在知识、指令遵循、数学、代码和工具使用方面优于同类不到 2 B 的模型，使其成为开发者构建具有文化细腻度的日语应用程序的理想选择。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 12k / ⭐ 7 / 预训练的 TinyLlama 在日语（≈50 k 步），基于约3 B OSCAR/mC4 tokens，可通过 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 和 Renju Aoki 创建。
 * [LFM2.5-1.2B-JP-202606-ONNX](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-ONNX) - 📥 12k / ⭐ 1 / 将日本 LFM2.5‑1.2B 模型导出为 ONNX，以便在跨平台推理中使用 ONNX Runtime、Transformers.js 和 WebGPU，提供多种精度变体（FP32、FP16、INT4/FP16 混合）以及推荐的 WebGPU 友好 INT4+FP16 格式。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 12k / ⭐ 39 / 提供了一款来自 SB Intuitions 的自回归式日语语言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已与其他模型进行基准测试，并附示例使用脚本，且安全训练有限。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 11k / ⭐ 17 / 来自 NII 研发中心的日本大型语言模型集合（1.8 b 至 172 b beta1，含 instruct 版本），以 Hugging Face Transformers 格式打包，并在混合日语、英语与网络语料库（总计>1万亿个标记）上预训练。需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29 以及 flash‑attn ≥ 2.5。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 9k / ⭐ 10 / llm‑jp‑4‑8b‑instruct 是 NII 的 LLM‑jp‑4 系列 4.1 B 参数的日语 LLM，先在大型语料库上预训练，随后仅使用监督指令数据进行微调（不使用 DPO/REINFORCE），并附带类似食谱的使用指南和 byte‑fallback unigram tokenizer。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 9k / ⭐ 2 / Qwen3‑Swallow v0.2 提供了 30‑B 和 32‑B 双语日英 LLM，采用 CPT、SFT 与 RLVR 训练，提升日语准确性、翻译、数学与编码能力，以匹配或超越原始 Qwen3，提供九个模型（CPT、SFT、RL）和 AWQ‑quantized 版本，同时发布 GPT‑OSS‑Swallow。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 9k / ⭐ 21 / Llama3 Swallow 是 Meta Llama 3 系列的日语增强版本，于 2024 年 7 月 1 日发布，提供 8B 与 70B 版本的 Instruct 与 chat 模式，已在 Megatron‑LM 上使用 SFT 与 Chat Vector 进行微调，并在关键的日语 NLP 任务上进行了基准测试。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 8k / ⭐ 85 / Rinna 的 24 层、1024 隐藏单元的日语 GPT‑2‑medium 模型，基于 CC‑100 和维基百科训练，采用 SentencePiece 分词，已在 rinna/japanese‑pretrained‑models 仓库公开（MIT 许可证，2021 年 4 月 7 日发布，2021 年 8 月 25 日更新）。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 8k / ⭐ 19 / Llama 3.1 Swallow 是一组 8‑B 和 70‑B 模型，它们继续对 Meta 的 Llama 3.1 进行预训练，以提升日语语言性能，然后在合成日语数据上进行指令微调，提供多种已发布的变体，其对话行为已改进，与 gemma‑3‑27b‑it 相当。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 实验性日语模型通过使用聊天向量方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 与 Meta‑Llama‑3‑8B‑Instruct 之间的差异创建，然后上采样并应用于 Meta‑Llama‑3‑70B‑Instruct，显示出变化不大，并计划未来扩大规模。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 7k / ⭐ 149 / Llama‑3‑ELYZA‑JP‑8B 是由 ELYZA 开发的、经过日语增强的 80 亿参数 Llama 3 模型，在 Meta‑Llama‑3‑8B‑Instruct 上针对日语微调。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 6k / ⭐ 10 / 仓库提供 GGUF 格式、量化的模型文件，适用于 Stability AI 的日本版 StableLM Instruct Gamma 7B，由 Massed Compute 硬件创建，并且是 TheBloke 的 a16z‑资助 LLM 工作的一部分。
 * [LFM2.5-1.2B-JP-202606-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-GGUF) - 📥 6k / ⭐ 21 / 液体AI的混合 LFM2 模型，例如 1.2 B 日语 GGUF 版本，提供高质量、快速且内存高效的边缘 AI，用于设备端部署，并可通过 Hugging Face 仓库使用 llama.cpp 本地运行。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 6k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27 B 参数扩展版，已在包含 instruct 和 fast 变体的日语数据上预训练，可通过 Hugging Face Transformers 使用。
 * [Qwen3-Swallow-8B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2-AWQ-INT4) - 📥 5k / ⭐ 1 / Qwen3‑Swallow v0.2 提供双语日英 30B‑A3B 和 32B 模型，基于 Qwen3 通过持续预训练、监督微调和带可验证奖励的强化学习构建，以提升日语水平、翻译、数学与编码推理能力，同时保持核心 Qwen3 性能，并提供若干量化变体。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 5k / ⭐ 24 / Llama 3.1 Swallow 是一系列日语增强的 8B/70B Llama 3.1 模型，通过持续预训练和日语特定指令微调训练，最新的 8B‑Instruct‑v0.3 在日语 MT‑Bench 上取得了最先进的结果。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 4k / ⭐ 6 / 一个存储库，托管来自国立信息研究所LLM研发中心的8.6 B参数llm‑jp‑4‑8b‑base transformer，采用预训练和中间训练，随后进行监督微调和直接偏好优化（不使用强化学习），并提供PyTorch‑transformers使用指南。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 4k / ⭐ 27 / rinna 的日语 GPT‑2 small 是一个 12 层、768 维隐藏层的 Transformer，训练于日语 CC‑100 和 Wikipedia，使用 SentencePiece 进行分词，发布于 2021 年 8 月 25 日，遵循 MIT 协议（Hugging Face: rinna/japanese‑gpt2‑small，参见 https://arxiv.org/abs/2404.01657）。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 4k / ⭐ 15 / SB Intuitions的 Sarashina2.2‑0.5B instruct v0.1 是一个拥有5亿参数的日语自回归模型，在日语和英语 MT 基准上表现良好，并已准备好通过 torch‑transformers 加载。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 3k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 与 Swallow Team 开发的紧凑型日语指令遵循语言模型，采用 Qwen2.5‑32B‑Instruct 的 TAID 蒸馏，并在日语文本上进一步预训练，且仅以 Apache 2.0 许可证供研究使用。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 3k / ⭐ 11 / Qwen3‑Swallow v0.2 提供了通过 CPT、SFT 和 RLVR 训练的日英 LLM（30B‑A3B 和 32B），保持了强大的数学、编码和推理能力，已发布九个模型以及 AWQ 量化版本。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 3k / ⭐ 49 / 一款日本持续预训练的 Mistral‑Nemo 模型（Mistral‑Nemo‑Japanese‑Instruct‑2408），基于 mistralai/Mistral‑Nemo‑Instruct‑2407 构建，可通过 transformers 使用设备映射和 ChatML 提示进行使用，已由 Ryosuke Ishigami 以 Apache‑2.0 许可证发布。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 3k / ⭐ 21 / 提供 1.8 B 参数 llm‑jp‑3.1‑1.8b‑instruct4 日本指令微调模型，来自 NII，兼容 Hugging Face Transformers 和 Torch ≥ 2.3.0，包括预训练和微调检查点以及使用示例.
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 3k / ⭐ 12 / 东京科技-LLM（TokyoTech‑LLM）基于 LLaMA‑2，并通过日语数据（SFT）微调，包含 Swallow‑7b/13b/70b 变体及其 instruct、NVE 和 “plus” 版本，发布时间从2023年12月到2024年4月。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 3k / ⭐ 21 / OpenCALM 是 CyberAgent 开发的日本解码器（decoder‑only）Transformers 语言模型系列（160 M–6.8 B 参数），基于日本维基百科和 Common Crawl 训练，并以 CC BY‑SA 4.0 许可证发布。
 * [LFM2-350M-PII-Extract-JP](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP) - 📥 2k / ⭐ 56 / LFM2‑350M‑PII‑Extract‑JP 是一款 350‑million 参数、在设备上运行的日语 PII 提取模型，性能可与 GPT‑5 相媲美，能够在合同、电子邮件和医疗报告中进行敏感数据遮蔽。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 2k / ⭐ 25 / 与 Hugging Face 兼容的日语中心 transformer 模型（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct）来自国立信息学研究所，在包含 Wikipedia、Common Crawl、WARP、Kaken、Dolma 在内的多种日语和英语语料库上预训练，并要求 torch ≥ 2.3、transformers ≥ 4.40、accelerate 与 flash‑attn。
 * [llm-jp-3-1.8b-instruct3](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct3) - 📥 2k / ⭐ 2 / 仓库托管了 llm‑jp‑3‑1.8b‑instruct3，这是日本国立信息学研究所的 1.8 B 参数日语 LLM，预训练于日语维基百科和 Common Crawl，已准备好在 Hugging Face Transformers（torch ≥ 2.3, transformers ≥ 4.40）中使用。
 * [llm-jp-3-150m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-150m-instruct3) - 📥 2k / ⭐ 4 / 来自日本信息学研究所的日语 150M 参数指令型 LLM，可作为符合 Hugging Face 的 Transformer 模型使用，需 torch ≥ 2.3.0 和 transformers ≥ 4.40.1。
 * [Wanabi-Gemma4-31B-GGUF](https://huggingface.co/kawaimasa/Wanabi-Gemma4-31B-GGUF) - 📥 2k / ⭐ 5 / 一款针对Project Wannabe结构化提示格式和日语创意写作优化的 Google Gemma 4 31B 的精调 GGUF 版本，同时保留通用对话与推理能力，适用于多种聊天 UI。
 * [japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - 📥 2k / ⭐ 74 / 一个 3.6‑B‑parameter 的日本 GPT‑NeoX 模型——36 层、2816 维隐藏层 transformer——采用 PPO‑based RLHF 在翻译后的 Anthropic 数据上训练，遵循指令式对话，表现出约 30 % 的人类对位和 34 % 的 ChatGPT‑based PPO 胜率超过 SFT，但倾向于生成重复文本。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 2k / ⭐ 17 / TokyoTech‑LLM 仓库提供了经过日本数据增强的 Swallow Llama‑2 系列 LLaMA‑2 模型，涵盖 7B、13B 和 70B 变体，其中包括 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以来发布的 7B Plus 版本。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 148 / LFM2.5‑1.2B‑JP 是一款针对日语优化的聊天模型，在日语知识与指令遵循方面优于 LFM2，支持使用 LoRA 进行微调，支持通过 Transformers、vLLM 和 llama.cpp 进行推理，取得 50.7 JMMLU、58.1 M‑IFEval 与 56.0 GSM8K 分数。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 58 / TinySwallow‑1.5B‑Instruct 是一个 1.5 B 的日语指令调优自回归语言模型，使用 TAID 从 Qwen2.5‑32B‑Instruct 进行蒸馏，供研究用途。
 * [sarashina2.2-1b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1) - 📥 2k / ⭐ 16 / 本仓库托管了 SB Intuitions 的 1 B‑parameter 自回归日语指令模型 sarashina2.2‑1b‑instruct‑v0.1，已在日语和英语 MT 与指令任务上与其他 Japanese‑BERTs 进行基准测试，附带 torch-transformer 使用代码片段和有限安全训练的警告。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 2k / ⭐ 15 / LLM‑jp提供13 B和1.3 B变压器语言模型，包括多种指令调优变体，采用Megatron‑DeepSpeed和Hugging Face Transformers生态系统构建。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 2k / ⭐ 16 / 一个6层、512隐藏单元的Transformer，称为Japanese GPT‑2 xSmall，在Japanese CC‑100和Wikipedia上使用SentencePiece分词训练，于2021年8月25日以MIT许可发布，并托管在Hugging Face（rinna/japanese‑gpt2‑xsmall）上，在arXiv 2404.01657中被引用。
 * [gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - 📥 1k / ⭐ 18 / 由 ABEJA, Inc. 在 Japanese CC‑100、Wikipedia 与 OSCAR 上训练的大型日语 GPT‑2 模型，使用 sentencepiece 进行分词，可通过 Hugging Face transformers 在 PyTorch 或 TensorFlow 上使用，依据 MIT license。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking-gguf) - 📥 1k / ⭐ 8 / LLM‑jp‑4‑8b‑thinking‑gguf 是日本信息学研究所（≈8 B 参数）的日语大型语言模型，使用中训练进行预训练，并通过监督学习和直接偏好优化对“思考”变体进行微调，可在 GGUF 格式下获取，并在食谱中提供详细的使用说明。
 * [Sakura-13B-Galgame-GGUF](https://huggingface.co/QuantFactory/Sakura-13B-Galgame-GGUF) - 📥 1k / ⭐ 2 / 量化、离线可用的 Galgame/轻小说翻译模型（Sakura-13B-Galgame-GGUF），使用 llama.cpp 构建，提供 GPT-3.5 级别性能，兼容 OpenAI‑API，并基于 Qwen/Qwen2 核心发布多种 GGUF 变体。该模型以 CC BY‑NC‑SA 4.0 授权，伴随非商业使用警告。
 * [open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - 📥 1k / ⭐ 4 / OpenCALM 是 CyberAgent 开发的一套日语仅解码器（decoder‑only）Transformer 语言模型，参数规模从 160 M 到 6.8 B，训练数据来自日语维基百科与 Common Crawl，并按 CC BY‑SA 4.0 许可发布。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 1k / ⭐ 30 / LFM2.5‑1.2B‑JP 是一个 1.2 B 参数的日语文本生成模型，基于 LFM2.5 混合架构构建，优化用于生成和完成任务，托管在 Hugging Face 上，并可通过 llama.cpp 运行。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 1k / ⭐ 108 / 一款 1.3‑B‑parameter、24‑layer transformer GPT‑1B，使用 Japanese C4、CC‑100 和 Wikipedia 进行训练，于 2022 年 1 月 26 日由 rinna Co. 发布，并在 MIT license 下公开。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 1k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一个 13‑B 的、基于指令预训练的日语语言模型，由 NII 的研发中心开发，并以 Hugging‑Face Transformers 检查点的形式发布，使用 UNIGRAM‑byte‑fallback 分词器。

### fill-mask
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 2M / ⭐ 39 / Japanese‑Roberta‑Base 是来自 rinna Co., Ltd. 的预训练掩码语言模型，提供了正确加载、token 预处理、position‑id 处理的准则，以及强调需要前置 [CLS] token 和一致 tokenization 的使用示例。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 481k / ⭐ 9 / 日语 DeBERTa V2 大型模型，已在 171 GB 的日语 Wikipedia、CC‑100 与 OSCAR 上训练，使用字符级 SentencePiece 分词和全词掩码，已准备好通过 Hugging Face Transformers 进行下游微调。
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 390k / ⭐ 76 / Japanese BERT‑base 在 2019 年日本维基百科上预训练，使用 IPA‑dictionary 与全词掩码，12 层 768 维，32,000 词表，512 标记序列，1 M 步骤，可在 cl‑tohoku/bert‑japanese 获取，遵循 CC‑BY‑SA 许可。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 213k / ⭐ 41 / 一个预训练于约 17 M 条日语维基百科句子（2.6 GB）的 BERT base 模型，使用 IPA 字典和 WordPiece 进行分词，拥有 12 层 / 768‑维隐藏状态 / 12 头，32 000‑token 词汇表，已在 Cloud TPUs 上训练了 1 M 步，并以 CC‑BY‑SA 3.0 许可发布。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 70k / ⭐ 6 / 一个 BERT‑base 日语模型（12 层，768-维隐藏状态，12 头），在 3000 万条维基百科句子（约 4 GB）上训练，使用 Unidic 2.1.2 词级分词，随后进行字符级分词和全词掩码，使用 512 令牌序列，256 批次，以及 1 M 训练步骤。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 16k / ⭐ 25 / ModernBERT‑Ja‑310M 是一种日语 BERT 变体，融合了局部-全局注意力和 RoPE，训练于 4.09 T 日语/英语文本，支持 102 400 词汇量、8 192 令牌序列，并针对 Flash Attention 2 进行了优化。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 14k / ⭐ 49 / LINE DistilBERT Japanese 是一个 6600 万参数的 DistilBERT 模型，已在 131 GB 的日语网页文本上使用内部 BERT‑base 教师进行预训练，评估基准为 JGLUE，采用 MeCab Unidic 与 SentencePiece 进行分词，并以 Apache 2.0 许可证发布。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 13k / ⭐ 49 / 这是一款 1.32 亿参数的日语 ModernBERT 模型，融合了 local‑global 与 RoPE 注意力机制，训练于 4.39 T 词条（日语/英语），词表大小 102k，最大序列长度 8,192，针对 Flash Attention 2 做了优化。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 11k / ⭐ 8 / 一个 BERT‑base 日语模型（12 层，768 维隐藏，12 头），使用 MeCab IPA 词级分词后再进行字符级分词生成 4000 词的词表，在约 1700 万句来自日语维基百科（2.6 GB）的句子上预训练，训练代码位于 cl‑tohoku/bert‑japanese，采用 CC BY‑SA 3.0 许可证发布。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 8k / ⭐ 26 / Japanese BERT‑base（12 层，768 隐藏，12 头）在 4 GB 的日语维基百科（≈30 M 句）上预训练，使用 Unidic 2.1.2 词级分词、WordPiece 子词分词和全词遮蔽。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 4k / ⭐ 5 / DeBERTaV2 base 在日本语语料库（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上训练，并使用 FP‑16 微调进行 NLU 任务（JSTS、JNLI、JCommonsenseQA），以 CC BY‑SA 4.0 许可发布，并由日本研究资助。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 4k / ⭐ 7 / ModernBERT‑Ja‑30M 是一种日语 BERT 变体，融合了本地和全局注意力与 RoPE，训练于 4.39 TB 日英文本，支持 8,192 令牌序列，参数规模从 30 M 到 130 M，最佳搭配 Flash Attention 2。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 3k / ⭐ 30 / Japanese DeBERTa V2 基础模型已在 171 GB 的日语维基百科、CC‑100 和 OSCAR 数据上预训练，使用 Juman++ 分词和 SentencePiece 标记化，经过三周在八块 NVIDIA A100 GPU 上训练，现已准备好用于微调。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 3k / ⭐ 1 / 一款日本DeBERTa‑V2基础模型，已在171 GB的日本维基百科、CC‑100和OSCAR文本上预训练，使用字符级分词、全词掩码，训练耗时20天，使用8块A100 GPU，并已准备好进行下游微调。
 * [llm-jp-modernbert-base](https://huggingface.co/llm-jp/llm-jp-modernbert-base) - 📥 2k / ⭐ 12 / 一个 ModernBERT-base 模型在 3.4 TB 日语 llm‑jp‑corpus v4 上训练，经过两阶段微调（max_seq_len 1024 → 8192），达到了 0.92 JSTS、0.91 JNLI 和 0.88 JCoLA。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 2k / ⭐ 4 / 日本语 RoBERTa‑base 模型，预训练于约1千万条医学科学摘要（≈1.6 GB）来自 JST，用 SentencePiece Unigram (30k vocab) 进行分词，采用 CC‑BY‑4.0 许可，可通过 Hugging Face pipelines 微调。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 2k / ⭐ 2 / Japanese DeBERTa V2 tiny，在约171 GB的日本维基百科、CC‑100 与 OSCAR 语料库上预训练，需使用 Juman++ 词分割，训练耗时 33 小时，使用8块 NVIDIA A100 GPU，并可用于下游任务的微调。
 * [modernbert-base-japanese-wikipedia](https://huggingface.co/KoichiYasuoka/modernbert-base-japanese-wikipedia) - 📥 2k / ⭐ 5 / A ModernBERT 模型在日语维基百科和青空文库上预训练，使用 NVIDIA A100 GPU 训练了 56 小时，可用于下游任务的微调，例如词性标注和依存句法分析。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 2k / ⭐ 7 / ModernBERT‑Ja‑70M 是一种轻量级的日语 BERT 变体，结合本地和全局注意力与 RoPE，在 4.39 T 的混合语言词元（词表 102 400，最大 8 192 个词元）上训练，支持 Flash Attention 2，并提供 30 M 到 310 M 参数的多种尺寸。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 682k / ⭐ 81 / Ruri v3 是基于 ModernBERT‑Ja 的先进日语文本嵌入模型，支持多达 8,192 词元输入，100K 词元词汇表，FlashAttention 加速推理，并提供多种尺寸变体，便于快速使用 sentence‑transformer。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 219k / ⭐ 10 / Ruri v3是一个最先进的日语文本嵌入模型，基于ModernBERT‑Ja构建，支持最多8,192个标记，拥有100 k词汇量，支持FlashAttention加速，并提供多种规模，从37 M到315 M参数。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 133k / ⭐ 24 / GLuCoSE v2 是一款 CPU 友好的日语文本嵌入模型，通过蒸馏和多阶段对比学习进行微调，提供卓越的语义相似性和检索性能——在 MIRACL 及相关基准上优于同等规模的模型。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 59k / ⭐ 3 / Ruri v3 提供高性能的日语文本嵌入，支持至 8192 个 token，拥有 100k 个 token 的词汇表，支持 FlashAttention，并提供多种模型规模（30 m–310 m），以实现高效推理和通过 sentence‑transformers 进行微调。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 53k / ⭐ 47 / PLaMo‑Embedding‑1B 是 Preferred Networks 的一款日语文本嵌入模型，它将日语文本转换为向量，用于信息检索、分类和聚类，在 JMTEB 基准上表现出强大性能，并且在 Apache v2.0 许可证下可免费使用。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 44k / ⭐ 6 / Ruri v3 是基于 ModernBERT‑Ja 的前沿日语文本嵌入模型，支持最多 8192 token 序列、100K token 词汇量、FlashAttention，并以 30 M 至 310 M 参数规模发布，供 sentence‑transformers 使用。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 19k / ⭐ 34 / GLuCoSE 是一个基于 LUKE 的日语句子嵌入模型，输出 768 维均值池化向量（最多 512 个标记），在 Web 和 NLI/搜索数据上训练，在相似性基准测试中达到了 0.864 的 Spearman 相关系数和 0.818 的 Pearson 相关系数。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 17k / ⭐ 45 / 一组已准备好发布的 Ruri v3 日语文本嵌入模型（30m–310m），完整附带 SentenceTransformer 使用技巧、查询/段落前缀，以及 JMTEB 基准结果，展示它们与其他日语和多语言嵌入模型的比较。
 * [ruri-large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2) - 📥 15k / ⭐ 10 / 日本通用文本嵌入仓库 Ruri 提供 v3 模型，参数数从 30 M 到 310 M，具备 JMTEB 分数；并演示如何使用 sentence_transformers（使用 “クエリ: ” / “文章: ” 前缀）加载它们，并给出基准结果比较多个日语嵌入模型。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 13k / ⭐ 9 / 包括 Ruri v3 日语文本嵌入（30 M–310 M 参数，8192‑token 限制，JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前缀的 Sentence Transformers 指令，以及对数个日语模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基准结果。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 9k / ⭐ 12 / 日语通用文本嵌入模型（Ruri‑v3，30‑310 M 参数，8192‑token 最大，JMTEB 分数高）与 Sentence‑Transformers 使用示例以及与其他日语嵌入模型的基准对比一起提供。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 7k / ⭐ 16 / JaColBERTv2 是一个仅适用于日语的基于 ColBERT 的检索模型，在 MMarco 上通过知识蒸馏训练（每个正例 31 个负例，250k 次，batch 32）。目前它优于 multilingual‑e5‑large、BGE‑M3 和 JaColBERT，完整评估正在进行中。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 3k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一个 768 维的句子变换器，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，训练了一个 epoch 的 shunk031/jsnli，并包含用于聚类、语义搜索以及同时兼容 Sentence‑Transformers 和 HuggingFace 的示例。
 * [simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) - 📥 2k / ⭐ 15 / 一个从 tohok u/bert-base-japanese-v2 在 JSNLI 数据集上微调的日本 SimCSE 模型，按 CC-BY-SA 4.0 许可证发布，并可使用 fugashi/unidic-lite 分词进行 sentence-transformers 使用。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 1k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B 是一个 1.2 B 参数的日语文本嵌入模型，构建于 Sarashina2.1‑1B 上，使用多阶段对比学习训练，以在 JMTEB 上达到最先进的分数，同时在非商业许可下生成 1,792 维的稠密向量，用于语义相似度、搜索和分类。
 * [ruri-base-v2](https://huggingface.co/cl-nagoya/ruri-base-v2) - 📥 1k / ⭐ 5 / 仓库提供新的日语文本嵌入 v3 模型（30M‑310M 参数，8 k‑token 最大，JMTEB 74‑77），可使用 sentence_transformers（使用 query/passage 前缀）加载，并包含与监督/无监督 SimCSE、LaBSE、E5 以及其他模型的基准比较。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 6M / ⭐ 61 / Japanese wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 与 JSUT 上微调，需 16 kHz 音频，并可通过 HuggingSound 或 HuggingFace 管道使用。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 216k / ⭐ 115 / Kotoba‑Whisper‑v2.2 是一个日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了说话人划分和自动标点功能，通过 HuggingFace‑Transformers pipeline，并与 Asahi Ushio 与 Kotoba Technologies 合作开发。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 35k / ⭐ 141 / Anime Whisper 是一款轻量级的日语 ASR 模型，在约 5,300 小时的动漫风格对话上进行微调，能够提供低幻觉、节奏对齐标点，以及准确转录非言语声音和 NSFW 内容，并且需要在没有初始提示的情况下运行。
 * [japanese-hubert-base-phoneme-ctc](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc) - 📥 11k / ⭐ 5 / 基于 rinna/japanese‑hubert‑base 的微调日语音素 CTC 模型，使用 ReazonSpeech v2 数据和 pyopenjtalk‑plus 标签进行训练，在新版 v2 发布（prj-beatrice/japanese-hubert-base-phoneme-ctc-v2）中实现了更高的准确率。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 10k / ⭐ 93 / Kotoba‑Whisper v2.0 是从 OpenAI Whisper large‑v3 蒸馏出的日语 ASR 模型，训练于 720 万个 ReazonSpeech 剪辑，推理速度快 6.3 倍，同时在同域测试中匹配教师模型的 CER/WER，并提供 stable‑ts/标点支持以及完整的训练代码在 GitHub 上。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 9k / ⭐ 11 / 一个由 facebook/wav2vec2‑large‑xlsr‑53 在 Common Voice 和 JSUT corpus 上微调的日本语音识别模型，针对 16 kHz 音频输入进行了优化。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 9k / ⭐ 56 / NVIDIA NeMo 的 0.6 B 参数 Hybrid FastConformer‑TDT‑CTC ASR 模型可转写带标点的日语语音，并可在 NeMo 框架内用于推理或微调。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 7k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供了快 6.3 倍的蒸馏 Whisper 模型，用于日语和英语 ASR，并实现双向语音转文本翻译，这些模型是基于 OpenAI 的 Whisper large‑v3 通过知识蒸馏、交叉熵和 KL‑divergence 损失构建。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 3k / ⭐ 18 / Kotoba‑Whisper‑v2.1 是一种日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了标点后处理管道，保持可比的 CER 性能，同时实现无缝、标点感知的转录。
 * [Qwen3-ASR-1.7B-JA](https://huggingface.co/neosophie/Qwen3-ASR-1.7B-JA) - 📥 3k / ⭐ 5 / 针对日语 ASR 对 Qwen3-ASR-1.7B 进行微调，优化其准确转写专有名词、机构和产品名称，以及以汉字为主或混合日英的技术术语。
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 2k / ⭐ 25 / Kotoba Whisper v2.0 被转换为 CTranslate2 格式，以便与 CTranslate2 和 faster-whisper 一起使用，提供安装、推理示例、Apple M2 基准测试和转换说明。
 * [japanese-hubert-base-phoneme-ctc-v3](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v3) - 📥 1k / ⭐ 5 / 为CTC音素识别微调的日本HuBERT-base（v3），加入了MeCab N‑best与pyopenjtalk‑plus后处理、结合CTC和MeCab成本的加权损失、更新排除规则，以及新增“ty”音素。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 1k / ⭐ 38 / reazonspeech-nemo-v2 是一个 619‑M‑参数的日语长文本 ASR 模型，基于改进版 Fast‑Conformer 及 Linearly Scalable Attention，在 ReazonSpeech v2.0 语料库上训练，支持通过 subword RNN‑T decoder（3000‑token SentencePiece）进行多小时推理，并以 Apache 2.0 许可分发。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 1k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一个 96.7 M 参数的 wav2vec 2.0 Base 模型，经过在 ReazonSpeech v2.0 日语 ASR 语料库上微调，达到 13.22 % 的 CER，可与 Hugging Face transformers 一同部署，并在 Apache 2.0 许可证下发布。
 * [parakeet-tdt-0.6b-ja-GGUF](https://huggingface.co/cstr/parakeet-tdt-0.6b-ja-GGUF) - 📥 1k / ⭐ 1 / A GGUF‑converted 0.6 B Japanese Parakeet TDT‑CTC model，能够与 CrispASR 的 CLI 一起用于 TDT 解码（CTC 回退），在 JSUT 上实现 6.4 % CER，并提供词级时间戳，可获得完整的 1.24 GB 精确构建版本以及约 470 MB Q4_K 量化变体（该变体在 ~8 个 token 后性能下降，建议使用 F16）。

### feature-extraction
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 133k / ⭐ 56 / 一个Japanese‑language T5 model，在约100 GB的Wikipedia和OSCAR数据上使用SentencePiece tokenization进行预训练，超越了Google’s multilingual T5在news‑classification benchmark上的表现，但需要fine‑tuning，并可能产生biased outputs.
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 43k / ⭐ 51 / 一款在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上使用 MultipleNegativesRankingLoss 细调的 Japanese Sentence‑BERT v2，较 v1 提升了约 1.5–2 %的准确率，并以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 发布。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 32k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一个 Apache‑2.0 许可的日语 CLIP 模型，基于 ViT‑B/16，训练于 CC12M captions 翻译成日语，并于 2022 年 5 月 12 日发布。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 24k / ⭐ 18 / 日本CLIP模型 clip‑japanese‑base‑v2，升级后约20亿图像‑文本对并采用蒸馏，配合 Eva02‑B 图像编码器和 12 层 BERT 文本编码器，将 ImageNet‑1k 准确率提升至 0.708，超过前代模型。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 24k / ⭐ 30 / LY Corporation的clip‑japanese‑base 是一个日语 CLIP 模型，在约10亿对图像‑文本对上训练，使用 Eva02‑B transformer 图像编码器和 12 层 BERT 文本编码器，在 STAIR 上实现 R@1 0.30，在 Recruit 上得到 0.89 的准确率，在 ImageNet‑1K 上得到 0.58 的准确率，并支持 zero‑shot 图像分类和检索。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 22k / ⭐ 11 / 用于生成句子嵌入的 Japanese Sentence‑BERT (v1) 模型，已提供改进版 v2，并通过 Hugging Face Transformers 以及自定义的 `SentenceBertJapanese` 类进行示例使用。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 9k / ⭐ 14 / Japanese Sentence‑LUKE 模型在与 Sentence‑BERT 同一数据集上训练，表现超过或匹配其性能，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，并通过 Hugging Face Transformers 的 MLukeTokenizer 与 LukeModel 进行使用。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 7k / ⭐ 2 / ja_ginza_electra 是一个 spaCy v3 Python 包，提供一个在 mC4 和 UD_Japanese_BCCWJ r2.8（基于 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator）上微调的日语 ELECTRA 模型，并配有自定义 bunsetu‑phrase 检测功能，按 MIT license 分发。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 3k / ⭐ 3 / 一个日语 BERT‑base 模型，在 JSNLI 上使用有监督 SimCSE 进行微调，通过 Sentence‑Transformers 或 HuggingFace 提供，采用 CLS 池化。在 1M 个样本上训练，批量大小为 512，学习率为 5×10⁻⁵，温度为 5×10⁻⁵，64 令牌限制，采用 BFloat16 精度。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 2k / ⭐ 25 / Sarashina‑Embedding‑v2‑1B 是一个 1,792 维的日语句子变换器，使用多阶段对比学习训练，获得了前沿的 JMTEB 分数，可通过 Sentence‑Transformers 并搭配可选指令前缀，用于语义相似度、搜索、改写挖掘、分类和聚类。
 * [llm-jp-4-vl-9b-beta](https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta) - 📥 1k / ⭐ 14 / LLM‑jp‑4‑VL 9B beta 是一个 90 亿参数的日语视觉语言模型，以 llm‑jp‑4‑8b‑instruct 和 SigLIP‑2 为基础，采用 InternVL3.0 样式的动态切块和轻量化 MLP 投影器，并在 FineVision 和 Jagle 上训练后，在日语基准测试中获得了竞争性表现。

### text-ranking
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 358k / ⭐ 5 / 日本训练的 CrossEncoder 重新排序器，尺寸从 xsmall（384）到 large（1024），以及 BGE‑v2‑m3‑v1 模型，提供微调、推理和 JQaRA、JaCWIR、MIRACL、JSQuAD 上的基准分数示例代码。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 280k / ⭐ 14 / Ruri‑v3 Reranker 是一个基于 ModernBERT‑Ja 构建的稳健日语文本重排器，支持最高 8,192‑token 序列、100k‑token 词汇表、FlashAttention 以及 SentencePiece 分词器，并可通过 sentence‑transformers 使用。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 56k / ⭐ 7 / 日语 CrossEncoder 再排序模型，覆盖 xsmall 到 large（含 BGE），在 JQaRA、JaCWIR、MIRACL 与 JSQuAD 上进行评估，并为 sentence_transformers 与 HuggingFace 提供即用的集成示例。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 50k / ⭐ 6 / 快、轻量级的日语 Reranker v2 模型（tiny、xsmall、small、base），带有基准测试分数和 GPU 速度，可通过 sentence_transformers CrossEncoder 与 transformers ≥ v4.48 使用（可选闪存加速 flash‑attn），并且在 ONNX/量化形式下可用于 CPU/ARM。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 7k / ⭐ 12 / 一个日语跨编码器重新排序器，使用 Sentence Transformers 构建，演示了不同规模 Ruri‑Reranker 模型的推理使用和基准结果。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 7k / ⭐ 2 / 使用 Sentence Transformers（交叉编码器）构建的日语重排序模型，可通过 `trust_remote_code` 加载，在 JQaRA、JaCWIR 和 MIRACL 数据集上进行基准测试，并由 hotchpotch 组织提供从小到大尺寸版本。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / Japanese CrossEncoder Reranker 模型（xsmall、small、base、large、BGE‑v2 m3）隐藏尺寸为 384–1024，示例推理通过 sentence_transformers 和 Hugging Face， 在 JQaRA、JaCWIR、MIRACL 和 JSQuAD 上得分 0.71–0.97+。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 2k / ⭐ 8 / 一个日本 Reranker v2 套件，发布 CrossEncoder 和 base 模型，覆盖从 tiny 到 large，每个都有基准得分和 GPU 推理时间，并要求 HuggingFace Transformers ≥ 4.48（可选 flash‑attn 用于更快推理）。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 1k / ⭐ 6 / 紧凑、高速的日语重排序库（v2）提供 tiny‑through‑base 和 cross‑encoder 模型，并给出详细的延迟与准确率统计，要求 Transformers ≥ 4.48（可选 Flash‑Attention 2），支持 ONNX/量化，适用于 CPU/ARM 部署。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 1k / ⭐ 16 / 日语 CrossEncoder 重排序模型——从xsmall到large——在日语文本上训练，通过sentence_transformers公开，评估在JQaRA、JaCWIR、MIRACL和JSQuAD上。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 758k / ⭐ 15 / 一个基于新 VNTL 数据集构建的 LLaMA 3 Youko qlora 微调模型，优化用于准确、逐字翻译日本视觉小说为英文，不使用聊天模式，采用默认 LLaMA 3 提示，并推荐中性采样（温度 0，无重复惩罚）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 187k / ⭐ 12 / Sugoi LLM 14B Ultra (GGUF) 是一个日语到英语的翻译模型，BLEU 分数为 21.38，几乎是其之前的 13.67 的两倍，在 RPG‑Maker 括号文本、提示遵循强度以及为交互式聊天 UI 的 JSON 输出方面表现出色。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 40k / ⭐ 75 / 来自 Opus 语料库的日语‑英语 Transformer‑Align 机器翻译模型，使用归一化和 SentencePiece 预处理，在 Tatoeba 测试集上达到了 41.7 BLEU 和 0.589 chr‑F。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 6k / ⭐ 123 / PLaMo Translation Model 是由 Preferred Networks 创建的大规模语言模型，专用于翻译任务，提供基础版、后训练版和评估版，在 PLaMo community license 下发布，并未针对聊天或其他下游用途进行 instruction‑tuned。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 3k / ⭐ 33 / FuguMT 是一个从日语到英语的 Marian‑NMT 翻译模型，使用 transformers 和 SentencePiece 构建，在 Tatoeba 上得分 39.1 BLEU。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 2k / ⭐ 35 / 已微调、GGUF-量化的 LFM2-350M checkpoint，用于近实时双向日英短至中等文本翻译，可通过 llama.cpp 使用。
 * [opus-tatoeba-en-ja](https://huggingface.co/Helsinki-NLP/opus-tatoeba-en-ja) - 📥 1k / ⭐ 15 / 英文到日语 transformer‑align MT 模型，BLEU 15.2，构建于 opus+bt‑2021‑04‑10，使用 normalization+SentencePiece，托管于 Tatoeba Challenge。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 1k / ⭐ 55 / FuguMT 是一个基于 Marian‑NMT 的英日翻译模型，使用 Hugging Face Transformers 和 SentencePiece 构建，并在 Tatoeba 上获得了 32.7 的 BLEU 分数。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 417k / ⭐ 176 / Manga OCR 是一款 Vision Encoder‑Decoder OCR 工具，可读取纵向和横向的日语漫画文本，包括 furigana，适用于多种字体和低质量图像，并且源代码可免费获取。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 66k / ⭐ 6 / Meikiocr的 `meiki.text.recognition.v0`——基于 D‑FINE 的 MobileNetV4 模型，在日本视频游戏文本上微调——为水平文本提供最先进的准确率和延迟，能够从 960×32 的输入中检测多达 48 个字符，并输出每个字符的边界框和置信度分数。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 49k / ⭐ 3 / meikiocr 提供一个基于 D‑FINE、开源权重的视频游戏文本检测模型（v0.1，使用 MobileNet‑v4 骨干网络，提供两种分辨率变体和 64‑box 限制），以及实验性的低延迟 tiny 与 small 变体，训练材料来自日本视频游戏和漫画。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 2k / ⭐ 4 / Manga OCR 是一种 Vision Encoder‑Decoder 系统，可在各种字体和低质量图像中提供高质量的日语漫画 OCR——包括带有假名覆盖的纵向和横向文本——并且也可用于一般印刷日语 OCR。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 1k / ⭐ 31 / Sarashina2.2‑OCR 是一个 3‑B 参数的端到端 OCR 模型，经过人工偏好优化后，能够将日文和英文文档解析为 Markdown，同时将表格转换为 HTML，数学公式转换为 LaTeX，图形转换为边界框注释，其实现方式是将 SigLIP2‑基础的视觉编码器与 Sarashina2.2‑3B‑Instruct LLM 集成，从而实现高分辨率视觉‑语言理解。

### token-classification
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 15k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日语 NER，能够提取八种实体类型（公司、政治/其他组织、设施、产品、事件），通过 `BertForTokenClassification` 实现，训练数据来自 Stockmark Wikipedia dataset，并可通过安装 `transformers`、`unidic_lite` 和 `fugashi` 使用，遵循 CC BY‑SA 3.0 许可。
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 9k / ⭐ 4 / 一款面向日语的 DeBERTa V3 模型，包含 xsmall、base 和 large 这三种变体，在推理阶段不使用形态学分析器，遵循词边界，采用精简词表（仅 large 版本使用 BPE），并兼容 Hugging Face。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 8k / ⭐ 26 / 在日语 NER 语料库上对 XLM‑RoBERTa‑base 进行微调（标签 PER, ORG, LOC, INS, PRD, EVT），使用 5‑epoch Adam（lr 5e‑5，batch 12），达到 0.0173 的验证损失，已发布在 Transformers 4.23.1 和 PyTorch 1.12.1。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 4k / ⭐ 11 / Fine‑tuned Japanese BERT‑Base适用于在维基百科数据集上的命名实体识别，该模型在《*Large Language Model Introduction*》一书第六章中呈现，并可通过Hugging Face transformers pipeline进行部署（Apache 2.0 许可）。
 * [yomi-linter-modernbert-ja-130m](https://huggingface.co/ayousanz/yomi-linter-modernbert-ja-130m) - 📥 1k / ⭐ 3 / Fine-tuned a ModernBERT-Ja-130m模型用于日语TTS预检错误检测，识别可能被G2P/字典基础系统（如OpenJTalk、piper-plus和VOICEVOX）误读的片段，并具有高召回率（≈80%）以及动态INT8量化支持。

### text-classification
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 10k / ⭐ 16 / 在亚马逊产品评论上对日语 BERT (cl‑tohoku/bert‑base‑japanese‑v2) 进行微调，用于情感分类，经过6个周期，学习率为2 × 10⁻⁵，达到约81 %准确率和0.73 F1。
 * [bert-for-japanese-twitter-sentiment](https://huggingface.co/LoneWolfgang/bert-for-japanese-twitter-sentiment) - 📥 10k / ⭐ 2 / 微调后的 BERT，用于 JTS1k 数据集上的日本推特情感分析，将推文分类为负面 (0)、中立 (1) 和正面 (2) 标签，已准备好用于 transformers pipeline.
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 3k / ⭐ 2 / 一个基于 Japanese BERT‑based model 的模型，已在 JGLUE JSTS 数据集上 fine‑tuned，用于语义相似性评分——在《Large Language Model Introduction》第5章中介绍——配有 Colab notebooks、transformers‑pipeline 用法以及 Apache 2.0 许可证。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 2k / ⭐ 15 / 训练于 chABSA 数据集的日语情感分析模型，获得 loss 0.0001、accuracy 1.0、F1 1.0，由 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 构建，使用 Adam（learning rate 2e‑05、10 epochs、batch size 16）优化，并通过 `model(**inputs)` 进行评估。
 * [bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - 📥 2k / ⭐ 9 / 基于cl-tohoku/bert-base-japanese-v3的Japanese BERT-Base v3，在MARC-ja JGLUE情感分析数据集上微调，可与Hugging Face `pipeline` 一起使用，采用 Apache License 2.0 发布。

### text-to-speech
 * [sarashina2.2-tts](https://huggingface.co/sbintuitions/sarashina2.2-tts) - 📥 60k / ⭐ 63 / sarashina2.2-tts 是一个 SB Intuitions 基于 LLM 的日语中心化 TTS 系统，提供高精度的日语和英语合成、自然富有表现力的声音、零样本克隆、跨语言一致性以及无缝代码切换。
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 2k / ⭐ 11 / 一款名为 **tsukuyomi‑wavlm** 的日本文本转语音模型——在 tsukuyomi corpus 的 100 条语句上经过 300 个周期的微调，使用 WavLM 判别器和 A1/A2/A3 声韵特征，基于 VITS 架构，导出为 61 MB 的 ONNX 文件，用以生成 22.05 kHz 的合成语音。

### any-to-any
 * [gemma-4-12B-it-qat-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-12B-it-qat-UD-japanese-imatrix) - 📥 20k / ⭐ 9 / 一个 1/4 大小、CPU‑friendly 的日语优化量化 Gemma 4 模型（Apache 2.0），可全程在本地运行，提供可选的开发者支持与稳健的基准测试。

### audio-to-audio
 * [LFM2.5-Audio-1.5B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF) - 📥 5k / ⭐ 23 / LiquidAI 的 LFM 2.5‑Audio 1.5B JP 模型的量化 GGUF 版本，包括语言、音频编码器和声码器权重（F32/F16/Q8_0/Q4_0），以及使用 llama.cpp 的 ASR 和 TTS CLI/Server 运行器。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 122k / ⭐ 11 / 日本语言 BERT‑Base（12 层，768 维，12 头）使用 Unidic 基于词级加字符级分词和全词掩码在 CC‑100 及 2023 Wikipedia 上进行预训练，产生 7,027 名词表。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 76k / ⭐ 64 / Japanese BERT‑base（12层，768维隐藏层，12头，32 k词汇表）在 CC‑100 和 2023‑Jan Wikipedia 上使用全词遮蔽预训练，采用 Unidic 2.1.2 词级分词加 WordPiece，训练 200 万步。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 69k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上训练，使用 Unidic‑lite 单词级标记化配合 WordPiece 子词和全词掩码（24 层，1024 维隐藏层，16 头，32k 词表），预训练代码在 cl‑tohoku/bert‑japanese。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 16k / ⭐ 11 / 一个预训练在≈100 GB的维基百科和 OS CC‑100 数据（SentencePiece 采用 10:1 混合且带 byte‑fallback）的日文 T5‑v1.1 模型，需要微调以适用于下游任务，包含迁移学习示例代码，指出输出中的潜在偏差，并遵循 CC‑BY‑SA 4.0 许可。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 7k / ⭐ 13 / 提供了 gguf 格式的 moonshotai 的 Moonlight‑16B‑A3B‑Instruct，已在 TFMC 的 imatrix 日语数据集上训练，准备好与 llama.cpp（CUDA‑enabled）一起使用，并通过执行 recipe‑request 提示来演示。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 5k / ⭐ 17 / 高性能的日本 SPLADE v2 通过 WebUI demo 实现稀疏向量转换和推理，使用 YAST 进行训练，提供 YASEM 嵌入，并报告 JMTEB benchmark 结果。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 4k / ⭐ 19 / Japanese DeBERTa V3 base 在 LLM‑jp v1.0 的 540 B tokens 上预训练，使用经过修改的 DeBERTa V3 设置训练，采用 unigram byte‑fallback tokenizer（不使用形态学分析器），并针对 JGLUE NLU 任务进行微调。
 * [kana-whisper](https://huggingface.co/sbintuitions/kana-whisper) - 📥 3k / ⭐ 6 / 一个经过微调的 Whisper large‑v3‑turbo 模型，用于将日语语音转录为片假名，作为 Sarashina2.2‑TTS 项目中 Joyo Kanji Yomi Benchmark 的 ASR 组件，并驱动 Kana CER Usage With Transformers 管道。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 75 / Llama‑3‑ELYZA‑JP‑8B 是一款经过日本增强的 8‑B Llama 3 模型，采用 GGUF (Q4_K_M) 和 AWQ 量化，支持通过 llama.cpp、LM Studio 或 OpenAI‑compatible API 运行。
 * [Qwen3.5-0.8B-JP-Tuned-v1.0](https://huggingface.co/CloudGoat/Qwen3.5-0.8B-JP-Tuned-v1.0) - 📥 2k / ⭐ 1 / 在 3.72 M 日语 token 上对 Qwen3.5‑0.8B 进行微调，取得了 61.39% JCommonsenseQA、49.88% JNLI、54.01% JSQuAD 和 70.43% MARC‑ja 的成绩，并实现了整体响应率提升 3.53%。
 * [llm-jp-4-kappa-32b-a3b-v0.1-gguf](https://huggingface.co/mmnga-o/llm-jp-4-kappa-32b-a3b-v0.1-gguf) - 📥 2k / ⭐ 2 / 第三智能的 llm‑jp‑4‑kappa‑32b‑a3b‑v0.1 的 GGUF 转换版本，使用 TFMC/imatrix-dataset-for-japanese-llm 的 imatrix 数据构建，可通过带 CUDA 支持的 llama.cpp 使用。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一个拥有80亿参数的 LLM，通过在合成日语数据上持续预训练和指令微调，提升了 Meta 的 Llama 3.1 在日语语言与代码/数学推理上的表现，同时保持了英语流畅性。
 * [gemma-4-E2B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E2B-it-UD-japanese-imatrix) - 📥 2k / ⭐ 2 / 经过 GGUF 转换的 Gemma‑4‑E2B‑it 模型，已细调以提升日语水平；使用 Unsloth® Dynamic Quantization 2.0 构建，已包含社区 Bug 修复和日文校准数据；可在 CPU 上运行（≥8 GB RAM，≥4 GB 磁盘），通过 llama.cpp。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 2k / ⭐ 15 / Sarashina2.2 提供 0.5‑B、1‑B 和 3‑B 语言模型， 这些模型由 SB Intuitions 通过三阶段流水线和合成数据训练，达到了日本 QA、数学和编码的顶级成绩，同时提供的预训练权重未进行指令微调，可能产生偏见输出。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 22 / 由 imatrix 数据构建的 pfnet 的 plamo‑2‑translate 的 GGUF‑格式发布，基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带通过 llama.cpp 在启用 CUDA 的硬件上编译和运行的说明。
 * [tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf](https://huggingface.co/mmnga/tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf) - 📥 1k / ⭐ 4 / 此仓库托管了 tokyotech‑llm 的 Llama‑3.1‑Swallow‑8B‑Instruct‑v0.3 模型的 gguf-format 转换，基于 imatrix 数据集构建，并已准备好在 llama.cpp 运行。
 * [t5-base-japanese-web](https://huggingface.co/megagonlabs/t5-base-japanese-web) - 📥 1k / ⭐ 21 / 32K词汇表的T5模型，预训练于日语网络文本（mC4 + Wikipedia），使用字节回退机制，在TPU v3‑8上进行100万步训练，并以Apache 2.0许可发布。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 1k / ⭐ 1 / 一个高度优化的 GGUF 版本的 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 并进行广泛的错误修复，专为日语语言能力调优，可在 llama.cpp 上运行，至少需要 16 GB 内存和 6 GB 磁盘（GPU 可选）。
 * [sarashina2.2-1b](https://huggingface.co/sbintuitions/sarashina2.2-1b) - 📥 1k / ⭐ 13 / 一款拥有10亿参数的日语大型语言模型Sarashina2.2‑1B，采用三阶段训练——基础训练、合成数据微调（针对数学/编码）以及小样本任务调优——在问答、数学和编码基准测试中优于以往模型，但仍未针对指令遵循进行调优，并可能产生偏见或不准确的输出。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5-gguf](https://huggingface.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf) - 📥 1k / ⭐ 2 / 由 tokyotech‑llm 完成的 Llama‑3.1‑Swallow‑8B‑Instruct‑v0.5 的 GGUF 转换，结合 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带用于 llama.cpp 的 Build/Run 指令。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 2M / ⭐ 62 / 聚合了2009年至2024年NicoNico Live的评论日志，总计超过150 GB，包括转移前、转移后以及实时NX‑Jikkyo捕获，提供了一个API，便于检索历史电视广播讨论。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 14k / ⭐ 9 / Cauldron‑JA 是一个日语视觉‑语言数据集，包含 44 个子数据集，使用 DeepL API 从 The Cauldron 翻译而来，可通过 HuggingFace’s datasets library 获取，并与原始数据集使用相同的许可证，prompts 在 CC‑BY‑4.0 下发布。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 12k / ⭐ 32 / FineWeb2 Edu Japanese 提供约120 million高质量教育日语文本（≈89.3 billion tokens）来自 FineWeb2，经过 DeepSeek‑API classifier（score ≥ 2.5）过滤，通过 ModernBERT‑Ja‑130M tokenized，并包含一个小-token子集（≤512 tokens）。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 8k / ⭐ 7 / VOICEVOX‑generated synthetic voice dataset comprising 445,793 .wav files (totaling 577 h 51 m 23 s) built from the ITA, つくよみちゃん, and ROHAN corpora.
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 6k / ⭐ 17 / Reazon Speech v2 数据集的镜像发布，包含已通过 UVR 去噪并去除背景音乐的音频文件（在八块 A800 GPU 上大约十天内处理了 4096 个文件中的 3674 个）。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 5k / ⭐ 35 / 为高效加载 Hugging Face datasets，重新结构化并重新上传 Galgame VisualNovel 数据集（OOPPEENN/5669737465666C656E63655F44617461337072657330），保留所有原始 audio/text，并提供带多种 game-subset 选项的 extraction script。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 5k / ⭐ 11 / Reazon Speech v2 Japanese dataset 在 Hugging Face 上的镜像，分发依据 CDLA-Sharing-1.0，使用受限于日本著作权法第30‑4条，包含 4,096 个 16 kHz FLAC 音频文件及对应的 TSV/CSV 格式转录文本。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 5k / ⭐ 121 / Nemotron‑Personas‑Japan 是一个开放源代码、CC BY 4.0 许可证的高质量、合成生成的日本人物资料数据集—包含姓名、性别、年龄、背景、婚姻状况、教育、职业和地点—基于真实世界的人口统计、地理和人格分布，并采用概率图模型和 GPT‑OSS‑120B 进行工程设计，以提升多样性、降低偏见、防止模型崩溃、支持主权 AI 发展，并支持商业使用。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 3k / ⭐ 5 / Japanese JaQuAD，QG‑Bench 的一个子集，提供句子级和段落级的数据，包含高亮的答案词元，用于训练日语问句生成模型，并通过 BLEU4、METEOR、ROUGE‑L、BERTScore 和 MoverScore 进行评估。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 3k / ⭐ 47 / 一个用户友好、去重的 CSV 数据集，包含 Aozora Bunko 的公有域日语文本，使用 globis‑org/aozorabunko‑extractor 处理，并已清理以适用于现代日语机器学习。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 3k / ⭐ 49 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小时匿名 1,033,142 对 eroge 音频-转录配对（主要为女性，含 NSFW），MIT 许可用于学术研究。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 99 / 一个包含100个样本的日语指令微调评估数据集，包含已注释的任务——从摘要校正、数学推理到翻译、创意生成和用户意图理解——旨在对微调模型进行手动或自动的5分制评分。
 * [Lux-Japanese-Speech-Corpus](https://huggingface.co/datasets/Lami/Lux-Japanese-Speech-Corpus) - 📥 2k / ⭐ 5 / 一份日语语音数据集，特色是原始角色“Lux”，包含 96 kHz/16‑bit 原始与清洗后的 WAV 文件、`metadata.csv` 中的转录元数据，以及 `dataset_infos.json` 中的整体数据集信息，按 CC BY 4.0 许可提供用于 TTS 研究和应用。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 2k / ⭐ 7 / JMedBench 是一个日语生物医学 LLM 基准，涵盖 20 个数据集，覆盖五个任务（MCQA、NER、STS 等），来源于 MedMCQA、PubMedQA、MMLU 等，每个都有自己的许可，并包含一条说明：翻译可能包含偏差，需要人工审核。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEB 是一个日本文本嵌入基准，包含 5 个任务（聚类、分类、STS、检索、再排序）和 28 个数据集，提供一行评估脚本，并邀请社区贡献。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 2k / ⭐ 24 / 一份包含 2,300 万本个人收集的日本网络小说的数据库，总计 80.85 亿字符，仅供合法的机器学习使用，并需详细的访问请求。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 2k / ⭐ 141 / Japanese Anime Speech Dataset V2 提供 292,637 条已清洗的音频-文本对——约 397.5 小时的 SFW 内容和 52.4 小时的 NSFW 内容——以 128‑kbps MP3 文件形式按安全级别划分，专为训练自动语音识别模型而设计。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 1k / ⭐ 20 / JMMMU 是一个日语多模态基准，已扩大十倍至 1,320 个具有文化多样性的问题（720 个与文化无关，600 个与文化相关），由母语专家翻译，现在设有公开排行榜。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 1k / ⭐ 18 / Databricks‑dolly‑15k‑ja 数据集是 DeepL 翻译的日本语版 databricks‑dolly‑15k，用于指令调优，由日本 LLM‑jp 项目创建，并由 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 和 Takumi Okamoto 撰写。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 1k / ⭐ 8 / llm‑jp‑instructions 是一个手工整理的日语指令数据集（v1.0），提供训练、验证和测试拆分，可通过 load_dataset 访问。
 * [CAT-Thinking-Dataset](https://huggingface.co/datasets/cyberagent/CAT-Thinking-Dataset) - 📥 1k / ⭐ 2 / 用于训练CAT‑Thinking的数据集：包含日本推理任务的精选子集（如Swallow‑Nemotron、Big‑Math‑RL、DAPO‑Math、rStar‑Coder、AReaL‑boba‑2‑RL‑Code、extraction‑wiki‑ja、magpie），配有轨迹提示和完成，全部授权为CC BY 4.0或Apache 2.0。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 1k / ⭐ 13 / LLM‑jp 提供了一个日语指令调优数据集，该数据集是 DeepL 翻译自 oasst2 的英文子集（来自 kunishou/oasst2‑135k‑ja），并由 Kiyomaru 和 Kodama 编译。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 1k / ⭐ 118 / ReazonSpeech 是一个免费、FLAC 编码的日语语音语料库，附带转录，提供五种规模，从 8.5 h 到 35,000 h，可通过 Hugging Face 下载，遵循 CDLA‑Sharing‑1.0 许可证，且使用受到《日本著作权法》第30‑4条的限制。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 1k / ⭐ 6 / 日本 MC4 数据集卡 (mc4-ja)
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 1k / ⭐ 3 / 从 Hugging Face (if001/oscar_2023_filtered) 加载 312,396 行过滤后的 Oscar 2023 数据集，并在 if001/HojiChar_OSCAR_sample GitHub 仓库中提供示例代码。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 1k / ⭐ 2 / WAON 是一个大型、高质量的日语图文配对数据集，采用尺寸、SigLIP‑score 过滤和去重（按 URL、标题和 pHash）构建，并在 HuggingFace 上以 Apache 2.0 许可证公开，用于信息分析。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 938 / ⭐ 4 / 提供了一个日语搜索/问答数据集，其中包含按查询计算的分数，这些分数是由五个多语言/日语重排序器（例如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）计算的，数据集包括每个查询约200个正例和负例文档的平均分数。
 * [japanese-qa-reasoning-100k](https://huggingface.co/datasets/hotchpotch/japanese-qa-reasoning-100k) - 📥 921 / ⭐ 3 / 使用DeepSeek‑R1从fineweb2‑edu‑japanese文本生成的日语问答数据集，包含问题、关键词和答案以及推理过程，并附有来自原始测试集的样本，按ODC‑BY许可发布。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 900 / ⭐ 89 / 一个自动翻译的日语版本的databricks‑dolly‑15k数据集，许可为CC‑BY‑SA‑3.0，最后更新于2023‑05‑11。
 * [japan-law](https://huggingface.co/datasets/y2lan/japan-law) - 📥 847 / ⭐ 22 / 一份包含日本电子政府法律的数据集，内容包括编号、标题、ID、制定日期、全文，并已去重至截至 2023 年 8 月 1 日的最新生效版本。
 * [Medical-o1-Reasoning-SFT-Japanese](https://huggingface.co/datasets/ronantakizawa/Medical-o1-Reasoning-SFT-Japanese) - 📥 845 / ⭐ 3 / 由GPT‑4o‑mini通过OpenAI批量API生成的FreedomIntelligence医学‑o1‑reasoning‑SFT数据集（19,688条记录）的日语翻译，包含已翻译的问题、思路链推理和答案，以及原始英文文本。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 837 / ⭐ 3 / A 2010 Japanese Web Corpus, uploaded to HuggingFace and licensed for research per the 2009 copyright reform, 包含来自基于形态学的解析和转换脚本的自动标点化文本。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 807 / ⭐ 8 / Rakuda 提供 40 道日语问题——开放式的历史、社会与政府问题，以及针对地理的特定问题——用于对日本 AI 助手进行基准测试，类似于 vicuna‑eval，并且可以使用 `datasets.load_dataset` 加载。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 801 / ⭐ 2 / 18,612 个日语翻译的 Python 指令–响应对——使用 GPT‑4o‑mini 生成，保留原始英文提示、代码和示例——为训练、微调、聊天机器人、研究和教育提供多样化的编码任务，全部遵循 MIT 许可证发布。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 789 / ⭐ 17 / oasst1‑21k‑ja 是由 DeepL 从英文 OASST1 子集派生的日语指令调优数据集，透过日本 LLM‑jp 合作项目创建；请联系 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 和 Okamoto。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 780 / ⭐ 6 / JamC‑QA 是一个双语基准，涵盖八个日本文化与知识类别的多项选择题，排行榜指标用于比较最先进模型。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 779 / ⭐ 2 / Japanese Common Voice 17.0 子集已过滤为 649 个客户端 ID，每个拥有 30–300 个样本，按 8:2 分为训练/验证集，批量为 1,000‑样本 Parquet 文件，总计 45,668 个样本（CC0 许可）。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 769 / ⭐ 57 / AnswerCarefully Dataset提供日语和多语种数据，用于商业或非商业LLM安全增强，禁止任何其他用途——包括安全规避——允许带署名的衍生作品，并声明不承担因伤害或服务变更导致的责任。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 747 / ⭐ 47 / 更新了 JGLUE 数据集卡与加载脚本，适用于由 Yahoo Japan 与早稻田大学创建的日语 NLP 基准，涵盖文本分类（MARC‑ja、JCoLA）、句对分类（JNLI）以及问答（JSQuAD、JCommonsenseQA），发行链接保存在 GitHub 与 Hugging Face 上。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 733 / ⭐ 5 / 来自 Fate/Stay Night 的角色 “Emilia” 的对话和背景故事数据集，格式化用于训练和评估会话语言模型。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 708 / ⭐ 14 / EDINET‑Bench 是一个日本金融基准，用来评估 LLMs 在诸如会计欺诈检测、盈利预测和行业预测等任务，使用十年的 EDINET‑API 披露报告，提供构建和评估代码，并将数据集重新许可为 PDL 1.0。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 682 / ⭐ 7 / 一个量化语音与文本输入在语音语言模型之间智能差距的数据集，由从 Elyza‑tasks‑100、M‑IFEval 与 JamC‑QA 基准生成的音频组成，分为四个子集，文本采用 CC‑BY‑SA 4.0 许可，音频仅限非商业用途且不可再分发。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 645 / ⭐ 5 / 一个受限、非商业派生数据集，基于 EDINET XBRL 财务数据，禁止再分发、AI 训练和商业用途，请求访问需人工批准。
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 621 / ⭐ 4 / Arknights Waifus的JP语音文本数据集：10,905个日语语音片段（总计26.3小时），来自单一角色，适用于微调或评估ASR/ASV模型。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 595 / ⭐ 155 / 日本动漫语音数据集提供73,004对音频-文本（总计110小时，已从V1升级至V5），用于提升ASR模型，例如OpenAI的Whisper，按开放许可证提供给所有使用，欢迎署名。
 * [jaCappella](https://huggingface.co/datasets/jaCappella/jaCappella) - 📥 575 / ⭐ 5 / jaCappella语料库是一个日语无伴奏合唱声乐团数据集，包含六部和弦谱以及各类歌曲的独立音频，涵盖爵士、朋克摇滚、波萨诺瓦、流行、雷鬼、演歌、中性、抒情、EDM 和灵魂/放克等风格。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 566 / ⭐ 3 / 日语指令数据集，具有 632,636 条多轮样本（约 6.35 B 个 token），并包含 GPT‑OSS‑120b 的推理轨迹，用于跨 135 个金融主题和 20 个通用主题的开放式、数学、写作和 MCQA 任务，旨在微调 LLM 在金融领域的推理能力。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 565 / ⭐ 5 / 可供免费下载的81岁日本女性语音语料库（包含原始和去噪 wav、音素/假名+韵律标签），免费学术使用时请注明来源为“Fusic Saoyoshi Voice Corpus”。
 * [OpenSakura-DS-260220-LN-ja-zh-COT-Lilith](https://huggingface.co/datasets/OpenSakura/OpenSakura-DS-260220-LN-ja-zh-COT-Lilith) - 📥 565 / ⭐ 2 / OpenSakura-DS-260220-LN-ja-zh-COT-Lilith 是一个包含1.64百万行的日语到中文轻小说翻译数据集（约18 GB），采用基于映射的5路拆分，保留推理内容和结构化字段，如 uuid、episode 和 segment 索引。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 511 / ⭐ 3 / 日语维基百科句子被转换为各种嵌入和 FAISS 索引，提供 Hugging Face Space 演示、转换脚本，以及对搜索、问答和 OpenAI text-embedding-3-small 在 RAG 中的评估；嵌入模型为 OpenAI‑licensed，其他为 CC‑BY‑SA‑4.0。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 509 / ⭐ 142 / 用于微调 LLMs（如 LoRA）的日语指令聊天数据集，包含 9 M+ 样本，最近已更新，删除授权的 Alpaca 数据，并清理了 Wikipedia 和 ALT 输出，采用 CC‑BY‑SA 4.0 许可证发布。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 503 / ⭐ 27 / WRIME 数据集是一个包含 42,200 条帖子的日本语集合，帖子已为作者、三位读者及其平均值标注了 Plutchik 的八种情感，结构为 40k 训练集、1.2k 验证集和 2k 测试集，用于情感分析任务。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 472 / ⭐ 7 / Japanese Medical VQA 12M 是一个可商业使用的多模态数据集，包含超过 1200 万张日语医学图像和标题，源自 Open‑PMC‑18M，采用 Parquet/Webdataset 格式，并包含原始和日语翻译图像、增强后的标题以及使用 InternVL3.5、Qwen3‑30B 和 GPT‑oss 120B 生成的 VQA 风格问答对。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 445 / ⭐ 13 / ‘wikipedia-ja-20230720’ 日本维基百科快照的数据集卡。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 445 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 数据集的 500 份样本子集，采用 CC BY 4.0 许可，用于基准测试 EvoVLM‑JP‑v1‑7B。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 420 / ⭐ 24 / cc100-ja 是 cc100 数据集日语部分的集合，提供为分片的 Parquet 文件。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 420 / ⭐ 7 / JHumanEval 是 HumanEval 基准的人工翻译日语版本，提供 164 个 Python 编程问题，配有并行的英文和日文注释，用于评估日语 LLM 的代码生成，同时保留原始英文错误。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 401 / ⭐ 7 / Livedoor News Corpus 提供了一个日语新闻文章数据集，划分为 5,894 条训练样本、737 条验证样本和 736 条测试样本，已清除 HTML 标签，并在 Creative Commons Attribution‑NoDerivs 许可证下发布。
 * [JParaCrawl-Filtered-English-Japanese-Parallel-Corpus](https://huggingface.co/datasets/Verah/JParaCrawl-Filtered-English-Japanese-Parallel-Corpus) - 📥 399 / ⭐ 3 / 提供了一个经过清洗的日语-英语翻译语料库，并配备了微调后的 Mistral/Stable‑LM 模型，该模型对每一对进行评估，只接受高质量翻译，拒绝任何不完整、不准确或写得差劲的翻译。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 394 / ⭐ 5 / 数据集卡片详细说明了日语变体 “mc4‑ja‑filter‑ja‑normal”，后续信息正在待补充。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 377 / ⭐ 3 / WildGuardTestJP 是一个包含 1,725 个样本的日语评估数据集，经过多阶段精炼管道（Seed‑X‑PPO‑7B、gpt‑oss‑120b、Qwen2.5‑72B‑Instruct、gemma‑3‑27b‑it）忠实翻译自 WildGuardTest，并以 ODC‑BY 许可证在 Hugging Face 上发布。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 366 / ⭐ 35 / Syosetu711K 是一个约 711,700 本小说的日本数据集，采自 2023 年 3 月 26‑27 日从 小説家になろう 抓取，提供全文及元数据（标题、作者、NCode、简介等），用于无监督文本生成和分类任务。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 365 / ⭐ 4 / 一个266小时的日语音频数据集，来源于Emilia数据集，并通过Scribe v1（ElevenLabs STT/ASR）进行分类，同时使用Facebook音频美学预过滤，可在HuggingFace和Discord上供协作使用。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 355 / ⭐ 34 / 一个时长为409小时的日本 eroge 语音数据集，使用 2-pass loudnorm（‑23 LUFS，‑1 dB 峰值，11 LRA）处理，已由 litagin/anime-whisper 转录、匿名化，存储为 WebDataset（FLAC、JSON、TXT），主要包含女性声音，可能存在 AI 转录错误，并采用 MIT 许可证用于学术研究。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 342 / ⭐ 4 / 包含日语和英语网络语料库的集合——包括一个 9 B‑token 日语集（JA‑WEB‑9B）、63 B‑token 英语和日语集（EN‑WEB‑63B、JA‑WEB‑63B）以及合成版本，如改写版 JA‑PARAPHRASE‑63B、指令式 JA‑INSTRUCT‑63B 和翻译版 JA‑TRANSLATE‑63B——用于在数据受限环境下研究日语 LLM 预训练的数据增强。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 333 / ⭐ 14 / JMMLU 是一个日语大型多任务语言理解基准（Benchmark），包括 7,536 道教师精心制作的问题，覆盖 56 个学科，包括专业医学、心理学、会计、哲学以及各种高中学科。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 330 / ⭐ 9 / 面向 llm‑book/wrime‑sentiment 的数据集卡，提供从 WRIME 派生的二元日语情感分析集，依据 Avg. Readers_Sentiment 标记为正向或负向（可选包含中性案例），用于《大型语言模型导论》一书的示例数据。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 318 / ⭐ 16 / Jagle 是一个约 920 万实例的日本多模态后训练数据集，构建自图像–文本对和 PDF 文本，用于训练 LLM‑jp‑4‑VL 9B beta，并已被证明能提升日语视觉语言任务性能。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 317 / ⭐ 16 / 一份日语和多语种 QA、NLI 与同义句重述数据集的目录，详细说明每个数据集的检索或问答任务及其许可（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 314 / ⭐ 17 / Galgame_Speech_SER_16kHz 是一份 3.7 百万文件（5,353 小时，104 GB）的情感语音数据集，源自 Galgame_Speech_ASR_16kHz，由本地 LLM 注释，按 GNU GPL v3.0 发行，禁止商业使用，并要求基于它训练的模型保持开源且无需强制引用。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 314 / ⭐ 9 / JMMMU‑Pro 是一个通过 Vibe Construction 构建的日语多模态基准——结合生成建模和人工验证——用于生成低成本、高质量的 image‑QA 数据，以揭示开源 LMMs 的缺陷并引领未来 VQA 研究。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/llm-book/ner-wikipedia-dataset) - 📥 310 / ⭐ 4 / 日本命名实体识别数据集“Wikipedia-based Named Entity Extraction”（v2.0），用于书籍 *Large Language Models: An Introduction*，由 Stockmark 创建，并根据 CC‑BY‑SA 3.0 许可发布。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 310 / ⭐ 47 / Galgame_Speech_ASR_16kHz 是一个 16 kHz 的 ASR 数据集，包含 3.75 百万对（≈5,354 小时），源自 Galgame_Dataset，遵循 GPL v3.0，禁止商业使用，并要求任何训练的模型必须开源（可选引证）。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 309 / ⭐ 5 / STAIR‑Captions，发布于2017年，提供820,310条日语字幕，用于字幕生成、多模态检索和图像生成，并配有详细注释、元数据以及Creative Commons BY‑4.0 license。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 298 / ⭐ 3 / 本数据集说明书用于本书《Introduction to Large‑Scale LLM II》中的 ja‑vicuna‑qa‑benchmark，并由 llm‑jp‑eval 创建，供跨数据集日语 LLM 评估使用（Apache 2.0）。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 295 / ⭐ 6 / J-HARD‑TTS‑Eval 对自回归日语 TTS 模型在短序列稳定性、重复处理和上下文完成方面的鲁棒性进行基准测试，数据集可通过 Hugging Face 获得（short, repetition, rhyme, continuation）。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 295 / ⭐ 5 / JAMMEval 是七个日本 VQA 数据集的精炼基准，经过两轮人工注释以消除歧义和非视觉问题，能够为多模态日本任务提供对视觉‑语言模型的可靠评估。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 291 / ⭐ 6 / 数据集简介：“oscar2301‑ja‑filter‑ja‑normal”，是 Oscar 语料库的日语过滤版和普通子集。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 289 / ⭐ 15 / 用于《大型语言模型简介》一书的 JGLUE 数据集数据卡，来源于原始仓库，代码采用 CC BY‑SA 4.0 许可证，数据按发行者的许可协议，引用 Kurihara & Kawahara（日本语），并基于 Shunsuke Kitada 的仓库构建。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 287 / ⭐ 20 / 一个用于评估 Retrieval‑Augmented Generation（RAG）的日语 QA 数据集，由 JAQKET 问题和 Wikipedia 段落以及金标准检索相关性标签构建，并在 HuggingFace 和 GitHub 上发布，主要依据 nDCG@10 评分。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 254 / ⭐ 3 / 一个清理过的日语网络语料库（例如 mc4‑ja），通过无监督学习聚成大约10,000组，可用于合法分析，只在“out”文件夹中列出一些 Parquet 格式的文件，并可通过 Git LFS 下载。
 * [JDocQA-Reasoning](https://huggingface.co/datasets/ricoh-ai/JDocQA-Reasoning) - 📥 253 / ⭐ 5 / 日本的一个基准测试称为 JDocQA Reasoning Bench，由理光（Ricoh）在 GENIAC 项目的一部分中发布，用于评估大规模多模态语言模型在 1,286 个涉及解释图表、表格、图解和真实文档图像中的复杂文本的推理问题上的表现，并通过 LLM‑as‑Judge 系统进行自动评分。
 * [Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k) - 📥 249 / ⭐ 7 / 一个 39,600 样本的日语创意写作数据集，使用 deepseek-ai/DeepSeek-V3-0324 构建，每条记录包含两轮 OpenAI 风格消息（instruction_1/output_1 和 instruction_2/output_2），其中含有一些 NSFW 内容，并在 MIT 许可证下发布。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 244 / ⭐ 12 / JaQuAD 是 2022 年的日语 QA 数据集，包含 39,696 对 SQuAD‑style 的抽取式问题‑答案对，取自 Wikipedia，文件总大小 73.2 MB。使用 BERT‑Japanese 微调时，获得 78.92 % F1（63.38 % EM）。
 * [Umamusume-voice-transcription](https://huggingface.co/datasets/TLME/Umamusume-voice-transcription) - 📥 232 / ⭐ 8 / Umamusume‑voice‑transcription 是一个包含 77 个字符的数据集，提供每匹赛马角色的转录文件，并列出其总音频时长（以秒计）（例如，“东商变革” 799 s，“北部玄驹” 1128 s）。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 231 / ⭐ 3 / 一份包含 64,139 条标注有生物性别的日语姓名的数据集，呈现为汉字、假名和平罗马字，其 44.9k 训练集、6.41k 验证集和 12.8k 测试集划分已在 ISDA’23 被接受。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 230 / ⭐ 2 / JCommonsenseQA 是一份日语的多项选择常识推理数据集——CommonsenseQA 的改编版本——其授权为 CC BY‑SA 4.0，并以 doi:10.5715/jnlp.30.63 引用。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 229 / ⭐ 9 / JSICK 是一个日英 NLI 和 STS 数据集，基于翻译 SICK 语料库创建，包含一个压力测试集合，用以检验词序和格助词处理，共有 1,666、797 与 1,006 对句子用于不同的语法关系。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 226 / ⭐ 5 / 从 CC‑100、OSCAR‑2301、HPLT v1.2 和 wiki40b‑ja 提取的 5.6 B-token 日英代码数据集，用于预训练 Contrail‑200m‑64k，适用于 LOCAL AI HACKATHON #000 “calm2-chat”，但缺少句子边界和困惑度过滤。
 * [OpenAI-MRCR-Translation-JPN](https://huggingface.co/datasets/abeja/OpenAI-MRCR-Translation-JPN) - 📥 223 / ⭐ 2 / 一个日语评估数据集，采用LLMs将OpenAI的长上下文MRCR翻译而来，保留原有结构，同时生成新的助手回复，并保持MIT许可。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 219 / ⭐ 22 / AI生成的动漫插图，使用英文提示，并基于Phi‑3 Vision的字幕（英文和日文），已发布到公共领域，供免费使用。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 215 / ⭐ 5 / 20,800 文件的 WAV 数据集，包含 195 位日本 AItuber 人格——包括参考、原始、描述性和情感性发言，并提供详细的人格和声音元数据，准备通过数据科学 APIs 检索。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 204 / ⭐ 33 / 通过发布数据集、自动评估框架以及 Claude 3.5‑Sonnet、GPT‑4o 等模型的比较结果，提供跨金融、电信、制造、公共、零售五个行业领域的日语 RAG 基准。
 * [ScreenTalk_JA2ZH-XS](https://huggingface.co/datasets/Itbanque/ScreenTalk_JA2ZH-XS) - 📥 201 / ⭐ 3 / 10,000 份配对数据集，约30小时的日语音频与对应的简体中文文本，以 Parquet 格式存储（CC BY 4.0），专为语音转文字翻译和多语言 ASR+MT 研究设计。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 198 / ⭐ 2 / 由重述过的维基百科文本生成的LLM生成的日语查询和答案的数据集，采用CC‑BY‑SA 4.0发布。
 * [swallow-magpie-ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1) - 📥 185 / ⭐ 5 / 一套日英指令调优数据集（每类 42k 对），作为 Swallow‑Magpie‑Ultra‑v0.1 的一部分发布，用于训练 tokyotech‑llm 模型，来源于 magpie‑ultra‑v0.1，并具有平均良好的质量。
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 176 / ⭐ 3 / 使用 Whisper Large‑V2 从视频中转录了牧瀬红莉栖的视觉小说对话，随后用 pydub 进行拆分；未经清理的文本用于 TTS 模型训练（版权未归属）。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 175 / ⭐ 33 / 适用于指令-响应微调（如使用 LoRA）的日语聊天数据集，来源于 llm‑japanese‑dataset，去除日英翻译示例，提供 1.8–2.5 百万条条目，覆盖各版本发布，并以 CC‑BY‑SA 4.0 许可发行，引用 DOI 10.1109/BigData59044.2023.10386605。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 175 / ⭐ 10 / 一份将 llm‑jp‑corpus‑v3 的 kaken 子集译为日英的日英平行语料库，使用 Qwen/Qwen2.5‑32B‑Instruct，包含自定义翻译列，并在 CC‑BY‑4.0 许可下授权。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 169 / ⭐ 2 / 一个多模态日语表格问答数据集，用于直接从年度证券报告表格中提取单元格值，提供图像、带边界框的 OCR 文本、问题和答案，并遵循 CC‑BY‑4.0 许可。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 169 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) 提供了一个多分类 QA 数据集——涵盖 Integration、Reasoning、Logical、Table 和 Abstention——旨在评估日本 RAG 生成器，采用人工努力和 GPT‑4.1 构建，并在 CC BY‑SA 4.0 许可下发布。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 168 / ⭐ 18 / 一份 NLP‑ready dataset，包含从 2024 年 1 月的 HTML dump 中提取的 Wikipedia articles，保留段落结构、元数据（如 disambiguation、sexual、violent flags、templates、timestamps）以及托管在 GitHub 上的 extraction scripts。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 163 / ⭐ 6 / Range3 的 wikipedia‑ja‑20230101 仓库提供只包含日语维基百科文本的 Parquet 文件，这些文件是从完整维基百科数据集中提取的，并使用 Python 代码生成。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 154 / ⭐ 26 / 此仓库托管了 OpenAssistant/oasst1 数据集的日语翻译，包括带有错误标记的自动翻译条目，大约 2,000 条人工修正，一个基于聊天格式的子集，以及将数据转换为用于微调的指令-输出对的脚本。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 148 / ⭐ 2 / COVID‑19 日本推特数据集提供了日本推文 ID 与评估码（63–68），用于标识 COVID‑19 相关性以及事实/观点状态，从而支持文本分类研究。
 * [DEJIMA-dataset](https://huggingface.co/datasets/MIL-UT/DEJIMA-dataset) - 📥 148 / ⭐ 4 / 一份日本规模的网络数据集，包含388万张图像、LLM生成的标题和开放式问答对，已去重并添加检测标签，可提供多种变体（simple、refined、detection、all），并托管在 Hugging Face。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 147 / ⭐ 21 / 用于日英文本简化和翻译的 SNOW T15/T23 日语简化语料库数据卡，包含 50 k 条手工对齐的原文、简化日语（≤2 k‑词汇量）和英语翻译记录，以及 35 k 条扩展集。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 144 / ⭐ 4 / 郭等人对Wiki40B数据集中的日语部分进行了重排。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 140 / ⭐ 15 / 一个用于测试角色‑LLMs的简单 Zundamon 角色设定数据集——由线上来源和管理数据编制——以 zmnjp.jsonl 和 zmn.jsonl 格式提供，并在指定许可下发布。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 137 / ⭐ 10 / JA‑Multi‑Image‑VQA 是一个包含 39 张图像、55 道题目的数据集，其中包含手工制作的日语问答，适用于多图像 VQA，通过 load_dataset 访问，文本部分采用 Apache 2.0 许可（图像受限）。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 137 / ⭐ 7 / 将日语数据集重新格式化为适合 SentenceTransformers 的列和结构，并根据 RelRank 分数从多个 HuggingFace 来源过滤成正样本（≥0.7）和负样本（≤0.3）的对，用于对比学习。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 132 / ⭐ 6 / Japanese XL‑Sum subset 通过 PaLM‑2 15-gram 重叠过滤，包含 4,215 训练样本，758 验证样本和 766 测试样本。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 131 / ⭐ 5 / JAQKET 是一个基于维基百科的日语开放域问答数据集，提供 1.0 版包含多项选择测验题（13,061 条训练样本，271 条验证样本）以及 2.0 版仅包含需要提取答案的提问提示（2,154 条训练样本，1,164 条验证样本），旨在促进问答系统研究。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 129 / ⭐ 16 / Hachi‑Alpaca 是一个由 Stanford Alpaca 使用 ‑mistralai/Mixtral‑8x22B‑Instruct‑v0.1 生成的日本合成数据集，经过该模型清洗，在 Deepinfra 上提供服务，并以 Apache‑2.0 许可证发布，供 Alpaca‑jp 研究使用。
 * [japanese-confidential-information-extraction-sft](https://huggingface.co/datasets/akiFQC/japanese-confidential-information-extraction-sft) - 📥 127 / ⭐ 2 / 一份用于从文本中提取11类机密实体的日语 SFT 数据集，专为 LFM2 模型的 LoRA 微调而设计，包含 40,897 条样本，划分为训练/验证集合，并输出包含所有键的 JSON（缺失时为空列表）。
 * [pjsk-emu-dataset](https://huggingface.co/datasets/chitsanfei/pjsk-emu-dataset) - 📥 126 / ⭐ 11 / 2735 文件 WAV 声音数据集，适用于 so‑vits‑svc 4.0，按 CC‑BY‑NC 4.0 许可授权，仅限科研使用，需通过电子邮件申请获取。
 * [danbooru-ja-tag-pair-20241015](https://huggingface.co/datasets/p1atdev/danbooru-ja-tag-pair-20241015) - 📥 124 / ⭐ 9 / 一个包含150K条目的Danbooru标签与日语翻译配对的数据集（截至2024年10月15日更新），基于扩展的wiki源构建，使用FastText过滤以移除非日语标签，并通过少量示例Calam Chat翻译完成缺失条目。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 123 / ⭐ 2 / 一个日语在线广告数据集，包含五个 NLP 任务——ad acceptability、consistency、performance estimation、A3 recognition 和 similarity，并以 TSV 格式提供 train/dev/test 拆分。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 119 / ⭐ 13 / 日本角色扮演对话数据集，过滤后仅包含足够长度的多发布者记录、标准化的发布者名称和均衡的主要发言者，旨在用于机器学习应用。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 117 / ⭐ 24 / AutoWikiQA 是最大的免费日语问答数据集，提供超过 230 万个手工过滤的问答对，这些对是使用 Swallow‑MX 和 LLMs（不使用基于规则的模板）从维基百科自动生成的，用于支持知识教学和检索增强生成应用。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 116 / ⭐ 4 / 包含问题、答案以及逐步推导链接至 Wikipedia 文章的日本 Explainable Multi-hop Question Answering 数据集，已更新推导格式并发布多个版本。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 115 / ⭐ 3 / BBH‑ja提供了BIG‑Bench Hard数据集的日语翻译，提供JSON‑L（输入、正确目标）格式的评估问题以及使用PLaMo模型翻译的YAML（输入、目标）格式的Chain‑of‑Thought提示。
 * [sakura_japanese_dataset](https://huggingface.co/datasets/saldra/sakura_japanese_dataset) - 📥 114 / ⭐ 20 / Sakura_dataset 是一个商业级、超小型、高质量的日语数据集，涵盖常识问答、数学题（Calc‑ape210k）和自定义日语常识问题，按 DbCL v1.0 许可，并可与如 rinna/japanese‑gpt‑neox‑3.6b 等模型的 LoRA 微调一起使用。
 * [med-slm-ja-before-after](https://huggingface.co/datasets/genshiai-daichi/med-slm-ja-before-after) - 📥 113 / ⭐ 2 / 一个包含 46,705 项变更的数据集，涉及 201 份日本医学指南（2010‑2024），按修订、添加、新概念和无关项目分类，并为每项变更提供来源引用。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 112 / ⭐ 82 / 一份日本网络小说章节数据集，配有英文粉丝翻译，在版本 2 中扩展到 106K 条对齐句子，包含系列元数据，无质量过滤，并在公平使用/Apache 2.0 下分发，同时提供下架条款。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 107 / ⭐ 4 / 一个来自 livedoor News Corpus 的日语命名实体识别数据集——在书籍 *大規模言語モデル入門* 中使用，并由 RONWIT 提供——包含经过清理的 HTML 文章，采用 CC BY‑ND 2.1 JP 许可证。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 105 / ⭐ 2 / KokoroChat 是最大的日本心理咨询对话数据集——由 480 名受过训练的辅导员进行 6,589 次角色扮演会话，每次平均 91 条发言——包含丰富、长篇对话，详细的 20 维客户反馈，并支持同理响应生成、对话评估和心理健康语言建模方面的研究，并已被 ACL 2025 接收。
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 104 / ⭐ 24 / RealPersonaChat 是一个约14,000条日本对话语料库，包含会话数据、说话者人物设定和大五人格特质，以及评估分数和人口统计属性，并提醒不要用于重新识别或冒充。
 * [alpaca_jp_python](https://huggingface.co/datasets/HachiML/alpaca_jp_python) - 📥 103 / ⭐ 8 / 使用mistralai/Mixtral‑8x22B‑Instruct‑v0.1生成的合成日语Alpaca数据集，并通过Deepinfra进行细化，作为HachiML项目的一部分，以Apache 2.0许可证发布。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 102 / ⭐ 22 / 一个名为MOMIJI的日语网页文档和图像数据集（≈5600万页，1100亿字符，2.49亿张图片），旨在训练视觉语言模型，并配有交互式可视化工具和用于生成文本字段的实用脚本。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 101 / ⭐ 11 / 一个大型的基于日语PDF的问答数据集（JDocQA），包含5 504份文档和11 600个带注释的四类问题–答案对：是/否、事实性、数值型以及开放式，包含图片、不可回答示例，并划分为训练/验证/测试集。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 101 / ⭐ 5 / 日本动漫语音数据集，原始 joujiboi/japanese‑anime‑speech‑v2 集合的拆分版本。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 101 / ⭐ 11 / 一个高质量的合成日语数学题数据集，具有经过验证的思考链推理，采用 Qwen2‑7B‑Instruct 翻译 PRM800K 和 GSM8K 并进行正确性筛选后构建，可通过 Hugging Face 数据集库获取。
