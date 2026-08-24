# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专门收录日语NLP相关的Python库、LLM、词典和语料库资源的精选列表。
本页面列出了Hugging Face上可用的日语NLP专用模型和数据集。目前包含213个模型和155个数据集。

_更新于2026年8月24日_

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

| # | 模型名称 | Downloads | Likes | 类别 |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 9M | ⭐ 62 | automatic-speech-recognition |
| 2 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 659k | ⭐ 178 | image-to-text |
| 3 | [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) | 📥 549k | ⭐ 11 | automatic-speech-recognition |
| 4 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 517k | ⭐ 15 | text-generation |
| 5 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 505k | ⭐ 9 | fill-mask |
| 6 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 501k | ⭐ 17 | translation |
| 7 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 436k | ⭐ 81 | sentence-similarity |
| 8 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 352k | ⭐ 76 | fill-mask |
| 9 | [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) | 📥 325k | ⭐ 15 | text-ranking |
| 10 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 269k | ⭐ 10 | sentence-similarity |
| 11 | [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) | 📥 221k | ⭐ 24 | sentence-similarity |
| 12 | [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) | 📥 216k | ⭐ 56 | feature-extraction |
| 13 | [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) | 📥 198k | ⭐ 51 | feature-extraction |
| 14 | [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) | 📥 187k | ⭐ 5 | feature-extraction |
| 15 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 144k | ⭐ 42 | fill-mask |
| 16 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 137k | ⭐ 15 | translation |
| 17 | [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) | 📥 133k | ⭐ 64 | others |
| 18 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 132k | ⭐ 11 | others |
| 19 | [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) | 📥 125k | ⭐ 38 | sentence-similarity |
| 20 | [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) | 📥 119k | ⭐ 51 | fill-mask |

### Datasets-ranking

| # | 数据集名称 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 4M | ⭐ 75 |
| 2 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 12k | ⭐ 7 |
| 3 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 7k | ⭐ 34 |
| 4 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 4k | ⭐ 9 |
| 5 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 4k | ⭐ 126 |
| 6 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 3k | ⭐ 36 |
| 7 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 3k | ⭐ 19 |
| 8 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 2k | ⭐ 47 |
| 9 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 101 |
| 10 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 2k | ⭐ 7 |
| 11 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 2k | ⭐ 47 |
| 12 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 2k | ⭐ 7 |
| 13 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 2k | ⭐ 6 |
| 14 | [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) | 📥 1k | ⭐ 2 |
| 15 | [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) | 📥 1k | ⭐ 5 |
| 16 | [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) | 📥 1k | ⭐ 5 |
| 17 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 1k | ⭐ 12 |
| 18 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 1k | ⭐ 146 |
| 19 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 1k | ⭐ 49 |
| 20 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 1k | ⭐ 16 |

