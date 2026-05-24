# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专门收录日语NLP相关的Python库、LLM、词典和语料库资源的精选列表。
本页面列出了Hugging Face上可用的日语NLP专用模型和数据集。目前包含199个模型和208个数据集。

_更新于2026年5月24日_

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)

## Contents
 * [Ranking](#Ranking)
   * [Models](#models-ranking)
   * [Datasets](#datasets-ranking)
 * [Models](#Models)
   * [text-generation](#text-generation)
   * [fill-mask](#fill-mask)
   * [sentence-similarity](#sentence-similarity)
   * [feature-extraction](#feature-extraction)
   * [automatic-speech-recognition](#automatic-speech-recognition)
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

| # | 模型名称 | Downloads | Likes | 类别 |
|---|-------|-----------|-------|----------|
| 1 | [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) | 📥 1M | ⭐ 57 | automatic-speech-recognition |
| 2 | [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) | 📥 894k | ⭐ 14 | translation |
| 3 | [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) | 📥 394k | ⭐ 74 | sentence-similarity |
| 4 | [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) | 📥 354k | ⭐ 76 | fill-mask |
| 5 | [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) | 📥 321k | ⭐ 41 | fill-mask |
| 6 | [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) | 📥 318k | ⭐ 11 | feature-extraction |
| 7 | [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) | 📥 295k | ⭐ 171 | image-to-text |
| 8 | [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) | 📥 230k | ⭐ 5 | text-ranking |
| 9 | [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) | 📥 229k | ⭐ 21 | text-generation |
| 10 | [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) | 📥 213k | ⭐ 100 | automatic-speech-recognition |
| 11 | [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) | 📥 212k | ⭐ 11 | translation |
| 12 | [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) | 📥 158k | ⭐ 39 | fill-mask |
| 13 | [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) | 📥 155k | ⭐ 136 | text-generation |
| 14 | [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) | 📥 147k | ⭐ 15 | text-generation |
| 15 | [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) | 📥 128k | ⭐ 11 | others |
| 16 | [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) | 📥 126k | ⭐ 9 | sentence-similarity |
| 17 | [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) | 📥 115k | ⭐ 8 | fill-mask |
| 18 | [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) | 📥 94k | ⭐ 59 | text-generation |
| 19 | [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) | 📥 72k | ⭐ 14 | others |
| 20 | [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) | 📥 66k | ⭐ 6 | fill-mask |

### Datasets-ranking

| # | 数据集名称 | Downloads | Likes |
|---|---------|-----------|-------|
| 1 | [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) | 📥 3M | ⭐ 47 |
| 2 | [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) | 📥 19k | ⭐ 9 |
| 3 | [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) | 📥 13k | ⭐ 4 |
| 4 | [WAON](https://huggingface.co/datasets/speed/WAON) | 📥 7k | ⭐ 2 |
| 5 | [emb](https://huggingface.co/datasets/hpprc/emb) | 📥 6k | ⭐ 16 |
| 6 | [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) | 📥 5k | ⭐ 7 |
| 7 | [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) | 📥 4k | ⭐ 6 |
| 8 | [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) | 📥 4k | ⭐ 18 |
| 9 | [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) | 📥 4k | ⭐ 6 |
| 10 | [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) | 📥 4k | ⭐ 117 |
| 11 | [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) | 📥 4k | ⭐ 140 |
| 12 | [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) | 📥 3k | ⭐ 5 |
| 13 | [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) | 📥 3k | ⭐ 29 |
| 14 | [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) | 📥 3k | ⭐ 99 |
| 15 | [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) | 📥 3k | ⭐ 43 |
| 16 | [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) | 📥 3k | ⭐ 4 |
| 17 | [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) | 📥 3k | ⭐ 10 |
| 18 | [jawiki](https://huggingface.co/datasets/hpprc/jawiki) | 📥 2k | ⭐ 18 |
| 19 | [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) | 📥 2k | ⭐ 2 |
| 20 | [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) | 📥 2k | ⭐ 5 |

## Models
### text-generation
 * [open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - 📥 229k / ⭐ 21 / OpenCALM 是 CyberAgent, Inc. 在 CC‑BY‑SA 4.0 许可证下发布的一套仅解码的日本 transformer 语言模型（160 M–6.8 B 参数），训练于 Japanese Wikipedia 和 Common Crawl，并可通过 Hugging Face’s torch‑transformers 使用。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2-Japanese) - 📥 155k / ⭐ 136 / 9亿参数的日语优化LLM，NVIDIA Nemotron‑Nano‑9B‑v2‑Japanese，训练数据截至2024年9月，采用混合 Mamba‑2/MLP/4‑层注意力架构，已在 Nemotron‑Personas‑Japan 工具调用数据集上微调，可选地在生成最终答案前生成可控的推理轨迹，且可商用。
 * [japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 📥 147k / ⭐ 15 / 一个 12 层、768 隐藏层的日语 GPT‑NeoX 模型，训练数据为 CC‑100、C4 以及 Wikipedia，兼容 Huggingface，并配备可选的玩具前缀调优权重，能强制每个句子末尾以笑脸表情符号结束。
 * [gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - 📥 94k / ⭐ 59 / 一款由 ABEJA Inc. 使用日语 CC‑100 和 OSCAR 训练的 2.7B 参数日语 GPT‑NeoX 模型，可通过 Hugging Face Transformers 管道或 PyTorch 使用，按 MIT 许可证发布。
 * [karasu-1.1B](https://huggingface.co/lightblue/karasu-1.1B) - 📥 51k / ⭐ 7 / 预训练的 TinyLlama 在日语（≈50 k 步），基于约3 B OSCAR/mC4 tokens，可通过 HuggingFace Transformers 或 VLLM 使用，由 Peter Devine、Sho Higuchi、Yuuki Yamanaka、Atom Sonoda、Shunichi Taniguchi、Tomioka Wataru 和 Renju Aoki 创建。
 * [llm-jp-3-150m](https://huggingface.co/llm-jp/llm-jp-3-150m) - 📥 40k / ⭐ 6 / LLM‑jp‑3‑150m——来自国立信息学研究所LLM研发中心的150 M参数日语语言模型——以 Hugging Face Transformers 格式发布，需要 torch ≥ 2.3.0、transformers ≥ 4.40.1、accelerate ≥ 0.29.3、flash‑attn ≥ 2.5.8，并且在日本维基百科、Common Crawl、WARP/PDF、WARP/HTML 和 Kaken 数据上使用 unigram byte‑fallback tokenizer 进行预训练。
 * [shisa-gamma-7b-v1](https://huggingface.co/augmxnt/shisa-gamma-7b-v1) - 📥 33k / ⭐ 18 / 使用 Shisa 7B 数据，微调了日语 Stable LM Base Gamma 7B，在 JA MT‑Bench 上取得了强劲的表现。
 * [llm-jp-4-8b-thinking](https://huggingface.co/llm-jp/llm-jp-4-8b-thinking) - 📥 16k / ⭐ 38 / 提供来自 NII 的 8 B 参数 LLM‑jp‑4‑8b‑thinking 日语语言模型，使用 pre‑/mid‑training 训练并通过 SFT/DPO 对齐，已准备好与 torch‑transformers 一起使用，并附有详细的教程说明。
 * [llm-jp-4-8b-instruct](https://huggingface.co/llm-jp/llm-jp-4-8b-instruct) - 📥 13k / ⭐ 7 / llm‑jp‑4‑8b‑instruct 是 NII 的 LLM‑jp‑4 系列 4.1 B 参数的日语 LLM，先在大型语料库上预训练，随后仅使用监督指令数据进行微调（不使用 DPO/REINFORCE），并附带类似食谱的使用指南和 byte‑fallback unigram tokenizer。
 * [Mistral-Nemo-Japanese-Instruct-2408](https://huggingface.co/cyberagent/Mistral-Nemo-Japanese-Instruct-2408) - 📥 11k / ⭐ 48 / 一款日本持续预训练的 Mistral‑Nemo 模型（Mistral‑Nemo‑Japanese‑Instruct‑2408），基于 mistralai/Mistral‑Nemo‑Instruct‑2407 构建，可通过 transformers 使用设备映射和 ChatML 提示进行使用，已由 Ryosuke Ishigami 以 Apache‑2.0 许可证发布。
 * [Llama-3-Swallow-8B-Instruct-v0.1](https://huggingface.co/tokyotech-llm/Llama-3-Swallow-8B-Instruct-v0.1) - 📥 11k / ⭐ 21 / Llama3 Swallow 是 Meta Llama 3 系列的日语增强版本，于 2024 年 7 月 1 日发布，提供 8B 与 70B 版本的 Instruct 与 chat 模式，已在 Megatron‑LM 上使用 SFT 与 Chat Vector 进行微调，并在关键的日语 NLP 任务上进行了基准测试。
 * [Llama-3-70B-japanese-suzume-vector-v0.1](https://huggingface.co/mmnga/Llama-3-70B-japanese-suzume-vector-v0.1) - 📥 8k / ⭐ 4 / 实验性日语模型通过使用聊天向量方法提取 lightblue/suzume‑llama‑3‑8B‑japanese 与 Meta‑Llama‑3‑8B‑Instruct 之间的差异创建，然后上采样并应用于 Meta‑Llama‑3‑70B‑Instruct，显示出变化不大，并计划未来扩大规模。
 * [Gemma-2-Llama-Swallow-9b-pt-v0.1](https://huggingface.co/tokyotech-llm/Gemma-2-Llama-Swallow-9b-pt-v0.1) - 📥 8k / ⭐ 1 / 日本增强、指令调优的 Gemma‑2 模型，基于 Llama（2b/9b/27b 预训练和指令版本），于 2025 年 5 月 19 日发布，可通过 HuggingFace 和 Swallow 团队网站获取。
 * [japanese-stablelm-instruct-gamma-7B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-gamma-7B-GGUF) - 📥 8k / ⭐ 10 / 仓库提供 GGUF 格式、量化的模型文件，适用于 Stability AI 的日本版 StableLM Instruct Gamma 7B，由 Massed Compute 硬件创建，并且是 TheBloke 的 a16z‑资助 LLM 工作的一部分。
 * [Llama-3.1-Swallow-8B-Instruct-v0.3](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3) - 📥 8k / ⭐ 24 / Llama 3.1 Swallow 是一系列日语增强的 8B/70B Llama 3.1 模型，通过持续预训练和日语特定指令微调训练，最新的 8B‑Instruct‑v0.3 在日语 MT‑Bench 上取得了最先进的结果。
 * [Llama-3-ELYZA-JP-8B](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B) - 📥 7k / ⭐ 148 / Llama‑3‑ELYZA‑JP‑8B 是由 ELYZA 开发的、经过日语增强的 80 亿参数 Llama 3 模型，在 Meta‑Llama‑3‑8B‑Instruct 上针对日语微调。
 * [japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - 📥 7k / ⭐ 85 / Rinna 的 24 层、1024 隐藏单元的日语 GPT‑2‑medium 模型，基于 CC‑100 和维基百科训练，采用 SentencePiece 分词，已在 rinna/japanese‑pretrained‑models 仓库公开（MIT 许可证，2021 年 4 月 7 日发布，2021 年 8 月 25 日更新）。
 * [Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF](https://huggingface.co/k0ndra/Qwen3.6-35B-A3B-uncensored-heretic-ja-imatrix-GGUF) - 📥 5k / ⭐ 1 / 针对日语的 imatrix GGUF 量化版本，应用于已被消融的 Qwen3.6‑35B‑A3B‑uncensored‑heretic 模型，并用日语文本校准以提升日语生成质量，但安全过滤器显著减弱。
 * [japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - 📥 5k / ⭐ 27 / rinna 的日语 GPT‑2 small 是一个 12 层、768 维隐藏层的 Transformer，训练于日语 CC‑100 和 Wikipedia，使用 SentencePiece 进行分词，发布于 2021 年 8 月 25 日，遵循 MIT 协议（Hugging Face: rinna/japanese‑gpt2‑small，参见 https://arxiv.org/abs/2404.01657）。
 * [llm-jp-4-8b-base](https://huggingface.co/llm-jp/llm-jp-4-8b-base) - 📥 5k / ⭐ 6 / 一个存储库，托管来自国立信息研究所LLM研发中心的8.6 B参数llm‑jp‑4‑8b‑base transformer，采用预训练和中间训练，随后进行监督微调和直接偏好优化（不使用强化学习），并提供PyTorch‑transformers使用指南。
 * [japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - 📥 4k / ⭐ 108 / 一款 1.3‑B‑parameter、24‑layer transformer GPT‑1B，使用 Japanese C4、CC‑100 和 Wikipedia 进行训练，于 2022 年 1 月 26 日由 rinna Co. 发布，并在 MIT license 下公开。
 * [japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 📥 3k / ⭐ 16 / 一个6层、512隐藏单元的Transformer，称为Japanese GPT‑2 xSmall，在Japanese CC‑100和Wikipedia上使用SentencePiece分词训练，于2021年8月25日以MIT许可发布，并托管在Hugging Face（rinna/japanese‑gpt2‑xsmall）上，在arXiv 2404.01657中被引用。
 * [llm-jp-3.1-1.8b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b-instruct4) - 📥 3k / ⭐ 20 / 提供 1.8 B 参数 llm‑jp‑3.1‑1.8b‑instruct4 日本指令微调模型，来自 NII，兼容 Hugging Face Transformers 和 Torch ≥ 2.3.0，包括预训练和微调检查点以及使用示例.
 * [llm-jp-4-32b-a3b-thinking](https://huggingface.co/llm-jp/llm-jp-4-32b-a3b-thinking) - 📥 3k / ⭐ 29 / 32亿参数的日语 Transformer LLM（llm‑jp‑4‑32b‑a3b‑thinking）来自国立信息学研究所，预训练和校准通过有监督微调和直接偏好优化完成——不使用强化学习——使用unigram byte‑fallback tokenizer。
 * [sarashina2.2-0.5b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-0.5b-instruct-v0.1) - 📥 3k / ⭐ 15 / SB Intuitions的 Sarashina2.2‑0.5B instruct v0.1 是一个拥有5亿参数的日语自回归模型，在日语和英语 MT 基准上表现良好，并已准备好通过 torch‑transformers 加载。
 * [llm-jp-3-1.8b](https://huggingface.co/llm-jp/llm-jp-3-1.8b) - 📥 3k / ⭐ 16 / 来自 NII 研发中心的日本大型语言模型集合（1.8 b 至 172 b beta1，含 instruct 版本），以 Hugging Face Transformers 格式打包，并在混合日语、英语与网络语料库（总计>1万亿个标记）上预训练。需要 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29 以及 flash‑attn ≥ 2.5。
 * [TinySwallow-1.5B-Instruct](https://huggingface.co/SakanaAI/TinySwallow-1.5B-Instruct) - 📥 3k / ⭐ 57 / TinySwallow‑1.5B‑Instruct 是一个 1.5 B 的日语指令调优自回归语言模型，使用 TAID 从 Qwen2.5‑32B‑Instruct 进行蒸馏，供研究用途。
 * [GPT-OSS-Swallow-20B-RL-v0.1](https://huggingface.co/tokyotech-llm/GPT-OSS-Swallow-20B-RL-v0.1) - 📥 3k / ⭐ 20 / GPT‑OSS‑Swallow v0.1 提供 20B 和 120B 双语日英 LLM，通过 CPT、SFT 和 RLVR 训练，能够在数学和编码任务上与 GPT‑OSS 匹配或超越，于 2026 年 2 月发布，包含四种 SFT/RL 变体，并将推出量化版本。
 * [sarashina2.2-3b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1) - 📥 3k / ⭐ 37 / 提供了一款来自 SB Intuitions 的自回归式日语语言模型 (sarashina2.2‑3B‑instruct‑v0.1)，已与其他模型进行基准测试，并附示例使用脚本，且安全训练有限。
 * [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) - 📥 3k / ⭐ 146 / LFM2.5‑1.2B‑JP 是一款针对日语优化的聊天模型，在日语知识与指令遵循方面优于 LFM2，支持使用 LoRA 进行微调，支持通过 Transformers、vLLM 和 llama.cpp 进行推理，取得 50.7 JMMLU、58.1 M‑IFEval 与 56.0 GSM8K 分数。
 * [Qwen3-Swallow-8B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-8B-RL-v0.2) - 📥 3k / ⭐ 9 / Qwen3‑Swallow v0.2 提供了通过 CPT、SFT 和 RLVR 训练的日英 LLM（30B‑A3B 和 32B），保持了强大的数学、编码和推理能力，已发布九个模型以及 AWQ 量化版本。
 * [Qwen3-Swallow-32B-RL-v0.2](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2) - 📥 3k / ⭐ 1 / Qwen3‑Swallow v0.2 提供了 30‑B 和 32‑B 双语日英 LLM，采用 CPT、SFT 与 RLVR 训练，提升日语准确性、翻译、数学与编码能力，以匹配或超越原始 Qwen3，提供九个模型（CPT、SFT、RL）和 AWQ‑quantized 版本，同时发布 GPT‑OSS‑Swallow。
 * [gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - 📥 2k / ⭐ 18 / 由 ABEJA, Inc. 在 Japanese CC‑100、Wikipedia 与 OSCAR 上训练的大型日语 GPT‑2 模型，使用 sentencepiece 进行分词，可通过 Hugging Face transformers 在 PyTorch 或 TensorFlow 上使用，依据 MIT license。
 * [TinySwallow-1.5B](https://huggingface.co/SakanaAI/TinySwallow-1.5B) - 📥 2k / ⭐ 35 / TinySwallow‑1.5B 是 Sakana AI 与 Swallow Team 开发的紧凑型日语指令遵循语言模型，采用 Qwen2.5‑32B‑Instruct 的 TAID 蒸馏，并在日语文本上进一步预训练，且仅以 Apache 2.0 许可证供研究使用。
 * [Swallow-7b-hf](https://huggingface.co/tokyotech-llm/Swallow-7b-hf) - 📥 2k / ⭐ 17 / TokyoTech‑LLM 仓库提供了经过日本数据增强的 Swallow Llama‑2 系列 LLaMA‑2 模型，涵盖 7B、13B 和 70B 变体，其中包括 instruction‑tuned、NVE‑tuned 以及自 2023 年 12 月以来发布的 7B Plus 版本。
 * [ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - 📥 2k / ⭐ 23 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2‑7B 的 6.27‑B‑parameter Japanese extension，进一步预训练以适用于日语语言任务，并提供 base、instruct、fast 和 fast‑instruct 变体，由 ELYZA team 在 Llama 2 Community License 下维护。
 * [Llama-3.1-Swallow-8B-Instruct-v0.5](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.5) - 📥 2k / ⭐ 19 / Llama 3.1 Swallow 是一组 8‑B 和 70‑B 模型，它们继续对 Meta 的 Llama 3.1 进行预训练，以提升日语语言性能，然后在合成日语数据上进行指令微调，提供多种已发布的变体，其对话行为已改进，与 gemma‑3‑27b‑it 相当。
 * [open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - 📥 2k / ⭐ 20 / OpenCALM 是 CyberAgent 开发的日本解码器（decoder‑only）Transformers 语言模型系列（160 M–6.8 B 参数），基于日本维基百科和 Common Crawl 训练，并以 CC BY‑SA 4.0 许可证发布。
 * [sarashina2.2-1b-instruct-v0.1](https://huggingface.co/sbintuitions/sarashina2.2-1b-instruct-v0.1) - 📥 2k / ⭐ 16 / 本仓库托管了 SB Intuitions 的 1 B‑parameter 自回归日语指令模型 sarashina2.2‑1b‑instruct‑v0.1，已在日语和英语 MT 与指令任务上与其他 Japanese‑BERTs 进行基准测试，附带 torch-transformer 使用代码片段和有限安全训练的警告。
 * [LFM2.5-1.2B-JP-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP-GGUF) - 📥 2k / ⭐ 29 / LFM2.5‑1.2B‑JP 是一个 1.2 B 参数的日语文本生成模型，基于 LFM2.5 混合架构构建，优化用于生成和完成任务，托管在 Hugging Face 上，并可通过 llama.cpp 运行。
 * [ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - 📥 2k / ⭐ 75 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 模型的 6.27 B 参数扩展版，已在包含 instruct 和 fast 变体的日语数据上预训练，可通过 Hugging Face Transformers 使用。
 * [gpt2-japanese-lyric-small](https://huggingface.co/skytnt/gpt2-japanese-lyric-small) - 📥 2k / ⭐ 3 / 日语 GPT‑2 歌词生成模型，训练于 143,587 首 uta‑net 歌曲，提供 Web 演示及 Torch/Transformers 使用示例。
 * [llm-jp-3.1-1.8b](https://huggingface.co/llm-jp/llm-jp-3.1-1.8b) - 📥 2k / ⭐ 13 / llm-jp-3.1-1.8b 是来自 NII 的 Large Language Models R&D Center 的 1.8 b‑parameter 日本 LLM，以 Hugging Face checkpoint 的形式分发（torch ≥ 2.3, transformers ≥ 4.40, accelerate ≥ 0.29, flash‑attn ≥ 2.5），仓库中包含完整的 model specs、tokenizer 和 pre‑training details。
 * [gpt2-large-japanese-char](https://huggingface.co/ku-nlp/gpt2-large-japanese-char) - 📥 2k / ⭐ 5 / 日语字符级 GPT‑2 Large（717 M 参数）预训练于约 171 GB 的日本维基百科、CC‑100 和 OSCAR 数据，使用 NVIDIA A100 在 AdamW 优化器和线性学习率调度下训练约 8 个月，可通过 Hugging Face pipelines 用于文本生成或特征提取。
 * [llm-jp-3.1-13b-instruct4](https://huggingface.co/llm-jp/llm-jp-3.1-13b-instruct4) - 📥 2k / ⭐ 19 / LLM‑jp‑3.1‑13b‑instruct4 是一个 13‑B 的、基于指令预训练的日语语言模型，由 NII 的研发中心开发，并以 Hugging‑Face Transformers 检查点的形式发布，使用 UNIGRAM‑byte‑fallback 分词器。
 * [shisa-v2.1-qwen3-8b](https://huggingface.co/shisa-ai/shisa-v2.1-qwen3-8b) - 📥 2k / ⭐ 9 / Shisa V2.1 引入了升级版双语日英聊天模型——基于全新数据集，增强了指令、翻译和礼貌细调——在 Llama 3.2、Qwen 3‑8B 和 UnPhi‑4 14B 等变体中，显著提升了性能。
 * [Swallow-13b-hf](https://huggingface.co/tokyotech-llm/Swallow-13b-hf) - 📥 1k / ⭐ 12 / 东京科技-LLM（TokyoTech‑LLM）基于 LLaMA‑2，并通过日语数据（SFT）微调，包含 Swallow‑7b/13b/70b 变体及其 instruct、NVE 和 “plus” 版本，发布时间从2023年12月到2024年4月。
 * [Sakura-13B-Galgame](https://huggingface.co/sakuraumi/Sakura-13B-Galgame) - 📥 1k / ⭐ 126 / SakuraLLM 提供非商业的、RLHF‑fine‑tuned 日语至中文翻译模型，面向轻小说和 galgame 领域，基于开源 LLMs，使用领域特定数据，支持多种尺寸、离线部署以及明确的许可与使用指南。
 * [RakutenAI-7B-chat](https://huggingface.co/Rakuten/RakutenAI-7B-chat) - 📥 1k / ⭐ 67 / RakutenAI‑7B‑chat 是基于 Mistral‑7B‑v0.1 架构打造的日本 LLM，提供了优秀的日语理解基准成绩，并在英语上具有竞争力的表现，拥有基础模型（RakutenAI‑7B）和指令微调版本（RakutenAI‑7B‑instruct）。
 * [llm-jp-3-150m-instruct3](https://huggingface.co/llm-jp/llm-jp-3-150m-instruct3) - 📥 1k / ⭐ 4 / 来自日本信息学研究所的日语 150M 参数指令型 LLM，可作为符合 Hugging Face 的 Transformer 模型使用，需 torch ≥ 2.3.0 和 transformers ≥ 4.40.1。
 * [RakutenAI-7B-instruct](https://huggingface.co/Rakuten/RakutenAI-7B-instruct) - 📥 1k / ⭐ 50 / RakutenAI‑7B‑instruct, 基于 Mistral‑7B‑v0.1 构建，是一款聚焦日语的 LLM，在日语基准测试中获得最高分，同时匹配英语性能，并发布了聊天调优版本。
 * [llm-jp-13b-v1.0](https://huggingface.co/llm-jp/llm-jp-13b-v1.0) - 📥 1k / ⭐ 41 / 来自 LLM‑jp 的大规模语言模型 — 13B 和 1.3B 日英双语 transformer，拥有多种指令和 LoRA 变体，使用 Megatron‑DeepSpeed 预训练，并以 Hugging Face 格式（torch ≥ 2.0，transformers ≥ 4.34）发布。
 * [ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - 📥 1k / ⭐ 96 / ELYZA‑japanese‑Llama‑2‑7b 是 Meta 的 Llama‑2 7 B 的日语优化扩展，提供 instruct 和 fast 变体，参数为 6.27–6.37 B，可通过 Hugging‑Face Transformers 库访问。
 * [youri-7b](https://huggingface.co/rinna/youri-7b) - 📥 1k / ⭐ 21 / youri‑7b 是一个32层、4096隐藏单元的 transformer，基于 Llama2‑7b 构建，持续在约 40 B 个日语 token（CC‑100、C4、OSCAR、Pile、Wikipedia）上进行预训练，并于 2023 年 10 月 31 日发布，在 AI2 Reasoning Challenge、HellaSwag、MMLU、TruthfulQA 和 Winogrande 上取得了竞争性的分数。
 * [llm-jp-1.3b-v1.0](https://huggingface.co/llm-jp/llm-jp-1.3b-v1.0) - 📥 1k / ⭐ 15 / LLM‑jp提供13 B和1.3 B变压器语言模型，包括多种指令调优变体，采用Megatron‑DeepSpeed和Hugging Face Transformers生态系统构建。
 * [japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) - 📥 1k / ⭐ 121 / Japanese‑StableLM‑Base‑Alpha‑7B 是一个 7 B 参数的仅解码器语言模型，在混合日语/英语数据集上预训练，以在日语语言建模和下游任务中提供强劲性能。
 * [diafill-sarashina2.2-3b-instruct](https://huggingface.co/sbintuitions/diafill-sarashina2.2-3b-instruct) - 📥 1k / ⭐ 3 / DiaFill 是一款经过精细调校的日本双说话人对话脚本生成器，能够根据种子提示生成自然、充满填充语的口语式对话，训练数据来自专有的 GENIAC 数据。
 * [ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - 📥 1k / ⭐ 82 / 来自 ELYZA 的日语增强版 Llama‑2‑7B，已预训练以提供扩展的日语语言能力，提供标准、指导和快速版本，附有详细使用示例、开发者署名，并遵循 Meta’s Llama‑2 Community License 许可。
 * [japanese-stablelm-instruct-beta-70B-GGUF](https://huggingface.co/TheBloke/japanese-stablelm-instruct-beta-70B-GGUF) - 📥 1k / ⭐ 12 / 提供了用于Stability AI的70亿参数日语StableLM Instruct Beta的GGUF格式、硬件量化模型文件，已准备好与LLaMA‑cpp基于工具一起使用。
 * [open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - 📥 1k / ⭐ 4 / OpenCALM 是 CyberAgent 开发的一套日语仅解码器（decoder‑only）Transformer 语言模型，参数规模从 160 M 到 6.8 B，训练数据来自日语维基百科与 Common Crawl，并按 CC BY‑SA 4.0 许可发布。
 * [open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - 📥 1k / ⭐ 205 / OpenCALM 是 CyberAgent, Inc. 开发的日语仅解码器 Transformer 语言模型套件，包含 160 M 至 6.8 B 参数的版本，预训练于 Wikipedia 和 Common Crawl， 可通过 Transformers 库以 CC BY‑SA 4.0 许可证获取。
 * [NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf](https://huggingface.co/mmnga-o/NVIDIA-Nemotron-Nano-9B-v2-Japanese-gguf) - 📥 1k / ⭐ 50 / GGUF‑formatted NVIDIA‑Nemotron‑Nano‑9B‑v2‑Japanese，已从 imatrix 数据集重建，并准备好在 CUDA 上使用 llama.cpp 运行。
 * [Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4](https://huggingface.co/tokyotech-llm/Qwen3-Swallow-32B-RL-v0.2-AWQ-INT4) - 📥 1k / ⭐ 2 / 在 Qwen3‑Swallow v0.2 中的中日双语 LLM（30B‑A3B / 32B）通过 CPT、SFT 和 RLVR 进行训练，以保持数学和编码表现、提升推理能力，并已在 Hugging Face 上发布数个量化版本。
 * [japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - 📥 1k / ⭐ 75 / 一个 3.6‑B‑parameter 的日本 GPT‑NeoX 模型——36 层、2816 维隐藏层 transformer——采用 PPO‑based RLHF 在翻译后的 Anthropic 数据上训练，遵循指令式对话，表现出约 30 % 的人类对位和 34 % 的 ChatGPT‑based PPO 胜率超过 SFT，但倾向于生成重复文本。
 * [open-calm-large](https://huggingface.co/cyberagent/open-calm-large) - 📥 1k / ⭐ 10 / OpenCALM 是来自 CyberAgent 的一个仅解码器的日语 Transformer 系列（参数量 160 M – 6.8 B，范围从 open‑calm‑small 到 open‑calm‑7b），训练数据为日语 Wikipedia 和 Common‑Crawl，采用 CC BY‑SA 4.0 许可证，可通过 Hugging Face transformers 使用。
 * [sarashina2-7b](https://huggingface.co/sbintuitions/sarashina2-7b) - 📥 1k / ⭐ 28 / Sarashina2‑7B 是一个 7 B-参数 Llama‑2 模型，训练数据包括约 1 T 的日语 Common Crawl 令牌和 SlimPajama 英语数据，采用 RoPE‑based 架构，但它仍未进行指令微调，可能生成有偏见或不准确的输出。
 * [t5-base-long-livedoor-news-corpus](https://huggingface.co/llm-book/t5-base-long-livedoor-news-corpus) - 📥 1k / ⭐ 1 / 一个在日本 Livedoor 新闻语料库上微调的 T5‑base 摘要模型，展示于《Large‑Scale Language Model Introduction guide》第七章。
 * [japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - 📥 1k / ⭐ 26 / Japanese 3.6 B‑parameter GPT‑NeoX 模型细调以适应指令遵循（SFT‑v2），对比之前的 SFT 与 ChatGPT 在 100 条提示上进行评估，发布于 2023 年 3 月 31 日。
 * [ELYZA-japanese-Llama-2-13b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-13b-instruct) - 📥 1k / ⭐ 43 / ELYZA‑japanese‑Llama‑2‑13b 扩展了 Meta’s Llama 2，额外对日语进行预训练，提供 13 B 参数模型（包括 instruct 和 fast 变体），可在 Llama 2 Community License 下使用 PyTorch 和 🤗 Transformers 加载。
 * [llm-jp-3-980m-instruct2](https://huggingface.co/llm-jp/llm-jp-3-980m-instruct2) - 📥 1k / ⭐ 3 / 提供了 NII 研发中心的 980 M 参数 LLM‑jp‑3‑instruct2 模型作为 Hugging Face 检查点，要求 torch ≥ 2.3、transformers ≥ 4.40、accelerate ≥ 0.29、flash‑attn ≥ 2.5，并使用单字节回退 tokenizer 进行预训练，数据来源为日本维基百科和 Common Crawl。
 * [open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) - 📥 1k / ⭐ 17 / OpenCALM 是 CyberAgent 出品的一套日本解码器模型，参数范围为 160 M 至 6.8 B，基于 GPT‑NeoX 构建，采用 CC BY‑SA 4.0 许可发布。

### fill-mask
 * [bert-base-japanese-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-whole-word-masking) - 📥 354k / ⭐ 76 / Japanese BERT‑base 在 2019 年日本维基百科上预训练，使用 IPA‑dictionary 与全词掩码，12 层 768 维，32,000 词表，512 标记序列，1 M 步骤，可在 cl‑tohoku/bert‑japanese 获取，遵循 CC‑BY‑SA 许可。
 * [bert-base-japanese](https://huggingface.co/tohoku-nlp/bert-base-japanese) - 📥 321k / ⭐ 41 / 一个预训练于约 17 M 条日语维基百科句子（2.6 GB）的 BERT base 模型，使用 IPA 字典和 WordPiece 进行分词，拥有 12 层 / 768‑维隐藏状态 / 12 头，32 000‑token 词汇表，已在 Cloud TPUs 上训练了 1 M 步，并以 CC‑BY‑SA 3.0 许可发布。
 * [japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 📥 158k / ⭐ 39 / Japanese‑Roberta‑Base 是来自 rinna Co., Ltd. 的预训练掩码语言模型，提供了正确加载、token 预处理、position‑id 处理的准则，以及强调需要前置 [CLS] token 和一致 tokenization 的使用示例。
 * [bert-base-japanese-char](https://huggingface.co/tohoku-nlp/bert-base-japanese-char) - 📥 115k / ⭐ 8 / 一个 BERT‑base 日语模型（12 层，768 维隐藏，12 头），使用 MeCab IPA 词级分词后再进行字符级分词生成 4000 词的词表，在约 1700 万句来自日语维基百科（2.6 GB）的句子上预训练，训练代码位于 cl‑tohoku/bert‑japanese，采用 CC BY‑SA 3.0 许可证发布。
 * [bert-base-japanese-char-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v2) - 📥 66k / ⭐ 6 / 一个 BERT‑base 日语模型（12 层，768-维隐藏状态，12 头），在 3000 万条维基百科句子（约 4 GB）上训练，使用 Unidic 2.1.2 词级分词，随后进行字符级分词和全词掩码，使用 512 令牌序列，256 批次，以及 1 M 训练步骤。
 * [deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 📥 34k / ⭐ 9 / 日语 DeBERTa V2 大型模型，已在 171 GB 的日语 Wikipedia、CC‑100 与 OSCAR 上训练，使用字符级 SentencePiece 分词和全词掩码，已准备好通过 Hugging Face Transformers 进行下游微调。
 * [modernbert-ja-130m](https://huggingface.co/sbintuitions/modernbert-ja-130m) - 📥 19k / ⭐ 48 / 这是一款 1.32 亿参数的日语 ModernBERT 模型，融合了 local‑global 与 RoPE 注意力机制，训练于 4.39 T 词条（日语/英语），词表大小 102k，最大序列长度 8,192，针对 Flash Attention 2 做了优化。
 * [modernbert-ja-310m](https://huggingface.co/sbintuitions/modernbert-ja-310m) - 📥 10k / ⭐ 25 / ModernBERT‑Ja‑310M 是一种日语 BERT 变体，融合了局部-全局注意力和 RoPE，训练于 4.09 T 日语/英语文本，支持 102 400 词汇量、8 192 令牌序列，并针对 Flash Attention 2 进行了优化。
 * [deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 📥 9k / ⭐ 2 / Japanese DeBERTa V2 tiny，在约171 GB的日本维基百科、CC‑100 与 OSCAR 语料库上预训练，需使用 Juman++ 词分割，训练耗时 33 小时，使用8块 NVIDIA A100 GPU，并可用于下游任务的微调。
 * [bert-base-japanese-v2](https://huggingface.co/tohoku-nlp/bert-base-japanese-v2) - 📥 6k / ⭐ 26 / Japanese BERT‑base（12 层，768 隐藏，12 头）在 4 GB 的日语维基百科（≈30 M 句）上预训练，使用 Unidic 2.1.2 词级分词、WordPiece 子词分词和全词遮蔽。
 * [line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - 📥 6k / ⭐ 49 / LINE DistilBERT Japanese 是一个 6600 万参数的 DistilBERT 模型，已在 131 GB 的日语网页文本上使用内部 BERT‑base 教师进行预训练，评估基准为 JGLUE，采用 MeCab Unidic 与 SentencePiece 进行分词，并以 Apache 2.0 许可证发布。
 * [deberta-v2-base-japanese](https://huggingface.co/izumi-lab/deberta-v2-base-japanese) - 📥 5k / ⭐ 5 / DeBERTaV2 base 在日本语语料库（CC‑100、mC4、OSCAR2301、Wikipedia、Wikinews）上训练，并使用 FP‑16 微调进行 NLU 任务（JSTS、JNLI、JCommonsenseQA），以 CC BY‑SA 4.0 许可发布，并由日本研究资助。
 * [deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 📥 2k / ⭐ 30 / Japanese DeBERTa V2 基础模型已在 171 GB 的日语维基百科、CC‑100 和 OSCAR 数据上预训练，使用 Juman++ 分词和 SentencePiece 标记化，经过三周在八块 NVIDIA A100 GPU 上训练，现已准备好用于微调。
 * [luke-japanese-large](https://huggingface.co/studio-ousia/luke-japanese-large) - 📥 2k / ⭐ 9 / 日语LUKE，一种知识增强的Transformer，将单词和维基百科实体视为独立标记——提供上下文化表示，并在JGLUE上优于基线（例如MARC‑ja 96.5 %准确率），并提供一个无实体任务的精简版。
 * [deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 📥 2k / ⭐ 1 / 一款日本DeBERTa‑V2基础模型，已在171 GB的日本维基百科、CC‑100和OSCAR文本上预训练，使用字符级分词、全词掩码，训练耗时20天，使用8块A100 GPU，并已准备好进行下游微调。
 * [roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - 📥 2k / ⭐ 32 / Japanese RoBERTa‑base 在日本 Wikipedia 与日本 CC‑100 上预训练，采用 Juman++ 词分割与 SentencePiece 分词，使用 Adam（lr = 1e‑4，native AMP）在 8 台 NVIDIA A100 GPU 上训练了一周，可微调，并在 JGLUE 上报告了结果。
 * [modernbert-ja-30m](https://huggingface.co/sbintuitions/modernbert-ja-30m) - 📥 1k / ⭐ 7 / ModernBERT‑Ja‑30M 是一种日语 BERT 变体，融合了本地和全局注意力与 RoPE，训练于 4.39 TB 日英文本，支持 8,192 令牌序列，参数规模从 30 M 到 130 M，最佳搭配 Flash Attention 2。
 * [deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 📥 1k / ⭐ 9 / Japanese DeBERTa‑V2 大模型预训练于 171 GB 日文文本（Wikipedia、CC‑100、OSCAR），使用 Juman++ 分词，在 8 台 A100 GPU 上训练 36 天，可针对下游任务进行微调。
 * [bert-base-japanese-char-whole-word-masking](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-whole-word-masking) - 📥 1k / ⭐ 4 / 12 层，768 维度的 BERT‑Base 日语模型，在 2.6 GB Wikipedia（≈17 M 句子）上训练，使用 IPA‑dictionary 字符分词与 whole‑word masking，并在 CC‑BY‑SA 3.0 许可下发布。

### sentence-similarity
 * [ruri-v3-310m](https://huggingface.co/cl-nagoya/ruri-v3-310m) - 📥 394k / ⭐ 74 / Ruri v3 是基于 ModernBERT‑Ja 的先进日语文本嵌入模型，支持多达 8,192 词元输入，100K 词元词汇表，FlashAttention 加速推理，并提供多种尺寸变体，便于快速使用 sentence‑transformer。
 * [ruri-v3-30m](https://huggingface.co/cl-nagoya/ruri-v3-30m) - 📥 126k / ⭐ 9 / Ruri v3是一个最先进的日语文本嵌入模型，基于ModernBERT‑Ja构建，支持最多8,192个标记，拥有100 k词汇量，支持FlashAttention加速，并提供多种规模，从37 M到315 M参数。
 * [ruri-v3-130m](https://huggingface.co/cl-nagoya/ruri-v3-130m) - 📥 39k / ⭐ 6 / Ruri v3 是基于 ModernBERT‑Ja 的前沿日语文本嵌入模型，支持最多 8192 token 序列、100K token 词汇量、FlashAttention，并以 30 M 至 310 M 参数规模发布，供 sentence‑transformers 使用。
 * [GLuCoSE-base-ja-v2](https://huggingface.co/pkshatech/GLuCoSE-base-ja-v2) - 📥 17k / ⭐ 24 / GLuCoSE v2 是一款 CPU 友好的日语文本嵌入模型，通过蒸馏和多阶段对比学习进行微调，提供卓越的语义相似性和检索性能——在 MIRACL 及相关基准上优于同等规模的模型。
 * [GLuCoSE-base-ja](https://huggingface.co/pkshatech/GLuCoSE-base-ja) - 📥 17k / ⭐ 34 / GLuCoSE 是一个基于 LUKE 的日语句子嵌入模型，输出 768 维均值池化向量（最多 512 个标记），在 Web 和 NLI/搜索数据上训练，在相似性基准测试中达到了 0.864 的 Spearman 相关系数和 0.818 的 Pearson 相关系数。
 * [ruri-base](https://huggingface.co/cl-nagoya/ruri-base) - 📥 15k / ⭐ 12 / 日语通用文本嵌入模型（Ruri‑v3，30‑310 M 参数，8192‑token 最大，JMTEB 分数高）与 Sentence‑Transformers 使用示例以及与其他日语嵌入模型的基准对比一起提供。
 * [ruri-v3-70m](https://huggingface.co/cl-nagoya/ruri-v3-70m) - 📥 11k / ⭐ 3 / Ruri v3 提供高性能的日语文本嵌入，支持至 8192 个 token，拥有 100k 个 token 的词汇表，支持 FlashAttention，并提供多种模型规模（30 m–310 m），以实现高效推理和通过 sentence‑transformers 进行微调。
 * [JaColBERTv2](https://huggingface.co/bclavie/JaColBERTv2) - 📥 11k / ⭐ 16 / JaColBERTv2 是一个仅适用于日语的基于 ColBERT 的检索模型，在 MMarco 上通过知识蒸馏训练（每个正例 31 个负例，250k 次，batch 32）。目前它优于 multilingual‑e5‑large、BGE‑M3 和 JaColBERT，完整评估正在进行中。
 * [ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 📥 10k / ⭐ 45 / 一组已准备好发布的 Ruri v3 日语文本嵌入模型（30m–310m），完整附带 SentenceTransformer 使用技巧、查询/段落前缀，以及 JMTEB 基准结果，展示它们与其他日语和多语言嵌入模型的比较。
 * [ruri-base-v2](https://huggingface.co/cl-nagoya/ruri-base-v2) - 📥 7k / ⭐ 5 / 仓库提供新的日语文本嵌入 v3 模型（30M‑310M 参数，8 k‑token 最大，JMTEB 74‑77），可使用 sentence_transformers（使用 query/passage 前缀）加载，并包含与监督/无监督 SimCSE、LaBSE、E5 以及其他模型的基准比较。
 * [plamo-embedding-1b](https://huggingface.co/pfnet/plamo-embedding-1b) - 📥 7k / ⭐ 44 / PLaMo‑Embedding‑1B 是 Preferred Networks 的一款日语文本嵌入模型，它将日语文本转换为向量，用于信息检索、分类和聚类，在 JMTEB 基准上表现出强大性能，并且在 Apache v2.0 许可证下可免费使用。
 * [sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - 📥 2k / ⭐ 36 / sbert-jsnli‑luke‑japanese‑base‑lite 是一个 768 维的句子变换器，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，训练了一个 epoch 的 shunk031/jsnli，并包含用于聚类、语义搜索以及同时兼容 Sentence‑Transformers 和 HuggingFace 的示例。
 * [ruri-small-v2](https://huggingface.co/cl-nagoya/ruri-small-v2) - 📥 2k / ⭐ 4 / Ruri发布日本通用文本嵌入模型v3（30 M–310 M 参数，8192‑Token 最大长度），在JMTEB上取得最高分，提供直接的 sentence_transformers 用法（以「クエリ:」或「文章:」为前缀），并给出检索、STS、分类、重排序、聚类和成对分类任务的基准结果。
 * [fio-base-japanese-v0.1](https://huggingface.co/bclavie/fio-base-japanese-v0.1) - 📥 2k / ⭐ 7 / fio‑base‑japanese‑v0.1 是一个概念验证的日语嵌入模型，基于 cl‑tohoku/bert‑base‑japanese‑v3 在有限数据上进行微调，使用单个 GPU，已发布用于文本蕴含和检索任务。
 * [ruri-small](https://huggingface.co/cl-nagoya/ruri-small) - 📥 1k / ⭐ 9 / 包括 Ruri v3 日语文本嵌入（30 M–310 M 参数，8192‑token 限制，JMTEB 74.5–77.2），使用 “クエリ:” 或 “文章:” 前缀的 Sentence Transformers 指令，以及对数个日语模型（如 Sup/Unsup SimCSE、GLuCoSE、LaBSE）的基准结果。
 * [sarashina-embedding-v1-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v1-1b) - 📥 1k / ⭐ 38 / Sarashina‑Embedding‑v1‑1B 是一个 1.2 B 参数的日语文本嵌入模型，构建于 Sarashina2.1‑1B 上，使用多阶段对比学习训练，以在 JMTEB 上达到最先进的分数，同时在非商业许可下生成 1,792 维的稠密向量，用于语义相似度、搜索和分类。

### feature-extraction
 * [sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 📥 318k / ⭐ 11 / 用于生成句子嵌入的 Japanese Sentence‑BERT (v1) 模型，已提供改进版 v2，并通过 Hugging Face Transformers 以及自定义的 `SentenceBertJapanese` 类进行示例使用。
 * [sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 📥 52k / ⭐ 51 / 一款在 cl‑tohoku/bert‑base‑japanese‑whole‑word‑masking 上使用 MultipleNegativesRankingLoss 细调的 Japanese Sentence‑BERT v2，较 v1 提升了约 1.5–2 %的准确率，并以 sonoisa/sentence‑bert‑base‑ja‑mean‑tokens‑v2 发布。
 * [sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 📥 30k / ⭐ 14 / Japanese Sentence‑LUKE 模型在与 Sentence‑BERT 同一数据集上训练，表现超过或匹配其性能，基于 studio‑ousia/luke‑japanese‑base‑lite 构建，并通过 Hugging Face Transformers 的 MLukeTokenizer 与 LukeModel 进行使用。
 * [transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - 📥 28k / ⭐ 2 / ja_ginza_electra 是一个 spaCy v3 Python 包，提供一个在 mC4 和 UD_Japanese_BCCWJ r2.8（基于 megagonlabs/transformers‑ud‑japanese‑electra‑base‑discrimininator）上微调的日语 ELECTRA 模型，并配有自定义 bunsetu‑phrase 检测功能，按 MIT license 分发。
 * [japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - 📥 27k / ⭐ 24 / rinna/japanese-clip‑vit‑b‑16 是一个 Apache‑2.0 许可的日语 CLIP 模型，基于 ViT‑B/16，训练于 CC12M captions 翻译成日语，并于 2022 年 5 月 12 日发布。
 * [clip-japanese-base](https://huggingface.co/line-corporation/clip-japanese-base) - 📥 26k / ⭐ 29 / LY Corporation的clip‑japanese‑base 是一个日语 CLIP 模型，在约10亿对图像‑文本对上训练，使用 Eva02‑B transformer 图像编码器和 12 层 BERT 文本编码器，在 STAIR 上实现 R@1 0.30，在 Recruit 上得到 0.89 的准确率，在 ImageNet‑1K 上得到 0.58 的准确率，并支持 zero‑shot 图像分类和检索。
 * [japanese-hubert-base](https://huggingface.co/yky-h/japanese-hubert-base) - 📥 5k / ⭐ 4 / 日语HuBERT Base，12层 Transformer 与 rinna 原版相同，使用约19,000小时的 ReazonSpeech v1 日语语音训练，并以 Apache 2.0 许可证发布。
 * [t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 📥 5k / ⭐ 56 / 一个Japanese‑language T5 model，在约100 GB的Wikipedia和OSCAR数据上使用SentencePiece tokenization进行预训练，超越了Google’s multilingual T5在news‑classification benchmark上的表现，但需要fine‑tuning，并可能产生biased outputs.
 * [llm-jp-4-vl-9b-beta](https://huggingface.co/llm-jp/llm-jp-4-vl-9b-beta) - 📥 2k / ⭐ 12 / LLM‑jp‑4‑VL 9B beta 是一个 90 亿参数的日语视觉语言模型，以 llm‑jp‑4‑8b‑instruct 和 SigLIP‑2 为基础，采用 InternVL3.0 样式的动态切块和轻量化 MLP 投影器，并在 FineVision 和 Jagle 上训练后，在日语基准测试中获得了竞争性表现。
 * [japanese-avhubert-large_noise_pt](https://huggingface.co/enactic/japanese-avhubert-large_noise_pt) - 📥 2k / ⭐ 2 / 一个预训练的 2,250 小时 AVHuBERT Large 自监督模型，在日本音频-视觉数据上训练并使用噪声增强，以稳健支持音频-视觉语音识别。
 * [clip-japanese-base-v2](https://huggingface.co/line-corporation/clip-japanese-base-v2) - 📥 2k / ⭐ 18 / 日本CLIP模型 clip‑japanese‑base‑v2，升级后约20亿图像‑文本对并采用蒸馏，配合 Eva02‑B 图像编码器和 12 层 BERT 文本编码器，将 ImageNet‑1k 准确率提升至 0.708，超过前代模型。
 * [japanese-hubert-large](https://huggingface.co/yky-h/japanese-hubert-large) - 📥 1k / ⭐ 2 / Japanese‑HuBERT‑Large 是一个基于 Apache 2.0 许可的镜像，复制了 rinna 原始的 24 层、16 头 transformer 模型，该模型在约 19,000 小时的 ReazonSpeech v1 日语语音上训练，并于 2024 年 3 月 7 日发布。
 * [sup-simcse-ja-base](https://huggingface.co/cl-nagoya/sup-simcse-ja-base) - 📥 1k / ⭐ 3 / 一个日语 BERT‑base 模型，在 JSNLI 上使用有监督 SimCSE 进行微调，通过 Sentence‑Transformers 或 HuggingFace 提供，采用 CLS 池化。在 1M 个样本上训练，批量大小为 512，学习率为 5×10⁻⁵，温度为 5×10⁻⁵，64 令牌限制，采用 BFloat16 精度。
 * [sup-simcse-ja-large](https://huggingface.co/cl-nagoya/sup-simcse-ja-large) - 📥 1k / ⭐ 15 / Sup‑simcse‑ja‑large 提供了一个经过监督训练的 SimCSE 微调的日文 BERT‑large (cl‑tohoku/bert‑large‑japanese‑v2) 模型，采用 CLS‑plus‑MLP 池化，在约 1 M 的 JSNLI 句子上训练（lr 5e‑5, batch 512, temp 0.05, max 64），并可直接与 Sentence‑Transformers 或 Hugging Face Transformers 一起使用。
 * [sarashina-embedding-v2-1b](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b) - 📥 1k / ⭐ 25 / Sarashina‑Embedding‑v2‑1B 是一个 1,792 维的日语句子变换器，使用多阶段对比学习训练，获得了前沿的 JMTEB 分数，可通过 Sentence‑Transformers 并搭配可选指令前缀，用于语义相似度、搜索、改写挖掘、分类和聚类。

### automatic-speech-recognition
 * [wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 📥 1M / ⭐ 57 / Japanese wav2vec‑2 XLSR‑53 在 Common Voice 6.1、CSS10 与 JSUT 上微调，需 16 kHz 音频，并可通过 HuggingSound 或 HuggingFace 管道使用。
 * [kotoba-whisper-v2.2](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2) - 📥 213k / ⭐ 100 / Kotoba‑Whisper‑v2.2 是一个日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了说话人划分和自动标点功能，通过 HuggingFace‑Transformers pipeline，并与 Asahi Ushio 与 Kotoba Technologies 合作开发。
 * [kotoba-whisper-v2.1](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.1) - 📥 33k / ⭐ 19 / Kotoba‑Whisper‑v2.1 是一种日语 ASR 模型，扩展了 kotoba‑whisper‑v2.0，集成了标点后处理管道，保持可比的 CER 性能，同时实现无缝、标点感知的转录。
 * [anime-whisper](https://huggingface.co/litagin/anime-whisper) - 📥 31k / ⭐ 136 / Anime Whisper 是一款轻量级的日语 ASR 模型，在约 5,300 小时的动漫风格对话上进行微调，能够提供低幻觉、节奏对齐标点，以及准确转录非言语声音和 NSFW 内容，并且需要在没有初始提示的情况下运行。
 * [wav2vec2-large-xlsr-japanese-hiragana](https://huggingface.co/vumichien/wav2vec2-large-xlsr-japanese-hiragana) - 📥 18k / ⭐ 10 / 一个由 facebook/wav2vec2‑large‑xlsr‑53 在 Common Voice 和 JSUT corpus 上微调的日本语音识别模型，针对 16 kHz 音频输入进行了优化。
 * [parakeet-tdt_ctc-0.6b-ja](https://huggingface.co/nvidia/parakeet-tdt_ctc-0.6b-ja) - 📥 15k / ⭐ 53 / NVIDIA NeMo 的 0.6 B 参数 Hybrid FastConformer‑TDT‑CTC ASR 模型可转写带标点的日语语音，并可在 NeMo 框架内用于推理或微调。
 * [kotoba-whisper-v2.0](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0) - 📥 12k / ⭐ 90 / Kotoba‑Whisper v2.0 是从 OpenAI Whisper large‑v3 蒸馏出的日语 ASR 模型，训练于 720 万个 ReazonSpeech 剪辑，推理速度快 6.3 倍，同时在同域测试中匹配教师模型的 CER/WER，并提供 stable‑ts/标点支持以及完整的训练代码在 GitHub 上。
 * [kotoba-whisper-bilingual-v1.0](https://huggingface.co/kotoba-tech/kotoba-whisper-bilingual-v1.0) - 📥 10k / ⭐ 19 / Kotoba‑Whisper‑Bilingual v1.0 提供了快 6.3 倍的蒸馏 Whisper 模型，用于日语和英语 ASR，并实现双向语音转文本翻译，这些模型是基于 OpenAI 的 Whisper large‑v3 通过知识蒸馏、交叉熵和 KL‑divergence 损失构建。
 * [japanese-wav2vec2-large-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-large-rs35kh) - 📥 8k / ⭐ 3 / 日语 wav2vec 2.0 Large (319 M parameters) 微调于 ReazonSpeech v2.0，在日语 ASR 上提供平均 16.25 % CER，优于其他 wav2vec 2.0 系列。
 * [japanese-hubert-base-phoneme-ctc-v4](https://huggingface.co/prj-beatrice/japanese-hubert-base-phoneme-ctc-v4) - 📥 3k / ⭐ 4 / 微调日语 Hubert‑Base 用于 CTC 音素识别（v4）并更新句子过滤规则、发音调整以及将 GPU 切换到 A6000，训练在 110k 步时停止。
 * [reazonspeech-nemo-v2](https://huggingface.co/reazon-research/reazonspeech-nemo-v2) - 📥 1k / ⭐ 38 / reazonspeech-nemo-v2 是一个 619‑M‑参数的日语长文本 ASR 模型，基于改进版 Fast‑Conformer 及 Linearly Scalable Attention，在 ReazonSpeech v2.0 语料库上训练，支持通过 subword RNN‑T decoder（3000‑token SentencePiece）进行多小时推理，并以 Apache 2.0 许可分发。
 * [kotoba-whisper-v2.0-faster](https://huggingface.co/kotoba-tech/kotoba-whisper-v2.0-faster) - 📥 1k / ⭐ 24 / Kotoba Whisper v2.0 被转换为 CTranslate2 格式，以便与 CTranslate2 和 faster-whisper 一起使用，提供安装、推理示例、Apple M2 基准测试和转换说明。
 * [japanese-wav2vec2-base-rs35kh](https://huggingface.co/reazon-research/japanese-wav2vec2-base-rs35kh) - 📥 1k / ⭐ 2 / Japanese‑wav2vec2‑base‑rs35kh 是一个 96.7 M 参数的 wav2vec 2.0 Base 模型，经过在 ReazonSpeech v2.0 日语 ASR 语料库上微调，达到 13.22 % 的 CER，可与 Hugging Face transformers 一同部署，并在 Apache 2.0 许可证下发布。
 * [whisper-ja-1.5B](https://huggingface.co/efwkjn/whisper-ja-1.5B) - 📥 1k / ⭐ 3 / 一个微调的 Whisper‑Large‑v3 基线在 KitsuneX07、TEDxJP、kotoba‑tech、Saruwatari‑lab 和 grider‑without‑ai 测试集上提供了竞争性的 SOTA CER，训练数据来自 OOPPEENN、Reazon、小虫哥_、Common Voice 20 和 deepghs，比早期模型拥有更小的检查点并偶尔出现重复。

### text-ranking
 * [japanese-reranker-cross-encoder-small-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-small-v1) - 📥 230k / ⭐ 5 / 日本训练的 CrossEncoder 重新排序器，尺寸从 xsmall（384）到 large（1024），以及 BGE‑v2‑m3‑v1 模型，提供微调、推理和 JQaRA、JaCWIR、MIRACL、JSQuAD 上的基准分数示例代码。
 * [japanese-reranker-cross-encoder-xsmall-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-xsmall-v1) - 📥 49k / ⭐ 7 / 日语 CrossEncoder 再排序模型，覆盖 xsmall 到 large（含 BGE），在 JQaRA、JaCWIR、MIRACL 与 JSQuAD 上进行评估，并为 sentence_transformers 与 HuggingFace 提供即用的集成示例。
 * [ruri-v3-reranker-310m](https://huggingface.co/cl-nagoya/ruri-v3-reranker-310m) - 📥 39k / ⭐ 14 / Ruri‑v3 Reranker 是一个基于 ModernBERT‑Ja 构建的稳健日语文本重排器，支持最高 8,192‑token 序列、100k‑token 词汇表、FlashAttention 以及 SentencePiece 分词器，并可通过 sentence‑transformers 使用。
 * [japanese-reranker-xsmall-v2](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2) - 📥 17k / ⭐ 6 / 快、轻量级的日语 Reranker v2 模型（tiny、xsmall、small、base），带有基准测试分数和 GPU 速度，可通过 sentence_transformers CrossEncoder 与 transformers ≥ v4.48 使用（可选闪存加速 flash‑attn），并且在 ONNX/量化形式下可用于 CPU/ARM。
 * [japanese-reranker-cross-encoder-base-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-base-v1) - 📥 2k / ⭐ 2 / Japanese CrossEncoder Reranker 模型（xsmall、small、base、large、BGE‑v2 m3）隐藏尺寸为 384–1024，示例推理通过 sentence_transformers 和 Hugging Face， 在 JQaRA、JaCWIR、MIRACL 和 JSQuAD 上得分 0.71–0.97+。
 * [japanese-bge-reranker-v2-m3-v1](https://huggingface.co/hotchpotch/japanese-bge-reranker-v2-m3-v1) - 📥 2k / ⭐ 15 / 一个日语 CrossEncoder 重新排序器套件——包括 xsmall、small、base、large 和 japanese‑bge‑reranker‑v2‑m3‑v1——配合示例用法、在多个基准上的评估指标和支持文档。
 * [japanese-reranker-tiny-v2](https://huggingface.co/hotchpotch/japanese-reranker-tiny-v2) - 📥 2k / ⭐ 6 / 紧凑、高速的日语重排序库（v2）提供 tiny‑through‑base 和 cross‑encoder 模型，并给出详细的延迟与准确率统计，要求 Transformers ≥ 4.48（可选 Flash‑Attention 2），支持 ONNX/量化，适用于 CPU/ARM 部署。
 * [japanese-reranker-cross-encoder-large-v1](https://huggingface.co/hotchpotch/japanese-reranker-cross-encoder-large-v1) - 📥 1k / ⭐ 16 / 日语 CrossEncoder 重排序模型——从xsmall到large——在日语文本上训练，通过sentence_transformers公开，评估在JQaRA、JaCWIR、MIRACL和JSQuAD上。
 * [japanese-reranker-base-v2](https://huggingface.co/hotchpotch/japanese-reranker-base-v2) - 📥 1k / ⭐ 7 / 一个日本 Reranker v2 套件，发布 CrossEncoder 和 base 模型，覆盖从 tiny 到 large，每个都有基准得分和 GPU 推理时间，并要求 HuggingFace Transformers ≥ 4.48（可选 flash‑attn 用于更快推理）。

### translation
 * [vntl-llama3-8b-v2-gguf](https://huggingface.co/lmg-anon/vntl-llama3-8b-v2-gguf) - 📥 894k / ⭐ 14 / 一个基于新 VNTL 数据集构建的 LLaMA 3 Youko qlora 微调模型，优化用于准确、逐字翻译日本视觉小说为英文，不使用聊天模式，采用默认 LLaMA 3 提示，并推荐中性采样（温度 0，无重复惩罚）。
 * [Sugoi-14B-Ultra-GGUF](https://huggingface.co/sugoitoolkit/Sugoi-14B-Ultra-GGUF) - 📥 212k / ⭐ 11 / Sugoi LLM 14B Ultra (GGUF) 是一个日语到英语的翻译模型，BLEU 分数为 21.38，几乎是其之前的 13.67 的两倍，在 RPG‑Maker 括号文本、提示遵循强度以及为交互式聊天 UI 的 JSON 输出方面表现出色。
 * [opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) - 📥 43k / ⭐ 74 / 来自 Opus 语料库的日语‑英语 Transformer‑Align 机器翻译模型，使用归一化和 SentencePiece 预处理，在 Tatoeba 测试集上达到了 41.7 BLEU 和 0.589 chr‑F。
 * [fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 📥 3k / ⭐ 33 / FuguMT 是一个从日语到英语的 Marian‑NMT 翻译模型，使用 transformers 和 SentencePiece 构建，在 Tatoeba 上得分 39.1 BLEU。
 * [plamo-2-translate](https://huggingface.co/pfnet/plamo-2-translate) - 📥 3k / ⭐ 120 / PLaMo Translation Model 是由 Preferred Networks 创建的大规模语言模型，专用于翻译任务，提供基础版、后训练版和评估版，在 PLaMo community license 下发布，并未针对聊天或其他下游用途进行 instruction‑tuned。
 * [LFM2-350M-ENJP-MT-GGUF](https://huggingface.co/LiquidAI/LFM2-350M-ENJP-MT-GGUF) - 📥 3k / ⭐ 32 / 已微调、GGUF-量化的 LFM2-350M checkpoint，用于近实时双向日英短至中等文本翻译，可通过 llama.cpp 使用。
 * [fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 📥 2k / ⭐ 55 / FuguMT 是一个基于 Marian‑NMT 的英日翻译模型，使用 Hugging Face Transformers 和 SentencePiece 构建，并在 Tatoeba 上获得了 32.7 的 BLEU 分数。

### image-to-text
 * [manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 📥 295k / ⭐ 171 / Manga OCR 是一款 Vision Encoder‑Decoder OCR 工具，可读取纵向和横向的日语漫画文本，包括 furigana，适用于多种字体和低质量图像，并且源代码可免费获取。
 * [meiki.txt.recognition.v0](https://huggingface.co/rtr46/meiki.txt.recognition.v0) - 📥 46k / ⭐ 6 / Meikiocr的 `meiki.text.recognition.v0`——基于 D‑FINE 的 MobileNetV4 模型，在日本视频游戏文本上微调——为水平文本提供最先进的准确率和延迟，能够从 960×32 的输入中检测多达 48 个字符，并输出每个字符的边界框和置信度分数。
 * [meiki.text.detect.v0](https://huggingface.co/rtr46/meiki.text.detect.v0) - 📥 28k / ⭐ 3 / meikiocr 提供一个基于 D‑FINE、开源权重的视频游戏文本检测模型（v0.1，使用 MobileNet‑v4 骨干网络，提供两种分辨率变体和 64‑box 限制），以及实验性的低延迟 tiny 与 small 变体，训练材料来自日本视频游戏和漫画。
 * [sarashina2.2-vision-3b](https://huggingface.co/sbintuitions/sarashina2.2-vision-3b) - 📥 4k / ⭐ 17 / Sarashina2.2‑Vision‑3B 是一个 3B 参数的日本大型视觉语言模型，基于 Sarashina2.2‑3B‑Instruct 和 SigLIP 图像编码器，在日本 VQA 基准测试上表现出强劲的性能。
 * [manga-ocr](https://huggingface.co/mayocream/manga-ocr) - 📥 2k / ⭐ 2 / Manga OCR 是一种 Vision Encoder‑Decoder 系统，可在各种字体和低质量图像中提供高质量的日语漫画 OCR——包括带有假名覆盖的纵向和横向文本——并且也可用于一般印刷日语 OCR。
 * [sarashina2.2-ocr](https://huggingface.co/sbintuitions/sarashina2.2-ocr) - 📥 1k / ⭐ 30 / Sarashina2.2‑OCR 是一个 3‑B 参数的端到端 OCR 模型，经过人工偏好优化后，能够将日文和英文文档解析为 Markdown，同时将表格转换为 HTML，数学公式转换为 LaTeX，图形转换为边界框注释，其实现方式是将 SigLIP2‑基础的视觉编码器与 Sarashina2.2‑3B‑Instruct LLM 集成，从而实现高分辨率视觉‑语言理解。

### text-classification
 * [japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 📥 17k / ⭐ 15 / 训练于 chABSA 数据集的日语情感分析模型，获得 loss 0.0001、accuracy 1.0、F1 1.0，由 Transformers 4.24.0 和 PyTorch 1.12.1+cu113 构建，使用 Adam（learning rate 2e‑05、10 epochs、batch size 16）优化，并通过 `model(**inputs)` 进行评估。
 * [bert-for-japanese-twitter-sentiment](https://huggingface.co/LoneWolfgang/bert-for-japanese-twitter-sentiment) - 📥 8k / ⭐ 2 / 微调后的 BERT，用于 JTS1k 数据集上的日本推特情感分析，将推文分类为负面 (0)、中立 (1) 和正面 (2) 标签，已准备好用于 transformers pipeline.
 * [bert-base-japanese-v2-wrime-fine-tune](https://huggingface.co/patrickramos/bert-base-japanese-v2-wrime-fine-tune) - 📥 8k / ⭐ 6 / 一款在 WRIME 数据集上微调的日语 BERT BASE 可为作家和读者预测八种情绪（喜悦、悲伤、期待、惊讶、愤怒、恐惧、厌恶、信任）的 0‑4 强度得分，代码已公开，在 K80 上训练耗时 3 小时，作家的均方误差约为 0.6，读者约为 0.2。
 * [bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - 📥 5k / ⭐ 2 / 一个基于 Japanese BERT‑based model 的模型，已在 JGLUE JSTS 数据集上 fine‑tuned，用于语义相似性评分——在《Large Language Model Introduction》第5章中介绍——配有 Colab notebooks、transformers‑pipeline 用法以及 Apache 2.0 许可证。
 * [bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - 📥 4k / ⭐ 16 / 在亚马逊产品评论上对日语 BERT (cl‑tohoku/bert‑base‑japanese‑v2) 进行微调，用于情感分类，经过6个周期，学习率为2 × 10⁻⁵，达到约81 %准确率和0.73 F1。
 * [bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - 📥 1k / ⭐ 9 / 基于cl-tohoku/bert-base-japanese-v3的Japanese BERT-Base v3，在MARC-ja JGLUE情感分析数据集上微调，可与Hugging Face `pipeline` 一起使用，采用 Apache License 2.0 发布。

### token-classification
 * [MedNERN-CR-JA](https://huggingface.co/sociocom/MedNERN-CR-JA) - 📥 35k / ⭐ 4 / 一个训练于 MedTxt‑CR‑JA 的日语医学 NER 模型，配备与 HuggingFace 兼容的 predict 脚本，该脚本能够输出 XML‑tagged 文本并对实体进行规范化，同时提供可选的重新训练工具。
 * [bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 📥 19k / ⭐ 11 / 使用 cl‑tohoku/bert‑base‑japanese‑v2 的日语 NER，能够提取八种实体类型（公司、政治/其他组织、设施、产品、事件），通过 `BertForTokenClassification` 实现，训练数据来自 Stockmark Wikipedia dataset，并可通过安装 `transformers`、`unidic_lite` 和 `fugashi` 使用，遵循 CC BY‑SA 3.0 许可。
 * [deberta-v3-japanese-large](https://huggingface.co/globis-university/deberta-v3-japanese-large) - 📥 2k / ⭐ 4 / 一款面向日语的 DeBERTa V3 模型，包含 xsmall、base 和 large 这三种变体，在推理阶段不使用形态学分析器，遵循词边界，采用精简词表（仅 large 版本使用 BPE），并兼容 Hugging Face。
 * [bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - 📥 2k / ⭐ 10 / Fine‑tuned Japanese BERT‑Base适用于在维基百科数据集上的命名实体识别，该模型在《*Large Language Model Introduction*》一书第六章中呈现，并可通过Hugging Face transformers pipeline进行部署（Apache 2.0 许可）。
 * [xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - 📥 2k / ⭐ 26 / 在日语 NER 语料库上对 XLM‑RoBERTa‑base 进行微调（标签 PER, ORG, LOC, INS, PRD, EVT），使用 5‑epoch Adam（lr 5e‑5，batch 12），达到 0.0173 的验证损失，已发布在 Transformers 4.23.1 和 PyTorch 1.12.1。

### audio-to-audio
 * [Anime-XCodec2-44.1kHz-v2](https://huggingface.co/NandemoGHS/Anime-XCodec2-44.1kHz-v2) - 📥 4k / ⭐ 14 / Anime-XCodec2-44.1kHz-v2 将 16 kHz 的日语语音上采样至 44.1 kHz 的高保真音频，采用仅解码器的 RMS‑loss 微调，保持编码器/码本冻结并保留相同的语音令牌。

### text-to-speech
 * [piper-plus-tsukuyomi-chan](https://huggingface.co/ayousanz/piper-plus-tsukuyomi-chan) - 📥 3k / ⭐ 11 / 一款名为 **tsukuyomi‑wavlm** 的日本文本转语音模型——在 tsukuyomi corpus 的 100 条语句上经过 300 个周期的微调，使用 WavLM 判别器和 A1/A2/A3 声韵特征，基于 VITS 架构，导出为 61 MB 的 ONNX 文件，用以生成 22.05 kHz 的合成语音。

### image-text-to-text
 * [PaddleOCR-VL-For-Manga](https://huggingface.co/jzhang533/PaddleOCR-VL-For-Manga) - 📥 3k / ⭐ 130 / 从 PaddleOCR‑VL 微调得到的 PaddleOCR‑VL‑For‑Manga 在 Manga109 的对话框裁剪图像上实现了70%完整句子准确率—是27%基线的三倍以上—并使用多语言数据集，包含训练代码和开发者指南。

### others
 * [bert-base-japanese-char-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-char-v3) - 📥 128k / ⭐ 11 / 日本语言 BERT‑Base（12 层，768 维，12 头）使用 Unidic 基于词级加字符级分词和全词掩码在 CC‑100 及 2023 Wikipedia 上进行预训练，产生 7,027 名词表。
 * [bert-large-japanese-v2](https://huggingface.co/tohoku-nlp/bert-large-japanese-v2) - 📥 72k / ⭐ 14 / Japanese‑BERT‑Large 在 CC‑100 和 Wikipedia 上训练，使用 Unidic‑lite 单词级标记化配合 WordPiece 子词和全词掩码（24 层，1024 维隐藏层，16 头，32k 词表），预训练代码在 cl‑tohoku/bert‑japanese。
 * [bert-base-japanese-v3](https://huggingface.co/tohoku-nlp/bert-base-japanese-v3) - 📥 63k / ⭐ 63 / Japanese BERT‑base（12层，768维隐藏层，12头，32 k词汇表）在 CC‑100 和 2023‑Jan Wikipedia 上使用全词遮蔽预训练，采用 Unidic 2.1.2 词级分词加 WordPiece，训练 200 万步。
 * [t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 📥 15k / ⭐ 11 / 一个预训练在≈100 GB的维基百科和 OS CC‑100 数据（SentencePiece 采用 10:1 混合且带 byte‑fallback）的日文 T5‑v1.1 模型，需要微调以适用于下游任务，包含迁移学习示例代码，指出输出中的潜在偏差，并遵循 CC‑BY‑SA 4.0 许可。
 * [llm-jp-moshi-v1](https://huggingface.co/llm-jp/llm-jp-moshi-v1) - 📥 6k / ⭐ 39 / LLM‑jp‑Moshi‑v1 是一个实验性的日语全双工语音聊天模型，基于 7‑B 参数的 Moshi 架构构建，并使用 J‑CHAT 和 Zoom 对话数据进行微调，已在 Apache 2.0 许可证下为 Linux GPU 系统发布了 web‑UI 演示。
 * [gemma-4-E2B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E2B-it-UD-japanese-imatrix) - 📥 6k / ⭐ 1 / 经过 GGUF 转换的 Gemma‑4‑E2B‑it 模型，已细调以提升日语水平；使用 Unsloth® Dynamic Quantization 2.0 构建，已包含社区 Bug 修复和日文校准数据；可在 CPU 上运行（≥8 GB RAM，≥4 GB 磁盘），通过 llama.cpp。
 * [gemma-4-E4B-it-UD-japanese-imatrix](https://huggingface.co/dahara1/gemma-4-E4B-it-UD-japanese-imatrix) - 📥 5k / ⭐ 1 / 一个高度优化的 GGUF 版本的 google/gemma‑4‑E4B‑it，使用 Unsloth Dynamic Quantization 2.0 并进行广泛的错误修复，专为日语语言能力调优，可在 llama.cpp 上运行，至少需要 16 GB 内存和 6 GB 磁盘（GPU 可选）。
 * [Qwen3.5-4B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-4B-UD-japanese-imatrix) - 📥 4k / ⭐ 6 / Qwen3.5-4B‑UD‑japanese‑imatrix by dahara1 是一个顶尖的、面向日语的 GGUF 模型，使用 Unsloth Dynamic Quantization 2.0，配有广泛的日语校准和社区修复的错误，能够在 llama.cpp 上运行，即使没有 GPU，也只需至少 8 GB RAM 和 3 GB disk。
 * [japanese-splade-v2](https://huggingface.co/hotchpotch/japanese-splade-v2) - 📥 4k / ⭐ 17 / 高性能的日本 SPLADE v2 通过 WebUI demo 实现稀疏向量转换和推理，使用 YAST 进行训练，提供 YASEM 嵌入，并报告 JMTEB benchmark 结果。
 * [t5-small-short](https://huggingface.co/retrieva-jp/t5-small-short) - 📥 3k / ⭐ 3 / 一款使用日语维基百科和 mC4/ja 预训练的 T5 v1.1 模型，采用 GEGLU 激活函数，预训练期间不使用 dropout，未与嵌入层共享分类器，按 CC‑BY‑SA 4.0 许可证发布（商业用途须事先联系）。
 * [Llama-3.1-70B-Japanese-Instruct-2407-gguf](https://huggingface.co/mmnga/Llama-3.1-70B-Japanese-Instruct-2407-gguf) - 📥 3k / ⭐ 8 / 一个使用 gguf 格式的 cyberagent 的 Llama‑3.1‑70B‑Japanese‑Instruct‑2407 版本，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 数据构建，并通过 llama.cpp 的 CLI 运行。
 * [deberta-v3-base-japanese](https://huggingface.co/ku-nlp/deberta-v3-base-japanese) - 📥 3k / ⭐ 18 / Japanese DeBERTa V3 base 在 LLM‑jp v1.0 的 540 B tokens 上预训练，使用经过修改的 DeBERTa V3 设置训练，采用 unigram byte‑fallback tokenizer（不使用形态学分析器），并针对 JGLUE NLU 任务进行微调。
 * [Qwen3-Swallow-8B-RL-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-8B-RL-v0.2-gguf) - 📥 3k / ⭐ 1 / Qwen3‑Swallow‑8B‑RL‑v0.2 的 GGUF 格式版本，使用 imatrix 日本语 LLM 数据构建，已准备好供 CUDA 支持的 llama.cpp 使用。
 * [Llama-3-ELYZA-JP-8B-GGUF](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B-GGUF) - 📥 3k / ⭐ 73 / Llama‑3‑ELYZA‑JP‑8B 是一款经过日本增强的 8‑B Llama 3 模型，采用 GGUF (Q4_K_M) 和 AWQ 量化，支持通过 llama.cpp、LM Studio 或 OpenAI‑compatible API 运行。
 * [Moonlight-16B-A3B-Instruct-gguf](https://huggingface.co/mmnga/Moonlight-16B-A3B-Instruct-gguf) - 📥 2k / ⭐ 13 / 提供了 gguf 格式的 moonshotai 的 Moonlight‑16B‑A3B‑Instruct，已在 TFMC 的 imatrix 日语数据集上训练，准备好与 llama.cpp（CUDA‑enabled）一起使用，并通过执行 recipe‑request 提示来演示。
 * [Anime-Speech-Japanese-Refiner-i1-GGUF](https://huggingface.co/mradermacher/Anime-Speech-Japanese-Refiner-i1-GGUF) - 📥 2k / ⭐ 1 / 提供 Anime‑Speech‑Japanese‑Refiner 模型的加权/imatix GGUF 量化版本，列出量化类型和尺寸，对比图表，以及对视觉模型文件的使用指导。
 * [Qwen3.5-9B-UD-japanese-imatrix](https://huggingface.co/dahara1/Qwen3.5-9B-UD-japanese-imatrix) - 📥 2k / ⭐ 7 / 一个针对日语微调的 Qwen 3.5‑9B GGUF 模型，使用 Unsloth Dynamic Quantization 2.0、广泛的错误修复、大规模日语校准，并可通过 llama.cpp 在 CPU 上使用 16 GB RAM 和 6 GB 磁盘运行。
 * [llm-jp-4-8b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-thinking-gguf) - 📥 2k / ⭐ 13 / 这是 LLM‑JP 的 4.8‑b “thinking” 模型的 GGUF 编译版本，使用 llama.cpp 并基于 imatrix 数据集和 custom chat template 构建。
 * [AXCXEPT-EZO-phi-4-v2_900-gguf](https://huggingface.co/mmnga/AXCXEPT-EZO-phi-4-v2_900-gguf) - 📥 2k / ⭐ 1 / AXCXEPT‑EZO‑phi‑4‑v2_900‑gguf 是 EZO‑phi‑4‑v2_900 模型的 gguf 格式版本，使用 TFMC/imatrix‑dataset‑for‑japanese‑llm 的 imatrix 数据构建，可通过 llama.cpp 的 CUDA 版使用。
 * [llm-jp-4-32b-a3b-thinking-gguf](https://huggingface.co/mmnga-o/llm-jp-4-32b-a3b-thinking-gguf) - 📥 2k / ⭐ 11 / GGUF 格式转换的 llm‑jp‑4‑32b‑a3b‑thinking，使用 TFMC 的 imatrix 数据集构建，适用于通过 llama.cpp 在支持 CUDA 的推理。
 * [llm-jp-4-8b-instruct-gguf](https://huggingface.co/mmnga-o/llm-jp-4-8b-instruct-gguf) - 📥 1k / ⭐ 6 / 用于 llm‑jp‑4‑8b‑instruct gguf 格式转换的容器，基于 imatrix 数据构建，包含 LMStudio 设置和 llama.cpp CUDA 命令示例。
 * [plamo-2-translate-gguf](https://huggingface.co/mmnga/plamo-2-translate-gguf) - 📥 1k / ⭐ 22 / 由 imatrix 数据构建的 pfnet 的 plamo‑2‑translate 的 GGUF‑格式发布，基于 TFMC/imatrix‑dataset‑for‑japanese‑LLM，附带通过 llama.cpp 在启用 CUDA 的硬件上编译和运行的说明。
 * [Anime-Speech-Japanese-Refiner](https://huggingface.co/NandemoGHS/Anime-Speech-Japanese-Refiner) - 📥 1k / ⭐ 9 / Anime‑Speech‑Japanese‑Refiner 是一个通过 Qwen3‑Omni 30B 微调的模型，用于处理日语动漫/游戏语音音频，生成详细描述（情感、档案等）和带有非语音事件的精细转录，训练数据来自 Galgame Gemini Captions 数据集，最佳运行环境是 vLLM。
 * [Qwen3-Swallow-8B-SFT-v0.2-gguf](https://huggingface.co/mmnga-o/Qwen3-Swallow-8B-SFT-v0.2-gguf) - 📥 1k / ⭐ 1 / 一个 gguf‑converted Qwen3‑Swallow‑8B‑SFT‑v0.2 模型，用于日语 LLM，使用 imatrix 数据构建，配有 llama.cpp 推理指令。
 * [sarashina2.2-0.5b](https://huggingface.co/sbintuitions/sarashina2.2-0.5b) - 📥 1k / ⭐ 13 / Sarashina2.2 提供 0.5‑B、1‑B 和 3‑B 语言模型， 这些模型由 SB Intuitions 通过三阶段流水线和合成数据训练，达到了日本 QA、数学和编码的顶级成绩，同时提供的预训练权重未进行指令微调，可能产生偏见输出。
 * [Llama-3-ELYZA-JP-8B-gguf](https://huggingface.co/mmnga/Llama-3-ELYZA-JP-8B-gguf) - 📥 1k / ⭐ 4 / 由 elyza 制作的 GGUF 转换版 Llama‑3‑ELYZA‑JP‑8B，使用 TFMC/imatrix‑dataset‑for‑japanese‑LLM 构建，已准备好与 llama.cpp 一起使用。
 * [nekomata-7b-instruction-i1-GGUF](https://huggingface.co/mradermacher/nekomata-7b-instruction-i1-GGUF) - 📥 1k / ⭐ 1 / Weighted/imatrix 定量的 7B “nekomata‑instruction” 模型可作为 GGUF 文件提供（不同 IQ 和 Q 等级，大小为 2.1–6.4 GB），并附带使用说明链接至 TheBloke READMEs、比较图表，以及 HuggingFace 模型请求页面以获取进一步支持。
 * [sarashina2.2-3b-instruct-v0.1-gguf](https://huggingface.co/mmnga/sarashina2.2-3b-instruct-v0.1-gguf) - 📥 1k / ⭐ 8 / 一个 GGUF 格式的 sbintuitions 的 sarashina2.2-3b-instruct-v0.1 模型转换，使用 TFMC/imatrix-dataset-for-japanese-llm 构建，准备通过 llama.cpp 进行 CUDA 启用推理。

## Datasets
 * [KakologArchives](https://huggingface.co/datasets/KakologArchives/KakologArchives) - 📥 3M / ⭐ 47 / 聚合了2009年至2024年NicoNico Live的评论日志，总计超过150 GB，包括转移前、转移后以及实时NX‑Jikkyo捕获，提供了一个API，便于检索历史电视广播讨论。
 * [Cauldron-JA](https://huggingface.co/datasets/turing-motors/Cauldron-JA) - 📥 19k / ⭐ 9 / Cauldron‑JA 是一个日语视觉‑语言数据集，包含 44 个子数据集，使用 DeepL API 从 The Cauldron 翻译而来，可通过 HuggingFace’s datasets library 获取，并与原始数据集使用相同的许可证，prompts 在 CC‑BY‑4.0 下发布。
 * [financial-lakehouse](https://huggingface.co/datasets/Yoshi-Dai/financial-lakehouse) - 📥 13k / ⭐ 4 / 一个受限、非商业派生数据集，基于 EDINET XBRL 财务数据，禁止再分发、AI 训练和商业用途，请求访问需人工批准。
 * [WAON](https://huggingface.co/datasets/speed/WAON) - 📥 7k / ⭐ 2 / WAON 是一个大型、高质量的日语图文配对数据集，采用尺寸、SigLIP‑score 过滤和去重（按 URL、标题和 pHash）构建，并在 HuggingFace 上以 Apache 2.0 许可证公开，用于信息分析。
 * [emb](https://huggingface.co/datasets/hpprc/emb) - 📥 6k / ⭐ 16 / 一份日语和多语种 QA、NLI 与同义句重述数据集的目录，详细说明每个数据集的检索或问答任务及其许可（Apache 2.0、CC‑BY‑SA/CC‑BY、MIT 等）。
 * [JMedBench](https://huggingface.co/datasets/Coldog2333/JMedBench) - 📥 5k / ⭐ 7 / JMedBench 是一个日语生物医学 LLM 基准，涵盖 20 个数据集，覆盖五个任务（MCQA、NER、STS 等），来源于 MedMCQA、PubMedQA、MMLU 等，每个都有自己的许可，并包含一条说明：翻译可能包含偏差，需要人工审核。
 * [mc4-ja](https://huggingface.co/datasets/izumi-lab/mc4-ja) - 📥 4k / ⭐ 6 / 日本 MC4 数据集卡 (mc4-ja)
 * [JMTEB](https://huggingface.co/datasets/sbintuitions/JMTEB) - 📥 4k / ⭐ 18 / JMTEB 是一个日本文本嵌入基准，包含 5 个任务（聚类、分类、STS、检索、再排序）和 28 个数据集，提供一行评估脚本，并邀请社区贡献。
 * [Japanese-Medical-VQA-12m](https://huggingface.co/datasets/MIL-UT/Japanese-Medical-VQA-12m) - 📥 4k / ⭐ 6 / Japanese Medical VQA 12M 是一个可商业使用的多模态数据集，包含超过 1200 万张日语医学图像和标题，源自 Open‑PMC‑18M，采用 Parquet/Webdataset 格式，并包含原始和日语翻译图像、增强后的标题以及使用 InternVL3.5、Qwen3‑30B 和 GPT‑oss 120B 生成的 VQA 风格问答对。
 * [Nemotron-Personas-Japan](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Japan) - 📥 4k / ⭐ 117 / Nemotron‑Personas‑Japan 是一个开放源代码、CC BY 4.0 许可证的高质量、合成生成的日本人物资料数据集—包含姓名、性别、年龄、背景、婚姻状况、教育、职业和地点—基于真实世界的人口统计、地理和人格分布，并采用概率图模型和 GPT‑OSS‑120B 进行工程设计，以提升多样性、降低偏见、防止模型崩溃、支持主权 AI 发展，并支持商业使用。
 * [japanese-anime-speech-v2](https://huggingface.co/datasets/joujiboi/japanese-anime-speech-v2) - 📥 4k / ⭐ 140 / Japanese Anime Speech Dataset V2 提供 292,637 条已清洗的音频-文本对——约 397.5 小时的 SFW 内容和 52.4 小时的 NSFW 内容——以 128‑kbps MP3 文件形式按安全级别划分，专为训练自动语音识别模型而设计。
 * [emilia-yodas](https://huggingface.co/datasets/TTS-AGI/emilia-yodas) - 📥 3k / ⭐ 5 / 来自 Fate/Stay Night 的角色 “Emilia” 的对话和背景故事数据集，格式化用于训练和评估会话语言模型。
 * [fineweb-2-edu-japanese](https://huggingface.co/datasets/hotchpotch/fineweb-2-edu-japanese) - 📥 3k / ⭐ 29 / FineWeb2 Edu Japanese 提供约120 million高质量教育日语文本（≈89.3 billion tokens）来自 FineWeb2，经过 DeepSeek‑API classifier（score ≥ 2.5）过滤，通过 ModernBERT‑Ja‑130M tokenized，并包含一个小-token子集（≤512 tokens）。
 * [ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - 📥 3k / ⭐ 99 / 一个包含100个样本的日语指令微调评估数据集，包含已注释的任务——从摘要校正、数学推理到翻译、创意生成和用户意图理解——旨在对微调模型进行手动或自动的5分制评分。
 * [aozorabunko-clean](https://huggingface.co/datasets/globis-university/aozorabunko-clean) - 📥 3k / ⭐ 43 / 一个用户友好、去重的 CSV 数据集，包含 Aozora Bunko 的公有域日语文本，使用 globis‑org/aozorabunko‑extractor 处理，并已清理以适用于现代日语机器学习。
 * [reranker-scores](https://huggingface.co/datasets/hpprc/reranker-scores) - 📥 3k / ⭐ 4 / 提供了一个日语搜索/问答数据集，其中包含按查询计算的分数，这些分数是由五个多语言/日语重排序器（例如 BAAI/bge‑reranker‑v2‑m3、Alibaba‑NLP/gte‑multilingual‑reranker‑base）计算的，数据集包括每个查询约200个正例和负例文档的平均分数。
 * [kaken-trans-ja-en](https://huggingface.co/datasets/hpprc/kaken-trans-ja-en) - 📥 3k / ⭐ 10 / 一份将 llm‑jp‑corpus‑v3 的 kaken 子集译为日英的日英平行语料库，使用 Qwen/Qwen2.5‑32B‑Instruct，包含自定义翻译列，并在 CC‑BY‑4.0 许可下授权。
 * [jawiki](https://huggingface.co/datasets/hpprc/jawiki) - 📥 2k / ⭐ 18 / 一份 NLP‑ready dataset，包含从 2024 年 1 月的 HTML dump 中提取的 Wikipedia articles，保留段落结构、元数据（如 disambiguation、sexual、violent flags、templates、timestamps）以及托管在 GitHub 上的 extraction scripts。
 * [paraphrase-qa](https://huggingface.co/datasets/hpprc/paraphrase-qa) - 📥 2k / ⭐ 2 / 由重述过的维基百科文本生成的LLM生成的日语查询和答案的数据集，采用CC‑BY‑SA 4.0发布。
 * [qg_jaquad](https://huggingface.co/datasets/lmqg/qg_jaquad) - 📥 2k / ⭐ 5 / Japanese JaQuAD，QG‑Bench 的一个子集，提供句子级和段落级的数据，包含高亮的答案词元，用于训练日语问句生成模型，并通过 BLEU4、METEOR、ROUGE‑L、BERTScore 和 MoverScore 进行评估。
 * [reazon-speech-v2-clone](https://huggingface.co/datasets/litagin/reazon-speech-v2-clone) - 📥 2k / ⭐ 11 / Reazon Speech v2 Japanese dataset 在 Hugging Face 上的镜像，分发依据 CDLA-Sharing-1.0，使用受限于日本著作权法第30‑4条，包含 4,096 个 16 kHz FLAC 音频文件及对应的 TSV/CSV 格式转录文本。
 * [oscar_2023_filtered](https://huggingface.co/datasets/if001/oscar_2023_filtered) - 📥 2k / ⭐ 3 / 从 Hugging Face (if001/oscar_2023_filtered) 加载 312,396 行过滤后的 Oscar 2023 数据集，并在 if001/HojiChar_OSCAR_sample GitHub 仓库中提供示例代码。
 * [Japanese-Eroge-Voice-V2](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice-V2) - 📥 2k / ⭐ 48 / Japanese‑Eroge‑Voice‑V2 提供 2,657 小时匿名 1,033,142 对 eroge 音频-转录配对（主要为女性，含 NSFW），MIT 许可用于学术研究。
 * [japanese-anime-speech](https://huggingface.co/datasets/joujiboi/japanese-anime-speech) - 📥 1k / ⭐ 153 / 日本动漫语音数据集提供73,004对音频-文本（总计110小时，已从V1升级至V5），用于提升ASR模型，例如OpenAI的Whisper，按开放许可证提供给所有使用，欢迎署名。
 * [Voice-KusanagiNene](https://huggingface.co/datasets/MomoyamaSawa/Voice-KusanagiNene) - 📥 1k / ⭐ 18 / 包含草薙寧々（来源 CV Machico）的 *Project Sekai* 歌声轨的部分数据集，附带 nene_org.txt 标注文件，计划扩充并标准化数据，并呼吁用户点星此 repo、分享想法、加入 QQ 群以获取完整收藏。
 * [JamC-QA](https://huggingface.co/datasets/sbintuitions/JamC-QA) - 📥 1k / ⭐ 4 / JamC‑QA 是一个双语基准，涵盖八个日本文化与知识类别的多项选择题，排行榜指标用于比较最先进模型。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/kunishou/databricks-dolly-15k-ja) - 📥 1k / ⭐ 89 / 一个自动翻译的日语版本的databricks‑dolly‑15k数据集，许可为CC‑BY‑SA‑3.0，最后更新于2023‑05‑11。
 * [ABEJA-CC-JA](https://huggingface.co/datasets/kajuma/ABEJA-CC-JA) - 📥 1k / ⭐ 2 / Hugging Face 镜像版 ABEJA‑CC‑JA 开源数据集，来自 AWS（https://registry.opendata.aws/abeja-cc-ja/），详细信息见 Abeja 的技术博客。
 * [Japanese-Eroge-Voice](https://huggingface.co/datasets/NandemoGHS/Japanese-Eroge-Voice) - 📥 1k / ⭐ 33 / 一个时长为409小时的日本 eroge 语音数据集，使用 2-pass loudnorm（‑23 LUFS，‑1 dB 峰值，11 LRA）处理，已由 litagin/anime-whisper 转录、匿名化，存储为 WebDataset（FLAC、JSON、TXT），主要包含女性声音，可能存在 AI 转录错误，并采用 MIT 许可证用于学术研究。
 * [Jagle](https://huggingface.co/datasets/llm-jp/Jagle) - 📥 978 / ⭐ 14 / Jagle 是一个约 920 万实例的日本多模态后训练数据集，构建自图像–文本对和 PDF 文本，用于训练 LLM‑jp‑4‑VL 9B beta，并已被证明能提升日语视觉语言任务性能。
 * [JGLUE](https://huggingface.co/datasets/shunk031/JGLUE) - 📥 964 / ⭐ 47 / 更新了 JGLUE 数据集卡与加载脚本，适用于由 Yahoo Japan 与早稻田大学创建的日语 NLP 基准，涵盖文本分类（MARC‑ja、JCoLA）、句对分类（JNLI）以及问答（JSQuAD、JCommonsenseQA），发行链接保存在 GitHub 与 Hugging Face 上。
 * [JMMLU](https://huggingface.co/datasets/nlp-waseda/JMMLU) - 📥 910 / ⭐ 13 / JMMLU 是一个日语大型多任务语言理解基准（Benchmark），包括 7,536 道教师精心制作的问题，覆盖 56 个学科，包括专业医学、心理学、会计、哲学以及各种高中学科。
 * [ApolloCorpus-ja](https://huggingface.co/datasets/kunishou/ApolloCorpus-ja) - 📥 900 / ⭐ 4 / 一份 525k 条目日语指令调优集，自动从 ApolloCorpus 的英文医学文件 “medicalPaper_en_qa.json” 翻译而来，提供高质量但不完美的医学数据集，供日语语言 LLMs 谨慎使用。
 * [scaling-data-constrained-llms](https://huggingface.co/datasets/llm-jp/scaling-data-constrained-llms) - 📥 876 / ⭐ 2 / 用于扩展受数据限制的日语LLM的预训练语料库，包含有机日语/英语网络数据集（9B-令牌 JA-WEB-9B，63B-令牌 EN-WEB-63B/JA-WEB-63B）以及合成集（Qwen3-14B，JA-PARAPHRASE-63B，JA-INSTRUCT-63B，JA-TRANSLATE-63B），这些被用于 EACL 2026 研究。
 * [cc100-ja-documents](https://huggingface.co/datasets/hotchpotch/cc100-ja-documents) - 📥 875 / ⭐ 4 / 将行分割的 cc100‑ja 数据合并为 HuggingFace 的文档单元，同时保留原始 CC100 许可证。
 * [STAIR-Captions](https://huggingface.co/datasets/shunk031/STAIR-Captions) - 📥 829 / ⭐ 5 / STAIR‑Captions，发布于2017年，提供820,310条日语字幕，用于字幕生成、多模态检索和图像生成，并配有详细注释、元数据以及Creative Commons BY‑4.0 license。
 * [reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - 📥 819 / ⭐ 117 / ReazonSpeech 是一个免费、FLAC 编码的日语语音语料库，附带转录，提供五种规模，从 8.5 h 到 35,000 h，可通过 Hugging Face 下载，遵循 CDLA‑Sharing‑1.0 许可证，且使用受到《日本著作权法》第30‑4条的限制。
 * [anime-with-caption-cc0](https://huggingface.co/datasets/alfredplpl/anime-with-caption-cc0) - 📥 819 / ⭐ 22 / AI生成的动漫插图，使用英文提示，并基于Phi‑3 Vision的字幕（英文和日文），已发布到公共领域，供免费使用。
 * [Synthetic-JP-Conversations-Magpie-Nemotron-4-10k](https://huggingface.co/datasets/Aratako/Synthetic-JP-Conversations-Magpie-Nemotron-4-10k) - 📥 781 / ⭐ 11 / 一个约10,000条样本的日语指令微调数据集，使用 Magpie 的方法在 DeepInfra 上对 nvidia/Nemotron‑4‑340B‑Instruct 处理生成，包含创建代码但未做后置过滤，因此可能存在一些低质量记录。
 * [JMMMU](https://huggingface.co/datasets/JMMMU/JMMMU) - 📥 761 / ⭐ 19 / JMMMU 是一个日语多模态基准，已扩大十倍至 1,320 个具有文化多样性的问题（720 个与文化无关，600 个与文化相关），由母语专家翻译，现在设有公开排行榜。
 * [JAMMEval](https://huggingface.co/datasets/llm-jp/JAMMEval) - 📥 754 / ⭐ 5 / JAMMEval 是七个日本 VQA 数据集的精炼基准，经过两轮人工注释以消除歧义和非视觉问题，能够为多模态日本任务提供对视觉‑语言模型的可靠评估。
 * [wikipedia-ja-20230101](https://huggingface.co/datasets/range3/wikipedia-ja-20230101) - 📥 730 / ⭐ 6 / Range3 的 wikipedia‑ja‑20230101 仓库提供只包含日语维基百科文本的 Parquet 文件，这些文件是从完整维基百科数据集中提取的，并使用 Python 代码生成。
 * [Galgame_Speech_SER_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_SER_16kHz) - 📥 730 / ⭐ 17 / Galgame_Speech_SER_16kHz 是一份 3.7 百万文件（5,353 小时，104 GB）的情感语音数据集，源自 Galgame_Speech_ASR_16kHz，由本地 LLM 注释，按 GNU GPL v3.0 发行，禁止商业使用，并要求基于它训练的模型保持开源且无需强制引用。
 * [EliteVoiceProject](https://huggingface.co/datasets/Elite35P-Server/EliteVoiceProject) - 📥 724 / ⭐ 13 / Hololive VTuber 樱井美子（Sakura Miko）语音的非官方数据集，用于语音识别研究，按来源平台组织并划分为训练/测试文件夹，遵循 Hololive 的粉丝创作准则授权，所有权归 Cover Corporation 所有。
 * [AItuber-Persona-Voices-JA](https://huggingface.co/datasets/kizuna-intelligence/AItuber-Persona-Voices-JA) - 📥 721 / ⭐ 5 / 20,800 文件的 WAV 数据集，包含 195 位日本 AItuber 人格——包括参考、原始、描述性和情感性发言，并提供详细的人格和声音元数据，准备通过数据科学 APIs 检索。
 * [reazon-speech-v2-denoised](https://huggingface.co/datasets/litagin/reazon-speech-v2-denoised) - 📥 700 / ⭐ 17 / Reazon Speech v2 数据集的镜像发布，包含已通过 UVR 去噪并去除背景音乐的音频文件（在八块 A800 GPU 上大约十天内处理了 4096 个文件中的 3674 个）。
 * [mc4-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/mc4-ja-filter-ja-normal) - 📥 698 / ⭐ 5 / 数据集卡片详细说明了日语变体 “mc4‑ja‑filter‑ja‑normal”，后续信息正在待补充。
 * [Knowledge-QA-MultiTurn-Dataset](https://huggingface.co/datasets/DataPilot/Knowledge-QA-MultiTurn-Dataset) - 📥 692 / ⭐ 2 / 一个 3‑轮日语知识问答数据集（约 3,000 条 JSONL 条目），使用 SDG‑LOOM 流程创建，DeepSeek V3.2 用于问题细化和后续提问，Kimi K2.5 用于答案生成，并动态标注推理难度标签，按 ODC‑BY 许可。
 * [Hachi-Alpaca](https://huggingface.co/datasets/HachiML/Hachi-Alpaca) - 📥 677 / ⭐ 15 / Hachi‑Alpaca 是一个由 Stanford Alpaca 使用 ‑mistralai/Mixtral‑8x22B‑Instruct‑v0.1 生成的日本合成数据集，经过该模型清洗，在 Deepinfra 上提供服务，并以 Apache‑2.0 许可证发布，供 Alpaca‑jp 研究使用。
 * [sayoko-tts-corpus](https://huggingface.co/datasets/bandad/sayoko-tts-corpus) - 📥 675 / ⭐ 5 / 该仓库托管了一位81岁日本女性的语音语料库——原始与降噪的WAV文件、音素和假名标签——可通过Google Drive链接获取，免费用于研究和商业语音合成，需要署名，但禁止直接文件链接或色情用途。
 * [cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - 📥 637 / ⭐ 24 / cc100-ja 是 cc100 数据集日语部分的集合，提供为分片的 Parquet 文件。
 * [vntl-leaderboard](https://huggingface.co/datasets/lmg-anon/vntl-leaderboard) - 📥 624 / ⭐ 43 / 将LLM按其把日语视觉小说准确翻译成英文的能力进行排名，VNTL 排行榜使用与256份参考翻译的余弦相似度（也报告了 chrF 但未进行排名），并报告初步结果，优于 Sugoi Translator、Google Translate、Papago 和 Alibaba Translate 等工具。
 * [alpaca_jp_python](https://huggingface.co/datasets/HachiML/alpaca_jp_python) - 📥 587 / ⭐ 8 / alpaca_jp_python 是用 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 创建的日本合成 Alpaca 数据集，由同一模型进行清洗，托管在 Deepinfra 上，并在 HachiML Japanese Apache 2.0 license 下发布。
 * [livedoor-news-corpus](https://huggingface.co/datasets/shunk031/livedoor-news-corpus) - 📥 586 / ⭐ 7 / Livedoor News Corpus 提供了一个日语新闻文章数据集，划分为 5,894 条训练样本、737 条验证样本和 736 条测试样本，已清除 HTML 标签，并在 Creative Commons Attribution‑NoDerivs 许可证下发布。
 * [Japanese-Novels-23M](https://huggingface.co/datasets/OmniAICreator/Japanese-Novels-23M) - 📥 583 / ⭐ 11 / 一份包含 2,300 万本个人收集的日本网络小说的数据库，总计 80.85 亿字符，仅供合法的机器学习使用，并需详细的访问请求。
 * [JaMARD](https://huggingface.co/datasets/elyza/JaMARD) - 📥 581 / ⭐ 11 / 一个高质量的合成日语数学题数据集，具有经过验证的思考链推理，采用 Qwen2‑7B‑Instruct 翻译 PRM800K 和 GSM8K 并进行正确性筛选后构建，可通过 Hugging Face 数据集库获取。
 * [JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - 📥 577 / ⭐ 12 / JaQuAD 是 2022 年的日语 QA 数据集，包含 39,696 对 SQuAD‑style 的抽取式问题‑答案对，取自 Wikipedia，文件总大小 73.2 MB。使用 BERT‑Japanese 微调时，获得 78.92 % F1（63.38 % EM）。
 * [Galgame-VisualNovel-Reupload](https://huggingface.co/datasets/joujiboi/Galgame-VisualNovel-Reupload) - 📥 577 / ⭐ 34 / 为高效加载 Hugging Face datasets，重新结构化并重新上传 Galgame VisualNovel 数据集（OOPPEENN/5669737465666C656E63655F44617461337072657330），保留所有原始 audio/text，并提供带多种 game-subset 选项的 extraction script。
 * [wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - 📥 548 / ⭐ 11 / Range3/wiki40b‑ja 托管了 wiki40b 数据集的日语子集，作为由 Python 数据处理管道生成的三个 Parquet 文件。
 * [rakuda-questions](https://huggingface.co/datasets/yuzuai/rakuda-questions) - 📥 533 / ⭐ 8 / Rakuda 提供 40 道日语问题——开放式的历史、社会与政府问题，以及针对地理的特定问题——用于对日本 AI 助手进行基准测试，类似于 vicuna‑eval，并且可以使用 `datasets.load_dataset` 加载。
 * [nri-fin-reasoning](https://huggingface.co/datasets/nri-ai/nri-fin-reasoning) - 📥 533 / ⭐ 3 / 日语指令数据集，具有 632,636 条多轮样本（约 6.35 B 个 token），并包含 GPT‑OSS‑120b 的推理轨迹，用于跨 135 个金融主题和 20 个通用主题的开放式、数学、写作和 MCQA 任务，旨在微调 LLM 在金融领域的推理能力。
 * [jawiki-bullet-points](https://huggingface.co/datasets/hpprc/jawiki-bullet-points) - 📥 532 / ⭐ 4 / 基于日语维基百科的项目符号数据集，使用 Apache 2.0 许可的 rinna/deepseek‑r1‑distill‑qwen2.5‑bakeneko‑32b 模型生成，并按 CC‑BY‑SA 4.0 分发。
 * [livedoor-news-corpus](https://huggingface.co/datasets/llm-book/livedoor-news-corpus) - 📥 525 / ⭐ 4 / 经过清理的 livedoor 新闻语料库子集（许可 CC BY‑ND 2.1 JP），用于《大规模语言模型导论》一书，见 llm‑book/ner‑wikinews‑dataset 卡片。
 * [Galgame_Speech_ASR_16kHz](https://huggingface.co/datasets/litagin/Galgame_Speech_ASR_16kHz) - 📥 517 / ⭐ 45 / Galgame_Speech_ASR_16kHz 是一个 16 kHz 的 ASR 数据集，包含 3.75 百万对（≈5,354 小时），源自 Galgame_Dataset，遵循 GPL v3.0，禁止商业使用，并要求任何训练的模型必须开源（可选引证）。
 * [japanese2010](https://huggingface.co/datasets/hatakeyama-llm-team/japanese2010) - 📥 500 / ⭐ 3 / A 2010 Japanese Web Corpus, uploaded to HuggingFace and licensed for research per the 2009 copyright reform, 包含来自基于形态学的解析和转换脚本的自动标点化文本。
 * [CC-news-2024-July-October-cleaned](https://huggingface.co/datasets/kajuma/CC-news-2024-July-October-cleaned) - 📥 489 / ⭐ 15 / 一份从 Common Crawl 新闻子集中使用 Uzushio 和 pipeline_03a.conf 过滤设置提取的日本新闻语料库，时间范围为 2024 年 7 月至 10 月。
 * [JA-VG-VQA-500](https://huggingface.co/datasets/SakanaAI/JA-VG-VQA-500) - 📥 477 / ⭐ 17 / JA‑VG‑VQA‑500 是日本 Visual Genome VQA 数据集的 500 份样本子集，采用 CC BY 4.0 许可，用于基准测试 EvoVLM‑JP‑v1‑7B。
 * [python-code-instructions-japanese](https://huggingface.co/datasets/ronantakizawa/python-code-instructions-japanese) - 📥 476 / ⭐ 2 / 18,612 个日语翻译的 Python 指令–响应对——使用 GPT‑4o‑mini 生成，保留原始英文提示、代码和示例——为训练、微调、聊天机器人、研究和教育提供多样化的编码任务，全部遵循 MIT 许可证发布。
 * [sentence_transformer_japanese](https://huggingface.co/datasets/hotchpotch/sentence_transformer_japanese) - 📥 465 / ⭐ 6 / 将日语数据集转换为适合 SentenceTransformers 的列，依据来自多个 HuggingFace 来源的 Rerank 分数（正样本 ≥0.7，负样本 ≤0.3）进行过滤，以支持对比学习，同时尊重原始许可证。
 * [HelpSteer2-20k-ja](https://huggingface.co/datasets/kunishou/HelpSteer2-20k-ja) - 📥 463 / ⭐ 7 / 日语翻译的HelpSteer2，NVIDIA 为 SteerLM（在 Nemotron‑4‑430B‑Reward 中使用）提供的试用数据集，以及对齐和训练资源的链接。
 * [J-HARD-TTS-Eval](https://huggingface.co/datasets/Parakeet-Inc/J-HARD-TTS-Eval) - 📥 441 / ⭐ 6 / J-HARD‑TTS‑Eval 对自回归日语 TTS 模型在短序列稳定性、重复处理和上下文完成方面的鲁棒性进行基准测试，数据集可通过 Hugging Face 获得（short, repetition, rhyme, continuation）。
 * [llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - 📥 437 / ⭐ 142 / 用于微调 LLMs（如 LoRA）的日语指令聊天数据集，包含 9 M+ 样本，最近已更新，删除授权的 Alpaca 数据，并清理了 Wikipedia 和 ALT 输出，采用 CC‑BY‑SA 4.0 许可证发布。
 * [japanese-anime-speech-v2-split](https://huggingface.co/datasets/hhim8826/japanese-anime-speech-v2-split) - 📥 434 / ⭐ 5 / 日语动漫对话数据集，来源于原始的 `joujiboi/japanese-anime-speech-v2` 集合。
 * [r1-distill-qwen-pseudo-qa](https://huggingface.co/datasets/hpprc/r1-distill-qwen-pseudo-qa) - 📥 433 / ⭐ 5 / 包含来自 DeepSeek‑R1‑Distill‑Qwen‑32B‑Japanese 的 LLM 生成问题和答案的日语维基百科问答数据集，采用 CC‑BY‑SA 4.0 许可发布。
 * [JGLUE](https://huggingface.co/datasets/llm-book/JGLUE) - 📥 424 / ⭐ 15 / 用于《大型语言模型简介》一书的 JGLUE 数据集数据卡，来源于原始仓库，代码采用 CC BY‑SA 4.0 许可证，数据按发行者的许可协议，引用 Kurihara & Kawahara（日本语），并基于 Shunsuke Kitada 的仓库构建。
 * [wikipedia-passages-jawiki-embeddings](https://huggingface.co/datasets/hotchpotch/wikipedia-passages-jawiki-embeddings) - 📥 417 / ⭐ 3 / 日语维基百科句子被转换为各种嵌入和 FAISS 索引，提供 Hugging Face Space 演示、转换脚本，以及对搜索、问答和 OpenAI text-embedding-3-small 在 RAG 中的评估；嵌入模型为 OpenAI‑licensed，其他为 CC‑BY‑SA‑4.0。
 * [MangaOCR](https://huggingface.co/datasets/hal-utokyo/MangaOCR) - 📥 415 / ⭐ 2 / 包含约20.9万条叙事文本实例的MangaOCR数据集，来自Manga109和漫画拟声词集合，具有多样化的视觉风格和布局。
 * [JCommonsenseQA](https://huggingface.co/datasets/sbintuitions/JCommonsenseQA) - 📥 407 / ⭐ 2 / JCommonsenseQA 是一份日语的多项选择常识推理数据集——CommonsenseQA 的改编版本——其授权为 CC BY‑SA 4.0，并以 doi:10.5715/jnlp.30.63 引用。
 * [nekopara-speech](https://huggingface.co/datasets/grider-transwithai/nekopara-speech) - 📥 397 / ⭐ 16 / 提供一份Nekopara音频数据集，采样率为44.1 kHz，按角色名称、音量、原文件名、转录文本以及是否成人(is_adult)进行标注，需要谨慎使用以进行NSFW过滤。
 * [bbh-ja](https://huggingface.co/datasets/pfnet/bbh-ja) - 📥 389 / ⭐ 3 / BBH‑ja提供了BIG‑Bench Hard数据集的日语翻译，提供JSON‑L（输入、正确目标）格式的评估问题以及使用PLaMo模型翻译的YAML（输入、目标）格式的Chain‑of‑Thought提示。
 * [oasst2-33k-ja](https://huggingface.co/datasets/llm-jp/oasst2-33k-ja) - 📥 382 / ⭐ 13 / LLM‑jp 提供了一个日语指令调优数据集，该数据集是 DeepL 翻译自 oasst2 的英文子集（来自 kunishou/oasst2‑135k‑ja），并由 Kiyomaru 和 Kodama 编译。
 * [oasst1-89k-ja](https://huggingface.co/datasets/kunishou/oasst1-89k-ja) - 📥 378 / ⭐ 26 / 此仓库托管了 OpenAssistant/oasst1 数据集的日语翻译，包括带有错误标记的自动翻译条目，大约 2,000 条人工修正，一个基于聊天格式的子集，以及将数据转换为用于微调的指令-输出对的脚本。
 * [japanese-text-difficulty](https://huggingface.co/datasets/ronantakizawa/japanese-text-difficulty) - 📥 377 / ⭐ 5 / 一份包含5,000条日本文本的数据集，来自Aozora Bunko，并使用jReadability进行难度评分，提供整体、汉字、词汇和详细可读性指标，用于课程设计与自适应学习。
 * [databricks-dolly-15k-ja](https://huggingface.co/datasets/llm-jp/databricks-dolly-15k-ja) - 📥 373 / ⭐ 18 / Databricks‑dolly‑15k‑ja 数据集是 DeepL 翻译的日本语版 databricks‑dolly‑15k，用于指令调优，由日本 LLM‑jp 项目创建，并由 Hirokazu Kiyomaru、Hiroshi Matsuda、Jun Suzuki、Namgi Han、Saku Sugawara、Shota Sasaki、Shuhei Kurita、Taishi Nakamura、Takashi Kodama 和 Takumi Okamoto 撰写。
 * [llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - 📥 367 / ⭐ 33 / 适用于指令-响应微调（如使用 LoRA）的日语聊天数据集，来源于 llm‑japanese‑dataset，去除日英翻译示例，提供 1.8–2.5 百万条条目，覆盖各版本发布，并以 CC‑BY‑SA 4.0 许可发行，引用 DOI 10.1109/BigData59044.2023.10386605。
 * [RyokoAI_Syosetu711K](https://huggingface.co/datasets/botp/RyokoAI_Syosetu711K) - 📥 365 / ⭐ 34 / Syosetu711K 是一个约 711,700 本小说的日本数据集，采自 2023 年 3 月 26‑27 日从 小説家になろう 抓取，提供全文及元数据（标题、作者、NCode、简介等），用于无监督文本生成和分类任务。
 * [JQaRA](https://huggingface.co/datasets/hotchpotch/JQaRA) - 📥 363 / ⭐ 20 / 一个用于评估 Retrieval‑Augmented Generation（RAG）的日语 QA 数据集，由 JAQKET 问题和 Wikipedia 段落以及金标准检索相关性标签构建，并在 HuggingFace 和 GitHub 上发布，主要依据 nDCG@10 评分。
 * [Magpie-Tanuki-8B-97k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-97k) - 📥 362 / ⭐ 12 / 一个由97,269条记录的日语对话数据集，使用Magpie的方法生成于 weblab‑GENIAC/Tanuki‑8B‑dpo‑v1.0，并未进行后期过滤，可能包含低质量条目。
 * [MOMIJI](https://huggingface.co/datasets/turing-motors/MOMIJI) - 📥 351 / ⭐ 22 / 一套来自日本网络的5600万份文档、110 B字符与2.49亿张图片，用于训练大型视觉语言模型——提供momiji_generator用于数据填充，OBELICS‑style可视化，以及示例模型（Heron‑NVILA‑Lite）。
 * [AKU-d_ms-0.5B-v0.1_dataset](https://huggingface.co/datasets/YukiTomita-CC/AKU-d_ms-0.5B-v0.1_dataset) - 📥 350 / ⭐ 4 / 提供用于训练 AKU 系列中 AKU-d_ms-0.5B-chat-v0.1 模型的 1.56 B‑token 预训练数据集（来自各种已授权公开语料库）的仓库，并附带相应的处理脚本。
 * [ScreenTalk_JA2ZH-XS](https://huggingface.co/datasets/Itbanque/ScreenTalk_JA2ZH-XS) - 📥 350 / ⭐ 3 / 10,000 份配对数据集，约30小时的日语音频与对应的简体中文文本，以 Parquet 格式存储（CC BY 4.0），专为语音转文字翻译和多语言 ASR+MT 研究设计。
 * [JA_audio_JA_text_180k_samples](https://huggingface.co/datasets/Sin2pi/JA_audio_JA_text_180k_samples) - 📥 349 / ⭐ 9 / “Regexp.ja” Wiki 页面位于 MeCab‑IPADIC‑Neologd 仓库中，说明了用于去除不必要标点并规范文本的日语正则表达式规则。
 * [japanese_alpaca_data](https://huggingface.co/datasets/fn-aka-mur/japanese_alpaca_data) - 📥 342 / ⭐ 16 / Japanese Alpaca 数据，源自 masa3141 的 Japanese Alpaca‑LoRA 工作，并引用原始仓库以获取更多细节。
 * [JEMHopQA](https://huggingface.co/datasets/sbintuitions/JEMHopQA) - 📥 341 / ⭐ 4 / 包含问题、答案以及逐步推导链接至 Wikipedia 文章的日本 Explainable Multi-hop Question Answering 数据集，已更新推导格式并发布多个版本。
 * [EDINET-Bench](https://huggingface.co/datasets/SakanaAI/EDINET-Bench) - 📥 339 / ⭐ 13 / EDINET‑Bench 是一个日本金融基准，用来评估 LLMs 在诸如会计欺诈检测、盈利预测和行业预测等任务，使用十年的 EDINET‑API 披露报告，提供构建和评估代码，并将数据集重新许可为 PDL 1.0。
 * [jhumaneval](https://huggingface.co/datasets/kogi-jwu/jhumaneval) - 📥 333 / ⭐ 7 / JHumanEval 是 HumanEval 基准的人工翻译日语版本，提供 164 个 Python 编程问题，配有并行的英文和日文注释，用于评估日语 LLM 的代码生成，同时保留原始英文错误。
 * [image-text-pairs-ja-cc0-2](https://huggingface.co/datasets/alfredplpl/image-text-pairs-ja-cc0-2) - 📥 328 / ⭐ 2 / 一份 CC‑0 日本文本‑图像数据集，使用 GPT‑OSS‑20B 构建，基于约 80 k 单词/短句，生成 1 M 和 100 k 图像，使用 Pillow/Python 并采用 Noto Sans JP 字体。
 * [Zero_SFT_Ja_v3.5](https://huggingface.co/datasets/DataPilot/Zero_SFT_Ja_v3.5) - 📥 327 / ⭐ 5 / 使用 BARE 方法生成的 108k 个日语指令‑响应对，使用 Sarashina2‑70B 处理查询、Qwen3‑235B‑A22B 处理回答，并经过 Multilingual‑E5‑Large 与 Phi‑4 过滤，输出为 JSON Lines 格式。
 * [jimba-instuction-1k-beta](https://huggingface.co/datasets/Kendamarron/jimba-instuction-1k-beta) - 📥 325 / ⭐ 6 / 这是一个日语指令数据集，手工审阅并编辑了来自 cyberagent/calm2-7b-chat 的输出（请参阅链接文章了解详细信息）。
 * [jsnli](https://huggingface.co/datasets/shunk031/jsnli) - 📥 318 / ⭐ 5 / JSNLI 是 SNLI 自然语言推理基准的日语翻译，提供为过滤与未过滤的训练和验证拆分中的形态素分割前提–假设–标签三元组的 TSV 文件，授权协议为 CC BY‑SA 4.0。
 * [ParallelFiction-Ja_En-100k](https://huggingface.co/datasets/NilanE/ParallelFiction-Ja_En-100k) - 📥 316 / ⭐ 81 / 句对齐的日本网络小说章节和英文粉丝翻译（106千章节，V2），更新了对齐，添加了系列元数据，保留了标题，无质量过滤，以 Apache 2.0 许可，按合理使用规定，并提供基于 HuggingFace 的下架程序。
 * [KokushiMD-10](https://huggingface.co/datasets/humanalysis-square/KokushiMD-10) - 📥 313 / ⭐ 7 / KokushiMD‑10 是一个多语种基准，用于十项日本国家医疗执照考试，提供日语、英语和混合语言的文本和图像多选、计算和填空题，涵盖十个职业，每个题目都有专家链式思维解释。
 * [2ch.sc](https://huggingface.co/datasets/DSULT-Core/2ch.sc) - 📥 313 / ⭐ 2 / 包含匿名 2ch.sc/2ch.net 帖子的极大压缩 JSON‑Lines 数据集，包括帖子 IDs、标题、板块与地区信息、回复计数，以及完整帖子元数据（作者、邮件、日期、内容）。
 * [msmarco-ja-hard-negatives](https://huggingface.co/datasets/hotchpotch/msmarco-ja-hard-negatives) - 📥 309 / ⭐ 3 / 一份基于 MS MARCO 翻译的日语硬负样本挖掘数据集，使用 BAAI/bge‑reranker‑v2‑m3 进行过滤和重新排序，并由 japanese‑splade‑base‑v1‑mmarco‑only 打分，显示在 0.7/0.8 阈值下，其正样本率相较于 mMARCO(ja) 显著更高（≈ 1.3–1.7 % 改善）。
 * [voicebench-ja](https://huggingface.co/datasets/sbintuitions/voicebench-ja) - 📥 306 / ⭐ 3 / 一个量化语音与文本输入在语音语言模型之间智能差距的数据集，由从 Elyza‑tasks‑100、M‑IFEval 与 JamC‑QA 基准生成的音频组成，分为四个子集，文本采用 CC‑BY‑SA 4.0 许可，音频仅限非商业用途且不可再分发。
 * [cv-corpus-17.0-ja-client_id-grouped](https://huggingface.co/datasets/masuidrive/cv-corpus-17.0-ja-client_id-grouped) - 📥 288 / ⭐ 2 / Japanese Common Voice 17.0 子集已过滤为 649 个客户端 ID，每个拥有 30–300 个样本，按 8:2 分为训练/验证集，批量为 1,000‑样本 Parquet 文件，总计 45,668 个样本（CC0 许可）。
 * [wrime-sentiment](https://huggingface.co/datasets/llm-book/wrime-sentiment) - 📥 277 / ⭐ 9 / 面向 llm‑book/wrime‑sentiment 的数据集卡，提供从 WRIME 派生的二元日语情感分析集，依据 Avg. Readers_Sentiment 标记为正向或负向（可选包含中性案例），用于《大型语言模型导论》一书的示例数据。
 * [japan-law](https://huggingface.co/datasets/y2lan/japan-law) - 📥 269 / ⭐ 22 / 日本 e‑Gov 法律数据集，每条记录提供编号、标题、唯一 ID、生效日期及全文，并已去重至 2023 年 8 月 1 日的最新生效版本。
 * [simple-zundamon](https://huggingface.co/datasets/alfredplpl/simple-zundamon) - 📥 262 / ⭐ 15 / 一个用于测试角色‑LLMs的简单 Zundamon 角色设定数据集——由线上来源和管理数据编制——以 zmnjp.jsonl 和 zmn.jsonl 格式提供，并在指定许可下发布。
 * [monster-girl-encyclopedia-stories](https://huggingface.co/datasets/lemonilia/monster-girl-encyclopedia-stories) - 📥 259 / ⭐ 3 / 仅限日语的 MGE-universe 故事已预先批准并按时间顺序排序，每条故事都包含元数据（章节、标题、作者、摘要、标签、浏览量、投票数、更新时间、字节/令牌长度），并拥有多达 50 万原始文本字符，已准备好进一步处理。
 * [oasst1-21k-ja](https://huggingface.co/datasets/llm-jp/oasst1-21k-ja) - 📥 252 / ⭐ 17 / oasst1‑21k‑ja 是由 DeepL 从英文 OASST1 子集派生的日语指令调优数据集，透过日本 LLM‑jp 合作项目创建；请联系 llm‑jp@nii.ac.jp，作者包括 Kiyomaru、Matsuda、Suzuki、Han、Sugawara、Sasaki、Kurita、Nakamura、Kodama 和 Okamoto。
 * [japanese-corpus-categorized](https://huggingface.co/datasets/kanhatakeyama/japanese-corpus-categorized) - 📥 246 / ⭐ 3 / 一个清理过的日语网络语料库（例如 mc4‑ja），通过无监督学习聚成大约10,000组，可用于合法分析，只在“out”文件夹中列出一些 Parquet 格式的文件，并可通过 Git LFS 下载。
 * [gendec-dataset](https://huggingface.co/datasets/tarudesu/gendec-dataset) - 📥 242 / ⭐ 3 / 一份包含 64,139 条标注有生物性别的日语姓名的数据集，呈现为汉字、假名和平罗马字，其 44.9k 训练集、6.41k 验证集和 12.8k 测试集划分已在 ISDA’23 被接受。
 * [oscar2301-ja-filter-ja-normal](https://huggingface.co/datasets/izumi-lab/oscar2301-ja-filter-ja-normal) - 📥 240 / ⭐ 6 / 数据集简介：“oscar2301‑ja‑filter‑ja‑normal”，是 Oscar 语料库的日语过滤版和普通子集。
 * [JA-Multi-Image-VQA](https://huggingface.co/datasets/SakanaAI/JA-Multi-Image-VQA) - 📥 237 / ⭐ 10 / JA‑Multi‑Image‑VQA 是一个包含 39 张图像、55 道题目的数据集，其中包含手工制作的日语问答，适用于多图像 VQA，通过 load_dataset 访问，文本部分采用 Apache 2.0 许可（图像受限）。
 * [JMMMU-Pro](https://huggingface.co/datasets/JMMMU/JMMMU-Pro) - 📥 233 / ⭐ 9 / JMMMU‑Pro 是一个通过 Vibe Construction 构建的日语多模态基准——结合生成建模和人工验证——用于生成低成本、高质量的 image‑QA 数据，以揭示开源 LMMs 的缺陷并引领未来 VQA 研究。
 * [AdTEC](https://huggingface.co/datasets/cyberagent/AdTEC) - 📥 232 / ⭐ 2 / 一个日语在线广告数据集，包含五个 NLP 任务——ad acceptability、consistency、performance estimation、A3 recognition 和 similarity，并以 TSV 格式提供 train/dev/test 拆分。
 * [japanese-image-classification-evaluation-dataset](https://huggingface.co/datasets/recruit-jp/japanese-image-classification-evaluation-dataset) - 📥 227 / ⭐ 7 / Recruit Co. 在一份 CC‑BY‑4.0 许可下，提供了一套包含四个以日本为中心的图像分类任务的 dataset：jafood101（101道菜）、jaflower30（30种花）、jafacility20（20种设施）以及 jalandmark10（10个地标）。
 * [snow_simplified_japanese_corpus](https://huggingface.co/datasets/SNOW-NLP/snow_simplified_japanese_corpus) - 📥 225 / ⭐ 21 / 用于日英文本简化和翻译的 SNOW T15/T23 日语简化语料库数据卡，包含 50 k 条手工对齐的原文、简化日语（≤2 k‑词汇量）和英语翻译记录，以及 35 k 条扩展集。
 * [llm-jp-instructions](https://huggingface.co/datasets/llm-jp/llm-jp-instructions) - 📥 225 / ⭐ 7 / llm‑jp‑instructions 是一个手工整理的日语指令数据集（v1.0），提供训练、验证和测试拆分，可通过 load_dataset 访问。
 * [JAQKET](https://huggingface.co/datasets/kumapo/JAQKET) - 📥 224 / ⭐ 5 / JAQKET 是一个基于维基百科的日语开放域问答数据集，提供 1.0 版包含多项选择测验题（13,061 条训练样本，271 条验证样本）以及 2.0 版仅包含需要提取答案的提问提示（2,154 条训练样本，1,164 条验证样本），旨在促进问答系统研究。
 * [Japanese-Roleplay-Dialogues](https://huggingface.co/datasets/OmniAICreator/Japanese-Roleplay-Dialogues) - 📥 224 / ⭐ 12 / 日本角色扮演对话数据集，过滤后仅包含足够长度的多发布者记录、标准化的发布者名称和均衡的主要发言者，旨在用于机器学习应用。
 * [Aya_ja](https://huggingface.co/datasets/ryota39/Aya_ja) - 📥 223 / ⭐ 4 / 来自 CohereForAI/aya_dataset 的 6,259 条手动注释的指令–响应对的日语指令数据集，可通过 Python 的 datasets.load_dataset() 使用。
 * [japanese-reasoning-dataset-sample](https://huggingface.co/datasets/APTO-001/japanese-reasoning-dataset-sample) - 📥 223 / ⭐ 3 / 一份高质量的合成推理问答对数据集，每个对准包含<think>包装的推理过程和最终答案，采用JSON形式提供，包含问题类型、答案格式和对话类型的标签，用于微调推理模型。
 * [amenokaku-code-instruct](https://huggingface.co/datasets/kunishou/amenokaku-code-instruct) - 📥 222 / ⭐ 17 / 一个聚焦于代码的5.2 k项目指令数据集，现在新增180个 JaxTon 和专业 Java 条目，包含1,050条代码生成、150条代码行为检查和4,000条代码修复记录，收集自已被翻译成日语并完全授权用于商业用途的商业许可学习内容。
 * [HelpSteer-35k-ja](https://huggingface.co/datasets/kunishou/HelpSteer-35k-ja) - 📥 213 / ⭐ 3 / 日语翻译的 NVIDIA HelpSteer 试验数据集，用于测试和对齐 SteerLM，并附带 SteerLM 训练资源链接。
 * [AnswerCarefully](https://huggingface.co/datasets/llm-jp/AnswerCarefully) - 📥 210 / ⭐ 53 / AnswerCarefully Dataset提供日语和多语种数据，用于商业或非商业LLM安全增强，禁止任何其他用途——包括安全规避——允许带署名的衍生作品，并声明不承担因伤害或服务变更导致的责任。
 * [azurlane_voices_jp](https://huggingface.co/datasets/deepghs/azurlane_voices_jp) - 📥 208 / ⭐ 9 / 一份日语配音文本数据集，包含Azur Lane 角色的30,160 条录音（共 75.8 小时），用于单声道声音的 ASR/ASV 微调与评估。
 * [covid_tweets_japanese](https://huggingface.co/datasets/community-datasets/covid_tweets_japanese) - 📥 205 / ⭐ 2 / COVID‑19 日本推特数据集提供了日本推文 ID 与评估码（63–68），用于标识 COVID‑19 相关性以及事实/观点状态，从而支持文本分类研究。
 * [WildGuardTestJP](https://huggingface.co/datasets/sbintuitions/WildGuardTestJP) - 📥 202 / ⭐ 3 / WildGuardTestJP 是一个包含 1,725 个样本的日语评估数据集，经过多阶段精炼管道（Seed‑X‑PPO‑7B、gpt‑oss‑120b、Qwen2.5‑72B‑Instruct、gemma‑3‑27b‑it）忠实翻译自 WildGuardTest，并以 ODC‑BY 许可证在 Hugging Face 上发布。
 * [arknights_voices_jp](https://huggingface.co/datasets/deepghs/arknights_voices_jp) - 📥 201 / ⭐ 3 / Arknights Waifus的JP语音文本数据集：10,905个日语语音片段（总计26.3小时），来自单一角色，适用于微调或评估ASR/ASV模型。
 * [wikipedia-ja-20230720](https://huggingface.co/datasets/izumi-lab/wikipedia-ja-20230720) - 📥 200 / ⭐ 13 / ‘wikipedia-ja-20230720’ 日本维基百科快照的数据集卡。
 * [Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k-formatted](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k-formatted) - 📥 195 / ⭐ 11 / 日本角色扮演数据集已从约19,800例扩展到约39,600例，采用 GPT‑4o‑mini ，格式化时添加了系统消息，授权协议为 CC‑BY‑NC‑SA 4.0，且不允许构建与 OpenAI 服务竞争的模型。
 * [u4-table-cell-qa](https://huggingface.co/datasets/stockmark/u4-table-cell-qa) - 📥 195 / ⭐ 2 / 一个多模态日语表格问答数据集，用于直接从年度证券报告表格中提取单元格值，提供图像、带边界框的 OCR 文本、问题和答案，并遵循 CC‑BY‑4.0 许可。
 * [Japanese-wiki-dump-sentence-dataset](https://huggingface.co/datasets/AhmedSSabir/Japanese-wiki-dump-sentence-dataset) - 📥 194 / ⭐ 7 / 一个包含五百万句、干净的日语完整句子上下文的数据集，非常适合无监督语义相似度学习。
 * [JDocQA](https://huggingface.co/datasets/shunk031/JDocQA) - 📥 194 / ⭐ 11 / 日本文档问答（JDocQA）是一个大规模的基于 PDF 的 QA 数据集，包含 5,504 篇文件和 11,600 条标注的日语问答对，涵盖了是/否、事实性、数值以及开放式问题，包括不可回答实例，旨在评估对视觉与文本内容的复杂理解。
 * [girlsfrontline_voices_jp](https://huggingface.co/datasets/deepghs/girlsfrontline_voices_jp) - 📥 194 / ⭐ 9 / 日本《Girls Front Line》Waifu 语音文本数据集：12,508 条单声道女角色录音（20.9 小时），非常适合 ASR/ASV 微调与评估。
 * [Japanese-Heron-Bench](https://huggingface.co/datasets/turing-motors/Japanese-Heron-Bench) - 📥 193 / ⭐ 11 / Japanese‑Heron‑Bench 提供了21张带有文化标签的日本图片，并包含102个问答，覆盖 Conversation、Detail、Complex 三个类别，已针对日本视觉语言模型进行基准测试。
 * [AnimuSubtitle-JP](https://huggingface.co/datasets/KaraKaraWitch/AnimuSubtitle-JP) - 📥 192 / ⭐ 4 / AnimuSubtitle‑JP 是一个使用 Advanced SubStation Alpha 格式的日语字幕数据集，可通过 Python ‘ass’ 库或像 Aegisub 这样的编辑器使用，并以 ODC‑By 许可授权。
 * [CCMatrix-v1-Ja_Zh-filtered](https://huggingface.co/datasets/larryvrh/CCMatrix-v1-Ja_Zh-filtered) - 📥 191 / ⭐ 11 / 从 CCMatrix v1 过滤的日语/中文双语数据，已通过正则表达式和长度检查去除异常对，裁剪到 LaBSE 语义相似度 0.6，并使用 zhconv 将所有繁体中文文本转换为简体中文。
 * [jaCappella](https://huggingface.co/datasets/jaCappella/jaCappella) - 📥 190 / ⭐ 5 / 一套日语无伴奏合唱声乐数据集，包含六声部（领唱、女高音、女中音、男中音、低音和打击乐），附有谱面、分离录音以及按流派划分的子集，包括爵士、朋克摇滚、波萨诺瓦、流行音乐、雷鬼、恩卡、中性、叙事歌、EDM 和灵魂/放克。
 * [auto-wiki-qa](https://huggingface.co/datasets/cl-nagoya/auto-wiki-qa) - 📥 190 / ⭐ 24 / AutoWikiQA 是最大的免费日语问答数据集，提供超过 230 万个手工过滤的问答对，这些对是使用 Swallow‑MX 和 LLMs（不使用基于规则的模板）从维基百科自动生成的，用于支持知识教学和检索增强生成应用。
 * [jsick](https://huggingface.co/datasets/hpprc/jsick) - 📥 189 / ⭐ 9 / JSICK 是一份日本 NLI 和 STS 数据集，译自 SICK 语料库，包含一个压力测试集，对句对进行打乱和改写，以评估模型在词序和格助词上的敏感度，用于高级多语种组合推断。
 * [xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 📥 189 / ⭐ 6 / Japanese XL‑Sum subset 通过 PaLM‑2 15-gram 重叠过滤，包含 4,215 训练样本，758 验证样本和 766 测试样本。
 * [DEJIMA-dataset](https://huggingface.co/datasets/MIL-UT/DEJIMA-dataset) - 📥 189 / ⭐ 2 / 一份日本规模的网络数据集，包含388万张图像、LLM生成的标题和开放式问答对，已去重并添加检测标签，可提供多种变体（simple、refined、detection、all），并托管在 Hugging Face。
 * [JFWIR](https://huggingface.co/datasets/hotchpotch/JFWIR) - 📥 184 / ⭐ 4 / JFWIR 是一份从 fine‑web 教育爬虫构建的 6400 万对日语信息检索数据集，提供每个文档七种查询类型、难负样本，并在基准测试中明显优于以往基线。
 * [makise-kurisu-vn-voicelines](https://huggingface.co/datasets/zhonglongbao/makise-kurisu-vn-voicelines) - 📥 181 / ⭐ 2 / 使用 Whisper Large‑V2 从视频中转录了牧瀬红莉栖的视觉小说对话，随后用 pydub 进行拆分；未经清理的文本用于 TTS 模型训练（版权未归属）。
 * [ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset) - 📥 179 / ⭐ 14 / 一个采用 CC‑BY‑SA 3.0 许可的日语命名实体抽取数据集，来源于 Wikipedia，托管在 https://github.com/stockmarkteam/ner-wikipedia-dataset/，由 Stockmark Inc. 开发。
 * [Malum-230](https://huggingface.co/datasets/Manual-Dataset-Creation-Project/Malum-230) - 📥 179 / ⭐ 8 / Malum‑230 是一个人工制作的日语多轮对话和文章数据集，专为逻辑推理设计，适合用于预训练和后训练，并在 Japanese MT‑Bench 上使用 Qwen2.5‑7B 进行评估。
 * [JA_Emilia_Yodas_266h](https://huggingface.co/datasets/MrDragonFox/JA_Emilia_Yodas_266h) - 📥 178 / ⭐ 2 / 来自Emilia collection的266小时日语音频数据集，已由Facebook Audio Aesthetics预过滤并通过Scribe v1/ElevenLabs STT进行分类，托管在Hugging Face，并在Discord上开放协作。
 * [KokoroChat](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat) - 📥 177 / ⭐ 2 / KokoroChat 是最大的日本心理咨询对话数据集——由 480 名受过训练的辅导员进行 6,589 次角色扮演会话，每次平均 91 条发言——包含丰富、长篇对话，详细的 20 维客户反馈，并支持同理响应生成、对话评估和心理健康语言建模方面的研究，并已被 ACL 2025 接收。
 * [ja-rag-cot](https://huggingface.co/datasets/jaeyong2/ja-rag-cot) - 📥 176 / ⭐ 2 / 使用 Qwen/Qwen2‑72B‑Instruct 在 CC‑BY‑SA‑3.0/GNU Free Documentation 许可下，并得到 TPU Research Cloud 支持，对一个包含 209,496 条条目的日本维基百科数据集进行了链式思考生成处理。
 * [zenz-v2.5-dataset](https://huggingface.co/datasets/Miwa-Keita/zenz-v2.5-dataset) - 📥 174 / ⭐ 17 / 一个 1.9 亿对 JSONL 数据集，用于日语假名到汉字转换，为 zenz‑v2.5 medium、small 和 xsmall 模型提供动力，并包含 AJIMEE‑Bench 评估语料库。
 * [llm-jp-eval](https://huggingface.co/datasets/llm-book/llm-jp-eval) - 📥 173 / ⭐ 3 / 本数据集说明书用于本书《Introduction to Large‑Scale LLM II》中的 ja‑vicuna‑qa‑benchmark，并由 llm‑jp‑eval 创建，供跨数据集日语 LLM 评估使用（Apache 2.0）。
 * [wiki40b_ja](https://huggingface.co/datasets/fn-aka-mur/wiki40b_ja) - 📥 170 / ⭐ 4 / 由 Mandy Guo、Zihang Dai 和 Denny Vrandečić 撰写的 Wiki40B 数据集的重新格式化日语子集。
 * [oasst1-chat-44k-ja](https://huggingface.co/datasets/kunishou/oasst1-chat-44k-ja) - 📥 169 / ⭐ 10 / Chat‑formatted ShareGPT 数据集，来源于 oasst1‑89k‑ja，适合多轮微调，但拥有长 token 序列，需大量计算，已在 GitHub 和 HuggingFace 上提供。
 * [wrime](https://huggingface.co/datasets/shunk031/wrime) - 📥 167 / ⭐ 27 / WRIME 数据集是一个包含 42,200 条帖子的日本语集合，帖子已为作者、三位读者及其平均值标注了 Plutchik 的八种情感，结构为 40k 训练集、1.2k 验证集和 2k 测试集，用于情感分析任务。
 * [fgo_voices_jp](https://huggingface.co/datasets/deepghs/fgo_voices_jp) - 📥 167 / ⭐ 15 / 日语配音文本数据集，适用于《Fate/Grand Order》角色，共30,800条片段（约66.4小时），全部为单一演员录制，适合ASR/ASV微调和评估。
 * [JaGovFaqs-22k](https://huggingface.co/datasets/matsuxr/JaGovFaqs-22k) - 📥 163 / ⭐ 29 / 从日本政府机构网站手动提取并质控的 FAQ 数据集，采用 CC‑BY‑4.0 许可，呈现为 QA 格式并附有源 URL，供 LLM 指令微调和 RAG 测试使用，但受 PDF‑to‑text 转换的奇异现象和强烈的政府视角所影响。
 * [Tengentoppa-sft-v1.0](https://huggingface.co/datasets/DeL-TaiseiOzaki/Tengentoppa-sft-v1.0) - 📥 162 / ⭐ 21 / Tengentoppa语料库是一个大型的JSON格式日语指令遵循数据集，源自16个多样化的公开数据集，链接到处理脚本，并来源于众多开源来源。
 * [CABankSakuraCHJP](https://huggingface.co/datasets/Fhrozen/CABankSakuraCHJP) - 📥 158 / ⭐ 2 / 日语CallHome语料库：120名说话者在美国录制了200次电话通话（最长30分钟），并转录为80个训练集、20个开发测试集和100个评估测试集，录音可通过免费LDC机器人操作员获取。
 * [Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-gpt-4o-mini-39.6k) - 📥 157 / ⭐ 2 / 39,600 条人工合成的日语角色扮演对话，每条包含 5–10 回合，使用 gpt‑4o‑mini 生成，并按流派、年龄标签、世界/场景/用户/助手设置与语调进行注释，采用 OpenAI 消息格式，在 CC‑BY‑NC‑SA 4.0 许可证下提供，禁止与 OpenAI 竞争的模型使用。
 * [wikipedia-human-retrieval-ja](https://huggingface.co/datasets/baobab-trees/wikipedia-human-retrieval-ja) - 📥 156 / ⭐ 34 / Japanese Wikipedia Human Retrieval dataset 记录了受过培训的工作人员对 838 个已回答和 433 个未回答的日语问答对进行的手工基于维基百科的检索，定义者为 Yusuke Oda，收集、检查并格式化由 Baobab Inc. 完成。
 * [LLaVA-Pretrain-JA](https://huggingface.co/datasets/turing-motors/LLaVA-Pretrain-JA) - 📥 156 / ⭐ 4 / Japanese LLaVA Pretrain 是 DeepL 转移的本地化版本，保留 CC‑3M 和 BLIP 许可证，面向研究人员和业余爱好者构建日语多模态模型和聊天机器人。
 * [Magpie-Tanuki-8B-annotated-96k](https://huggingface.co/datasets/Aratako/Magpie-Tanuki-8B-annotated-96k) - 📥 155 / ⭐ 6 / 一份 96k 样本的数据集，已将 Magpie 应用于 Tanuki‑8B，并由 cyberagent/calm3‑22b‑chat 标注了难度、质量和任务类别标签。
 * [real-persona-chat](https://huggingface.co/datasets/nu-dialogue/real-persona-chat) - 📥 154 / ⭐ 24 / RealPersonaChat 是一个包含 14,000 条发言的日语对话语料库，收录了对话记录、说话者人物设定、BigFive 个性评分、人口统计数据以及评估评分（1–5）。可通过 Hugging Face 的 `load_dataset` 访问，但需严格遵守隐私和非冒充性合规要求。
 * [Japanese-RAG-Generator-Benchmark](https://huggingface.co/datasets/neoai-inc/Japanese-RAG-Generator-Benchmark) - 📥 147 / ⭐ 4 / Japanese RAG Generator Benchmark (J‑RAGBench) 提供了一个多分类 QA 数据集——涵盖 Integration、Reasoning、Logical、Table 和 Abstention——旨在评估日本 RAG 生成器，采用人工努力和 GPT‑4.1 构建，并在 CC BY‑SA 4.0 许可下发布。
 * [japanese_hh-rlhf-49k](https://huggingface.co/datasets/fn-aka-mur/japanese_hh-rlhf-49k) - 📥 146 / ⭐ 12 / 一个修改过的 kunishou/hh‑rlhf‑49k‑ja 版本，排除了 ng_translation = 1 的条目，并引用了原始数据集。
 * [JParaCrawl-Filtered-English-Japanese-Parallel-Corpus](https://huggingface.co/datasets/Verah/JParaCrawl-Filtered-English-Japanese-Parallel-Corpus) - 📥 145 / ⭐ 3 / 提供了一个经过清洗的日语-英语翻译语料库，并配备了微调后的 Mistral/Stable‑LM 模型，该模型对每一对进行评估，只接受高质量翻译，拒绝任何不完整、不准确或写得差劲的翻译。
 * [RAG-Evaluation-Dataset-JA](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-JA) - 📥 143 / ⭐ 33 / 通过发布数据集、自动评估框架以及 Claude 3.5‑Sonnet、GPT‑4o 等模型的比较结果，提供跨金融、电信、制造、公共、零售五个行业领域的日语 RAG 基准。
 * [shisa-pretrain-en-ja-v1](https://huggingface.co/datasets/augmxnt/shisa-pretrain-en-ja-v1) - 📥 139 / ⭐ 7 / shisa‑base‑7b‑v1 的预训练数据集，基于 DSIR 样本的 MADLAD‑400 日语/英语 tokens，比例为 90 %/10 %。
 * [hh-rlhf-12k-ja](https://huggingface.co/datasets/llm-jp/hh-rlhf-12k-ja) - 📥 139 / ⭐ 14 / 日语翻译 hh‑rlhf 人类偏好数据集的一个子集，由日本本土 LLM‑jp 合作项目使用 DeepL 生成。
 * [Synthetic-JP-EN-Translation-Dataset-Magpie-Nemotron-4-20k](https://huggingface.co/datasets/Aratako/Synthetic-JP-EN-Translation-Dataset-Magpie-Nemotron-4-20k) - 📥 139 / ⭐ 6 / 一份 20 k 日语-英语和英语-日语翻译数据集，使用 Magpie 的方法在 nvidia/Nemotron‑4‑340B‑Instruct 上通过 DeepInfra 生成，公开发布了代码但未做后期过滤，因此可能包含一些低质量记录。
 * [AutoMultiTurnByCalm3-22B](https://huggingface.co/datasets/kanhatakeyama/AutoMultiTurnByCalm3-22B) - 📥 138 / ⭐ 2 / 自动生成的多轮问答数据集：最初的问题来自公开来源，后续所有回复由 Calm3‑22b 合成，使用 Tokyo Tech 的 TSUBAME4.0 构建，并在列出的许可证下发布。
 * [japanese-photos-conversation](https://huggingface.co/datasets/llm-jp/japanese-photos-conversation) - 📥 138 / ⭐ 7 / 一个11,808个样本的多轮对话数据集，内容关于日本图片，来源于ThePioneer/japanese-photos，部分使用Azure OpenAI进行过滤，按CC‑BY‑4.0许可，并遵守OpenAI条款。
 * [arxiver_ja](https://huggingface.co/datasets/speed/arxiver_ja) - 📥 138 / ⭐ 3 / 使用 gemma‑2‑2b‑it 生成的 neuralwork/arXiv 摘要栏目的日语翻译，采用 CC BY‑NC‑SA 4.0 许可证。
 * [J-ResearchCorpus](https://huggingface.co/datasets/kunishou/J-ResearchCorpus) - 📥 137 / ⭐ 32 / J‑ResearchCorpus 提供约 3.9 亿字符的高质量日本研究论文文本，源自 1,343 个 CC‑BY‑4.0 许可来源，包括 NLP2024 会议论文和期刊文章，供语言模型预训练和 RAG 使用。
 * [oscor-2301-ja-text-content](https://huggingface.co/datasets/ayousanz/oscor-2301-ja-text-content) - 📥 137 / ⭐ 2 / 提取OSCOR‑2301‑ja JSON文件中 “content” 字段的文本，并提供一段Python脚本，用于从指定文件夹中的每个JSON文件中提取这些值。
 * [aozorabunko-clean-sin](https://huggingface.co/datasets/if001/aozorabunko-clean-sin) - 📥 131 / ⭐ 4 / AozoRABunko‑clean 数据集的分支，过滤后仅包含 meta['文字遣い種別'] 等于 '新字新仮名' 的行。
 * [oasst2-chat-68k-ja](https://huggingface.co/datasets/kunishou/oasst2-chat-68k-ja) - 📥 131 / ⭐ 8 / 一个 ChatGPT 风格的 “ShareGPT” 格式数据集（oasst2‑135k‑ja）已准备好进行多轮微调，虽然每条记录的长 token 长度需要大量计算资源，并通过 OpenAssistant Hugging Face 仓库提供指导。
 * [voicevox-voice-corpus](https://huggingface.co/datasets/ayousanz/voicevox-voice-corpus) - 📥 131 / ⭐ 7 / 一个由 Voicevox 生成的人工语音数据集，包含来自 ITA、つくよみちゃん 和 ROHAN 语料库的 445,793 个 .wav 文件，总计 577 小时 51 分钟 23 秒的音频。
 * [Synthetic-JP-Roleplay-Instruction-Nemotron-4-1k](https://huggingface.co/datasets/Aratako/Synthetic-JP-Roleplay-Instruction-Nemotron-4-1k) - 📥 130 / ⭐ 6 / 约1,000条日本角色扮演指令集，由将 Synthetic‑JP‑Roleplay‑Instruction‑Nemotron‑4 Magpie 方法应用于 NVIDIA/Nemotron‑4‑340B‑Instruct 并使用 DeepInfra 生成，包含未经过滤的数据，可能包含低质量条目。
 * [guanaco_ja](https://huggingface.co/datasets/fn-aka-mur/guanaco_ja) - 📥 129 / ⭐ 6 / 日语子集的Guanaco数据集，可与如 inu‑ai/alpaca‑guanaco‑japanese‑gpt‑1b 等仓库相媲美。
 * [Knowledge-QA-SingleTurn-Dataset](https://huggingface.co/datasets/DataPilot/Knowledge-QA-SingleTurn-Dataset) - 📥 127 / ⭐ 2 / 一份包含7,000条项目的日语单轮知识问答数据集，由Aratako/Synthetic-JP-Conversations-Magpie-Nemotron-4-10k生成，使用DeepSeek V3.2进行问题细化，并使用Kimi K2.5结合动态推理（低/中/高）来产生答案，全部以JSONL格式存储，采用ODC-BY许可证。
 * [japanese-stackexchange](https://huggingface.co/datasets/p1atdev/japanese-stackexchange) - 📥 126 / ⭐ 3 / 已处理的日本 Stack Exchange QA 数据集，包含28,428条英日问答对，提供默认和简易子集，包括帖子和答案的元数据（ID、已接受/热门答案、得分、标签、标题、正文），可通过 Hugging Face `datasets` 库读取，并按 CC BY‑SA 4.0 许可。
 * [AItuber-Personas-Japan](https://huggingface.co/datasets/DataPilot/AItuber-Personas-Japan) - 📥 126 / ⭐ 28 / 一套合成的195条 AI‑VTuber 角色数据集，使用 Kimi‑K2.5 通过 SDG‑LOOM 流水线生成，提供概念文档、系统提示和主题列表，角色由六个种子参数（流派、个性、年龄、性别表达、视觉动机、语音风格）定义，覆盖约25个流派和20种个性类型，许可为 ODC‑BY。
 * [JaCWIR](https://huggingface.co/datasets/hotchpotch/JaCWIR) - 📥 125 / ⭐ 6 / JaCWIR 是一个日语休闲网络信息检索（web IR）数据集，包含 5,000 条由 ChatGPT 生成的查询，并与来自 Hatena Bookmark 的约 500k 个标题和描述相连，可通过 BM25/embedding 重新排序并使用 MAP@10 指标进行非商业性搜索模型评估。
 * [alpaca_jp_math](https://huggingface.co/datasets/HachiML/alpaca_jp_math) - 📥 125 / ⭐ 6 / alpaca_jp_math 是一个使用 Stanford Alpaca 和 mistralai/Mixtral‑8x22B‑Instruct‑v0.1 生成的日本合成数学数据集，通过一个验证程序计算结果与文本输出在小数点后三位一致的提示进行清洗，并在 HachiML Apache 2.0 许可下发布。
 * [LLaVA-CC3M-Pretrain-595K-JA](https://huggingface.co/datasets/toshi456/LLaVA-CC3M-Pretrain-595K-JA) - 📥 124 / ⭐ 11 / LLaVA CC3M 595K 视觉指令数据集的日语翻译版本，用于多模态模型和聊天机器人的研究。
 * [Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k-formatted](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k-formatted) - 📥 123 / ⭐ 2 / 一份由 deepseek-ai/DeepSeek-V3-0324 创建的日语角色扮演数据集（20 k 样本），已重新格式化为系统消息并以 MIT 许可证发布。
 * [Longcontext-aozora-summary](https://huggingface.co/datasets/aixsatoshi/Longcontext-aozora-summary) - 📥 120 / ⭐ 6 / 来自 Aozora Bunko 语料库（globis‑university/aozorabunko-clean）的长文本生成的摘要对数据集，使用 CC BY 4.0 许可证。
 * [MGSM_ja](https://huggingface.co/datasets/sbintuitions/MGSM_ja) - 📥 119 / ⭐ 2 / 一款仅支持日语的 Hugging Face 克隆版 MGSM，MGSM 是 2021 年发布的多语言思维链语言模型，保证可复现的评估分数，并包含 SB Intuitions 修订。
 * [llmjp-kaken](https://huggingface.co/datasets/hpprc/llmjp-kaken) - 📥 119 / ⭐ 6 / 已将 llm-jp-corpus-v3 的 kaken 子集转换为 Hugging Face 格式，并在可能的情况下附加了每个 URL 检索到的文章标题，采用 CC‑BY 4.0 许可证。
 * [abc-multiple-choice](https://huggingface.co/datasets/tohoku-nlp/abc-multiple-choice) - 📥 118 / ⭐ 4 / 一个基于日本四选一测验题构建的多项选择问答数据集，使用于abc竞赛，并在GitHub托管评估脚本，仅供研究用途。
 * [LLaVA-v1.5-Instruct-620K-JA](https://huggingface.co/datasets/turing-motors/LLaVA-v1.5-Instruct-620K-JA) - 📥 118 / ⭐ 7 / Japanese LLaVA v1.5 Instruct 620K 是 655K Visual Instruct 数据集的 DeepL 翻译子集，用于研究日语大型多模态模型和聊天机器人的研究，采用 CC BY‑NC‑4.0 发布。
 * [Ideal-TSUNDERE-Loli-Girl-Japanese-v1](https://huggingface.co/datasets/Rikunarita-ORG/Ideal-TSUNDERE-Loli-Girl-Japanese-v1) - 📥 118 / ⭐ 2 / 高质量、手工制作的日语对话数据集，聚焦傲娇萝莉主题，以JSONL格式提供简短而情感丰富的交流，用于在MIT许可下微调Gemma、Qwen、Llama、Mistral和OpenHermes等聊天模型。
 * [cosmopedia-japanese-100k](https://huggingface.co/datasets/aixsatoshi/cosmopedia-japanese-100k) - 📥 114 / ⭐ 7 / Cosmopedia Japanese data 已经扩展到 100k 条记录（含提示翻译），可作为 Hugging Face 数据集以及存于仓库中。
 * [oasst2-135k-ja](https://huggingface.co/datasets/kunishou/oasst2-135k-ja) - 📥 112 / ⭐ 13 / 一个日语聊天格式的数据集，**oasst2‑chat‑68k‑ja**，来源于 DeepL‑translated OpenAssistant/oasst2，并提供将其转换为 Instruction/Output pairs 进行微调的代码。
 * [cosmopedia-100k-ja-preview](https://huggingface.co/datasets/kunishou/cosmopedia-100k-ja-preview) - 📥 112 / ⭐ 4 / 日本语自动翻译的 cosmopedia‑100k 条目，索引范围为 20k–100k（省略长文本记录），随后将与 0–20k 翻译集合并并删除，但数据集仍被归档。
 * [databricks-dolly-69k-ja-en-translation](https://huggingface.co/datasets/kunishou/databricks-dolly-69k-ja-en-translation) - 📥 108 / ⭐ 13 / 自动将 “databricks-dolly-15k” 翻译为日语，这个 69 K ja‑en 翻译数据集采用 CC BY‑SA 3.0 许可证，并在 2023‑04‑18 最后更新。
 * [Japanese_Wikipedia_Conversation](https://huggingface.co/datasets/shi3z/Japanese_Wikipedia_Conversation) - 📥 108 / ⭐ 7 / 使用GPT‑3.5‑Turbo从维基百科日语版本（izumi‑lab/wikipedia‑ja‑20230720）生成的对话文本数据集，不适合商业用途。
 * [iterative-dpo-data-for-ORPO-iter3](https://huggingface.co/datasets/Aratako/iterative-dpo-data-for-ORPO-iter3) - 📥 107 / ⭐ 3 / 由 Aratako/Self‑Instruct‑Qwen2.5‑72B‑Instruct‑60k 构建的日语偏好数据集，通过使用开发模型为每个指令生成五条响应，并用 Qwen/Qwen2.5‑72B‑Instruct‑GPTQ‑Int8 对其进行 0–5 分评分，选择得分最高作为“选定”，最低作为“拒绝”，排除平局或得分 ≤2 的情况，并受 Meta LLama 3.1 Community License、Gemma Terms of Use 和 Qwen 许可要求约束。
 * [Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k](https://huggingface.co/datasets/Aratako/Synthetic-Japanese-Roleplay-SFW-DeepSeek-V3-0324-20k) - 📥 107 / ⭐ 9 / 约20k条合成日语角色扮演数据集，由DeepSeek V3生成，包含10–20回合对话，并按类型、年龄标签、世界/场景/用户/助手设置、语调以及OpenAI消息格式进行注释，MIT许可证，便于模型训练。
 * [Japanese-Creative-Writing-39.6k](https://huggingface.co/datasets/Aratako/Japanese-Creative-Writing-39.6k) - 📥 107 / ⭐ 6 / 一个 39,600 样本的日语创意写作数据集，使用 deepseek-ai/DeepSeek-V3-0324 构建，每条记录包含两轮 OpenAI 风格消息（instruction_1/output_1 和 instruction_2/output_2），其中含有一些 NSFW 内容，并在 MIT 许可证下发布。
 * [pjsk-emu-dataset](https://huggingface.co/datasets/chitsanfei/pjsk-emu-dataset) - 📥 106 / ⭐ 11 / 2735 文件 WAV 声音数据集，适用于 so‑vits‑svc 4.0，按 CC‑BY‑NC 4.0 许可授权，仅限科研使用，需通过电子邮件申请获取。
 * [OpenMathInstruct-1-1.8m-ja](https://huggingface.co/datasets/kunishou/OpenMathInstruct-1-1.8m-ja) - 📥 105 / ⭐ 14 / 1.8 百万条日语翻译的 OpenMathInstruct‑1 数学指令调优数据集，来源于 GSM8K 和 MATH 基准问题，并配合 Mixtral‑8x7B 解决方案生成，已筛选为正确答案，并在商业 NVIDIA 许可证下发布，该许可证必须在再分发时继承。
 * [WAON](https://huggingface.co/datasets/llm-jp/WAON) - 📥 105 / ⭐ 7 / WAON 是一个大型、高质量的日语图文对数据集，专为视觉‑语言模型构建。它采用严格过滤（图像尺寸、SigLIP 分数）和去重（URL、标题、感知哈希），并在 Apache 2.0 许可证下发布，用于“信息分析”用途。
 * [wikidata-parallel-descriptions-en-ja](https://huggingface.co/datasets/Mitsua/wikidata-parallel-descriptions-en-ja) - 📥 104 / ⭐ 9 / 一个英日双语平行语料库，用于机器翻译，从 Wikidata dump 中提取并过滤成 JSONL 格式，已进行 deduplication，但仍包含一些 noise，按 CC0 1.0 发行。
