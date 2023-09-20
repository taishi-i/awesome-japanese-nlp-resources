# awesome-japanese-nlp-resources

此页面列出了注册在 [Haggingface](https://huggingface.co) 的专用于日本NLP的模型和数据集。目前，列出了137个模型和27个数据集。

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)


## Contents

 * [Models](#models)
 * [Datasets](#datasets)


## Models

 * [tsmatz/xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - xlm-roberta-ner-japanese（日语标题：日本语的命名实体识别模型）该模型是xlm-roberta-base的微调版本（预训练的跨语言RobertaModel），用于命名实体识别（NER）标记分类。
 * [jonatasgrosman/wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 用于日语语音识别的经过微调的XLSR-53大型模型，使用Common Voice 6.1、CSS10和JSUT的训练和验证数据集对facebook/wav2vec2-large-xlsr-53进行了日语微调。在使用此模型时，请确保您的语音输入采样率为16kHz。
 * [cl-tohoku/bert-base-japanese-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-whole-word-masking) - BERT基础日语（使用IPA字典，启用整词掩码）
 * [cl-tohoku/bert-base-japanese](https://huggingface.co/cl-tohoku/bert-base-japanese) - BERT基础版日语（国际音标词典）
 * [christian-phu/bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - bert-finetuned-japanese-sentiment 这个模型是在产品亚马逊评论日语数据集上对 cl-tohoku/bert-base-japanese-v2 进行微调的版本。
 * [ku-nlp/deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 日本DeBERTa V2基础模型的模型卡描述。该模型是在日本维基百科、CC-100的日本部分和OSCAR的日本部分上进行预训练的。
 * [sonoisa/sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 这是一个日本句子BERT模型。
 * [ku-nlp/deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 日语字符级DeBERTa V2基础模型模型卡描述 这是一个在日语维基百科、CC-100的日语部分和OSCAR的日语部分上预训练的日语DeBERTa V2基础模型。该模型使用字符级标记和整词掩码进行训练。
 * [cl-tohoku/bert-base-japanese-char](https://huggingface.co/cl-tohoku/bert-base-japanese-char) - BERT基础日语（字符分词）
 * [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) - Sentence BERT基础日语模型 该存储库包含了一个用于日语的Sentence BERT基础模型。
 * [kha-white/manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 漫画OCR光学字符识别，主要关注日本漫画。
 * [megagonlabs/transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - transformers-ud-japanese-electra-ginza-510（sudachitra-wordpiece，mC4日语）
变压器-UD-日语-电子-银座-510（sudachitra-wordpiece，mC4日语）
 * [cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - OpenCALM-7B模型描述 OpenCALM是一个仅解码器的语言模型套件，预先在日本数据集上进行训练和开发。
 * [staka/fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - FuguMT
河豚MT
 * [cl-tohoku/bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3) - BERT基础日语（使用unidic-lite进行整词掩码，CC-100和jawiki-20230102）
 * [rinna/japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16) - rinna / 日本衣物-Vit-B-16
 * [cl-tohoku/bert-base-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2) - BERT基础版日语（字符级标记化，全词掩码，jawiki-20200831）
 * [sonoisa/t5-base-japanese-title-generation](https://huggingface.co/sonoisa/t5-base-japanese-title-generation) - 从文章生成标题的模型 SEE:
 * [rinna/japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - japanese-roberta-base 这个仓库提供了一个基础大小的日语 RoBERTa 模型。
 * [elyza/ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - ELYZA-japanese-Llama-2-7b模型描述 ELYZA-japanese-Llama-2-7b是在Llama2的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [kit-nlp/bert-base-japanese-sentiment-irony](https://huggingface.co/kit-nlp/bert-base-japanese-sentiment-irony) - BERT基础版日语用于讽刺
 * [sociocom/MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - 这是一个用于识别日本医疗文件中命名实体的模型。
 * [jarvisx17/japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - japanese-sentiment-analysis 这个模型是从头开始在chABSA数据集上训练的。
 * [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 日本语T5事前学习完成模型 这是一个在日本语语料库上预训练的T5（文本到文本转换变压器）模型。
 * [sonoisa/sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 这是一个日语句子-LUKE模型。
 * [staka/fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - FuguMT
河豚MT
 * [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) - 日本SimCSE（BERT-base）日本语的README/日本语README摘要模型名称：pkshatech/simcse-ja-bert-base-clcmlp 这是一个日本SimCSE模型。
 * [Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 这个模型是通过对Luke-japanese-large-lite进行微调得到的。
 * [ku-nlp/deberta-v2-tiny-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm) - 日语字符级DeBERTa V2微型模型的模型卡描述
这是一个在日语维基百科、CC-100的日语部分和OSCAR的日语部分上预训练的日语DeBERTa V2微型模型。该模型使用字符级标记和整词掩码进行训练。
 * [rinna/japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) - japanese-gpt-neox-3.6b 概述 该存储库提供了一个拥有36亿参数的日语GPT-NeoX模型。
 * [elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - ELYZA-japanese-Llama-2-7b模型描述 ELYZA-japanese-Llama-2-7b是在Llama2的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [abeja/gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - gpt-neox-japanese-2.7b
 * [line-corporation/line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - LINE DistilBERT 日语 这是一个在131GB日语网络文本上预训练的DistilBERT模型。
 * [line-corporation/japanese-large-lm-3.6b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft) - 日语大型语言模型3.6B指令SFT
 * [rinna/japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - japanese-gpt-1b 这个仓库提供了一个拥有13亿参数的日语GPT模型。
 * [stabilityai/japanese-instructblip-alpha](https://huggingface.co/stabilityai/japanese-instructblip-alpha) - 日本InstructBLIP Alpha模型详细信息
日本InstructBLIP Alpha是一个视觉语言指令跟随模型，可以为输入图像生成日本描述，并可选择性地输入文本，如问题。
 * [cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - OpenCALM-3B模型描述 OpenCALM是一个仅解码器的语言模型套件，预先在日本数据集上进行训练和开发。
 * [cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large) - OpenCALM-Large模型描述
OpenCALM是一个仅解码器的语言模型套件，预训练于日本数据集，由开发。
 * [cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) - OpenCALM-1B模型描述 OpenCALM是一个仅解码器的语言模型套件，预先在日本数据集上进行训练和开发。
 * [cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - OpenCALM-Small模型描述
OpenCALM是一个仅解码器的语言模型套件，预训练于日本数据集，由开发。
 * [ku-nlp/deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 日本DeBERTa V2微型模型的模型卡描述
 * [stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b) - 这个仓库是公开可访问的，但您必须接受条件才能访问其文件和内容。
 * [cl-tohoku/bert-large-japanese-v2](https://huggingface.co/cl-tohoku/bert-large-japanese-v2) - BERT大型日语模型（使用unidic-lite进行整词掩码，CC-100和jawiki-20230102）
 * [elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - ELYZA-japanese-Llama-2-7b 模型描述 ELYZA-japanese-Llama-2-7b 是在 Llama2 的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - japanese-gpt-neox-3.6b-instruction-sft-v2 概述
 * [rinna/japanese-hubert-base](https://huggingface.co/rinna/japanese-hubert-base) - japanese-hubert-base 这是由rinna有限公司训练的日语HuBERT（双向编码器表示转换器中的隐藏单元）模型。
 * [cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - OpenCALM-Medium模型描述
OpenCALM是一个仅解码器的语言模型套件，预先在日本数据集上进行训练和开发。
 * [studio-ousia/luke-japanese-base-lite](https://huggingface.co/studio-ousia/luke-japanese-base-lite) - luke-japanese是LUKE（基于知识嵌入的语言理解）的日语版本，是一个预训练的知识增强上下文化词汇和实体表示。
 * [elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - ELYZA-japanese-Llama-2-7b模型描述 ELYZA-japanese-Llama-2-7b是在Llama2的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [cl-tohoku/bert-large-japanese](https://huggingface.co/cl-tohoku/bert-large-japanese) - BERT大型日语（使用unidic-lite进行整词掩码，jawiki-20200831）
 * [speechbrain/lang-id-voxlingua107-ecapa](https://huggingface.co/speechbrain/lang-id-voxlingua107-ecapa) - VoxLingua107 ECAPA-TDNN口语语言识别模型模型描述该模型是使用SpeechBrain在VoxLingua107数据集上训练的口语语言识别模型。
 * [rinna/japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - japanese-gpt2-small 这个仓库提供了一个小型的日语GPT-2模型。
 * [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) - bilingual-gpt-neox-4b-instruction-ppo 概述 该存储库提供了一个拥有38亿参数的英日双语GPT-NeoX模型。
 * [kit-nlp/bert-base-japanese-sentiment-cyberbullying](https://huggingface.co/kit-nlp/bert-base-japanese-sentiment-cyberbullying) - electra-base-cyberbullying 这是一个针对日语的BERT基础模型，用于自动检测网络欺凌。
 * [ku-nlp/roberta-base-japanese-char-wwm](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) - ku-nlp/roberta-base-japanese-char-wwm 模型描述 这是一个基于日语的 RoBERTa 基础模型，预训练于日语维基百科和 CC-100 的日语部分。该模型使用字符级别的分词和整词掩码进行训练。
 * [line-corporation/japanese-large-lm-1.7b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft) - japanese-large-lm-1.7b-instruction-sft
该存储库提供了由LINE公司进行微调和训练的1.7B参数的日语语言模型。
 * [rinna/bilingual-gpt-neox-4b-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k) - bilingual-gpt-neox-4b-8k 概述通知：此模型需要 transformers&gt;=4.31.0 版本才能正常工作。
 * [sonoisa/t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 日本语T5事前学习完成模型 这是一个在日本语语料库上预训练的T5（文本到文本转换变压器）模型。
 * [nlp-waseda/roberta-large-japanese-seq512](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512) - nlp-waseda/roberta-large-japanese-seq512 模型描述 这是一个在日本维基百科和CC-100的日本部分上预训练的日本RoBERTa大型模型，最大序列长度为512。
 * [studio-ousia/luke-japanese-large](https://huggingface.co/studio-ousia/luke-japanese-large) - luke-japanese-large是LUKE（基于知识增强的上下文化表示）的日语版本，它是一个预训练的知识增强的上下文化词汇和实体表示。
 * [cl-tohoku/bert-base-japanese-char-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v3) - BERT基础日语（字符级标记化，全词掩码，CC-100和jawiki-20230102）
 * [stockmark/gpt-neox-japanese-1.4b](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b) - stockmark/gpt-neox-japanese-1.4b 该存储库提供了一个基于GPT-NeoX的模型，该模型具有14亿个参数，在大约200亿个令牌的日语语料库上进行了预训练。
 * [llm-book/bert-base-japanese-v3-jnli](https://huggingface.co/llm-book/bert-base-japanese-v3-jnli) - bert-base-japanese-v3-jnli 是《大规模语言模型入门》第5章介绍的(自然语言推理)模型。
 * [abeja/gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - gpt2-large-japanese 该存储库提供了一个大型的日语GPT-2模型。
 * [rinna/japanese-stable-diffusion](https://huggingface.co/rinna/japanese-stable-diffusion) - 在获得这个模型之前还需要再走一步。
 * [nlp-waseda/roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - nlp-waseda/roberta-base-japanese 模型描述 这是一个在日本维基百科和CC-100的日文部分上预训练的日本RoBERTa基础模型。
 * [cl-tohoku/bert-base-japanese-char-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-char-whole-word-masking) - BERT基础版日语（字符分词，全词掩码启用）
 * [turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0) - Heron BLIP 日本稳定LM
 * [stanfordnlp/stanza-ja](https://huggingface.co/stanfordnlp/stanza-ja) - 日语（ja）的诗节模型
 * [llm-book/bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - bert-base-japanese-v3-jsts 「大规模语言模型入门」第5章介绍的（意义相似度计算）模型。
 * [Formzu/bert-base-japanese-jsnli](https://huggingface.co/Formzu/bert-base-japanese-jsnli) - bert-base-japanese-jsnli 这个模型是在JSNLI数据集上对cl-tohoku/bert-base-japanese-v2进行微调的版本。
bert-base-japanese-jsnli 这个模型是在JSNLI数据集上对cl-tohoku/bert-base-japanese-v2进行微调的版本。
 * [sonoisa/clip-vit-b-32-japanese-v1](https://huggingface.co/sonoisa/clip-vit-b-32-japanese-v1) - 日本语版CLIP模型
 * [llm-book/bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - bert-base-japanese-v3-marc_ja 是《大规模语言模型入门》第5章介绍的情感分析模型。
 * [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) - 这是AIBunCho/japanese-novel-gpt-j-6b AI BunCho使用的模型。
 * [nlp-waseda/roberta-large-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp) - nlp-waseda/roberta-large-japanese-with-auto-jumanpp 模型描述
 * [llm-book/bert-base-japanese-v3-unsup-simcse-jawiki](https://huggingface.co/llm-book/bert-base-japanese-v3-unsup-simcse-jawiki) - bert-base-japanese-v3-unsup-simcse-jawiki 这是在《大规模语言模型入门》第8章中介绍的无监督SimCSE模型。
 * [cl-tohoku/bert-large-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-large-japanese-char-v2) - BERT大型日语模型（字符级标记化，整词掩码，CC-100和jawiki-20230102）
 * [larryvrh/mt5-translation-ja_zh](https://huggingface.co/larryvrh/mt5-translation-ja_zh) - 这是google/mt5-large的微调版本，用于将日语翻译成简体中文。
 * [studio-ousia/luke-japanese-base](https://huggingface.co/studio-ousia/luke-japanese-base) - luke-japanese是LUKE（基于知识增强的上下文化表示）的日语版本，它是一个预训练的知识增强上下文化词汇和实体表示模型。
luke-japanese是LUKE（基于知识增强的上下文化表示）的日语版本，它是一个预训练的知识增强上下文化词汇和实体表示模型。
 * [ku-nlp/deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 日语字符级DeBERTa V2大型模型的模型卡描述
这是一个在日语维基百科、CC-100的日语部分和OSCAR的日语部分上预训练的日语DeBERTa V2大型模型。该模型使用字符级标记和整词掩码进行训练。
 * [nlp-waseda/roberta-base-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) - nlp-waseda/roberta-base-japanese-with-auto-jumanpp 模型描述
 * [ku-nlp/bart-large-japanese](https://huggingface.co/ku-nlp/bart-large-japanese) - 日本BART大型模型描述的模型卡
 * [llm-book/bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - llm-book/bert-base-japanese-v3-ner-wikipedia-dataset 这是在《大规模语言模型入门》第6章中介绍的命名实体识别模型。
 * [tsmatz/mt5_summarize_japanese](https://huggingface.co/tsmatz/mt5_summarize_japanese) - mt5_summarize_japanese（日语标题：日本语摘要模型）该模型是google/mt5-small的经过微调的版本，用于日语摘要。
 * [stockmark/bart-base-japanese-news](https://huggingface.co/stockmark/bart-base-japanese-news) - bart-base-japanese-news（基本大小模型）
 * [ybelkada/japanese-roberta-question-answering](https://huggingface.co/ybelkada/japanese-roberta-question-answering) - RoBERTa基础日语 - JaQuAD描述一个在JaQuAD上微调的日语问答模型。有关预训练模型的详细信息，请参阅RoBERTa基础日语。
 * [ku-accms/bert-base-japanese-ssuw](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) - ku-accms/bert-base-japanese-ssuw 模型描述 这是一个针对超短单元词（SSUW）的预训练日语BERT基础模型。
 * [alabnii/jmedroberta-base-sentencepiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece-vocab50000) - alabnii/jmedroberta-base-sentencepiece-vocab50000 模型描述 这是一个基于日本科学技术振兴机构（JST）收集的医学科学学术文章预训练的日语 RoBERTa 基础模型。该模型在 Creative Commons 4.0 国际许可证（CC BY-NC-SA 4.0）下发布。
 * [llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset) - llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset 这是在《大规模语言模型入门》第6章中介绍的命名实体识别模型。
 * [inu-ai/dolly-japanese-gpt-1b](https://huggingface.co/inu-ai/dolly-japanese-gpt-1b) - 更新历史 2023年5月7日，添加了“oasst1-89k-ja”数据集并支持对话系统。
 * [ptaszynski/yacis-electra-small-japanese-cyberbullying](https://huggingface.co/ptaszynski/yacis-electra-small-japanese-cyberbullying) - yacis-electra-small-cyberbullying
yacis-electra-small-网络欺凌
 * [nlp-waseda/comet-t5-base-japanese](https://huggingface.co/nlp-waseda/comet-t5-base-japanese) - COMET-T5和Finetuned T5在ATOMIC上使用文本到文本的语言建模目标。
COMET-T5和Finetuned T5在ATOMIC上使用文本到文本的语言建模目标。
 * [MuneK/bert-large-japanese-v2-finetuned-wrime](https://huggingface.co/MuneK/bert-large-japanese-v2-finetuned-wrime) - bert-large-japanese-v2-finetuned-wrime
bert-large-japanese-v2-finetuned-wrime
 * [ku-nlp/gpt2-medium-japanese-char](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char) - 日本角色级GPT-2中型模型的模型卡描述。这是一个日本角色级GPT-2中型（310M参数）的语言模型，它是在日本维基百科、CC-100的日本部分和OSCAR的日本部分上进行预训练的。
 * [turing-motors/heron-chat-git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0) - Heron GIT 日本稳定LM
 * [izumi-lab/bert-small-japanese-fin](https://huggingface.co/izumi-lab/bert-small-japanese-fin) - BERT小型日本金融 这是一个在日本语言文本上预训练的BERT模型。
 * [nlp-waseda/roberta-large-japanese](https://huggingface.co/nlp-waseda/roberta-large-japanese) - nlp-waseda/roberta-large-japanese 模型描述 这是一个在日本维基百科和CC-100的日文部分上预训练的日本RoBERTa大型模型。
 * [dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ](https://huggingface.co/dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ) - 模型ID为原始模型elyza/ELYZA-japanese-Llama-2-7b-fast-instruct的模型卡，该模型基于Meta的“Llama 2”，并在日语上进行了额外的预训练，以及原始的后训练和加速调优。

模型ID为原始模型elyza/ELYZA-japanese-Llama-2-7b-fast-instruct的模型卡，该模型基于Meta的“Llama 2”，并在日语上进行了额外的预训练，以及原始的后训练和加速调优。
 * [studio-ousia/luke-japanese-large-lite](https://huggingface.co/studio-ousia/luke-japanese-large-lite) - luke-japanese-large-lite是LUKE（基于知识增强的上下文化表示）的日语版本，是一个预训练的知识增强上下文化词汇和实体表示。
 * [alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000) - alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000 模型描述 这是一个基于日本科学技术振兴机构（JST）收集的医学科学学术文章预训练的日语 RoBERTa 基础模型。该模型在 Creative Commons 4.0 国际许可证（CC BY-NC-SA 4.0）下发布。
 * [Mizuiro-sakura/luke-japanese-base-finetuned-ner](https://huggingface.co/Mizuiro-sakura/luke-japanese-base-finetuned-ner) - 这个模型是通过对luke-japanese-base进行微调，使其可以用于命名实体识别（NER）。
 * [nlp-waseda/gpt2-small-japanese](https://huggingface.co/nlp-waseda/gpt2-small-japanese) - nlp-waseda/gpt2-small-japanese 这个模型是在日本维基百科和CC-100上预训练的日语GPT-2模型。
 * [hajime9652/xlnet-japanese](https://huggingface.co/hajime9652/xlnet-japanese) - XLNet日语模型描述。此模型需要Mecab和senetencepiece与XLNetTokenizer一起使用。
XLNet日语模型描述。此模型需要Mecab和senetencepiece与XLNetTokenizer一起使用。
 * [KoichiYasuoka/bert-base-japanese-upos](https://huggingface.co/KoichiYasuoka/bert-base-japanese-upos) - bert-base-japanese-upos模型描述
 * [sonoisa/t5-base-english-japanese](https://huggingface.co/sonoisa/t5-base-english-japanese) - 英语+日语T5事前学习完成的模型 这是一个在英语和日语平衡语料库上预训练的T5（文本到文本转换变压器）模型。
 * [ken11/albert-base-japanese-v1](https://huggingface.co/ken11/albert-base-japanese-v1) - albert-base-japanese-v1 是一个预先训练好的日语ALBERT模型。
 * [alabnii/jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - alabnii/jmedroberta-base-sentencepiece 模型描述 这是一个基于日本科学技术振兴机构（JST）收集的医学科学学术文章预训练的日语 RoBERTa 基础模型。该模型在 Creative Commons 4.0 国际许可证（CC BY-NC-SA 4.0）下发布。
 * [NTQAI/wav2vec2-large-japanese](https://huggingface.co/NTQAI/wav2vec2-large-japanese) - 使用Common Voice、JSUT、TEDxJP和其他一些数据，将Wav2Vec2-Large-Japanese Fine-tuned facebook/wav2vec2-large-xlsr-53模型在日语上进行微调。
 * [ku-nlp/deberta-v2-base-japanese-with-auto-jumanpp](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-with-auto-jumanpp) - 日本DeBERTa V2基础模型的模型卡描述。该模型是在日本维基百科、CC-100的日本部分和OSCAR的日本部分上进行预训练的。
 * [uzabase/luke-japanese-wordpiece-base](https://huggingface.co/uzabase/luke-japanese-wordpiece-base) - 这是对studio-ousia/luke-japanese-base进行的修改模型。
 * [izumi-lab/bert-base-japanese-fin-additional](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional) - 额外的预训练 BERT 基础日本金融 这是一个在日语文本上预训练的 BERT 模型。
 * [KoichiYasuoka/bert-base-japanese-wikipedia-ud-head](https://huggingface.co/KoichiYasuoka/bert-base-japanese-wikipedia-ud-head) - bert-base-japanese-wikipedia-ud-head模型描述
 * [TeamFnord/manga-ocr](https://huggingface.co/TeamFnord/manga-ocr) - 漫画OCR光学字符识别，主要关注日本漫画。
 * [clu-ling/whisper-large-v2-japanese-5k-steps](https://huggingface.co/clu-ling/whisper-large-v2-japanese-5k-steps) - whisper-large-v2-japanese-5k-steps 这个模型是在日本CommonVoice数据集（v11）上对openai/whisper-large-v2进行微调的版本。
 * [sonoisa/t5-base-japanese-article-generation](https://huggingface.co/sonoisa/t5-base-japanese-article-generation) - 通过标题生成文章内容的模型 SEE:
 * [minutillamolinara/bert-japanese_finetuned-sentiment-analysis](https://huggingface.co/minutillamolinara/bert-japanese_finetuned-sentiment-analysis) - bert-japanese_finetuned-sentiment-analysis 这个模型是从头开始在日本情感极性词典数据集上训练的。
 * [KoichiYasuoka/deberta-base-japanese-aozora-ud-head](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-aozora-ud-head) - deberta-base-japanese-aozora-ud-head模型描述
 * [reazon-research/reazonspeech-espnet-next](https://huggingface.co/reazon-research/reazonspeech-espnet-next) - reazonspeech-espnet-next是一个项目，旨在维护免费提供的日语音频数据集和机器学习模型。reazonspeech-espnet-next是一个“前沿”的存储库，包含由ReazonSpeech团队训练的最新ASR模型。
 * [alabnii/jmedroberta-base-manbyo-wordpiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece) - alabnii/jmedroberta-base-manbyo-wordpiece 模型描述 这是一个基于日本科学技术振兴机构（JST）收集的医学科学学术文章进行预训练的日语 RoBERTa 基础模型。该模型在 Creative Commons 4.0 国际许可证（CC BY-NC-SA 4.0）下发布。
 * [izumi-lab/bert-small-japanese](https://huggingface.co/izumi-lab/bert-small-japanese) - BERT小型日本金融 这是一个在日本语言文本上预训练的BERT模型。
 * [ku-nlp/bart-base-japanese](https://huggingface.co/ku-nlp/bart-base-japanese) - 日本BART基础模型的模型卡描述 这是一个在日本维基百科上预训练的日本BART基础模型。
 * [izumi-lab/electra-small-japanese-fin-discriminator](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator) - ELECTRA小型日本金融鉴别器 这是一个在日语文本上预训练的ELECTRA模型。
 * [ku-nlp/deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 日本DeBERTa V2大型模型的模型卡描述。这是一个在日本维基百科、CC-100的日本部分和OSCAR的日本部分上进行预训练的日本DeBERTa V2大型模型。
 * [oshizo/sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - sbert-jsnli-luke-japanese-base-lite 这是一个句子转换模型：它将句子和段落映射到一个768维的稠密向量空间，并可用于聚类或语义搜索等任务。
 * [rinna/japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 日本-gpt2-xsmall
 * [Tanrei/GPTSAN-japanese](https://huggingface.co/Tanrei/GPTSAN-japanese) - Tanrei/GPTSAN模型卡-基于日语的通用开关变压器的日语语言模型GPTSAN具有一些独特的特点。
 * [line-corporation/japanese-large-lm-1.7b](https://huggingface.co/line-corporation/japanese-large-lm-1.7b) - japanese-large-lm-1.7b 这个仓库提供了一个由LINE公司训练的1.7B参数的日语语言模型。
 * [jurabi/bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 使用BERT的BertForTokenClassification模型，从日语文本中提取专有名词。
 * [rinna/japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft) - japanese-gpt-neox-3.6b-instruction-sft 概述 该存储库提供了一个拥有36亿参数的日语GPT-NeoX模型。
 * [rinna/japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - japanese-gpt-neox-small 该存储库提供了一个小型的日语GPT-NeoX模型。
 * [line-corporation/japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) - 日语大型语言模型3.6b
 * [rinna/japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - japanese-gpt2-medium 这个仓库提供了一个中等大小的日语GPT-2模型。
 * [rinna/japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - rinna /日本夹子维生素B-16
 * [sonoisa/sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 这是一个日本句子BERT模型。
 * [cl-tohoku/bert-base-japanese-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-v2) - BERT基础版日语（使用unidic-lite和整词掩码，jawiki-20200831）
 * [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - japanese-gpt-neox-3.6b-instruction-ppo 概述 该存储库提供了一个拥有36亿参数的日语GPT-NeoX模型。
 * [stabilityai/japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) - 日本稳定LM基础Alpha-7B“能说日语、浮世绘、江户时代的鹦鹉” — 稳定扩散XL模型描述 japanese-stablelm-base-alpha-7b是一个7B参数的仅解码语言模型，它在多样化的日本和英语数据集上进行了预训练，重点是最大化日语语言建模性能和日语下游任务性能。


## Datasets

 * [mkshing/xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 这是经过过滤的日语子集XL-Sum，后跟PaLM 2filters15-gram overlap*代码：https://gist.github.com/mkshing/d6371cbfdd50d4f352cee247fd4dd86a示例数量训练：4215（之前：7113）验证：758（之前：889）测试：766（之前：889）
 * [turing-motors/LLaVA-Instruct-150K-JA](https://huggingface.co/datasets/turing-motors/LLaVA-Instruct-150K-JA) - 数据集详情 数据集类型：日语 LLaVA Instruct 150K 是原始 LLaVA Visual Instruct 150K 数据集的本地化版本。
 * [izumi-lab/llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - llm-japanese-dataset LLM构建用的日本语指令（聊天）数据集主要用于对使用英语构建的LLM模型等进行聊天（指令）回应任务的调优，可在LoRA等平台上使用。
 * [SkelterLabsInc/JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - JaQuAD数据集的数据卡片概述
JaQuAD数据集是一个人工标注的数据集，用于日语机器阅读理解，于2022年发布。
 * [datasets/snow_simplified_japanese_corpus](https://huggingface.co/datasets/snow_simplified_japanese_corpus) - SNOW T15和T23（简化日语语料库）的数据集卡片
 * [zan/lima-ja](https://huggingface.co/datasets/zan/lima-ja) - LIMA-JA数据集的数据卡描述
这是日本LIMA数据集，是由Meta的LIMA模型（周等人，2023年）训练而来的LIMA数据集的翻译。
 * [fujiki/japanese_alpaca_data](https://huggingface.co/datasets/fujiki/japanese_alpaca_data) - 用于“japanese_alpaca_data”的数据集卡片。该数据集基于masa3141在japanese-alpaca-lora上的出色工作。
 * [Atsushi/fungi_indexed_mycological_papers_japanese](https://huggingface.co/datasets/Atsushi/fungi_indexed_mycological_papers_japanese) - fungi_indexed_mycological_papers_japanese大菌轮「论文3行总结」数据集最终更新日期：2023/8/26（R3-10914为止）====语言日语此数据集仅提供日语版本。
 * [taishi-i/nagisa_stopwords](https://huggingface.co/datasets/taishi-i/nagisa_stopwords) - 日语停用词列表：nagisa
 * [hpprc/janli](https://huggingface.co/datasets/hpprc/janli) - JaNLI数据集概述的数据集卡
 * [izumi-lab/llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - llm-japanese-dataset-vanilla是用于构建LLM的日语聊天数据集izumi-lab/llm-japanese-dataset，已剔除了日英翻译的数据集等内容。
 * [sudy-super/dialogsum-ja](https://huggingface.co/datasets/sudy-super/dialogsum-ja) - dialogsum-ja这个数据集是dialogsum、CSDS等翻译成日语的对话摘要数据集。
 * [shunk031/jsnli](https://huggingface.co/datasets/shunk031/jsnli) - JSNLI数据集的数据卡片概述 日本語 SNLI(JSNLI) データセット - KUROHASHI-CHU-MURAWAKI LAB より：本データセットは自然言語推論 (NLI) の標準的ベンチマークである SNLI を日本語に翻訳したものです。
JSNLI数据集的数据卡片概述 日本語 SNLI(JSNLI) 数据集 - KUROHASHI-CHU-MURAWAKI实验室：该数据集是将自然语言推理（NLI）的标准基准SNLI翻译成日语的结果。
 * [fujiki/guanaco_ja](https://huggingface.co/datasets/fujiki/guanaco_ja) - 这是Guanaco数据集的一个日语部分。
 * [range3/wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - range3 / wiki40b-ja此数据集由wiki40b数据集中提取的仅包含日语数据的三个parquet文件组成。
 * [nakayama/hh-rlhf-helpful-base-ja](https://huggingface.co/datasets/nakayama/hh-rlhf-helpful-base-ja) - https://github.com/anthropics/hh-rlhf 的内容中，翻译了helpful-base文件夹中的英文内容，使用了fuguMT进行翻译，并排除了翻译不准确的部分，并进行了修正。
 * [larryvrh/WikiMatrix-v1-Ja_Zh-filtered](https://huggingface.co/datasets/larryvrh/WikiMatrix-v1-Ja_Zh-filtered) - 经过基本的正则表达式过滤和长度检查，删除异常对后，得到了WikiMatrix v1中日语/中文语言对数据的筛选和修改版本。
 * [if001/aozorabunko-clean-sin](https://huggingface.co/datasets/if001/aozorabunko-clean-sin) - 这是forkhttps://huggingface.co/datasets/globis-university/aozorabunko-cleanfilteredrow["meta"]["文字遣い種別"] == "新字新仮名"
 * [saldra/sakura_japanese_dataset](https://huggingface.co/datasets/saldra/sakura_japanese_dataset) - Sakura_dataset 商用可用的超小规模高品质日本语数据集。
 * [range3/cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - range3/cc100-ja 这个数据集包含了从cc100数据集中提取出来的只包含日语的parquet文件，并进行了分片处理。
 * [elyza/ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - ELYZA-tasks-100: 日本语instruction模型评估数据集 数据描述 本数据集是进行instruction调优的模型的评估用数据集。
 * [AhmedSSabir/Japanese-wiki-dump-sentence-dataset](https://huggingface.co/datasets/AhmedSSabir/Japanese-wiki-dump-sentence-dataset) - 数据集5M（5121625），包含清洁的日语完整句子及其上下文。
 * [fujiki/japanese_hh-rlhf-49k](https://huggingface.co/datasets/fujiki/japanese_hh-rlhf-49k) - 这是一个稍微不同版本的kunishou/hh-rlhf-49k-ja，没有ng_translation == 1的例子。
 * [Atsushi/fungi_diagnostic_chars_comparison_japanese](https://huggingface.co/datasets/Atsushi/fungi_diagnostic_chars_comparison_japanese) - fungi_diagnostic_chars_comparison_japanese大菌轮「识别形质总结」数据集最终更新日：2023/8/26（R3-10914まで）==== 语言日语 此数据集仅提供日语版本。
 * [datasets/covid_tweets_japanese](https://huggingface.co/datasets/covid_tweets_japanese) - COVID-19日本语推特数据集的数据卡片
 * [datasets/bsd_ja_en](https://huggingface.co/datasets/bsd_ja_en) - 商业场景对话的数据集卡
 * [reazon-research/reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - ReazonSpeech数据集的数据卡片概述ReazonSpeech是从日本电视节目中收集的大型音频语料库。
ReazonSpeech是从日本电视节目中收集的大型音频语料库。
