# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专用于 Python 库、预训练模型、词典和日语 NLP 语料库的精选资源列表

- [列出了670个GitHub仓库的信息 ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)
- [列出了1702个Hugging Face仓库的信息（模型和数据集） ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md) を掲載中
- [发布了一个工具，用于搜索大量仓库信息 🔎](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## The latest additions 🎉

**Hugging Face 🤗**
- We have added a feature to [the search tool🔍](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search) that allows you to search by **NLP research field**. You can now search through 1,750+ repositories!

- We have released a new dataset, **[awesome-japanese-nlp-multilabel-dataset](https://huggingface.co/datasets/taishi-i/awesome-japanese-nlp-multilabel-dataset)**. This is a dataset for Japanese natural language processing with multi-label annotations of [research field labels](https://huggingface.co/datasets/TimSchopf/nlp_taxonomy_data) for GitHub repositories in the NLP domain.

**Python**
 * [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) - 尝试使用Elasticsearch、GiNZA和患者表现词典来吸收患者表现的波动，进行意义结构搜索。

_Updated on Mar 04, 2025_

## Contents
 * [Hugging Face](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md)
   * [Models](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md#models)
   * [Datasets](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md#datasets)
 * [Python library](#python-library)
   * [Morphology analysis](#morphology-analysis)
   * [Parsing](#parsing)
   * [Converter](#converter)
   * [Preprocessor](#preprocessor)
   * [Sentence spliter](#sentence-spliter)
   * [Sentiment analysis](#sentiment-analysis)
   * [Machine translation](#machine-translation)
   * [Named entity recognition](#named-entity-recognition)
   * [OCR](#ocr)
   * [Tool for pretrained models](#tool-for-pretrained-models)
   * [Others](#others)
 * [C++](#c)
   * [Morphology analysis](#morphology-analysis-1)
   * [Parsing](#parsing-1)
   * [Others](#others-1)
 * [Rust crate](#rust-crate)
   * [Morphology analysis](#morphology-analysis-2)
   * [Converter](#converter-1)
   * [Search engine library](#search-engine-library)
   * [Others](#others-2)
 * [JavaScript](#javaScript)
   * [Morphology analysis](#morphology-analysis-3)
   * [Converter](#converter-2)
   * [Others](#others-3)
 * [Go](#go)
   * [Morphology analysis](#morphology-analysis-4)
   * [Others](#others-4)
 * [Java](#java)
   * [Morphology analysis](#morphology-analysis-5)
   * [Others](#others-5)
 * [Pretrained model](#pretrained-model)
   * [Word2Vec](#word2Vec)
   * [Transformer based models](#transformer-based-models)
 * [ChatGPT](#chatgpt)
 * [Dictionary and IME](#dictionary-and-ime)
 * [Corpus](#corpus)
   * [Part-of-speech tagging / Named entity recognition](#part-of-speech-tagging--named-entity-recognition)
   * [Text classification](#text-classification)
   * [Parallel corpus](#parallel-corpus)
   * [Dialog corpus](#dialog-corpus)
   * [Others](#others-3)
 * [Tutorial](#tutorial)
 * [Research summary](#research-summary)
 * [Reference](#reference)
 * [Contributors](#contributors)


## Python library

### Morphology analysis

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - SudachiPy 0.6及以上版本已经开发为Sudachi.rs。
 * [Janome](https://github.com/mocobeta/janome) - 用纯Python编写的日语形态分析引擎
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - mecab-python。mecab-python。您可以在此处找到原始版本：http://taku910.github.io/mecab/。
 * [mecab](https://github.com/ikegami-yukino/mecab) - 这个仓库用于构建Windows 64位MeCab二进制文件并改进MeCab Python绑定。
 * [fugashi](https://github.com/polm/fugashi) - 一个Cython MeCab包装器，用于快速、Pythonic的日语分词和形态分析。
 * [nagisa](https://github.com/taishi-i/nagisa) - 基于循环神经网络的日语分词器
 * [pyknp](https://github.com/ku-nlp/pyknp) - 一个用于JUMAN++/KNP的Python模块
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - KyTea的Python封装程序
 * [konoha](https://github.com/himkt/konoha) - Konoha：日语分词器的简单封装
 * [natto-py](https://github.com/buruzaemon/natto-py) - natto-py将Python编程语言与MeCab（日语的词性和形态分析器）结合起来。
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - 乐天 MA（Python 版本）
 * [python-vaporetto](https://github.com/daac-tools/python-vaporetto) - Vaporetto是一种快速且轻量级的基于点预测的分词器。这是Vaporetto的Python封装。
 * [dango](https://github.com/mkartawijaya/dango) - 一个易于使用的日语文本分词器，旨在为语言学习者和非语言学家提供帮助。
 * [rhoknp](https://github.com/ku-nlp/rhoknp) - 又一个Python绑定Juman++/KNP
 * [python-vibrato](https://github.com/daac-tools/python-vibrato) - 基于维特比算法的加速分词器（Python封装）
 * [jagger-python](https://github.com/lighttransport/jagger-python) - Python绑定Jagger（基于模式的日语形态分析器的C++实现）


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Parsing

 * [ginza](https://github.com/megagonlabs/ginza) - 一个基于通用依存关系的spaCy框架的日语NLP库。
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - 另一个日语依存结构分析器
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - 现代和当代日语的分词器、词性标注器、词形还原器和依存句法分析器
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - Camphr - 用于创建管道组件的NLP库
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - 使用BERT模型的现代和当代日语分词器、词性标注器、词形还原器和依存句法分析器。
 * [depccg](https://github.com/masashi-y/depccg) - 带有超级标签和依存因素模型的A* CCG解析器
 * [bertknp](https://github.com/ku-nlp/bertknp) - 基于BERT的日语依存句法分析器
 * [esupar](https://github.com/KoichiYasuoka/esupar) - 使用BERT/RoBERTa/DeBERTa模型的分词器POS-标注器和依存句法分析器，适用于日语和其他语言。
 * [yomikata](https://github.com/passaglia/yomikata) - 使用经过微调的BERT模型的异音词消歧库。
 * [jdepp-python](https://github.com/lighttransport/jdepp-python) - Python绑定J.DepP（日语依存解析器的C++实现）
 * [lightblue](https://github.com/daisukebekki/lightblue) - 一个用于日语的带有DTS表示的CCG解析器
 * [natsume-simple](https://github.com/borh-lab/natsume-simple) - natsume-simple是一个日语依存关系搜索系统


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Converter

 * [pykakasi](https://github.com/miurahr/pykakasi) - 将日语假名汉字句子转换为假名罗马字的轻量级转换器。
 * [cutlet](https://github.com/polm/cutlet) - Python中的日语转罗马字转换器
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - 将英文字母转换为片假名
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - 将阿拉伯数字或“西方”风格的数字转换为日本语境。
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Python的Mozc：假名汉字转换器
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - 日语文本解析器，将平假名/片假名字符串分离成音节（拼音）。
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - 将日语文本转换为音素序列的脚本
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - 一个快速的字符转换和音译库，基于日本国税局的法人番号系统定义的方案。
 * [wiredify](https://github.com/eggplants/wiredify) - 将日语假名从ba-bi-bu-be-bo转换为va-vi-vu-ve-vo
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - 使用MeCab获取日语读音（yomigana）和重音的简单Python包（CLI/Python API）。
 * [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) - 使用Python实现NormalizeNumexp，用于提取和规范化数量和时间表达式。
 * [Jusho](https://github.com/nagataaaas/Jusho) - 日本邮政编码数据的简易封装器
 * [yurenizer](https://github.com/sea-turt1e/yurenizer) - 日语文本规范化工具，解决拼写不一致问题。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Preprocessor

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - 针对mecab-neologd的日语文本规范化工具
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - 纯Python日语字符互转器，支持平假名、片假名、半角和全角。
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - 一个快速转换日语半角和全角字符的转换器
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 一款强大的日语网页文本清理工具
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 管理多个前处理的文本前处理工具
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho是一个Python模块，用于在日语中半角片假名和全角片假名之间进行双向转换的工具。
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - 另一个快速的日语字符串转换器
 * [kairyou](https://github.com/bikatr7/kairyou) - 使用SpaCy快速预处理日文文本，以便进行日文翻译或其他自然语言处理任务。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Sentence spliter

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日语文本句子边界消歧工具
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日语句子分割器
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 又一个用于日语文本的句子级分词器
 * [budoux](https://github.com/google/budoux) - 独立的。小巧的。语言中立的。BudouX是机器学习驱动的断行组织工具Budou的继承者。
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - Python的日语句子分割库
 * [hasami](https://github.com/mkartawijaya/hasami) - 一个用于对日语文本进行句子分割的工具
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - 用Rust编写的Python日语文本分段器
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日语句子分割工具比较


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Sentiment analysis

 * [oseti](https://github.com/ikegami-yukino/oseti) - 基于词典的日语情感分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 日语文档的负面和正面分类判断。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日语文本情感分析器
 * [asari](https://github.com/Hironsan/asari) - Python实现的日语情感分析器。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Machine translation

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawl预训练神经机器翻译（NMT）模型的示例用法。
 * [JASS](https://github.com/Mao-KU/JASS) - JASS：面向日本特定序列到序列预训练的神经机器翻译（LREC2020）和基于语言驱动的多任务预训练的低资源神经机器翻译（ACM TALLIP）。
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 一份针对日英机器翻译鲁棒性的现象级评估数据集。该数据集基于MTNT数据集，额外注释了四种语言现象：专有名词、缩写名词、口语表达和变体。COLING 2020。
 * [VISA](https://github.com/ku-nlp/VISA) - 一份用于视觉场景感知机器翻译的模糊字幕数据集


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Named entity recognition

 * [namaco](https://github.com/chakki-works/namaco) - 基于字符的命名实体识别。
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia是来自维基百科的扩展命名实体词典。
 * [noyaki](https://github.com/ken11/noyaki) - 将字符跨度标签信息转换为基于分词文本的标签信息。
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - 用于BERT模型微调的代码。这是一个用于创建和使用用于命名实体识别任务的模型的示例。
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 基于详细的注释标准的病例报告语料库，进行实体和关系抽取精度推理的代码。
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp，一个用于对日语文本进行地理标记的Python模块。
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - 使用BERT进行日语命名实体抽取的微调程序
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - 用于调整仅编码器和编码器-解码器变压器以适应日语的示例（Hugging Face）资源


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### OCR

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - 关于日文文本的光学字符识别，主要关注于日本漫画。
 * [mokuro](https://github.com/kha-white/mokuro) - 在浏览器中阅读日本漫画，可选择文本。
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - 使用Intel OpenVINO工具包，通过触摸面板绘制输入文本的手写日语OCR演示。
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - 日语OCR
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - NDLOCR应用程序
 * [donut](https://github.com/clovaai/donut) - OCR-free文档理解变压器（Donut）和合成文档生成器（SynthDoG）的官方实现，ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - 漫画翻译器 - 从网址获取日本漫画以翻译漫画图像
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - 用于识别现代日本杂志的OCR系统
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - NDLOCR文本识别模块
 * [Poricom](https://github.com/blueaxis/Poricom) - 漫画图像的光学字符识别。漫画OCR桌面应用程序。
 * [owocr](https://github.com/aurorawright/owocr) - 日文文本的光学字符识别
 * [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) - Yomitoku是一款由人工智能驱动的文件图像分析软件包，专门为日语设计。
 * [findtextcenternet](https://github.com/lithium0003/findtextcenternet) - 使用CenterNet的日语OCR


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Tool for pretrained models

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE：日本通用语言理解评估
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - 在spacy-transformers中使用自定义分词器
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - 使用T5生成对话
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - 调查各种DNN文本分类器，包括MLP、CNN、RNN、BERT方法。
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - 使用FastAPI和BERT部署情感分析服务器
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - 基于掩码语言模型的日语和越南语评分
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - Shiba的AllenNLP集成：日本CANINE模型
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - 用于评估预训练的日语word2vec模型在日语相似性数据集上的脚本
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - 基于BERT的日语GEC标记
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - 日语-BPE编码器
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - 日语-BPE编码器版本2
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - 日语语法错误校正工具
 * [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) - 日本稳定扩散是一种日本特有的潜在文本到图像扩散模型，能够根据任何文本输入生成逼真的照片。
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - 一个用于nagisa的BERT模型
 * [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) - 用于前缀调整GPT/GPT-NeoX模型的示例代码以及使用训练好的前缀进行推理的代码。
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - JGLUE的训练和评估脚本，是一个日语理解基准测试。
 * [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) - Transformers库的日语分词器
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP语言模型评估工具
 * [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) - 不同的分词器在连续书写语言的下游任务中表现如何？：以日语为例的案例研究 - ACL SRW 2023
 * [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) - 一个用于自回归语言模型少样本评估的框架。
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classification
llm-lora-分类
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP语言模型评估工具
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - 该存储库包含已修改的脚本和合并脚本，用于适应Alpaca-Lora适配器的LoRA调谐，假设使用转换为ggml的"gpt-neox"模型的"rinna/japanese-gpt-neox..."。
该存储库包含已修改的脚本和合并脚本，用于适应Alpaca-Lora适配器的LoRA调谐，假设使用转换为ggml的"gpt-neox"模型的"rinna/japanese-gpt-neox..."。
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - 这个存储库是为了评估日本语LLM角色扮演的性能而创建的。
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - 该存储库支持YuzuAI的Rakuda排行榜，该排行榜是日本LLMs的日本重点模拟版本，类似于LMSYS的Vicuna评估。
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - 这个工具可以跨多个数据集对日语大规模语言模型进行自动评估。
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - 该存储库包含了LLM-jp模型的监督微调代码。
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - 这是一个整理了在LLM勉强会（LLM-jp）中开发的与LLM的分词器相关的存储库。
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - 日语语言模型金融评估工具
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - 日本维库纳问答基准
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - 燕子项目 大规模语言模型 评估脚本


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Others

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - 一个将日本全名分成姓和名的工具。
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - 一个精选的资源列表，专门介绍用于日语自然语言处理的Python库。
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - Python版日本语意义角色标注系统（ASA）
 * [toiro](https://github.com/taishi-i/toiro) - 日本分词工具比较工具
 * [ja-timex](https://github.com/yagays/ja-timex) - 基于规则的解析器，用于提取/规范自然语言中的时间信息表达。
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - 从文本数据中选择特征的一组度量标准
 * [daaja](https://github.com/kajyuuen/daaja) - 这个仓库包含了针对日语自然语言处理的数据增强实现。
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - 这个仓库的目的是在概念验证（PoC）和研究开发（R＆D）的背景下制作原型作为案例研究，这些案例研究我已经在我的网站上写过。主要研究主题是与表示学习相关的自动编码器，基于能量模型的统计机器学习，对抗生成网络等。
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - 一个用于KyotoCorpus、KWDLC和AnnotatedFKCCorpus的处理器。
 * [nlplot](https://github.com/takapy0210/nlplot) - 自然语言处理可视化模块
 * [rake-ja](https://github.com/kanjirz50/rake-ja) - 用于日语的快速自动关键词提取算法
 * [jel](https://github.com/izuna385/jel) - 日本实体链接器。
 * [MedNER-J](https://github.com/sociocom/MedNER-J) - 最新版本的MedEX/J（日本疾病名称提取器）
 * [zunda-python](https://github.com/ikegami-yukino/zunda-python) - Zunda：Python的日语增强模态分析器客户端。
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/ 

https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
 * [showcase](https://github.com/cl-tohoku/showcase) - 一个PyTorch实现的日语谓词-论元结构（PAS）分析器，基于Matsubayashi＆Inui（2018）的论文，并进行了一些改进。
 * [darts-clone-python](https://github.com/rixwew/darts-clone-python) - 飞镖克隆 Python 绑定
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - 日本现实文本蕴含语料库的示例代码
 * [desuwa](https://github.com/megagonlabs/desuwa) - 基于KNP规则文件的特征注释器，可将单词和短语转换为形态素（纯Python实现）。
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - 通过日语对话的餐厅搜索系统。
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - 日语自然语言处理的样本代码
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - Python处理日语文本的小例子脚本
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - DNorm的日语版本
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - EventGraph是一个用于日语高级自然语言处理应用程序开发的平台。
 * [ishi](https://github.com/ku-nlp/ishi) - 石：日语意愿分类器
 * [python-npylm](https://github.com/musyoku/python-npylm) - 基于贝叶斯层次语言模型的无监督形态素分析。
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - 通过条件付概率场和贝叶斯层次语言模型的整合实现半监督形态分析。
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - 无教师词性标注推测
 * [negima](https://github.com/cocodrips/negima) - Negima是一个Python包，可以通过使用您定义的基于词性的规则来提取日语文本中的短语。
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - 使用BertSum作为摘要模型的提取式摘要器
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - 一个自然语言中的日语数字（汉字、阿拉伯数字）解析器。
 * [kantan](https://github.com/itayperl/kantan) - 按部首查找日语单词
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - 获取日语对话语料库
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - 日本文章摘要器。
 * [chirptext](https://github.com/letuananh/chirptext) - ChirpText是Python的文本处理工具集合。
 * [yubin](https://github.com/alvations/yubin) - 日本地址Munger
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - 日语维基百科清理工具
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - 一个将日语转换为音素的Python库。
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - 这个代码库包含与“基于情感的文本分类的日语分词器的实验评估”相关的代码。
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - 关于
This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - 从青空文库生成纯文本或标记化文本文件。
 * [JLM](https://github.com/jiali-ms/JLM) - 一个快速的LSTM语言模型，适用于日语和中文等大词汇语言。
 * [NTM](https://github.com/m3yrin/NTM) - 日本文章的神经主题建模测试
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - 这是一个英日机器学习和深度学习术语词典。
 * [text-generation](https://github.com/discus0434/text-generation) - 易于使用的脚本，可通过您自己的文本对GPT-2-JA进行微调，生成句子并自动发布推文。
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - 神经图像描述（NIC）在Chainer上的预训练模型，其英语和日语图像描述数据集的预训练模型。
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - “UnihanLM: 基于Unihan数据库的中日语言模型预训练的官方代码库”，AACL-IJCNLP 2020
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - 用于微调mBART模型的代码。
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - 在jtubespeech上的xvector模型
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - 用于创建TinySegmenter学习模型的工具。
 * [Grongish](https://github.com/shogo82148/Grongish) - 日语和格龙基语的相互转换脚本
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - 使用WordCloud生成的日语文章，无需使用Mecab（形态素解析引擎），即可实现形态素解析式的显示脚本。
 * [snark](https://github.com/hiraokusky/snark) - 使用日语WordNet的DB访问库
 * [toEmoji](https://github.com/mkan0141/toEmoji) - 将日语文本转换为仅包含表情符号的文本的工具
 * [termextract](https://github.com/kanjirz50/termextract) - - 专业术语抽取算法的实现练习
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - 对于Japanese-Dialog-Transformer的响应候选，使用KenLM的N-gram语言模型进行评分，进行过滤或重新排序。
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - Python中的混合Unigram模型和无限混合Unigram模型。
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - Python中的隐马尔可夫模型（HMM）和无限隐马尔可夫模型（iHMM）。
 * [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) - Python中的Ngram语言模型。
 * [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) - 使用PyTorch中的deepspeech2模型和Zakuro AI的支持进行自动语音识别。
 * [neural_ime](https://github.com/yohokuno/neural_ime) - 神经输入法引擎：神经输入法引擎
 * [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) - 神经网络能正确地将罗马字转写成日语吗？
 * [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) - 为日语指定的分词器
 * [AugLy-jp](https://github.com/chck/AugLy-jp) - AugLy上的日语文本数据增强
 * [furigana4epub](https://github.com/Mumumu4/furigana4epub) - 一个使用Mecab和Unidic为日语epub书籍添加振仮名的Python脚本。
 * [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) - 日语动词/形容词变形工具
 * [jageocoder](https://github.com/t-sagara/jageocoder) - 纯Python日本地址地理编码器
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp，一个用于对日语文本进行地理标记的Python模块。
 * [nksnd](https://github.com/yoriyuki/nksnd) - 新的假名汉字转换引擎
 * [JaMIE](https://github.com/racerandom/JaMIE) - 一个日本医疗信息提取工具包
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - 这是有关fasttext和word2vec的比较，以及执行脚本和学习脚本。
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - 最小的搜索引擎/PageRank/tf-idf
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - 通过网络爬虫获取5ch的历史记录，跟踪调查过去流行的词语（例如，香具师，orz）等。
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - 用于Twitter日语评价分析数据集的推文下载器
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - 基于Juman++和ConceptNet5.5聚合日语单词。
 * [jinf](https://github.com/hkiyomaru/jinf) - 一个日语变形转换器
 * [kwja](https://github.com/ku-nlp/kwja) - 一个用于日语的统一语言分析器
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - 基于掩码语言模型评分的复制包（ACL2020）。
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - [PyTorch] 日语ClipCap
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - [PyTorch] 展示、关注和讲述日语
 * [cihai](https://github.com/cihai/cihai) - Python CJK（中文、日文、韩文）语言字典库
 * [marine](https://github.com/6gsn/marine) - MARINE：基于多任务学习的日语口音估计
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - 微调Whisper ASR模型
 * [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) - 使用BERT和Transformer解码器的日语聊天机器人的PyTorch实现
 * [radicalchar](https://github.com/yamamaya/radicalchar) - 部首文字规范化库
 * [akaza](https://github.com/tokuhirom/akaza) - 又一个适用于IBus/Linux的日语输入法
 * [posuto](https://github.com/polm/posuto) - 日本邮政编码数据。
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - Tacotron2的日语实现
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - IBus平假名输入法
 * [furiganapad](https://github.com/esrille/furiganapad) - 假名垫
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - 日语同义词库
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - Mecab + NEologd + Docker + Python3 的输出
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - 日语嵌入评估
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPT将成为YouTuber。
 * [shuwa](https://github.com/google/shuwa) - 扩展GNOME屏幕键盘以支持输入法
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - 这个代码库提供了日语NLI模型的代码，这是一个经过微调的掩码语言模型。
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - 使用FuguMT进行日英翻译和英日翻译的工具
 * [fugumt](https://github.com/s-taka/fugumt) - 这是一个使用在Plofile Hub Connect上公开的机器翻译引擎的翻译环境。可以翻译输入到表格中的字符串和PDF文件。
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - JaSPICE：使用谓词-论元结构自动评估图像字幕模型的评估指标
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - 日本本地化
 * [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) - Python封装OpenJTalk
 * [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) - 通过在电子书中为每个汉字添加读音，使学习日语更容易。
 * [N46Whisper](https://github.com/Ayanaminn/N46Whisper) - 基于耳语的日文字幕生成器
 * [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) - Rinna-3.6B、OpenCALM等是用于日语支持的大规模语言模型（LLM）的简易Web界面。
 * [pdf-translator](https://github.com/discus0434/pdf-translator) - pdf-translator将英文PDF文件翻译成日语，保留原始布局。
 * [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) - 使用Haystack + Elasticsearch + wikipedia(ja)构建的日语问答系统示例
 * [mozc-devices](https://github.com/google/mozc-devices) - 自动从code.google.com/p/mozc-morse导出
 * [natsume](https://github.com/faruzan0820/natsume) - 一个日文文本前端处理工具包
 * [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) - 日本语TTS（VITS）的学习和音频合成的Gradio WebUI
 * [ja-law-parser](https://github.com/takuyaa/ja-law-parser) - 一个日本法律解析器
 * [dictation-kit](https://github.com/julius-speech/dictation-kit) - 使用Julius的日语口述套件
 * [julius4seg](https://github.com/Hiroshiba/julius4seg) - 使用Julius的分割支援工具
 * [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) - 免费使用的中等质量的文本朗读软件，VOICEVOX的语音合成引擎
 * [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) - LLaVA-JP是一种由LLaVA方法训练的日本VLM。
 * [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) - 用于日本低资源环境中的开源RAG和Llama指数的LLM
 * [bertjsc](https://github.com/er-ri/bertjsc) - 使用BERT（遮蔽语言模型）的日语拼写错误校正器。基于BERT的日语校正器。
 * [llm-leaderboard](https://github.com/wandb/llm-leaderboard) - 日本任务的llm评估项目
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - 关于JGLUE的培训和评估脚本，这是一个日语理解基准测试。
Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - 使用在日本数据集上预训练的模型来修改LAVIS的BLIP2 Q-former。
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - wikipedia 日本语的文本转换为各种日本语嵌入和faiss索引的脚本等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - 探索日本SimCSE
 * [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) - 基于Wikipedia日语文章的Gradio基础RAG示例，用于回答用户问题。
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - 使用GPT-4来自动评估语言模型的响应的脚本
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - 日语T5模型
 * [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) - 用于评估日本语LLM的存储库
 * [jmteb](https://github.com/sbintuitions/jmteb) - JMTEB（日本大规模文本嵌入基准测试）的评估脚本
 * [pydomino](https://github.com/dwangomediavillage/pydomino) - 这是一个用于对日语语音进行音素标签对齐的工具。
 * [easynovelassistant](https://github.com/zuntan03/easynovelassistant) - 轻量且无限制和审查的日语本地LLM“LightChatAssistant-TypeB”提供简易小说生成助手。通过本地特权的永久生成功能，堆积中奖抽奖。支持朗读功能。
 * [clip-japanese](https://github.com/sonoisa/clip-japanese) - 日语CLIP模型
 * [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) - Rime输入法的日语罗马字输入方案
 * [deep-question-generation](https://github.com/sonoisa/deep-question-generation) - 使用深度学习生成的自动化测验（日语T5模型）
 * [magpie-nemotron](https://github.com/aratako/magpie-nemotron) - 使用Magpie技术和Nemotron-4-340B-Instruct创建合成对话数据集的代码
 * [qlora_ja](https://github.com/sosuke115/qlora_ja) - 在日语数据集上进行qlora指令调整的学习示例代码
 * [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) - Mozc UT Jawiki词典是从日文维基百科为Mozc生成的词典。
 * [shisa-v2](https://github.com/shisa-ai/shisa-v2) - 日英双语法学硕士
 * [llm-translator](https://github.com/hpprc/llm-translator) - 基于Mixtral的Ja-En（En-Ja）翻译模型
 * [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) - 将Whisper的解码器替换为llm-jp-1.3b-v1.0版本的语音识别模型的学习代码
 * [rag-japanese](https://github.com/akimfromparis/rag-japanese) - 在资源匮乏的环境中，使用Llama指数为日本LLM开源的RAG
 * [monaka](https://github.com/komiya-lab/monaka) - 一个日语解析器（包括历史日语）
 * [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) - 基于最新的NMT研究，采用最先进的开源日语<-->英语机器翻译系统。
 * [substring-word-finder](https://github.com/toufu-24/substring-word-finder) - 进行连续子字符串的单词判断
 * [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) - 这个项目是一个基准工具，用于评估和比较各种视觉语言模型（VLMs）的性能。它使用两个数据集：LLaVA-Bench-In-the-Wild和日本HERON Bench来衡量模型的性能。
 * [text2dataset](https://github.com/llm-jp/text2dataset) - 使用开放的LLMs轻松将大型英文文本数据集转换为日文文本数据集。
 * [mecab-web-api](https://github.com/bungoume/mecab-web-api) - 使用MeCab的日语形态素解析WebAPI
 * [mecab_controller](https://github.com/ajatt-tools/mecab_controller) - 用于生成振り仮名读音的Mecab包装器。
 * [vits](https://github.com/zassou65535/vits) - VITS文本朗读器和声音变换器
 * [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) - 使用语音识别、文章生成和语音合成进行对话的聊天机器人应用程序
 * [kudasai](https://github.com/bikatr7/kudasai) - 利用先进的预处理和集成翻译技术简化日英翻译
 * [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) - 使用MeCab进行词素分析结果可视化的工具
 * [add-dictionary](https://github.com/massao000/add-dictionary) - 使用GUI添加OpenJTalk用户词典的应用程序
 * [j-moshi](https://github.com/nu-dialogue/j-moshi) - J-Moshi：一个日本全双工口语对话系统
 * [jatts](https://github.com/unilight/jatts) - JATTS: 日语TTS（用于研究）
 * [tsukasa-speech](https://github.com/respaired/tsukasa-speech) - 一个前沿的日语语音生成网络
 * [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) - 尝试使用Elasticsearch、GiNZA和患者表现词典来吸收患者表现的波动，进行意义结构搜索。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## C++

### Morphology analysis

 * [mecab](https://github.com/taku910/mecab) - 又一个日语形态分析器
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++（一个形态分析工具包）
 * [kytea](https://github.com/neubig/kytea) - 京都文本分析工具包，用于词语分割和发音估计等。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)
### Parsing

 * [cabocha](https://github.com/taku910/cabocha) - 另一个日语依存结构分析器
 * [knp](https://github.com/ku-nlp/knp) - 一个日语解析器


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)
### Others

 * [jsc](https://github.com/yohokuno/jsc) - 联合源通道模型用于日语假名汉字转换、汉语拼音输入和CJE混合输入。
 * [aquaskk](https://github.com/codefirst/aquaskk) - 没有形态分析的输入法。
 * [mozc](https://github.com/google/mozc) - Mozc - 一款为多平台设计的日语输入法编辑器
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch：一个（精确|前缀|近似）字符串匹配库
 * [resembla](https://github.com/tuem/resembla) - Resembla：基于单词的日语相似句子搜索库
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ 适用于Windows的类似SKK的日语输入法编辑器


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Rust crate

### Morphology analysis

 * [lindera](https://github.com/lindera-morphology/lindera) - 一个形态分析库。
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto：基于点预测的加速分词器
 * [goya](https://github.com/Leko/goya) - 用Rust编写的日语形态分析
 * [vibrato](https://github.com/daac-tools/vibrato) - 颤音：基于维特比加速的分词器
 * [yoin](https://github.com/agatan/yoin) - 一个用纯Rust编写的日语形态分析器
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 安全的Rust绑定，用于mecab词性和形态分析库。
 * [awabi](https://github.com/nakagami/awabi) - 一个使用mecab字典的形态分析器
 * [kanpyo](https://github.com/togatoga/kanpyo) - 用Rust编写的日语形态分析器


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Converter

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 用于检查和转换日语字符（平假名、片假名和罗马字）的实用程序库。
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 一个 Rust 库，用于将日语半角假名和全角英数字转换为普通字符。
 * [kana](https://github.com/gbrlsnchs/kana) - 【镜像】用于将罗马字文本转换为平假名或片假名的CLI程序。
 * [kanaria](https://github.com/samunohito/kanaria) - 这个库提供了平假名、片假名、半角和全角之间的相互转换和识别功能。
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - 这是一个将日本地址分割为都道府县/市区町村/町名/其他部分的库。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Search engine library

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Tantivy 的 Lindera 分词器。
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - 使用Vibrato的Tantivy分词器。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Others

 * [daachorse](https://github.com/daac-tools/daachorse) - 使用Rust中的紧凑双数组数据结构快速实现Aho-Corasick算法。
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - 高效地找到所有相似文档的配对
 * [crawdad](https://github.com/daac-tools/crawdad) - 使用字符级双数组字典树的自然语言词典 Rust 库。
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) - 各种分词器的比较代码
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - 这里提供基准工具来比较字符串匹配数据结构的性能。
 * [vime](https://github.com/algon-320/vime) - 使用Vim作为X11应用程序的输入法
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - VOICEVOX的核心是一款中等质量的免费文本朗读软件。
 * [akaza](https://github.com/akaza-im/akaza) - 又一个适用于IBus/Linux的日语输入法
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - 一个免费的在线、自托管、多语言的日语词典。
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - 谷歌日语输入用DvorakJP罗马字表 / DvorakJP罗马字表适用于谷歌日语输入
 * [niinii](https://github.com/Netdex/niinii) - 使用Ichiran辅助阅读文本的日语注释器
 * [cskk](https://github.com/naokiri/cskk) - SKK（简单假名汉字转换）库
 * [japanki](https://github.com/tysonwu/japanki) - 通过在CLI上做测验来学习日语词汇🇯🇵！
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - 用于文本转语音应用程序的日语文本预处理器（OpenJTalk在Rust语言中的重写）
用于文本转语音应用程序的日语文本预处理器（用Rust语言重写的OpenJTalk）
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - 使用软件从法院网站(https://www.courts.go.jp/index.html) 爬取裁判例数据并生成数据列表。
 * [jisho](https://github.com/eagleflo/jisho) - Jisho是一个提供日语-英语词典的CLI工具和Rust库。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## JavaScript

### Morphology analysis

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日语形态分析器的JavaScript实现
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - Rakuten MA - 用纯JavaScript编写的中文和日文形态分析器（词分割器+词性标注器）。
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - 又一个用于nodejs的mecab包装器
 * [juman-bin](https://github.com/thammin/juman-bin) - 一个用户可扩展的日语形态学分析器。日本语形态学分析系统。
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - 使用MeCab的异步日语形态分析器。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Converter

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - 日语语言库，可将日语句子转换为平假名、片假名或罗马字，并支持振假名和送假名模式。
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - Kuroshiro 的 Kuromoji 形态分析器。
 * [hepburn](https://github.com/lovell/hepburn) - 使用Hepburn罗马化将日语平假名和片假名转换为罗马字的Node.js模块。
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - 将日语数字转换为阿拉伯数字
 * [jslingua](https://github.com/kariminf/jslingua) - 处理文本的Javascript库：阿拉伯语、日语等。
 * [WanaKana](https://github.com/WaniKani/WanaKana) - 用于检测和转换平假名<-->片假名<-->罗马字的Javascript库
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - 规范和修复基于罗马字的日本姓名中常见的问题。
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - 用于使日文文本老式化的实用集合
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - 开源地址规范化库。
 * [jaconv](https://github.com/kazuhikoarase/jaconv) - 日本语文字转换库（javascript）
 * [romaji-conv](https://github.com/koozaki/romaji-conv) - 将罗马字转换为平假名
 * [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) - 全国住址数据API
 * [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) - 将文本单词转换为表情符号


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Others

 * [bangumi-data](https://github.com/bangumi-data/bangumi-data) - 日本动漫的原始数据
 * [yomichan](https://github.com/FooSoft/yomichan) - Chrome和Firefox的日语弹出式词典扩展。
 * [proofreading-tool](https://github.com/gecko655/proofreading-tool) - GUI工具，用于文本校对。
 * [kanjigrid](https://github.com/minosvasilias/kanjigrid) - 一个网页应用程序，展示了《记忆汉字》第六版中教授的2200个汉字。
 * [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) - 单一代码库用于汉字、假名、日语数据库等其他内容。
 * [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) - 解析敬体（ですます语气）和常体（である语气）的JavaScript库。
 * [hatsuon](https://github.com/DJTB/hatsuon) - 日语声调工具
 * [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) - 使用JavaScript进行日语情感分析，使用sentiment_ja。
 * [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) - mecab-ipadic 种子词典阅读器
 * [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) - 每天一个不同的日语单词。
 * [oskim](https://github.com/esrille/oskim) - 扩展GNOME屏幕键盘以支持输入法
 * [tweetMapping](https://github.com/wtnv-lab/tweetMapping) - 这是一个带有地理标签的推文数字档案，记录了发生在东日本大地震后24小时内发布的推文。
 * [pitch-accent](https://github.com/shirakaba/pitch-accent) - 预测日语的声调重音
 * [kana2ipa](https://github.com/amanoese/kana2ipa) - 将「ひらがな」或「カタカナ」转换为日语发音时的音标(IPA)的命令。
 * [voicevox](https://github.com/VOICEVOX/voicevox) - 免费使用的中等质量的文本朗读软件，VOICEVOX的编辑器
 * [kamiya-codec](https://github.com/fasiha/kamiya-codec) - 基于神谷多恵子的《日本动词手册》和《日本形容词和副词手册》，开发一个日语动词变位器和去变位器。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Go

### Morphology analysis

 * [kagome](https://github.com/ikawaha/kagome) - 用纯Go编写的自包含日语形态分析器


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Others

 * [ojosama](https://github.com/jiro4989/ojosama) - 将文本转换为百万天原萨洛梅小姐风格的口吻。
 * [nihongo](https://github.com/gojp/nihongo) - 日语词典
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - Yomichan的外部词典导入器。
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - 《偶像大师》日语输入法词典（由imas-db.jp提供）
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - 汉字转换为平假名/片假名/罗马字母，在围棋游戏中
 * [go-moji](https://github.com/ktnyt/go-moji) - 一个用于全角/半角转换的Go库
 * [ojichat](https://github.com/greymd/ojichat) - 生成一个似乎是叔叔通过LINE或邮件发送的句子。
 * [name](https://github.com/kuniwak/name) - 日语姓名搜索器


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Java

### Morphology analysis

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji是一个自包含且非常易于使用的日语形态分析器，专为搜索而设计。
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - 一个Sudachi词汇表
 * [meval](https://github.com/teru-oka-1933/meval) - 形态素解析器性能评估系统 MevAL


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Others

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 用于从图像中识别日语字符的Java库
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 将日语汉字转换为罗马字（拉丁字母）的Java库和命令行工具。
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Java中的汉字音译为平假名/片假名/罗马字。
 * [Kamite](https://github.com/fauu/Kamite) - 一款桌面语言沉浸式伴侣，适用于学习日语的学习者。
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - React Native异步日语分词原生插件，适用于iOS和Android。
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本分析器使用ElasticSearch的kuromoji日本分词器。
 * [moji4j](https://github.com/andree-surya/moji4j) - 一个Java库，用于在日语平假名、片假名和罗马字之间进行转换。
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - 针对mecab-neologd的日语文本规范化工具
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - 日本的elasticsearch分析插件


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Pretrained model

### Word2Vec

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - 使用Gensim和Mecab的Word2vec（单词到向量）方法来处理日语。
 * [chiVe](https://github.com/WorksApplications/chiVe) - 使用Sudachi和NWJC的日语词嵌入
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - 艾尔莫-日语
 * [embedrank](https://github.com/yagays/embedrank) - EmbedRank的Python实现
 * [aovec](https://github.com/eggplants/aovec) - 易用的青空文库Word2Vec构建器 - 包含所有书籍的Word2Vec构建器和预先构建的模型。
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - 这是AI LAB文章“係り受けに基づく日本語単語埋込（基于依存关系的日语词嵌入）”的存储库（文章网址https://ai-lab.lapras.com/nlp/japanese-word-embedding/）。
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - 又一个日语维基百科实体向量
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 使用最新的日本语Wikipedia转储数据，使用MeCab在IPA词典和最新的Neologd词典中进行形态分析，并基于其结果学习word2vec、fastText和GloVe的词向量表示的脚本。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Transformer based models

 * [bert-japanese](https://github.com/cl-tohoku/bert-japanese) - 用于日语文本的BERT模型。
 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - rinna有限公司提供的生成日语预训练模型的代码。
 * [bert-japanese](https://github.com/yoheikikuta/bert-japanese) - 使用SentencePiece的BERT模型用于日语文本。
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - 用于变形金刚的日语分词器
 * [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) - NTT有提供用于评估日语预训练模型的代码。
 * [shiba](https://github.com/octanove/shiba) - CANINE是一种高效的字符级转换器，提供了Pytorch实现和预训练的日语模型。
 * [Dialog](https://github.com/reppy4620/Dialog) - 使用BERT和Transformer解码器的日语聊天机器人的PyTorch实现
 * [language-pretraining](https://github.com/retarfi/language-pretraining) - PyTorch实现的BERT和ELECTRA模型，适用于日语文本。
 * [medbertjp](https://github.com/ou-medinfo/medbertjp) - 在日本医疗领域中，对预训练BERT模型进行试验。
 * [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) - ILYS-傲霸聊天机器人
 * [t5-japanese](https://github.com/megagonlabs/t5-japanese) - 用于预训练日语T5模型的代码
 * [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) - 使用Pytorch利用BERT的日语预训练模型。
 * [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) - 劳动BERT日语：使用Web语料库预训练的日语BERT
 * [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) - 日语BERT预训练模型
 * [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) - 用于日语的aMLP Transformer模型
 * [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) - 使用UniDic和SudachiPy进行预分词的日语BERT，训练数据来自青空文库和维基百科。
 * [sbert-ja](https://github.com/colorfulscoop/sbert-ja) - 用于 Hugging Face 模型中心训练 Sentence BERT 日语模型的代码
 * [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) - “日本推文情感分析与疫苗接种比较”的官方微调代码。
 * [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) - 日本GPT2生成模型
 * [text2text-japanese](https://github.com/tanreinama/text2text-japanese) - 基于GPT-2的文本转换模型
 * [gpt-ja](https://github.com/colorfulscoop/gpt-ja) - HuggingFace的转换器GPT-2日语模型
 * [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) - 使用友好的日语语料库训练的MT模型，尝试使用拉丁/英语衍生的片假名词汇表，而不是标准的汉日词汇表，使日语更易于/更容易接近西方人。
 * [albert-japanese](https://github.com/alinear-corp/albert-japanese) - 使用SentencePiece的BERT模型用于日语文本。
 * [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) - 用于在日语Wikipedia语料库上生成BERT预训练模型的存储库。
 * [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) - 一个在维基百科上训练的日本DistilBERT预训练模型。
 * [bert](https://github.com/informatix-inc/bert) - 该存储库提供了使用RoBERTa在日语语料库上预训练的代码片段。我们的数据集包括日语维基百科和网络滚动文章，总共25GB。发布的模型是基于HuggingFace的模型构建的。
 * [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) - 劳罗DistilBERT日语
 * [luke](https://github.com/studio-ousia/luke) - LUKE -- 基于知识嵌入的语言理解
 * [GPTSAN](https://github.com/tanreinama/GPTSAN) - 通用开关变压器基于日语模式
 * [japanese-clip](https://github.com/rinnakk/japanese-clip) - 日本CLIP由rinna有限公司制造。
 * [AcademicBART](https://github.com/EhimeNLP/AcademicBART) - 我们在学术数据库CiNii Articles的论文摘要上预训练了一个基于BART的日语掩码语言模型。
 * [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) - 我们在学术数据库CiNii Articles的论文摘要上预训练了一个基于RoBERTa的日语掩码语言模型。
 * [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) - DistilBERT模型在131GB的日语网络文本上进行了预训练。教师模型是LINE内部构建的BERT-base模型。
 * [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) - 使用翻译成日语的Stanford Alpaca数据集对LLaMA进行微调，创建了Low-Rank Adapter，并提供了链接和生成示例代码。
 * [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) - 提供预训练模型、代码和指南，以在日本维基百科资源上预训练官方ALBERT（https://github.com/google-research/albert）。
 * [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) - 日本的LLaMa实验
 * [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) - EasyLightChatAssistant是一个轻量级的、没有审查或限制的本地日语模型LightChatAssistant，在KoboldCpp中可以轻松尝试的环境。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## ChatGPT

 * [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) - 使用ChatGPT程序，可以在VRChat上进行聊天。
 * [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) - 我们正在开发AITuber的基础部分。
 * [wanna](https://github.com/hirokidaichi/wanna) - 带自然语言的Shell命令启动器
 * [ChatdollKit](https://github.com/uezo/ChatdollKit) - ChatdollKit 可以让你将你的3D模型制作成聊天机器人。
 * [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) - ChatGPT API的日语GUI
 * [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) - 这是搭载了ChatGPT3.5的伺かGhost“AI妹妹爱酱”。使用需要另外获取ChatGPT的API密钥。
 * [vrchatbot](https://github.com/Geson-anko/vrchatbot) - 用于创建VRChat AI机器人的代码库
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPT将成为YouTuber。
 * [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) - 一个使用Nuxt 3构建的聊天框应用程序，由Open AI文本完成端点提供支持。您可以选择不同的AI朋友个性。默认情况下，它会用日语回复。您可以使用此应用程序练习您的日语技能！
 * [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) - 这个Chrome扩展程序可以使用ChatGPT将选定的日语文本翻译成平假名。
 * [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) - 在这个样例中，我们使用检索增强生成模式，展示了几种方法来创建类似于ChatGPT的体验，以适用于您自己的数据。
 * [chatvrm](https://github.com/pixiv/chatvrm) - ChatVRM是一个可以在浏览器中轻松与3D角色交谈的演示应用程序。
 * [sftly-replace](https://github.com/kmizu/sftly-replace) - 一个Chrome扩展，可以轻松替换所选文本
 * [summarize_arxv](https://github.com/rkmt/summarize_arxv) - 用图表总结arXiv论文
 * [aiavatarkit](https://github.com/uezo/aiavatarkit) - 快速构建基于人工智能的对话化头像
 * [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) - 这个存储库是为了将在神户市政府试用ChatGPT的流程等转化为解决方案并公开而创建的。
 * [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) - 为了提供使用Azure OpenAI实现应用程序的参考，我们免费提供应用程序示例（参考架构、示例代码和部署步骤）。
 * [character_chat](https://github.com/mutaguchi/character_chat) - 这是一个使用OpenAI API的聊天脚本，可以与设定的角色用日语进行对话。
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - 用于在Slack上使用OpenAI的ChatGPT API的Slackbot脚本（假设使用日语）
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - 这是ChatGPT的提示示例。
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - 一个使用Python和Langchain构建的日语汉字闪卡应用，结合了GPT-4的智能功能。
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - 评估GPT-4和ChatGPT在日本医学执照考试中的表现
 * [japagen](https://github.com/retrieva/japagen) - 使用LLM在日语任务中生成伪学习数据的研究
  * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - ChatGPT和Copilot等各种生成AI用的“日本语”提示的示例
ChatGPT和Copilot等各种生成AI用的“日本语”提示的示例


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Dictionary and IME

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - 基于网络语言资源的新词典，适用于mecab-ipadic。
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - 一个日语口音词典生成器
 * [jamdict](https://github.com/neocl/jamdict) - Python 3 库，用于操作 Jim Breen 的 JMdict、KanjiDic2、JMnedict 和汉字-部首映射。
 * [unidic-py](https://github.com/polm/unidic-py) - 通过pip安装的Unidic包。
 * [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) - 日本公司词典（JCLdic）
 * [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) - Sudachi专用万病词典
 * [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) - 从维基百科（日文版）生成SKK/MeCab词典
 * [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) - 用于查找与文本相关的情感的字典
 * [JumanDIC](https://github.com/ku-nlp/JumanDIC) - 这个仓库包含源字典文件，用于构建 JUMAN 和 Juman++ 的字典。
 * [ipadic-py](https://github.com/polm/ipadic-py) - IPAdic打包为Python易用的形式。
 * [unidic-lite](https://github.com/polm/unidic-lite) - 一个小版本的UniDic，方便进行pip安装。
 * [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) - 用于在日语中输入表情符号的 IME 附加词典，如 Google 日语输入法等，可将日语转换为表情符号的 IME 扩展词典。
 * [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) - 用于日英转换和英语缩写展开的 IME 附加词典 orange_book，可在 Google 日本语输入或 ATOK 等中实现从日语到英语的和英转换和英语缩写展开的 IME 扩展词典。
 * [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) - NicoNico大百科和Pixiv百科全书共同部分的IME词典。
 * [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) - 这是GoogleIME用的日语片假名词典项目的存档，从片假名词（即日语外来词）翻译成英语。
 * [emoticon](https://github.com/tiwanari/emoticon) - Google日本语输入的表情符号字典∩(,,Ò‿Ó,,)∩
 * [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) - 这是将开源mozc词典转换为MeCab词典格式的结果。
 * [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) - 电音IME：用于Microsoft IME等的“电音部”相关术语词典。
 * [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) - 这是一个“虹三”相关术语词典，旨在供Microsoft IME等使用。
 * [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) - 这是一个包含目前已知的所有宝可梦名称的术语词典，旨在供Microsoft IME等输入法使用。
 * [EJDict](https://github.com/kujirahand/EJDict) - 英日词典数据（公共领域）EJDict-hand
 * [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) - 通过使用贵样笔画，可以正规地使用日语。
 * [genshin-dict](https://github.com/kotofurumiya/genshin-dict) - 这是一个可在Windows/macOS上使用的原神词典。
 * [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) - JMdict和JMnedict的JSON格式
 * [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) - 将外部词汇转换为Mozc系统词典
 * [mh-dict-jp](https://github.com/utubo/mh-dict-jp) - 想要制作Monster Hunter的用户词典…
 * [jitenbot](https://github.com/stephenmk/jitenbot) - 将日语字典网站和应用程序中的数据转换为便携文件格式
 * [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) - 基于网络语言资源的mecab-unidic新词典
 * [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) - 这是关于Hololive（Hololive Production）的词典文件。您可以使用./dictionary文件夹中的文本文件将单词添加到输入法中。详细信息请参阅README.md。
 * [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) - Yomitan / Yomichan的JMdict，JMnedict，KANJIDIC。
 * [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) - Yomichan中单词的JLPT级别标签
 * [Jitendex](https://github.com/stephenmk/Jitendex) - 一个免费且开放许可的日英词典，可与多个词典客户端兼容。
 * [jiten](https://github.com/obfusk/jiten) - 基于jmdict/kanjidic的日本安卓/命令行/网络词典 — 日英词典、汉英字典、德英词典、荷英词典
 * [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) - Pixiv百科全书关于与那城的词典
 * [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) - 乌恩辞典（冲绳语辞典）
 * [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) - 与读谷村的日语和中文词典。
 * [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) - 将鼠标悬停在单词上自动读取的通用词典工具
 * [jisyo](https://github.com/skk-dict/jisyo) - 为SKK输入法的新词典格式
 * [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) - 将日语读音转换为 Emoji 的 SKK 字典 😂
 * [anthy](https://github.com/netsphere-labs/anthy) - Anthy是一个用于日语的假名-汉字转换引擎。它可以将罗马字转换为假名，然后将假名文本转换为混合假名和汉字。
 * [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) - AWS服务名称的适用于Google日语输入的词典
 * [cl-skkserv](https://github.com/tani/cl-skkserv) - 使用Common Lisp构建的SKK词典服务器及其扩展
 * [anthy](https://github.com/xorgy/anthy) - 安蒂维护
 * [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) - 安蒂Unicode - 另一个安蒂
 * [azooKey](https://github.com/ensan-hcl/azooKey) - azooKey：一款完全使用Swift开发的日本键盘iOS应用程序
 * [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) - 日语输入法azooKey适用于桌面电脑，支持macOS。
 * [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) - 由azooKey引擎驱动的fcitx5日语输入法
由azooKey引擎驱动的fcitx5日语输入法
 * [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) - Mozc UT地名词典是从日本邮政的邮政编码数据转换而来的词典，用于Mozc。
 * [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) - 用Swift编写的假名汉字转换模块
 * [libkkc](https://github.com/ueno/libkkc) - 日文假名汉字转换输入法库
 * [libskk](https://github.com/ueno/libskk) - 日本SKK输入法库
 * [kanayomi-dict](https://github.com/warihima/kanayomi-dict) - openjtalk形式的用户词典
 * [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) - 汉字数据库的词典相关数据
 * [wlsp-classical](https://github.com/yocjyet/wlsp-classical) - 古典日本语的分类词汇表数据
 * [kanji-dict](https://github.com/marmooo/kanji-dict) - 这是一个用于查找汉字的笔顺、发音、画数、部首、用例和成立的汉字词典。收录了Unicode 15.1版本中的所有98,682个汉字。
 * [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) - (๑ ᴖ ᴑ ᴖ ๑)みょんかおもじ（旧Kaomoji_proj）是一个为Microsoft公司的输入软件Microsoft IME创建表情符号字典的项目。
 * [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) - Kotlin 平假名汉字转换程序
 * [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) - 使用jisho.org的日英词典，具有音频功能，可以导出条目的csv文件，并预览词典网站。
 * [ichiran](https://github.com/tshatrov/ichiran) - 日语文本的语言工具
 * [mikan](https://github.com/mojyack/mikan) - 一个日本输入法。
 * [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) - 关于关西方言日语教学材料的快速参考。
 * [jisho-open](https://github.com/hlorenzi/jisho-open) - JMdict日语-英语词典项目的Web前端，支持学习列表！
JMdict日语-英语词典项目的Web前端，支持学习列表！
 * [macskk](https://github.com/mtgto/macskk) - 另一个 macOS SKK 输入法
 * [nandoku](https://github.com/marmooo/nandoku) - 这是一个按年级整理的难读汉字词典。


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Corpus

### Part-of-speech tagging / Named entity recognition

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - 使用维基百科进行日语专有名词提取的数据集
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 用于命名实体识别的日语IOB2标记语料库。
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本语 Twitter 语料库
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - 并行通用依存关系。
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - 谷歌UDT 2.0的日本数据。
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大学网页文档引导语料库
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 注释版富满开拓中心语料库


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Parallel corpus

 * [small_parallel_enja](https://github.com/odashi/small_parallel_enja) - 50k英日平行语料库，用于机器翻译基准测试。
 * [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) - 一个用于日中机器翻译的网络爬取语料库
 * [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) - Coursera语料库挖掘和多阶段微调，以提高讲座翻译质量。
 * [JESC](https://github.com/rpryzant/JESC) - 一个大型的英日平行语料库
 * [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) - AMI会议平行语料库
 * [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) - 这个目录包含一个巨大的日英字幕语料库。原始数据来自斯坦福大学的JESC项目。
 * [jesc_small](https://github.com/yusugomori/jesc_small) - 小型日英字幕语料库
 * [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) - 这是一个考虑禁用词和单词级别的日英对照语料库。
 * [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) - CJK计算机科学术语对照 / 中日韩电脑科学术语对照 / 日中韩计算机科学术语对照 / 韩中日计算机科学术语对照
 * [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) - 用于创建日英平行语料库和训练NMT模型的脚本
 * [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) - 谷歌 vs DeepL


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

### Dialog corpus

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本电影推荐对话数据集
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - 使用爬虫程序从2ch论坛抓取并创建的对话语料库
 * [BSD](https://github.com/tsuruoka-lab/BSD) - 商业场景对话语料库
 * [asdc](https://github.com/megagonlabs/asdc) - 住宿搜索对话语料库
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - 用于seq2seq等的日语对话数据
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - 这个仓库包含了日英双语聊天语料库BPersona-chat，该语料库已发表在AACL-IJCNLP 2022的Eval4NLP 2022研讨会上的论文《聊天翻译错误检测以协助跨语言交流》中。
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 日本日常对话语料库，或日本语日常対話コーパス，是一个高质量的多轮对话数据集，包含五个主题的日常对话：日常生活，学校，旅行，健康和娱乐。
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - LLM构建用的日语聊天数据集

To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)
### Others

 * [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) - 日本现实文本蕴含语料库（NLP 2020，LREC 2020）
 * [kanji-data](https://github.com/davidluzgouveia/kanji-data) - 一个带有更新的JLPT级别和WaniKani信息的JSON汉字数据集。
 * [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) - 日语词语相似度数据集
 * [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) - 一个用于日语文本简化的释义数据库
 * [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) - 查基的基于方面的情感分析数据集
 * [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) - JaQuAD：用于机器阅读理解的日语问答数据集（2022年，Skelter Labs）
 * [JaNLI](https://github.com/verypluming/JaNLI) - 日本对抗自然语言推理数据集
 * [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) - 基于证据的解释数据集（AACL-IJCNLP 2020）
 * [emoji-ja](https://github.com/yagays/emoji-ja) - UNICODE表情符号的日语读音/关键词/分类词典
 * [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) - 由维基百科创建的日语姓名对齐数据集
 * [ja.text8](https://github.com/Hironsan/ja.text8) - 用于词嵌入的日语文本8语料库。
 * [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) - 3行摘要数据集
 * [japanese](https://github.com/hingston/japanese) - 这个仓库包含了由利兹大学语料库确定的按频率排序的44,998个最常见的日语单词列表。
 * [kanji-frequency](https://github.com/scriptin/kanji-frequency) - 从各种来源收集的汉字使用频率数据
 * [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) - TEDxJP-10K ASR 评估数据集
 * [CoARiJ](https://github.com/chakki-works/CoARiJ) - 日本年度报告语料库
 * [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) - 收集了用日语编写的技术书籍的生语料库/工具
 * [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) - ITA语料库的分块词注释
 * [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) - 用于自然语言处理前处理维基百科文本的实用脚本
 * [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) - 收集日语中不适当的表达方式。可用于自然语言处理时的数据清理等。
 * [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) - 我们整理了参议院官方网站上的会派、议员、议案和质询意见书的数据。
 * [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) - 国会议案数据库：众议院
 * [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) - STAIR字幕：大规模日本图像字幕数据集
 * [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) - Winograd模式挑战的日语翻译
 * [speechBSD](https://github.com/ku-nlp/speechBSD) - 一个带有音频和说话人属性信息的BSD语料库扩展
 * [ita-corpus](https://github.com/mmorise/ita-corpus) - ITA语料库的文章列表
 * [rohan4600](https://github.com/mmorise/rohan4600) - 摩拉平衡型日语语料库
 * [anlp-jp-history](https://github.com/whym/anlp-jp-history) - 语言处理学会年度大会演讲的完整列表和机器可读版本等。
 * [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) - 敬语转换任务的评估数据集
 * [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) - 日语中的英语借词
 * [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) - 日语维基百科链接语料库
 * [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) - 这是日本首相一般政策演讲的语料库。
 * [wrime](https://github.com/ids-cv/wrime) - WRIME：主观和客观情感分析数据集
 * [jtubespeech](https://github.com/sarulab-speech/jtubespeech) - JTubeSpeech：从YouTube收集的日语语音语料库
 * [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) - 在日语维基百科中使用频繁的单词列表
 * [kokkosho_data](https://github.com/rindybell/kokkosho_data) - 车辆不具合信息数据集
 * [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) - 在数字化资料OCR文本化业务中创建的OCR学习用数据集
 * [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) - 从全国书志数据创建的假名数据集
 * [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) - JVS（日本通用语音）语料库的自制标签
 * [hirakanadic](https://github.com/po3rin/hirakanadic) - 允许Sudachi从任何复合词列表中将平假名标准化为片假名。
 * [animedb](https://github.com/anilogia/animedb) - 约100年的动画作品列表数据库
 * [security_words](https://github.com/SaitoLab/security_words) - 与网络安全相关的公共机构的日英对应
 * [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) - 日本国会议员的数据
 * [honkoku-data](https://github.com/yuta1984/honkoku-data) - 这是一个历史资料的市民参与型翻刻平台“大家一起翻刻”的文本数据存储处。在这里可以找到由日本历史文献众包翻译平台“大家一起翻刻”创建的转录文本。
 * [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) - 维基百科数据集（日语版）
 * [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) - 日英工程师词汇表
 * [JSICK](https://github.com/verypluming/JSICK) - 日语组合知识句子（JSICK）数据集/JSICK压力测试集
 * [phishurl-list](https://github.com/JPCERTCC/phishurl-list) - 来自JPCERT/CC的网络钓鱼URL数据集
 * [jcms](https://github.com/shigashiyama/jcms) - 一个日语多个专业领域语料库（JCMS）
 * [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) - www.aozora.gr.jp的纯文本档案
 * [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) - friendly_JA是一个平行的日语到日语语料库，旨在通过使用拉丁/英语衍生的片假名词汇表，而不是标准的汉日词汇表，使日语更容易理解。
 * [topokanji](https://github.com/scriptin/topokanji) - 拓扑排序的汉字列表，以实现有效学习。
 * [isbn4groups](https://github.com/uribo/isbn4groups) - 与ISBN-13标准下的日语出版物（978-4-XXXXXXXXX）相关的数据等。
 * [NMeCab](https://github.com/komutan/NMeCab) - NMeCab：关于.NET上的日语形态分析器
 * [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) - 由数字化资料创建的OCR文本数据的ngram频率统计信息数据集
 * [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) - 2023年1月更新的NDL Ngram Viewer源代码等套装
 * [data_set](https://github.com/japanese-law-analysis/data_set) - 法律·判例相关的数据集
 * [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) - WRIME用于huggingface数据集。
 * [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) - NDL古典籍OCR学习用数据集（大家一起翻刻加工数据）
 * [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) - GIS和考古模拟器。正在开发中，预计2023年发布。
 * [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) - LIWC2015的日语版本
 * [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) - 日本Livedoor新闻语料库，用于huggingface数据集。
 * [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) - JGLUE：适用于huggingface数据集的日语通用语言理解评估
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality是通过众包创建的数据集，反映了日本标注者的常识道德。
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - COMET-ATOMIC ja
COMET-ATOMIC ja
 * [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) - 对话常识图（日语）
 * [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) - 《日本毒性模式的提案和评估》提供了一个日语毒性模式和数据集。
 * [camera](https://github.com/CyberAgentAILab/camera) - CAMERA（CyberAgent多模态广告文本生成评估）是日本广告文本生成数据集。
 * [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) - 日语假新闻数据集
 * [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) - jpn可解释问答数据集
 * [copa-japanese](https://github.com/nlp-titech/copa-japanese) - COPA数据集（日语）
 * [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) - “语义原则词汇表（WLSP）”中的单词熟悉度率
 * [ProSub](https://github.com/matbahasa/ProSub) - 代词替代和称谓词的跨语言研究
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality是通过众包创建的数据集，反映了日本标注者的常识道德。
 * [ramendb](https://github.com/nuko-yokohama/ramendb) - 从某种数据库（https://supleks.jp/）进行的网络爬虫工具和收集的数据。
 * [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) - 针对huggingface数据集的CAMERA（CyberAgent多模态广告文本生成评估）
 * [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) - 事实核查句子NLI数据集
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - 这是一个将 databricks/dolly-v2-12b 的训练数据中使用的 databricks-dolly-15k.jsonl 翻译成日语的数据集。
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELD是基于MELD的情感感知语音翻译的英日数据集。
 * [meconaudio](https://github.com/elith-co-jp/meconaudio) - Mecon Audio（医疗会议音频）是厚生劳动省主办的先进医疗会议记录的朗读数据集。
 * [japanese-addresses](https://github.com/geolonia/japanese-addresses) - 全国镇街道级别（277,191条）的地址数据开放数据
 * [aozorasearch](https://github.com/myokoym/aozorasearch) - Groonga为青空文库提供的全文搜索系统。
 * [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) - 该存储库包含用于重现LLM-jp语料库的脚本。
 * [alpaca_ja](https://github.com/shi3z/alpaca_ja) - 这是将alpaca数据集翻译成日语的内容。
 * [instruction_ja](https://github.com/megagonlabs/instruction_ja) - 日语指示数据
 * [japanese-family-names](https://github.com/siikamiika/japanese-family-names) - 前5000个日本姓氏，附带读音，按频率排序。
 * [kanji-data-media](https://github.com/kanjialive/kanji-data-media) - 来自Kanji alive的关于汉字、部首、媒体文件、字体和相关资源的日语语言数据
 * [reazonspeech](https://github.com/reazon-research/reazonspeech) - 在家构建大规模的日语音频语料库
 * [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) - 青空文库和Sapie的点字数据创建的假名数据集
 * [koniwa](https://github.com/koniwa/koniwa) - 一个用日语语言注释的开放声音收集
 * [JMMLU](https://github.com/nlp-waseda/JMMLU) - 日本語大规模多任务语言理解基准测试
 * [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) - 青空文库振り仮名注释附带音频语料库数据集
 * [jqara](https://github.com/hotchpotch/jqara) - JQaRA：具有检索增强功能的日语问答系统 - 用于检索增强（RAG）评估的日语问答数据集
 * [jemhopqa](https://github.com/aiishii/jemhopqa) - JEMHopQA（日本可解释的多跳问题回答）是一个日本多跳QA数据集，可以评估内部推理。
 * [jacred](https://github.com/youmima/jacred) - 日文文档级关系抽取数据集存储库（计划于三月发布）。
 * [jades](https://github.com/naist-nlp/jades) - JADES是一个用于日语文本简化的数据集，详细描述在《JADES: 面向非母语者的日语新文本简化数据集》（论文即将发布）。
 * [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) - 2023年8月，墨尔本大学发布了安全性评估数据集“Do-Not-Answer”，现在已经将其自动翻译成日语，以便用于评估日语LLM，并根据日本文化进行了修正的数据集。
 * [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) - OpenAssistant的开源数据OASST1已被翻译成日语的数据集。
 * [jacwir](https://github.com/hotchpotch/jacwir) - JaCWIR：日本休闲网络信息检索  用于评估日语信息检索的小型休闲Web标题和摘要数据集
 * [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) - 适用于日语学习者的常用片假名和原始单词对照表在科学技术行业中。
 * [j-unimorph](https://github.com/cl-tohoku/j-unimorph) - 日语UniMorph数据集
 * [GazeVQA](https://github.com/riken-grp/GazeVQA) - LREC-COLING 2024 论文《一个注视引导的视觉问答数据集，用于澄清模糊的日语问题》的数据集
 * [J-CRe3](https://github.com/riken-grp/J-CRe3) - J-CRe3实验代码（上田等人，LREC-COLING，2024）
 * [jmed-llm](https://github.com/sociocom/jmed-llm) - JMED-LLM：用于大型语言模型的日本医学评估数据集
 * [lawtext](https://github.com/yamachig/lawtext) - 日本法律的纯文本格式
简体中文
 * [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) - OCR处理程序研究开发项目中创建的OCR学习数据集
 * [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) - 基于话题的语义模糊消除评估集合
 * [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) - Jamp: 用于评估语言模型泛化能力的受控日语时间推理数据集
 * [JSeM](https://github.com/DaisukeBekki/JSeM) - 日语语义测试套件（FraCaS对应和扩展）
 * [niilc-qa](https://github.com/mynlp/niilc-qa) - NIILC QA 数据
 * [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) - 日本论文链式思维提示验证数据集
 * [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) - 这是一个包含维基百科文章和各种语言注释的日语文本语料库。
 * [elaws-history](https://github.com/kissge/elaws-history) - 通过e-Gov法令搜索定期下载分发的“所有法令数据”，并进行归档。
 * [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) - Japanese-RP-Bench是用于衡量LLM的日语角色扮演能力的基准。
 * [hdic](https://github.com/shikeda/hdic) - HDIC：日本早期汉字词典集成数据库
 * [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) - 日本开放数据精选 - 日本开放数据信息汇总


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Tutorial

 * [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) - spaCy教程（英文和日文）。spacy-transformers、BERT、GiNZA。
 * [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) - 使用日语语料库训练fastText的教程
 * [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) - AllenNLP-NER-ja：使用AllenNLP进行针对日语的命名实体识别。
 * [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) - 使用 chariot 和 PyTorch 进行日语文本分类的实验
 * [ginza-examples](https://github.com/poyo46/ginza-examples) - 推荐日语NLP库GiNZA
 * [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) - 使用BERT进行文档分类-日语
 * [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) - 这是在Google Colaboratory上运行日语BERT的方法。
 * [bert-book](https://github.com/stockmarkteam/bert-book) - “BERT自然语言处理入门：使用Transformers的实践编程”支持页面
 * [janome-tutorial](https://github.com/mocobeta/janome-tutorial) - 这是一个使用Janome进行文本挖掘的入门教程。
 * [handson-language-models](https://github.com/hnishi/handson-language-models) - 这是关于日语语言模型的实践资料。
 * [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) - 在Google Colab上尝试日语文本推理。
 * [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) - 这是deep-learning-with-pytorch的日文版存储库。
 * [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) -【2023年版】BERTによるテキスト分類
 * [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) - 这是《自然语言处理：基于深度学习》（共立出版社）的支持页面。
 * [llm-book](https://github.com/ghmagazine/llm-book) - 「大规模语言模型入门」（技术评论社，2023）的GitHub仓库
 * [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) - NLP2024 教程3 制作和学习日语大规模语言模型 - 环境搭建步骤和源代码
 * [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) - 日本语信息检索教程
 * [nlpbook](https://github.com/mamorlis/nlpbook) - "自然语言处理教科书"支持网站
 * [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) - 制作并学习正则表达式引擎
 * [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) - 【2024年版】基于BERT的文本分类
 * [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) - 对Google Gemma进行日语指令的微调
 * [nlp100v2020](https://github.com/upura/nlp100v2020) - 用Python解决“自然语言处理100道题目2020”
 * [textmining-ja](https://github.com/paithiov909/textmining-ja) - 使用R进行自然语言处理和文本分析的练习


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Research summary

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 一个预训练的BERT模型列表，包括日语的单词/子词分词和词汇构建算法信息。
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 收集和分类有关日语文法错误修正的文献的存储库。
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - 文本语料库列表和更多（主要是日语）
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - 深度学习模型性能最大化的系统指南
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 尝试将日语音标，特别是声调资源整合成一个列表。
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - 开源的日语LLM总结


To check the statistics table (GitHub stars/Downloads), please refer to [this page](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.full.md).
 [🔝 Back to Top](#contents)

## Reference

 * [自然言語処理の餅屋](https://www.jnlp.org/nlp/top)
 * [yasuokaの日記： 日本語係り受け解析器「2020年の総ざらえ」](https://srad.jp/~yasuoka/journal/643631/)
 * [yasuokaの日記： 日本語係り受け解析器「2021年の総ざらえ」](https://srad.jp/~yasuoka/journal/651542/)
 * https://github.com/topics/japanese?l=python
 * https://github.com/topics/japanese-language?l=python
 * https://github.com/search?o=desc&q=corpus+japanese&s=&type=Repositories
 * https://paperswithcode.com/datasets?lang=japanese
 * https://github.com/himkt/awesome-bert-japanese
 * [Awesome-Rust-MachineLearning-日本語向けのrustクレートや記事等をまとめたもの](https://github.com/vaaaaanquish/Awesome-Rust-MachineLearning/blob/main/README.ja.md)
 * [大規模言語モデル入門Ⅱ 〜生成型LLMの実装と評価](https://gihyo.jp/book/2024/978-4-297-14393-0)


## Contributors

 * [kaisugi](https://github.com/kaisugi) - [website](https://kaisugi.me)
 * [bomin0624](https://github.com/bomin0624) - [twitter](https://twitter.com/bomin0624_c)
 * [passaglia](https://github.com/passaglia) - [twitter](https://twitter.com/SamPassaglia)
