# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专门收录日语NLP相关的Python库、LLM、词典和语料库资源的精选列表。
本页面列出了Hugging Face上可用的日语NLP专用模型和数据集。目前包含148个模型和96个数据集。

_更新于2026年2月24日_

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
   * [token-classification](#token-classification)
   * [image-to-text](#image-to-text)
   * [translation](#translation)
   * [text-classification](#text-classification)
   * [image-text-to-text](#image-text-to-text)
   * [audio-to-audio](#audio-to-audio)
   * [text-to-speech](#text-to-speech)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | 模型名称 | Downloads | Likes | 类别 |
|---|-------|-----------|-------|----------|
| 1 | [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) | 📥 3M | ⭐ 22 | sentence-similarity |
| 2 | [llm-jp-3-3.7b-instruct](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct) | 📥 2M | ⭐ 13 | text-generation |
| 3 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 1M | ⭐ 52 | automatic-speech-recognition |
| 4 | [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) | 📥 1M | ⭐ 3 | text-classification |
| 5 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 495k | ⭐ 74 | fill-mask |
| 6 | [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) | 📥 345k | ⭐ 11 | sentence-similarity |
| 7 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 275k | ⭐ 15 | text-generation |
| 8 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 270k | ⭐ 66 | sentence-similarity |
| 9 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 221k | ⭐ 168 | image-to-text |
| 10 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 214k | ⭐ 11 | translation |
| 11 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 188k | ⭐ 40 | fill-mask |
| 12 | [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) | 📥 171k | ⭐ 9 | sentence-similarity |
| 13 | [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) | 📥 159k | ⭐ 4 | token-classification |
| 14 | [MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) | 📥 158k | ⭐ 12 | token-classification |
| 15 | [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 📥 151k | ⭐ 20 | text-generation |
| 16 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 129k | ⭐ 7 | sentence-similarity |
| 17 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 97k | ⭐ 10 | others |
| 18 | [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) | 📥 96k | ⭐ 8 | fill-mask |
| 19 | [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) | 📥 95k | ⭐ 3 | fill-mask |
| 20 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 91k | ⭐ 58 | text-generation |

### Datasets-ranking

| # | 数据集名称 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 2M | ⭐ 22 |
| 2 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 7k | ⭐ 8 |
| 3 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 6k | ⭐ 16 |
| 4 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 6k | ⭐ 102 |
| 5 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 3k | ⭐ 33 |
| 6 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 3k | ⭐ 10 |
| 7 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 99 |
| 8 | [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) | 📥 2k | ⭐ 16 |
| 9 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 2k | ⭐ 38 |
| 10 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 2k | ⭐ 19 |
| 11 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 2k | ⭐ 24 |
| 12 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 1k | ⭐ 4 |
| 13 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 1k | ⭐ 47 |
| 14 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 1k | ⭐ 18 |
| 15 | [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) | 📥 1k | ⭐ 8 |
| 16 | [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) | 📥 1k | ⭐ 10 |
| 17 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 879 | ⭐ 7 |
| 18 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 878 | ⭐ 6 |
| 19 | [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) | 📥 858 | ⭐ 32 |
| 20 | [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) | 📥 818 | ⭐ 6 |

## Models
### text-generation
 * [llm-jp-3-3.7b-instruct](https://huggingface.co/llm-jp/llm-jp-3-3.7b-instruct) - 📥 2M / ⭐ 13 / 日语和多语言语言模型（1.8 十亿到 13 十亿参数，base 与 instruct 变体）由国立信息研究所（NII）的 Large Language Models R&D Center 发行，已封装为 Hugging Face Transformers 并在日语维基百科、Common Crawl、WARP/PDF/HTML、Kaken、英文维基百科以及 Dolma 数据集上进行预训练。
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 275k / ⭐ 15 / 一个 12 层、768 隐藏层的日语 GPT‑NeoX 模型，训练数据为 CC‑100、C4 以及 Wikipedia，兼容 Huggingface，并配备可选的玩具前缀调优权重，能强制每个句子末尾以笑脸表情符号结束。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 151k / ⭐ 20 / OpenCALM 是 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 许可证下发布的一套仅解码的日本 transformer 语言模型（160 M–6.8 B 参数），训练于 Japanese Wikipedia 和 Common Crawl，并可通过 Hugging Face’s torch‑transformers 使用。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 91k / ⭐ 58 / 一款由 ABEJA Inc. 使用日语 CC‑100 和 OSCAR 训练的 2.7B 参数日语 GPT‑NeoX 模型，可通过 Hugging Face Transformers 管道或 PyTorch 使用，按 MIT 许可证发布。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 32k / ⭐ 28 / LFM2.5‑1.2B‑JP 是一个 1.2 B 参数的日语文本生成模型，基于 LFM2.5 混合架构构建，优化用于生成和完成任务，托管在 Hugging Face 上，并可通过 llama.cpp 运行。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 21k / ⭐ 21 / Llama3 Swallow 是 Meta Llama 3 系列的日语增强版本，于 2024 年 7 月 1 日发布，提供 8B 与 70B 版本的 Instruct 与 chat 模式，已在 Megatron‑LM 上使用 SFT 与 Chat Vector 进行微调，并在关键的日语 NLP 任务上进行了基准测试。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 19k / ⭐ 142 / Llama‑3‑ELYZA‑JP‑8B 是由 ELYZA 开发的、经过日语增强的 80 亿参数 Llama 3 模型，在 Meta‑Llama‑3‑8B‑Instruct 上针对日语微调。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 17k / ⭐ 18 / 使用 Shisa 7B 数据，微调了日语 Stable LM Base Gamma 7B，在 JA MT‑Bench 上取得了强劲的表现。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 11k / ⭐ 25 / rinna 的日语 GPT‑2 small 是一个 12 层、768 维隐藏层的 Transformer，训练于日语 CC‑100 和 Wikipedia，使用 SentencePiece 进行分词，发布于 2021 年 8 月 25 日，遵循 MIT 协议（Hugging Face: rinna/japanese‑gpt2‑small，参见 https://arxiv.org/abs/2404.01657）。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 9k / ⭐ 18 / Llama 3.1 Swallow 是一组 8‑B 和 70‑B 模型，它们继续对 Meta 的 Llama 3.1 进行预训练，以提升日语语言性能，然后在合成日语数据上进行指令微调，提供多种已发布的变体，其对话行为已改进，与 gemma‑3‑27b‑it 相当。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 9k / ⭐ 105 / 9亿参数的日语优化LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，训练数据截至2024年9月，采用混合 Mamba‑2/MLP/4‑层注意力架构，已在 Nemotron‑Personas‑Japan 工具调用数据集上微调，可选地在生成最终答案前生成可控的推理轨迹，且可商用。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 8k / ⭐ 41 / GGUF‑formatted NVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese，已从 imatrix 数据集重建，并准备好在 CUDA 上使用 llama.cpp 运行。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 实验性日语模型通过使用聊天向量方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 与 Meta‑Llama‑3‑8B‑Instruct 之间的差异创建，然后上采样并应用于 Meta‑Llama‑3‑70B‑Instruct，显示出变化不大，并计划未来扩大规模。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 7k / ⭐ 138 / LFM2.5‑1.2B‑JP 是一款针对日语优化的聊天模型，在日语知识与指令遵循方面优于 LFM2，支持使用 LoRA 进行微调，支持通过 Transformers、vLLM 和 llama.cpp 进行推理，取得 50.7 JMMLU、58.1 M‑IFEval 与 56.0 GSM8K 分数。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 6k / ⭐ 24 / Llama 3.1 Swallow 是一系列日语增强的 8B/70B Llama 3.1 模型，通过持续预训练和日语特定指令微调训练，最新的 8B‑Instruct‑v0.3 在日语 MT‑Bench 上取得了最先进的结果。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 6k / ⭐ 85 / Rinna 的 24 层、1024 隐藏单元的日语 GPT‑2‑medium 模型，基于 CC‑100 和维基百科训练，采用 SentencePiece 分词，已在 rinna/japanese‑pretrained‑models 仓库公开（MIT 许可证，2021 年 4 月 7 日发布，2021 年 8 月 25 日更新）。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 5k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 与 Swallow Team 开发的紧凑型日语指令遵循语言模型，采用 Qwen2.5‑32B‑Instruct 的 TAID 蒸馏，并在日语文本上进一步预训练，且仅以 Apache 2.0 许可证供研究使用。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 4k / ⭐ 26 / Japanese 3.6 B‑parameter GPT‑NeoX 模型细调以适应指令遵循（SFT‑v2），对比之前的 SFT 与 ChatGPT 在 100 条提示上进行评估，发布于 2023 年 3 月 31 日。
 * [shisa-v2.1-unphi4-14b](https://huggingface.co/shisa-ai/shisa-v2.1-unphi4-14b) - 📥 4k / ⭐ 4 / Shisa V2.1 在 Shisa V2 双语日英聊天模型基础上，通过重新采样数据以及新增指令跟随、翻译、礼貌和其他日语特定增强功能，推出 1.2 B 至 70 B 的版本——包括 Llama 3.2/3.3 和 Qwen 3 变体——并在 Apache 2.0、MIT 与 LLM 许可证下提供，同时在日英基准测试中表现竞争力。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 3k / ⭐ 20 / OpenCALM 是 CyberAgent 开发的日本解码器（decoder‑only）Transformers 语言模型系列（160 M–6.8 B 参数），基于日本维基百科和 Common Crawl 训练，并以 CC BY‑SA 4.0 许可证发布。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 3k / ⭐ 74 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27 B 参数扩展版，已在包含 instruct 和 fast 变体的日语数据上预训练，可通过 Hugging Face Transformers 使用。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 2k / ⭐ 17 / LLM‑jp‑3.1‑13b‑instruct4 是一个 13‑B 的、基于指令预训练的日语语言模型，由 NII 的研发中心开发，并以 Hugging‑Face Transformers 检查点的形式发布，使用 UNIGRAM‑byte‑fallback 分词器。
 * [Murasaki-8B-v0.1-GGUF](https://huggingface.co/Murasaki-Project/Murasaki-8B-v0.1-GGUF) - 📥 2k / ⭐ 4 / Murasaki‑8B‑v0.1 是一个8‑billion‑parameter、CoT‑enabled 的 System 2 翻译器，专用于 ACGN 内容，已以多种 GGUF‑quantized 格式发布，并在 Murasaki‑ACGN benchmark 上优于竞争 LLM。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 57 / TinySwallow‑1.5B‑Instruct 是一个 1.5 B 的日语指令调优自回归语言模型，使用 TAID 从 Qwen2.5‑32B‑Instruct 进行蒸馏，供研究用途。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 2k / ⭐ 10 / 仓库提供 GGUF 格式、量化的模型文件，适用于 Stability AI 的日本版 StableLM Instruct Gamma 7B，由 Massed Compute 硬件创建，并且是 TheBloke 的 a16z‑资助 LLM 工作的一部分。
 * [GPT-OSS-Swallow-20B-SFT-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-SFT-v0.1) - 📥 2k / ⭐ 5 / GPT‑OSS‑Swallow v0.1 是一个双语日英模型系列（20B & 120B），通过持续预训练、监督微调和带可验证奖励的强化学习来训练，以保持数学和编码性能，目前已发布 SFT 和 RL 变体，并计划发布量化版本。
 * [Qwen3-Swallow-30B-A3B-SFT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-30B-A3B-SFT-v0.2) - 📥 2k / ⭐ 1 / Qwen3‑Swallow v0.2 提供了 30-32 亿参数的日英双语大型语言模型，这些模型通过 CPT、SFT 和 RLVR 训练，保持了数学和编程性能，在推理任务上优于 Qwen3，并提供了九个公开的（AWQ量化）模型变体，同时将 GPTQ量化版本保持私有。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 2k / ⭐ 1 / 日本增强、指令调优的 Gemma‑2 模型，基于 Llama（2b/9b/27b 预训练和指令版本），于 2025 年 5 月 19 日发布，可通过 HuggingFace 和 Swallow 团队网站获取。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 2k / ⭐ 16 / 一个6层、512隐藏单元的Transformer，称为Japanese GPT‑2 xSmall，在Japanese CC‑100和Wikipedia上使用SentencePiece分词训练，于2021年8月25日以MIT许可发布，并托管在Hugging Face（rinna/japanese‑gpt2‑xsmall）上，在arXiv 2404.01657中被引用。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 2k / ⭐ 16 / 提供 1.8 B 参数 llm‑jp‑3.1‑1.8b‑instruct4 日本指令微调模型，来自 NII，兼容 Hugging Face Transformers 和 Torch ≥ 2.3.0，包括预训练和微调检查点以及使用示例.
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 2k / ⭐ 48 / 一款日本持续预训练的 Mistral‑Nemo 模型（Mistral‑Nemo‑Japanese‑Instruct‑2408），基于 mistralai/Mistral‑Nemo‑Instruct‑2407 构建，可通过 transformers 使用设备映射和 ChatML 提示进行使用，已由 Ryosuke Ishigami 以 Apache‑2.0 许可证发布。
 * [Mistral-Nemo-Japanese-Instruct-2408-GGUF](https://huggingface.co/QuantFactory/Mistral-Nemo-Japanese-Instruct-2408-GGUF) - 📥 1k / ⭐ 18 / 一版 gguf 量化的 U‑Lens 版本，来自 cyberagent 的 Mistral‑Nemo‑Japanese‑Instruct‑2408，使用 llama.cpp 构建，基于 mistralai 的 Mistral‑Nemo‑Instruct‑2407，在 Apache‑2.0 许可下分发，并通过更新后的 transformers 接口使用。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 1k / ⭐ 96 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 7 B 的日语优化扩展，提供 instruct 和 fast 变体，参数为 6.27–6.37 B，可通过 Hugging‑Face Transformers 库访问。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 1k / ⭐ 34 / 提供了一款来自 SB Intuitions 的自回归式日语语言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已与其他模型进行基准测试，并附示例使用脚本，且安全训练有限。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 1k / ⭐ 12 / GPT‑OSS‑Swallow v0.1 提供 20B 和 120B 双语日英 LLM，通过 CPT、SFT 和 RLVR 训练，能够在数学和编码任务上与 GPT‑OSS 匹配或超越，于 2026 年 2 月发布，包含四种 SFT/RL 变体，并将推出量化版本。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 1k / ⭐ 21 / youri‑7b 是一个32层、4096隐藏单元的 transformer，基于 Llama2‑7b 构建，持续在约 40 B 个日语 token（CC‑100、C4、OSCAR、Pile、Wikipedia）上进行预训练，并于 2023 年 10 月 31 日发布，在 AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA 和 Winogrande 上取得了竞争性的分数。
 * [Llama-3.1-Future-Code-Ja-8B](https://huggingface.co/future-architect/Llama-3.1-Future-Code-Ja-8B) - 📥 1k / ⭐ 8 / 8B‑参数 Llama 3.1 Future Code Ja，在代码量大且主要为日语的数据上精调，擅长日语和英语代码补全，支持 Fill‑in‑the‑Middle，并在日语生成任务中超过 Llama 3.1 和 Qwen。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 1k / ⭐ 25 / 与 Hugging Face 兼容的日语中心 transformer 模型（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct）来自国立信息学研究所，在包含 Wikipedia、Common Crawl、WARP、Kaken、Dolma 在内的多种日语和英语语料库上预训练，并要求 torch ≥ 2.3、transformers ≥ 4.40、accelerate 与 flash‑attn。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 81 / 来自 ELYZA 的日语增强版 Llama‑2‑7B，已预训练以提供扩展的日语语言能力，提供标准、指导和快速版本，附有详细使用示例、开发者署名，并遵循 Meta’s Llama‑2 Community License 许可。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 495k / ⭐ 74 / Japanese BERT‑base 在 2019 年日本维基百科上预训练，使用 IPA‑dictionary 与全词掩码，12 层 768 维，32,000 词表，512 标记序列，1 M 步骤，可在 cl‑tohoku/bert‑japanese 获取，遵循 CC‑BY‑SA 许可。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 188k / ⭐ 40 / 一个预训练于约 17 M 条日语维基百科句子（2.6 GB）的 BERT base 模型，使用 IPA 字典和 WordPiece 进行分词，拥有 12 层 / 768‑维隐藏状态 / 12 头，32 000‑token 词汇表，已在 Cloud TPUs 上训练了 1 M 步，并以 CC‑BY‑SA 3.0 许可发布。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 96k / ⭐ 8 / 一个 BERT‑base 日语模型（12 层，768 维隐藏，12 头），使用 MeCab IPA 词级分词后再进行字符级分词生成 4000 词的词表，在约 1700 万句来自日语维基百科（2.6 GB）的句子上预训练，训练代码位于 cl‑tohoku/bert‑japanese，采用 CC BY‑SA 3.0 许可证发布。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 95k / ⭐ 3 / 日本 RoBERTa‑base 模型，预训练于约1000万条日本医学摘要和140万条来自 JST 的正文文本，采用 30 k‑token SentencePiece 进行分词，采用 CC BY‑4.0 许可证发布，可通过 Hugging Face pipelines 使用。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 55k / ⭐ 6 / 一个 BERT‑base 日语模型（12 层，768-维隐藏状态，12 头），在 3000 万条维基百科句子（约 4 GB）上训练，使用 Unidic 2.1.2 词级分词，随后进行字符级分词和全词掩码，使用 512 令牌序列，256 批次，以及 1 M 训练步骤。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 40k / ⭐ 48 / LINE DistilBERT Japanese 是一个 6600 万参数的 DistilBERT 模型，已在 131 GB 的日语网页文本上使用内部 BERT‑base 教师进行预训练，评估基准为 JGLUE，采用 MeCab Unidic 与 SentencePiece 进行分词，并以 Apache 2.0 许可证发布。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 21k / ⭐ 8 / 日语 DeBERTa V2 大型模型，已在 171 GB 的日语 Wikipedia、CC‑100 与 OSCAR 上训练，使用字符级 SentencePiece 分词和全词掩码，已准备好通过 Hugging Face Transformers 进行下游微调。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 10k / ⭐ 27 / Japanese BERT‑base（12 层，768 隐藏，12 头）在 4 GB 的日语维基百科（≈30 M 句）上预训练，使用 Unidic 2.1.2 词级分词、WordPiece 子词分词和全词遮蔽。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 10k / ⭐ 39 / Japanese‑Roberta‑Base 是来自 rinna Co., Ltd. 的预训练掩码语言模型，提供了正确加载、token 预处理、position‑id 处理的准则，以及强调需要前置 [CLS] token 和一致 tokenization 的使用示例。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 8k / ⭐ 5 / ModernBERT‑Ja‑30M 是一种日语 BERT 变体，融合了本地和全局注意力与 RoPE，训练于 4.39 TB 日英文本，支持 8,192 令牌序列，参数规模从 30 M 到 130 M，最佳搭配 Flash Attention 2。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 8k / ⭐ 47 / 这是一款 1.32 亿参数的日语 ModernBERT 模型，融合了 local‑global 与 RoPE 注意力机制，训练于 4.39 T 词条（日语/英语），词表大小 102k，最大序列长度 8,192，针对 Flash Attention 2 做了优化。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 4k / ⭐ 30 / Japanese DeBERTa V2 基础模型已在 171 GB 的日语维基百科、CC‑100 和 OSCAR 数据上预训练，使用 Juman++ 分词和 SentencePiece 标记化，经过三周在八块 NVIDIA A100 GPU 上训练，现已准备好用于微调。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 3k / ⭐ 32 / Japanese RoBERTa‑base 在日本 Wikipedia 与日本 CC‑100 上预训练，采用 Juman++ 词分割与 SentencePiece 分词，使用 Adam（lr = 1e‑4，native AMP）在 8 台 NVIDIA A100 GPU 上训练了一周，可微调，并在 JGLUE 上报告了结果。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 3k / ⭐ 20 / ModernBERT‑Ja‑310M 是一种日语 BERT 变体，融合了局部-全局注意力和 RoPE，训练于 4.09 T 日语/英语文本，支持 102 400 词汇量、8 192 令牌序列，并针对 Flash Attention 2 进行了优化。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 2k / ⭐ 2 / Japanese DeBERTa V2 tiny，在约171 GB的日本维基百科、CC‑100 与 OSCAR 语料库上预训练，需使用 Juman++ 词分割，训练耗时 33 小时，使用8块 NVIDIA A100 GPU，并可用于下游任务的微调。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 2k / ⭐ 4 / DeBERTaV2 base 在日本语语料库（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上训练，并使用 FP‑16 微调进行 NLU 任务（JSTS、JNLI、JCommonsenseQA），以 CC BY‑SA 4.0 许可发布，并由日本研究资助。
 * [modernbert-ja-70m](https://huggingface.co/sbintuitions/modernbert-ja-70m) - 📥 2k / ⭐ 6 / ModernBERT‑Ja‑70M 是一种轻量级的日语 BERT 变体，结合本地和全局注意力与 RoPE，在 4.39 T 的混合语言词元（词表 102 400，最大 8 192 个词元）上训练，支持 Flash Attention 2，并提供 30 M 到 310 M 参数的多种尺寸。
 * [llm-jp-modernbert-base](https://huggingface.co/llm-jp/llm-jp-modernbert-base) - 📥 1k / ⭐ 11 / 一个 ModernBERT-base 模型在 3.4 TB 日语 llm‑jp‑corpus v4 上训练，经过两阶段微调（max_seq_len 1024 → 8192），达到了 0.92 JSTS、0.91 JNLI 和 0.88 JCoLA。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 12 层，768 维度的 BERT‑Base 日语模型，在 2.6 GB Wikipedia（≈17 M 句子）上训练，使用 IPA‑dictionary 字符分词与 whole‑word masking，并在 CC‑BY‑SA 3.0 许可下发布。

### sentence-similarity
 * [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) - 📥 3M / ⭐ 22 / 用于最终 JaColBERTv2.5 检查点的权重，仅在 JaColBERTv2 数据的 40% 及新配方下训练，已在所有数据集上优于之前所有模型——包括 JaColBERTV2 多语言变体，如 BGE‑M3。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 345k / ⭐ 11 / 日语通用文本嵌入模型（Ruri‑v3，30‑310 M 参数，8192‑token 最大，JMTEB 分数高）与 Sentence‑Transformers 使用示例以及与其他日语嵌入模型的基准对比一起提供。
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 270k / ⭐ 66 / Ruri v3 是基于 ModernBERT‑Ja 的先进日语文本嵌入模型，支持多达 8,192 词元输入，100K 词元词汇表，FlashAttention 加速推理，并提供多种尺寸变体，便于快速使用 sentence‑transformer。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 171k / ⭐ 9 / 包括 Ruri v3 日语文本嵌入（30 M–310 M 参数，8192‑token 限制，JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前缀的 Sentence Transformers 指令，以及对数个日语模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基准结果。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 129k / ⭐ 7 / Ruri v3是一个最先进的日语文本嵌入模型，基于ModernBERT‑Ja构建，支持最多8,192个标记，拥有100 k词汇量，支持FlashAttention加速，并提供多种规模，从37 M到315 M参数。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 28k / ⭐ 34 / GLuCoSE 是一个基于 LUKE 的日语句子嵌入模型，输出 768 维均值池化向量（最多 512 个标记），在 Web 和 NLI/搜索数据上训练，在相似性基准测试中达到了 0.864 的 Spearman 相关系数和 0.818 的 Pearson 相关系数。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 26k / ⭐ 16 / JaColBERTv2 是一个仅适用于日语的基于 ColBERT 的检索模型，在 MMarco 上通过知识蒸馏训练（每个正例 31 个负例，250k 次，batch 32）。目前它优于 multilingual‑e5‑large、BGE‑M3 和 JaColBERT，完整评估正在进行中。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 25k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一个 768 维的句子变换器，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，训练了一个 epoch 的 shunk031/jsnli，并包含用于聚类、语义搜索以及同时兼容 Sentence‑Transformers 和 HuggingFace 的示例。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 21k / ⭐ 22 / GLuCoSE v2 是一款 CPU 友好的日语文本嵌入模型，通过蒸馏和多阶段对比学习进行微调，提供卓越的语义相似性和检索性能——在 MIRACL 及相关基准上优于同等规模的模型。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 11k / ⭐ 44 / 一组已准备好发布的 Ruri v3 日语文本嵌入模型（30m–310m），完整附带 SentenceTransformer 使用技巧、查询/段落前缀，以及 JMTEB 基准结果，展示它们与其他日语和多语言嵌入模型的比较。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 9k / ⭐ 44 / PLaMo‑Embedding‑1B 是 Preferred Networks 的一款日语文本嵌入模型，它将日语文本转换为向量，用于信息检索、分类和聚类，在 JMTEB 基准上表现出强大性能，并且在 Apache v2.0 许可证下可免费使用。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 8k / ⭐ 4 / Ruri v3 是基于 ModernBERT‑Ja 的前沿日语文本嵌入模型，支持最多 8192 token 序列、100K token 词汇量、FlashAttention，并以 30 M 至 310 M 参数规模发布，供 sentence‑transformers 使用。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 3k / ⭐ 2 / Ruri v3 提供高性能的日语文本嵌入，支持至 8192 个 token，拥有 100k 个 token 的词汇表，支持 FlashAttention，并提供多种模型规模（30 m–310 m），以实现高效推理和通过 sentence‑transformers 进行微调。
 * [ruri-large-v2](https://huggingface.co/cl-nagoya/ruri-large-v2) - 📥 2k / ⭐ 10 / 日本通用文本嵌入仓库 Ruri 提供 v3 模型，参数数从 30 M 到 310 M，具备 JMTEB 分数；并演示如何使用 sentence_transformers（使用 “クエリ: ” / “文章: ” 前缀）加载它们，并给出基准结果比较多个日语嵌入模型。
 * [ruri-small-v2](https://huggingface.co/cl-nagoya/ruri-small-v2) - 📥 1k / ⭐ 4 / Ruri发布日本通用文本嵌入模型v3（30 M–310 M 参数，8192‑Token 最大长度），在JMTEB上取得最高分，提供直接的 sentence_transformers 用法（以「クエリ:」或「文章:」为前缀），并给出检索、STS、分类、重排序、聚类和成对分类任务的基准结果。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 1k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B 是一个 1.2 B 参数的日语文本嵌入模型，构建于 Sarashina2.1‑1B 上，使用多阶段对比学习训练，以在 JMTEB 上达到最先进的分数，同时在非商业许可下生成 1,792 维的稠密向量，用于语义相似度、搜索和分类。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 1M / ⭐ 52 / Japanese wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 与 JSUT 上微调，需 16 kHz 音频，并可通过 HuggingSound 或 HuggingFace 管道使用。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 16k / ⭐ 93 / Kotoba‑Whisper‑v2.2 是一个日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了说话人划分和自动标点功能，通过 HuggingFace‑Transformers pipeline，并与 Asahi Ushio 与 Kotoba Technologies 合作开发。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 10k / ⭐ 18 / Kotoba‑Whisper‑Bilingual v1.0 提供了快 6.3 倍的蒸馏 Whisper 模型，用于日语和英语 ASR，并实现双向语音转文本翻译，这些模型是基于 OpenAI 的 Whisper large‑v3 通过知识蒸馏、交叉熵和 KL‑divergence 损失构建。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 5k / ⭐ 119 / Anime Whisper 是一款轻量级的日语 ASR 模型，在约 5,300 小时的动漫风格对话上进行微调，能够提供低幻觉、节奏对齐标点，以及准确转录非言语声音和 NSFW 内容，并且需要在没有初始提示的情况下运行。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 5k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一个 96.7 M 参数的 wav2vec 2.0 Base 模型，经过在 ReazonSpeech v2.0 日语 ASR 语料库上微调，达到 13.22 % 的 CER，可与 Hugging Face transformers 一同部署，并在 Apache 2.0 许可证下发布。
 * [japanese-wav2vec2-large-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-large-rs35kh) - 📥 4k / ⭐ 3 / 日语 wav2vec 2.0 Large (319 M parameters) 微调于 ReazonSpeech v2.0，在日语 ASR 上提供平均 16.25 % CER，优于其他 wav2vec 2.0 系列。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 4k / ⭐ 35 / reazonspeech-nemo-v2 是一个 619‑M‑参数的日语长文本 ASR 模型，基于改进版 Fast‑Conformer 及 Linearly Scalable Attention，在 ReazonSpeech v2.0 语料库上训练，支持通过 subword RNN‑T decoder（3000‑token SentencePiece）进行多小时推理，并以 Apache 2.0 许可分发。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 4k / ⭐ 45 / NVIDIA NeMo 的 0.6 B 参数 Hybrid FastConformer‑TDT‑CTC ASR 模型可转写带标点的日语语音，并可在 NeMo 框架内用于推理或微调。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 4k / ⭐ 87 / Kotoba‑Whisper v2.0 是从 OpenAI Whisper large‑v3 蒸馏出的日语 ASR 模型，训练于 720 万个 ReazonSpeech 剪辑，推理速度快 6.3 倍，同时在同域测试中匹配教师模型的 CER/WER，并提供 stable‑ts/标点支持以及完整的训练代码在 GitHub 上。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 2k / ⭐ 19 / Kotoba‑Whisper‑v2.1 是一种日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了标点后处理管道，保持可比的 CER 性能，同时实现无缝、标点感知的转录。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 60k / ⭐ 51 / 一款在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上使用 MultipleNegativesRankingLoss 细调的 Japanese Sentence‑BERT v2，较 v1 提升了约 1.5–2 %的准确率，并以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 发布。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 39k / ⭐ 11 / 用于生成句子嵌入的 Japanese Sentence‑BERT (v1) 模型，已提供改进版 v2，并通过 Hugging Face Transformers 以及自定义的 `SentenceBertJapanese` 类进行示例使用。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 30k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一个 Apache‑2.0 许可的日语 CLIP 模型，基于 ViT‑B/16，训练于 CC12M captions 翻译成日语，并于 2022 年 5 月 12 日发布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 20k / ⭐ 29 / LY Corporation的clip‑japanese‑base 是一个日语 CLIP 模型，在约10亿对图像‑文本对上训练，使用 Eva02‑B transformer 图像编码器和 12 层 BERT 文本编码器，在 STAIR 上实现 R@1 0.30，在 Recruit 上得到 0.89 的准确率，在 ImageNet‑1K 上得到 0.58 的准确率，并支持 zero‑shot 图像分类和检索。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 11k / ⭐ 2 / ja_ginza_electra 是一个 spaCy v3 Python 包，提供一个在 mC4 和 UD_Japanese_BCCWJ r2.8（基于 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator）上微调的日语 ELECTRA 模型，并配有自定义 bunsetu‑phrase 检测功能，按 MIT license 分发。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 10k / ⭐ 21 / Sarashina‑Embedding‑v2‑1B 是一个 1,792 维的日语句子变换器，使用多阶段对比学习训练，获得了前沿的 JMTEB 分数，可通过 Sentence‑Transformers 并搭配可选指令前缀，用于语义相似度、搜索、改写挖掘、分类和聚类。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 9k / ⭐ 14 / Japanese Sentence‑LUKE 模型在与 Sentence‑BERT 同一数据集上训练，表现超过或匹配其性能，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，并通过 Hugging Face Transformers 的 MLukeTokenizer 与 LukeModel 进行使用。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 5k / ⭐ 17 / 日本CLIP模型 clip‑japanese‑base‑v2，升级后约20亿图像‑文本对并采用蒸馏，配合 Eva02‑B 图像编码器和 12 层 BERT 文本编码器，将 ImageNet‑1k 准确率提升至 0.708，超过前代模型。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 2k / ⭐ 55 / 一个Japanese‑language T5 model，在约100 GB的Wikipedia和OSCAR数据上使用SentencePiece tokenization进行预训练，超越了Google’s multilingual T5在news‑classification benchmark上的表现，但需要fine‑tuning，并可能产生biased outputs.
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 1k / ⭐ 4 / fastText 是一个轻量级、开源库，能够在标准的 CPU 上快速学习单词和句子嵌入以及分类器，几分钟内训练数十亿个单词，可压缩以便移动使用，并提供用于分类和语言识别的预训练向量。

### text-ranking
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 40k / ⭐ 7 / 日语 CrossEncoder 再排序模型，覆盖 xsmall 到 large（含 BGE），在 JQaRA、JaCWIR、MIRACL 与 JSQuAD 上进行评估，并为 sentence_transformers 与 HuggingFace 提供即用的集成示例。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 11k / ⭐ 13 / Ruri‑v3 Reranker 是一个基于 ModernBERT‑Ja 构建的稳健日语文本重排器，支持最高 8,192‑token 序列、100k‑token 词汇表、FlashAttention 以及 SentencePiece 分词器，并可通过 sentence‑transformers 使用。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 7k / ⭐ 6 / 快、轻量级的日语 Reranker v2 模型（tiny、xsmall、small、base），带有基准测试分数和 GPU 速度，可通过 sentence_transformers CrossEncoder 与 transformers ≥ v4.48 使用（可选闪存加速 flash‑attn），并且在 ONNX/量化形式下可用于 CPU/ARM。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 2k / ⭐ 4 / 日本训练的 CrossEncoder 重新排序器，尺寸从 xsmall（384）到 large（1024），以及 BGE‑v2‑m3‑v1 模型，提供微调、推理和 JQaRA、JaCWIR、MIRACL、JSQuAD 上的基准分数示例代码。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 1k / ⭐ 2 / Japanese‑reranker‑small‑v2 是一系列轻量级、快速的日语重排序模型（v2），提供从极小到基础的变体，最高可达 0.89 的平均分，GPU 推理时间为 2–15 秒，支持交叉编码器选项，并需要 Hugging Face Transformers v4.48+，可选 Flash Attention 2 进行加速。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 1k / ⭐ 15 / 一个日语 CrossEncoder 重新排序器套件——包括 xsmall、small、base、large 和 japanese‑bge‑reranker‑v2‑m3‑v1——配合示例用法、在多个基准上的评估指标和支持文档。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 1k / ⭐ 16 / 日语 CrossEncoder 重排序模型——从xsmall到large——在日语文本上训练，通过sentence_transformers公开，评估在JQaRA、JaCWIR、MIRACL和JSQuAD上。

### token-classification
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 159k / ⭐ 4 / 专为日语定制的 DeBERTa V3，在 Kudo 词元化下微调，推理时不使用形态学分析器，使用减小词汇量以实现高效嵌入，并在 Hugging Face 上发布（xsmall、base、large，large 版本使用 BPE 训练）。
 * [MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - 📥 158k / ⭐ 12 / 日本医学文档命名实体识别模型（下载这五个文件，运行 **predict.py** – 输出疾病、药物、日期等实体标签），用于 NAISTSOC 2022 NTCIR‑16 Real‑MedNLP 任务。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 10k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日语 NER，能够提取八种实体类型（公司、政治/其他组织、设施、产品、事件），通过 `BertForTokenClassification` 实现，训练数据来自 Stockmark Wikipedia dataset，并可通过安装 `transformers`、`unidic_lite` 和 `fugashi` 使用，遵循 CC BY‑SA 3.0 许可。
 * [MedNERN-CR-JA](https://huggingface.co/sociocom/MedNERN-CR-JA) - 📥 9k / ⭐ 4 / 一个兼容 Hugging‑Face 的 NER 模型，在 MedTxt‑CR‑JA 日文医学数据集上训练，附带一个预测脚本用于标准化实体输出、生成 XML 标记文本，并使用外部的 `id_to_tags.pkl` 将标签 ID 映射为真实标签。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 8k / ⭐ 10 / Fine‑tuned Japanese BERT‑Base适用于在维基百科数据集上的命名实体识别，该模型在《*Large Language Model Introduction*》一书第六章中呈现，并可通过Hugging Face transformers pipeline进行部署（Apache 2.0 许可）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 在日语 NER 语料库上对 XLM‑RoBERTa‑base 进行微调（标签 PER, ORG, LOC, INS, PRD, EVT），使用 5‑epoch Adam（lr 5e‑5，batch 12），达到 0.0173 的验证损失，已发布在 Transformers 4.23.1 和 PyTorch 1.12.1。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 221k / ⭐ 168 / Manga OCR 是一款 Vision Encoder‑Decoder OCR 工具，可读取纵向和横向的日语漫画文本，包括 furigana，适用于多种字体和低质量图像，并且源代码可免费获取。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 34k / ⭐ 3 / meikiocr 提供一个基于 D‑FINE、开源权重的视频游戏文本检测模型（v0.1，使用 MobileNet‑v4 骨干网络，提供两种分辨率变体和 64‑box 限制），以及实验性的低延迟 tiny 与 small 变体，训练材料来自日本视频游戏和漫画。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 33k / ⭐ 4 / Meikiocr的 `meiki.text.recognition.v0`——基于 D‑FINE 的 MobileNetV4 模型，在日本视频游戏文本上微调——为水平文本提供最先进的准确率和延迟，能够从 960×32 的输入中检测多达 48 个字符，并输出每个字符的边界框和置信度分数。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 3k / ⭐ 14 / Sarashina2.2‑Vision‑3B 是一个 3B 参数的日本大型视觉语言模型，基于 Sarashina2.2‑3B‑Instruct 和 SigLIP 图像编码器，在日本 VQA 基准测试上表现出强劲的性能。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 1k / ⭐ 2 / Manga OCR 是一种 Vision Encoder‑Decoder 系统，可在各种字体和低质量图像中提供高质量的日语漫画 OCR——包括带有假名覆盖的纵向和横向文本——并且也可用于一般印刷日语 OCR。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 214k / ⭐ 11 / 一个基于新 VNTL 数据集构建的 LLaMA 3 Youko qlora 微调模型，优化用于准确、逐字翻译日本视觉小说为英文，不使用聊天模式，采用默认 LLaMA 3 提示，并推荐中性采样（温度 0，无重复惩罚）。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 42k / ⭐ 28 / 已微调、GGUF-量化的 LFM2-350M checkpoint，用于近实时双向日英短至中等文本翻译，可通过 llama.cpp 使用。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 42k / ⭐ 68 / 来自 Opus 语料库的日语‑英语 Transformer‑Align 机器翻译模型，使用归一化和 SentencePiece 预处理，在 Tatoeba 测试集上达到了 41.7 BLEU 和 0.589 chr‑F。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 7k / ⭐ 116 / PLaMo Translation Model 是由 Preferred Networks 创建的大规模语言模型，专用于翻译任务，提供基础版、后训练版和评估版，在 PLaMo community license 下发布，并未针对聊天或其他下游用途进行 instruction‑tuned。
 * [opus-tatoeba-en-ja](https://huggingface.co/Helsinki-NLP/opus-tatoeba-en-ja) - 📥 2k / ⭐ 14 / 英文到日语 transformer‑align MT 模型，BLEU 15.2，构建于 opus+bt‑2021‑04‑10，使用 normalization+SentencePiece，托管于 Tatoeba Challenge。

### text-classification
 * [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) - 📥 1M / ⭐ 3 / Finance Sentiment JA (base) 是基于 BERT 的日语情感模型，训练于翻译后的 Financial PhraseBank，能够将日语金融新闻分类为正面、负面或中性，宏观 f1 为 0.959，准确率 0.967，每秒 134.9 个样本。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 11k / ⭐ 15 / 训练于 chABSA 数据集的日语情感分析模型，获得 loss 0.0001、accuracy 1.0、F1 1.0，由 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 构建，使用 Adam（learning rate 2e‑05、10 epochs、batch size 16）优化，并通过 `model(**inputs)` 进行评估。
 * [luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 📥 5k / ⭐ 43 / 一个在WRIME数据集上微调的日本LUKE模型，用于分类句子中表达的八种情绪——喜悦、悲伤、期待、惊讶、愤怒、恐惧、厌恶、信任。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 4k / ⭐ 2 / 一个基于 Japanese BERT‑based model 的模型，已在 JGLUE JSTS 数据集上 fine‑tuned，用于语义相似性评分——在《Large Language Model Introduction》第5章中介绍——配有 Colab notebooks、transformers‑pipeline 用法以及 Apache 2.0 许可证。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 2k / ⭐ 119 / 从 PaddleOCR‑VL 微调得到的 PaddleOCR‑VL‑For‑Manga 在 Manga109 的对话框裁剪图像上实现了70%完整句子准确率—是27%基线的三倍以上—并使用多语言数据集，包含训练代码和开发者指南。
 * [Heron-NVILA-Lite-15B](https://huggingface.co/turing-motors/Heron-NVILA-Lite-15B) - 📥 1k / ⭐ 14 / Heron‑NVILA‑Lite‑15B‑hf 是一个日语中心的视觉语言模型，基于 NVILA‑Lite 架构构建，采用 PALIGEMMA‑SIGLIP 视觉编码器、一个 MLP‑downsample 投影器以及 Qwen2.5‑14B‑Instruct LLM，支持日语和英语，并与 Hugging Face 无缝集成。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 3k / ⭐ 14 / Anime-XCodec2-44.1kHz-v2 将 16 kHz 的日语语音上采样至 44.1 kHz 的高保真音频，采用仅解码器的 RMS‑loss 微调，保持编码器/码本冻结并保留相同的语音令牌。

### text-to-speech
 * [Anime-Llasa-3B](https://huggingface.co/NandemoGHS/Anime-Llasa-3B) - 📥 2k / ⭐ 26 / Anime‑Llasa‑3B 是一款日本TTS模型，基于 HKUSTAudio/Llasa‑3B，增强了更多训练数据以提升表达力和稳定性，并采用 CC‑BY‑NC‑4.0 许可证。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 97k / ⭐ 10 / 日本语言 BERT‑Base（12 层，768 维，12 头）使用 Unidic 基于词级加字符级分词和全词掩码在 CC‑100 及 2023 Wikipedia 上进行预训练，产生 7,027 名词表。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 65k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上训练，使用 Unidic‑lite 单词级标记化配合 WordPiece 子词和全词掩码（24 层，1024 维隐藏层，16 头，32k 词表），预训练代码在 cl‑tohoku/bert‑japanese。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 39k / ⭐ 59 / Japanese BERT‑base（12层，768维隐藏层，12头，32 k词汇表）在 CC‑100 和 2023‑Jan Wikipedia 上使用全词遮蔽预训练，采用 Unidic 2.1.2 词级分词加 WordPiece，训练 200 万步。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 13k / ⭐ 11 / 一个预训练在≈100 GB的维基百科和 OS CC‑100 数据（SentencePiece 采用 10:1 混合且带 byte‑fallback）的日文 T5‑v1.1 模型，需要微调以适用于下游任务，包含迁移学习示例代码，指出输出中的潜在偏差，并遵循 CC‑BY‑SA 4.0 许可。
 * [GPT-OSS-Swallow-20B-SFT-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-SFT-v0.1-gguf) - 📥 12k / ⭐ 1 / GPT‑OSS‑Swallow‑20B‑SFT‑v0.1‑gguf 是 tokyotech‑llm GPT‑OSS‑Swallow 20B SFT 模型的 gguf 转换版本，训练于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，并为 CUDA‑enabled llama.cpp 构建，准备通过 llama‑cli 运行（例如，专业厨师食谱提示）。
 * [GPT-OSS-Swallow-120B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-120B-RL-v0.1-gguf) - 📥 6k / ⭐ 4 / 使用TFMC/imatrix日语数据集构建的120 B GPT‑OSS‑Swallow RL 模型的 gguf-format 转换，并附带编译支持CUDA的 llama.cpp 以及通过 llama‑cli 运行该模型的说明。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 6k / ⭐ 17 / Japanese DeBERTa V3 base 在 LLM‑jp v1.0 的 540 B tokens 上预训练，使用经过修改的 DeBERTa V3 设置训练，采用 unigram byte‑fallback tokenizer（不使用形态学分析器），并针对 JGLUE NLU 任务进行微调。
 * [GPT-OSS-Swallow-20B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-RL-v0.1-gguf) - 📥 4k / ⭐ 4 / 一个 gguf‑格式转换的 GPT‑OSS‑Swallow 20B RL v0.1 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 数据构建，已准备好通过 llama.cpp 运行并支持 CUDA。
 * [tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf](https://huggingface.co/mmnga/tokyotech-llm-Llama-3.1-Swallow-8B-Instruct-v0.3-gguf) - 📥 3k / ⭐ 4 / 此仓库托管了 tokyotech‑llm 的 Llama‑3.1‑Swallow‑8B‑Instruct‑v0.3 模型的 gguf-format 转换，基于 imatrix 数据集构建，并已准备好在 llama.cpp 运行。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 2k / ⭐ 17 / 高性能的日本 SPLADE v2 通过 WebUI demo 实现稀疏向量转换和推理，使用 YAST 进行训练，提供 YASEM 嵌入，并报告 JMTEB benchmark 结果。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 71 / Llama‑3‑ELYZA‑JP‑8B 是一款经过日本增强的 8‑B Llama 3 模型，采用 GGUF (Q4_K_M) 和 AWQ 量化，支持通过 llama.cpp、LM Studio 或 OpenAI‑compatible API 运行。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一个拥有80亿参数的 LLM，通过在合成日语数据上持续预训练和指令微调，提升了 Meta 的 Llama 3.1 在日语语言与代码/数学推理上的表现，同时保持了英语流畅性。
 * [Qwen2.5-7B-ja-struct-tooled-base-i1-GGUF](https://huggingface.co/mradermacher/Qwen2.5-7B-ja-struct-tooled-base-i1-GGUF) - 📥 2k / ⭐ 1 / 为 Qwen2.5‑7B‑ja‑struct‑tooled‑base 模型提供了加权/imatrix GGUF 量化版本，使用静态量化并托管在 Hugging Face 上。表格列出文件名、大小以及从低质量的 i1‑IQ2_XXS 到高质量的 i1‑IQ4_K_M 的质量说明，并通过 TheBloke READMEs 指导如何合并多部分文件。
 * [tokyotech-llm-Llama-3.1-Swallow-70B-Instruct-v0.3-gguf](https://huggingface.co/mmnga/tokyotech-llm-Llama-3.1-Swallow-70B-Instruct-v0.3-gguf) - 📥 2k / ⭐ 2 / 一款 gguf 格式的 TokyoTech‑LLM 的 Llama‑3.1‑Swallow‑70B‑Instruct‑v0.3 模型变体，基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM 构建，并附有通过 llama.cpp 在 CUDA 上运行的使用说明。
 * [gemma-3-12b-it-qat-japanese-imatrix](https://huggingface.co/dahara1/gemma-3-12b-it-qat-japanese-imatrix) - 📥 2k / ⭐ 6 / 一个以日语为主的 imatrix‑quantized 版本的 Google Gemma 3‑12b，已准备好用于 llama.cpp，并支持 llama‑mtmd‑cli/mmproj.gguf 的图像读取，托管在 Hugging Face 上。
 * [shisa-v2.1-qwen3-8b-UD-japanese-imatrix](https://huggingface.co/dahara1/shisa-v2.1-qwen3-8b-UD-japanese-imatrix) - 📥 2k / ⭐ 3 / 一个使用 Unsloth Dynamic 2.0 构建、已进行社区补丁以减少故障的 Qwen3 设置、提供更大 imatrix 以提升日语性能，并拥有 40K 最大上下文长度的 GGUF‑quantized shisa‑v2.1‑qwen3‑8b 模型。
 * [pfnet-nekomata-14b-pfn-qfin-gguf](https://huggingface.co/mmnga/pfnet-nekomata-14b-pfn-qfin-gguf) - 📥 2k / ⭐ 1 / GGUF‑converted pfnet nekomata‑14b‑pfn‑qfin，基于 TFMC/imatrix 日语 LLM 数据集构建，并以 Tongyi‑Qianwen 许可证发布。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 20 / 由 imatrix 数据构建的 pfnet 的 plamo‑2‑translate 的 GGUF‑格式发布，基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带通过 llama.cpp 在启用 CUDA 的硬件上编译和运行的说明。
 * [DataPilot-ArrowPro-7B-KUJIRA-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-KUJIRA-gguf) - 📥 1k / ⭐ 10 / DataPilot 的 ArrowPro‑7B‑KUJIRA 模型的 gguf 格式转换，使用 TFMC 的 imatrix 日语 LLM 数据集构建，并使用 llama.cpp 运行。
 * [Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf) - 📥 1k / ⭐ 2 / GGUF格式的 Qwen3‑Swallow‑30B‑A3B‑SFT‑v0.2 模型版本，由 tokyotech‑llm 发布，使用来自 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 数据构建，已准备好用于 llama.cpp 的 CUDA 使用。
 * [cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf](https://huggingface.co/mmnga/cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf) - 📥 1k / ⭐ 55 / Cyberagent’s gguf‑converted DeepSeek‑R1‑Distill‑Qwen‑14B‑Japanese model（基于 TFMC imatrix 数据集构建）在 mmnga 下可用，并可使用 llama.cpp 进行 CUDA 支持的运行。
 * [ELYZA-Shortcut-1.0-Qwen-7B-gguf](https://huggingface.co/mmnga/ELYZA-Shortcut-1.0-Qwen-7B-gguf) - 📥 1k / ⭐ 3 / 一个 gguf 格式转换的 ELYZA‑Shortcut‑1.0‑Qwen‑7B 模型，该模型使用 TFMC/imatrix‑dataset‑for‑japanese‑LLM 数据构建，已准备好使用已编译为 CUDA 的 llama.cpp 运行。
 * [llama-3-youko-8b-instruct-i1-GGUF](https://huggingface.co/mradermacher/llama-3-youko-8b-instruct-i1-GGUF) - 📥 1k / ⭐ 1 / rinna/llama‑3‑youko‑8b‑instruct 的 GGUF 量化版本集合，列出它们的尺寸/质量权衡，并提供使用指导、对比图表以及 FAQ/模型请求链接。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 2M / ⭐ 22 / 聚合了2009年至2024年NicoNico Live的评论日志，总计超过150 GB，包括转移前、转移后以及实时NX‑Jikkyo捕获，提供了一个API，便于检索历史电视广播讨论。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 7k / ⭐ 8 / Cauldron‑JA 是一个日语视觉‑语言数据集，包含 44 个子数据集，使用 DeepL API 从 The Cauldron 翻译而来，可通过 HuggingFace’s datasets library 获取，并与原始数据集使用相同的许可证，prompts 在 CC‑BY‑4.0 下发布。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 6k / ⭐ 16 / 一份日语和多语种 QA、NLI 与同义句重述数据集的目录，详细说明每个数据集的检索或问答任务及其许可（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 6k / ⭐ 102 / Nemotron‑Personas‑Japan 是一个开放源代码、CC BY 4.0 许可证的高质量、合成生成的日本人物资料数据集—包含姓名、性别、年龄、背景、婚姻状况、教育、职业和地点—基于真实世界的人口统计、地理和人格分布，并采用概率图模型和 GPT‑OSS‑120B 进行工程设计，以提升多样性、降低偏见、防止模型崩溃、支持主权 AI 发展，并支持商业使用。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 3k / ⭐ 33 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小时匿名 1,033,142 对 eroge 音频-转录配对（主要为女性，含 NSFW），MIT 许可用于学术研究。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 3k / ⭐ 10 / Reazon Speech v2 dataset 在 🤗 的镜像，授权 CDLA‑Sharing‑1.0，并受限于 Japanese Copyright Act Article 30‑4，包含 16 kHz FLAC 音频及其元数据。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 99 / 一个包含100个样本的日语指令微调评估数据集，包含已注释的任务——从摘要校正、数学推理到翻译、创意生成和用户意图理解——旨在对微调模型进行手动或自动的5分制评分。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 2k / ⭐ 16 / Reazon Speech v2 数据集的镜像：3,674 个已使用 UVR 在 8 台 A800 GPU 上处理 10 天的去噪音频文件，由 Stardust‑minus 提供，遵循 CDLA‑Sharing‑1.0 协议，未包含转录文本。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 2k / ⭐ 38 / 一个用户友好、去重的 CSV 数据集，包含 Aozora Bunko 的公有域日语文本，使用 globis‑org/aozorabunko‑extractor 处理，并已清理以适用于现代日语机器学习。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 2k / ⭐ 19 / JMMMU 是一个日语多模态基准，已扩大十倍至 1,320 个具有文化多样性的问题（720 个与文化无关，600 个与文化相关），由母语专家翻译，现在设有公开排行榜。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 2k / ⭐ 24 / FineWeb2 Edu Japanese 提供约120 million高质量教育日语文本（≈89.3 billion tokens）来自 FineWeb2，经过 DeepSeek‑API classifier（score ≥ 2.5）过滤，通过 ModernBERT‑Ja‑130M tokenized，并包含一个小-token子集（≤512 tokens）。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 4 / JamC‑QA 是一个双语基准，涵盖八个日本文化与知识类别的多项选择题，排行榜指标用于比较最先进模型。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 1k / ⭐ 47 / 更新了 JGLUE 数据集卡与加载脚本，适用于由 Yahoo Japan 与早稻田大学创建的日语 NLP 基准，涵盖文本分类（MARC‑ja、JCoLA）、句对分类（JNLI）以及问答（JSQuAD、JCommonsenseQA），发行链接保存在 GitHub 与 Hugging Face 上。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 1k / ⭐ 18 / JMTEB 是一个日本文本嵌入基准，包含 5 个任务（聚类、分类、STS、检索、再排序）和 28 个数据集，提供一行评估脚本，并邀请社区贡献。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 1k / ⭐ 8 / Rakuda 提供 40 道日语问题——开放式的历史、社会与政府问题，以及针对地理的特定问题——用于对日本 AI 助手进行基准测试，类似于 vicuna‑eval，并且可以使用 `datasets.load_dataset` 加载。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 1k / ⭐ 10 / JDocQA 是一个基于日文 PDF 的问答数据集，包含 5,504 篇文档和 11,600 对问答，使用视觉和文本信息测试是/否、事实性、数值、开放式和不可回答的理解。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 879 / ⭐ 7 / JMedBench 是一个日语生物医学 LLM 基准，涵盖 20 个数据集，覆盖五个任务（MCQA、NER、STS 等），来源于 MedMCQA、PubMedQA、MMLU 等，每个都有自己的许可，并包含一条说明：翻译可能包含偏差，需要人工审核。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 878 / ⭐ 6 / 使用 VOICEVOX 从 ITA、Tsukuyomi‑chan 以及 ROHAN 语料库创建的人工声数据集，包含 445,793 条 WAV 文件，总计 577 小时 51 分钟 23 秒。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 858 / ⭐ 32 / 一个时长为409小时的日本 eroge 语音数据集，使用 2-pass loudnorm（‑23 LUFS，‑1 dB 峰值，11 LRA）处理，已由 litagin/anime-whisper 转录、匿名化，存储为 WebDataset（FLAC、JSON、TXT），主要包含女性声音，可能存在 AI 转录错误，并采用 MIT 许可证用于学术研究。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 818 / ⭐ 6 / 日本 MC4 数据集卡 (mc4-ja)
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 802 / ⭐ 130 / Japanese Anime Speech Dataset V2 提供 292,637 条已清洗的音频-文本对——约 397.5 小时的 SFW 内容和 52.4 小时的 NSFW 内容——以 128‑kbps MP3 文件形式按安全级别划分，专为训练自动语音识别模型而设计。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 768 / ⭐ 108 / ReazonSpeech 是一个免费、FLAC 编码的日语语音语料库，附带转录，提供五种规模，从 8.5 h 到 35,000 h，可通过 Hugging Face 下载，遵循 CDLA‑Sharing‑1.0 许可证，且使用受到《日本著作权法》第30‑4条的限制。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 646 / ⭐ 88 / 一个自动翻译的日语版本的databricks‑dolly‑15k数据集，许可为CC‑BY‑SA‑3.0，最后更新于2023‑05‑11。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 598 / ⭐ 146 / 日本动漫语音数据集提供73,004对音频-文本（总计110小时，已从V1升级至V5），用于提升ASR模型，例如OpenAI的Whisper，按开放许可证提供给所有使用，欢迎署名。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 583 / ⭐ 4 / 提供了一个日语搜索/问答数据集，其中包含按查询计算的分数，这些分数是由五个多语言/日语重排序器（例如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）计算的，数据集包括每个查询约200个正例和负例文档的平均分数。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 569 / ⭐ 10 / EDINET‑Bench 是一个日本金融基准，用来评估 LLMs 在诸如会计欺诈检测、盈利预测和行业预测等任务，使用十年的 EDINET‑API 披露报告，提供构建和评估代码，并将数据集重新许可为 PDL 1.0。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 561 / ⭐ 6 / Japanese XL‑Sum subset 通过 PaLM‑2 15-gram 重叠过滤，包含 4,215 训练样本，758 验证样本和 766 测试样本。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 544 / ⭐ 11 / JMMLU 是一个日语大型多任务语言理解基准（Benchmark），包括 7,536 道教师精心制作的问题，覆盖 56 个学科，包括专业医学、心理学、会计、哲学以及各种高中学科。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 536 / ⭐ 5 / 将日语数据集转换为适合 SentenceTransformers 的列，依据来自多个 HuggingFace 来源的 Rerank 分数（正样本 ≥0.7，负样本 ≤0.3）进行过滤，以支持对比学习，同时尊重原始许可证。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 522 / ⭐ 2 / 包含匿名 2ch.sc/2ch.net 帖子的极大压缩 JSON‑Lines 数据集，包括帖子 IDs、标题、板块与地区信息、回复计数，以及完整帖子元数据（作者、邮件、日期、内容）。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 497 / ⭐ 5 / JAQKET 是一个基于维基百科的日语开放域问答数据集，提供 1.0 版包含多项选择测验题（13,061 条训练样本，271 条验证样本）以及 2.0 版仅包含需要提取答案的提问提示（2,154 条训练样本，1,164 条验证样本），旨在促进问答系统研究。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 486 / ⭐ 31 / 为高效加载 Hugging Face datasets，重新结构化并重新上传 Galgame VisualNovel 数据集（OOPPEENN/5669737465666C656E63655F44617461337072657330），保留所有原始 audio/text，并提供带多种 game-subset 选项的 extraction script。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 452 / ⭐ 13 / ‘wikipedia-ja-20230720’ 日本维基百科快照的数据集卡。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 449 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 数据集的 500 份样本子集，采用 CC BY 4.0 许可，用于基准测试 EvoVLM‑JP‑v1‑7B。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 429 / ⭐ 2 / 日文维基百科文本改写所生成的LLM查询和答案数据集，未使用受许可限制的模型构建，且在CC‑BY‑SA 4.0下发布。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 401 / ⭐ 3 / 已清理的日语网络语料库（mc4‑ja 等）通过无监督学习聚类成约10k 文本，仅部分文件为 Parquet；文件列表在 out 文件夹中，可使用 Git LFS 下载，用于合法可行的信息分析用途。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 398 / ⭐ 142 / 用于微调 LLMs（如 LoRA）的日语指令聊天数据集，包含 9 M+ 样本，最近已更新，删除授权的 Alpaca 数据，并清理了 Wikipedia 和 ALT 输出，采用 CC‑BY‑SA 4.0 许可证发布。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 352 / ⭐ 23 / cc100-ja 是 cc100 数据集日语部分的集合，提供为分片的 Parquet 文件。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 336 / ⭐ 10 / 一份将 llm‑jp‑corpus‑v3 的 kaken 子集译为日英的日英平行语料库，使用 Qwen/Qwen2.5‑32B‑Instruct，包含自定义翻译列，并在 CC‑BY‑4.0 许可下授权。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 329 / ⭐ 32 / Syosetu711K 是一个约 711,700 本小说的日本数据集，采自 2023 年 3 月 26‑27 日从 小説家になろう 抓取，提供全文及元数据（标题、作者、NCode、简介等），用于无监督文本生成和分类任务。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 310 / ⭐ 3 / BBH‑ja提供了BIG‑Bench Hard数据集的日语翻译，提供JSON‑L（输入、正确目标）格式的评估问题以及使用PLaMo模型翻译的YAML（输入、目标）格式的Chain‑of‑Thought提示。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 303 / ⭐ 3 / 包含问题、答案以及逐步推导链接至 Wikipedia 文章的日本 Explainable Multi-hop Question Answering 数据集，已更新推导格式并发布多个版本。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 298 / ⭐ 21 / 一套来自日本网络的5600万份文档、110 B字符与2.49亿张图片，用于训练大型视觉语言模型——提供momiji_generator用于数据填充，OBELICS‑style可视化，以及示例模型（Heron‑NVILA‑Lite）。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 295 / ⭐ 15 / 一个 1.9 亿对 JSONL 数据集，用于日语假名到汉字转换，为 zenz‑v2.5 medium、small 和 xsmall 模型提供动力，并包含 AJIMEE‑Bench 评估语料库。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 293 / ⭐ 3 / Japanese Guardrail model evaluation dataset (1,725 samples)，是 WildGuardTest 的高质量、多阶段翻译，采用 ODC‑BY 许可发布，并可在 Hugging Face 获取。
 * [jhle](https://huggingface.co/datasets/llm-jp/jhle) - 📥 290 / ⭐ 96 / 由 LLM‑jp 策划的日本翻译版 Humanity’s Last Exam 数据集，省略图像问题，每个 raw_subject 采样五条，已机器翻译并由专家审核，作者为 Yuji Tamakoshi、Kouta Nakayama 和 Yusuke Miyao，并且绝不应用于训练语料库。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 286 / ⭐ 33 / Allganize RAG Leaderboard 发布了跨五个行业领域——金融、电信、制造业、公共部门和零售业的日本 RAG 性能数据和自动端到端评估结果，帮助公司在没有完整日本基准的情况下基准化解析器、检索和生成组件。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 281 / ⭐ 11 / JaQuAD 是 2022 年的日语 QA 数据集，包含 39,696 对 SQuAD‑style 的抽取式问题‑答案对，取自 Wikipedia，文件总大小 73.2 MB。使用 BERT‑Japanese 微调时，获得 78.92 % F1（63.38 % EM）。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 278 / ⭐ 10 / 一个高质量的合成日语数学题数据集，具有经过验证的思考链推理，采用 Qwen2‑7B‑Instruct 翻译 PRM800K 和 GSM8K 并进行正确性筛选后构建，可通过 Hugging Face 数据集库获取。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 277 / ⭐ 19 / 一个用于评估 Retrieval‑Augmented Generation（RAG）的日语 QA 数据集，由 JAQKET 问题和 Wikipedia 段落以及金标准检索相关性标签构建，并在 HuggingFace 和 GitHub 上发布，主要依据 nDCG@10 评分。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 265 / ⭐ 15 / 用于《大型语言模型简介》一书的 JGLUE 数据集数据卡，来源于原始仓库，代码采用 CC BY‑SA 4.0 许可证，数据按发行者的许可协议，引用 Kurihara & Kawahara（日本语），并基于 Shunsuke Kitada 的仓库构建。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 243 / ⭐ 3 / 日语维基百科句子被转换为各种嵌入和 FAISS 索引，提供 Hugging Face Space 演示、转换脚本，以及对搜索、问答和 OpenAI text-embedding-3-small 在 RAG 中的评估；嵌入模型为 OpenAI‑licensed，其他为 CC‑BY‑SA‑4.0。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 236 / ⭐ 4 / 数据集卡片：关于由 Loonwit 提供、用于书《Introduction to Large Language Models》的 livedoor 新闻语料库，包含已去除 HTML 标签的 Creative Commons 许可新闻文章（CC BY‑ND 2.1 JP）。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 227 / ⭐ 2 / 将日本 Callhome 语音文件转换为 WAV，并附带 JSON 格式的元数据数组和 RTMM 说话人标签文件以供评估。
 * [relaion2B-en-research-safe-japanese-translation](https://huggingface.co/datasets/llm-jp/relaion2B-en-research-safe-japanese-translation) - 📥 222 / ⭐ 4 / 一个快速的英日翻译流水线，使用 text2dataset、Gemma‑2‑9b‑it 和 vLLM 构建，能够通过简洁的开源加权 LLM 提示，将大型 relaion2B‑en‑research‑safe 语料库转换。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 218 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) 提供了一个多分类 QA 数据集——涵盖 Integration、Reasoning、Logical、Table 和 Abstention——旨在评估日本 RAG 生成器，采用人工努力和 GPT‑4.1 构建，并在 CC BY‑SA 4.0 许可下发布。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 215 / ⭐ 6 / Range3 的 wikipedia‑ja‑20230101 仓库提供只包含日语维基百科文本的 Parquet 文件，这些文件是从完整维基百科数据集中提取的，并使用 Python 代码生成。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 213 / ⭐ 27 / WRIME 数据集是一个包含 42,200 条帖子的日本语集合，帖子已为作者、三位读者及其平均值标注了 Plutchik 的八种情感，结构为 40k 训练集、1.2k 验证集和 2k 测试集，用于情感分析任务。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 212 / ⭐ 9 / 面向 llm‑book/wrime‑sentiment 的数据集卡，提供从 WRIME 派生的二元日语情感分析集，依据 Avg. Readers_Sentiment 标记为正向或负向（可选包含中性案例），用于《大型语言模型导论》一书的示例数据。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 212 / ⭐ 7 / JHumanEval 是 HumanEval 基准的人工翻译日语版本，提供 164 个 Python 编程问题，配有并行的英文和日文注释，用于评估日语 LLM 的代码生成，同时保留原始英文错误。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 210 / ⭐ 24 / AutoWikiQA 是日本最大的免费问答数据集（2,377,503 对），该数据集是从维基百科文本使用 Swallow‑MX 和 vLLM 生成的，提供多样化、无模板的问答，用于知识注入和检索增强生成。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 210 / ⭐ 13 / 一份104 GB的数据集，共3,746,131条Galgame音频文件（5,353 小时），为现有16 kHz ASR集添加了LLM生成的情绪标签（可能不准确），并按GPL v3.0许可发布，禁止商业使用，且要求任何训练得到的模型必须开源。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 209 / ⭐ 2 / WAON 是一个大规模、高质量的日语图像–文本配对数据集，面向视觉语言模型，该数据集通过基于大小和 SigLIP-Score 的筛选以及在 URL、标题和感知哈希上的去重构建，采用 Apache 2.0 许可证，使用仅限于根据日本法律进行信息分析。
 * [wiki40b_ja](https://huggingface.co/datasets/fujiki/wiki40b_ja) - 📥 198 / ⭐ 4 / 由 Mandy Guo、Zihang Dai 和 Denny Vrandečić 重新格式化的 Wiki40B 数据集的日语子集。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 196 / ⭐ 40 / VNTL 排行榜通过在256个样本上平均余弦相似度分数，评估大型语言模型将日语视觉小说翻译成英语的能力，随后对初步结果进行排名，并与 Sugoi Translator、Google Translate 和 Naver Papago 等工具进行基准比较。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 196 / ⭐ 5 / STAIR‑Captions，发布于2017年，提供820,310条日语字幕，用于字幕生成、多模态检索和图像生成，并配有详细注释、元数据以及Creative Commons BY‑4.0 license。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 192 / ⭐ 11 / Range3/wiki40b‑ja 托管了 wiki40b 数据集的日语子集，作为由 Python 数据处理管道生成的三个 Parquet 文件。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 181 / ⭐ 14 / 一个用于测试角色‑LLMs的简单 Zundamon 角色设定数据集——由线上来源和管理数据编制——以 zmnjp.jsonl 和 zmn.jsonl 格式提供，并在指定许可下发布。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 180 / ⭐ 26 / 带有失败标记的日语翻译 OpenAssistant/oasst1 数据，约2,000个人工纠正的代码翻译错误，一个已发布的对话格式子集 (oasst1‑chat‑44k‑ja)，以及一段用于将条目转换为指令‑输出对以进行微调的脚本。
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 179 / ⭐ 6 / 已去重、NFKC‑标准化的 mQA query–passage pairs，pos_ids/neg_ids 映射到 collection 索引，用于通过 collection[pos_id] 直接检索，并按原始数据集的许可条款授权。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 177 / ⭐ 21 / AI生成的动漫插图，使用英文提示，并基于Phi‑3 Vision的字幕（英文和日文），已发布到公共领域，供免费使用。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 176 / ⭐ 41 / Galgame_Speech_ASR_16kHz 是一个 16 kHz 的 ASR 数据集，包含 3.75 百万对（≈5,354 小时），源自 Galgame_Dataset，遵循 GPL v3.0，禁止商业使用，并要求任何训练的模型必须开源（可选引证）。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 172 / ⭐ 3 / 本数据集说明书用于本书《Introduction to Large‑Scale LLM II》中的 ja‑vicuna‑qa‑benchmark，并由 llm‑jp‑eval 创建，供跨数据集日语 LLM 评估使用（Apache 2.0）。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 170 / ⭐ 50 / AnswerCarefully Dataset提供日语和多语种数据，用于商业或非商业LLM安全增强，禁止任何其他用途——包括安全规避——允许带署名的衍生作品，并声明不承担因伤害或服务变更导致的责任。
 * [cc100-ja-documents](https://huggingface.co/datasets/hotchpotch/cc100-ja-documents) - 📥 167 / ⭐ 3 / 将按行拆分的 cc100‑ja 数据集聚合为文档级块，同时保留原始 cc100 许可证。
 * [oscor-2301-ja-text-content](https://huggingface.co/datasets/ayousanz/oscor-2301-ja-text-content) - 📥 165 / ⭐ 2 / 仓库提供从 OSCOR‑2301‑ja JSON 文件的「content」字段中提取的文本，并附带一个 Python 脚本，用于转换并打印每个「content」值。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 164 / ⭐ 15 / Hachi‑Alpaca 提供基于 Stanford Alpaca 的日语合成数据，经过 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 细化和验证，并通过 Deepinfra 使用，同时提供已通过模型质量检查的 “_cleaned” 版本。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 164 / ⭐ 4 / 来自 Fate/Stay Night 的角色 “Emilia” 的对话和背景故事数据集，格式化用于训练和评估会话语言模型。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 160 / ⭐ 32 / 剔除英文翻译数据的日本聊天机器人数据集，来源于 izumi‑lab/llm‑japanese‑dataset，提供 2.5 million+ 条条目（v1.0.0），用于在 CC‑BY‑SA 4.0 许可下对 Japanese LLMs 进行 instruction‑response tasks 的微调。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 158 / ⭐ 2 / 一份包含 64,139 条标注有生物性别的日语姓名的数据集，呈现为汉字、假名和平罗马字，其 44.9k 训练集、6.41k 验证集和 12.8k 测试集划分已在 ISDA’23 被接受。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 154 / ⭐ 13 / 一个采用 CC‑BY‑SA 3.0 许可的日语命名实体抽取数据集，来源于 Wikipedia，托管在 https://github.com/stockmarkteam/ner-wikipedia-dataset/，由 Stockmark Inc. 开发。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 153 / ⭐ 9 / JSICK 是从 SICK 翻译成日语的 NLI/STS 数据集，提供了一套压力测试，利用多个转换过的 sentence-pair subsets 来探测 word‑order 和 case‑particle 的处理，以支持多语言组合推理的研究。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 152 / ⭐ 5 / Japanese JaQuAD，QG‑Bench 的一个子集，提供句子级和段落级的数据，包含高亮的答案词元，用于训练日语问句生成模型，并通过 BLEU4、METEOR、ROUGE‑L、BERTScore 和 MoverScore 进行评估。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 146 / ⭐ 2 / Japanese COVID‑19 Twitter dataset: 一份 CSV，包含推文 ID，使用六种评估选项标注：一般事实、个人事实、观点、含糊 COVID 关联、不相关及未确定，旨在用于推文相关性与事实性的文本分类。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 137 / ⭐ 79 / 句式对齐的日文网络小说章节以及英文粉丝翻译 (106 K+ 条目，version 2) 旨在用于翻译研究，已更新对齐、添加系列元数据、无质量筛选，并按 fair‑use 与 Apache 2.0 分发，并可通过 Hugging Face 接受下架请求。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 131 / ⭐ 17 / 包含草薙寧々（来源 CV Machico）的 *Project Sekai* 歌声轨的部分数据集，附带 nene_org.txt 标注文件，计划扩充并标准化数据，并呼吁用户点星此 repo、分享想法、加入 QQ 群以获取完整收藏。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 130 / ⭐ 29 / 一个 CC‑BY‑4.0 许可的、手工提取的日本政府 FAQ 问答对（包含源 URL）的数据集，旨在用于指令调优和 RAG 测试，因其高质量而受到赞誉，但也被指出偶尔存在格式错误和强烈的官方政策语言。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 127 / ⭐ 7 / 已清洗的日语新闻语料库来自 livedoor news，使用 CC‑licensed，划分为 5,894 训练样本、737 验证样本和 736 测试样本。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 125 / ⭐ 3 / A 2010 Japanese Web Corpus, uploaded to HuggingFace and licensed for research per the 2009 copyright reform, 包含来自基于形态学的解析和转换脚本的自动标点化文本。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 125 / ⭐ 3 / J‑HARD‑TTS‑Eval 对日语自回归 TTS 模型在短序列稳定性、重复、韵律和连贯性等失败方面进行基准测试，提供带有提示音频和文本的数据集，可通过 Hugging Face 加载。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 120 / ⭐ 2 / JCommonsenseQA 是一份日语的多项选择常识推理数据集——CommonsenseQA 的改编版本——其授权为 CC BY‑SA 4.0，并以 doi:10.5715/jnlp.30.63 引用。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 120 / ⭐ 3 / AnimuSubtitle‑JP托管日本 ASS/SSA 字幕数据集（data_ass, data_TS），可使用 Python’s ass library 解析或在 Aegisub 编辑，并以 ODC‑By license 发布。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/llm-book/ner-wikipedia-dataset) - 📥 119 / ⭐ 2 / 日语版“Wikipedia‑based NER” v2.0 数据集卡，已由 StockMark 为书籍《Large Language Model Introduction》创建，基于 stockmarkteam/ner‑wikipedia‑dataset，并按 CC‑BY‑SA 3.0 分发。
 * [Longcontext-aozora-summary](https://huggingface.co/datasets/aixsatoshi/Longcontext-aozora-summary) - 📥 116 / ⭐ 6 / 来自 globis‑university/aozorabunko‑clean Aozora Bunko 集合中长文本的摘要数据集，使用 CC BY 4.0 许可证。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 116 / ⭐ 2 / 提供一个 Japanese Common Voice 17.0 子集，包含 649 位说话人（每人 30–300 条样本），共 45,668 条发声记录，按说话人按 80/20 分割，批量存入 1,000 条样本的 Parquet 文件，全部采用 CC0 许可。
 * [CC-news-2024-July-October-cleaned](https://huggingface.co/datasets/kajuma/CC-news-2024-July-October-cleaned) - 📥 106 / ⭐ 15 / 日本新闻文章（2024 年 7 月至 10 月）来自 Common Crawl 新闻子集，已用 Uzushio 清洗并通过 pipeline_03a.conf 过滤。