## Models
### text-generation
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 517k / ⭐ 15 / 一个 12 层、768 隐藏层的日语 GPT‑NeoX 模型，训练数据为 CC‑100、C4 以及 Wikipedia，兼容 Huggingface，并配备可选的玩具前缀调优权重，能强制每个句子末尾以笑脸表情符号结束。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 105k / ⭐ 19 / Llama 3.1 Swallow 是一组 8‑B 和 70‑B 模型，它们继续对 Meta 的 Llama 3.1 进行预训练，以提升日语语言性能，然后在合成日语数据上进行指令微调，提供多种已发布的变体，其对话行为已改进，与 gemma‑3‑27b‑it 相当。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 78k / ⭐ 59 / 一款由 ABEJA Inc. 使用日语 CC‑100 和 OSCAR 训练的 2.7B 参数日语 GPT‑NeoX 模型，可通过 Hugging Face Transformers 管道或 PyTorch 使用，按 MIT 许可证发布。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 75k / ⭐ 8 / LLM‑jp‑3‑150m——来自国立信息学研究所LLM研发中心的150 M参数日语语言模型——以 Hugging Face Transformers 格式发布，需要 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，并且在日本维基百科、Common Crawl、WARP/PDF、WARP/HTML 和 Kaken 数据上使用 unigram byte‑fallback tokenizer 进行预训练。
 * [Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4) - 📥 49k / ⭐ 2 / 在 Qwen3‑Swallow v0.2 中的中日双语 LLM（30B‑A3B / 32B）通过 CPT、SFT 和 RLVR 进行训练，以保持数学和编码表现、提升推理能力，并已在 Hugging Face 上发布数个量化版本。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 45k / ⭐ 21 / OpenCALM 是 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 许可证下发布的一套仅解码的日本 transformer 语言模型（160 M–6.8 B 参数），训练于 Japanese Wikipedia 和 Common Crawl，并可通过 Hugging Face’s torch‑transformers 使用。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 38k / ⭐ 16 / SB Intuitions的 Sarashina2.2‑0.5B instruct v0.1 是一个拥有5亿参数的日语自回归模型，在日语和英语 MT 基准上表现良好，并已准备好通过 torch‑transformers 加载。
 * [LFM2.5-1.2B-JP-202606](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606) - 📥 21k / ⭐ 75 / LFM 2.5-1.2B-JP-202606 是一款高性能、通用的日语聊天模型，在知识、指令遵循、数学、代码和工具使用方面优于同类不到 2 B 的模型，使其成为开发者构建具有文化细腻度的日语应用程序的理想选择。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 14k / ⭐ 18 / 使用 Shisa 7B 数据，微调了日语 Stable LM Base Gamma 7B，在 JA MT‑Bench 上取得了强劲的表现。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 12k / ⭐ 3 / Qwen3‑Swallow v0.2 提供了 30‑B 和 32‑B 双语日英 LLM，采用 CPT、SFT 与 RLVR 训练，提升日语准确性、翻译、数学与编码能力，以匹配或超越原始 Qwen3，提供九个模型（CPT、SFT、RL）和 AWQ‑quantized 版本，同时发布 GPT‑OSS‑Swallow。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 9k / ⭐ 12 / llm‑jp‑4‑8b‑instruct 是 NII 的 LLM‑jp‑4 系列 4.1 B 参数的日语 LLM，先在大型语料库上预训练，随后仅使用监督指令数据进行微调（不使用 DPO/REINFORCE），并附带类似食谱的使用指南和 byte‑fallback unigram tokenizer。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 9k / ⭐ 21 / Llama3 Swallow 是 Meta Llama 3 系列的日语增强版本，于 2024 年 7 月 1 日发布，提供 8B 与 70B 版本的 Instruct 与 chat 模式，已在 Megatron‑LM 上使用 SFT 与 Chat Vector 进行微调，并在关键的日语 NLP 任务上进行了基准测试。
 * [LFM2.5-1.2B-JP-202606-ONNX](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-ONNX) - 📥 8k / ⭐ 6 / 将日本 LFM2.5‑1.2B 模型导出为 ONNX，以便在跨平台推理中使用 ONNX Runtime、Transformers.js 和 WebGPU，提供多种精度变体（FP32、FP16、INT4/FP16 混合）以及推荐的 WebGPU 友好 INT4+FP16 格式。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 实验性日语模型通过使用聊天向量方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 与 Meta‑Llama‑3‑8B‑Instruct 之间的差异创建，然后上采样并应用于 Meta‑Llama‑3‑70B‑Instruct，显示出变化不大，并计划未来扩大规模。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 8k / ⭐ 17 / 来自 NII 研发中心的日本大型语言模型集合（1.8 b 至 172 b beta1，含 instruct 版本），以 Hugging Face Transformers 格式打包，并在混合日语、英语与网络语料库（总计>1万亿个标记）上预训练。需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29 以及 flash‑attn ≥ 2.5。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 7k / ⭐ 150 / Llama‑3‑ELYZA‑JP‑8B 是由 ELYZA 开发的、经过日语增强的 80 亿参数 Llama 3 模型，在 Meta‑Llama‑3‑8B‑Instruct 上针对日语微调。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 7k / ⭐ 39 / 提供了一款来自 SB Intuitions 的自回归式日语语言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已与其他模型进行基准测试，并附示例使用脚本，且安全训练有限。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 6k / ⭐ 46 / 提供来自 NII 的 8 B 参数 LLM‑jp‑4‑8b‑thinking 日语语言模型，使用 pre‑/mid‑training 训练并通过 SFT/DPO 对齐，已准备好与 torch‑transformers 一起使用，并附有详细的教程说明。
 * [asmr-qwen3.5-9b-zh-cn-echo-mtp-gguf-v0.1](https://huggingface.co/mmis1000/asmr-qwen3.5-9b-zh-cn-echo-mtp-gguf-v0.1) - 📥 6k / ⭐ 2 / Fine‑tuned Qwen3.5 MTP 在 GGUF 格式下，能够将日语 ASMR 转录翻译为简体中文，同时回声原文、应用领域术语表，并通过多种量化版本（q4_k_m, q6_k, q8_0, bf16）保留情感。
 * [DeepSeek-R1-Distill-Qwen-32B-Japanese](https://huggingface.co/cyberagent/DeepSeek-R1-Distill-Qwen-32B-Japanese) - 📥 5k / ⭐ 254 / 一个使用日本微调的 DeepSeek‑R1‑Distill‑Qwen‑32B 模型（MIT‑licensed）用于通过 transformers 生成文本，采用自定义 prompt 格式并支持 streaming 输出。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 5k / ⭐ 10 / 仓库提供 GGUF 格式、量化的模型文件，适用于 Stability AI 的日本版 StableLM Instruct Gamma 7B，由 Massed Compute 硬件创建，并且是 TheBloke 的 a16z‑资助 LLM 工作的一部分。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking-gguf) - 📥 5k / ⭐ 7 / NII的LLM研发中心推出的大型语言模型 llm-jp-4-32b-a3b-thinking-gguf 提供32 B参数，采用预训练/中期训练加SFT/DPO（或仅SFT用于指令版），并通过cookbook提供使用指南。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 5k / ⭐ 85 / Rinna 的 24 层、1024 隐藏单元的日语 GPT‑2‑medium 模型，基于 CC‑100 和维基百科训练，采用 SentencePiece 分词，已在 rinna/japanese‑pretrained‑models 仓库公开（MIT 许可证，2021 年 4 月 7 日发布，2021 年 8 月 25 日更新）。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 5k / ⭐ 24 / Llama 3.1 Swallow 是一系列日语增强的 8B/70B Llama 3.1 模型，通过持续预训练和日语特定指令微调训练，最新的 8B‑Instruct‑v0.3 在日语 MT‑Bench 上取得了最先进的结果。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 4k / ⭐ 13 / Qwen3‑Swallow v0.2 提供了通过 CPT、SFT 和 RLVR 训练的日英 LLM（30B‑A3B 和 32B），保持了强大的数学、编码和推理能力，已发布九个模型以及 AWQ 量化版本。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 4k / ⭐ 7 / 一个存储库，托管来自国立信息研究所LLM研发中心的8.6 B参数llm‑jp‑4‑8b‑base transformer，采用预训练和中间训练，随后进行监督微调和直接偏好优化（不使用强化学习），并提供PyTorch‑transformers使用指南。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 4k / ⭐ 141 / 9亿参数的日语优化LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，训练数据截至2024年9月，采用混合 Mamba‑2/MLP/4‑层注意力架构，已在 Nemotron‑Personas‑Japan 工具调用数据集上微调，可选地在生成最终答案前生成可控的推理轨迹，且可商用。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 4k / ⭐ 153 / LFM2.5‑1.2B‑JP 是一款针对日语优化的聊天模型，在日语知识与指令遵循方面优于 LFM2，支持使用 LoRA 进行微调，支持通过 Transformers、vLLM 和 llama.cpp 进行推理，取得 50.7 JMMLU、58.1 M‑IFEval 与 56.0 GSM8K 分数。
 * [llm-jp-3-440m](https://huggingface.co/llm-jp/llm-jp-3-440m) - 📥 4k / ⭐ 1 / LLM‑jp‑3‑440m 是一个兼容 Hugging Face 的日语 Transformer 模型（44 亿参数），来自 NII 的 LLM‑jp‑3 系列，预训练于约 1 万亿个 token，并且需要 torch ≥2.3.0、transformers ≥4.40.1、accelerate ≥0.29.3 和 flash‑attn ≥2.5.8。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 4k / ⭐ 28 / rinna 的日语 GPT‑2 small 是一个 12 层、768 维隐藏层的 Transformer，训练于日语 CC‑100 和 Wikipedia，使用 SentencePiece 进行分词，发布于 2021 年 8 月 25 日，遵循 MIT 协议（Hugging Face: rinna/japanese‑gpt2‑small，参见 https://arxiv.org/abs/2404.01657）。
 * [Qwen3-Swallow-8B-CPT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2) - 📥 4k / ⭐ 1 / 双语 30 B‑和 32 B‑参数 LLMs，Qwen3‑Swallow v0.2，采用 CPT、SFT 和 RLVR 构建，擅长日语、日英翻译、数学和编码，匹配或超越 Qwen3，并以 AWQ‑量化形式在 Hugging Face 上发布。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/ash2813/llm-jp-4-32b-a3b-thinking-gguf) - 📥 3k / ⭐ 3 / 提供一个 Q4_K_M GGUF‑量化版本的 llm‑jp/llm‑jp‑4‑32b‑a3b‑thinking 日语模型，该模型使用与 llm‑jp‑corpus‑v4 校准的 importance‑matrix，保持其学术领域性能，同时提供校准数据、swap‑shard 脚本和可选 f16 片段。
 * [japanese-stablelm-instruct-beta-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-7B-GGUF) - 📥 3k / ⭐ 1 / Repo托管 GGUF 格式的 7B 日语 StableLM Instruct Beta 模型，采用 Massed Compute 硬件进行量化，已可用于 llama.cpp 和流行 AI UI 框架。
 * [Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF) - 📥 3k / ⭐ 2 / 面向日语、低位 GGUF 量化的 Qwen 3.5‑35B‑A3B 模型，使用基于日语文本校准的重要性矩阵，并减少安全过滤器，建议使用提供的 .GGUF 文件。
 * [llm-jp-4-33b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-33b-thinking-gguf) - 📥 3k / ⭐ 7 / LLM‑jp‑4‑33b‑thinking‑gguf 是日本国立信息学研究所的 33 B 日语语言模型，已使用 SFT 和 DPO（无 RL）预训练，可通过 LLM‑jp fork 在 llama.cpp 上使用，并在其 cookbook 中提供详细使用说明。
 * [Llama-3.1-Swallow-8B-Instruct-v0.2](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.2) - 📥 3k / ⭐ 16 / 日本增强版Llama 3.1语言模型（8B和70B）通过在Meta基础模型上持续预训练和指令微调构建，作为Llama‑3.1‑Swallow‑v0.x及Instruct变体以日语为中心的数据发布。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking-gguf) - 📥 3k / ⭐ 15 / LLM‑jp‑4‑8b‑thinking‑gguf 是日本信息学研究所（≈8 B 参数）的日语大型语言模型，使用中训练进行预训练，并通过监督学习和直接偏好优化对“思考”变体进行微调，可在 GGUF 格式下获取，并在食谱中提供详细的使用说明。
 * [japanese-stablelm-instruct-beta-70B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-70B-GGUF) - 📥 3k / ⭐ 12 / 提供了用于Stability AI的70亿参数日语StableLM Instruct Beta的GGUF格式、硬件量化模型文件，已准备好与LLaMA‑cpp基于工具一起使用。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 3k / ⭐ 37 / 32亿参数的日语 Transformer LLM（llm‑jp‑4‑32b‑a3b‑thinking）来自国立信息学研究所，预训练和校准通过有监督微调和直接偏好优化完成——不使用强化学习——使用unigram byte‑fallback tokenizer。
 * [jinen-v1.1-beta.gguf](https://huggingface.co/togatogah/jinen-v1.1-beta.gguf) - 📥 3k / ⭐ 1 / 一个 GGUF 格式的“jinen”（v1.1‑beta）日语假名-汉字转换模型原型，针对 NFKC 规范化提示进行了优化，在 AJIMEE‑Bench 上基准测试显示 Accuracy@1 为 80%，并支持多种量化（f16、Q8_0、Q5_K_M、Q4_K_M）。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 2k / ⭐ 25 / 与 Hugging Face 兼容的日语中心 transformer 模型（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct）来自国立信息学研究所，在包含 Wikipedia、Common Crawl、WARP、Kaken、Dolma 在内的多种日语和英语语料库上预训练，并要求 torch ≥ 2.3、transformers ≥ 4.40、accelerate 与 flash‑attn。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 2k / ⭐ 17 / TokyoTech‑LLM 仓库提供了经过日本数据增强的 Swallow Llama‑2 系列 LLaMA‑2 模型，涵盖 7B、13B 和 70B 变体，其中包括 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以来发布的 7B Plus 版本。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 58 / TinySwallow‑1.5B‑Instruct 是一个 1.5 B 的日语指令调优自回归语言模型，使用 TAID 从 Qwen2.5‑32B‑Instruct 进行蒸馏，供研究用途。
 * [aibuncho-japanese-novel-gpt-j-6b-gguf](https://huggingface.co/mmnga/aibuncho-japanese-novel-gpt-j-6b-gguf) - 📥 2k / ⭐ 4 / 将日语小说 GPT‑J‑6B 转换为 GGUF 以供 llama.cpp（分支 mmnga‑dev）使用，已提供使用示例，但请注意，当 llama.cpp 引入本地 gptneox 或 gpt2 支持时，它可能会变得不兼容。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 2k / ⭐ 35 / LFM2.5‑1.2B‑JP 是一个 1.2 B 参数的日语文本生成模型，基于 LFM2.5 混合架构构建，优化用于生成和完成任务，托管在 Hugging Face 上，并可通过 llama.cpp 运行。
 * [LFM2.5-1.2B-JP-202606-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-202606-GGUF) - 📥 2k / ⭐ 27 / 液体AI的混合 LFM2 模型，例如 1.2 B 日语 GGUF 版本，提供高质量、快速且内存高效的边缘 AI，用于设备端部署，并可通过 Hugging Face 仓库使用 llama.cpp 本地运行。
 * [Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF) - 📥 2k / ⭐ 2 / 针对日语的 imatrix GGUF 量化版本，应用于已被消融的 Qwen3.6‑35B‑A3B‑uncensored‑heretic 模型，并用日语文本校准以提升日语生成质量，但安全过滤器显著减弱。
 * [llm-jp-4-33b-thinking](https://huggingface.co/llm-jp/llm-jp-4-33b-thinking) - 📥 2k / ⭐ 35 / 仓库托管了来自 NII 的 LLM 研究中心的 llm‑jp‑4‑33b‑thinking 33 B 参数 Transformer 模型，经过监督和偏好优化微调，并附有实用使用指南。
 * [ELYZA-japanese-Llama-2-13b-fast-instruct-GGUF](https://huggingface.co/second-state/ELYZA-japanese-Llama-2-13b-fast-instruct-GGUF) - 📥 2k / ⭐ 1 / 量化的日本 LLaMA‑2‑13B 快速指令模型（多种 GGUF 格式），供 LlamaEdge v0.2.8+ 使用，提供不同大小–质量权衡以及命令行或 wasm API 示例。
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 2k / ⭐ 12 / 东京科技-LLM（TokyoTech‑LLM）基于 LLaMA‑2，并通过日语数据（SFT）微调，包含 Swallow‑7b/13b/70b 变体及其 instruct、NVE 和 “plus” 版本，发布时间从2023年12月到2024年4月。
 * [japanese-stablelm-base-beta-70B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-base-beta-70B-GGUF) - 📥 2k / ⭐ 2 / 提供由 Stability AI（使用 Massed Compute 硬件生成）的 GGUF 量化 70 B 日语 StableLM Base Beta 模型文件，以及 a16z 捐赠、TheBloke 的 Discord、Patreon 和兼容的 UI 与库链接，例如 text-generation-webui、KoboldCpp、LM Studio、LoLLMS、Faraday.dev、ctransformers 和 llama‑cpp‑python。
 * [Lumi-v2-llm-jp-4-8b](https://huggingface.co/SousiOmine/Lumi-v2-llm-jp-4-8b) - 📥 2k / ⭐ 1 / Lumi‑v2‑llm‑jp‑4‑8b 是基于 ChatML 模板的 SFT，针对 llm‑jp/llm‑jp‑4‑8b‑base 进行微调，训练数据约为 1.7 B 个 token，来源包括 NVIDIA 的 Nemotron SFT 集合、Open‑SWE Traces、NRI‑AI 财务推理以及 OpenResearcher 数据。
 * [Wanabi-Gemma4-31B-GGUF](https://huggingface.co/kawaimasa/Wanabi-Gemma4-31B-GGUF) - 📥 2k / ⭐ 8 / 一款针对Project Wannabe结构化提示格式和日语创意写作优化的 Google Gemma 4 31B 的精调 GGUF 版本，同时保留通用对话与推理能力，适用于多种聊天 UI。
 * [zenz-v2.5-medium](https://huggingface.co/Miwa-Keita/zenz-v2.5-medium) - 📥 1k / ⭐ 10 / 基于 GPT‑2 的条件语言模型（zenz‑v2.5），专为假名-汉字转换而设计，提供三种尺寸（310 M、91 M、26 M）。它使用字符+字节 BPE 分词器，并在 zenz‑v2.5‑dataset 上训练，以实现高性能、上下文感知的转换。
 * [llm-jp-3-13b-instruct](https://huggingface.co/llm-jp/llm-jp-3-13b-instruct) - 📥 1k / ⭐ 30 / 来自国立信息学研究所 LLM 研发中心的 Large language models（llm‑jp‑3‑1.8b、3‑3.7b、3‑13b 和 beta 3‑172b）以 Hugging Face Transformers 检查点形式发布，要求 torch≥2.3.0、transformers≥4.40.1、accelerate≥0.29.3、flash‑attn≥2.5.8，并在日本维基百科、Common Crawl、WARP/PDF/HTML、Kaken、英文维基百科和 Dolma 数据集的混合上训练。
 * [ABEJA-Qwen2.5-32b-Japanese-v1.0](https://huggingface.co/abeja/ABEJA-Qwen2.5-32b-Japanese-v1.0) - 📥 1k / ⭐ 6 / 一款专注于日语的 Qwen 2.5‑32B 模型，基于 abeja/ABEJA‑Qwen2.5-32b-Japanese‑v0.1 通过 SFT 和 DPO 微调后发布为 ABEJA‑Qwen2.5‑32b‑Japanese‑v1.0。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 1k / ⭐ 49 / 一款日本持续预训练的 Mistral‑Nemo 模型（Mistral‑Nemo‑Japanese‑Instruct‑2408），基于 mistralai/Mistral‑Nemo‑Instruct‑2407 构建，可通过 transformers 使用设备映射和 ChatML 提示进行使用，已由 Ryosuke Ishigami 以 Apache‑2.0 许可证发布。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 1k / ⭐ 1 / 日本增强、指令调优的 Gemma‑2 模型，基于 Llama（2b/9b/27b 预训练和指令版本），于 2025 年 5 月 19 日发布，可通过 HuggingFace 和 Swallow 团队网站获取。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 1k / ⭐ 21 / 提供 1.8 B 参数 llm‑jp‑3.1‑1.8b‑instruct4 日本指令微调模型，来自 NII，兼容 Hugging Face Transformers 和 Torch ≥ 2.3.0，包括预训练和微调检查点以及使用示例.
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 1k / ⭐ 21 / OpenCALM 是 CyberAgent 开发的日本解码器（decoder‑only）Transformers 语言模型系列（160 M–6.8 B 参数），基于日本维基百科和 Common Crawl 训练，并以 CC BY‑SA 4.0 许可证发布。
 * [GPT-OSS-Swallow-120B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-120B-RL-v0.1) - 📥 1k / ⭐ 16 / GPT-OSS-Swallow v0.1 提供了 20 B 和 120 B 参数的日英双语 LLM，采用 CPT、SFT 和 RLVR 训练，以在保持数学和编码性能的同时，在推理与翻译方面匹配或超越 GPT‑OSS。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 1k / ⭐ 22 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter Japanese extension，进一步预训练以适用于日语语言任务，并提供 base、instruct、fast 和 fast‑instruct 变体，由 ELYZA team 在 Llama 2 Community License 下维护。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 1k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一个 13‑B 的、基于指令预训练的日语语言模型，由 NII 的研发中心开发，并以 Hugging‑Face Transformers 检查点的形式发布，使用 UNIGRAM‑byte‑fallback 分词器。
 * [Gemma-2-Llama-Swallow-2b-it-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-2b-it-v0.1) - 📥 1k / ⭐ 4 / 日语增强的 Gemma‑2 “Swallow” 语言模型，采用连续预训练与指令微调构建，在 Hugging Face 上提供 2 b、9 b 和 27 b 三种变体。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 9M / ⭐ 62 / Japanese wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 与 JSUT 上微调，需 16 kHz 音频，并可通过 HuggingSound 或 HuggingFace 管道使用。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 549k / ⭐ 11 / 一个由 facebook/wav2vec2‑large‑xlsr‑53 在 Common Voice 和 JSUT corpus 上微调的日本语音识别模型，针对 16 kHz 音频输入进行了优化。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 65k / ⭐ 154 / Anime Whisper 是一款轻量级的日语 ASR 模型，在约 5,300 小时的动漫风格对话上进行微调，能够提供低幻觉、节奏对齐标点，以及准确转录非言语声音和 NSFW 内容，并且需要在没有初始提示的情况下运行。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 32k / ⭐ 126 / Kotoba‑Whisper‑v2.2 是一个日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了说话人划分和自动标点功能，通过 HuggingFace‑Transformers pipeline，并与 Asahi Ushio 与 Kotoba Technologies 合作开发。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 13k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供了快 6.3 倍的蒸馏 Whisper 模型，用于日语和英语 ASR，并实现双向语音转文本翻译，这些模型是基于 OpenAI 的 Whisper large‑v3 通过知识蒸馏、交叉熵和 KL‑divergence 损失构建。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 13k / ⭐ 95 / Kotoba‑Whisper v2.0 是从 OpenAI Whisper large‑v3 蒸馏出的日语 ASR 模型，训练于 720 万个 ReazonSpeech 剪辑，推理速度快 6.3 倍，同时在同域测试中匹配教师模型的 CER/WER，并提供 stable‑ts/标点支持以及完整的训练代码在 GitHub 上。
 * [Qwen3-ASR-1.7B-JA](https://huggingface.co/neosophie/Qwen3-ASR-1.7B-JA) - 📥 8k / ⭐ 8 / 针对日语 ASR 对 Qwen3-ASR-1.7B 进行微调，优化其准确转写专有名词、机构和产品名称，以及以汉字为主或混合日英的技术术语。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 5k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一个 96.7 M 参数的 wav2vec 2.0 Base 模型，经过在 ReazonSpeech v2.0 日语 ASR 语料库上微调，达到 13.22 % 的 CER，可与 Hugging Face transformers 一同部署，并在 Apache 2.0 许可证下发布。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 5k / ⭐ 60 / NVIDIA NeMo 的 0.6 B 参数 Hybrid FastConformer‑TDT‑CTC ASR 模型可转写带标点的日语语音，并可在 NeMo 框架内用于推理或微调。
 * [qwen3-asr-1.7b-ja-anime-GGUF](https://huggingface.co/cstr/qwen3-asr-1.7b-ja-anime-GGUF) - 📥 3k / ⭐ 2 / GGUF‑quantized Qwen3‑ASR‑1.7B fine‑tuned for Japanese anime/galgame speech, supporting 30+ languages and CrispASR with two sizes (~1.3 GB Q4_K and ~2.5 GB Q8_0) under an Apache 2.0 license.
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 3k / ⭐ 25 / Kotoba Whisper v2.0 被转换为 CTranslate2 格式，以便与 CTranslate2 和 faster-whisper 一起使用，提供安装、推理示例、Apple M2 基准测试和转换说明。
 * [japanese-hubert-base-phoneme-ctc-v4](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v4) - 📥 2k / ⭐ 5 / 微调日语 Hubert‑Base 用于 CTC 音素识别（v4）并更新句子过滤规则、发音调整以及将 GPU 切换到 A6000，训练在 110k 步时停止。
 * [japanese-hubert-base-phoneme-ctc](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc) - 📥 2k / ⭐ 5 / 基于 rinna/japanese‑hubert‑base 的微调日语音素 CTC 模型，使用 ReazonSpeech v2 数据和 pyopenjtalk‑plus 标签进行训练，在新版 v2 发布（prj-beatrice/japanese-hubert-base-phoneme-ctc-v2）中实现了更高的准确率。
 * [parakeet-tdt-0.6b-ja-GGUF](https://huggingface.co/cstr/parakeet-tdt-0.6b-ja-GGUF) - 📥 2k / ⭐ 1 / A GGUF‑converted 0.6 B Japanese Parakeet TDT‑CTC model，能够与 CrispASR 的 CLI 一起用于 TDT 解码（CTC 回退），在 JSUT 上实现 6.4 % CER，并提供词级时间戳，可获得完整的 1.24 GB 精确构建版本以及约 470 MB Q4_K 量化变体（该变体在 ~8 个 token 后性能下降，建议使用 F16）。
 * [mms-300m-ForcedAligner-karaoke-ja-Latn](https://huggingface.co/NextFire/mms-300m-ForcedAligner-karaoke-ja-Latn) - 📥 2k / ⭐ 2 / 一个经过微调的日语罗马音卡拉OK歌词强制对齐模型（MMS-300M），附带笔记本和TrackIO工具。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 2k / ⭐ 18 / Kotoba‑Whisper‑v2.1 是一种日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了标点后处理管道，保持可比的 CER 性能，同时实现无缝、标点感知的转录。
 * [Qwen3-ASR-1.7B-JA-Anime-Galgame-hf](https://huggingface.co/jaykwok/Qwen3-ASR-1.7B-JA-Anime-Galgame-hf) - 📥 1k / ⭐ 3 / 兼容 Hugging Face 的 Qwen3‑ASR‑1.7B‑JA‑Anime‑Galgame 检查点转换，保留微调权重，同时调整其布局以适配本地 Transformers 加载，并支持日语动漫/galgame 语音生成。
 * [kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) - 📥 1k / ⭐ 34 / Kotoba‑Whisper v1.1 是一款日语 ASR 模型，它在 kotoba‑whisper‑v1.0 的基础上扩展了无缝标点添加后处理管道，提升了转录准确率并比多个 Whisper 基线减少了延迟。
 * [japanese-wav2vec2-large-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-large-rs35kh) - 📥 1k / ⭐ 4 / 日语 wav2vec 2.0 Large (319 M parameters) 微调于 ReazonSpeech v2.0，在日语 ASR 上提供平均 16.25 % CER，优于其他 wav2vec 2.0 系列。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 1k / ⭐ 38 / reazonspeech-nemo-v2 是一个 619‑M‑参数的日语长文本 ASR 模型，基于改进版 Fast‑Conformer 及 Linearly Scalable Attention，在 ReazonSpeech v2.0 语料库上训练，支持通过 subword RNN‑T decoder（3000‑token SentencePiece）进行多小时推理，并以 Apache 2.0 许可分发。
 * [japanese-hubert-base-phoneme-ctc-v3](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v3) - 📥 1k / ⭐ 5 / 为CTC音素识别微调的日本HuBERT-base（v3），加入了MeCab N‑best与pyopenjtalk‑plus后处理、结合CTC和MeCab成本的加权损失、更新排除规则，以及新增“ty”音素。

### fill-mask
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 505k / ⭐ 9 / 日语 DeBERTa V2 大型模型，已在 171 GB 的日语 Wikipedia、CC‑100 与 OSCAR 上训练，使用字符级 SentencePiece 分词和全词掩码，已准备好通过 Hugging Face Transformers 进行下游微调。
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 352k / ⭐ 76 / Japanese BERT‑base 在 2019 年日本维基百科上预训练，使用 IPA‑dictionary 与全词掩码，12 层 768 维，32,000 词表，512 标记序列，1 M 步骤，可在 cl‑tohoku/bert‑japanese 获取，遵循 CC‑BY‑SA 许可。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 144k / ⭐ 42 / 一个预训练于约 17 M 条日语维基百科句子（2.6 GB）的 BERT base 模型，使用 IPA 字典和 WordPiece 进行分词，拥有 12 层 / 768‑维隐藏状态 / 12 头，32 000‑token 词汇表，已在 Cloud TPUs 上训练了 1 M 步，并以 CC‑BY‑SA 3.0 许可发布。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 119k / ⭐ 51 / 这是一款 1.32 亿参数的日语 ModernBERT 模型，融合了 local‑global 与 RoPE 注意力机制，训练于 4.39 T 词条（日语/英语），词表大小 102k，最大序列长度 8,192，针对 Flash Attention 2 做了优化。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 68k / ⭐ 6 / 一个 BERT‑base 日语模型（12 层，768-维隐藏状态，12 头），在 3000 万条维基百科句子（约 4 GB）上训练，使用 Unidic 2.1.2 词级分词，随后进行字符级分词和全词掩码，使用 512 令牌序列，256 批次，以及 1 M 训练步骤。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 17k / ⭐ 27 / ModernBERT‑Ja‑310M 是一种日语 BERT 变体，融合了局部-全局注意力和 RoPE，训练于 4.09 T 日语/英语文本，支持 102 400 词汇量、8 192 令牌序列，并针对 Flash Attention 2 进行了优化。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 14k / ⭐ 8 / 一个 BERT‑base 日语模型（12 层，768 维隐藏，12 头），使用 MeCab IPA 词级分词后再进行字符级分词生成 4000 词的词表，在约 1700 万句来自日语维基百科（2.6 GB）的句子上预训练，训练代码位于 cl‑tohoku/bert‑japanese，采用 CC BY‑SA 3.0 许可证发布。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 10k / ⭐ 40 / Japanese‑Roberta‑Base 是来自 rinna Co., Ltd. 的预训练掩码语言模型，提供了正确加载、token 预处理、position‑id 处理的准则，以及强调需要前置 [CLS] token 和一致 tokenization 的使用示例。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 7k / ⭐ 50 / LINE DistilBERT Japanese 是一个 6600 万参数的 DistilBERT 模型，已在 131 GB 的日语网页文本上使用内部 BERT‑base 教师进行预训练，评估基准为 JGLUE，采用 MeCab Unidic 与 SentencePiece 进行分词，并以 Apache 2.0 许可证发布。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 7k / ⭐ 26 / Japanese BERT‑base（12 层，768 隐藏，12 头）在 4 GB 的日语维基百科（≈30 M 句）上预训练，使用 Unidic 2.1.2 词级分词、WordPiece 子词分词和全词遮蔽。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 5k / ⭐ 4 / Japanese DeBERTa V2 tiny，在约171 GB的日本维基百科、CC‑100 与 OSCAR 语料库上预训练，需使用 Juman++ 词分割，训练耗时 33 小时，使用8块 NVIDIA A100 GPU，并可用于下游任务的微调。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 5k / ⭐ 1 / 一款日本DeBERTa‑V2基础模型，已在171 GB的日本维基百科、CC‑100和OSCAR文本上预训练，使用字符级分词、全词掩码，训练耗时20天，使用8块A100 GPU，并已准备好进行下游微调。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 5k / ⭐ 30 / Japanese DeBERTa V2 基础模型已在 171 GB 的日语维基百科、CC‑100 和 OSCAR 数据上预训练，使用 Juman++ 分词和 SentencePiece 标记化，经过三周在八块 NVIDIA A100 GPU 上训练，现已准备好用于微调。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 4k / ⭐ 5 / DeBERTaV2 base 在日本语语料库（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上训练，并使用 FP‑16 微调进行 NLU 任务（JSTS、JNLI、JCommonsenseQA），以 CC BY‑SA 4.0 许可发布，并由日本研究资助。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 3k / ⭐ 32 / Japanese RoBERTa‑base 在日本 Wikipedia 与日本 CC‑100 上预训练，采用 Juman++ 词分割与 SentencePiece 分词，使用 Adam（lr = 1e‑4，native AMP）在 8 台 NVIDIA A100 GPU 上训练了一周，可微调，并在 JGLUE 上报告了结果。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 2k / ⭐ 9 / ModernBERT‑Ja‑70M 是一种轻量级的日语 BERT 变体，结合本地和全局注意力与 RoPE，在 4.39 T 的混合语言词元（词表 102 400，最大 8 192 个词元）上训练，支持 Flash Attention 2，并提供 30 M 到 310 M 参数的多种尺寸。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 1k / ⭐ 8 / ModernBERT‑Ja‑30M 是一种日语 BERT 变体，融合了本地和全局注意力与 RoPE，训练于 4.39 TB 日英文本，支持 8,192 令牌序列，参数规模从 30 M 到 130 M，最佳搭配 Flash Attention 2。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 12 层，768 维度的 BERT‑Base 日语模型，在 2.6 GB Wikipedia（≈17 M 句子）上训练，使用 IPA‑dictionary 字符分词与 whole‑word masking，并在 CC‑BY‑SA 3.0 许可下发布。
 * [jmedroberta-base-sentencepiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece-vocab50000) - 📥 1k / ⭐ 1 / Japanese RoBERTa‑base模型在约10 M来自JST的医学文章摘要上预训练，使用50k SentencePiece（Unigram）词表，并以CC‑BY‑4.0授权发布，提供全角文本输入说明以及通过Hugging Face pipelines进行微调的指导。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 436k / ⭐ 81 / Ruri v3 是基于 ModernBERT‑Ja 的先进日语文本嵌入模型，支持多达 8,192 词元输入，100K 词元词汇表，FlashAttention 加速推理，并提供多种尺寸变体，便于快速使用 sentence‑transformer。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 269k / ⭐ 10 / Ruri v3是一个最先进的日语文本嵌入模型，基于ModernBERT‑Ja构建，支持最多8,192个标记，拥有100 k词汇量，支持FlashAttention加速，并提供多种规模，从37 M到315 M参数。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 221k / ⭐ 24 / GLuCoSE v2 是一款 CPU 友好的日语文本嵌入模型，通过蒸馏和多阶段对比学习进行微调，提供卓越的语义相似性和检索性能——在 MIRACL 及相关基准上优于同等规模的模型。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 125k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B 是一个 1.2 B 参数的日语文本嵌入模型，构建于 Sarashina2.1‑1B 上，使用多阶段对比学习训练，以在 JMTEB 上达到最先进的分数，同时在非商业许可下生成 1,792 维的稠密向量，用于语义相似度、搜索和分类。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 64k / ⭐ 7 / Ruri v3 是基于 ModernBERT‑Ja 的前沿日语文本嵌入模型，支持最多 8192 token 序列、100K token 词汇量、FlashAttention，并以 30 M 至 310 M 参数规模发布，供 sentence‑transformers 使用。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 40k / ⭐ 5 / Ruri v3 提供高性能的日语文本嵌入，支持至 8192 个 token，拥有 100k 个 token 的词汇表，支持 FlashAttention，并提供多种模型规模（30 m–310 m），以实现高效推理和通过 sentence‑transformers 进行微调。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 28k / ⭐ 34 / GLuCoSE 是一个基于 LUKE 的日语句子嵌入模型，输出 768 维均值池化向量（最多 512 个标记），在 Web 和 NLI/搜索数据上训练，在相似性基准测试中达到了 0.864 的 Spearman 相关系数和 0.818 的 Pearson 相关系数。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 14k / ⭐ 45 / 一组已准备好发布的 Ruri v3 日语文本嵌入模型（30m–310m），完整附带 SentenceTransformer 使用技巧、查询/段落前缀，以及 JMTEB 基准结果，展示它们与其他日语和多语言嵌入模型的比较。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 12k / ⭐ 48 / PLaMo‑Embedding‑1B 是 Preferred Networks 的一款日语文本嵌入模型，它将日语文本转换为向量，用于信息检索、分类和聚类，在 JMTEB 基准上表现出强大性能，并且在 Apache v2.0 许可证下可免费使用。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 12k / ⭐ 13 / 日语通用文本嵌入模型（Ruri‑v3，30‑310 M 参数，8192‑token 最大，JMTEB 分数高）与 Sentence‑Transformers 使用示例以及与其他日语嵌入模型的基准对比一起提供。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 7k / ⭐ 17 / JaColBERTv2 是一个仅适用于日语的基于 ColBERT 的检索模型，在 MMarco 上通过知识蒸馏训练（每个正例 31 个负例，250k 次，batch 32）。目前它优于 multilingual‑e5‑large、BGE‑M3 和 JaColBERT，完整评估正在进行中。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 6k / ⭐ 9 / 包括 Ruri v3 日语文本嵌入（30 M–310 M 参数，8192‑token 限制，JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前缀的 Sentence Transformers 指令，以及对数个日语模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基准结果。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 2k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一个 768 维的句子变换器，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，训练了一个 epoch 的 shunk031/jsnli，并包含用于聚类、语义搜索以及同时兼容 Sentence‑Transformers 和 HuggingFace 的示例。
 * [ruri-large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2) - 📥 2k / ⭐ 10 / 日本通用文本嵌入仓库 Ruri 提供 v3 模型，参数数从 30 M 到 310 M，具备 JMTEB 分数；并演示如何使用 sentence_transformers（使用 “クエリ: ” / “文章: ” 前缀）加载它们，并给出基准结果比较多个日语嵌入模型。

### feature-extraction
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 216k / ⭐ 56 / 一个Japanese‑language T5 model，在约100 GB的Wikipedia和OSCAR数据上使用SentencePiece tokenization进行预训练，超越了Google’s multilingual T5在news‑classification benchmark上的表现，但需要fine‑tuning，并可能产生biased outputs.
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 198k / ⭐ 51 / 一款在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上使用 MultipleNegativesRankingLoss 细调的 Japanese Sentence‑BERT v2，较 v1 提升了约 1.5–2 %的准确率，并以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 发布。
 * [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) - 📥 187k / ⭐ 5 / 日语HuBERT Base，12层 Transformer 与 rinna 原版相同，使用约19,000小时的 ReazonSpeech v1 日语语音训练，并以 Apache 2.0 许可证发布。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 33k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一个 Apache‑2.0 许可的日语 CLIP 模型，基于 ViT‑B/16，训练于 CC12M captions 翻译成日语，并于 2022 年 5 月 12 日发布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 25k / ⭐ 30 / LY Corporation的clip‑japanese‑base 是一个日语 CLIP 模型，在约10亿对图像‑文本对上训练，使用 Eva02‑B transformer 图像编码器和 12 层 BERT 文本编码器，在 STAIR 上实现 R@1 0.30，在 Recruit 上得到 0.89 的准确率，在 ImageNet‑1K 上得到 0.58 的准确率，并支持 zero‑shot 图像分类和检索。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 14k / ⭐ 11 / 用于生成句子嵌入的 Japanese Sentence‑BERT (v1) 模型，已提供改进版 v2，并通过 Hugging Face Transformers 以及自定义的 `SentenceBertJapanese` 类进行示例使用。
 * [japanese-hubert-large](https://huggingface.co/yky-h/japanese-hubert-large) - 📥 7k / ⭐ 2 / Japanese HuBERT Large 是 rinna Co., Ltd. 开发的 24 层、16 头 transformer 模型，使用约 19,000 小时 ReazonSpeech v1 日语音频训练，于 2024 年 3 月 7 日以 Apache 2.0 许可证发布。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 6k / ⭐ 14 / Japanese Sentence‑LUKE 模型在与 Sentence‑BERT 同一数据集上训练，表现超过或匹配其性能，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，并通过 Hugging Face Transformers 的 MLukeTokenizer 与 LukeModel 进行使用。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 6k / ⭐ 18 / 日本CLIP模型 clip‑japanese‑base‑v2，升级后约20亿图像‑文本对并采用蒸馏，配合 Eva02‑B 图像编码器和 12 层 BERT 文本编码器，将 ImageNet‑1k 准确率提升至 0.708，超过前代模型。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 4k / ⭐ 27 / Sarashina‑Embedding‑v2‑1B 是一个 1,792 维的日语句子变换器，使用多阶段对比学习训练，获得了前沿的 JMTEB 分数，可通过 Sentence‑Transformers 并搭配可选指令前缀，用于语义相似度、搜索、改写挖掘、分类和聚类。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 3k / ⭐ 2 / ja_ginza_electra 是一个 spaCy v3 Python 包，提供一个在 mC4 和 UD_Japanese_BCCWJ r2.8（基于 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator）上微调的日语 ELECTRA 模型，并配有自定义 bunsetu‑phrase 检测功能，按 MIT license 分发。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 2k / ⭐ 3 / 一个日语 BERT‑base 模型，在 JSNLI 上使用有监督 SimCSE 进行微调，通过 Sentence‑Transformers 或 HuggingFace 提供，采用 CLS 池化。在 1M 个样本上训练，批量大小为 512，学习率为 5×10⁻⁵，温度为 5×10⁻⁵，64 令牌限制，采用 BFloat16 精度。

### text-ranking
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 325k / ⭐ 15 / Ruri‑v3 Reranker 是一个基于 ModernBERT‑Ja 构建的稳健日语文本重排器，支持最高 8,192‑token 序列、100k‑token 词汇表、FlashAttention 以及 SentencePiece 分词器，并可通过 sentence‑transformers 使用。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 92k / ⭐ 6 / 快、轻量级的日语 Reranker v2 模型（tiny、xsmall、small、base），带有基准测试分数和 GPU 速度，可通过 sentence_transformers CrossEncoder 与 transformers ≥ v4.48 使用（可选闪存加速 flash‑attn），并且在 ONNX/量化形式下可用于 CPU/ARM。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 73k / ⭐ 5 / 日本训练的 CrossEncoder 重新排序器，尺寸从 xsmall（384）到 large（1024），以及 BGE‑v2‑m3‑v1 模型，提供微调、推理和 JQaRA、JaCWIR、MIRACL、JSQuAD 上的基准分数示例代码。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 64k / ⭐ 7 / 日语 CrossEncoder 再排序模型，覆盖 xsmall 到 large（含 BGE），在 JQaRA、JaCWIR、MIRACL 与 JSQuAD 上进行评估，并为 sentence_transformers 与 HuggingFace 提供即用的集成示例。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 5k / ⭐ 2 / 使用 Sentence Transformers（交叉编码器）构建的日语重排序模型，可通过 `trust_remote_code` 加载，在 JQaRA、JaCWIR 和 MIRACL 数据集上进行基准测试，并由 hotchpotch 组织提供从小到大尺寸版本。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 3k / ⭐ 8 / 一个日本 Reranker v2 套件，发布 CrossEncoder 和 base 模型，覆盖从 tiny 到 large，每个都有基准得分和 GPU 推理时间，并要求 HuggingFace Transformers ≥ 4.48（可选 flash‑attn 用于更快推理）。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / Japanese CrossEncoder Reranker 模型（xsmall、small、base、large、BGE‑v2 m3）隐藏尺寸为 384–1024，示例推理通过 sentence_transformers 和 Hugging Face， 在 JQaRA、JaCWIR、MIRACL 和 JSQuAD 上得分 0.71–0.97+。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 2k / ⭐ 16 / 日语 CrossEncoder 重排序模型——从xsmall到large——在日语文本上训练，通过sentence_transformers公开，评估在JQaRA、JaCWIR、MIRACL和JSQuAD上。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 1k / ⭐ 3 / Japanese‑reranker‑small‑v2 是一系列轻量级、快速的日语重排序模型（v2），提供从极小到基础的变体，最高可达 0.89 的平均分，GPU 推理时间为 2–15 秒，支持交叉编码器选项，并需要 Hugging Face Transformers v4.48+，可选 Flash Attention 2 进行加速。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 1k / ⭐ 15 / 一个日语 CrossEncoder 重新排序器套件——包括 xsmall、small、base、large 和 japanese‑bge‑reranker‑v2‑m3‑v1——配合示例用法、在多个基准上的评估指标和支持文档。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 501k / ⭐ 17 / 一个基于新 VNTL 数据集构建的 LLaMA 3 Youko qlora 微调模型，优化用于准确、逐字翻译日本视觉小说为英文，不使用聊天模式，采用默认 LLaMA 3 提示，并推荐中性采样（温度 0，无重复惩罚）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 137k / ⭐ 15 / Sugoi LLM 14B Ultra (GGUF) 是一个日语到英语的翻译模型，BLEU 分数为 21.38，几乎是其之前的 13.67 的两倍，在 RPG‑Maker 括号文本、提示遵循强度以及为交互式聊天 UI 的 JSON 输出方面表现出色。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 34k / ⭐ 75 / 来自 Opus 语料库的日语‑英语 Transformer‑Align 机器翻译模型，使用归一化和 SentencePiece 预处理，在 Tatoeba 测试集上达到了 41.7 BLEU 和 0.589 chr‑F。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 3k / ⭐ 33 / FuguMT 是一个从日语到英语的 Marian‑NMT 翻译模型，使用 transformers 和 SentencePiece 构建，在 Tatoeba 上得分 39.1 BLEU。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 3k / ⭐ 55 / FuguMT 是一个基于 Marian‑NMT 的英日翻译模型，使用 Hugging Face Transformers 和 SentencePiece 构建，并在 Tatoeba 上获得了 32.7 的 BLEU 分数。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 2k / ⭐ 41 / 已微调、GGUF-量化的 LFM2-350M checkpoint，用于近实时双向日英短至中等文本翻译，可通过 llama.cpp 使用。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 2k / ⭐ 123 / PLaMo Translation Model 是由 Preferred Networks 创建的大规模语言模型，专用于翻译任务，提供基础版、后训练版和评估版，在 PLaMo community license 下发布，并未针对聊天或其他下游用途进行 instruction‑tuned。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 659k / ⭐ 178 / Manga OCR 是一款 Vision Encoder‑Decoder OCR 工具，可读取纵向和横向的日语漫画文本，包括 furigana，适用于多种字体和低质量图像，并且源代码可免费获取。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 100k / ⭐ 7 / Meikiocr的 `meiki.text.recognition.v0`——基于 D‑FINE 的 MobileNetV4 模型，在日本视频游戏文本上微调——为水平文本提供最先进的准确率和延迟，能够从 960×32 的输入中检测多达 48 个字符，并输出每个字符的边界框和置信度分数。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 51k / ⭐ 3 / meikiocr 提供一个基于 D‑FINE、开源权重的视频游戏文本检测模型（v0.1，使用 MobileNet‑v4 骨干网络，提供两种分辨率变体和 64‑box 限制），以及实验性的低延迟 tiny 与 small 变体，训练材料来自日本视频游戏和漫画。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 3k / ⭐ 4 / Manga OCR 是一种 Vision Encoder‑Decoder 系统，可在各种字体和低质量图像中提供高质量的日语漫画 OCR——包括带有假名覆盖的纵向和横向文本——并且也可用于一般印刷日语 OCR。
 * [manga-ocr-2025-onnx](https://huggingface.co/l0wgear/manga-ocr-2025-onnx) - 📥 3k / ⭐ 9 / 基于 kha‑white 的 manga‑ocr 和 jzhang533 的 2025 baseline 构建的 ONNX Vision‑Encoder‑Decoder Manga OCR 模型，支持竖排/横排日语文本、假名注音、叠加文字和低质量图像，训练数据包括 manga109‑s 与合成数据，可通过 Hugging Face Optimum 使用 TrOCRProcessor 和 ORTModelForVision2Seq 部署。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 2k / ⭐ 32 / Sarashina2.2‑OCR 是一个 3‑B 参数的端到端 OCR 模型，经过人工偏好优化后，能够将日文和英文文档解析为 Markdown，同时将表格转换为 HTML，数学公式转换为 LaTeX，图形转换为边界框注释，其实现方式是将 SigLIP2‑基础的视觉编码器与 Sarashina2.2‑3B‑Instruct LLM 集成，从而实现高分辨率视觉‑语言理解。

### text-classification
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 55k / ⭐ 6 / 一款在 WRIME 数据集上微调的日语 BERT BASE 可为作家和读者预测八种情绪（喜悦、悲伤、期待、惊讶、愤怒、恐惧、厌恶、信任）的 0‑4 强度得分，代码已公开，在 K80 上训练耗时 3 小时，作家的均方误差约为 0.6，读者约为 0.2。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 4k / ⭐ 16 / 在亚马逊产品评论上对日语 BERT (cl‑tohoku/bert‑base‑japanese‑v2) 进行微调，用于情感分类，经过6个周期，学习率为2 × 10⁻⁵，达到约81 %准确率和0.73 F1。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 3k / ⭐ 2 / 一个基于 Japanese BERT‑based model 的模型，已在 JGLUE JSTS 数据集上 fine‑tuned，用于语义相似性评分——在《Large Language Model Introduction》第5章中介绍——配有 Colab notebooks、transformers‑pipeline 用法以及 Apache 2.0 许可证。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 2k / ⭐ 15 / 训练于 chABSA 数据集的日语情感分析模型，获得 loss 0.0001、accuracy 1.0、F1 1.0，由 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 构建，使用 Adam（learning rate 2e‑05、10 epochs、batch size 16）优化，并通过 `model(**inputs)` 进行评估。

### token-classification
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 11k / ⭐ 11 / Fine‑tuned Japanese BERT‑Base适用于在维基百科数据集上的命名实体识别，该模型在《*Large Language Model Introduction*》一书第六章中呈现，并可通过Hugging Face transformers pipeline进行部署（Apache 2.0 许可）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 7k / ⭐ 27 / 在日语 NER 语料库上对 XLM‑RoBERTa‑base 进行微调（标签 PER, ORG, LOC, INS, PRD, EVT），使用 5‑epoch Adam（lr 5e‑5，batch 12），达到 0.0173 的验证损失，已发布在 Transformers 4.23.1 和 PyTorch 1.12.1。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 5k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日语 NER，能够提取八种实体类型（公司、政治/其他组织、设施、产品、事件），通过 `BertForTokenClassification` 实现，训练数据来自 Stockmark Wikipedia dataset，并可通过安装 `transformers`、`unidic_lite` 和 `fugashi` 使用，遵循 CC BY‑SA 3.0 许可。

### text-to-speech
 * [sarashina2.2-tts](https://huggingface.co/sbintuitions/sarashina2.2-tts) - 📥 13k / ⭐ 69 / sarashina2.2-tts 是一个 SB Intuitions 基于 LLM 的日语中心化 TTS 系统，提供高精度的日语和英语合成、自然富有表现力的声音、零样本克隆、跨语言一致性以及无缝代码切换。
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 4k / ⭐ 11 / 一款名为 **tsukuyomi‑wavlm** 的日本文本转语音模型——在 tsukuyomi corpus 的 100 条语句上经过 300 个周期的微调，使用 WavLM 判别器和 A1/A2/A3 声韵特征，基于 VITS 架构，导出为 61 MB 的 ONNX 文件，用以生成 22.05 kHz 的合成语音。

### any-to-any
 * [gemma-4-12B-it-qat-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-12B-it-qat-UD-japanese-imatrix) - 📥 5k / ⭐ 12 / 一个 1/4 大小、CPU‑friendly 的日语优化量化 Gemma 4 模型（Apache 2.0），可全程在本地运行，提供可选的开发者支持与稳健的基准测试。

### text-to-image
 * [stable-diffusion-xl-jp-base-1.0](https://huggingface.co/tohoku-nlp/stable-diffusion-xl-jp-base-1.0) - 📥 2k / ⭐ 5 / 5.8 十亿参数的 SD‑XL 1.0 基础模型，使用 OpenCLIP‑ViT 文本编码器和 multilingual‑e5 嵌入进行日语微调，在约 2800 万个 WMT‑Japanese/English 对上训练，并加入约 1300 万个已过滤的 LAION2B 标注（已翻译为英文），并以 Open RAIL++‑M 许可证发布。

### audio-to-audio
 * [LFM2.5-Audio-1.5B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B-JP-GGUF) - 📥 2k / ⭐ 31 / LiquidAI 的 LFM 2.5‑Audio 1.5B JP 模型的量化 GGUF 版本，包括语言、音频编码器和声码器权重（F32/F16/Q8_0/Q4_0），以及使用 llama.cpp 的 ASR 和 TTS CLI/Server 运行器。

### image-text-to-text
 * [Stockmark-Nemotron-3-Nano-Omni-JapanDocReader](https://huggingface.co/stockmark/Stockmark-Nemotron-3-Nano-Omni-JapanDocReader) - 📥 1k / ⭐ 8 / Stockmark‑Nemotron‑3‑Nano‑Omni‑JapanDocReader 是一款基于 NVIDIA 的 Nemotron‑3‑Nano‑Omni 构建的日语多模态文档阅读模型，使用混合 VQA 与结构化解析数据进行微调，并通过 DAPO 强化，以在保持 VQA 推理能力的同时提升文档解析质量。

### others
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 133k / ⭐ 64 / Japanese BERT‑base（12层，768维隐藏层，12头，32 k词汇表）在 CC‑100 和 2023‑Jan Wikipedia 上使用全词遮蔽预训练，采用 Unidic 2.1.2 词级分词加 WordPiece，训练 200 万步。
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 132k / ⭐ 11 / 日本语言 BERT‑Base（12 层，768 维，12 头）使用 Unidic 基于词级加字符级分词和全词掩码在 CC‑100 及 2023 Wikipedia 上进行预训练，产生 7,027 名词表。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 80k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上训练，使用 Unidic‑lite 单词级标记化配合 WordPiece 子词和全词掩码（24 层，1024 维隐藏层，16 头，32k 词表），预训练代码在 cl‑tohoku/bert‑japanese。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 39k / ⭐ 13 / 提供了 gguf 格式的 moonshotai 的 Moonlight‑16B‑A3B‑Instruct，已在 TFMC 的 imatrix 日语数据集上训练，准备好与 llama.cpp（CUDA‑enabled）一起使用，并通过执行 recipe‑request 提示来演示。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 17k / ⭐ 11 / 一个预训练在≈100 GB的维基百科和 OS CC‑100 数据（SentencePiece 采用 10:1 混合且带 byte‑fallback）的日文 T5‑v1.1 模型，需要微调以适用于下游任务，包含迁移学习示例代码，指出输出中的潜在偏差，并遵循 CC‑BY‑SA 4.0 许可。
 * [kana-whisper](https://huggingface.co/sbintuitions/kana-whisper) - 📥 12k / ⭐ 8 / 一个经过微调的 Whisper large‑v3‑turbo 模型，用于将日语语音转录为片假名，作为 Sarashina2.2‑TTS 项目中 Joyo Kanji Yomi Benchmark 的 ASR 组件，并驱动 Kana CER Usage With Transformers 管道。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 6k / ⭐ 17 / 高性能的日本 SPLADE v2 通过 WebUI demo 实现稀疏向量转换和推理，使用 YAST 进行训练，提供 YASEM 嵌入，并报告 JMTEB benchmark 结果。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 4k / ⭐ 19 / Japanese DeBERTa V3 base 在 LLM‑jp v1.0 的 540 B tokens 上预训练，使用经过修改的 DeBERTa V3 设置训练，采用 unigram byte‑fallback tokenizer（不使用形态学分析器），并针对 JGLUE NLU 任务进行微调。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-32b-a3b-thinking-gguf) - 📥 4k / ⭐ 12 / GGUF 格式转换的 llm‑jp‑4‑32b‑a3b‑thinking，使用 TFMC 的 imatrix 数据集构建，适用于通过 llama.cpp 在支持 CUDA 的推理。
 * [umiyuki-Umievo-itr012-Gleipnir-7B-gguf](https://huggingface.co/mmnga/umiyuki-Umievo-itr012-Gleipnir-7B-gguf) - 📥 3k / ⭐ 9 / Umievo‑itr012‑Gleipnir‑7B（已在 TFMC/imatrix‑dataset‑for‑japanese‑llm 上训练）的 gguf‑格式版本，已就绪可在 llama.cpp 上运行。
 * [Qwen3.5-2B-Ideal-TSUNDERE-Loli-Girl-Japanese-v1-i1-GGUF](https://huggingface.co/mradermacher/Qwen3.5-2B-Ideal-TSUNDERE-Loli-Girl-Japanese-v1-i1-GGUF) - 📥 3k / ⭐ 2 / 提供了 Qwen3.5‑2B “Ideal TSUNDERE Loli Girl Japanese” 模型的加权和 imatrix 量化版本，格式为 GGUF（从 0.1 GB 到 1.7 GB 的多种 IQ/K 等级），并包含 Hugging Face 页面链接、静态下载地址以及使用分块文件的指导。
 * [umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf](https://huggingface.co/mmnga/umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf) - 📥 3k / ⭐ 3 / 一个从 TFMC/imatrix 数据集构建的 GGUF‑converted 日语聊天模型 “Japanese‑Chat‑Umievo‑itr001‑7b”，可通过单文件命令行在 llama.cpp 中使用。
 * [YuisekinAIEvol-Mistral-7B-ja-math-v0.1.1-gguf](https://huggingface.co/mmnga/YuisekinAIEvol-Mistral-7B-ja-math-v0.1.1-gguf) - 📥 3k / ⭐ 2 / GGUF 格式的 YuisekinAIEvol‑Mistral‑7B‑ja‑math‑v0.1.1（基于 TFMC/imatrix‑dataset）已准备好用于 llama.cpp。
 * [gemma-4-E2B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E2B-it-UD-japanese-imatrix) - 📥 3k / ⭐ 2 / 经过 GGUF 转换的 Gemma‑4‑E2B‑it 模型，已细调以提升日语水平；使用 Unsloth® Dynamic Quantization 2.0 构建，已包含社区 Bug 修复和日文校准数据；可在 CPU 上运行（≥8 GB RAM，≥4 GB 磁盘），通过 llama.cpp。
 * [Fugaku-LLM-13B-instruct-gguf](https://huggingface.co/mmnga/Fugaku-LLM-13B-instruct-gguf) - 📥 3k / ⭐ 6 / Fugaku‑LLM‑13B‑instruct‑gguf 是 Fugaku‑LLM‑13B‑instruct 的 gguf 格式转换，使用 TFMC/imatrix-dataset-for-japanese-llm 中的 imatrix 数据构建，并要求用户同意其使用条款。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一个拥有80亿参数的 LLM，通过在合成日语数据上持续预训练和指令微调，提升了 Meta 的 Llama 3.1 在日语语言与代码/数学推理上的表现，同时保持了英语流畅性。
 * [tokyotech-llm-Swallow-13b-instruct-v0.1-gguf](https://huggingface.co/mmnga/tokyotech-llm-Swallow-13b-instruct-v0.1-gguf) - 📥 2k / ⭐ 1 / 来自TokyoTech-LLM的 GGUF 格式 13B 指令模型，已在 TFMC 的日语数据集上进行微调，可与 llama.cpp 一起使用处理日语提示。
 * [karakuri-lm-8x7b-instruct-v0.1-gguf](https://huggingface.co/mmnga/karakuri-lm-8x7b-instruct-v0.1-gguf) - 📥 2k / ⭐ 2 / 由 karakuri‑ai 发布的 GGUF 格式版本 karakuri‑lm‑8x7b‑instruct‑v0.1，基于 TFMC/imatrix‑dataset‑for‑japanese‑llm 训练，可通过提供的命令行使用 llama.cpp。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 75 / Llama‑3‑ELYZA‑JP‑8B 是一款经过日本增强的 8‑B Llama 3 模型，采用 GGUF (Q4_K_M) 和 AWQ 量化，支持通过 llama.cpp、LM Studio 或 OpenAI‑compatible API 运行。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 2k / ⭐ 2 / DataPilot 的 ArrowPro-7B-RobinHood 模型的 GGUF 转换版本，基于 TFMC/imatrix 数据集构建，可与 llama.cpp 一起用于日语 LLM 任务。
 * [ArrowPro-7B-KillerWhale-gguf](https://huggingface.co/mmnga/ArrowPro-7B-KillerWhale-gguf) - 📥 2k / ⭐ 1 / 已将 ArrowPro-7B-KillerWhale 模型转换为 gguf（使用 TFMC/imatrix-dataset-for-japanese-LLM 训练），可直接用于 llama.cpp。
 * [lightblue-suzume-llama-3-8B-japanese-gguf](https://huggingface.co/mmnga/lightblue-suzume-llama-3-8B-japanese-gguf) - 📥 2k / ⭐ 2 / Lightblue的 suzume‑Llama‑3‑8B 的日语优化版 GGUF，使用 TFMC/imatrix 数据构建，并与 llama.cpp 兼容用于推理。
 * [tokyotech-llm-Swallow-70b-instruct-v0.1-gguf](https://huggingface.co/mmnga/tokyotech-llm-Swallow-70b-instruct-v0.1-gguf) - 📥 2k / ⭐ 1 / 一个从东京工科大学LLM转换为GGUF格式的70 B Swallow‑instruct模型，训练数据来自imatrix日语数据集，可使用llama.cpp进行推理。
 * [DataPilot-ArrowPro-7B-KUJIRA-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-KUJIRA-gguf) - 📥 2k / ⭐ 10 / ArrowPro‑7B‑KUJIRA 在 GGUF 格式中发布，由 DataPilot 发布，并基于 TFMC/imatrix-dataset-for-japanese-LLM 构建，可与 llama.cpp 一起用于日语 LLM 推理。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 2k / ⭐ 1 / 一个高度优化的 GGUF 版本的 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 并进行广泛的错误修复，专为日语语言能力调优，可在 llama.cpp 上运行，至少需要 16 GB 内存和 6 GB 磁盘（GPU 可选）。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 2k / ⭐ 3 / T5 v1.1 日语模型，预训练于 mC4/ja 和 Wikipedia，采用 GEGLU 激活函数，预训练期间无 dropout，使用独立的嵌入/分类器层，并且 d_model 较大但头数更少。商业用途许可为 CC‑BY‑SA 4.0。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 2k / ⭐ 22 / 由 imatrix 数据构建的 pfnet 的 plamo‑2‑translate 的 GGUF‑格式发布，基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带通过 llama.cpp 在启用 CUDA 的硬件上编译和运行的说明。
 * [pfnet-nekomata-14b-pfn-qfin-gguf](https://huggingface.co/mmnga/pfnet-nekomata-14b-pfn-qfin-gguf) - 📥 2k / ⭐ 1 / 一款基于 TFMC/imatrix 数据构建的 GGUF 转换版本，采用 pfnet 的 nekomata‑14b‑pfn‑qfin 模型，并按通义千问许可协议授权，可直接用于 llama.cpp。
 * [Llama-3-Swallow-8B-Instruct-v0.1-gguf](https://huggingface.co/mmnga/Llama-3-Swallow-8B-Instruct-v0.1-gguf) - 📥 2k / ⭐ 3 / 一个 gguf 格式的转换，针对 tokyotech‑llm 的 Llama‑3‑Swallow‑8B‑Instruct‑v0.1，使用来自 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 数据构建，可通过 llama.cpp 运行（例如：`./main -m 'Llama-3-Swallow-8B-Instruct-v0.1-Q4_0.gguf'`）。
 * [Llama-3-Swallow-70B-Instruct-v0.1-gguf](https://huggingface.co/mmnga/Llama-3-Swallow-70B-Instruct-v0.1-gguf) - 📥 1k / ⭐ 8 / 由 tokyotech‑llm 发布的 Llama‑3‑Swallow‑70B‑Instruct‑v0.1 的 gguf 格式转换，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 训练，可通过 llama.cpp 使用（例如 `./main -m 'Llama-3-Swallow-70B-Instruct-v0.1-Q4_0.gguf'`）。
 * [japanese-stablelm-2-instruct-1_6b-gguf](https://huggingface.co/mmnga/japanese-stablelm-2-instruct-1_6b-gguf) - 📥 1k / ⭐ 3 / GGUF‑formatted version of stabilityai’s japanese‑stablelm‑2‑instruct‑1_6b built with TFMC’s imatrix‑dataset, requiring license agreement (commercial use needs a membership), and conversion scripts using llama.cpp.
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 1k / ⭐ 6 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一个顶尖的、面向日语的 GGUF 模型，使用 Unsloth Dynamic Quantization 2.0，配有广泛的日语校准和社区修复的错误，能够在 llama.cpp 上运行，即使没有 GPU，也只需至少 8 GB RAM 和 3 GB disk。
 * [llama-3-youko-8b-instruct-i1-GGUF](https://huggingface.co/mradermacher/llama-3-youko-8b-instruct-i1-GGUF) - 📥 1k / ⭐ 1 / rinna/llama‑3‑youko‑8b‑instruct 的 GGUF 量化版本集合，列出它们的尺寸/质量权衡，并提供使用指导、对比图表以及 FAQ/模型请求链接。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 16 / Sarashina2.2 提供 0.5‑B、1‑B 和 3‑B 语言模型， 这些模型由 SB Intuitions 通过三阶段流水线和合成数据训练，达到了日本 QA、数学和编码的顶级成绩，同时提供的预训练权重未进行指令微调，可能产生偏见输出。
 * [Llama-3.1-8B-EZO-1.1-it-gguf](https://huggingface.co/mmnga/Llama-3.1-8B-EZO-1.1-it-gguf) - 📥 1k / ⭐ 7 / HODACHI 的 GGUF 转换版 Llama 3.1 8B “EZO‑1.1‑it”模型（在 TFMC/imatrix‑dataset-for-japanese‑LLM 上训练）已准备好可与 llama.cpp 命令行界面一起使用。
 * [Ninja-v1-NSFW-128k-gguf](https://huggingface.co/mmnga/Ninja-v1-NSFW-128k-gguf) - 📥 1k / ⭐ 11 / 提供 GGUF‑format 转换的 Ninja‑v1‑NSFW‑128k 模型的存储库，该模型基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM 构建，并附带在 llama.cpp 中运行以生成日本小说文本的使用说明。
 * [SakanaAI-EvoLLM-JP-v1-7B-gguf](https://huggingface.co/mmnga/SakanaAI-EvoLLM-JP-v1-7B-gguf) - 📥 1k / ⭐ 4 / EvoLLM‑JP‑v1‑7B（gguf 格式），是从 Shisa Gamma 7B、WizardMath 7B V1.1 和 Abel 7B 002 合并得到的基础模型，可与 llama.cpp 一起用于日语语言任务。
 * [sarashina2.2-3b-instruct-v0.1-gguf](https://huggingface.co/mmnga/sarashina2.2-3b-instruct-v0.1-gguf) - 📥 1k / ⭐ 9 / 一个 GGUF 格式的 sbintuitions 的 sarashina2.2-3b-instruct-v0.1 模型转换，使用 TFMC/imatrix-dataset-for-japanese-llm 构建，准备通过 llama.cpp 进行 CUDA 启用推理。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct-gguf](https://huggingface.co/mmnga/ELYZA-japanese-Llama-2-7b-fast-instruct-gguf) - 📥 1k / ⭐ 45 / 已将 ELYZA 的 7b 日语 Llama‑2 指导模型转换为 GGUF，添加日语词汇以实现 1.8 倍加速，并可在 Llama 2 许可证下使用 llama.cpp 运行。
 * [Llama-3.1-70B-Japanese-Instruct-2407-gguf](https://huggingface.co/mmnga/Llama-3.1-70B-Japanese-Instruct-2407-gguf) - 📥 1k / ⭐ 8 / 一个使用 gguf 格式的 cyberagent 的 Llama‑3.1‑70B‑Japanese‑Instruct‑2407 版本，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 数据构建，并通过 llama.cpp 的 CLI 运行。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5-gguf](https://huggingface.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf) - 📥 1k / ⭐ 2 / 由 tokyotech‑llm 完成的 Llama‑3.1‑Swallow‑8B‑Instruct‑v0.5 的 GGUF 转换，结合 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带用于 llama.cpp 的 Build/Run 指令。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 1k / ⭐ 7 / 一个针对日语微调的 Qwen 3.5‑9B GGUF 模型，使用 Unsloth Dynamic Quantization 2.0、广泛的错误修复、大规模日语校准，并可通过 llama.cpp 在 CPU 上使用 16 GB RAM 和 6 GB 磁盘运行。
 * [karakuri-lm-8x7b-chat-v0.1-gguf](https://huggingface.co/mmnga/karakuri-lm-8x7b-chat-v0.1-gguf) - 📥 1k / ⭐ 4 / GGUF 转换版本的 karakuri‑lm‑8x7b‑chat‑v0.1，基于 TFMC/imatrix 数据集为日语 LLM 构建，可与 llama.cpp 一起使用（例如 `./main -m karakuri-lm-8x7b-chat-v0.1-Q4_0.gguf`）。
 * [nekomata-7b-instruction-i1-GGUF](https://huggingface.co/mradermacher/nekomata-7b-instruction-i1-GGUF) - 📥 1k / ⭐ 1 / Weighted/imatrix 定量的 7B “nekomata‑instruction” 模型可作为 GGUF 文件提供（不同 IQ 和 Q 等级，大小为 2.1–6.4 GB），并附带使用说明链接至 TheBloke READMEs、比较图表，以及 HuggingFace 模型请求页面以获取进一步支持。
 * [llm-jp-4-33b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-33b-thinking-gguf) - 📥 1k / ⭐ 3 / 一个 GGUF 格式的 llm-jp 的 “llm‑jp‑4‑33b‑thinking” 模型版本，基于 TFMC/imatrix 数据集构建，并使用支持 CUDA、flash‑attn 和可调 GPU 内存设置的自定义 llama.cpp 编译运行。
 * [Qwen3-8B-JP-Uncensored-GGUF](https://huggingface.co/ryo559/Qwen3-8B-JP-Uncensored-GGUF) - 📥 1k / ⭐ 1 / 一个 GGUF‑量化的 Qwen3‑8B 日语无审查模型（Q4_K_M 大约 5 GB，Q8_0 大约 8.5 GB），可通过 Ollama 或 llama.cpp 本地运行，并已发布用于研究，使用者需对生成内容承担责任。
 * [aixsatoshi-Honyaku-13b-gguf](https://huggingface.co/mmnga/aixsatoshi-Honyaku-13b-gguf) - 📥 1k / ⭐ 1 / A GGUF‑converted version of aixsatoshi’s Honyaku‑13B model, built with imatrix data from TFMC/imatrix-dataset-for-japanese-llm and usable via llama.cpp (e.g., `./main -m 'aixsatoshi-Honyaku-13b-Q4_0.gguf'`).

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 4M / ⭐ 75 / 聚合了2009年至2024年NicoNico Live的评论日志，总计超过150 GB，包括转移前、转移后以及实时NX‑Jikkyo捕获，提供了一个API，便于检索历史电视广播讨论。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 12k / ⭐ 7 / VOICEVOX‑generated synthetic voice dataset comprising 445,793 .wav files (totaling 577 h 51 m 23 s) built from the ITA, つくよみちゃん, and ROHAN corpora.
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 7k / ⭐ 34 / FineWeb2 Edu Japanese 提供约120 million高质量教育日语文本（≈89.3 billion tokens）来自 FineWeb2，经过 DeepSeek‑API classifier（score ≥ 2.5）过滤，通过 ModernBERT‑Ja‑130M tokenized，并包含一个小-token子集（≤512 tokens）。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 4k / ⭐ 9 / Cauldron‑JA 是一个日语视觉‑语言数据集，包含 44 个子数据集，使用 DeepL API 从 The Cauldron 翻译而来，可通过 HuggingFace’s datasets library 获取，并与原始数据集使用相同的许可证，prompts 在 CC‑BY‑4.0 下发布。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 4k / ⭐ 126 / Nemotron‑Personas‑Japan 是一个开放源代码、CC BY 4.0 许可证的高质量、合成生成的日本人物资料数据集—包含姓名、性别、年龄、背景、婚姻状况、教育、职业和地点—基于真实世界的人口统计、地理和人格分布，并采用概率图模型和 GPT‑OSS‑120B 进行工程设计，以提升多样性、降低偏见、防止模型崩溃、支持主权 AI 发展，并支持商业使用。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 3k / ⭐ 36 / 为高效加载 Hugging Face datasets，重新结构化并重新上传 Galgame VisualNovel 数据集（OOPPEENN/5669737465666C656E63655F44617461337072657330），保留所有原始 audio/text，并提供带多种 game-subset 选项的 extraction script。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 3k / ⭐ 19 / JMTEB 是一个日本文本嵌入基准，包含 5 个任务（聚类、分类、STS、检索、再排序）和 28 个数据集，提供一行评估脚本，并邀请社区贡献。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 2k / ⭐ 47 / 一个用户友好、去重的 CSV 数据集，包含 Aozora Bunko 的公有域日语文本，使用 globis‑org/aozorabunko‑extractor 处理，并已清理以适用于现代日语机器学习。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 101 / 一个包含100个样本的日语指令微调评估数据集，包含已注释的任务——从摘要校正、数学推理到翻译、创意生成和用户意图理解——旨在对微调模型进行手动或自动的5分制评分。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 2k / ⭐ 7 / Japanese Medical VQA 12M 是一个大规模多模态数据集（≈12 M 样本），包含日语医学图像的原始和增强说明文字，均提供源语言和日语版本，以及生成的 VQA 问答对。该数据集以 Parquet/Webdataset 格式发布，并使用 InternVL3.5 对 Open‑PMC‑18M 进行增强，使用 Qwen3‑30B‑A3B 进行翻译，使用 GPT‑OSS 120B 生成 VQA。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 2k / ⭐ 47 / 更新了 JGLUE 数据集卡与加载脚本，适用于由 Yahoo Japan 与早稻田大学创建的日语 NLP 基准，涵盖文本分类（MARC‑ja、JCoLA）、句对分类（JNLI）以及问答（JSQuAD、JCommonsenseQA），发行链接保存在 GitHub 与 Hugging Face 上。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 2k / ⭐ 7 / JMedBench 是一个日语生物医学 LLM 基准，涵盖 20 个数据集，覆盖五个任务（MCQA、NER、STS 等），来源于 MedMCQA、PubMedQA、MMLU 等，每个都有自己的许可，并包含一条说明：翻译可能包含偏差，需要人工审核。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 2k / ⭐ 6 / JamC‑QA 是一个双语基准，涵盖八个日本文化与知识类别的多项选择题，排行榜指标用于比较最先进模型。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 1k / ⭐ 2 / 18,612 个日语翻译的 Python 指令–响应对——使用 GPT‑4o‑mini 生成，保留原始英文提示、代码和示例——为训练、微调、聊天机器人、研究和教育提供多样化的编码任务，全部遵循 MIT 许可证发布。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 1k / ⭐ 5 / 来自 Fate/Stay Night 的角色 “Emilia” 的对话和背景故事数据集，格式化用于训练和评估会话语言模型。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 1k / ⭐ 5 / Japanese JaQuAD，QG‑Bench 的一个子集，提供句子级和段落级的数据，包含高亮的答案词元，用于训练日语问句生成模型，并通过 BLEU4、METEOR、ROUGE‑L、BERTScore 和 MoverScore 进行评估。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 1k / ⭐ 12 / Reazon Speech v2 Japanese dataset 在 Hugging Face 上的镜像，分发依据 CDLA-Sharing-1.0，使用受限于日本著作权法第30‑4条，包含 4,096 个 16 kHz FLAC 音频文件及对应的 TSV/CSV 格式转录文本。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 1k / ⭐ 146 / Japanese Anime Speech Dataset V2 提供 292,637 条已清洗的音频-文本对——约 397.5 小时的 SFW 内容和 52.4 小时的 NSFW 内容——以 128‑kbps MP3 文件形式按安全级别划分，专为训练自动语音识别模型而设计。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 1k / ⭐ 49 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小时匿名 1,033,142 对 eroge 音频-转录配对（主要为女性，含 NSFW），MIT 许可用于学术研究。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 1k / ⭐ 16 / 一份日语和多语种 QA、NLI 与同义句重述数据集的目录，详细说明每个数据集的检索或问答任务及其许可（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 1k / ⭐ 14 / EDINET‑Bench 是一个日本金融基准，用来评估 LLMs 在诸如会计欺诈检测、盈利预测和行业预测等任务，使用十年的 EDINET‑API 披露报告，提供构建和评估代码，并将数据集重新许可为 PDL 1.0。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 1k / ⭐ 6 / 日本 MC4 数据集卡 (mc4-ja)
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 1k / ⭐ 120 / ReazonSpeech 是一个免费、FLAC 编码的日语语音语料库，附带转录，提供五种规模，从 8.5 h 到 35,000 h，可通过 Hugging Face 下载，遵循 CDLA‑Sharing‑1.0 许可证，且使用受到《日本著作权法》第30‑4条的限制。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 999 / ⭐ 5 / 一个受限、非商业派生数据集，基于 EDINET XBRL 财务数据，禁止再分发、AI 训练和商业用途，请求访问需人工批准。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 945 / ⭐ 20 / JMMMU 是一个日语多模态基准，已扩大十倍至 1,320 个具有文化多样性的问题（720 个与文化无关，600 个与文化相关），由母语专家翻译，现在设有公开排行榜。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 926 / ⭐ 14 / ‘wikipedia-ja-20230720’ 日本维基百科快照的数据集卡。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 813 / ⭐ 89 / 一个自动翻译的日语版本的databricks‑dolly‑15k数据集，许可为CC‑BY‑SA‑3.0，最后更新于2023‑05‑11。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 797 / ⭐ 61 / AnswerCarefully Dataset提供日语和多语种数据，用于商业或非商业LLM安全增强，禁止任何其他用途——包括安全规避——允许带署名的衍生作品，并声明不承担因伤害或服务变更导致的责任。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 762 / ⭐ 14 / JMMLU 是一个日语大型多任务语言理解基准（Benchmark），包括 7,536 道教师精心制作的问题，覆盖 56 个学科，包括专业医学、心理学、会计、哲学以及各种高中学科。
 * [Hadou-Voice-Dataset](https://huggingface.co/datasets/hadou1225/Hadou-Voice-Dataset) - 📥 731 / ⭐ 2 / 由哈多制作的日语语音数据集，包含966段“Calm Voice”片段（约114分钟）和424段“ITA Corpus”片段（约39分钟），可用于 AI 训练、TTS、声音转换、LoRA 创建或直接在任何项目中使用，并可选择性署名。
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 712 / ⭐ 3 / 从 Hugging Face (if001/oscar_2023_filtered) 加载 312,396 行过滤后的 Oscar 2023 数据集，并在 if001/HojiChar_OSCAR_sample GitHub 仓库中提供示例代码。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 652 / ⭐ 5 / STAIR‑Captions，发布于2017年，提供820,310条日语字幕，用于字幕生成、多模态检索和图像生成，并配有详细注释、元数据以及Creative Commons BY‑4.0 license。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 637 / ⭐ 3 / A 2010 Japanese Web Corpus, uploaded to HuggingFace and licensed for research per the 2009 copyright reform, 包含来自基于形态学的解析和转换脚本的自动标点化文本。
 * [Wiki-JA-Pair](https://huggingface.co/datasets/llm-jp/Wiki-JA-Pair) - 📥 623 / ⭐ 2 / 由 jawiki-20250501 文章构建的日本维基百科图像说明数据集，包含1,054,434个唯一（图片，说明）对和1,047,565张已下载图片，附有尺寸、哈希值、页面信息等元数据，并且下载成功率为99.35%。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 601 / ⭐ 7 / JHumanEval 是 HumanEval 基准的人工翻译日语版本，提供 164 个 Python 编程问题，配有并行的英文和日文注释，用于评估日语 LLM 的代码生成，同时保留原始英文错误。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 590 / ⭐ 12 / JaQuAD 是 2022 年的日语 QA 数据集，包含 39,696 对 SQuAD‑style 的抽取式问题‑答案对，取自 Wikipedia，文件总大小 73.2 MB。使用 BERT‑Japanese 微调时，获得 78.92 % F1（63.38 % EM）。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 574 / ⭐ 5 / JAMMEval 是七个日本 VQA 数据集的精炼基准，经过两轮人工注释以消除歧义和非视觉问题，能够为多模态日本任务提供对视觉‑语言模型的可靠评估。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 567 / ⭐ 8 / Rakuda 提供 40 道日语问题——开放式的历史、社会与政府问题，以及针对地理的特定问题——用于对日本 AI 助手进行基准测试，类似于 vicuna‑eval，并且可以使用 `datasets.load_dataset` 加载。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 561 / ⭐ 3 / WildGuardTestJP 是一个包含 1,725 个样本的日语评估数据集，经过多阶段精炼管道（Seed‑X‑PPO‑7B、gpt‑oss‑120b、Qwen2.5‑72B‑Instruct、gemma‑3‑27b‑it）忠实翻译自 WildGuardTest，并以 ODC‑BY 许可证在 Hugging Face 上发布。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 559 / ⭐ 20 / 一个用于评估 Retrieval‑Augmented Generation（RAG）的日语 QA 数据集，由 JAQKET 问题和 Wikipedia 段落以及金标准检索相关性标签构建，并在 HuggingFace 和 GitHub 上发布，主要依据 nDCG@10 评分。
 * [honkoku-lines](https://huggingface.co/datasets/yuta1984/honkoku-lines) - 📥 549 / ⭐ 2 / 一份公民科学数据集，包含 1,169,304 条已转录的日语历史行，来源于 79,086 张 IIIF 页面图像，以约 1 GB 的 WebDataset 分片形式提供，每个分片含有高度为 256 像素的 JPEG 行裁剪以及相应元数据，适用于训练/验证/测试划分。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 543 / ⭐ 159 / 日本动漫语音数据集提供73,004对音频-文本（总计110小时，已从V1升级至V5），用于提升ASR模型，例如OpenAI的Whisper，按开放许可证提供给所有使用，欢迎署名。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 535 / ⭐ 13 / LLM‑jp 提供了一个日语指令调优数据集，该数据集是 DeepL 翻译自 oasst2 的英文子集（来自 kunishou/oasst2‑135k‑ja），并由 Kiyomaru 和 Kodama 编译。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 534 / ⭐ 5 / 数据集卡片详细说明了日语变体 “mc4‑ja‑filter‑ja‑normal”，后续信息正在待补充。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 527 / ⭐ 3 / 日语指令数据集，具有 632,636 条多轮样本（约 6.35 B 个 token），并包含 GPT‑OSS‑120b 的推理轨迹，用于跨 135 个金融主题和 20 个通用主题的开放式、数学、写作和 MCQA 任务，旨在微调 LLM 在金融领域的推理能力。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 508 / ⭐ 3 / 日语维基百科句子被转换为各种嵌入和 FAISS 索引，提供 Hugging Face Space 演示、转换脚本，以及对搜索、问答和 OpenAI text-embedding-3-small 在 RAG 中的评估；嵌入模型为 OpenAI‑licensed，其他为 CC‑BY‑SA‑4.0。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 506 / ⭐ 2 / Hugging Face 镜像的 ABEJA‑CC‑JA 数据集，托管在 OpenData AWS 注册表上，并链接到 Abeja 的技术博客。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 491 / ⭐ 35 / Syosetu711K 是一个约 711,700 本小说的日本数据集，采自 2023 年 3 月 26‑27 日从 小説家になろう 抓取，提供全文及元数据（标题、作者、NCode、简介等），用于无监督文本生成和分类任务。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 475 / ⭐ 6 / Range3 的 wikipedia‑ja‑20230101 仓库提供只包含日语维基百科文本的 Parquet 文件，这些文件是从完整维基百科数据集中提取的，并使用 Python 代码生成。
 * [joyo-kanji-yomi-benchmark-parakeet](https://huggingface.co/datasets/Parakeet-Inc/joyo-kanji-yomi-benchmark-parakeet) - 📥 469 / ⭐ 4 / 一套基准数据集和评估工具包，用于衡量日语G2P、形态分析器以及TTS系统在从文化厅的常用汉字表中朗读汉字时的准确性，包含4,512个汉字-发音对，每个对都有三个标注示例句子，并为多种读法提供详细注释。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 451 / ⭐ 6 / 数据集简介：“oscar2301‑ja‑filter‑ja‑normal”，是 Oscar 语料库的日语过滤版和普通子集。
 * [EliteVoiceProject](https://huggingface.co/datasets/Elite35P-Server/EliteVoiceProject) - 📥 446 / ⭐ 13 / 非官方的Hololive VTuber樱井美子（Sakura Miko）语音数据集，用于语音识别研究，按来源平台组织并分为训练/测试文件夹，使用受 Hololive 粉丝创作指南约束，版权归 Cover Corp 所有。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 442 / ⭐ 24 / cc100-ja 是 cc100 数据集日语部分的集合，提供为分片的 Parquet 文件。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 434 / ⭐ 15 / 用于《大型语言模型简介》一书的 JGLUE 数据集数据卡，来源于原始仓库，代码采用 CC BY‑SA 4.0 许可证，数据按发行者的许可协议，引用 Kurihara & Kawahara（日本语），并基于 Shunsuke Kitada 的仓库构建。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 424 / ⭐ 143 / 用于微调 LLMs（如 LoRA）的日语指令聊天数据集，包含 9 M+ 样本，最近已更新，删除授权的 Alpaca 数据，并清理了 Wikipedia 和 ALT 输出，采用 CC‑BY‑SA 4.0 许可证发布。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 388 / ⭐ 5 / 一份日语开放域问答数据集JAQKET，提供了多项选择题风格的问答（v1.0）和自由文本答案生成（v2.0），v1.0包含13 061个训练样本和271个验证样本，v2.0包含2 154个训练样本和1 164个验证样本。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 379 / ⭐ 2 / JCommonsenseQA 是一份日语的多项选择常识推理数据集——CommonsenseQA 的改编版本——其授权为 CC BY‑SA 4.0，并以 doi:10.5715/jnlp.30.63 引用。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 373 / ⭐ 2 / 一个多模态日语表格问答数据集，用于直接从年度证券报告表格中提取单元格值，提供图像、带边界框的 OCR 文本、问题和答案，并遵循 CC‑BY‑4.0 许可。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 362 / ⭐ 10 / llm‑jp‑instructions 是一个手工整理的日语指令数据集（v1.0），提供训练、验证和测试拆分，可通过 load_dataset 访问。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 356 / ⭐ 5 / 包含日语和英语网络语料库的集合——包括一个 9 B‑token 日语集（JA‑WEB‑9B）、63 B‑token 英语和日语集（EN‑WEB‑63B、JA‑WEB‑63B）以及合成版本，如改写版 JA‑PARAPHRASE‑63B、指令式 JA‑INSTRUCT‑63B 和翻译版 JA‑TRANSLATE‑63B——用于在数据受限环境下研究日语 LLM 预训练的数据增强。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 355 / ⭐ 4 / 提供了一个日语搜索/问答数据集，其中包含按查询计算的分数，这些分数是由五个多语言/日语重排序器（例如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）计算的，数据集包括每个查询约200个正例和负例文档的平均分数。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 321 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 数据集的 500 份样本子集，采用 CC BY 4.0 许可，用于基准测试 EvoVLM‑JP‑v1‑7B。
 * [Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k) - 📥 315 / ⭐ 8 / 一份由 deepseek-ai/DeepSeek-V3-0324 生成的39,600样本日语小说写作任务数据集，包含两轮 OpenAI 风格对话（包括可选的 NSFW 内容），并以 MIT 许可证发布。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 306 / ⭐ 25 / AI生成的动漫插图，使用英文提示，并基于Phi‑3 Vision的字幕（英文和日文），已发布到公共领域，供免费使用。
 * [oscor-2301-ja-text-content](https://huggingface.co/datasets/ayousanz/oscor-2301-ja-text-content) - 📥 304 / ⭐ 2 / 从 OSCOR-2301-ja JSON 文档的 “content” 字段中提取的文本文件，由一个 Python 脚本生成，该脚本解析每一行 JSON 并将 content 值写入输出文件。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 293 / ⭐ 18 / 一份 NLP‑ready dataset，包含从 2024 年 1 月的 HTML dump 中提取的 Wikipedia articles，保留段落结构、元数据（如 disambiguation、sexual、violent flags、templates、timestamps）以及托管在 GitHub 上的 extraction scripts。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 288 / ⭐ 26 / 此仓库托管了 OpenAssistant/oasst1 数据集的日语翻译，包括带有错误标记的自动翻译条目，大约 2,000 条人工修正，一个基于聊天格式的子集，以及将数据转换为用于微调的指令-输出对的脚本。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 287 / ⭐ 4 / 一份采用 Advanced SubStation Alpha（SSA/ASS）格式的日本动漫字幕数据集，可通过 `ass` Python 库或像 Aegisub 这样的字幕编辑器使用，按 ODC‑BY 许可协议发布。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 283 / ⭐ 6 / JetCopper‑10B 是一个日本文本语料库，约 4.7 十亿个标记（再加上 0.9 十亿英文代码），来源于 CC‑100、OSCAR‑2301、HPLT v1.2 和 wiki40b‑ja，在清洗和去重后用于预训练 Contrail‑200m‑64k，以供 LOCAL AI HACKATHON #000 calm2‑chat 使用，虽然它缺少句子边界和困惑度过滤。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 281 / ⭐ 47 / Galgame_Speech_ASR_16kHz 是一个 16 kHz 的 ASR 数据集，包含 3.75 百万对（≈5,354 小时），源自 Galgame_Dataset，遵循 GPL v3.0，禁止商业使用，并要求任何训练的模型必须开源（可选引证）。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 279 / ⭐ 6 / Japanese XL‑Sum subset 通过 PaLM‑2 15-gram 重叠过滤，包含 4,215 训练样本，758 验证样本和 766 测试样本。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 279 / ⭐ 22 / 一个名为MOMIJI的日语网页文档和图像数据集（≈5600万页，1100亿字符，2.49亿张图片），旨在训练视觉语言模型，并配有交互式可视化工具和用于生成文本字段的实用脚本。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 270 / ⭐ 3 / 一个清理过的日语网络语料库（例如 mc4‑ja），通过无监督学习聚成大约10,000组，可用于合法分析，只在“out”文件夹中列出一些 Parquet 格式的文件，并可通过 Git LFS 下载。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 268 / ⭐ 7 / 一个量化语音与文本输入在语音语言模型之间智能差距的数据集，由从 Elyza‑tasks‑100、M‑IFEval 与 JamC‑QA 基准生成的音频组成，分为四个子集，文本采用 CC‑BY‑SA 4.0 许可，音频仅限非商业用途且不可再分发。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 256 / ⭐ 4 / 一个266小时的日语音频数据集，来源于Emilia数据集，并通过Scribe v1（ElevenLabs STT/ASR）进行分类，同时使用Facebook音频美学预过滤，可在HuggingFace和Discord上供协作使用。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 255 / ⭐ 16 / 日本角色扮演对话数据集，过滤后仅包含足够长度的多发布者记录、标准化的发布者名称和均衡的主要发言者，旨在用于机器学习应用。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 248 / ⭐ 36 / 一个时长为409小时的日本 eroge 语音数据集，使用 2-pass loudnorm（‑23 LUFS，‑1 dB 峰值，11 LRA）处理，已由 litagin/anime-whisper 转录、匿名化，存储为 WebDataset（FLAC、JSON、TXT），主要包含女性声音，可能存在 AI 转录错误，并采用 MIT 许可证用于学术研究。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 247 / ⭐ 17 / 104 GB、370 万文件的 Galgame 语音数据集，采样率 16 kHz，带情感标签（由 LLM 自动标注，准确性未保证），需要符合 GNU GPL v3 协议，禁止商业使用，并要求基于该数据集训练的模型必须开源。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 246 / ⭐ 5 / 可供免费下载的81岁日本女性语音语料库（包含原始和去噪 wav、音素/假名+韵律标签），免费学术使用时请注明来源为“Fusic Saoyoshi Voice Corpus”。
 * [Umamusume-voice-transcription](https://huggingface.co/datasets/TLME/Umamusume-voice-transcription) - 📥 244 / ⭐ 8 / 一份用于《偶像大师 灰姑娘女孩》的转录数据集，包含77个角色的语音与对应的音频片段，总时长约为12,000秒，共计50匹命名马。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 243 / ⭐ 8 / Livedoor News Corpus 提供了一个日语新闻文章数据集，划分为 5,894 条训练样本、737 条验证样本和 736 条测试样本，已清除 HTML 标签，并在 Creative Commons Attribution‑NoDerivs 许可证下发布。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 237 / ⭐ 43 / 一个排行榜，按语义准确度对大型语言模型进行排名，用于将日文视觉小说翻译成英文。该排行榜使用256个样本的余弦相似度，并报告 chrF 分数，以与 Sugoi Translator、Google Translate、Naver Papago 和 Alibaba Translate 等工具进行比较。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 230 / ⭐ 33 / 一份去除了 izumi-lab 的 llm-japanese-dataset 中英日翻译数据的日本聊天数据集，旨在通过 LoRA 对日本 LLM 进行指令-响应任务的微调，并以 CC‑BY‑SA 4.0 发布。
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 228 / ⭐ 5 / 使用 Whisper Large‑V2 对视频中的 Makise Kurisu VN 对话进行转录，并用 pydub 将文本拆分为片段；未清理的文本用于 TTS 模型训练，且不属于作者。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 226 / ⭐ 3 / 本数据集说明书用于本书《Introduction to Large‑Scale LLM II》中的 ja‑vicuna‑qa‑benchmark，并由 llm‑jp‑eval 创建，供跨数据集日语 LLM 评估使用（Apache 2.0）。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 220 / ⭐ 17 / Jagle 是一个约 920 万实例的日本多模态后训练数据集，构建自图像–文本对和 PDF 文本，用于训练 LLM‑jp‑4‑VL 9B beta，并已被证明能提升日语视觉语言任务性能。
 * [japanese-math-synthetic-108k](https://huggingface.co/datasets/yamaTK/japanese-math-synthetic-108k) - 📥 217 / ⭐ 2 / 一个经过清理、无重复的日语数学题目数据集，供 LLM‑JP 2026 调参比赛使用，覆盖初中到高中 IIIC 水平，由 GPT‑OSS 120B 生成并验证，包括详细提示、逐步推理、求解器解决方案，以及跨年级和主题类别的结构化 JSON 架构。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 215 / ⭐ 18 / 一个190 M对的JSONL数据集，用于日语假名到汉字转换，包含“左上下文–输入–输出”三元组，并预训练模型（medium、small、xsmall）以及AJIMEE-Bench基准测试。该数据集以CC BY‑SA 4.0授权发布，子集来源于Wikipedia和Common Crawl。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 212 / ⭐ 7 / 将日语数据集重新格式化为适合 SentenceTransformers 的列和结构，并根据 RelRank 分数从多个 HuggingFace 来源过滤成正样本（≥0.7）和负样本（≤0.3）的对，用于对比学习。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 211 / ⭐ 3 / 一个大型、基于时间戳的 JSONL 数据集，包含来自 2ch.sc 的日本匿名论坛帖子，详细列出主题编号、标题、地区、板块名称、回复数，以及帖子数组，包括用户、邮件、日期、ID、正文和可选标题字段。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 206 / ⭐ 2 / 一个日语在线广告数据集，包含五个 NLP 任务——ad acceptability、consistency、performance estimation、A3 recognition 和 similarity，并以 TSV 格式提供 train/dev/test 拆分。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 204 / ⭐ 5 / SNLI自然语言推理基准的日语翻译（JSNLI），以TSV格式提供，前提和假设已按形态素分段，提供过滤与未过滤训练集，以及在CC BY‑SA 4.0下的3,916对验证集。
 * [OpenSakura-DS-260220-LN-ja-zh-COT-Lilith](https://huggingface.co/datasets/OpenSakura/OpenSakura-DS-260220-LN-ja-zh-COT-Lilith) - 📥 204 / ⭐ 2 / OpenSakura-DS-260220-LN-ja-zh-COT-Lilith 是一个包含1.64百万行的日语到中文轻小说翻译数据集（约18 GB），采用基于映射的5路拆分，保留推理内容和结构化字段，如 uuid、episode 和 segment 索引。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 203 / ⭐ 27 / WRIME 数据集是一个包含 42,200 条帖子的日本语集合，帖子已为作者、三位读者及其平均值标注了 Plutchik 的八种情感，结构为 40k 训练集、1.2k 验证集和 2k 测试集，用于情感分析任务。
 * [swallow-magpie-ultra-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-magpie-ultra-v0.1) - 📥 202 / ⭐ 5 / 一套日英指令调优数据集（每类 42k 对），作为 Swallow‑Magpie‑Ultra‑v0.1 的一部分发布，用于训练 tokyotech‑llm 模型，来源于 magpie‑ultra‑v0.1，并具有平均良好的质量。
 * [CABankSakuraCHJP](https://huggingface.co/datasets/Fhrozen/CABankSakuraCHJP) - 📥 200 / ⭐ 2 / 日本 CallHome 语料库：120 位说话者，200 条电话录音（每条最长 30 分钟），来自美国，通过免费 LDC 机器人操作员录制，每通电话支付 20 美元，并按 80/20/100 的比例划分为训练集/开发集/评估集。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 200 / ⭐ 2 / Japanese Common Voice 17.0 子集已过滤为 649 个客户端 ID，每个拥有 30–300 个样本，按 8:2 分为训练/验证集，批量为 1,000‑样本 Parquet 文件，总计 45,668 个样本（CC0 许可）。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 200 / ⭐ 4 / JFWIR 是一个大规模的日语信息检索数据集，包含超过6400万份文档-查询对——来自高质量教育网页内容生成，具有七种查询类型和难负样本，以提升对比学习并在 JQaRA、MIRACL(ja)、jsquad 和 JaCWIR 等任务上进行基准测试。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 195 / ⭐ 16 / 一份日语 Alpaca 风格的合成数据集，使用 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 创建，并通过 Deepinfra 进行细化，其中“_cleaned”条目已在 Apache 2.0 许可证下验证了指令清晰度、语言一致性和相关性。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 193 / ⭐ 2 / COVID‑19 日本推特数据集提供了日本推文 ID 与评估码（63–68），用于标识 COVID‑19 相关性以及事实/观点状态，从而支持文本分类研究。
 * [Japanese-Heron-Bench](https://huggingface.co/datasets/turing-motors/Japanese-Heron-Bench) - 📥 189 / ⭐ 11 / Japanese‑Heron‑Bench 是一个日语 VLM 基准测试，由七个子类别的21张图片组成，每张图片配有三类问题（Conversation、Detail、Complex），共计102个查询，全部采用 CC BY 许可证。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 188 / ⭐ 21 / 用于日英文本简化和翻译的 SNOW T15/T23 日语简化语料库数据卡，包含 50 k 条手工对齐的原文、简化日语（≤2 k‑词汇量）和英语翻译记录，以及 35 k 条扩展集。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 188 / ⭐ 2 / KokoroChat 是最大的日本心理咨询对话数据集——由 480 名受过训练的辅导员进行 6,589 次角色扮演会话，每次平均 91 条发言——包含丰富、长篇对话，详细的 20 维客户反馈，并支持同理响应生成、对话评估和心理健康语言建模方面的研究，并已被 ACL 2025 接收。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 185 / ⭐ 17 / oasst1‑21k‑ja 是由 DeepL 从英文 OASST1 子集派生的日语指令调优数据集，透过日本 LLM‑jp 合作项目创建；请联系 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 和 Okamoto。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 176 / ⭐ 18 / Databricks‑dolly‑15k‑ja 数据集是 DeepL 翻译的日本语版 databricks‑dolly‑15k，用于指令调优，由日本 LLM‑jp 项目创建，并由 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 和 Takumi Okamoto 撰写。
 * [Furigana-Aozora-Speech](https://huggingface.co/datasets/Calvin-Xu/Furigana-Aozora-Speech) - 📥 170 / ⭐ 2 / 已处理所有原始文本文件，生成了一个包含3,361,443 条目、去除重复项且剔除缺少kanji 的干净语料库。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 168 / ⭐ 82 / 一份日本网络小说章节数据集，配有英文粉丝翻译，在版本 2 中扩展到 106K 条对齐句子，包含系列元数据，无质量过滤，并在公平使用/Apache 2.0 下分发，同时提供下架条款。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 168 / ⭐ 24 / AutoWikiQA 是最大的免费日语问答数据集，提供超过 230 万个手工过滤的问答对，这些对是使用 Swallow‑MX 和 LLMs（不使用基于规则的模板）从维基百科自动生成的，用于支持知识教学和检索增强生成应用。
 * [DEJIMA-dataset](https://huggingface.co/datasets/MIL-UT/DEJIMA-dataset) - 📥 168 / ⭐ 5 / DEJIMA 是一个日语规模的网络数据集，包含 3.88 M 张图像与 LLM‑generated captions 和 VQA answers 配对，通过严格过滤、去重、基于检测的证据提取和 grounding constraints 生成，并提供多种 captioning 与 VQA 变体供分析。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 167 / ⭐ 2 / 由重述过的维基百科文本生成的LLM生成的日语查询和答案的数据集，采用CC‑BY‑SA 4.0发布。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 166 / ⭐ 4 / 由Guo, Mandy；Dai, Zihang；以及Vrandečić, Denny 所著的 Wiki40B 数据集的日语子集已被重新格式化。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 166 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) 提供了一个多分类 QA 数据集——涵盖 Integration、Reasoning、Logical、Table 和 Abstention——旨在评估日本 RAG 生成器，采用人工努力和 GPT‑4.1 构建，并在 CC BY‑SA 4.0 许可下发布。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 163 / ⭐ 9 / JSICK 是一个日英 NLI 和 STS 数据集，基于翻译 SICK 语料库创建，包含一个压力测试集合，用以检验词序和格助词处理，共有 1,666、797 与 1,006 对句子用于不同的语法关系。
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 161 / ⭐ 6 / 去重、已清理（NFKC 规范化）的查询–段落对集合来自 mQA 数据集，其中 `pos_ids` 和 `neg_ids` 索引到对应的集合以便轻松检索，按原始数据的条款授权。
 * [joyo-kanji-yomi-benchmark](https://huggingface.co/datasets/sbintuitions/joyo-kanji-yomi-benchmark) - 📥 158 / ⭐ 10 / 一项日语 TTS 基准测试，评估所有 2,136 个常用汉字的发音，共 4,378 种读法，使用 13,095 条由母语者验证的句子，每条句子针对单个读法，并标注以便在 MIT 许可证下自动计算 CER。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 157 / ⭐ 16 / 一个用于测试角色‑LLMs的简单 Zundamon 角色设定数据集——由线上来源和管理数据编制——以 zmnjp.jsonl 和 zmn.jsonl 格式提供，并在指定许可下发布。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 156 / ⭐ 3 / 一份包含 64,139 条标注有生物性别的日语姓名的数据集，呈现为汉字、假名和平罗马字，其 44.9k 训练集、6.41k 验证集和 12.8k 测试集划分已在 ISDA’23 被接受。
 * [hh-rlhf-12k-ja](https://huggingface.co/datasets/llm-jp/hh-rlhf-12k-ja) - 📥 156 / ⭐ 14 / 由LLM‑jp使用DeepL制作的hh‑rlhf 数据集子集的日语翻译，作者按字母顺序列出，联系邮箱 llm-jp(at)nii.ac.jp。
 * [KokushiMD-10](https://huggingface.co/datasets/humanalysis-square/KokushiMD-10) - 📥 155 / ⭐ 7 / KokushiMD-10 是一个多语言基准，面向十种日本医疗专业，提供文本和图像的单选、多选、计算以及填空题，并附有思路链解释，可分为独立的日语、英语或混合拆分。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 153 / ⭐ 33 / 通过发布数据集、自动评估框架以及 Claude 3.5‑Sonnet、GPT‑4o 等模型的比较结果，提供跨金融、电信、制造、公共、零售五个行业领域的日语 RAG 基准。
 * [danbooru-ja-tag-pair-20241015](https://huggingface.co/datasets/p1atdev/danbooru-ja-tag-pair-20241015) - 📥 152 / ⭐ 9 / 一个包含150K条目的Danbooru标签与日语翻译配对的数据集（截至2024年10月15日更新），基于扩展的wiki源构建，使用FastText过滤以移除非日语标签，并通过少量示例Calam Chat翻译完成缺失条目。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 145 / ⭐ 11 / 由所提供的Python脚本生成的三份 Parquet 文件，包含 Wiki40B 数据集的日语子集。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 145 / ⭐ 11 / 一个高质量的合成日语数学题数据集，具有经过验证的思考链推理，采用 Qwen2‑7B‑Instruct 翻译 PRM800K 和 GSM8K 并进行正确性筛选后构建，可通过 Hugging Face 数据集库获取。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 145 / ⭐ 9 / JMMMU‑Pro 是一个基于图像的日语多模态基准，通过使用真实模型生成视觉问题并进行人工验证创建，揭示当前开源 LMM 在其上的表现不佳，并提供了一种成本效益高的未来 VQA 基准开发方法。
 * [NMLE](https://huggingface.co/datasets/longisland3/NMLE) - 📥 144 / ⭐ 5 / 日本国家医学执业考试数据集（NMLE）提供来自110–117期考试的结构化问题，用于模型评估、进化合并和RAG任务，授权为CC‑BY‑NC‑ND4.0，仅限非商业使用。
 * [Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k) - 📥 143 / ⭐ 4 / 39.6k 条合成日语角色扮演数据集，由 gpt‑4o‑mini 生成，包含每段对话5–10回合以及元数据键，如类型、年龄标签、世界/场景/用户/助手设置、语气和 OpenAI 消息格式，采用 CC‑BY‑NC‑SA 4.0 授权。
 * [ogiri-bokete](https://huggingface.co/datasets/YANS-official/ogiri-bokete) - 📥 141 / ⭐ 4 / 来自Bokete众包笑话网站的仅日语数据集，分为三项任务——文本到文本、图像到文本以及文本在图像中的完成，每项分别有500个图像提示（对应2355个答案）和各100个其他两项（≈900个答案），通过OCR处理并过滤不当内容。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 139 / ⭐ 29 / 由手工从政府网站提取的日本 FAQ 数据集，采用 CC-BY-4.0 许可，旨在用于大型语言模型的指令调优和 RAG 测试，提供高质量问答对及来源 URL。
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 139 / ⭐ 4 / Arknights Waifus的JP语音文本数据集：10,905个日语语音片段（总计26.3小时），来自单一角色，适用于微调或评估ASR/ASV模型。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 135 / ⭐ 4 / 一个来自 livedoor News Corpus 的日语命名实体识别数据集——在书籍 *大規模言語モデル入門* 中使用，并由 RONWIT 提供——包含经过清理的 HTML 文章，采用 CC BY‑ND 2.1 JP 许可证。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 135 / ⭐ 11 / 来自 llm-jp-corpus-v3 的 kaken 子集的日文文本，使用 Qwen/Qwen2.5‑32B‑Instruct 翻译成英文，并以 CC‑BY 4.0 许可发布为开放的日英平行语料库，该许可继承了原始数据集的条款。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 134 / ⭐ 26 / 收集自个人的数据集，包含2300万条日本网络小说记录（约80亿字符），仅可在请求后用于合法的机器学习用途。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 133 / ⭐ 6 / 20,800 文件的 WAV 数据集，包含 195 位日本 AItuber 人格——包括参考、原始、描述性和情感性发言，并提供详细的人格和声音元数据，准备通过数据科学 APIs 检索。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 132 / ⭐ 14 / 一份商业用途的 180 万例日语翻译版本的 OpenMathInstruct‑1 数学指令调优数据集——该数据集由 GSM8K 和 MATH 基准问题生成，并使用经过 Mixtral‑8x7B 解答验证正确性的解决方案构成，且以 NVIDIA 授权发布，在重新分发时需继承许可证。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 129 / ⭐ 14 / 从维基百科提取的日语命名实体识别（NER）数据集，采用 CC‑BY‑SA 3.0 许可证，由 Stockmark Inc. 创建。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 124 / ⭐ 9 / 面向 llm‑book/wrime‑sentiment 的数据集卡，提供从 WRIME 派生的二元日语情感分析集，依据 Avg. Readers_Sentiment 标记为正向或负向（可选包含中性案例），用于《大型语言模型导论》一书的示例数据。
 * [jmultiwoz](https://huggingface.co/datasets/nu-dialogue/jmultiwoz) - 📥 120 / ⭐ 8 / JMultiWOZ 是一个大型日语多域任务导向对话数据集，包含 4,246 条 Wizard‑of‑Oz 收集的对话，覆盖六个领域（餐厅、酒店、景点、购物、出租车、天气），提供用户目标、对话状态和发言，用于训练对话状态跟踪与生成模型。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 120 / ⭐ 2 / WAON 是一个大型、高质量的日语图文配对数据集，采用尺寸、SigLIP‑score 过滤和去重（按 URL、标题和 pHash）构建，并在 HuggingFace 上以 Apache 2.0 许可证公开，用于信息分析。
 * [mbpp-ja](https://huggingface.co/datasets/llm-jp/mbpp-ja) - 📥 118 / ⭐ 3 / mbpp-ja 是一个日语协作 LLM-jp 项目，使用 DeepL 以及 HuggingFace 和 GitHub 的原始 mbpp 数据集，由 Namgi Han、Masatoshi Otake、Shintaro Ozaki 与 Yusuke Miyao 编写。
 * [Magpie-Tanuki-8B-annotated-96k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-annotated-96k) - 📥 118 / ⭐ 6 / 使用 Magpie 方法学对 Tanuki‑8B 进行注释，创建了一个包含 96,000 样本的数据集，并使用基于 calm3 的提示为每条指令评估难度、质量和类别。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 118 / ⭐ 6 / 日本动漫语音数据集，原始 joujiboi/japanese‑anime‑speech‑v2 集合的拆分版本。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 116 / ⭐ 17 / 数据集“japanese_alpaca_data”基于masa3141的Japanese‑Alpaca‑LORA工作，提供了一个精心策划的日语 Alpaca 数据集，用于研究和应用。
 * [fgo_voices_jp](https://huggingface.co/datasets/deepghs/fgo_voices_jp) - 📥 115 / ⭐ 16 / FGO Waifus的JP Voice‑Text 数据集：一个包含30,800条记录、66.4小时日本音频的集合，收录单一配音演员角色台词（每句约7.76秒），适用于ASR/ASV微调与评估。
 * [liz-nojaloli-ja-ds](https://huggingface.co/datasets/ebisuke/liz-nojaloli-ja-ds) - 📥 112 / ⭐ 3 / MIT‑licensed hand‑crafted Japanese dataset for training “liz‑nojaloli‑ja,” with accompanying Python code linked via Qiita and intended for future RLHF preparation.
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 110 / ⭐ 24 / RealPersonaChat 是一个约 14,000 条对话的日语语料库，包含说话者的人格和个性特征，提供发言数据（含评估分数）以及详细的说话者档案（人格、Big Five 分数、人口统计）。
 * [azurlane_voices_jp](https://huggingface.co/datasets/deepghs/azurlane_voices_jp) - 📥 110 / ⭐ 9 / 一个日语语音文本数据集，包含 30 160 条录音（≈75.8 小时），来自单个角色的声音，可用于微调或评估 ASR/ASV 模型。
 * [kansaiben](https://huggingface.co/datasets/shirochange/kansaiben) - 📥 110 / ⭐ 4 / 包含 400 个标准日语提示及其对应的自然关西方言（大阪）回答的数据集，已按微调 LLM 的方式进行格式化，用作亲切的关西口音 AI 助手。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 109 / ⭐ 3 / 一个日语版的 BIG‑Bench Hard 数据集（bbh‑ja），提供评估问题和 Chain‑of‑Thought 提示，分别以 JSON Lines 和 YAML 格式呈现，由 PLaMo 模型生成翻译。
 * [wikidata-parallel-descriptions-en-ja](https://huggingface.co/datasets/Mitsua/wikidata-parallel-descriptions-en-ja) - 📥 108 / ⭐ 9 / 一份可直接训练的英日机器翻译语料库，来自 Wikidata 描述，已清洗并去重为 JSONL 文件，可用于 Hugging Face transformers，并在 CC0 1.0 许可下提供。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 108 / ⭐ 2 / 将 JA CallHome 数据集转换为 WAV，并提供 JSON 结构化元数据和用于评估的 RTTM 说话人文件。
 * [modern_haiku](https://huggingface.co/datasets/p1atdev/modern_haiku) - 📥 107 / ⭐ 4 / 来自现代俳句协会的37,158条现代日语俳句精选数据集，每条记录包含ID、文本、作者、可选审阅者注释、季节标签，以及关联的季语(kigo)词（带发音和别名）。
 * [amenokaku-code-instruct](https://huggingface.co/datasets/kunishou/amenokaku-code-instruct) - 📥 106 / ⭐ 17 / 一份包含5,200个代码生成任务的日语指令数据集——其中1,050个用于代码生成，150个用于行为检查，4,000个用于 bug 修复——并辅以180个 JaxTon/Java 示例，所有内容均来自商业授权编程材料，并在清晰许可下发布。
 * [msmarco-ja-hard-negatives](https://huggingface.co/datasets/hotchpotch/msmarco-ja-hard-negatives) - 📥 106 / ⭐ 3 / 日本语硬负样本挖掘版的MS MARCO翻译数据集（msmarco‑ja），采用NFKC规范化、重复过滤以及基于BAAI/BGE重排序器的选择，用来训练SPLADE模型，并与mMARCO(ja)进行统计比较，显著提升正样本率。
 * [swallow-gemma-magpie-v0.1](https://huggingface.co/datasets/tokyotech-llm/swallow-gemma-magpie-v0.1) - 📥 102 / ⭐ 3 / 合成指令调优的日语问答数据集 “Swallow‑Gemma‑Magpie‑v0.1” 包含 148k 个由提示生成的问题–答案对（例如宏观经济学、保险、化学），这些对是使用 Google 的 gemma‑2‑27b‑it 产生并用于训练各种 Llama‑3.1 Swallow 模型。
 * [J-ResearchCorpus](https://huggingface.co/datasets/kunishou/J-ResearchCorpus) - 📥 101 / ⭐ 32 / 一份高质量的日语文本数据集（约3900万字符），由CC-BY-4.0学术论文和会议记录编译而成（如ACL 2024、*NLP*期刊、东京女子医科大学等），用于预训练语言模型或RAG系统，计划添加更多CC-BY许可内容。
