# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专门收录日语NLP相关的Python库、LLM、词典和语料库资源的精选列表。
本页面列出了Hugging Face上可用的日语NLP专用模型和数据集。目前包含164个模型和109个数据集。

_更新于2026年3月22日_

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

| # | 模型名称 | Downloads | Likes | 类别 |
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

| # | 数据集名称 | Downloads | Likes |
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
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 480k / ⭐ 15 / 一个 12 层、768 隐藏层的日语 GPT‑NeoX 模型，训练数据为 CC‑100、C4 以及 Wikipedia，兼容 Huggingface，并配备可选的玩具前缀调优权重，能强制每个句子末尾以笑脸表情符号结束。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 444k / ⭐ 131 / 9亿参数的日语优化LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，训练数据截至2024年9月，采用混合 Mamba‑2/MLP/4‑层注意力架构，已在 Nemotron‑Personas‑Japan 工具调用数据集上微调，可选地在生成最终答案前生成可控的推理轨迹，且可商用。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 219k / ⭐ 20 / OpenCALM 是 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 许可证下发布的一套仅解码的日本 transformer 语言模型（160 M–6.8 B 参数），训练于 Japanese Wikipedia 和 Common Crawl，并可通过 Hugging Face’s torch‑transformers 使用。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 118k / ⭐ 58 / 一款由 ABEJA Inc. 使用日语 CC‑100 和 OSCAR 训练的 2.7B 参数日语 GPT‑NeoX 模型，可通过 Hugging Face Transformers 管道或 PyTorch 使用，按 MIT 许可证发布。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 40k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一个 13‑B 的、基于指令预训练的日语语言模型，由 NII 的研发中心开发，并以 Hugging‑Face Transformers 检查点的形式发布，使用 UNIGRAM‑byte‑fallback 分词器。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 39k / ⭐ 28 / LFM2.5‑1.2B‑JP 是一个 1.2 B 参数的日语文本生成模型，基于 LFM2.5 混合架构构建，优化用于生成和完成任务，托管在 Hugging Face 上，并可通过 llama.cpp 运行。
 * [llm-jp-3.1-13b](https://huggingface.co/llm-jp/llm-jp-3.1-13b) - 📥 24k / ⭐ 2 / llm‑jp‑3.1‑13b 是来自 NII 研发中心的 13 B‑参数变换器 LLM，已在日语文本上预训练，并以 Hugging Face 格式提供，要求 torch ≥2.3、transformers ≥4.40，此外还提供微调 checkpoints 和 unigram byte‑fallback tokenizer。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 17k / ⭐ 18 / 使用 Shisa 7B 数据，微调了日语 Stable LM Base Gamma 7B，在 JA MT‑Bench 上取得了强劲的表现。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 14k / ⭐ 146 / Llama‑3‑ELYZA‑JP‑8B 是由 ELYZA 开发的、经过日语增强的 80 亿参数 Llama 3 模型，在 Meta‑Llama‑3‑8B‑Instruct 上针对日语微调。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 13k / ⭐ 56 / TinySwallow‑1.5B‑Instruct 是一个 1.5 B 的日语指令调优自回归语言模型，使用 TAID 从 Qwen2.5‑32B‑Instruct 进行蒸馏，供研究用途。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 11k / ⭐ 21 / Llama3 Swallow 是 Meta Llama 3 系列的日语增强版本，于 2024 年 7 月 1 日发布，提供 8B 与 70B 版本的 Instruct 与 chat 模式，已在 Megatron‑LM 上使用 SFT 与 Chat Vector 进行微调，并在关键的日语 NLP 任务上进行了基准测试。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 11k / ⭐ 18 / Llama 3.1 Swallow 是一组 8‑B 和 70‑B 模型，它们继续对 Meta 的 Llama 3.1 进行预训练，以提升日语语言性能，然后在合成日语数据上进行指令微调，提供多种已发布的变体，其对话行为已改进，与 gemma‑3‑27b‑it 相当。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 10k / ⭐ 25 / rinna 的日语 GPT‑2 small 是一个 12 层、768 维隐藏层的 Transformer，训练于日语 CC‑100 和 Wikipedia，使用 SentencePiece 进行分词，发布于 2021 年 8 月 25 日，遵循 MIT 协议（Hugging Face: rinna/japanese‑gpt2‑small，参见 https://arxiv.org/abs/2404.01657）。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 10k / ⭐ 50 / GGUF‑formatted NVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese，已从 imatrix 数据集重建，并准备好在 CUDA 上使用 llama.cpp 运行。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 9k / ⭐ 24 / Llama 3.1 Swallow 是一系列日语增强的 8B/70B Llama 3.1 模型，通过持续预训练和日语特定指令微调训练，最新的 8B‑Instruct‑v0.3 在日语 MT‑Bench 上取得了最先进的结果。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 9k / ⭐ 4 / 实验性日语模型通过使用聊天向量方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 与 Meta‑Llama‑3‑8B‑Instruct 之间的差异创建，然后上采样并应用于 Meta‑Llama‑3‑70B‑Instruct，显示出变化不大，并计划未来扩大规模。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 7k / ⭐ 18 / GPT‑OSS‑Swallow v0.1 提供 20B 和 120B 双语日英 LLM，通过 CPT、SFT 和 RLVR 训练，能够在数学和编码任务上与 GPT‑OSS 匹配或超越，于 2026 年 2 月发布，包含四种 SFT/RL 变体，并将推出量化版本。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 7k / ⭐ 19 / 提供 1.8 B 参数 llm‑jp‑3.1‑1.8b‑instruct4 日本指令微调模型，来自 NII，兼容 Hugging Face Transformers 和 Torch ≥ 2.3.0，包括预训练和微调检查点以及使用示例.
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 5k / ⭐ 8 / Qwen3‑Swallow v0.2 提供了通过 CPT、SFT 和 RLVR 训练的日英 LLM（30B‑A3B 和 32B），保持了强大的数学、编码和推理能力，已发布九个模型以及 AWQ 量化版本。
 * [Qwen3-Swallow-8B-CPT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2) - 📥 4k / ⭐ 1 / 双语 30 B‑和 32 B‑参数 LLMs，Qwen3‑Swallow v0.2，采用 CPT、SFT 和 RLVR 构建，擅长日语、日英翻译、数学和编码，匹配或超越 Qwen3，并以 AWQ‑量化形式在 Hugging Face 上发布。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 3k / ⭐ 20 / OpenCALM 是 CyberAgent 开发的日本解码器（decoder‑only）Transformers 语言模型系列（160 M–6.8 B 参数），基于日本维基百科和 Common Crawl 训练，并以 CC BY‑SA 4.0 许可证发布。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 3k / ⭐ 107 / 一款 1.3‑B‑parameter、24‑layer transformer GPT‑1B，使用 Japanese C4、CC‑100 和 Wikipedia 进行训练，于 2022 年 1 月 26 日由 rinna Co. 发布，并在 MIT license 下公开。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 3k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27 B 参数扩展版，已在包含 instruct 和 fast 变体的日语数据上预训练，可通过 Hugging Face Transformers 使用。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 3k / ⭐ 85 / Rinna 的 24 层、1024 隐藏单元的日语 GPT‑2‑medium 模型，基于 CC‑100 和维基百科训练，采用 SentencePiece 分词，已在 rinna/japanese‑pretrained‑models 仓库公开（MIT 许可证，2021 年 4 月 7 日发布，2021 年 8 月 25 日更新）。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 3k / ⭐ 26 / Japanese 3.6 B‑parameter GPT‑NeoX 模型细调以适应指令遵循（SFT‑v2），对比之前的 SFT 与 ChatGPT 在 100 条提示上进行评估，发布于 2023 年 3 月 31 日。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 3k / ⭐ 7 / 预训练的 TinyLlama 在日语（≈50 k 步），基于约3 B OSCAR/mC4 tokens，可通过 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 和 Renju Aoki 创建。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 3k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 与 Swallow Team 开发的紧凑型日语指令遵循语言模型，采用 Qwen2.5‑32B‑Instruct 的 TAID 蒸馏，并在日语文本上进一步预训练，且仅以 Apache 2.0 许可证供研究使用。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 3k / ⭐ 36 / 提供了一款来自 SB Intuitions 的自回归式日语语言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已与其他模型进行基准测试，并附示例使用脚本，且安全训练有限。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 2k / ⭐ 10 / 仓库提供 GGUF 格式、量化的模型文件，适用于 Stability AI 的日本版 StableLM Instruct Gamma 7B，由 Massed Compute 硬件创建，并且是 TheBloke 的 a16z‑资助 LLM 工作的一部分。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 140 / LFM2.5‑1.2B‑JP 是一款针对日语优化的聊天模型，在日语知识与指令遵循方面优于 LFM2，支持使用 LoRA 进行微调，支持通过 Transformers、vLLM 和 llama.cpp 进行推理，取得 50.7 JMMLU、58.1 M‑IFEval 与 56.0 GSM8K 分数。
 * [GPT-OSS-Swallow-20B-SFT-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-SFT-v0.1) - 📥 2k / ⭐ 5 / GPT‑OSS‑Swallow v0.1 是一个双语日英模型系列（20B & 120B），通过持续预训练、监督微调和带可验证奖励的强化学习来训练，以保持数学和编码性能，目前已发布 SFT 和 RL 变体，并计划发布量化版本。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 2k / ⭐ 21 / youri‑7b 是一个32层、4096隐藏单元的 transformer，基于 Llama2‑7b 构建，持续在约 40 B 个日语 token（CC‑100、C4、OSCAR、Pile、Wikipedia）上进行预训练，并于 2023 年 10 月 31 日发布，在 AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA 和 Winogrande 上取得了竞争性的分数。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 1k / ⭐ 1 / Qwen3‑Swallow v0.2 提供了 30‑B 和 32‑B 双语日英 LLM，采用 CPT、SFT 与 RLVR 训练，提升日语准确性、翻译、数学与编码能力，以匹配或超越原始 Qwen3，提供九个模型（CPT、SFT、RL）和 AWQ‑quantized 版本，同时发布 GPT‑OSS‑Swallow。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 1k / ⭐ 3 / LLM‑jp‑3‑150m——来自国立信息学研究所LLM研发中心的150 M参数日语语言模型——以 Hugging Face Transformers 格式发布，需要 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，并且在日本维基百科、Common Crawl、WARP/PDF、WARP/HTML 和 Kaken 数据上使用 unigram byte‑fallback tokenizer 进行预训练。
 * [japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) - 📥 1k / ⭐ 75 / 一个 3.6 billion 参数的日语 GPT‑NeoX 模型，训练于约 650 GB 的日语文本（C4、CC‑100、Oscar、网络爬虫），在内部 C4 验证集上达成 7.50 的困惑度，并以 Apache 2.0 许可证发布。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ](https://huggingface.co/dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ) - 📥 1k / ⭐ 3 / 提供一个 4‑bit、4.11 GB 的量化版本的 Meta Llama‑2 7B（ELYZA‑japanese‑Llama‑2‑7b‑fast‑instruct），减少内存使用但会降低指令遵循效果，需 GPU 和 autoGPTQ，并包含对替代 AWQ、llama.cpp 和 gguf 量化及基准结果的引用。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 1k / ⭐ 16 / 一个6层、512隐藏单元的Transformer，称为Japanese GPT‑2 xSmall，在Japanese CC‑100和Wikipedia上使用SentencePiece分词训练，于2021年8月25日以MIT许可发布，并托管在Hugging Face（rinna/japanese‑gpt2‑xsmall）上，在arXiv 2404.01657中被引用。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 82 / 来自 ELYZA 的日语增强版 Llama‑2‑7B，已预训练以提供扩展的日语语言能力，提供标准、指导和快速版本，附有详细使用示例、开发者署名，并遵循 Meta’s Llama‑2 Community License 许可。
 * [Murasaki-4B-v0.3-GGUF](https://huggingface.co/Murasaki-Project/Murasaki-4B-v0.3-GGUF) - 📥 1k / ⭐ 1 / Murasaki‑4B‑v0.3 是一个 4 billion 参数的 GGUF System 2 推理模型，专为 ACGN 日英翻译优化，具备提示控制的 CoT 开关、增强的 Non‑think 模式、BF16 基准以及多种量化；全部采用 CC BY‑NC‑SA 4.0 许可证。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 1k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter Japanese extension，进一步预训练以适用于日语语言任务，并提供 base、instruct、fast 和 fast‑instruct 变体，由 ELYZA team 在 Llama 2 Community License 下维护。
 * [japanese-stablelm-instruct-beta-70b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-beta-70b) - 📥 1k / ⭐ 26 / Japanese‑StableLM‑Instruct‑Beta‑70B 是一个 70‑十亿参数的仅解码端 Llama2‑基础日语语言模型，在 Dolly‑15k、Anthropic HH 以及其他公开数据上微调，可提供 7‑十亿参数版本，并在 Llama2 Community License 下发布。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 1k / ⭐ 96 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 7 B 的日语优化扩展，提供 instruct 和 fast 变体，参数为 6.27–6.37 B，可通过 Hugging‑Face Transformers 库访问。
 * [stockmark-13b](https://huggingface.co/stockmark/stockmark-13b) - 📥 1k / ⭐ 39 / Stockmark‑13b是一款拥有13 B 参数的日语大型语言模型（LLM），在大约220 亿个标记上进行训练——并提供一个指令调优版本——使用 AWS Trainium 上的 neuronx‑nemo‑megatron 构建，并由 Stockmark Inc. 以 MIT 许可证发布。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 1k / ⭐ 15 / LLM‑jp提供13 B和1.3 B变压器语言模型，包括多种指令调优变体，采用Megatron‑DeepSpeed和Hugging Face Transformers生态系统构建。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 1k / ⭐ 16 / 来自 NII 研发中心的日本大型语言模型集合（1.8 b 至 172 b beta1，含 instruct 版本），以 Hugging Face Transformers 格式打包，并在混合日语、英语与网络语料库（总计>1万亿个标记）上预训练。需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29 以及 flash‑attn ≥ 2.5。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 470k / ⭐ 76 / Japanese BERT‑base 在 2019 年日本维基百科上预训练，使用 IPA‑dictionary 与全词掩码，12 层 768 维，32,000 词表，512 标记序列，1 M 步骤，可在 cl‑tohoku/bert‑japanese 获取，遵循 CC‑BY‑SA 许可。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 234k / ⭐ 41 / 一个预训练于约 17 M 条日语维基百科句子（2.6 GB）的 BERT base 模型，使用 IPA 字典和 WordPiece 进行分词，拥有 12 层 / 768‑维隐藏状态 / 12 头，32 000‑token 词汇表，已在 Cloud TPUs 上训练了 1 M 步，并以 CC‑BY‑SA 3.0 许可发布。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 177k / ⭐ 9 / 日语 DeBERTa V2 大型模型，已在 171 GB 的日语 Wikipedia、CC‑100 与 OSCAR 上训练，使用字符级 SentencePiece 分词和全词掩码，已准备好通过 Hugging Face Transformers 进行下游微调。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 89k / ⭐ 8 / 一个 BERT‑base 日语模型（12 层，768 维隐藏，12 头），使用 MeCab IPA 词级分词后再进行字符级分词生成 4000 词的词表，在约 1700 万句来自日语维基百科（2.6 GB）的句子上预训练，训练代码位于 cl‑tohoku/bert‑japanese，采用 CC BY‑SA 3.0 许可证发布。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 44k / ⭐ 6 / 一个 BERT‑base 日语模型（12 层，768-维隐藏状态，12 头），在 3000 万条维基百科句子（约 4 GB）上训练，使用 Unidic 2.1.2 词级分词，随后进行字符级分词和全词掩码，使用 512 令牌序列，256 批次，以及 1 M 训练步骤。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 28k / ⭐ 5 / ModernBERT‑Ja‑30M 是一种日语 BERT 变体，融合了本地和全局注意力与 RoPE，训练于 4.39 TB 日英文本，支持 8,192 令牌序列，参数规模从 30 M 到 130 M，最佳搭配 Flash Attention 2。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 16k / ⭐ 48 / LINE DistilBERT Japanese 是一个 6600 万参数的 DistilBERT 模型，已在 131 GB 的日语网页文本上使用内部 BERT‑base 教师进行预训练，评估基准为 JGLUE，采用 MeCab Unidic 与 SentencePiece 进行分词，并以 Apache 2.0 许可证发布。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 13k / ⭐ 27 / Japanese BERT‑base（12 层，768 隐藏，12 头）在 4 GB 的日语维基百科（≈30 M 句）上预训练，使用 Unidic 2.1.2 词级分词、WordPiece 子词分词和全词遮蔽。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 11k / ⭐ 39 / Japanese‑Roberta‑Base 是来自 rinna Co., Ltd. 的预训练掩码语言模型，提供了正确加载、token 预处理、position‑id 处理的准则，以及强调需要前置 [CLS] token 和一致 tokenization 的使用示例。
 * [jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - 📥 6k / ⭐ 3 / 日本 RoBERTa‑base 模型，预训练于约1000万条日本医学摘要和140万条来自 JST 的正文文本，采用 30 k‑token SentencePiece 进行分词，采用 CC BY‑4.0 许可证发布，可通过 Hugging Face pipelines 使用。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 6k / ⭐ 47 / 这是一款 1.32 亿参数的日语 ModernBERT 模型，融合了 local‑global 与 RoPE 注意力机制，训练于 4.39 T 词条（日语/英语），词表大小 102k，最大序列长度 8,192，针对 Flash Attention 2 做了优化。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 5k / ⭐ 30 / Japanese DeBERTa V2 基础模型已在 171 GB 的日语维基百科、CC‑100 和 OSCAR 数据上预训练，使用 Juman++ 分词和 SentencePiece 标记化，经过三周在八块 NVIDIA A100 GPU 上训练，现已准备好用于微调。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 5k / ⭐ 2 / Japanese DeBERTa V2 tiny，在约171 GB的日本维基百科、CC‑100 与 OSCAR 语料库上预训练，需使用 Juman++ 词分割，训练耗时 33 小时，使用8块 NVIDIA A100 GPU，并可用于下游任务的微调。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 5k / ⭐ 20 / ModernBERT‑Ja‑310M 是一种日语 BERT 变体，融合了局部-全局注意力和 RoPE，训练于 4.09 T 日语/英语文本，支持 102 400 词汇量、8 192 令牌序列，并针对 Flash Attention 2 进行了优化。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 2k / ⭐ 4 / DeBERTaV2 base 在日本语语料库（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上训练，并使用 FP‑16 微调进行 NLU 任务（JSTS、JNLI、JCommonsenseQA），以 CC BY‑SA 4.0 许可发布，并由日本研究资助。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 12 层，768 维度的 BERT‑Base 日语模型，在 2.6 GB Wikipedia（≈17 M 句子）上训练，使用 IPA‑dictionary 字符分词与 whole‑word masking，并在 CC‑BY‑SA 3.0 许可下发布。
 * [deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 📥 1k / ⭐ 9 / Japanese DeBERTa‑V2 大模型预训练于 171 GB 日文文本（Wikipedia、CC‑100、OSCAR），使用 Juman++ 分词，在 8 台 A100 GPU 上训练 36 天，可针对下游任务进行微调。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 52k / ⭐ 11 / 用于生成句子嵌入的 Japanese Sentence‑BERT (v1) 模型，已提供改进版 v2，并通过 Hugging Face Transformers 以及自定义的 `SentenceBertJapanese` 类进行示例使用。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 48k / ⭐ 51 / 一款在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上使用 MultipleNegativesRankingLoss 细调的 Japanese Sentence‑BERT v2，较 v1 提升了约 1.5–2 %的准确率，并以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 发布。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 44k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一个 Apache‑2.0 许可的日语 CLIP 模型，基于 ViT‑B/16，训练于 CC12M captions 翻译成日语，并于 2022 年 5 月 12 日发布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 22k / ⭐ 29 / LY Corporation的clip‑japanese‑base 是一个日语 CLIP 模型，在约10亿对图像‑文本对上训练，使用 Eva02‑B transformer 图像编码器和 12 层 BERT 文本编码器，在 STAIR 上实现 R@1 0.30，在 Recruit 上得到 0.89 的准确率，在 ImageNet‑1K 上得到 0.58 的准确率，并支持 zero‑shot 图像分类和检索。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 13k / ⭐ 22 / Sarashina‑Embedding‑v2‑1B 是一个 1,792 维的日语句子变换器，使用多阶段对比学习训练，获得了前沿的 JMTEB 分数，可通过 Sentence‑Transformers 并搭配可选指令前缀，用于语义相似度、搜索、改写挖掘、分类和聚类。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 12k / ⭐ 2 / ja_ginza_electra 是一个 spaCy v3 Python 包，提供一个在 mC4 和 UD_Japanese_BCCWJ r2.8（基于 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator）上微调的日语 ELECTRA 模型，并配有自定义 bunsetu‑phrase 检测功能，按 MIT license 分发。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 10k / ⭐ 14 / Japanese Sentence‑LUKE 模型在与 Sentence‑BERT 同一数据集上训练，表现超过或匹配其性能，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，并通过 Hugging Face Transformers 的 MLukeTokenizer 与 LukeModel 进行使用。
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 9k / ⭐ 4 / fastText 是一个轻量级、开源库，能够在标准的 CPU 上快速学习单词和句子嵌入以及分类器，几分钟内训练数十亿个单词，可压缩以便移动使用，并提供用于分类和语言识别的预训练向量。
 * [japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16) - 📥 7k / ⭐ 13 / Japanese CLOOB‑VIT-B-16 是基于 vit‑base‑patch16‑224 的视觉-语言模型，在翻译后的 CC12M 标题上训练，并于 2022 年 5 月 12 日由 rinna Co., Ltd. 以 Apache 2.0 许可发布。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 5k / ⭐ 17 / 日本CLIP模型 clip‑japanese‑base‑v2，升级后约20亿图像‑文本对并采用蒸馏，配合 Eva02‑B 图像编码器和 12 层 BERT 文本编码器，将 ImageNet‑1k 准确率提升至 0.708，超过前代模型。
 * [japanese-avhubert-base_noise_pt](https://huggingface.co/enactic/japanese-avhubert-base_noise_pt) - 📥 4k / ⭐ 1 / 用于日语 AVHuBERT AV‑SR 模型的仓库，该模型在约2,250小时的音频‑视觉数据上预训练，并通过广泛的噪声增强实现了鲁棒的语音识别。
 * [japanese-avhubert-large_noise_pt](https://huggingface.co/enactic/japanese-avhubert-large_noise_pt) - 📥 2k / ⭐ 1 / 一个预训练的 2,250 小时 AVHuBERT Large 自监督模型，在日本音频-视觉数据上训练并使用噪声增强，以稳健支持音频-视觉语音识别。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 2k / ⭐ 55 / 一个Japanese‑language T5 model，在约100 GB的Wikipedia和OSCAR数据上使用SentencePiece tokenization进行预训练，超越了Google’s multilingual T5在news‑classification benchmark上的表现，但需要fine‑tuning，并可能产生biased outputs.
 * [amber-large](https://huggingface.co/retrieva-jp/amber-large) - 📥 2k / ⭐ 7 / AMBER 是 Retrieva Inc. 的一个 315 百万参数嵌入模型，扩展了 sbintuitions/modernbert‑ja‑310m 用于日语（可选英文支持），提供 768 维、提示驱动的嵌入，并以 Apache 2.0 许可发布。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 2k / ⭐ 3 / 一个日语 BERT‑base 模型，在 JSNLI 上使用有监督 SimCSE 进行微调，通过 Sentence‑Transformers 或 HuggingFace 提供，采用 CLS 池化。在 1M 个样本上训练，批量大小为 512，学习率为 5×10⁻⁵，温度为 5×10⁻⁵，64 令牌限制，采用 BFloat16 精度。

### sentence-similarity
 * [JaColBERTv2.5](https://huggingface.co/answerdotai/JaColBERTv2.5) - 📥 633k / ⭐ 22 / 用于最终 JaColBERTv2.5 检查点的权重，仅在 JaColBERTv2 数据的 40% 及新配方下训练，已在所有数据集上优于之前所有模型——包括 JaColBERTV2 多语言变体，如 BGE‑M3。
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 448k / ⭐ 67 / Ruri v3 是基于 ModernBERT‑Ja 的先进日语文本嵌入模型，支持多达 8,192 词元输入，100K 词元词汇表，FlashAttention 加速推理，并提供多种尺寸变体，便于快速使用 sentence‑transformer。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 395k / ⭐ 11 / 日语通用文本嵌入模型（Ruri‑v3，30‑310 M 参数，8192‑token 最大，JMTEB 分数高）与 Sentence‑Transformers 使用示例以及与其他日语嵌入模型的基准对比一起提供。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 179k / ⭐ 8 / Ruri v3是一个最先进的日语文本嵌入模型，基于ModernBERT‑Ja构建，支持最多8,192个标记，拥有100 k词汇量，支持FlashAttention加速，并提供多种规模，从37 M到315 M参数。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 129k / ⭐ 9 / 包括 Ruri v3 日语文本嵌入（30 M–310 M 参数，8192‑token 限制，JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前缀的 Sentence Transformers 指令，以及对数个日语模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基准结果。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 32k / ⭐ 44 / PLaMo‑Embedding‑1B 是 Preferred Networks 的一款日语文本嵌入模型，它将日语文本转换为向量，用于信息检索、分类和聚类，在 JMTEB 基准上表现出强大性能，并且在 Apache v2.0 许可证下可免费使用。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 30k / ⭐ 34 / GLuCoSE 是一个基于 LUKE 的日语句子嵌入模型，输出 768 维均值池化向量（最多 512 个标记），在 Web 和 NLI/搜索数据上训练，在相似性基准测试中达到了 0.864 的 Spearman 相关系数和 0.818 的 Pearson 相关系数。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 28k / ⭐ 4 / Ruri v3 是基于 ModernBERT‑Ja 的前沿日语文本嵌入模型，支持最多 8192 token 序列、100K token 词汇量、FlashAttention，并以 30 M 至 310 M 参数规模发布，供 sentence‑transformers 使用。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 28k / ⭐ 16 / JaColBERTv2 是一个仅适用于日语的基于 ColBERT 的检索模型，在 MMarco 上通过知识蒸馏训练（每个正例 31 个负例，250k 次，batch 32）。目前它优于 multilingual‑e5‑large、BGE‑M3 和 JaColBERT，完整评估正在进行中。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 21k / ⭐ 22 / GLuCoSE v2 是一款 CPU 友好的日语文本嵌入模型，通过蒸馏和多阶段对比学习进行微调，提供卓越的语义相似性和检索性能——在 MIRACL 及相关基准上优于同等规模的模型。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 21k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一个 768 维的句子变换器，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，训练了一个 epoch 的 shunk031/jsnli，并包含用于聚类、语义搜索以及同时兼容 Sentence‑Transformers 和 HuggingFace 的示例。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 11k / ⭐ 44 / 一组已准备好发布的 Ruri v3 日语文本嵌入模型（30m–310m），完整附带 SentenceTransformer 使用技巧、查询/段落前缀，以及 JMTEB 基准结果，展示它们与其他日语和多语言嵌入模型的比较。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 10k / ⭐ 2 / Ruri v3 提供高性能的日语文本嵌入，支持至 8192 个 token，拥有 100k 个 token 的词汇表，支持 FlashAttention，并提供多种模型规模（30 m–310 m），以实现高效推理和通过 sentence‑transformers 进行微调。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 3M / ⭐ 53 / Japanese wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 与 JSUT 上微调，需 16 kHz 音频，并可通过 HuggingSound 或 HuggingFace 管道使用。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 18k / ⭐ 89 / Kotoba‑Whisper v2.0 是从 OpenAI Whisper large‑v3 蒸馏出的日语 ASR 模型，训练于 720 万个 ReazonSpeech 剪辑，推理速度快 6.3 倍，同时在同域测试中匹配教师模型的 CER/WER，并提供 stable‑ts/标点支持以及完整的训练代码在 GitHub 上。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 15k / ⭐ 96 / Kotoba‑Whisper‑v2.2 是一个日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了说话人划分和自动标点功能，通过 HuggingFace‑Transformers pipeline，并与 Asahi Ushio 与 Kotoba Technologies 合作开发。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 9k / ⭐ 128 / Anime Whisper 是一款轻量级的日语 ASR 模型，在约 5,300 小时的动漫风格对话上进行微调，能够提供低幻觉、节奏对齐标点，以及准确转录非言语声音和 NSFW 内容，并且需要在没有初始提示的情况下运行。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 8k / ⭐ 46 / NVIDIA NeMo 的 0.6 B 参数 Hybrid FastConformer‑TDT‑CTC ASR 模型可转写带标点的日语语音，并可在 NeMo 框架内用于推理或微调。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 8k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供了快 6.3 倍的蒸馏 Whisper 模型，用于日语和英语 ASR，并实现双向语音转文本翻译，这些模型是基于 OpenAI 的 Whisper large‑v3 通过知识蒸馏、交叉熵和 KL‑divergence 损失构建。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 3k / ⭐ 19 / Kotoba‑Whisper‑v2.1 是一种日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了标点后处理管道，保持可比的 CER 性能，同时实现无缝、标点感知的转录。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 2k / ⭐ 37 / reazonspeech-nemo-v2 是一个 619‑M‑参数的日语长文本 ASR 模型，基于改进版 Fast‑Conformer 及 Linearly Scalable Attention，在 ReazonSpeech v2.0 语料库上训练，支持通过 subword RNN‑T decoder（3000‑token SentencePiece）进行多小时推理，并以 Apache 2.0 许可分发。
 * [moonshine-tiny-ja](https://huggingface.co/UsefulSensors/moonshine-tiny-ja) - 📥 2k / ⭐ 11 / Moonshine AI的小型、边缘就绪ASR模型能够实时转录日语语音，并在model card中详细说明低资源部署。
 * [kotoba-whisper-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.0) - 📥 2k / ⭐ 58 / Kotoba‑Whisper v1.0 是一个从 OpenAI 的 Whisper large‑v3 提炼出的日语 ASR 模型，提供了 6.3 倍的速度提升并保持相当的准确性，训练数据为 1,253 小时的 ReazonSpeech，其代码（以及在 Hugging Face 上的更新版 v2.0）已公开可用。

### text-ranking
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 46k / ⭐ 7 / 日语 CrossEncoder 再排序模型，覆盖 xsmall 到 large（含 BGE），在 JQaRA、JaCWIR、MIRACL 与 JSQuAD 上进行评估，并为 sentence_transformers 与 HuggingFace 提供即用的集成示例。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 19k / ⭐ 6 / 快、轻量级的日语 Reranker v2 模型（tiny、xsmall、small、base），带有基准测试分数和 GPU 速度，可通过 sentence_transformers CrossEncoder 与 transformers ≥ v4.48 使用（可选闪存加速 flash‑attn），并且在 ONNX/量化形式下可用于 CPU/ARM。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 8k / ⭐ 13 / Ruri‑v3 Reranker 是一个基于 ModernBERT‑Ja 构建的稳健日语文本重排器，支持最高 8,192‑token 序列、100k‑token 词汇表、FlashAttention 以及 SentencePiece 分词器，并可通过 sentence‑transformers 使用。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 3k / ⭐ 2 / Japanese‑reranker‑small‑v2 是一系列轻量级、快速的日语重排序模型（v2），提供从极小到基础的变体，最高可达 0.89 的平均分，GPU 推理时间为 2–15 秒，支持交叉编码器选项，并需要 Hugging Face Transformers v4.48+，可选 Flash Attention 2 进行加速。
 * [ruri-reranker-small](https://huggingface.co/cl-nagoya/ruri-reranker-small) - 📥 3k / ⭐ 2 / 基于 Sentence Transformers 的 CrossEncoder 构建的日语句子重排序器，提供推理代码、基准测试结果以及多种模型尺寸，用于日语文本排序。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 2k / ⭐ 15 / 一个日语 CrossEncoder 重新排序器套件——包括 xsmall、small、base、large 和 japanese‑bge‑reranker‑v2‑m3‑v1——配合示例用法、在多个基准上的评估指标和支持文档。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 2k / ⭐ 16 / 日语 CrossEncoder 重排序模型——从xsmall到large——在日语文本上训练，通过sentence_transformers公开，评估在JQaRA、JaCWIR、MIRACL和JSQuAD上。
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 1k / ⭐ 4 / 日本训练的 CrossEncoder 重新排序器，尺寸从 xsmall（384）到 large（1024），以及 BGE‑v2‑m3‑v1 模型，提供微调、推理和 JQaRA、JaCWIR、MIRACL、JSQuAD 上的基准分数示例代码。
 * [ruri-reranker-large](https://huggingface.co/cl-nagoya/ruri-reranker-large) - 📥 1k / ⭐ 12 / 一个日语跨编码器重新排序器，使用 Sentence Transformers 构建，演示了不同规模 Ruri‑Reranker 模型的推理使用和基准结果。

### text-classification
 * [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) - 📥 777k / ⭐ 3 / Finance Sentiment JA (base) 是基于 BERT 的日语情感模型，训练于翻译后的 Financial PhraseBank，能够将日语金融新闻分类为正面、负面或中性，宏观 f1 为 0.959，准确率 0.967，每秒 134.9 个样本。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 238k / ⭐ 15 / 在亚马逊产品评论上对日语 BERT (cl‑tohoku/bert‑base‑japanese‑v2) 进行微调，用于情感分类，经过6个周期，学习率为2 × 10⁻⁵，达到约81 %准确率和0.73 F1。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 11k / ⭐ 15 / 训练于 chABSA 数据集的日语情感分析模型，获得 loss 0.0001、accuracy 1.0、F1 1.0，由 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 构建，使用 Adam（learning rate 2e‑05、10 epochs、batch size 16）优化，并通过 `model(**inputs)` 进行评估。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 4k / ⭐ 2 / 一个基于 Japanese BERT‑based model 的模型，已在 JGLUE JSTS 数据集上 fine‑tuned，用于语义相似性评分——在《Large Language Model Introduction》第5章中介绍——配有 Colab notebooks、transformers‑pipeline 用法以及 Apache 2.0 许可证。
 * [luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 📥 3k / ⭐ 43 / 一个在WRIME数据集上微调的日本LUKE模型，用于分类句子中表达的八种情绪——喜悦、悲伤、期待、惊讶、愤怒、恐惧、厌恶、信任。
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 1k / ⭐ 6 / 一款在 WRIME 数据集上微调的日语 BERT BASE 可为作家和读者预测八种情绪（喜悦、悲伤、期待、惊讶、愤怒、恐惧、厌恶、信任）的 0‑4 强度得分，代码已公开，在 K80 上训练耗时 3 小时，作家的均方误差约为 0.6，读者约为 0.2。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 338k / ⭐ 12 / 一个基于新 VNTL 数据集构建的 LLaMA 3 Youko qlora 微调模型，优化用于准确、逐字翻译日本视觉小说为英文，不使用聊天模式，采用默认 LLaMA 3 提示，并推荐中性采样（温度 0，无重复惩罚）。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 54k / ⭐ 73 / 来自 Opus 语料库的日语‑英语 Transformer‑Align 机器翻译模型，使用归一化和 SentencePiece 预处理，在 Tatoeba 测试集上达到了 41.7 BLEU 和 0.589 chr‑F。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 47k / ⭐ 28 / 已微调、GGUF-量化的 LFM2-350M checkpoint，用于近实时双向日英短至中等文本翻译，可通过 llama.cpp 使用。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 12k / ⭐ 118 / PLaMo Translation Model 是由 Preferred Networks 创建的大规模语言模型，专用于翻译任务，提供基础版、后训练版和评估版，在 PLaMo community license 下发布，并未针对聊天或其他下游用途进行 instruction‑tuned。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 2k / ⭐ 8 / Sugoi LLM 14B Ultra (GGUF) 是一个日语到英语的翻译模型，BLEU 分数为 21.38，几乎是其之前的 13.67 的两倍，在 RPG‑Maker 括号文本、提示遵循强度以及为交互式聊天 UI 的 JSON 输出方面表现出色。

### token-classification
 * [MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - 📥 57k / ⭐ 12 / 日本医学文档命名实体识别模型（下载这五个文件，运行 **predict.py** – 输出疾病、药物、日期等实体标签），用于 NAISTSOC 2022 NTCIR‑16 Real‑MedNLP 任务。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 17k / ⭐ 10 / Fine‑tuned Japanese BERT‑Base适用于在维基百科数据集上的命名实体识别，该模型在《*Large Language Model Introduction*》一书第六章中呈现，并可通过Hugging Face transformers pipeline进行部署（Apache 2.0 许可）。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 15k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日语 NER，能够提取八种实体类型（公司、政治/其他组织、设施、产品、事件），通过 `BertForTokenClassification` 实现，训练数据来自 Stockmark Wikipedia dataset，并可通过安装 `transformers`、`unidic_lite` 和 `fugashi` 使用，遵循 CC BY‑SA 3.0 许可。
 * [bert-base-japanese-v3-crf-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset) - 📥 2k / ⭐ 2 / CRF增强的BERT-base-japanese-v3在Wikipedia数据上微调用于日语NER，正如《Large‑Language‑Model Intro》一书（Apache 2.0 许可证）所示。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 在日语 NER 语料库上对 XLM‑RoBERTa‑base 进行微调（标签 PER, ORG, LOC, INS, PRD, EVT），使用 5‑epoch Adam（lr 5e‑5，batch 12），达到 0.0173 的验证损失，已发布在 Transformers 4.23.1 和 PyTorch 1.12.1。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 312k / ⭐ 169 / Manga OCR 是一款 Vision Encoder‑Decoder OCR 工具，可读取纵向和横向的日语漫画文本，包括 furigana，适用于多种字体和低质量图像，并且源代码可免费获取。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 111k / ⭐ 5 / Meikiocr的 `meiki.text.recognition.v0`——基于 D‑FINE 的 MobileNetV4 模型，在日本视频游戏文本上微调——为水平文本提供最先进的准确率和延迟，能够从 960×32 的输入中检测多达 48 个字符，并输出每个字符的边界框和置信度分数。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 102k / ⭐ 3 / meikiocr 提供一个基于 D‑FINE、开源权重的视频游戏文本检测模型（v0.1，使用 MobileNet‑v4 骨干网络，提供两种分辨率变体和 64‑box 限制），以及实验性的低延迟 tiny 与 small 变体，训练材料来自日本视频游戏和漫画。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 1k / ⭐ 16 / Sarashina2.2‑Vision‑3B 是一个 3B 参数的日本大型视觉语言模型，基于 Sarashina2.2‑3B‑Instruct 和 SigLIP 图像编码器，在日本 VQA 基准测试上表现出强劲的性能。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 2k / ⭐ 121 / 从 PaddleOCR‑VL 微调得到的 PaddleOCR‑VL‑For‑Manga 在 Manga109 的对话框裁剪图像上实现了70%完整句子准确率—是27%基线的三倍以上—并使用多语言数据集，包含训练代码和开发者指南。
 * [Heron-NVILA-Lite-15B](https://huggingface.co/turing-motors/Heron-NVILA-Lite-15B) - 📥 1k / ⭐ 14 / Heron‑NVILA‑Lite‑15B‑hf 是一个日语中心的视觉语言模型，基于 NVILA‑Lite 架构构建，采用 PALIGEMMA‑SIGLIP 视觉编码器、一个 MLP‑downsample 投影器以及 Qwen2.5‑14B‑Instruct LLM，支持日语和英语，并与 Hugging Face 无缝集成。

### text-to-speech
 * [Anime-Llasa-3B](https://huggingface.co/NandemoGHS/Anime-Llasa-3B) - 📥 1k / ⭐ 26 / Anime‑Llasa‑3B 是一款日本TTS模型，基于 HKUSTAudio/Llasa‑3B，增强了更多训练数据以提升表达力和稳定性，并采用 CC‑BY‑NC‑4.0 许可证。
 * [japanese-parler-tts-mini](https://huggingface.co/2121-8/japanese-parler-tts-mini) - 📥 1k / ⭐ 26 / Japanese Parler‑TTS Mini 是一款轻量级、高质量的日语 TTS 模型，经过从 parler‑tts‑mini‑v1 的微调，以提供高效的语音生成。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 2k / ⭐ 14 / Anime-XCodec2-44.1kHz-v2 将 16 kHz 的日语语音上采样至 44.1 kHz 的高保真音频，采用仅解码器的 RMS‑loss 微调，保持编码器/码本冻结并保留相同的语音令牌。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 90k / ⭐ 11 / 日本语言 BERT‑Base（12 层，768 维，12 头）使用 Unidic 基于词级加字符级分词和全词掩码在 CC‑100 及 2023 Wikipedia 上进行预训练，产生 7,027 名词表。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 81k / ⭐ 61 / Japanese BERT‑base（12层，768维隐藏层，12头，32 k词汇表）在 CC‑100 和 2023‑Jan Wikipedia 上使用全词遮蔽预训练，采用 Unidic 2.1.2 词级分词加 WordPiece，训练 200 万步。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 67k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上训练，使用 Unidic‑lite 单词级标记化配合 WordPiece 子词和全词掩码（24 层，1024 维隐藏层，16 头，32k 词表），预训练代码在 cl‑tohoku/bert‑japanese。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / 一个预训练在≈100 GB的维基百科和 OS CC‑100 数据（SentencePiece 采用 10:1 混合且带 byte‑fallback）的日文 T5‑v1.1 模型，需要微调以适用于下游任务，包含迁移学习示例代码，指出输出中的潜在偏差，并遵循 CC‑BY‑SA 4.0 许可。
 * [GPT-OSS-Swallow-20B-SFT-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-SFT-v0.1-gguf) - 📥 12k / ⭐ 1 / GPT‑OSS‑Swallow‑20B‑SFT‑v0.1‑gguf 是 tokyotech‑llm GPT‑OSS‑Swallow 20B SFT 模型的 gguf 转换版本，训练于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，并为 CUDA‑enabled llama.cpp 构建，准备通过 llama‑cli 运行（例如，专业厨师食谱提示）。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 9k / ⭐ 1 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一个顶尖的、面向日语的 GGUF 模型，使用 Unsloth Dynamic Quantization 2.0，配有广泛的日语校准和社区修复的错误，能够在 llama.cpp 上运行，即使没有 GPU，也只需至少 8 GB RAM 和 3 GB disk。
 * [GPT-OSS-Swallow-20B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-RL-v0.1-gguf) - 📥 9k / ⭐ 4 / 一个 gguf‑格式转换的 GPT‑OSS‑Swallow 20B RL v0.1 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 数据构建，已准备好通过 llama.cpp 运行并支持 CUDA。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 6k / ⭐ 4 / 一个针对日语微调的 Qwen 3.5‑9B GGUF 模型，使用 Unsloth Dynamic Quantization 2.0、广泛的错误修复、大规模日语校准，并可通过 llama.cpp 在 CPU 上使用 16 GB RAM 和 6 GB 磁盘运行。
 * [Qwen3.5-0.8B-JP-gguf](https://huggingface.co/tatsuyaaaaaaa/Qwen3.5-0.8B-JP-gguf) - 📥 5k / ⭐ 1 / 一个 gguf 转换的 Qwen3.5‑0.8B‑JP（来自 Holy‑fox），使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 数据集进行量化。
 * [GPT-OSS-Swallow-120B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-120B-RL-v0.1-gguf) - 📥 5k / ⭐ 5 / 使用TFMC/imatrix日语数据集构建的120 B GPT‑OSS‑Swallow RL 模型的 gguf-format 转换，并附带编译支持CUDA的 llama.cpp 以及通过 llama‑cli 运行该模型的说明。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 3k / ⭐ 17 / Japanese DeBERTa V3 base 在 LLM‑jp v1.0 的 540 B tokens 上预训练，使用经过修改的 DeBERTa V3 设置训练，采用 unigram byte‑fallback tokenizer（不使用形态学分析器），并针对 JGLUE NLU 任务进行微调。
 * [Qwen3-8B-JP-Uncensored-i1-GGUF](https://huggingface.co/mradermacher/Qwen3-8B-JP-Uncensored-i1-GGUF) - 📥 3k / ⭐ 1 / 提供了针对 Qwen3‑8B‑JP‑Uncensored 模型的多种加权和 imatrix GGUF 量化方式，从 2.2 GB 的 IQ1 变体到 6.8 GB 的 IQ6，并附带使用说明、静态量化链接和支持资源。
 * [GPT-OSS-Swallow-20B-RL-v0.1-MXFP4](https://huggingface.co/dahara1/GPT-OSS-Swallow-20B-RL-v0.1-MXFP4) - 📥 3k / ⭐ 2 / GPT‑OSS‑Swallow‑20B‑RL‑v0.1‑MXFP4 是一个免费、无 GPU 的 GPT‑4o‑mini 级 AI，以 gguf 文件形式发行，已针对日语进行优化，并采纳了社区发现的 bug 修复、基准推导设置，仅使用默认 MXFP4 格式（不支持动态量化或大型 imatrix）。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 3k / ⭐ 72 / Llama‑3‑ELYZA‑JP‑8B 是一款经过日本增强的 8‑B Llama 3 模型，采用 GGUF (Q4_K_M) 和 AWQ 量化，支持通过 llama.cpp、LM Studio 或 OpenAI‑compatible API 运行。
 * [SIP-jmed-llm-3-13b-OP-4k-base](https://huggingface.co/SIP-med-LLM/SIP-jmed-llm-3-13b-OP-4k-base) - 📥 3k / ⭐ 1 / SIP‑jmed‑llm‑3‑13b‑OP‑4k‑base 是一个 Apache‑2.0 许可证、领域适配的日英医学 LLM，基于 llm‑jp‑3.1‑13b 构建，由 SIP 第三期医学知识项目开发的研究原型，但不适用于临床使用。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 2k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一个拥有80亿参数的 LLM，通过在合成日语数据上持续预训练和指令微调，提升了 Meta 的 Llama 3.1 在日语语言与代码/数学推理上的表现，同时保持了英语流畅性。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 2k / ⭐ 22 / 由 imatrix 数据构建的 pfnet 的 plamo‑2‑translate 的 GGUF‑格式发布，基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带通过 llama.cpp 在启用 CUDA 的硬件上编译和运行的说明。
 * [Holy-fox-Qwen3.5-0.8B-JP-gguf](https://huggingface.co/mmnga-o/Holy-fox-Qwen3.5-0.8B-JP-gguf) - 📥 2k / ⭐ 1 / 提供了从 **TFMC/imatrix‑dataset‑for‑japanese‑LLM** 构建的 **Holy‑fox** 的 **Qwen3.5‑0.8B‑JP** 模型的 **GGUF-format** 转换，并附有编译和运行带 **CUDA** 支持的 **llama.cpp** 的说明。
 * [gemma-2-2b-it-gguf](https://huggingface.co/mmnga/gemma-2-2b-it-gguf) - 📥 2k / ⭐ 1 / 使用TFMC/imatrix‑dataset‑for‑japanese‑llm中的imatrix数据，对Google的gemma‑2‑2b‑it模型进行GGUF格式转换，并包含llama.cpp使用说明。
 * [Qwen3.5-REAP-212B-A17B-gguf](https://huggingface.co/mmnga-o/Qwen3.5-REAP-212B-A17B-gguf) - 📥 2k / ⭐ 5 / GGUF 转换后的 OpenMOSE Qwen3.5‑REAP‑212B‑A17B，已从 TFMC/imatrix 日语 LLM 数据集重新构建，准备通过 llama.cpp 标准 CLI 进行 CUDA‑支持的推理。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 2k / ⭐ 17 / 高性能的日本 SPLADE v2 通过 WebUI demo 实现稀疏向量转换和推理，使用 YAST 进行训练，提供 YASEM 嵌入，并报告 JMTEB benchmark 结果。
 * [Qwen3-Swallow-8B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-8B-SFT-v0.2-gguf) - 📥 1k / ⭐ 1 / 一个 gguf‑converted Qwen3‑Swallow‑8B‑SFT‑v0.2 模型，用于日语 LLM，使用 imatrix 数据构建，配有 llama.cpp 推理指令。
 * [llm-jp-moshi-v1](https://huggingface.co/llm-jp/llm-jp-moshi-v1) - 📥 1k / ⭐ 35 / LLM‑jp‑Moshi‑v1 是一个实验性的日语全双工语音聊天模型，基于 7‑B 参数的 Moshi 架构构建，并使用 J‑CHAT 和 Zoom 对话数据进行微调，已在 Apache 2.0 许可证下为 Linux GPU 系统发布了 web‑UI 演示。
 * [Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-30B-A3B-SFT-v0.2-gguf) - 📥 1k / ⭐ 2 / GGUF格式的 Qwen3‑Swallow‑30B‑A3B‑SFT‑v0.2 模型版本，由 tokyotech‑llm 发布，使用来自 TFMC/imatrix‑dataset‑for‑japanese‑LLM 的 imatrix 数据构建，已准备好用于 llama.cpp 的 CUDA 使用。
 * [SIP-jmed-llm-3-8x13b-OP-32k-R0.1-GGUF](https://huggingface.co/hiratagoh/SIP-jmed-llm-3-8x13b-OP-32k-R0.1-GGUF) - 📥 1k / ⭐ 3 / GGUF‑converted、quantized、research‑only 版的日本 SIP‑jmed‑llm‑3‑8x13b‑OP‑32k‑R0.1 主权医疗推理模型，由日本 SIP 计划开发，用于安全、开放的医疗 LLM，适用于研究和演示（例如在 Ollama + Dify 上），但不适用于临床决策。
 * [RakutenAI-3.0-gguf](https://huggingface.co/mmnga-o/RakutenAI-3.0-gguf) - 📥 1k / ⭐ 5 / GGUF转换版本的 RakutenAI‑3.0，基于 imatrix 数据集构建，已准备好与 llama.cpp 一起使用以运行日本 LLMs。
 * [cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf](https://huggingface.co/mmnga/cyberagent-DeepSeek-R1-Distill-Qwen-14B-Japanese-gguf) - 📥 1k / ⭐ 55 / Cyberagent’s gguf‑converted DeepSeek‑R1‑Distill‑Qwen‑14B‑Japanese model（基于 TFMC imatrix 数据集构建）在 mmnga 下可用，并可使用 llama.cpp 进行 CUDA 支持的运行。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 1k / ⭐ 3 / 一款使用日语维基百科和 mC4/ja 预训练的 T5 v1.1 模型，采用 GEGLU 激活函数，预训练期间不使用 dropout，未与嵌入层共享分类器，按 CC‑BY‑SA 4.0 许可证发布（商业用途须事先联系）。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 1k / ⭐ 2 / DataPilot-ArrowPro-7B-RobinHood‑gguf 是使用 imatrix Japanese LLM dataset 转换为 gguf 格式的 DataPilot ArrowPro‑7B‑RobinHood 模型，已准备好在 llama.cpp 进行推理。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 12 / Sarashina2.2 提供 0.5‑B、1‑B 和 3‑B 语言模型， 这些模型由 SB Intuitions 通过三阶段流水线和合成数据训练，达到了日本 QA、数学和编码的顶级成绩，同时提供的预训练权重未进行指令微调，可能产生偏见输出。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 3M / ⭐ 23 / 聚合了2009年至2024年NicoNico Live的评论日志，总计超过150 GB，包括转移前、转移后以及实时NX‑Jikkyo捕获，提供了一个API，便于检索历史电视广播讨论。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 158k / ⭐ 7 / 使用 VOICEVOX 从 ITA、Tsukuyomi‑chan 以及 ROHAN 语料库创建的人工声数据集，包含 445,793 条 WAV 文件，总计 577 小时 51 分钟 23 秒。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 17k / ⭐ 16 / 一份日语和多语种 QA、NLI 与同义句重述数据集的目录，详细说明每个数据集的检索或问答任务及其许可（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 11k / ⭐ 9 / Cauldron‑JA 是一个日语视觉‑语言数据集，包含 44 个子数据集，使用 DeepL API 从 The Cauldron 翻译而来，可通过 HuggingFace’s datasets library 获取，并与原始数据集使用相同的许可证，prompts 在 CC‑BY‑4.0 下发布。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 9k / ⭐ 109 / Nemotron‑Personas‑Japan 是一个开放源代码、CC BY 4.0 许可证的高质量、合成生成的日本人物资料数据集—包含姓名、性别、年龄、背景、婚姻状况、教育、职业和地点—基于真实世界的人口统计、地理和人格分布，并采用概率图模型和 GPT‑OSS‑120B 进行工程设计，以提升多样性、降低偏见、防止模型崩溃、支持主权 AI 发展，并支持商业使用。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 5k / ⭐ 28 / FineWeb2 Edu Japanese 提供约120 million高质量教育日语文本（≈89.3 billion tokens）来自 FineWeb2，经过 DeepSeek‑API classifier（score ≥ 2.5）过滤，通过 ModernBERT‑Ja‑130M tokenized，并包含一个小-token子集（≤512 tokens）。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 5k / ⭐ 4 / Japanese Medical VQA 12M 是一个可商业使用的多模态数据集，包含超过 1200 万张日语医学图像和标题，源自 Open‑PMC‑18M，采用 Parquet/Webdataset 格式，并包含原始和日语翻译图像、增强后的标题以及使用 InternVL3.5、Qwen3‑30B 和 GPT‑oss 120B 生成的 VQA 风格问答对。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 3k / ⭐ 110 / ReazonSpeech 是一个免费、FLAC 编码的日语语音语料库，附带转录，提供五种规模，从 8.5 h 到 35,000 h，可通过 Hugging Face 下载，遵循 CDLA‑Sharing‑1.0 许可证，且使用受到《日本著作权法》第30‑4条的限制。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 3k / ⭐ 39 / 一个用户友好、去重的 CSV 数据集，包含 Aozora Bunko 的公有域日语文本，使用 globis‑org/aozorabunko‑extractor 处理，并已清理以适用于现代日语机器学习。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 3k / ⭐ 16 / Reazon Speech v2 数据集的镜像：3,674 个已使用 UVR 在 8 台 A800 GPU 上处理 10 天的去噪音频文件，由 Stardust‑minus 提供，遵循 CDLA‑Sharing‑1.0 协议，未包含转录文本。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 3k / ⭐ 99 / 一个包含100个样本的日语指令微调评估数据集，包含已注释的任务——从摘要校正、数学推理到翻译、创意生成和用户意图理解——旨在对微调模型进行手动或自动的5分制评分。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 2k / ⭐ 5 / JAQKET 是一个基于维基百科的日语开放域问答数据集，提供 1.0 版包含多项选择测验题（13,061 条训练样本，271 条验证样本）以及 2.0 版仅包含需要提取答案的提问提示（2,154 条训练样本，1,164 条验证样本），旨在促进问答系统研究。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 2k / ⭐ 36 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小时匿名 1,033,142 对 eroge 音频-转录配对（主要为女性，含 NSFW），MIT 许可用于学术研究。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 2k / ⭐ 4 / JamC‑QA 是一个双语基准，涵盖八个日本文化与知识类别的多项选择题，排行榜指标用于比较最先进模型。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 2k / ⭐ 19 / JMMMU 是一个日语多模态基准，已扩大十倍至 1,320 个具有文化多样性的问题（720 个与文化无关，600 个与文化相关），由母语专家翻译，现在设有公开排行榜。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEB 是一个日本文本嵌入基准，包含 5 个任务（聚类、分类、STS、检索、再排序）和 28 个数据集，提供一行评估脚本，并邀请社区贡献。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 2k / ⭐ 47 / 更新了 JGLUE 数据集卡与加载脚本，适用于由 Yahoo Japan 与早稻田大学创建的日语 NLP 基准，涵盖文本分类（MARC‑ja、JCoLA）、句对分类（JNLI）以及问答（JSQuAD、JCommonsenseQA），发行链接保存在 GitHub 与 Hugging Face 上。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 1k / ⭐ 89 / 一个自动翻译的日语版本的databricks‑dolly‑15k数据集，许可为CC‑BY‑SA‑3.0，最后更新于2023‑05‑11。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 1k / ⭐ 4 / 提供了一个日语搜索/问答数据集，其中包含按查询计算的分数，这些分数是由五个多语言/日语重排序器（例如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）计算的，数据集包括每个查询约200个正例和负例文档的平均分数。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 1k / ⭐ 6 / Japanese XL‑Sum subset 通过 PaLM‑2 15-gram 重叠过滤，包含 4,215 训练样本，758 验证样本和 766 测试样本。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 978 / ⭐ 23 / cc100-ja 是 cc100 数据集日语部分的集合，提供为分片的 Parquet 文件。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 919 / ⭐ 7 / JMedBench 是一个日语生物医学 LLM 基准，涵盖 20 个数据集，覆盖五个任务（MCQA、NER、STS 等），来源于 MedMCQA、PubMedQA、MMLU 等，每个都有自己的许可，并包含一条说明：翻译可能包含偏差，需要人工审核。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 918 / ⭐ 133 / Japanese Anime Speech Dataset V2 提供 292,637 条已清洗的音频-文本对——约 397.5 小时的 SFW 内容和 52.4 小时的 NSFW 内容——以 128‑kbps MP3 文件形式按安全级别划分，专为训练自动语音识别模型而设计。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 827 / ⭐ 2 / 日文维基百科文本改写所生成的LLM查询和答案数据集，未使用受许可限制的模型构建，且在CC‑BY‑SA 4.0下发布。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 798 / ⭐ 2 / 包含匿名 2ch.sc/2ch.net 帖子的极大压缩 JSON‑Lines 数据集，包括帖子 IDs、标题、板块与地区信息、回复计数，以及完整帖子元数据（作者、邮件、日期、内容）。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 787 / ⭐ 32 / 一个时长为409小时的日本 eroge 语音数据集，使用 2-pass loudnorm（‑23 LUFS，‑1 dB 峰值，11 LRA）处理，已由 litagin/anime-whisper 转录、匿名化，存储为 WebDataset（FLAC、JSON、TXT），主要包含女性声音，可能存在 AI 转录错误，并采用 MIT 许可证用于学术研究。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 731 / ⭐ 11 / JMMLU 是一个日语大型多任务语言理解基准（Benchmark），包括 7,536 道教师精心制作的问题，覆盖 56 个学科，包括专业医学、心理学、会计、哲学以及各种高中学科。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 706 / ⭐ 148 / 日本动漫语音数据集提供73,004对音频-文本（总计110小时，已从V1升级至V5），用于提升ASR模型，例如OpenAI的Whisper，按开放许可证提供给所有使用，欢迎署名。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 690 / ⭐ 4 / 来自 Fate/Stay Night 的角色 “Emilia” 的对话和背景故事数据集，格式化用于训练和评估会话语言模型。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 681 / ⭐ 8 / Rakuda 提供 40 道日语问题——开放式的历史、社会与政府问题，以及针对地理的特定问题——用于对日本 AI 助手进行基准测试，类似于 vicuna‑eval，并且可以使用 `datasets.load_dataset` 加载。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 665 / ⭐ 32 / 为高效加载 Hugging Face datasets，重新结构化并重新上传 Galgame VisualNovel 数据集（OOPPEENN/5669737465666C656E63655F44617461337072657330），保留所有原始 audio/text，并提供带多种 game-subset 选项的 extraction script。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 592 / ⭐ 12 / EDINET‑Bench 是一个日本金融基准，用来评估 LLMs 在诸如会计欺诈检测、盈利预测和行业预测等任务，使用十年的 EDINET‑API 披露报告，提供构建和评估代码，并将数据集重新许可为 PDL 1.0。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 563 / ⭐ 33 / Syosetu711K 是一个约 711,700 本小说的日本数据集，采自 2023 年 3 月 26‑27 日从 小説家になろう 抓取，提供全文及元数据（标题、作者、NCode、简介等），用于无监督文本生成和分类任务。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 553 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 数据集的 500 份样本子集，采用 CC BY 4.0 许可，用于基准测试 EvoVLM‑JP‑v1‑7B。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 549 / ⭐ 6 / 日本 MC4 数据集卡 (mc4-ja)
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 545 / ⭐ 44 / Galgame_Speech_ASR_16kHz 是一个 16 kHz 的 ASR 数据集，包含 3.75 百万对（≈5,354 小时），源自 Galgame_Dataset，遵循 GPL v3.0，禁止商业使用，并要求任何训练的模型必须开源（可选引证）。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 536 / ⭐ 141 / 用于微调 LLMs（如 LoRA）的日语指令聊天数据集，包含 9 M+ 样本，最近已更新，删除授权的 Alpaca 数据，并清理了 Wikipedia 和 ALT 输出，采用 CC‑BY‑SA 4.0 许可证发布。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 474 / ⭐ 22 / 一套来自日本网络的5600万份文档、110 B字符与2.49亿张图片，用于训练大型视觉语言模型——提供momiji_generator用于数据填充，OBELICS‑style可视化，以及示例模型（Heron‑NVILA‑Lite）。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 439 / ⭐ 3 / Japanese Guardrail model evaluation dataset (1,725 samples)，是 WildGuardTest 的高质量、多阶段翻译，采用 ODC‑BY 许可发布，并可在 Hugging Face 获取。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 418 / ⭐ 5 / Japanese JaQuAD，QG‑Bench 的一个子集，提供句子级和段落级的数据，包含高亮的答案词元，用于训练日语问句生成模型，并通过 BLEU4、METEOR、ROUGE‑L、BERTScore 和 MoverScore 进行评估。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 404 / ⭐ 10 / 一份将 llm‑jp‑corpus‑v3 的 kaken 子集译为日英的日英平行语料库，使用 Qwen/Qwen2.5‑32B‑Instruct，包含自定义翻译列，并在 CC‑BY‑4.0 许可下授权。
 * [jhle](https://huggingface.co/datasets/llm-jp/jhle) - 📥 396 / ⭐ 96 / 由 LLM‑jp 策划的日本翻译版 Humanity’s Last Exam 数据集，省略图像问题，每个 raw_subject 采样五条，已机器翻译并由专家审核，作者为 Yuji Tamakoshi、Kouta Nakayama 和 Yusuke Miyao，并且绝不应用于训练语料库。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 388 / ⭐ 6 / 将日语数据集转换为适合 SentenceTransformers 的列，依据来自多个 HuggingFace 来源的 Rerank 分数（正样本 ≥0.7，负样本 ≤0.3）进行过滤，以支持对比学习，同时尊重原始许可证。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 378 / ⭐ 5 / STAIR‑Captions，发布于2017年，提供820,310条日语字幕，用于字幕生成、多模态检索和图像生成，并配有详细注释、元数据以及Creative Commons BY‑4.0 license。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 361 / ⭐ 11 / JDocQA 是一个基于日文 PDF 的问答数据集，包含 5,504 篇文档和 11,600 对问答，使用视觉和文本信息测试是/否、事实性、数值、开放式和不可回答的理解。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 340 / ⭐ 27 / WRIME 数据集是一个包含 42,200 条帖子的日本语集合，帖子已为作者、三位读者及其平均值标注了 Plutchik 的八种情感，结构为 40k 训练集、1.2k 验证集和 2k 测试集，用于情感分析任务。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 340 / ⭐ 16 / Japanese Alpaca 数据，源自 masa3141 的 Japanese Alpaca‑LoRA 工作，并引用原始仓库以获取更多细节。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 338 / ⭐ 2 / 将日本 Callhome 语音文件转换为 WAV，并附带 JSON 格式的元数据数组和 RTMM 说话人标签文件以供评估。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 323 / ⭐ 13 / ‘wikipedia-ja-20230720’ 日本维基百科快照的数据集卡。
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 322 / ⭐ 6 / 已去重、NFKC‑标准化的 mQA query–passage pairs，pos_ids/neg_ids 映射到 collection 索引，用于通过 collection[pos_id] 直接检索，并按原始数据集的许可条款授权。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 319 / ⭐ 3 / 包含问题、答案以及逐步推导链接至 Wikipedia 文章的日本 Explainable Multi-hop Question Answering 数据集，已更新推导格式并发布多个版本。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 318 / ⭐ 18 / 包含草薙寧々（来源 CV Machico）的 *Project Sekai* 歌声轨的部分数据集，附带 nene_org.txt 标注文件，计划扩充并标准化数据，并呼吁用户点星此 repo、分享想法、加入 QQ 群以获取完整收藏。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 306 / ⭐ 21 / AI生成的动漫插图，使用英文提示，并基于Phi‑3 Vision的字幕（英文和日文），已发布到公共领域，供免费使用。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 293 / ⭐ 3 / BBH‑ja提供了BIG‑Bench Hard数据集的日语翻译，提供JSON‑L（输入、正确目标）格式的评估问题以及使用PLaMo模型翻译的YAML（输入、目标）格式的Chain‑of‑Thought提示。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 283 / ⭐ 3 / 已清理的日语网络语料库（mc4‑ja 等）通过无监督学习聚类成约10k 文本，仅部分文件为 Parquet；文件列表在 out 文件夹中，可使用 Git LFS 下载，用于合法可行的信息分析用途。
 * [LLMChat](https://huggingface.co/datasets/team-hatakeyama-phase2/LLMChat) - 📥 279 / ⭐ 4 / 来自LLMChat系统的2,139个人工评分问答对的数据仓库，在此系统中，每个用户问题都收到来自13个参与模型的两条随机回答，评审员选择更好的回复（1 = 第一条，2 = 第二条，0 = 两条都差，3 = 两条都好），条目包括问题、两条答案、评估、可选的更正答案、模型名称、时间戳，文本采用CC0许可，输出遵循模型特定的许可证。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 269 / ⭐ 7 / JHumanEval 是 HumanEval 基准的人工翻译日语版本，提供 164 个 Python 编程问题，配有并行的英文和日文注释，用于评估日语 LLM 的代码生成，同时保留原始英文错误。
 * [dataset-for-annotation-v2-annotated](https://huggingface.co/datasets/preference-team/dataset-for-annotation-v2-annotated) - 📥 260 / ⭐ 3 / 一份由日语母语者注释的合成问答配对数据集，标注了首选与强度（-3 到 3），涵盖多种体裁，展示了有限的变化、常见的 LLM 句型、缺失的真实场景，以及深入专业知识的机会。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 259 / ⭐ 9 / 面向 llm‑book/wrime‑sentiment 的数据集卡，提供从 WRIME 派生的二元日语情感分析集，依据 Avg. Readers_Sentiment 标记为正向或负向（可选包含中性案例），用于《大型语言模型导论》一书的示例数据。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 258 / ⭐ 2 / JCommonsenseQA 是一份日语的多项选择常识推理数据集——CommonsenseQA 的改编版本——其授权为 CC BY‑SA 4.0，并以 doi:10.5715/jnlp.30.63 引用。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 249 / ⭐ 15 / Hachi‑Alpaca 提供基于 Stanford Alpaca 的日语合成数据，经过 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 细化和验证，并通过 Deepinfra 使用，同时提供已通过模型质量检查的 “_cleaned” 版本。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 248 / ⭐ 3 / 日语维基百科句子被转换为各种嵌入和 FAISS 索引，提供 Hugging Face Space 演示、转换脚本，以及对搜索、问答和 OpenAI text-embedding-3-small 在 RAG 中的评估；嵌入模型为 OpenAI‑licensed，其他为 CC‑BY‑SA‑4.0。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 245 / ⭐ 14 / 180 万条日语翻译条目，来源于 OpenMathInstruct‑1，并由 GSM8K 与 MATH benchmark 问题组成，配合已验证的 Mixtral‑8x7B 生成的合成解答，已在 NVIDIA 的许可下商业提供。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 234 / ⭐ 5 / JSNLI 是 Kurohashi‑Chu‑Murawaki Lab 发布的 SNLI 自然语言推断基准的日语翻译版本，采用 TSV 格式提供，前提与假设均使用 JUMAN++ 进行分词，提供约 533,000 对和 548,000 对的过滤与非过滤训练集，并包含 3,916 对验证集，采用 CC BY‑SA 4.0 许可证。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 233 / ⭐ 15 / 一个用于测试角色‑LLMs的简单 Zundamon 角色设定数据集——由线上来源和管理数据编制——以 zmnjp.jsonl 和 zmn.jsonl 格式提供，并在指定许可下发布。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 233 / ⭐ 2 / Hugging Face 镜像的 ABEJA‑CC‑JA dataset 来自 AWS Open Data registry，细节见 ABEJA 的 tech‑blog entry。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 232 / ⭐ 11 / JaQuAD 是 2022 年的日语 QA 数据集，包含 39,696 对 SQuAD‑style 的抽取式问题‑答案对，取自 Wikipedia，文件总大小 73.2 MB。使用 BERT‑Japanese 微调时，获得 78.92 % F1（63.38 % EM）。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 215 / ⭐ 3 / A 2010 Japanese Web Corpus, uploaded to HuggingFace and licensed for research per the 2009 copyright reform, 包含来自基于形态学的解析和转换脚本的自动标点化文本。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 214 / ⭐ 6 / Range3 的 wikipedia‑ja‑20230101 仓库提供只包含日语维基百科文本的 Parquet 文件，这些文件是从完整维基百科数据集中提取的，并使用 Python 代码生成。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 214 / ⭐ 80 / 句式对齐的日文网络小说章节以及英文粉丝翻译 (106 K+ 条目，version 2) 旨在用于翻译研究，已更新对齐、添加系列元数据、无质量筛选，并按 fair‑use 与 Apache 2.0 分发，并可通过 Hugging Face 接受下架请求。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 206 / ⭐ 51 / AnswerCarefully Dataset提供日语和多语种数据，用于商业或非商业LLM安全增强，禁止任何其他用途——包括安全规避——允许带署名的衍生作品，并声明不承担因伤害或服务变更导致的责任。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 203 / ⭐ 9 / JSICK 是从 SICK 翻译成日语的 NLI/STS 数据集，提供了一套压力测试，利用多个转换过的 sentence-pair subsets 来探测 word‑order 和 case‑particle 的处理，以支持多语言组合推理的研究。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 202 / ⭐ 6 / 数据集卡片“oscar2301‑ja‑filter‑ja‑normal”，目前缺少详细信息。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 201 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) 提供了一个多分类 QA 数据集——涵盖 Integration、Reasoning、Logical、Table 和 Abstention——旨在评估日本 RAG 生成器，采用人工努力和 GPT‑4.1 构建，并在 CC BY‑SA 4.0 许可下发布。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 200 / ⭐ 16 / 一个 1.9 亿对 JSONL 数据集，用于日语假名到汉字转换，为 zenz‑v2.5 medium、small 和 xsmall 模型提供动力，并包含 AJIMEE‑Bench 评估语料库。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 198 / ⭐ 11 / Range3/wiki40b‑ja 托管了 wiki40b 数据集的日语子集，作为由 Python 数据处理管道生成的三个 Parquet 文件。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 197 / ⭐ 8 / JMMMU‑Pro 是一个通过 Vibe Construction 构建的日语多模态基准——结合生成建模和人工验证——用于生成低成本、高质量的 image‑QA 数据，以揭示开源 LMMs 的缺陷并引领未来 VQA 研究。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 185 / ⭐ 4 / JFWIR 是一份从 fine‑web 教育爬虫构建的 6400 万对日语信息检索数据集，提供每个文档七种查询类型、难负样本，并在基准测试中明显优于以往基线。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 185 / ⭐ 2 / 一个开放的 CC‑BY‑4.0 日本证券表格数据集，提供图像、带边界框的 OCR 文本，以及直接单元格值问答，用于多模态视觉语言模型训练，基于 NTCIR‑U4 和 EDINET。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 184 / ⭐ 16 / Galgame_Speech_SER_16kHz 是一份 3.7 百万文件（5,353 小时，104 GB）的情感语音数据集，源自 Galgame_Speech_ASR_16kHz，由本地 LLM 注释，按 GNU GPL v3.0 发行，禁止商业使用，并要求基于它训练的模型保持开源且无需强制引用。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 182 / ⭐ 15 / 用于《大型语言模型简介》一书的 JGLUE 数据集数据卡，来源于原始仓库，代码采用 CC BY‑SA 4.0 许可证，数据按发行者的许可协议，引用 Kurihara & Kawahara（日本语），并基于 Shunsuke Kitada 的仓库构建。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 182 / ⭐ 18 / Databricks‑dolly‑15k‑ja 数据集是 DeepL 翻译的日本语版 databricks‑dolly‑15k，用于指令调优，由日本 LLM‑jp 项目创建，并由 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 和 Takumi Okamoto 撰写。
 * [relaion2B-en-research-safe-japanese-translation](https://huggingface.co/datasets/llm-jp/relaion2B-en-research-safe-japanese-translation) - 📥 176 / ⭐ 4 / 一个快速的英日翻译流水线，使用 text2dataset、Gemma‑2‑9b‑it 和 vLLM 构建，能够通过简洁的开源加权 LLM 提示，将大型 relaion2B‑en‑research‑safe 语料库转换。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 175 / ⭐ 12 / LLM‑jp 提供了一个日语指令调优数据集，该数据集是 DeepL 翻译自 oasst2 的英文子集（来自 kunishou/oasst2‑135k‑ja），并由 Kiyomaru 和 Kodama 编译。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 168 / ⭐ 5 / J‑HARD‑TTS‑Eval 对日语自回归 TTS 模型在短序列稳定性、重复、韵律和连贯性等失败方面进行基准测试，提供带有提示音频和文本的数据集，可通过 Hugging Face 加载。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 167 / ⭐ 16 / oasst1‑21k‑ja 是由 DeepL 从英文 OASST1 子集派生的日语指令调优数据集，透过日本 LLM‑jp 合作项目创建；请联系 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 和 Okamoto。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 160 / ⭐ 10 / 一个高质量的合成日语数学题数据集，具有经过验证的思考链推理，采用 Qwen2‑7B‑Instruct 翻译 PRM800K 和 GSM8K 并进行正确性筛选后构建，可通过 Hugging Face 数据集库获取。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 157 / ⭐ 33 / Allganize RAG Leaderboard 发布了跨五个行业领域——金融、电信、制造业、公共部门和零售业的日本 RAG 性能数据和自动端到端评估结果，帮助公司在没有完整日本基准的情况下基准化解析器、检索和生成组件。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 155 / ⭐ 24 / AutoWikiQA 是日本最大的免费问答数据集（2,377,503 对），该数据集是从维基百科文本使用 Swallow‑MX 和 vLLM 生成的，提供多样化、无模板的问答，用于知识注入和检索增强生成。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 145 / ⭐ 26 / 带有失败标记的日语翻译 OpenAssistant/oasst1 数据，约2,000个人工纠正的代码翻译错误，一个已发布的对话格式子集 (oasst1‑chat‑44k‑ja)，以及一段用于将条目转换为指令‑输出对以进行微调的脚本。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 141 / ⭐ 19 / 一个用于评估 Retrieval‑Augmented Generation（RAG）的日语 QA 数据集，由 JAQKET 问题和 Wikipedia 段落以及金标准检索相关性标签构建，并在 HuggingFace 和 GitHub 上发布，主要依据 nDCG@10 评分。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 141 / ⭐ 3 / 本数据集说明书用于本书《Introduction to Large‑Scale LLM II》中的 ja‑vicuna‑qa‑benchmark，并由 llm‑jp‑eval 创建，供跨数据集日语 LLM 评估使用（Apache 2.0）。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 136 / ⭐ 10 / JA‑Multi‑Image‑VQA 是一个包含 39 张图像、55 道题目的数据集，其中包含手工制作的日语问答，适用于多图像 VQA，通过 load_dataset 访问，文本部分采用 Apache 2.0 许可（图像受限）。
 * [jawiki-bullet-points](https://huggingface.co/datasets/hpprc/jawiki-bullet-points) - 📥 136 / ⭐ 4 / 一个使用 CC‑BY‑SA‑4.0 许可的日文维基百科文本数据集，被 Apache‑2.0 许可的 DeepSeek R1 Distill Qwen 32B 模型转换成项目符号列表，采用允许重复的随机采样生成——但换行符可能在 Hugging Face 上不总是清晰显示。
 * [nagisa_stopwords](https://huggingface.co/datasets/taishi-i/nagisa_stopwords) - 📥 130 / ⭐ 2 / 一个包含147个单词的日语停用词列表，来源于 CC‑100 Wikipedia，采用 MIT 许可证，已内置于 nagisa tokenizer 的 nagisa.stopwords，方便使用。
 * [EliteVoiceProject](https://huggingface.co/datasets/Elite35P-Server/EliteVoiceProject) - 📥 119 / ⭐ 12 / Elite Voice Project 组装 Sakura Miko 语音录音成一个符合 Hololive 标准的数据集，用于语音识别研究，并邀请合作伙伴通过结构化的 `audio_raw` 文件夹（twitch, twitter, youtube）在 train/test 分区下添加新的片段，同时遵守 Hololive 的衍生作品指南。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 119 / ⭐ 2 / WAON 是一个大规模、高质量的日语图像–文本配对数据集，面向视觉语言模型，该数据集通过基于大小和 SigLIP-Score 的筛选以及在 URL、标题和感知哈希上的去重构建，采用 Apache 2.0 许可证，使用仅限于根据日本法律进行信息分析。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 118 / ⭐ 4 / 数据集卡片：关于由 Loonwit 提供、用于书《Introduction to Large Language Models》的 livedoor 新闻语料库，包含已去除 HTML 标签的 Creative Commons 许可新闻文章（CC BY‑ND 2.1 JP）。
 * [JetCopper-10B](https://huggingface.co/datasets/sudy-super/JetCopper-10B) - 📥 115 / ⭐ 5 / JetCopper‑10B 是一个日英数据集，包含 47 亿条日语 token 与 9 亿条英語‑代码 token，来源于 CC‑100、OSCAR‑2301、HPLT v1.2 和 wiki40b‑ja 的清理子集，用于预训练 Contrail‑200m‑64k 以支持 LOCAL AI HACKATHON #000，但它尚未经过句子边界或困惑度过滤。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 112 / ⭐ 2 / 提供一个 Japanese Common Voice 17.0 子集，包含 649 位说话人（每人 30–300 条样本），共 45,668 条发声记录，按说话人按 80/20 分割，批量存入 1,000 条样本的 Parquet 文件，全部采用 CC0 许可。
 * [oasst1-chat-44k-ja](https://huggingface.co/datasets/kunishou/oasst1-chat-44k-ja) - 📥 111 / ⭐ 10 / 一个基于 ShareGPT 格式的多轮聊天数据集，来源于 oasst1‑89k‑ja，用于微调，需大量计算资源；请参阅随附的文章和 GitHub/HuggingFace 链接。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 110 / ⭐ 11 / Japanese Roleplay Dialogues 数据集已被过滤，去除发帖者 ≤1 或帖子 ≤10 的记录，标准化并匿名化发帖者名称，仅保留前两位发帖者占帖子总数 ≥90% 且每人至少占 40% 的对话，以供机器学习应用。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 107 / ⭐ 7 / Livedoor News Corpus 提供了一个日语新闻文章数据集，划分为 5,894 条训练样本、737 条验证样本和 736 条测试样本，已清除 HTML 标签，并在 Creative Commons Attribution‑NoDerivs 许可证下发布。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 107 / ⭐ 2 / 一份包含 64,139 条标注有生物性别的日语姓名的数据集，呈现为汉字、假名和平罗马字，其 44.9k 训练集、6.41k 验证集和 12.8k 测试集划分已在 ISDA’23 被接受。
 * [japanese-stackexchange](https://huggingface.co/datasets/p1atdev/japanese-stackexchange) - 📥 106 / ⭐ 3 / 一个英文的 Japanese Stack Exchange QA 数据集，已从该站点的转储中提取并处理，提供默认和扁平化子集，可通过 Hugging Face datasets 加载，并遵循 CC BY‑SA 4.0 许可证。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 106 / ⭐ 41 / VNTL 排行榜通过在256个样本上平均余弦相似度分数，评估大型语言模型将日语视觉小说翻译成英语的能力，随后对初步结果进行排名，并与 Sugoi Translator、Google Translate 和 Naver Papago 等工具进行基准比较。
 * [Swallow-Instruct-v0.1](https://huggingface.co/datasets/tokyotech-llm/Swallow-Instruct-v0.1) - 📥 105 / ⭐ 11 / Swallow Instruct v0.1 数据集——从 OpenAssistant2 及其日语译版中抽取的 26,479 条对话，采用特定采样设置构建——用于微调 Swallow v0.1 Llama‑3 与 OpenAI GPT 模型（8B‑70B），由东京工业大学、YOKOTA Laboratory 与 AIST 的研究人员制作。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 103 / ⭐ 29 / 一个 CC‑BY‑4.0 许可的、手工提取的日本政府 FAQ 问答对（包含源 URL）的数据集，旨在用于指令调优和 RAG 测试，因其高质量而受到赞誉，但也被指出偶尔存在格式错误和强烈的官方政策语言。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 101 / ⭐ 13 / 一个采用 CC‑BY‑SA 3.0 许可的日语命名实体抽取数据集，来源于 Wikipedia，托管在 https://github.com/stockmarkteam/ner-wikipedia-dataset/，由 Stockmark Inc. 开发。
