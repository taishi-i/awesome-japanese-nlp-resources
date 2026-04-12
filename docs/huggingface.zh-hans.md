# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专门收录日语NLP相关的Python库、LLM、词典和语料库资源的精选列表。
本页面列出了Hugging Face上可用的日语NLP专用模型和数据集。目前包含197个模型和100个数据集。

_更新于2026年4月12日_

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
   * [image-text-to-text](#image-text-to-text)
   * [text-to-speech](#text-to-speech)
   * [audio-to-audio](#audio-to-audio)
   * [others](#others)
 * [Datasets](#Datasets)

## Ranking

### Models-ranking

| # | 模型名称 | Downloads | Likes | 类别 |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 3M | ⭐ 54 | automatic-speech-recognition |
| 2 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 1M | ⭐ 13 | translation |
| 3 | [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) | 📥 495k | ⭐ 5 | text-ranking |
| 4 | [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) | 📥 494k | ⭐ 132 | text-generation |
| 5 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 374k | ⭐ 69 | sentence-similarity |
| 6 | [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) | 📥 361k | ⭐ 12 | sentence-similarity |
| 7 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 360k | ⭐ 169 | image-to-text |
| 8 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 301k | ⭐ 76 | fill-mask |
| 9 | [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) | 📥 247k | ⭐ 9 | fill-mask |
| 10 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 242k | ⭐ 8 | sentence-similarity |
| 11 | [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 📥 214k | ⭐ 20 | text-generation |
| 12 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 212k | ⭐ 41 | fill-mask |
| 13 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 139k | ⭐ 15 | text-generation |
| 14 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 105k | ⭐ 58 | text-generation |
| 15 | [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) | 📥 105k | ⭐ 8 | fill-mask |
| 16 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 104k | ⭐ 11 | others |
| 17 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 77k | ⭐ 8 | translation |
| 18 | [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) | 📥 68k | ⭐ 3 | text-classification |
| 19 | [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) | 📥 65k | ⭐ 6 | image-to-text |
| 20 | [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) | 📥 64k | ⭐ 14 | others |

### Datasets-ranking

| # | 数据集名称 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 1M | ⭐ 32 |
| 2 | [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) | 📥 61k | ⭐ 7 |
| 3 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 9k | ⭐ 16 |
| 4 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 6k | ⭐ 9 |
| 5 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 6k | ⭐ 6 |
| 6 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 5k | ⭐ 112 |
| 7 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 4k | ⭐ 28 |
| 8 | [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) | 📥 3k | ⭐ 19 |
| 9 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 2k | ⭐ 99 |
| 10 | [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) | 📥 2k | ⭐ 111 |
| 11 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 2k | ⭐ 18 |
| 12 | [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) | 📥 2k | ⭐ 5 |
| 13 | [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) | 📥 1k | ⭐ 10 |
| 14 | [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) | 📥 1k | ⭐ 33 |
| 15 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 1k | ⭐ 7 |
| 16 | [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) | 📥 1k | ⭐ 4 |
| 17 | [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) | 📥 1k | ⭐ 36 |
| 18 | [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) | 📥 1k | ⭐ 89 |
| 19 | [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) | 📥 995 | ⭐ 47 |
| 20 | [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) | 📥 966 | ⭐ 3 |

## Models
### text-generation
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 494k / ⭐ 132 / 9亿参数的日语优化LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，训练数据截至2024年9月，采用混合 Mamba‑2/MLP/4‑层注意力架构，已在 Nemotron‑Personas‑Japan 工具调用数据集上微调，可选地在生成最终答案前生成可控的推理轨迹，且可商用。
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 214k / ⭐ 20 / OpenCALM 是 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 许可证下发布的一套仅解码的日本 transformer 语言模型（160 M–6.8 B 参数），训练于 Japanese Wikipedia 和 Common Crawl，并可通过 Hugging Face’s torch‑transformers 使用。
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 139k / ⭐ 15 / 一个 12 层、768 隐藏层的日语 GPT‑NeoX 模型，训练数据为 CC‑100、C4 以及 Wikipedia，兼容 Huggingface，并配备可选的玩具前缀调优权重，能强制每个句子末尾以笑脸表情符号结束。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 105k / ⭐ 58 / 一款由 ABEJA Inc. 使用日语 CC‑100 和 OSCAR 训练的 2.7B 参数日语 GPT‑NeoX 模型，可通过 Hugging Face Transformers 管道或 PyTorch 使用，按 MIT 许可证发布。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 35k / ⭐ 29 / LFM2.5‑1.2B‑JP 是一个 1.2 B 参数的日语文本生成模型，基于 LFM2.5 混合架构构建，优化用于生成和完成任务，托管在 Hugging Face 上，并可通过 llama.cpp 运行。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 25k / ⭐ 18 / 使用 Shisa 7B 数据，微调了日语 Stable LM Base Gamma 7B，在 JA MT‑Bench 上取得了强劲的表现。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 18k / ⭐ 26 / 提供来自 NII 的 8 B 参数 LLM‑jp‑4‑8b‑thinking 日语语言模型，使用 pre‑/mid‑training 训练并通过 SFT/DPO 对齐，已准备好与 torch‑transformers 一起使用，并附有详细的教程说明。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 16k / ⭐ 147 / Llama‑3‑ELYZA‑JP‑8B 是由 ELYZA 开发的、经过日语增强的 80 亿参数 Llama 3 模型，在 Meta‑Llama‑3‑8B‑Instruct 上针对日语微调。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 16k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一个 13‑B 的、基于指令预训练的日语语言模型，由 NII 的研发中心开发，并以 Hugging‑Face Transformers 检查点的形式发布，使用 UNIGRAM‑byte‑fallback 分词器。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 15k / ⭐ 5 / LLM‑jp‑3‑150m——来自国立信息学研究所LLM研发中心的150 M参数日语语言模型——以 Hugging Face Transformers 格式发布，需要 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，并且在日本维基百科、Common Crawl、WARP/PDF、WARP/HTML 和 Kaken 数据上使用 unigram byte‑fallback tokenizer 进行预训练。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 14k / ⭐ 20 / 提供 1.8 B 参数 llm‑jp‑3.1‑1.8b‑instruct4 日本指令微调模型，来自 NII，兼容 Hugging Face Transformers 和 Torch ≥ 2.3.0，包括预训练和微调检查点以及使用示例.
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 10k / ⭐ 10 / 仓库提供 GGUF 格式、量化的模型文件，适用于 Stability AI 的日本版 StableLM Instruct Gamma 7B，由 Massed Compute 硬件创建，并且是 TheBloke 的 a16z‑资助 LLM 工作的一部分。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 10k / ⭐ 21 / Llama3 Swallow 是 Meta Llama 3 系列的日语增强版本，于 2024 年 7 月 1 日发布，提供 8B 与 70B 版本的 Instruct 与 chat 模式，已在 Megatron‑LM 上使用 SFT 与 Chat Vector 进行微调，并在关键的日语 NLP 任务上进行了基准测试。
 * [llm-jp-3-1.8b-instruct](https://huggingface.co/llm-jp/llm-jp-3-1.8b-instruct) - 📥 8k / ⭐ 25 / 与 Hugging Face 兼容的日语中心 transformer 模型（llm‑jp‑3‑1.8b、1.8b‑instruct、3.7b、3.7b‑instruct、13b、13b‑instruct、17.2b‑beta1、17.2b‑beta1‑instruct）来自国立信息学研究所，在包含 Wikipedia、Common Crawl、WARP、Kaken、Dolma 在内的多种日语和英语语料库上预训练，并要求 torch ≥ 2.3、transformers ≥ 4.40、accelerate 与 flash‑attn。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 实验性日语模型通过使用聊天向量方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 与 Meta‑Llama‑3‑8B‑Instruct 之间的差异创建，然后上采样并应用于 Meta‑Llama‑3‑70B‑Instruct，显示出变化不大，并计划未来扩大规模。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 6k / ⭐ 26 / rinna 的日语 GPT‑2 small 是一个 12 层、768 维隐藏层的 Transformer，训练于日语 CC‑100 和 Wikipedia，使用 SentencePiece 进行分词，发布于 2021 年 8 月 25 日，遵循 MIT 协议（Hugging Face: rinna/japanese‑gpt2‑small，参见 https://arxiv.org/abs/2404.01657）。
 * [Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.5-35B-A3B-heretic-v2-ja-imatrix-GGUF) - 📥 6k / ⭐ 2 / 针对 Qwen3.5‑35B‑A3B‑heretic‑v2 模型的 Japanese‑calibrated importance‑matrix GGUF quantizations（IQ3/IQ4），旨在保持日语生成质量的同时显著降低安全过滤器，已在用户责任免责声明下发布。
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 6k / ⭐ 21 / 32亿参数的日语 Transformer LLM（llm‑jp‑4‑32b‑a3b‑thinking）来自国立信息学研究所，预训练和校准通过有监督微调和直接偏好优化完成——不使用强化学习——使用unigram byte‑fallback tokenizer。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 6k / ⭐ 18 / Llama 3.1 Swallow 是一组 8‑B 和 70‑B 模型，它们继续对 Meta 的 Llama 3.1 进行预训练，以提升日语语言性能，然后在合成日语数据上进行指令微调，提供多种已发布的变体，其对话行为已改进，与 gemma‑3‑27b‑it 相当。
 * [shisa-v2.1-qwen3-8b](https://huggingface.co/shisa-ai/shisa-v2.1-qwen3-8b) - 📥 6k / ⭐ 8 / Shisa V2.1 引入了升级版双语日英聊天模型——基于全新数据集，增强了指令、翻译和礼貌细调——在 Llama 3.2、Qwen 3‑8B 和 UnPhi‑4 14B 等变体中，显著提升了性能。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 5k / ⭐ 20 / OpenCALM 是 CyberAgent 开发的日本解码器（decoder‑only）Transformers 语言模型系列（160 M–6.8 B 参数），基于日本维基百科和 Common Crawl 训练，并以 CC BY‑SA 4.0 许可证发布。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 5k / ⭐ 9 / Qwen3‑Swallow v0.2 提供了通过 CPT、SFT 和 RLVR 训练的日英 LLM（30B‑A3B 和 32B），保持了强大的数学、编码和推理能力，已发布九个模型以及 AWQ 量化版本。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 5k / ⭐ 24 / Llama 3.1 Swallow 是一系列日语增强的 8B/70B Llama 3.1 模型，通过持续预训练和日语特定指令微调训练，最新的 8B‑Instruct‑v0.3 在日语 MT‑Bench 上取得了最先进的结果。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 5k / ⭐ 107 / 一款 1.3‑B‑parameter、24‑layer transformer GPT‑1B，使用 Japanese C4、CC‑100 和 Wikipedia 进行训练，于 2022 年 1 月 26 日由 rinna Co. 发布，并在 MIT license 下公开。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 5k / ⭐ 85 / Rinna 的 24 层、1024 隐藏单元的日语 GPT‑2‑medium 模型，基于 CC‑100 和维基百科训练，采用 SentencePiece 分词，已在 rinna/japanese‑pretrained‑models 仓库公开（MIT 许可证，2021 年 4 月 7 日发布，2021 年 8 月 25 日更新）。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 5k / ⭐ 16 / 一个6层、512隐藏单元的Transformer，称为Japanese GPT‑2 xSmall，在Japanese CC‑100和Wikipedia上使用SentencePiece分词训练，于2021年8月25日以MIT许可发布，并托管在Hugging Face（rinna/japanese‑gpt2‑xsmall）上，在arXiv 2404.01657中被引用。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 5k / ⭐ 7 / 预训练的 TinyLlama 在日语（≈50 k 步），基于约3 B OSCAR/mC4 tokens，可通过 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 和 Renju Aoki 创建。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 4k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 与 Swallow Team 开发的紧凑型日语指令遵循语言模型，采用 Qwen2.5‑32B‑Instruct 的 TAID 蒸馏，并在日语文本上进一步预训练，且仅以 Apache 2.0 许可证供研究使用。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 4k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27 B 参数扩展版，已在包含 instruct 和 fast 变体的日语数据上预训练，可通过 Hugging Face Transformers 使用。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 3k / ⭐ 36 / 提供了一款来自 SB Intuitions 的自回归式日语语言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已与其他模型进行基准测试，并附示例使用脚本，且安全训练有限。
 * [Qwen3-Swallow-8B-CPT-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-CPT-v0.2) - 📥 3k / ⭐ 1 / 双语 30 B‑和 32 B‑参数 LLMs，Qwen3‑Swallow v0.2，采用 CPT、SFT 和 RLVR 构建，擅长日语、日英翻译、数学和编码，匹配或超越 Qwen3，并以 AWQ‑量化形式在 Hugging Face 上发布。
 * [japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - 📥 3k / ⭐ 74 / 一个 3.6‑B‑parameter 的日本 GPT‑NeoX 模型——36 层、2816 维隐藏层 transformer——采用 PPO‑based RLHF 在翻译后的 Anthropic 数据上训练，遵循指令式对话，表现出约 30 % 的人类对位和 34 % 的 ChatGPT‑based PPO 胜率超过 SFT，但倾向于生成重复文本。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 3k / ⭐ 20 / GPT‑OSS‑Swallow v0.1 提供 20B 和 120B 双语日英 LLM，通过 CPT、SFT 和 RLVR 训练，能够在数学和编码任务上与 GPT‑OSS 匹配或超越，于 2026 年 2 月发布，包含四种 SFT/RL 变体，并将推出量化版本。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 3k / ⭐ 21 / youri‑7b 是一个32层、4096隐藏单元的 transformer，基于 Llama2‑7b 构建，持续在约 40 B 个日语 token（CC‑100、C4、OSCAR、Pile、Wikipedia）上进行预训练，并于 2023 年 10 月 31 日发布，在 AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA 和 Winogrande 上取得了竞争性的分数。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 3k / ⭐ 26 / Japanese 3.6 B‑parameter GPT‑NeoX 模型细调以适应指令遵循（SFT‑v2），对比之前的 SFT 与 ChatGPT 在 100 条提示上进行评估，发布于 2023 年 3 月 31 日。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 3k / ⭐ 50 / GGUF‑formatted NVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese，已从 imatrix 数据集重建，并准备好在 CUDA 上使用 llama.cpp 运行。
 * [gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - 📥 3k / ⭐ 18 / 由 ABEJA, Inc. 在 Japanese CC‑100、Wikipedia 与 OSCAR 上训练的大型日语 GPT‑2 模型，使用 sentencepiece 进行分词，可通过 Hugging Face transformers 在 PyTorch 或 TensorFlow 上使用，依据 MIT license。
 * [GPT-OSS-Swallow-20B-SFT-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-SFT-v0.1) - 📥 2k / ⭐ 5 / GPT‑OSS‑Swallow v0.1 是一个双语日英模型系列（20B & 120B），通过持续预训练、监督微调和带可验证奖励的强化学习来训练，以保持数学和编码性能，目前已发布 SFT 和 RL 变体，并计划发布量化版本。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 2k / ⭐ 143 / LFM2.5‑1.2B‑JP 是一款针对日语优化的聊天模型，在日语知识与指令遵循方面优于 LFM2，支持使用 LoRA 进行微调，支持通过 Transformers、vLLM 和 llama.cpp 进行推理，取得 50.7 JMMLU、58.1 M‑IFEval 与 56.0 GSM8K 分数。
 * [gpt2-japanese-lyric-small](https://huggingface.co/skytnt/gpt2-japanese-lyric-small) - 📥 2k / ⭐ 3 / 日语 GPT‑2 歌词生成模型，训练于 143,587 首 uta‑net 歌曲，提供 Web 演示及 Torch/Transformers 使用示例。
 * [gpt2-small-japanese-char](https://huggingface.co/ku-nlp/gpt2-small-japanese-char) - 📥 2k / ⭐ 3 / 日本字符级 GPT-2 Small（90 M 参数）已在171 GB 的日本维基百科、CC‑100 和 OSCAR 数据上预训练，训练约3个月，使用 A100 GPU，并已准备好通过 Hugging Face pipeline 进行文本生成。
 * [RakutenAI-7B-instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) - 📥 2k / ⭐ 50 / RakutenAI‑7B‑instruct, 基于 Mistral‑7B‑v0.1 构建，是一款聚焦日语的 LLM，在日语基准测试中获得最高分，同时匹配英语性能，并发布了聊天调优版本。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 2k / ⭐ 57 / TinySwallow‑1.5B‑Instruct 是一个 1.5 B 的日语指令调优自回归语言模型，使用 TAID 从 Qwen2.5‑32B‑Instruct 进行蒸馏，供研究用途。
 * [RakutenAI-7B](https://huggingface.co/Rakuten/RakutenAI-7B) - 📥 2k / ⭐ 52 / RakutenAI‑7B 是基于 Mistral‑7B‑v0.1 的日语 LLM，在日语基准测试中领先，同时在英语任务上也保持竞争力，提供指令调优和聊天调优版本，并在 arXiv 上发布技术报告。
 * [RakutenAI-7B-chat](https://huggingface.co/Rakuten/RakutenAI-7B-chat) - 📥 2k / ⭐ 66 / RakutenAI‑7B‑chat 是基于 Mistral‑7B‑v0.1 架构打造的日本 LLM，提供了优秀的日语理解基准成绩，并在英语上具有竞争力的表现，拥有基础模型（RakutenAI‑7B）和指令微调版本（RakutenAI‑7B‑instruct）。
 * [ALMA-7B-Ja-V2](https://huggingface.co/webbigdata/ALMA-7B-Ja-V2) - 📥 2k / ⭐ 20 / C3TR‑Adapter应用了4‑bit QLoRA到gemma‑7b，使得在免费Colab上仅需8.1 GB GPU使用量，而ALMA‑7B‑Ja‑V2提供日英翻译（并支持德语、中文、冰岛语、捷克语），其效果通过BLEU和chrF++指标评估。
 * [diafill-sarashina2.2-3b-instruct](https://huggingface.co/sbintuitions/diafill-sarashina2.2-3b-instruct) - 📥 2k / ⭐ 1 / DiaFill 是一款经过精细调校的日本双说话人对话脚本生成器，能够根据种子提示生成自然、充满填充语的口语式对话，训练数据来自专有的 GENIAC 数据。
 * [youri-7b-instruction](https://huggingface.co/rinna/youri-7b-instruction) - 📥 2k / ⭐ 15 / 一款70亿参数的日语指令调优变换器（32层，4096隐藏层），基于rinna/youri‑7b构建，使用Alpaca格式在Dolly、FLAN和Izumi数据集的日语子集上微调，于2023年10月31日发布。
 * [nekomata-7b-instruction](https://huggingface.co/rinna/nekomata-7b-instruction) - 📥 2k / ⭐ 10 / rinna/nekomata‑7b‑instruction 是一个 32 层、4096 隐层的日语指令调优 Transformer（基于 nekomata‑7b/Qwen 架构），它遵循 Alpaca 输入格式，并在挑选的 Dolly、FLAN、Izumi lab 以及其他日语数据集子集上进行训练。
 * [nekomata-14b](https://huggingface.co/rinna/nekomata-14b) - 📥 2k / ⭐ 19 / nekomata‑14B 是一个 40 层、5120 隐藏层的 Transformer，初始化自 Qwen‑14B，并在 66 B 日语 tokens（CC‑100、Japanese C4、OSCAR、The Pile、Wikipedia 以及 rinna 数据集）上持续预训练，使用包含 Qwen 词汇表 >150 k 的词表，在 16 台 Amazon Trainium 节点上训练约 7 天，并于 2023 年 12 月 21 日发布。
 * [youri-7b-chat](https://huggingface.co/rinna/youri-7b-chat) - 📥 2k / ⭐ 14 / rinna/youri‑7b‑chat 是一个 32 层、隐藏层维度 4096 的 Transformer，基于 rinna/youri‑7b 进行指令微调，采用聊天式输入格式，并使用 Dolly、Anthropic、FLAN、Izumi 以及日语语料的挑选子集进行训练，发行日期为 2023 年 10 月 31 日。
 * [Sakura-13B-Galgame](https://huggingface.co/sakuraumi/Sakura-13B-Galgame) - 📥 2k / ⭐ 125 / SakuraLLM 提供非商业的、RLHF‑fine‑tuned 日语至中文翻译模型，面向轻小说和 galgame 领域，基于开源 LLMs，使用领域特定数据，支持多种尺寸、离线部署以及明确的许可与使用指南。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 2k / ⭐ 1 / Qwen3‑Swallow v0.2 提供了 30‑B 和 32‑B 双语日英 LLM，采用 CPT、SFT 与 RLVR 训练，提升日语准确性、翻译、数学与编码能力，以匹配或超越原始 Qwen3，提供九个模型（CPT、SFT、RL）和 AWQ‑quantized 版本，同时发布 GPT‑OSS‑Swallow。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 2k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter Japanese extension，进一步预训练以适用于日语语言任务，并提供 base、instruct、fast 和 fast‑instruct 变体，由 ELYZA team 在 Llama 2 Community License 下维护。
 * [open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - 📥 2k / ⭐ 205 / OpenCALM 是 CyberAgent, Inc. 开发的日语仅解码器 Transformer 语言模型套件，包含 160 M 至 6.8 B 参数的版本，预训练于 Wikipedia 和 Common Crawl， 可通过 Transformers 库以 CC BY‑SA 4.0 许可证获取。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 2k / ⭐ 96 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 7 B 的日语优化扩展，提供 instruct 和 fast 变体，参数为 6.27–6.37 B，可通过 Hugging‑Face Transformers 库访问。
 * [open-calm-large](https://huggingface.co/cyberagent/open-calm-large) - 📥 1k / ⭐ 10 / OpenCALM 是来自 CyberAgent 的一个仅解码器的日语 Transformer 系列（参数量 160 M – 6.8 B，范围从 open‑calm‑small 到 open‑calm‑7b），训练数据为日语 Wikipedia 和 Common‑Crawl，采用 CC BY‑SA 4.0 许可证，可通过 Hugging Face transformers 使用。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 82 / 来自 ELYZA 的日语增强版 Llama‑2‑7B，已预训练以提供扩展的日语语言能力，提供标准、指导和快速版本，附有详细使用示例、开发者署名，并遵循 Meta’s Llama‑2 Community License 许可。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 1k / ⭐ 17 / TokyoTech‑LLM 仓库提供了经过日本数据增强的 Swallow Llama‑2 系列 LLaMA‑2 模型，涵盖 7B、13B 和 70B 变体，其中包括 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以来发布的 7B Plus 版本。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 1k / ⭐ 5 / 一个存储库，托管来自国立信息研究所LLM研发中心的8.6 B参数llm‑jp‑4‑8b‑base transformer，采用预训练和中间训练，随后进行监督微调和直接偏好优化（不使用强化学习），并提供PyTorch‑transformers使用指南。
 * [Murasaki-4B-v0.3-GGUF](https://huggingface.co/Murasaki-Project/Murasaki-4B-v0.3-GGUF) - 📥 1k / ⭐ 1 / Murasaki‑4B‑v0.3 是一个 4 billion 参数的 GGUF System 2 推理模型，专为 ACGN 日英翻译优化，具备提示控制的 CoT 开关、增强的 Non‑think 模式、BF16 基准以及多种量化；全部采用 CC BY‑NC‑SA 4.0 许可证。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 1k / ⭐ 16 / 来自 NII 研发中心的日本大型语言模型集合（1.8 b 至 172 b beta1，含 instruct 版本），以 Hugging Face Transformers 格式打包，并在混合日语、英语与网络语料库（总计>1万亿个标记）上预训练。需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29 以及 flash‑attn ≥ 2.5。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 1k / ⭐ 15 / LLM‑jp提供13 B和1.3 B变压器语言模型，包括多种指令调优变体，采用Megatron‑DeepSpeed和Hugging Face Transformers生态系统构建。
 * [ArrowCanaria-Llama-8B-SFT-v0.1](https://huggingface.co/DataPilot/ArrowCanaria-Llama-8B-SFT-v0.1) - 📥 1k / ⭐ 23 / ArrowCanaria‑Llama‑8B‑SFT‑v0.1 是一款 8‑B 参数的日语 LLM，在 17.5 万条合成对话上进行微调，以在 AI‑VTuber 场景中提供自然的闲聊、角色扮演、推理和工具使用，并基于 Llama 3.1‑Swallow 8B‑Instruct 构建。
 * [open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - 📥 1k / ⭐ 4 / OpenCALM 是 CyberAgent 开发的一套日语仅解码器（decoder‑only）Transformer 语言模型，参数规模从 160 M 到 6.8 B，训练数据来自日语维基百科与 Common Crawl，并按 CC BY‑SA 4.0 许可发布。
 * [llm-jp-13b-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0) - 📥 1k / ⭐ 41 / 来自 LLM‑jp 的大规模语言模型 — 13B 和 1.3B 日英双语 transformer，拥有多种指令和 LoRA 变体，使用 Megatron‑DeepSpeed 预训练，并以 Hugging Face 格式（torch ≥ 2.0，transformers ≥ 4.34）发布。
 * [shukatsu-gemma4](https://huggingface.co/careerbot/shukatsu-gemma4) - 📥 1k / ⭐ 1 / shukatsu‑gemma4‑26b‑v1 是一个针对日本求职支持微调的 Gemma 4 26B 模型，提供对入学表单、个人宣传和职业建议的逻辑且富有同理心的反馈，支持 GGUF 格式本地推理。
 * [llm-jp-13b-instruct-full-jaster-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-v1.0) - 📥 1k / ⭐ 15 / 13‑B 与 1.3‑B 参数的 LLM‑jp 指令微调模型（包含 LoRA 变体）的代码仓库，以 Hugging Face Transformers 格式打包，并要求 torch ≥ 2.0、transformers ≥ 4.34 与 accelerate 0.23，已在约 50k 个日语/英语/代码混合示例上使用 Megatron‑DeepSpeed 与 PEFT 训练。
 * [ELYZA-japanese-Llama-2-13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct) - 📥 1k / ⭐ 43 / ELYZA‑japanese‑Llama‑2‑13b 扩展了 Meta’s Llama 2，额外对日语进行预训练，提供 13 B 参数模型（包括 instruct 和 fast 变体），可在 Llama 2 Community License 下使用 PyTorch 和 🤗 Transformers 加载。
 * [llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-jaster-dolly-oasst-v1.0) - 📥 1k / ⭐ 8 / 托管LLM‑jp的13 B和1.3 B日英指令和预训练模型，在多个变体检查点中提供，需使用Hugging Face Transformers（torch ≥ 2.0、transformers ≥ 4.34、accelerate 0.23）以及DeepSpeed支持。
 * [llm-jp-13b-instruct-full-dolly-oasst-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-instruct-full-dolly-oasst-v1.0) - 📥 1k / ⭐ 4 / LLM‑jp 提供指令式以及预训练的 13B/1.3B Transformer 模型，格式为 Hugging Face 和 DeepSpeed，训练基于 50k+ 混合日语/英语/源代码数据，并要求 torch ≥ 2.0、transformers ≥ 4.34 以及 accelerate 0.23。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 1k / ⭐ 1 / 日本增强、指令调优的 Gemma‑2 模型，基于 Llama（2b/9b/27b 预训练和指令版本），于 2025 年 5 月 19 日发布，可通过 HuggingFace 和 Swallow 团队网站获取。
 * [LFM2-350M-PII-Extract-JP](https://huggingface.co/LiquidAI/LFM2-350M-PII-Extract-JP) - 📥 1k / ⭐ 54 / LFM2‑350M‑PII‑Extract‑JP 是一款 350‑million 参数、在设备上运行的日语 PII 提取模型，性能可与 GPT‑5 相媲美，能够在合同、电子邮件和医疗报告中进行敏感数据遮蔽。
 * [ELYZA-japanese-Llama-2-13b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast-instruct) - 📥 1k / ⭐ 24 / 一款日语适配的 Llama 2 13B 参数模型——ELYZA‑Japanese‑Llama‑2‑13B‑Fast‑Instruct，提供快速分词、使用示例、开发者署名，并符合 Llama 2 Community License。
 * [ELYZA-japanese-Llama-2-13b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-fast) - 📥 1k / ⭐ 7 / 本仓库提供了 ELYZA‑Japanese‑Llama‑2‑13B‑Fast 模型——在 Llama‑2‑13B 基础上加入了日语预训练——包括 instr‑styled 和 fast‑vocab 版本（≈13.1 B 参数，词表 44,581），并附带示例 PyTorch 用法，由 Akira Sasaki、Masato Hirakawa、Shintaro Horie、Tomoaki Nakamura、Sam Passaglia 和 Daisuke Oba 开发，并在 Meta 的 Llama 2 Community License 下发布。
 * [ELYZA-japanese-Llama-2-13b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b) - 📥 1k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑13b 在 Meta 的 Llama 2 上追加了额外的预训练，以提升日语能力，提供了多种 13 B 参数变体（包括 instruct 和 fast），由一组研究人员以 LLAMA 2 Community License 发布。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 301k / ⭐ 76 / Japanese BERT‑base 在 2019 年日本维基百科上预训练，使用 IPA‑dictionary 与全词掩码，12 层 768 维，32,000 词表，512 标记序列，1 M 步骤，可在 cl‑tohoku/bert‑japanese 获取，遵循 CC‑BY‑SA 许可。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 247k / ⭐ 9 / 日语 DeBERTa V2 大型模型，已在 171 GB 的日语 Wikipedia、CC‑100 与 OSCAR 上训练，使用字符级 SentencePiece 分词和全词掩码，已准备好通过 Hugging Face Transformers 进行下游微调。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 212k / ⭐ 41 / 一个预训练于约 17 M 条日语维基百科句子（2.6 GB）的 BERT base 模型，使用 IPA 字典和 WordPiece 进行分词，拥有 12 层 / 768‑维隐藏状态 / 12 头，32 000‑token 词汇表，已在 Cloud TPUs 上训练了 1 M 步，并以 CC‑BY‑SA 3.0 许可发布。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 105k / ⭐ 8 / 一个 BERT‑base 日语模型（12 层，768 维隐藏，12 头），使用 MeCab IPA 词级分词后再进行字符级分词生成 4000 词的词表，在约 1700 万句来自日语维基百科（2.6 GB）的句子上预训练，训练代码位于 cl‑tohoku/bert‑japanese，采用 CC BY‑SA 3.0 许可证发布。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 49k / ⭐ 6 / 一个 BERT‑base 日语模型（12 层，768-维隐藏状态，12 头），在 3000 万条维基百科句子（约 4 GB）上训练，使用 Unidic 2.1.2 词级分词，随后进行字符级分词和全词掩码，使用 512 令牌序列，256 批次，以及 1 M 训练步骤。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 29k / ⭐ 5 / ModernBERT‑Ja‑30M 是一种日语 BERT 变体，融合了本地和全局注意力与 RoPE，训练于 4.39 TB 日英文本，支持 8,192 令牌序列，参数规模从 30 M 到 130 M，最佳搭配 Flash Attention 2。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 25k / ⭐ 48 / LINE DistilBERT Japanese 是一个 6600 万参数的 DistilBERT 模型，已在 131 GB 的日语网页文本上使用内部 BERT‑base 教师进行预训练，评估基准为 JGLUE，采用 MeCab Unidic 与 SentencePiece 进行分词，并以 Apache 2.0 许可证发布。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 11k / ⭐ 39 / Japanese‑Roberta‑Base 是来自 rinna Co., Ltd. 的预训练掩码语言模型，提供了正确加载、token 预处理、position‑id 处理的准则，以及强调需要前置 [CLS] token 和一致 tokenization 的使用示例。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 11k / ⭐ 2 / Japanese DeBERTa V2 tiny，在约171 GB的日本维基百科、CC‑100 与 OSCAR 语料库上预训练，需使用 Juman++ 词分割，训练耗时 33 小时，使用8块 NVIDIA A100 GPU，并可用于下游任务的微调。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 9k / ⭐ 47 / 这是一款 1.32 亿参数的日语 ModernBERT 模型，融合了 local‑global 与 RoPE 注意力机制，训练于 4.39 T 词条（日语/英语），词表大小 102k，最大序列长度 8,192，针对 Flash Attention 2 做了优化。
 * [roberta-base-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) - 📥 5k / ⭐ 8 / Japanese RoBERTa base model 预训练于日本维基百科和 CC‑100，采用 Juman++ 分词，训练了 700k 步，使用八个 NVIDIA A100 GPU，学习率为 1e‑4。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 5k / ⭐ 27 / Japanese BERT‑base（12 层，768 隐藏，12 头）在 4 GB 的日语维基百科（≈30 M 句）上预训练，使用 Unidic 2.1.2 词级分词、WordPiece 子词分词和全词遮蔽。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 5k / ⭐ 30 / Japanese DeBERTa V2 基础模型已在 171 GB 的日语维基百科、CC‑100 和 OSCAR 数据上预训练，使用 Juman++ 分词和 SentencePiece 标记化，经过三周在八块 NVIDIA A100 GPU 上训练，现已准备好用于微调。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 5k / ⭐ 21 / ModernBERT‑Ja‑310M 是一种日语 BERT 变体，融合了局部-全局注意力和 RoPE，训练于 4.09 T 日语/英语文本，支持 102 400 词汇量、8 192 令牌序列，并针对 Flash Attention 2 进行了优化。
 * [deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 📥 3k / ⭐ 9 / Japanese DeBERTa‑V2 大模型预训练于 171 GB 日文文本（Wikipedia、CC‑100、OSCAR），使用 Juman++ 分词，在 8 台 A100 GPU 上训练 36 天，可针对下游任务进行微调。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 3k / ⭐ 4 / DeBERTaV2 base 在日本语语料库（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上训练，并使用 FP‑16 微调进行 NLU 任务（JSTS、JNLI、JCommonsenseQA），以 CC BY‑SA 4.0 许可发布，并由日本研究资助。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 3k / ⭐ 32 / Japanese RoBERTa‑base 在日本 Wikipedia 与日本 CC‑100 上预训练，采用 Juman++ 词分割与 SentencePiece 分词，使用 Adam（lr = 1e‑4，native AMP）在 8 台 NVIDIA A100 GPU 上训练了一周，可微调，并在 JGLUE 上报告了结果。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 12 层，768 维度的 BERT‑Base 日语模型，在 2.6 GB Wikipedia（≈17 M 句子）上训练，使用 IPA‑dictionary 字符分词与 whole‑word masking，并在 CC‑BY‑SA 3.0 许可下发布。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 374k / ⭐ 69 / Ruri v3 是基于 ModernBERT‑Ja 的先进日语文本嵌入模型，支持多达 8,192 词元输入，100K 词元词汇表，FlashAttention 加速推理，并提供多种尺寸变体，便于快速使用 sentence‑transformer。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 361k / ⭐ 12 / 日语通用文本嵌入模型（Ruri‑v3，30‑310 M 参数，8192‑token 最大，JMTEB 分数高）与 Sentence‑Transformers 使用示例以及与其他日语嵌入模型的基准对比一起提供。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 242k / ⭐ 8 / Ruri v3是一个最先进的日语文本嵌入模型，基于ModernBERT‑Ja构建，支持最多8,192个标记，拥有100 k词汇量，支持FlashAttention加速，并提供多种规模，从37 M到315 M参数。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 41k / ⭐ 9 / 包括 Ruri v3 日语文本嵌入（30 M–310 M 参数，8192‑token 限制，JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前缀的 Sentence Transformers 指令，以及对数个日语模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基准结果。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 30k / ⭐ 4 / Ruri v3 是基于 ModernBERT‑Ja 的前沿日语文本嵌入模型，支持最多 8192 token 序列、100K token 词汇量、FlashAttention，并以 30 M 至 310 M 参数规模发布，供 sentence‑transformers 使用。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 18k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一个 768 维的句子变换器，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，训练了一个 epoch 的 shunk031/jsnli，并包含用于聚类、语义搜索以及同时兼容 Sentence‑Transformers 和 HuggingFace 的示例。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 17k / ⭐ 16 / JaColBERTv2 是一个仅适用于日语的基于 ColBERT 的检索模型，在 MMarco 上通过知识蒸馏训练（每个正例 31 个负例，250k 次，batch 32）。目前它优于 multilingual‑e5‑large、BGE‑M3 和 JaColBERT，完整评估正在进行中。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 16k / ⭐ 44 / 一组已准备好发布的 Ruri v3 日语文本嵌入模型（30m–310m），完整附带 SentenceTransformer 使用技巧、查询/段落前缀，以及 JMTEB 基准结果，展示它们与其他日语和多语言嵌入模型的比较。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 15k / ⭐ 2 / Ruri v3 提供高性能的日语文本嵌入，支持至 8192 个 token，拥有 100k 个 token 的词汇表，支持 FlashAttention，并提供多种模型规模（30 m–310 m），以实现高效推理和通过 sentence‑transformers 进行微调。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 14k / ⭐ 34 / GLuCoSE 是一个基于 LUKE 的日语句子嵌入模型，输出 768 维均值池化向量（最多 512 个标记），在 Web 和 NLI/搜索数据上训练，在相似性基准测试中达到了 0.864 的 Spearman 相关系数和 0.818 的 Pearson 相关系数。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 10k / ⭐ 44 / PLaMo‑Embedding‑1B 是 Preferred Networks 的一款日语文本嵌入模型，它将日语文本转换为向量，用于信息检索、分类和聚类，在 JMTEB 基准上表现出强大性能，并且在 Apache v2.0 许可证下可免费使用。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 6k / ⭐ 22 / GLuCoSE v2 是一款 CPU 友好的日语文本嵌入模型，通过蒸馏和多阶段对比学习进行微调，提供卓越的语义相似性和检索性能——在 MIRACL 及相关基准上优于同等规模的模型。
 * [ruri-small-v2](https://huggingface.co/cl-nagoya/ruri-small-v2) - 📥 2k / ⭐ 4 / Ruri发布日本通用文本嵌入模型v3（30 M–310 M 参数，8192‑Token 最大长度），在JMTEB上取得最高分，提供直接的 sentence_transformers 用法（以「クエリ:」或「文章:」为前缀），并给出检索、STS、分类、重排序、聚类和成对分类任务的基准结果。
 * [ruri-v3-pt-310m](https://huggingface.co/cl-nagoya/ruri-v3-pt-310m) - 📥 2k / ⭐ 1 / Ruri v3 是一个基于 ModernBERT‑Ja 的预训练日语文本嵌入模型，提供 30 M 到 310 M 参数的不同版本（包括一个微调的 310 M 版本），可通过 sentence-transformers 使用，并可选择使用 Flash‑Attention 2，采用 Apache 2.0 协议发布。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 3M / ⭐ 54 / Japanese wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 与 JSUT 上微调，需 16 kHz 音频，并可通过 HuggingSound 或 HuggingFace 管道使用。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 30k / ⭐ 38 / reazonspeech-nemo-v2 是一个 619‑M‑参数的日语长文本 ASR 模型，基于改进版 Fast‑Conformer 及 Linearly Scalable Attention，在 ReazonSpeech v2.0 语料库上训练，支持通过 subword RNN‑T decoder（3000‑token SentencePiece）进行多小时推理，并以 Apache 2.0 许可分发。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 24k / ⭐ 133 / Anime Whisper 是一款轻量级的日语 ASR 模型，在约 5,300 小时的动漫风格对话上进行微调，能够提供低幻觉、节奏对齐标点，以及准确转录非言语声音和 NSFW 内容，并且需要在没有初始提示的情况下运行。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 15k / ⭐ 97 / Kotoba‑Whisper‑v2.2 是一个日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了说话人划分和自动标点功能，通过 HuggingFace‑Transformers pipeline，并与 Asahi Ushio 与 Kotoba Technologies 合作开发。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 12k / ⭐ 52 / NVIDIA NeMo 的 0.6 B 参数 Hybrid FastConformer‑TDT‑CTC ASR 模型可转写带标点的日语语音，并可在 NeMo 框架内用于推理或微调。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 9k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供了快 6.3 倍的蒸馏 Whisper 模型，用于日语和英语 ASR，并实现双向语音转文本翻译，这些模型是基于 OpenAI 的 Whisper large‑v3 通过知识蒸馏、交叉熵和 KL‑divergence 损失构建。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 4k / ⭐ 90 / Kotoba‑Whisper v2.0 是从 OpenAI Whisper large‑v3 蒸馏出的日语 ASR 模型，训练于 720 万个 ReazonSpeech 剪辑，推理速度快 6.3 倍，同时在同域测试中匹配教师模型的 CER/WER，并提供 stable‑ts/标点支持以及完整的训练代码在 GitHub 上。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 4k / ⭐ 19 / Kotoba‑Whisper‑v2.1 是一种日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了标点后处理管道，保持可比的 CER 性能，同时实现无缝、标点感知的转录。
 * [whisper-ja-1.5B](https://huggingface.co/efwkjn/whisper-ja-1.5B) - 📥 3k / ⭐ 2 / 一个微调的 Whisper‑Large‑v3 基线在 KitsuneX07、TEDxJP、kotoba‑tech、Saruwatari‑lab 和 grider‑without‑ai 测试集上提供了竞争性的 SOTA CER，训练数据来自 OOPPEENN、Reazon、小虫哥_、Common Voice 20 和 deepghs，比早期模型拥有更小的检查点并偶尔出现重复。
 * [kotoba-whisper-v1.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v1.1) - 📥 2k / ⭐ 34 / Kotoba‑Whisper v1.1 是一款日语 ASR 模型，它在 kotoba‑whisper‑v1.0 的基础上扩展了无缝标点添加后处理管道，提升了转录准确率并比多个 Whisper 基线减少了延迟。
 * [wav2vec2-large-xlsr-japanese](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese) - 📥 1k / ⭐ 5 / 针对日语精细调优的 Wav2Vec2‑Large‑XLSR‑53，在 Common Voice 和 JSUT 语料库上训练，使用 16 kHz 音频，已准备好用于 16 kHz 粤语使用与评估。
 * [moonshine-tiny-ja](https://huggingface.co/UsefulSensors/moonshine-tiny-ja) - 📥 1k / ⭐ 11 / Moonshine AI的小型、边缘就绪ASR模型能够实时转录日语语音，并在model card中详细说明低资源部署。

### feature-extraction
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 45k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一个 Apache‑2.0 许可的日语 CLIP 模型，基于 ViT‑B/16，训练于 CC12M captions 翻译成日语，并于 2022 年 5 月 12 日发布。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 41k / ⭐ 51 / 一款在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上使用 MultipleNegativesRankingLoss 细调的 Japanese Sentence‑BERT v2，较 v1 提升了约 1.5–2 %的准确率，并以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 发布。
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 34k / ⭐ 11 / 用于生成句子嵌入的 Japanese Sentence‑BERT (v1) 模型，已提供改进版 v2，并通过 Hugging Face Transformers 以及自定义的 `SentenceBertJapanese` 类进行示例使用。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 23k / ⭐ 29 / LY Corporation的clip‑japanese‑base 是一个日语 CLIP 模型，在约10亿对图像‑文本对上训练，使用 Eva02‑B transformer 图像编码器和 12 层 BERT 文本编码器，在 STAIR 上实现 R@1 0.30，在 Recruit 上得到 0.89 的准确率，在 ImageNet‑1K 上得到 0.58 的准确率，并支持 zero‑shot 图像分类和检索。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 12k / ⭐ 2 / ja_ginza_electra 是一个 spaCy v3 Python 包，提供一个在 mC4 和 UD_Japanese_BCCWJ r2.8（基于 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator）上微调的日语 ELECTRA 模型，并配有自定义 bunsetu‑phrase 检测功能，按 MIT license 分发。
 * [japanese-avhubert-large_noise_pt](https://huggingface.co/enactic/japanese-avhubert-large_noise_pt) - 📥 11k / ⭐ 1 / 一个预训练的 2,250 小时 AVHuBERT Large 自监督模型，在日本音频-视觉数据上训练并使用噪声增强，以稳健支持音频-视觉语音识别。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 3k / ⭐ 3 / 一个日语 BERT‑base 模型，在 JSNLI 上使用有监督 SimCSE 进行微调，通过 Sentence‑Transformers 或 HuggingFace 提供，采用 CLS 池化。在 1M 个样本上训练，批量大小为 512，学习率为 5×10⁻⁵，温度为 5×10⁻⁵，64 令牌限制，采用 BFloat16 精度。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 3k / ⭐ 14 / Japanese Sentence‑LUKE 模型在与 Sentence‑BERT 同一数据集上训练，表现超过或匹配其性能，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，并通过 Hugging Face Transformers 的 MLukeTokenizer 与 LukeModel 进行使用。
 * [fasttext-ja-vectors](https://huggingface.co/facebook/fasttext-ja-vectors) - 📥 2k / ⭐ 4 / fastText 是一个轻量级、开源库，能够在标准的 CPU 上快速学习单词和句子嵌入以及分类器，几分钟内训练数十亿个单词，可压缩以便移动使用，并提供用于分类和语言识别的预训练向量。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 2k / ⭐ 17 / 日本CLIP模型 clip‑japanese‑base‑v2，升级后约20亿图像‑文本对并采用蒸馏，配合 Eva02‑B 图像编码器和 12 层 BERT 文本编码器，将 ImageNet‑1k 准确率提升至 0.708，超过前代模型。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 2k / ⭐ 55 / 一个Japanese‑language T5 model，在约100 GB的Wikipedia和OSCAR数据上使用SentencePiece tokenization进行预训练，超越了Google’s multilingual T5在news‑classification benchmark上的表现，但需要fine‑tuning，并可能产生biased outputs.
 * [japanese-avhubert-base_noise_pt](https://huggingface.co/enactic/japanese-avhubert-base_noise_pt) - 📥 2k / ⭐ 1 / 用于日语 AVHuBERT AV‑SR 模型的仓库，该模型在约2,250小时的音频‑视觉数据上预训练，并通过广泛的噪声增强实现了鲁棒的语音识别。

### text-ranking
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 495k / ⭐ 5 / 日本训练的 CrossEncoder 重新排序器，尺寸从 xsmall（384）到 large（1024），以及 BGE‑v2‑m3‑v1 模型，提供微调、推理和 JQaRA、JaCWIR、MIRACL、JSQuAD 上的基准分数示例代码。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 46k / ⭐ 7 / 日语 CrossEncoder 再排序模型，覆盖 xsmall 到 large（含 BGE），在 JQaRA、JaCWIR、MIRACL 与 JSQuAD 上进行评估，并为 sentence_transformers 与 HuggingFace 提供即用的集成示例。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 27k / ⭐ 13 / Ruri‑v3 Reranker 是一个基于 ModernBERT‑Ja 构建的稳健日语文本重排器，支持最高 8,192‑token 序列、100k‑token 词汇表、FlashAttention 以及 SentencePiece 分词器，并可通过 sentence‑transformers 使用。
 * [japanese-reranker-small-v2](https://huggingface.co/hotchpotch/japanese-reranker-small-v2) - 📥 9k / ⭐ 2 / Japanese‑reranker‑small‑v2 是一系列轻量级、快速的日语重排序模型（v2），提供从极小到基础的变体，最高可达 0.89 的平均分，GPU 推理时间为 2–15 秒，支持交叉编码器选项，并需要 Hugging Face Transformers v4.48+，可选 Flash Attention 2 进行加速。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 6k / ⭐ 6 / 快、轻量级的日语 Reranker v2 模型（tiny、xsmall、small、base），带有基准测试分数和 GPU 速度，可通过 sentence_transformers CrossEncoder 与 transformers ≥ v4.48 使用（可选闪存加速 flash‑attn），并且在 ONNX/量化形式下可用于 CPU/ARM。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 6k / ⭐ 7 / 一个日本 Reranker v2 套件，发布 CrossEncoder 和 base 模型，覆盖从 tiny 到 large，每个都有基准得分和 GPU 推理时间，并要求 HuggingFace Transformers ≥ 4.48（可选 flash‑attn 用于更快推理）。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 3k / ⭐ 16 / 日语 CrossEncoder 重排序模型——从xsmall到large——在日语文本上训练，通过sentence_transformers公开，评估在JQaRA、JaCWIR、MIRACL和JSQuAD上。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 1k / ⭐ 6 / 紧凑、高速的日语重排序库（v2）提供 tiny‑through‑base 和 cross‑encoder 模型，并给出详细的延迟与准确率统计，要求 Transformers ≥ 4.48（可选 Flash‑Attention 2），支持 ONNX/量化，适用于 CPU/ARM 部署。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 1k / ⭐ 15 / 一个日语 CrossEncoder 重新排序器套件——包括 xsmall、small、base、large 和 japanese‑bge‑reranker‑v2‑m3‑v1——配合示例用法、在多个基准上的评估指标和支持文档。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 1M / ⭐ 13 / 一个基于新 VNTL 数据集构建的 LLaMA 3 Youko qlora 微调模型，优化用于准确、逐字翻译日本视觉小说为英文，不使用聊天模式，采用默认 LLaMA 3 提示，并推荐中性采样（温度 0，无重复惩罚）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 77k / ⭐ 8 / Sugoi LLM 14B Ultra (GGUF) 是一个日语到英语的翻译模型，BLEU 分数为 21.38，几乎是其之前的 13.67 的两倍，在 RPG‑Maker 括号文本、提示遵循强度以及为交互式聊天 UI 的 JSON 输出方面表现出色。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 47k / ⭐ 31 / 已微调、GGUF-量化的 LFM2-350M checkpoint，用于近实时双向日英短至中等文本翻译，可通过 llama.cpp 使用。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 34k / ⭐ 73 / 来自 Opus 语料库的日语‑英语 Transformer‑Align 机器翻译模型，使用归一化和 SentencePiece 预处理，在 Tatoeba 测试集上达到了 41.7 BLEU 和 0.589 chr‑F。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 6k / ⭐ 118 / PLaMo Translation Model 是由 Preferred Networks 创建的大规模语言模型，专用于翻译任务，提供基础版、后训练版和评估版，在 PLaMo community license 下发布，并未针对聊天或其他下游用途进行 instruction‑tuned。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 2k / ⭐ 32 / FuguMT 是一个从日语到英语的 Marian‑NMT 翻译模型，使用 transformers 和 SentencePiece 构建，在 Tatoeba 上得分 39.1 BLEU。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 1k / ⭐ 54 / FuguMT 是一个基于 Marian‑NMT 的英日翻译模型，使用 Hugging Face Transformers 和 SentencePiece 构建，并在 Tatoeba 上获得了 32.7 的 BLEU 分数。

### text-classification
 * [finance-sentiment-ja-base](https://huggingface.co/bardsai/finance-sentiment-ja-base) - 📥 68k / ⭐ 3 / Finance Sentiment JA (base) 是基于 BERT 的日语情感模型，训练于翻译后的 Financial PhraseBank，能够将日语金融新闻分类为正面、负面或中性，宏观 f1 为 0.959，准确率 0.967，每秒 134.9 个样本。
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 10k / ⭐ 15 / 训练于 chABSA 数据集的日语情感分析模型，获得 loss 0.0001、accuracy 1.0、F1 1.0，由 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 构建，使用 Adam（learning rate 2e‑05、10 epochs、batch size 16）优化，并通过 `model(**inputs)` 进行评估。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 5k / ⭐ 16 / 在亚马逊产品评论上对日语 BERT (cl‑tohoku/bert‑base‑japanese‑v2) 进行微调，用于情感分类，经过6个周期，学习率为2 × 10⁻⁵，达到约81 %准确率和0.73 F1。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 3k / ⭐ 2 / 一个基于 Japanese BERT‑based model 的模型，已在 JGLUE JSTS 数据集上 fine‑tuned，用于语义相似性评分——在《Large Language Model Introduction》第5章中介绍——配有 Colab notebooks、transformers‑pipeline 用法以及 Apache 2.0 许可证。
 * [luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 📥 2k / ⭐ 43 / 一个在WRIME数据集上微调的日本LUKE模型，用于分类句子中表达的八种情绪——喜悦、悲伤、期待、惊讶、愤怒、恐惧、厌恶、信任。
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 1k / ⭐ 6 / 一款在 WRIME 数据集上微调的日语 BERT BASE 可为作家和读者预测八种情绪（喜悦、悲伤、期待、惊讶、愤怒、恐惧、厌恶、信任）的 0‑4 强度得分，代码已公开，在 K80 上训练耗时 3 小时，作家的均方误差约为 0.6，读者约为 0.2。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 360k / ⭐ 169 / Manga OCR 是一款 Vision Encoder‑Decoder OCR 工具，可读取纵向和横向的日语漫画文本，包括 furigana，适用于多种字体和低质量图像，并且源代码可免费获取。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 65k / ⭐ 6 / Meikiocr的 `meiki.text.recognition.v0`——基于 D‑FINE 的 MobileNetV4 模型，在日本视频游戏文本上微调——为水平文本提供最先进的准确率和延迟，能够从 960×32 的输入中检测多达 48 个字符，并输出每个字符的边界框和置信度分数。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 53k / ⭐ 3 / meikiocr 提供一个基于 D‑FINE、开源权重的视频游戏文本检测模型（v0.1，使用 MobileNet‑v4 骨干网络，提供两种分辨率变体和 64‑box 限制），以及实验性的低延迟 tiny 与 small 变体，训练材料来自日本视频游戏和漫画。

### token-classification
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 16k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日语 NER，能够提取八种实体类型（公司、政治/其他组织、设施、产品、事件），通过 `BertForTokenClassification` 实现，训练数据来自 Stockmark Wikipedia dataset，并可通过安装 `transformers`、`unidic_lite` 和 `fugashi` 使用，遵循 CC BY‑SA 3.0 许可。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 14k / ⭐ 10 / Fine‑tuned Japanese BERT‑Base适用于在维基百科数据集上的命名实体识别，该模型在《*Large Language Model Introduction*》一书第六章中呈现，并可通过Hugging Face transformers pipeline进行部署（Apache 2.0 许可）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 在日语 NER 语料库上对 XLM‑RoBERTa‑base 进行微调（标签 PER, ORG, LOC, INS, PRD, EVT），使用 5‑epoch Adam（lr 5e‑5，batch 12），达到 0.0173 的验证损失，已发布在 Transformers 4.23.1 和 PyTorch 1.12.1。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 2k / ⭐ 123 / 从 PaddleOCR‑VL 微调得到的 PaddleOCR‑VL‑For‑Manga 在 Manga109 的对话框裁剪图像上实现了70%完整句子准确率—是27%基线的三倍以上—并使用多语言数据集，包含训练代码和开发者指南。
 * [Heron-NVILA-Lite-15B](https://huggingface.co/turing-motors/Heron-NVILA-Lite-15B) - 📥 1k / ⭐ 14 / Heron‑NVILA‑Lite‑15B‑hf 是一个日语中心的视觉语言模型，基于 NVILA‑Lite 架构构建，采用 PALIGEMMA‑SIGLIP 视觉编码器、一个 MLP‑downsample 投影器以及 Qwen2.5‑14B‑Instruct LLM，支持日语和英语，并与 Hugging Face 无缝集成。

### text-to-speech
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 2k / ⭐ 9 / 一款名为 **tsukuyomi‑wavlm** 的日本文本转语音模型——在 tsukuyomi corpus 的 100 条语句上经过 300 个周期的微调，使用 WavLM 判别器和 A1/A2/A3 声韵特征，基于 VITS 架构，导出为 61 MB 的 ONNX 文件，用以生成 22.05 kHz 的合成语音。
 * [Anime-Llasa-3B](https://huggingface.co/NandemoGHS/Anime-Llasa-3B) - 📥 1k / ⭐ 26 / Anime‑Llasa‑3B 是一款日本TTS模型，基于 HKUSTAudio/Llasa‑3B，增强了更多训练数据以提升表达力和稳定性，并采用 CC‑BY‑NC‑4.0 许可证。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 1k / ⭐ 14 / Anime-XCodec2-44.1kHz-v2 将 16 kHz 的日语语音上采样至 44.1 kHz 的高保真音频，采用仅解码器的 RMS‑loss 微调，保持编码器/码本冻结并保留相同的语音令牌。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 104k / ⭐ 11 / 日本语言 BERT‑Base（12 层，768 维，12 头）使用 Unidic 基于词级加字符级分词和全词掩码在 CC‑100 及 2023 Wikipedia 上进行预训练，产生 7,027 名词表。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 64k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上训练，使用 Unidic‑lite 单词级标记化配合 WordPiece 子词和全词掩码（24 层，1024 维隐藏层，16 头，32k 词表），预训练代码在 cl‑tohoku/bert‑japanese。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 45k / ⭐ 63 / Japanese BERT‑base（12层，768维隐藏层，12头，32 k词汇表）在 CC‑100 和 2023‑Jan Wikipedia 上使用全词遮蔽预训练，采用 Unidic 2.1.2 词级分词加 WordPiece，训练 200 万步。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 22k / ⭐ 16 / Japanese DeBERTa V3 base 在 LLM‑jp v1.0 的 540 B tokens 上预训练，使用经过修改的 DeBERTa V3 设置训练，采用 unigram byte‑fallback tokenizer（不使用形态学分析器），并针对 JGLUE NLU 任务进行微调。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 16k / ⭐ 1 / 一个高度优化的 GGUF 版本的 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 并进行广泛的错误修复，专为日语语言能力调优，可在 llama.cpp 上运行，至少需要 16 GB 内存和 6 GB 磁盘（GPU 可选）。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 16k / ⭐ 5 / 一个针对日语微调的 Qwen 3.5‑9B GGUF 模型，使用 Unsloth Dynamic Quantization 2.0、广泛的错误修复、大规模日语校准，并可通过 llama.cpp 在 CPU 上使用 16 GB RAM 和 6 GB 磁盘运行。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / 一个预训练在≈100 GB的维基百科和 OS CC‑100 数据（SentencePiece 采用 10:1 混合且带 byte‑fallback）的日文 T5‑v1.1 模型，需要微调以适用于下游任务，包含迁移学习示例代码，指出输出中的潜在偏差，并遵循 CC‑BY‑SA 4.0 许可。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 15k / ⭐ 3 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一个顶尖的、面向日语的 GGUF 模型，使用 Unsloth Dynamic Quantization 2.0，配有广泛的日语校准和社区修复的错误，能够在 llama.cpp 上运行，即使没有 GPU，也只需至少 8 GB RAM 和 3 GB disk。
 * [SIP-jmed-llm-3-13b-OP-4k-base](https://huggingface.co/SIP-med-LLM/SIP-jmed-llm-3-13b-OP-4k-base) - 📥 11k / ⭐ 1 / SIP‑jmed‑llm‑3‑13b‑OP‑4k‑base 是一个 Apache‑2.0 许可证、领域适配的日英医学 LLM，基于 llm‑jp‑3.1‑13b 构建，由 SIP 第三期医学知识项目开发的研究原型，但不适用于临床使用。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-thinking-gguf) - 📥 6k / ⭐ 7 / 这是 LLM‑JP 的 4.8‑b “thinking” 模型的 GGUF 编译版本，使用 llama.cpp 并基于 imatrix 数据集和 custom chat template 构建。
 * [Llama-3-ELYZA-JP-8B-gguf](https://huggingface.co/mmnga/Llama-3-ELYZA-JP-8B-gguf) - 📥 5k / ⭐ 4 / 由 elyza 制作的 GGUF 转换版 Llama‑3‑ELYZA‑JP‑8B，使用 TFMC/imatrix‑dataset‑for‑japanese‑LLM 构建，已准备好与 llama.cpp 一起使用。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/alfredplpl/llm-jp-4-8b-thinking-gguf) - 📥 3k / ⭐ 3 / 这是一个 GGUF‑quantized 版本的 llm‑jp‑4‑8b‑thinking 模型，保持最小聊天模板，可通过 llama‑cpp 的 llama‑completion 或 LM Studio 使用，但不支持 llama‑cli/llama‑server。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 3k / ⭐ 3 / 一款使用日语维基百科和 mC4/ja 预训练的 T5 v1.1 模型，采用 GEGLU 激活函数，预训练期间不使用 dropout，未与嵌入层共享分类器，按 CC‑BY‑SA 4.0 许可证发布（商业用途须事先联系）。
 * [Qwen3.5-9B-Japanese-awy](https://huggingface.co/Aikimi/Qwen3.5-9B-Japanese-awy) - 📥 3k / ⭐ 5 / 一个 9‑B Qwen3.5 日语模型，使用 Unsloth 微调并转换为 GGUF，提供多种量化权重（Q4_K_M、Q5_K_M、Q3_K_M、F16、BF16‑mmproj），并在 TFMC/imatrix‑Japanese‑LLM 数据集上训练速度提升两倍。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 2k / ⭐ 73 / Llama‑3‑ELYZA‑JP‑8B 是一款经过日本增强的 8‑B Llama 3 模型，采用 GGUF (Q4_K_M) 和 AWQ 量化，支持通过 llama.cpp、LM Studio 或 OpenAI‑compatible API 运行。
 * [Llama-3.1-Nemotron-Nano-8B-v1-gguf](https://huggingface.co/mmnga/Llama-3.1-Nemotron-Nano-8B-v1-gguf) - 📥 2k / ⭐ 1 / 一个 gguf‑converted Llama‑3.1‑Nemotron‑Nano‑8B‑v1 模型，基于 imatrix 数据集构建，并附带使用 CUDA 编译 llama.cpp 的说明以及通过 llama‑cli 运行模型的示例烹饪提示。
 * [ArrowCanaria-Llama-8B-SFT-v0.1-gguf](https://huggingface.co/mmnga-o/ArrowCanaria-Llama-8B-SFT-v0.1-gguf) - 📥 2k / ⭐ 4 / DataPilot 的 gguf 转换版本 ArrowCanaria‑Llama‑8B‑SFT‑v0.1，训练自 TFMC/imatrix‑dataset‑for‑japanese‑LLM 数据，可以在为 CUDA 构建的 llama.cpp 中使用提供的 llama‑cli 命令运行。
 * [japanese-llama-3-8b-instruct-v2-i1-GGUF](https://huggingface.co/mradermacher/japanese-llama-3-8b-instruct-v2-i1-GGUF) - 📥 2k / ⭐ 1 / 提供加权/IMatrix GGUF 量化（2.1–6.7 GB）的日本 Llama‑3 8B Instruct v2 模型，提供 HuggingFace 上的静态量化链接，使用指南，以及针对模型请求的 FAQ。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 2k / ⭐ 22 / 由 imatrix 数据构建的 pfnet 的 plamo‑2‑translate 的 GGUF‑格式发布，基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带通过 llama.cpp 在启用 CUDA 的硬件上编译和运行的说明。
 * [GPT-OSS-Swallow-20B-RL-v0.1-gguf](https://huggingface.co/mmnga-o/GPT-OSS-Swallow-20B-RL-v0.1-gguf) - 📥 2k / ⭐ 4 / 一个 gguf‑格式转换的 GPT‑OSS‑Swallow 20B RL v0.1 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 数据构建，已准备好通过 llama.cpp 运行并支持 CUDA。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-32b-a3b-thinking-gguf) - 📥 2k / ⭐ 7 / GGUF 格式转换的 llm‑jp‑4‑32b‑a3b‑thinking，使用 TFMC 的 imatrix 数据集构建，适用于通过 llama.cpp 在支持 CUDA 的推理。
 * [RakutenAI-3.0-gguf](https://huggingface.co/mmnga-o/RakutenAI-3.0-gguf) - 📥 2k / ⭐ 5 / GGUF转换版本的 RakutenAI‑3.0，基于 imatrix 数据集构建，已准备好与 llama.cpp 一起使用以运行日本 LLMs。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/alfredplpl/llm-jp-4-32b-a3b-thinking-gguf) - 📥 1k / ⭐ 1 / 一个 4 亿参数的日本 LLM 已转换为 GGUF，保留最小化聊天模板，可与 llama‑cpp 的 llama‑completion 或 LM Studio（原名 llm‑jp/llm‑jp‑4‑32b‑a3b‑thinking）一起使用。
 * [ABEJA-Qwen3-14B-Agentic-256k-v0.1-gguf](https://huggingface.co/mmnga-o/ABEJA-Qwen3-14B-Agentic-256k-v0.1-gguf) - 📥 1k / ⭐ 2 / 已将 ABEJA‑Qwen3‑14B‑Agentic‑256k‑v0.1 转换为 GGUF 格式，使用 TFMC/imatrix‑dataset‑for‑Japanese‑LLM，准备在启用 CUDA 的 llama.cpp 上进行推理，并附带示例日语烹饪提示。
 * [Llama-3.1-Swallow-8B-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-v0.5) - 📥 1k / ⭐ 9 / Llama 3.1 Swallow v0.5 是一个拥有80亿参数的 LLM，通过在合成日语数据上持续预训练和指令微调，提升了 Meta 的 Llama 3.1 在日语语言与代码/数学推理上的表现，同时保持了英语流畅性。
 * [Ninja-v1-NSFW-gguf](https://huggingface.co/mmnga/Ninja-v1-NSFW-gguf) - 📥 1k / ⭐ 5 / 来自 Local-Novel-LLM 项目的 Ninja-v1-NSFW 模型的 gguf-格式转换，使用 imatrix 数据集训练，并已准备好使用 llama.cpp 部署。
 * [Llama-3-ELYZA-JP-8B-Heretic-i1-GGUF](https://huggingface.co/mradermacher/Llama-3-ELYZA-JP-8B-Heretic-i1-GGUF) - 📥 1k / ⭐ 1 / 仓库提供了完整的 weighted/imatrix GGUF 量化模型，用于 Llama‑3‑ELYZA‑JP‑8B‑Heretic，涵盖不同质量和尺寸等级（例如：i1‑IQ1_S、i1‑IQ2_M、i1‑Q4_K_M），可从 Hugging Face 下载，并附带与 TheBloke’s READMEs 链接的使用指导。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 1k / ⭐ 17 / 高性能的日本 SPLADE v2 通过 WebUI demo 实现稀疏向量转换和推理，使用 YAST 进行训练，提供 YASEM 嵌入，并报告 JMTEB benchmark 结果。
 * [t5-base-long](https://huggingface.co/retrieva-jp/t5-base-long) - 📥 1k / ⭐ 2 / T5 v1.1日语编码‑解码模型，在日语维基百科和 mC4/ja 上训练，使用 GEGLU 激活，dropout 关闭，更大的 d_model 但头数更少，512 令牌输入，114 令牌输出，256 批次 fp32，采用 CC‑BY‑SA 4.0 许可，商业使用需联系。
 * [umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf](https://huggingface.co/mmnga/umiyuki-Japanese-Chat-Umievo-itr001-7b-gguf) - 📥 1k / ⭐ 3 / GGUF‑converted Japanese‑Chat‑Umievo‑itr001‑7b 模型，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 中的 imatrix 数据构建，运行通过 llama.cpp。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 12 / Sarashina2.2 提供 0.5‑B、1‑B 和 3‑B 语言模型， 这些模型由 SB Intuitions 通过三阶段流水线和合成数据训练，达到了日本 QA、数学和编码的顶级成绩，同时提供的预训练权重未进行指令微调，可能产生偏见输出。
 * [DataPilot-ArrowPro-7B-RobinHood-gguf](https://huggingface.co/mmnga/DataPilot-ArrowPro-7B-RobinHood-gguf) - 📥 1k / ⭐ 2 / DataPilot-ArrowPro-7B-RobinHood‑gguf 是使用 imatrix Japanese LLM dataset 转换为 gguf 格式的 DataPilot ArrowPro‑7B‑RobinHood 模型，已准备好在 llama.cpp 进行推理。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 1M / ⭐ 32 / 聚合了2009年至2024年NicoNico Live的评论日志，总计超过150 GB，包括转移前、转移后以及实时NX‑Jikkyo捕获，提供了一个API，便于检索历史电视广播讨论。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 61k / ⭐ 7 / 使用 VOICEVOX 从 ITA、Tsukuyomi‑chan 以及 ROHAN 语料库创建的人工声数据集，包含 445,793 条 WAV 文件，总计 577 小时 51 分钟 23 秒。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 9k / ⭐ 16 / 一份日语和多语种 QA、NLI 与同义句重述数据集的目录，详细说明每个数据集的检索或问答任务及其许可（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 6k / ⭐ 9 / Cauldron‑JA 是一个日语视觉‑语言数据集，包含 44 个子数据集，使用 DeepL API 从 The Cauldron 翻译而来，可通过 HuggingFace’s datasets library 获取，并与原始数据集使用相同的许可证，prompts 在 CC‑BY‑4.0 下发布。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 6k / ⭐ 6 / Japanese Medical VQA 12M 是一个可商业使用的多模态数据集，包含超过 1200 万张日语医学图像和标题，源自 Open‑PMC‑18M，采用 Parquet/Webdataset 格式，并包含原始和日语翻译图像、增强后的标题以及使用 InternVL3.5、Qwen3‑30B 和 GPT‑oss 120B 生成的 VQA 风格问答对。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 5k / ⭐ 112 / Nemotron‑Personas‑Japan 是一个开放源代码、CC BY 4.0 许可证的高质量、合成生成的日本人物资料数据集—包含姓名、性别、年龄、背景、婚姻状况、教育、职业和地点—基于真实世界的人口统计、地理和人格分布，并采用概率图模型和 GPT‑OSS‑120B 进行工程设计，以提升多样性、降低偏见、防止模型崩溃、支持主权 AI 发展，并支持商业使用。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 4k / ⭐ 28 / FineWeb2 Edu Japanese 提供约120 million高质量教育日语文本（≈89.3 billion tokens）来自 FineWeb2，经过 DeepSeek‑API classifier（score ≥ 2.5）过滤，通过 ModernBERT‑Ja‑130M tokenized，并包含一个小-token子集（≤512 tokens）。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 3k / ⭐ 19 / JMMMU 是一个日语多模态基准，已扩大十倍至 1,320 个具有文化多样性的问题（720 个与文化无关，600 个与文化相关），由母语专家翻译，现在设有公开排行榜。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 2k / ⭐ 99 / 一个包含100个样本的日语指令微调评估数据集，包含已注释的任务——从摘要校正、数学推理到翻译、创意生成和用户意图理解——旨在对微调模型进行手动或自动的5分制评分。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 2k / ⭐ 111 / ReazonSpeech 是一个免费、FLAC 编码的日语语音语料库，附带转录，提供五种规模，从 8.5 h 到 35,000 h，可通过 Hugging Face 下载，遵循 CDLA‑Sharing‑1.0 许可证，且使用受到《日本著作权法》第30‑4条的限制。
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 2k / ⭐ 18 / JMTEB 是一个日本文本嵌入基准，包含 5 个任务（聚类、分类、STS、检索、再排序）和 28 个数据集，提供一行评估脚本，并邀请社区贡献。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 2k / ⭐ 5 / JAQKET 是一个基于维基百科的日语开放域问答数据集，提供 1.0 版包含多项选择测验题（13,061 条训练样本，271 条验证样本）以及 2.0 版仅包含需要提取答案的提问提示（2,154 条训练样本，1,164 条验证样本），旨在促进问答系统研究。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 1k / ⭐ 10 / Reazon Speech v2 Japanese dataset 在 Hugging Face 上的镜像，分发依据 CDLA-Sharing-1.0，使用受限于日本著作权法第30‑4条，包含 4,096 个 16 kHz FLAC 音频文件及对应的 TSV/CSV 格式转录文本。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 1k / ⭐ 33 / 为高效加载 Hugging Face datasets，重新结构化并重新上传 Galgame VisualNovel 数据集（OOPPEENN/5669737465666C656E63655F44617461337072657330），保留所有原始 audio/text，并提供带多种 game-subset 选项的 extraction script。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 1k / ⭐ 7 / JMedBench 是一个日语生物医学 LLM 基准，涵盖 20 个数据集，覆盖五个任务（MCQA、NER、STS 等），来源于 MedMCQA、PubMedQA、MMLU 等，每个都有自己的许可，并包含一条说明：翻译可能包含偏差，需要人工审核。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 4 / JamC‑QA 是一个双语基准，涵盖八个日本文化与知识类别的多项选择题，排行榜指标用于比较最先进模型。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 1k / ⭐ 36 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小时匿名 1,033,142 对 eroge 音频-转录配对（主要为女性，含 NSFW），MIT 许可用于学术研究。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 1k / ⭐ 89 / 一个自动翻译的日语版本的databricks‑dolly‑15k数据集，许可为CC‑BY‑SA‑3.0，最后更新于2023‑05‑11。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 995 / ⭐ 47 / 更新了 JGLUE 数据集卡与加载脚本，适用于由 Yahoo Japan 与早稻田大学创建的日语 NLP 基准，涵盖文本分类（MARC‑ja、JCoLA）、句对分类（JNLI）以及问答（JSQuAD、JCommonsenseQA），发行链接保存在 GitHub 与 Hugging Face 上。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 966 / ⭐ 3 / 日语指令数据集，具有 632,636 条多轮样本（约 6.35 B 个 token），并包含 GPT‑OSS‑120b 的推理轨迹，用于跨 135 个金融主题和 20 个通用主题的开放式、数学、写作和 MCQA 任务，旨在微调 LLM 在金融领域的推理能力。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 957 / ⭐ 24 / cc100-ja 是 cc100 数据集日语部分的集合，提供为分片的 Parquet 文件。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 956 / ⭐ 16 / Reazon Speech v2 数据集的镜像：3,674 个已使用 UVR 在 8 台 A800 GPU 上处理 10 天的去噪音频文件，由 Stardust‑minus 提供，遵循 CDLA‑Sharing‑1.0 协议，未包含转录文本。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 849 / ⭐ 5 / Japanese JaQuAD，QG‑Bench 的一个子集，提供句子级和段落级的数据，包含高亮的答案词元，用于训练日语问句生成模型，并通过 BLEU4、METEOR、ROUGE‑L、BERTScore 和 MoverScore 进行评估。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 800 / ⭐ 11 / JMMLU 是一个日语大型多任务语言理解基准（Benchmark），包括 7,536 道教师精心制作的问题，覆盖 56 个学科，包括专业医学、心理学、会计、哲学以及各种高中学科。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 781 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 数据集的 500 份样本子集，采用 CC BY 4.0 许可，用于基准测试 EvoVLM‑JP‑v1‑7B。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 742 / ⭐ 40 / 一个用户友好、去重的 CSV 数据集，包含 Aozora Bunko 的公有域日语文本，使用 globis‑org/aozorabunko‑extractor 处理，并已清理以适用于现代日语机器学习。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 727 / ⭐ 13 / EDINET‑Bench 是一个日本金融基准，用来评估 LLMs 在诸如会计欺诈检测、盈利预测和行业预测等任务，使用十年的 EDINET‑API 披露报告，提供构建和评估代码，并将数据集重新许可为 PDL 1.0。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 661 / ⭐ 133 / Japanese Anime Speech Dataset V2 提供 292,637 条已清洗的音频-文本对——约 397.5 小时的 SFW 内容和 52.4 小时的 NSFW 内容——以 128‑kbps MP3 文件形式按安全级别划分，专为训练自动语音识别模型而设计。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 636 / ⭐ 6 / Japanese XL‑Sum subset 通过 PaLM‑2 15-gram 重叠过滤，包含 4,215 训练样本，758 验证样本和 766 测试样本。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 614 / ⭐ 2 / 包含匿名 2ch.sc/2ch.net 帖子的极大压缩 JSON‑Lines 数据集，包括帖子 IDs、标题、板块与地区信息、回复计数，以及完整帖子元数据（作者、邮件、日期、内容）。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 586 / ⭐ 5 / STAIR‑Captions，发布于2017年，提供820,310条日语字幕，用于字幕生成、多模态检索和图像生成，并配有详细注释、元数据以及Creative Commons BY‑4.0 license。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 565 / ⭐ 4 / 提供了一个日语搜索/问答数据集，其中包含按查询计算的分数，这些分数是由五个多语言/日语重排序器（例如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）计算的，数据集包括每个查询约200个正例和负例文档的平均分数。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 562 / ⭐ 141 / 用于微调 LLMs（如 LoRA）的日语指令聊天数据集，包含 9 M+ 样本，最近已更新，删除授权的 Alpaca 数据，并清理了 Wikipedia 和 ALT 输出，采用 CC‑BY‑SA 4.0 许可证发布。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 560 / ⭐ 44 / Galgame_Speech_ASR_16kHz 是一个 16 kHz 的 ASR 数据集，包含 3.75 百万对（≈5,354 小时），源自 Galgame_Dataset，遵循 GPL v3.0，禁止商业使用，并要求任何训练的模型必须开源（可选引证）。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 559 / ⭐ 11 / Range3/wiki40b‑ja 托管了 wiki40b 数据集的日语子集，作为由 Python 数据处理管道生成的三个 Parquet 文件。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 500 / ⭐ 22 / 一套来自日本网络的5600万份文档、110 B字符与2.49亿张图片，用于训练大型视觉语言模型——提供momiji_generator用于数据填充，OBELICS‑style可视化，以及示例模型（Heron‑NVILA‑Lite）。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 480 / ⭐ 8 / JMMMU‑Pro 是一个通过 Vibe Construction 构建的日语多模态基准——结合生成建模和人工验证——用于生成低成本、高质量的 image‑QA 数据，以揭示开源 LMMs 的缺陷并引领未来 VQA 研究。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 477 / ⭐ 32 / 一个时长为409小时的日本 eroge 语音数据集，使用 2-pass loudnorm（‑23 LUFS，‑1 dB 峰值，11 LRA）处理，已由 litagin/anime-whisper 转录、匿名化，存储为 WebDataset（FLAC、JSON、TXT），主要包含女性声音，可能存在 AI 转录错误，并采用 MIT 许可证用于学术研究。
 * [AItuber-Personas-Japan](https://huggingface.co/datasets/DataPilot/AItuber-Personas-Japan) - 📥 459 / ⭐ 27 / 一套合成的195条 AI‑VTuber 角色数据集，使用 Kimi‑K2.5 通过 SDG‑LOOM 流水线生成，提供概念文档、系统提示和主题列表，角色由六个种子参数（流派、个性、年龄、性别表达、视觉动机、语音风格）定义，覆盖约25个流派和20种个性类型，许可为 ODC‑BY。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 449 / ⭐ 2 / JAMMEval 是七个日本 VQA 数据集的精炼基准，经过两轮人工注释以消除歧义和非视觉问题，能够为多模态日本任务提供对视觉‑语言模型的可靠评估。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 433 / ⭐ 8 / Rakuda 提供 40 道日语问题——开放式的历史、社会与政府问题，以及针对地理的特定问题——用于对日本 AI 助手进行基准测试，类似于 vicuna‑eval，并且可以使用 `datasets.load_dataset` 加载。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 433 / ⭐ 4 / 来自 Fate/Stay Night 的角色 “Emilia” 的对话和背景故事数据集，格式化用于训练和评估会话语言模型。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 414 / ⭐ 11 / 一个高质量的合成日语数学题数据集，具有经过验证的思考链推理，采用 Qwen2‑7B‑Instruct 翻译 PRM800K 和 GSM8K 并进行正确性筛选后构建，可通过 Hugging Face 数据集库获取。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 411 / ⭐ 148 / 日本动漫语音数据集提供73,004对音频-文本（总计110小时，已从V1升级至V5），用于提升ASR模型，例如OpenAI的Whisper，按开放许可证提供给所有使用，欢迎署名。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 375 / ⭐ 4 / JFWIR 是一份从 fine‑web 教育爬虫构建的 6400 万对日语信息检索数据集，提供每个文档七种查询类型、难负样本，并在基准测试中明显优于以往基线。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 370 / ⭐ 6 / Range3 的 wikipedia‑ja‑20230101 仓库提供只包含日语维基百科文本的 Parquet 文件，这些文件是从完整维基百科数据集中提取的，并使用 Python 代码生成。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 349 / ⭐ 16 / Japanese Alpaca 数据，源自 masa3141 的 Japanese Alpaca‑LoRA 工作，并引用原始仓库以获取更多细节。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 349 / ⭐ 2 / 日文维基百科文本改写所生成的LLM查询和答案数据集，未使用受许可限制的模型构建，且在CC‑BY‑SA 4.0下发布。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 335 / ⭐ 13 / ‘wikipedia-ja-20230720’ 日本维基百科快照的数据集卡。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 304 / ⭐ 51 / AnswerCarefully Dataset提供日语和多语种数据，用于商业或非商业LLM安全增强，禁止任何其他用途——包括安全规避——允许带署名的衍生作品，并声明不承担因伤害或服务变更导致的责任。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 298 / ⭐ 10 / JA‑Multi‑Image‑VQA 是一个包含 39 张图像、55 道题目的数据集，其中包含手工制作的日语问答，适用于多图像 VQA，通过 load_dataset 访问，文本部分采用 Apache 2.0 许可（图像受限）。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 284 / ⭐ 33 / Syosetu711K 是一个约 711,700 本小说的日本数据集，采自 2023 年 3 月 26‑27 日从 小説家になろう 抓取，提供全文及元数据（标题、作者、NCode、简介等），用于无监督文本生成和分类任务。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 271 / ⭐ 3 / 包含问题、答案以及逐步推导链接至 Wikipedia 文章的日本 Explainable Multi-hop Question Answering 数据集，已更新推导格式并发布多个版本。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 269 / ⭐ 6 / 日本 MC4 数据集卡 (mc4-ja)
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 261 / ⭐ 15 / 一个用于测试角色‑LLMs的简单 Zundamon 角色设定数据集——由线上来源和管理数据编制——以 zmnjp.jsonl 和 zmn.jsonl 格式提供，并在指定许可下发布。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 256 / ⭐ 12 / LLM‑jp 提供了一个日语指令调优数据集，该数据集是 DeepL 翻译自 oasst2 的英文子集（来自 kunishou/oasst2‑135k‑ja），并由 Kiyomaru 和 Kodama 编译。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 247 / ⭐ 17 / oasst1‑21k‑ja 是由 DeepL 从英文 OASST1 子集派生的日语指令调优数据集，透过日本 LLM‑jp 合作项目创建；请联系 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 和 Okamoto。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 241 / ⭐ 2 / JCommonsenseQA 是一份日语的多项选择常识推理数据集——CommonsenseQA 的改编版本——其授权为 CC BY‑SA 4.0，并以 doi:10.5715/jnlp.30.63 引用。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 239 / ⭐ 7 / JHumanEval 是 HumanEval 基准的人工翻译日语版本，提供 164 个 Python 编程问题，配有并行的英文和日文注释，用于评估日语 LLM 的代码生成，同时保留原始英文错误。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 232 / ⭐ 3 / A 2010 Japanese Web Corpus, uploaded to HuggingFace and licensed for research per the 2009 copyright reform, 包含来自基于形态学的解析和转换脚本的自动标点化文本。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 228 / ⭐ 10 / 一份将 llm‑jp‑corpus‑v3 的 kaken 子集译为日英的日英平行语料库，使用 Qwen/Qwen2.5‑32B‑Instruct，包含自定义翻译列，并在 CC‑BY‑4.0 许可下授权。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 218 / ⭐ 3 / BBH‑ja提供了BIG‑Bench Hard数据集的日语翻译，提供JSON‑L（输入、正确目标）格式的评估问题以及使用PLaMo模型翻译的YAML（输入、目标）格式的Chain‑of‑Thought提示。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 215 / ⭐ 2 / 用于扩展受数据限制的日语LLM的预训练语料库，包含有机日语/英语网络数据集（9B-令牌 JA-WEB-9B，63B-令牌 EN-WEB-63B/JA-WEB-63B）以及合成集（Qwen3-14B，JA-PARAPHRASE-63B，JA-INSTRUCT-63B，JA-TRANSLATE-63B），这些被用于 EACL 2026 研究。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 213 / ⭐ 2 / Hugging Face 镜像的 ABEJA‑CC‑JA dataset 来自 AWS Open Data registry，细节见 ABEJA 的 tech‑blog entry。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 208 / ⭐ 21 / AI生成的动漫插图，使用英文提示，并基于Phi‑3 Vision的字幕（英文和日文），已发布到公共领域，供免费使用。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 197 / ⭐ 14 / 一个采用 CC‑BY‑SA 3.0 许可的日语命名实体抽取数据集，来源于 Wikipedia，托管在 https://github.com/stockmarkteam/ner-wikipedia-dataset/，由 Stockmark Inc. 开发。
 * [MGSM_ja](https://huggingface.co/datasets/sbintuitions/MGSM_ja) - 📥 190 / ⭐ 2 / 一个可公开复现的 MGSM 多语言链式思维数据集的日语子集，在 Hugging Face 上以 Creative Commons BY‑SA 4.0 许可证克隆，包含问题、答案、答案编号和方程式解答字段。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 187 / ⭐ 16 / 一个 1.9 亿对 JSONL 数据集，用于日语假名到汉字转换，为 zenz‑v2.5 medium、small 和 xsmall 模型提供动力，并包含 AJIMEE‑Bench 评估语料库。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 186 / ⭐ 27 / WRIME 数据集是一个包含 42,200 条帖子的日本语集合，帖子已为作者、三位读者及其平均值标注了 Plutchik 的八种情感，结构为 40k 训练集、1.2k 验证集和 2k 测试集，用于情感分析任务。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 186 / ⭐ 9 / 面向 llm‑book/wrime‑sentiment 的数据集卡，提供从 WRIME 派生的二元日语情感分析集，依据 Avg. Readers_Sentiment 标记为正向或负向（可选包含中性案例），用于《大型语言模型导论》一书的示例数据。
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 184 / ⭐ 2 / Makise Kurisu VN 对话从视频中使用 Whisper Large‑V2 转录，用 pydub 分割为片段，未清理，可能存在错误，旨在用于 TTS 模型训练，且不属于作者所有。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 183 / ⭐ 3 / 日语维基百科句子被转换为各种嵌入和 FAISS 索引，提供 Hugging Face Space 演示、转换脚本，以及对搜索、问答和 OpenAI text-embedding-3-small 在 RAG 中的评估；嵌入模型为 OpenAI‑licensed，其他为 CC‑BY‑SA‑4.0。
 * [image-text-pairs-ja-cc0-2](https://huggingface.co/datasets/alfredplpl/image-text-pairs-ja-cc0-2) - 📥 181 / ⭐ 2 / 一份 CC‑0 日本文本‑图像数据集，使用 GPT‑OSS‑20B 构建，基于约 80 k 单词/短句，生成 1 M 和 100 k 图像，使用 Pillow/Python 并采用 Noto Sans JP 字体。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 174 / ⭐ 18 / 包含草薙寧々（来源 CV Machico）的 *Project Sekai* 歌声轨的部分数据集，附带 nene_org.txt 标注文件，计划扩充并标准化数据，并呼吁用户点星此 repo、分享想法、加入 QQ 群以获取完整收藏。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 171 / ⭐ 17 / Galgame_Speech_SER_16kHz 是一份 3.7 百万文件（5,353 小时，104 GB）的情感语音数据集，源自 Galgame_Speech_ASR_16kHz，由本地 LLM 注释，按 GNU GPL v3.0 发行，禁止商业使用，并要求基于它训练的模型保持开源且无需强制引用。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 169 / ⭐ 5 / 该仓库托管了一位81岁日本女性的语音语料库——原始与降噪的WAV文件、音素和假名标签——可通过Google Drive链接获取，免费用于研究和商业语音合成，需要署名，但禁止直接文件链接或色情用途。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 168 / ⭐ 14 / 180 万条日语翻译条目，来源于 OpenMathInstruct‑1，并由 GSM8K 与 MATH benchmark 问题组成，配合已验证的 Mixtral‑8x7B 生成的合成解答，已在 NVIDIA 的许可下商业提供。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 165 / ⭐ 18 / Databricks‑dolly‑15k‑ja 数据集是 DeepL 翻译的日本语版 databricks‑dolly‑15k，用于指令调优，由日本 LLM‑jp 项目创建，并由 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 和 Takumi Okamoto 撰写。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 165 / ⭐ 6 / 将日语数据集转换为适合 SentenceTransformers 的列，依据来自多个 HuggingFace 来源的 Rerank 分数（正样本 ≥0.7，负样本 ≤0.3）进行过滤，以支持对比学习，同时尊重原始许可证。
 * [japanese-stackexchange](https://huggingface.co/datasets/p1atdev/japanese-stackexchange) - 📥 164 / ⭐ 3 / 一个英文的 Japanese Stack Exchange QA 数据集，已从该站点的转储中提取并处理，提供默认和扁平化子集，可通过 Hugging Face datasets 加载，并遵循 CC BY‑SA 4.0 许可证。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 153 / ⭐ 12 / JaQuAD 是 2022 年的日语 QA 数据集，包含 39,696 对 SQuAD‑style 的抽取式问题‑答案对，取自 Wikipedia，文件总大小 73.2 MB。使用 BERT‑Japanese 微调时，获得 78.92 % F1（63.38 % EM）。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 152 / ⭐ 7 / Livedoor News Corpus 提供了一个日语新闻文章数据集，划分为 5,894 条训练样本、737 条验证样本和 736 条测试样本，已清除 HTML 标签，并在 Creative Commons Attribution‑NoDerivs 许可证下发布。
 * [callhome-ja-plus](https://huggingface.co/datasets/ayousanz/callhome-ja-plus) - 📥 143 / ⭐ 2 / 将日本 Callhome 语音文件转换为 WAV，并附带 JSON 格式的元数据数组和 RTMM 说话人标签文件以供评估。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 140 / ⭐ 9 / 一份包含 2,300 万本个人收集的日本网络小说的数据库，总计 80.85 亿字符，仅供合法的机器学习使用，并需详细的访问请求。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 137 / ⭐ 15 / 用于《大型语言模型简介》一书的 JGLUE 数据集数据卡，来源于原始仓库，代码采用 CC BY‑SA 4.0 许可证，数据按发行者的许可协议，引用 Kurihara & Kawahara（日本语），并基于 Shunsuke Kitada 的仓库构建。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 135 / ⭐ 3 / 本数据集说明书用于本书《Introduction to Large‑Scale LLM II》中的 ja‑vicuna‑qa‑benchmark，并由 llm‑jp‑eval 创建，供跨数据集日语 LLM 评估使用（Apache 2.0）。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 134 / ⭐ 42 / 将LLM按其把日语视觉小说准确翻译成英文的能力进行排名，VNTL 排行榜使用与256份参考翻译的余弦相似度（也报告了 chrF 但未进行排名），并报告初步结果，优于 Sugoi Translator、Google Translate、Papago 和 Alibaba Translate 等工具。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 132 / ⭐ 7 / llm‑jp‑instructions 是一个手工整理的日语指令数据集（v1.0），提供训练、验证和测试拆分，可通过 load_dataset 访问。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 125 / ⭐ 5 / 来自 joujiboi/japanese‑anime‑speech‑v2 数据集的子集。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 124 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) 提供了一个多分类 QA 数据集——涵盖 Integration、Reasoning、Logical、Table 和 Abstention——旨在评估日本 RAG 生成器，采用人工努力和 GPT‑4.1 构建，并在 CC BY‑SA 4.0 许可下发布。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 123 / ⭐ 21 / 用于日英文本简化和翻译的 SNOW T15/T23 日语简化语料库数据卡，包含 50 k 条手工对齐的原文、简化日语（≤2 k‑词汇量）和英语翻译记录，以及 35 k 条扩展集。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 123 / ⭐ 3 / 一份包含 64,139 条标注有生物性别的日语姓名的数据集，呈现为汉字、假名和平罗马字，其 44.9k 训练集、6.41k 验证集和 12.8k 测试集划分已在 ISDA’23 被接受。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 117 / ⭐ 9 / JSICK 是从 SICK 翻译成日语的 NLI/STS 数据集，提供了一套压力测试，利用多个转换过的 sentence-pair subsets 来探测 word‑order 和 case‑particle 的处理，以支持多语言组合推理的研究。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 117 / ⭐ 15 / Hachi‑Alpaca 提供基于 Stanford Alpaca 的日语合成数据，经过 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 细化和验证，并通过 Deepinfra 使用，同时提供已通过模型质量检查的 “_cleaned” 版本。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 117 / ⭐ 5 / J‑HARD‑TTS‑Eval 对日语自回归 TTS 模型在短序列稳定性、重复、韵律和连贯性等失败方面进行基准测试，提供带有提示音频和文本的数据集，可通过 Hugging Face 加载。
 * [oasst1-chat-44k-ja](https://huggingface.co/datasets/kunishou/oasst1-chat-44k-ja) - 📥 112 / ⭐ 10 / 一个基于 ShareGPT 格式的多轮聊天数据集，来源于 oasst1‑89k‑ja，用于微调，需大量计算资源；请参阅随附的文章和 GitHub/HuggingFace 链接。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 111 / ⭐ 3 / 一个量化语音与文本输入在语音语言模型之间智能差距的数据集，由从 Elyza‑tasks‑100、M‑IFEval 与 JamC‑QA 基准生成的音频组成，分为四个子集，文本采用 CC‑BY‑SA 4.0 许可，音频仅限非商业用途且不可再分发。
 * [mqa-ja](https://huggingface.co/datasets/hpprc/mqa-ja) - 📥 110 / ⭐ 6 / 已去重、NFKC‑标准化的 mQA query–passage pairs，pos_ids/neg_ids 映射到 collection 索引，用于通过 collection[pos_id] 直接检索，并按原始数据集的许可条款授权。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 103 / ⭐ 19 / 一个用于评估 Retrieval‑Augmented Generation（RAG）的日语 QA 数据集，由 JAQKET 问题和 Wikipedia 段落以及金标准检索相关性标签构建，并在 HuggingFace 和 GitHub 上发布，主要依据 nDCG@10 评分。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 102 / ⭐ 5 / JSNLI 是由 KUROHASHI‑CHU‑MURAWAKI LAB 发布的 SNLI 自然语言推断基准的日语翻译，提供 TSV 格式的前提‑假设‑标签三元组（由 JUMAN++ 进行形态学分割），既有未过滤版又有高精度过滤版训练集（约 548 k/533 k 对），3,916 条评估对，采用 CC BY‑SA 4.0 进行分发。
