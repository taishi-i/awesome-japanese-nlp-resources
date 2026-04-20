# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

专用于 Python 库、预训练模型、词典和日语 NLP 语料库的精选资源列表

- [列出了854个GitHub仓库的信息 ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)
- [列出了304个Hugging Face仓库的信息（模型和数据集） ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md) を掲載中
- 🎉 我们于2026年3月1日正式发布了日语NLP资源调查工具 [awesome-japanese-nlp-survey](https://awesome-japanese-nlp-survey.vercel.app/)！


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## 🎉 The latest additions

**Python**
 * [OneCompression](https://github.com/FujitsuResearch/OneCompression) - 富士通研究所推出的LLM后学习量子化（PTQ）管道。集成了QEP（NeurIPS 2025）、ILP混合精度、旋转前处理、vLLM插件。论文：[arXiv:2603.28845](https://arxiv.org/abs/2603.28845)。
 * [manga-translator](https://github.com/georgescutelnicu/manga-translator) - 将漫画图片中的对话框内的文本翻译成简体中文。

_Updated on Apr 21, 2026_

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
将日语文本分词并标注词性和原形的库

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
 * [Mecari](https://github.com/zbller/Mecari) - Mecari（基于图神经网络的日语形态分析）


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [SudachiPy](https://github.com/WorksApplications/SudachiPy) | 📥 392k | 📦 63M | ⭐ 430 | 🔴 october 2022|
| 🔗 [Janome](https://github.com/mocobeta/janome) | 📥 47k | 📦 12M | ⭐ 910 | 🟡 october 2025|
| 🔗 [mecab-python3](https://github.com/SamuraiT/mecab-python3) | 📥 202k | 📦 37M | ⭐ 581 | 🟡 november 2025|
| 🔗 [mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python) | 📥 35k | 📦 797k | ⭐ 272 | 🔴 october 2024|
| 🔗 [fugashi](https://github.com/polm/fugashi) | 📥 120k | 📦 14M | ⭐ 518 | 🟡 october 2025|
| 🔗 [nagisa](https://github.com/taishi-i/nagisa) | 📥 45k | 📦 8M | ⭐ 417 | 🟢 february|
| 🔗 [pyknp](https://github.com/ku-nlp/pyknp) | 📥 923 | 📦 3M | ⭐ 93 | 🟡 january|
| 🔗 [Mykytea-python](https://github.com/chezou/Mykytea-python) | 📥 2k | 📦 566k | ⭐ 36 | 🟢 march|
| 🔗 [konoha](https://github.com/himkt/konoha) | 📥 48k | 📦 6M | ⭐ 261 | 🟢 march|
| 🔗 [natto-py](https://github.com/buruzaemon/natto-py) | 📥 30k | 📦 34M | ⭐ 95 | 🔴 november 2023|
| 🔗 [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) | 📥 19 | 📦 27k | ⭐ 23 | 🔴 may 2017|
| 🔗 [python-vaporetto](https://github.com/daac-tools/python-vaporetto) | 📥 210 | 📦 176k | ⭐ 21 | 🟡 june 2025|
| 🔗 [dango](https://github.com/mkartawijaya/dango) | 📥 51 | 📦 26k | ⭐ 25 | 🔴 november 2021|
| 🔗 [rhoknp](https://github.com/ku-nlp/rhoknp) | 📥 11k | 📦 1M | ⭐ 39 | 🟢 march|
| 🔗 [python-vibrato](https://github.com/daac-tools/python-vibrato) | 📥 166 | 📦 118k | ⭐ 43 | 🔴 september 2024|
| 🔗 [jagger-python](https://github.com/lighttransport/jagger-python) | 📥 2k | 📦 305k | ⭐ 13 | 🔴 march 2024|
| 🔗 [Mecari](https://github.com/zbller/Mecari) | - | - | ⭐ 39 | 🟡 september 2025|


### Parsing
分析日语句法和依存结构的库

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
 * [jdeppy](https://github.com/matsurih/jdeppy) - Python封装器用于J.DepP，快速的日语依赖解析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ginza](https://github.com/megagonlabs/ginza) | 📥 14k | 📦 2M | ⭐ 844 | 🔴 march 2024|
| 🔗 [cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python) | 📥 87 | 📦 54k | ⭐ 7 | 🔴 august 2022|
| 🔗 [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) | 📥 260 | 📦 331k | ⭐ 38 | 🟡 december 2025|
| 🔗 [camphr](https://github.com/PKSHATechnology-Research/camphr) | 📥 253 | 📦 271k | ⭐ 336 | 🔴 august 2021|
| 🔗 [SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic) | 📥 177 | 📦 119k | ⭐ 21 | 🔴 repo not found|
| 🔗 [depccg](https://github.com/masashi-y/depccg) | 📥 94 | 📦 46k | ⭐ 98 | 🔴 august 2023|
| 🔗 [bertknp](https://github.com/ku-nlp/bertknp) | - | - | ⭐ 23 | 🔴 october 2021|
| 🔗 [esupar](https://github.com/KoichiYasuoka/esupar) | 📥 925 | 📦 173k | ⭐ 56 | 🟢 february|
| 🔗 [yomikata](https://github.com/passaglia/yomikata) | 📥 25 | 📦 50k | ⭐ 32 | 🔴 october 2023|
| 🔗 [jdepp-python](https://github.com/lighttransport/jdepp-python) | 📥 1k | 📦 289k | ⭐ 4 | 🔴 february 2024|
| 🔗 [lightblue](https://github.com/daisukebekki/lightblue) | - | - | ⭐ 28 | 🟢 march|
| 🔗 [natsume-simple](https://github.com/borh-lab/natsume-simple) | - | - | ⭐ 5 | 🔴 february 2025|
| 🔗 [jdeppy](https://github.com/matsurih/jdeppy) | 📥 22 | 📦 12k | ⭐ 3 | 🔴 february 2022|


### Converter
在假名、罗马字与全角半角之间转换的库

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
 * [e2k](https://github.com/Patchethium/e2k) - 一个用于自动将英语转换为片假名的工具
 * [alkana.py](https://github.com/zomysan/alkana.py) - 一个工具，用于获取字母字符串的片假名读音。
 * [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) - 将英语文本转换为片假名的程序
 * [kanjiconv](https://github.com/sea-turt1e/kanjiconv) - 汉字转换器到平假名、片假名、罗马字母。
 * [kanjize](https://github.com/nagataaaas/kanjize) - Kanjize(カンジャイズ): 汉字数字和整数之间的简易转换器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [pykakasi](https://github.com/miurahr/pykakasi) | 📥 258k | 📦 31M | ⭐ 445 | 🔴 july 2022|
| 🔗 [cutlet](https://github.com/polm/cutlet) | 📥 18k | 📦 2M | ⭐ 376 | 🟡 june 2025|
| 🔗 [alphabet2kana](https://github.com/shihono/alphabet2kana) | 📥 215 | 📦 59k | ⭐ 14 | 🟢 february|
| 🔗 [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) | - | - | ⭐ 50 | 🔴 november 2020|
| 🔗 [mozcpy](https://github.com/ikegami-yukino/mozcpy) | 📥 88 | 📦 13k | ⭐ 47 | 🔴 february 2025|
| 🔗 [jamorasep](https://github.com/tachi-hi/jamorasep) | 📥 77 | 📦 9k | ⭐ 11 | 🟢 february|
| 🔗 [text2phoneme](https://github.com/korguchi/text2phoneme) | - | - | ⭐ 13 | 🔴 may 2023|
| 🔗 [jntajis-python](https://github.com/opencollector/jntajis-python) | 📥 1k | 📦 120k | ⭐ 21 | 🟢 march|
| 🔗 [wiredify](https://github.com/eggplants/wiredify) | 📥 14 | 📦 6k | ⭐ 3 | 🟡 december 2025|
| 🔗 [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) | 📥 48 | 📦 4k | ⭐ 7 | 🟢 february|
| 🔗 [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) | 📥 32 | 📦 14k | ⭐ 8 | 🔴 april 2024|
| 🔗 [Jusho](https://github.com/nagataaaas/Jusho) | 📥 484 | 📦 56k | ⭐ 11 | 🔴 june 2024|
| 🔗 [yurenizer](https://github.com/sea-turt1e/yurenizer) | 📥 87 | 📦 18k | ⭐ 5 | 🔴 march 2025|
| 🔗 [e2k](https://github.com/Patchethium/e2k) | 📥 727 | 📦 27k | ⭐ 16 | 🟢 march|
| 🔗 [alkana.py](https://github.com/zomysan/alkana.py) | - | - | ⭐ 34 | 🔴 october 2021|
| 🔗 [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) | - | - | ⭐ 4 | 🟢 today|
| 🔗 [kanjiconv](https://github.com/sea-turt1e/kanjiconv) | 📥 138 | 📦 13k | ⭐ 18 | 🟡 october 2025|
| 🔗 [kanjize](https://github.com/nagataaaas/kanjize) | 📥 12k | 📦 2M | ⭐ 68 | 🟡 june 2025|


### Preprocessor
在分析前进行文本规范化与清理的库

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - 针对mecab-neologd的日语文本规范化工具
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - 纯Python日语字符互转器，支持平假名、片假名、半角和全角。
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - 一个快速转换日语半角和全角字符的转换器
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 一款强大的日语网页文本清理工具
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 管理多个前处理的文本前处理工具
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho是一个Python模块，用于在日语中半角片假名和全角片假名之间进行双向转换的工具。
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - 另一个快速的日语字符串转换器
 * [kairyou](https://github.com/bikatr7/kairyou) - 使用SpaCy快速预处理日文文本，以便进行日文翻译或其他自然语言处理任务。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [neologdn](https://github.com/ikegami-yukino/neologdn) | 📥 10k | 📦 1M | ⭐ 288 | 🟡 december 2025|
| 🔗 [jaconv](https://github.com/ikegami-yukino/jaconv) | 📥 579k | 📦 65M | ⭐ 344 | 🟢 february|
| 🔗 [mojimoji](https://github.com/studio-ousia/mojimoji) | 📥 72k | 📦 12M | ⭐ 152 | 🔴 january 2024|
| 🔗 [text-cleaning](https://github.com/ku-nlp/text-cleaning) | - | - | ⭐ 12 | 🔴 november 2022|
| 🔗 [HojiChar](https://github.com/HojiChar/HojiChar) | 📥 34k | 📦 981k | ⭐ 126 | 🟢 april|
| 🔗 [utsuho](https://github.com/juno-rmks/utsuho) | 📥 100 | 📦 22k | ⭐ 5 | 🟢 march|
| 🔗 [python-habachen](https://github.com/Hizuru3/python-habachen) | 📥 8k | 📦 2M | ⭐ 6 | 🟡 october 2025|
| 🔗 [kairyou](https://github.com/bikatr7/kairyou) | 📥 231 | 📦 31k | ⭐ 6 | 🟡 june 2025|


### Sentence spliter
自动检测句子边界并分割文本的库

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日语文本句子边界消歧工具
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日语句子分割器
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 又一个用于日语文本的句子级分词器
 * [budoux](https://github.com/google/budoux) - 独立的。小巧的。语言中立的。BudouX是机器学习驱动的断行组织工具Budou的继承者。
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - Python的日语句子分割库
 * [hasami](https://github.com/mkartawijaya/hasami) - 一个用于对日语文本进行句子分割的工具
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - 用Rust编写的Python日语文本分段器
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日语句子分割工具比较
 * [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) - 通过一个由Rust加速的Python库，日本语句子分割速度提高了40-250倍，几乎完全兼容megagonlabs/bunkai的API。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bunkai](https://github.com/megagonlabs/bunkai) | 📥 664 | 📦 111k | ⭐ 199 | 🔴 august 2023|
| 🔗 [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) | 📥 15 | 📦 5k | ⭐ 14 | 🔴 february 2021|
| 🔗 [sengiri](https://github.com/ikegami-yukino/sengiri) | 📥 54 | 📦 136k | ⭐ 24 | 🟡 november 2025|
| 🔗 [budoux](https://github.com/google/budoux) | 📥 9k | 📦 470k | ⭐ 1.6k | 🟢 last friday|
| 🔗 [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) | 📥 3k | 📦 198k | ⭐ 74 | 🔴 april 2023|
| 🔗 [hasami](https://github.com/mkartawijaya/hasami) | 📥 323 | 📦 40k | ⭐ 6 | 🔴 february 2021|
| 🔗 [kuzukiri](https://github.com/alinear-corp/kuzukiri) | 📥 198 | 📦 27k | ⭐ 6 | 🟡 june 2025|
| 🔗 [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) | - | - | ⭐ 9 | 🔴 february 2023|
| 🔗 [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) | 📥 537 | 📦 5k | ⭐ 72 | 🟡 october 2025|


### Sentiment analysis
分析文本情感和情绪极性的库

 * [oseti](https://github.com/ikegami-yukino/oseti) - 基于词典的日语情感分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 日语文档的负面和正面分类判断。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日语文本情感分析器
 * [asari](https://github.com/Hironsan/asari) - Python实现的日语情感分析器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [oseti](https://github.com/ikegami-yukino/oseti) | 📥 229 | 📦 168k | ⭐ 97 | 🟡 august 2025|
| 🔗 [negapoji](https://github.com/liaoziyang/negapoji) | - | - | ⭐ 151 | 🔴 august 2017|
| 🔗 [pymlask](https://github.com/ikegami-yukino/pymlask) | 📥 48 | 📦 66k | ⭐ 116 | 🔴 july 2024|
| 🔗 [asari](https://github.com/Hironsan/asari) | 📥 108 | 📦 80k | ⭐ 153 | 🔴 october 2022|


### Machine translation
在不同语言之间自动翻译文本的库

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawl预训练神经机器翻译（NMT）模型的示例用法。
 * [JASS](https://github.com/Mao-KU/JASS) - JASS：面向日本特定序列到序列预训练的神经机器翻译（LREC2020）和基于语言驱动的多任务预训练的低资源神经机器翻译（ACM TALLIP）。
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 一份针对日英机器翻译鲁棒性的现象级评估数据集。该数据集基于MTNT数据集，额外注释了四种语言现象：专有名词、缩写名词、口语表达和变体。COLING 2020。
 * [VISA](https://github.com/ku-nlp/VISA) - 一份用于视觉场景感知机器翻译的模糊字幕数据集
 * [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) - 使用本地执行的plamo-2-translate模型进行翻译的命令行界面。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) | - | - | ⭐ 105 | 🔴 april 2021|
| 🔗 [JASS](https://github.com/Mao-KU/JASS) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [PheMT](https://github.com/cl-tohoku/PheMT) | - | - | ⭐ 19 | 🔴 february 2021|
| 🔗 [VISA](https://github.com/ku-nlp/VISA) | - | - | ⭐ 14 | 🔴 october 2022|
| 🔗 [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) | - | - | ⭐ 339 | 🟢 last wednesday|


### Named entity recognition
从文本中提取人名、地名和组织名的库

 * [namaco](https://github.com/chakki-works/namaco) - 基于字符的命名实体识别。
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia是来自维基百科的扩展命名实体词典。
 * [noyaki](https://github.com/ken11/noyaki) - 将字符跨度标签信息转换为基于分词文本的标签信息。
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - 用于BERT模型微调的代码。这是一个用于创建和使用用于命名实体识别任务的模型的示例。
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 基于详细的注释标准的病例报告语料库，进行实体和关系抽取精度推理的代码。
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp，一个用于对日语文本进行地理标记的Python模块。
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - 使用BERT进行日语命名实体抽取的微调程序
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - 用于调整仅编码器和编码器-解码器变压器以适应日语的示例（Hugging Face）资源
 * [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) - BERT模型微调用于命名实体识别


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namaco](https://github.com/chakki-works/namaco) | - | - | ⭐ 40 | 🔴 february 2018|
| 🔗 [entitypedia](https://github.com/chakki-works/entitypedia) | - | - | ⭐ 13 | 🔴 december 2018|
| 🔗 [noyaki](https://github.com/ken11/noyaki) | 📥 254 | 📦 21k | ⭐ 5 | 🔴 august 2022|
| 🔗 [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) | - | - | ⭐ 11 | 🔴 june 2022|
| 🔗 [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) | - | - | ⭐ 1 | 🔴 november 2021|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 79 | 📦 22k | ⭐ 22 | 🟢 march|
| 🔗 [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) | - | - | ⭐ 5 | 🔴 september 2022|
| 🔗 [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) | - | - | ⭐ 16 | 🔴 october 2023|
| 🔗 [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) | - | - | ⭐ 2 | 🔴 june 2024|


### OCR
从图像中识别文字并转换为文本的库

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
 * [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) - 一个简单的漫画OCR（日本传统和日本竖排）
 * [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) - 评估对日语文章图像的OCR性能
 * [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) - 在Manga109s数据集上对PaddleOCR-VL进行微调，用于日本漫画文本识别。基础模型在漫画中垂直日文文本阅读顺序方面存在困难。经过微调后，模型能正确处理漫画特定的文本布局。
 * [MangaOCR](https://github.com/gnurt2041/MangaOCR) - 一个轻量级的OCR模型，特别适用于日文文本，尤其是漫画。
 * [meikiocr](https://github.com/rtr46/meikiocr) - 高速、高精度、本地OCR用于日本电子游戏
 * [meikipop](https://github.com/rtr46/meikipop) - 通用日语OCR弹出式词典，适用于Windows、Linux和macOS


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [manga-ocr](https://github.com/kha-white/manga-ocr) | 📥 4k | 📦 276k | ⭐ 2.6k | 🟡 june 2025|
| 🔗 [mokuro](https://github.com/kha-white/mokuro) | 📥 658 | 📦 96k | ⭐ 1.6k | 🟢 february|
| 🔗 [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) | - | - | ⭐ 38 | 🔴 april 2022|
| 🔗 [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) | - | - | ⭐ 248 | 🔴 april 2021|
| 🔗 [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) | - | - | ⭐ 663 | 🟡 september 2025|
| 🔗 [donut](https://github.com/clovaai/donut) | 📥 309 | 📦 199k | ⭐ 6.8k | 🔴 july 2023|
| 🔗 [JMTrans](https://github.com/ttop32/JMTrans) | - | - | ⭐ 90 | 🔴 january 2021|
| 🔗 [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) | - | - | ⭐ 153 | 🔴 july 2023|
| 🔗 [text_recognition](https://github.com/ndl-lab/text_recognition) | - | - | ⭐ 8 | 🔴 july 2023|
| 🔗 [Poricom](https://github.com/blueaxis/Poricom) | - | - | ⭐ 426 | 🔴 june 2023|
| 🔗 [owocr](https://github.com/aurorawright/owocr) | - | - | ⭐ 237 | 🟢 march|
| 🔗 [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) | 📥 1k | 📦 89k | ⭐ 1.4k | 🟢 april|
| 🔗 [findtextcenternet](https://github.com/lithium0003/findtextcenternet) | - | - | ⭐ 60 | 🟡 august 2025|
| 🔗 [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-fogi-manga) | - | - | ⭐ 7 | 🔴 repo not found|
| 🔗 [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) | - | - | ⭐ 1 | 🔴 march 2024|
| 🔗 [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) | - | - | ⭐ 11 | 🟡 december 2025|
| 🔗 [MangaOCR](https://github.com/gnurt2041/MangaOCR) | - | - | ⭐ 35 | 🔴 may 2024|
| 🔗 [meikiocr](https://github.com/rtr46/meikiocr) | 📥 1k | 📦 26k | ⭐ 72 | 🟢 april|
| 🔗 [meikipop](https://github.com/rtr46/meikipop) | - | - | ⭐ 387 | 🟢 april|


### Tool for pretrained models
利用预训练模型提升精度与效率的库

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
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classificationllm-lora-分类
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP语言模型评估工具
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - 该存储库包含已修改的脚本和合并脚本，用于适应Alpaca-Lora适配器的LoRA调谐，假设使用转换为ggml的"gpt-neox"模型的"rinna/japanese-gpt-neox..."。该存储库包含已修改的脚本和合并脚本，用于适应Alpaca-Lora适配器的LoRA调谐，假设使用转换为ggml的"gpt-neox"模型的"rinna/japanese-gpt-neox..."。
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - 这个存储库是为了评估日本语LLM角色扮演的性能而创建的。
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - 该存储库支持YuzuAI的Rakuda排行榜，该排行榜是日本LLMs的日本重点模拟版本，类似于LMSYS的Vicuna评估。
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - 这个工具可以跨多个数据集对日语大规模语言模型进行自动评估。
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - 该存储库包含了LLM-jp模型的监督微调代码。
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - 这是一个整理了在LLM勉强会（LLM-jp）中开发的与LLM的分词器相关的存储库。
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - 日语语言模型金融评估工具
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - 日本维库纳问答基准
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - 燕子项目 大规模语言模型 评估脚本
 * [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) - 燕子项目 后续学习完成的大规模语言模型 评估框架
 * [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) - 预训练的doc2vec模型在日语维基百科上
 * [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) - 一个日语音素级别的BERT存储库


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 339 | 🔴 march 2025|
| 🔗 [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) | 📥 2k | 📦 192k | ⭐ 16 | 🔴 august 2022|
| 🔗 [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) | - | - | ⭐ 9 | 🔴 january 2020|
| 🔗 [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) | - | - | ⭐ 2 | 🔴 april 2021|
| 🔗 [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) | - | - | ⭐ 5 | 🔴 february 2022|
| 🔗 [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) | 📥 33 | 📦 20k | ⭐ 12 | 🔴 june 2021|
| 🔗 [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) | - | - | ⭐ 12 | 🔴 november 2024|
| 🔗 [gector-ja](https://github.com/jonnyli1125/gector-ja) | - | - | ⭐ 19 | 🔴 june 2021|
| 🔗 [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) | - | - | ⭐ 41 | 🔴 september 2021|
| 🔗 [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) | - | - | ⭐ 41 | 🔴 january 2023|
| 🔗 [transformer-copy](https://github.com/youichiro/transformer-copy) | - | - | ⭐ 29 | 🔴 september 2020|
| 🔗 [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [nagisa_bert](https://github.com/taishi-i/nagisa_bert) | 📥 74 | 📦 57k | ⭐ 5 | 🟢 february|
| 🔗 [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) | - | - | ⭐ 18 | 🟢 last tuesday|
| 🔗 [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) | 📥 68 | 📦 28k | ⭐ 5 | 🔴 february 2024|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) | - | - | ⭐ 6 | 🔴 june 2023|
| 🔗 [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) | - | - | ⭐ 1 | 🔴 june 2023|
| 🔗 [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) | - | - | ⭐ 98 | 🔴 july 2023|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) | - | - | ⭐ 19 | 🔴 may 2023|
| 🔗 [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) | - | - | ⭐ 40 | 🔴 november 2023|
| 🔗 [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) | - | - | ⭐ 50 | 🔴 march 2024|
| 🔗 [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | - | - | ⭐ 150 | 🟢 march|
| 🔗 [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) | - | - | ⭐ 62 | 🔴 june 2024|
| 🔗 [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) | - | - | ⭐ 47 | 🟢 march|
| 🔗 [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | - | - | ⭐ 77 | 🟡 january|
| 🔗 [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | - | - | ⭐ 33 | 🔴 june 2024|
| 🔗 [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) | - | - | ⭐ 24 | 🟡 september 2025|
| 🔗 [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) | - | - | ⭐ 27 | 🟡 october 2025|
| 🔗 [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) | - | - | ⭐ 25 | 🔴 january 2019|
| 🔗 [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) | - | - | ⭐ 24 | 🔴 december 2023|


### Others
支持日语处理的其他通用库


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
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/ https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
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
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 用于执行自动生成评估的Python工具
 * [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) - 在Colaboratory上尝试Asagi（使用合成数据集的大规模日语VLM）的示例。
 * [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) - 这个工具会自动评估日本多模态大型语言模型在多个数据集上的表现。
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 用于执行自动生成评估的Python工具
 * [manga109api](https://github.com/manga109/manga109api) - 简单的Python API，用于读取Manga109的注释数据
 * [fastrtc-jp](https://github.com/route250/fastrtc-jp) - 为fastrtc添加日语TTS和STT套件
 * [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) - 使用Python编写的Whisper模型进行语音转文字工具
 * [pocket-researcher](https://github.com/u-masao/pocket-researcher) - 利用LLM的自主调查代理。轻松收集信息，了解概要。
 * [jtransbench](https://github.com/webbigdata-jp/jtransbench) - 一个方便测试日语翻译能力的工具
 * [easyllasa](https://github.com/zuntan03/easyllasa) - EasyLlasa是一种从5到15秒的日语音频和日语文本生成日语音频的TSTS（文本语音转换）工具。
 * [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) - 姓名汉字假名对照模型
 * [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) - 使用OpenReview自动发现和分析论文的日语AI代理程序
 * [pitchbench](https://github.com/shewiiii/pitchbench) - 实验性的基于日语声调的LLM基准
 * [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) - 从头开始的英语到日语转换器
 * [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) - VOICEVOX核心中使用的深度学习模型推理代码
 * [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) - pyopenjtalk-plus：一个带有额外改进的OpenJTalk的Python封装器
 * [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) - 日语拼写纠正
 * [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) - Python 表情符号
 * [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) - 这个存储库包含了用于训练llm-jp/llm-jp-3-vila-14b的代码，修改自VILA存储库。
 * [kanjivg-radical](https://github.com/yagays/kanjivg-radical) - 汉字VG-部首
 * [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) - 这个项目使用Django构建的Web应用程序可视化日本语Wordnet（日本語ワードネット）。
 * [piper-plus](https://github.com/ayutaz/piper-plus) - 增强版的Piper TTS支持日语，WebAssembly，多GPU训练和质量改进。
 * [Japanera](https://github.com/nagataaaas/Japanera) - 日本年号系统的简易工具
 * [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) - 使用BERT进行日语句子总结
 * [kyujipy](https://github.com/drturnon/kyujipy) - 一个Python库，用于将日文文本从新字体（新字体）转换为旧字体（旧字体）以及反之。
 * [jitenbot](https://github.com/konstantindjairo/jitenbot) - 用于创建个人副本的网络爬虫日语词典
 * [ja-icd10](https://github.com/yagays/ja-icd10) - 用于处理ICD-10国际疾病分类的日语信息的Python软件包
 * [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) - VITS2使用音素级日语BERT
 * [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) - NDCPredictor的机器学习模型（从书目信息推测日本十进分类的fastText预训练模型）
 * [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) - pfmt-bench-fin-ja: 金融领域日语首选多轮对话基准测试
 * [marine-plus](https://github.com/tsukumijima/marine-plus) - MARINE：基于多任务学习的日本口音估计（也支持Windows）
 * [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) - 比较Python中各种日本分词器的速度。
 * [yat](https://github.com/yagays/yat) - yat：又一个用于日语自然语言处理的分词器
 * [igakuqa119](https://github.com/docto-rin/igakuqa119) - 评估第119届日本医师执照考试上的LLMs
 * [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) - 使用Transformers的RemBertTokenizerFast进行日语长单位词标记化。
 * [ibus-jig](https://github.com/y-koj/ibus-jig) - ibus-jig：使用GPT-4的日语输入法
 * [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) - 一个轻量级的Python库，旨在根据可定制的规则从日文文本中过滤停用词。
 * [yasumail](https://github.com/terallite/yasumail) - 用于机器学习训练数据的合成日本商务电子邮件生成器
 * [himotoki](https://github.com/msr2903/himotoki) - 一个基于Python的日语分词器、词典、形态分析器和罗马化工具。基于JMDict用于语言学习。
 * [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) - 用大型语言模型（LLMs）合成填充物丰富、短话语的日语对话脚本的工具包。该项目旨在通过两个阶段生成数据：种子生成（元数据创建）和对话生成（脚本创建）。
 * [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) - 评估多模态大型语言模型在竖排日文文本上的表现
 * [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) - 这段代码是用于从大规模语言模型（LLM）的训练语料库中过滤特别需要注意的个人信息，即“需要注意的个人信息”。
 * [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) - 评估多模态大型语言模型在竖排日文文本上的表现
 * [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) - 从小说文本中构建闲聊对话语料库的方法
 * [OneCompression](https://github.com/FujitsuResearch/OneCompression) - 富士通研究所推出的LLM后学习量子化（PTQ）管道。集成了QEP（NeurIPS 2025）、ILP混合精度、旋转前处理、vLLM插件。论文：[arXiv:2603.28845](https://arxiv.org/abs/2603.28845)。
 * [manga-translator](https://github.com/georgescutelnicu/manga-translator) - 将漫画图片中的对话框内的文本翻译成简体中文。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namedivider-python](https://github.com/rskmoi/namedivider-python) | 📥 909 | 📦 84k | ⭐ 251 | 🟡 november 2025|
| 🔗 [asa-python](https://github.com/ikegami-yukino/asa-python) | 📥 28 | 📦 31k | ⭐ 11 | 🔴 february 2019|
| 🔗 [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) | - | - | ⭐ 22 | 🔴 january 2020|
| 🔗 [toiro](https://github.com/taishi-i/toiro) | 📥 17 | 📦 27k | ⭐ 121 | 🟡 november 2025|
| 🔗 [ja-timex](https://github.com/yagays/ja-timex) | 📥 812 | 📦 95k | ⭐ 140 | 🔴 november 2023|
| 🔗 [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) | - | - | ⭐ 137 | 🔴 march 2019|
| 🔗 [daaja](https://github.com/kajyuuen/daaja) | 📥 71 | 📦 25k | ⭐ 64 | 🔴 february 2023|
| 🔗 [accel-brain-code](https://github.com/accel-brain/accel-brain-code) | 📥 171 | 📦 150k | ⭐ 324 | 🔴 december 2023|
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 339 | 🔴 march 2025|
| 🔗 [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) | 📥 172 | 📦 53k | ⭐ 10 | 🔴 june 2024|
| 🔗 [nlplot](https://github.com/takapy0210/nlplot) | 📥 356 | 📦 110k | ⭐ 238 | 🔴 september 2022|
| 🔗 [rake-ja](https://github.com/kanjirz50/rake-ja) | - | - | ⭐ 21 | 🔴 october 2018|
| 🔗 [jel](https://github.com/izuna385/jel) | 📥 17 | 📦 8k | ⭐ 12 | 🔴 july 2021|
| 🔗 [MedNER-J](https://github.com/sociocom/MedNER-J) | - | - | ⭐ 18 | 🔴 may 2022|
| 🔗 [zunda-python](https://github.com/ikegami-yukino/zunda-python) | 📥 8 | 📦 6k | ⭐ 10 | 🔴 november 2019|
| 🔗 [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [showcase](https://github.com/cl-tohoku/showcase) | 📥 10 | 📦 7k | ⭐ 6 | 🔴 june 2018|
| 🔗 [darts-clone-python](https://github.com/rixwew/darts-clone-python) | 📥 3k | 📦 9M | ⭐ 20 | 🔴 april 2022|
| 🔗 [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [desuwa](https://github.com/megagonlabs/desuwa) | 📥 31 | 📦 10k | ⭐ 6 | 🔴 may 2022|
| 🔗 [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) | - | - | ⭐ 277 | 🔴 may 2016|
| 🔗 [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) | - | - | ⭐ 66 | 🔴 april 2021|
| 🔗 [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) | - | - | ⭐ 26 | 🔴 june 2019|
| 🔗 [DNorm-J](https://github.com/sociocom/DNorm-J) | - | - | ⭐ 9 | 🔴 june 2022|
| 🔗 [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) | 📥 180 | 📦 66k | ⭐ 9 | 🔴 september 2022|
| 🔗 [ishi](https://github.com/ku-nlp/ishi) | 📥 13 | 📦 6k | ⭐ 2 | 🔴 may 2020|
| 🔗 [python-npylm](https://github.com/musyoku/python-npylm) | - | - | ⭐ 34 | 🔴 january 2019|
| 🔗 [python-npycrf](https://github.com/musyoku/python-npycrf) | - | - | ⭐ 11 | 🔴 march 2018|
| 🔗 [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) | - | - | ⭐ 16 | 🔴 october 2017|
| 🔗 [negima](https://github.com/cocodrips/negima) | 📥 38 | 📦 16k | ⭐ 14 | 🔴 august 2018|
| 🔗 [YouyakuMan](https://github.com/neilctwu/YouyakuMan) | - | - | ⭐ 52 | 🔴 september 2020|
| 🔗 [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) | 📥 1k | 📦 2M | ⭐ 21 | 🔴 april 2020|
| 🔗 [kantan](https://github.com/itayperl/kantan) | - | - | ⭐ 8 | 🔴 october 2024|
| 🔗 [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) | - | - | ⭐ 40 | 🔴 september 2017|
| 🔗 [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) | - | - | ⭐ 10 | 🔴 august 2022|
| 🔗 [chirptext](https://github.com/letuananh/chirptext) | 📥 6k | 📦 224k | ⭐ 7 | 🔴 october 2022|
| 🔗 [yubin](https://github.com/alvations/yubin) | 📥 10 | 📦 3k | ⭐ 3 | 🔴 october 2019|
| 🔗 [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) | 📥 87 | 📦 24k | ⭐ 6 | 🔴 february 2021|
| 🔗 [japanese2phoneme](https://github.com/iory/japanese2phoneme) | 📥 15 | 📦 4k | ⭐ 1 | 🔴 february 2022|
| 🔗 [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) | - | - | ⭐ 1 | 🔴 march 2022|
| 🔗 [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) | - | - | ⭐ 11 | 🔴 september 2017|
| 🔗 [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) | - | - | ⭐ 8 | 🟡 june 2025|
| 🔗 [JLM](https://github.com/jiali-ms/JLM) | - | - | ⭐ 111 | 🔴 june 2019|
| 🔗 [NTM](https://github.com/m3yrin/NTM) | - | - | ⭐ 13 | 🔴 july 2019|
| 🔗 [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) | - | - | ⭐ 41 | 🔴 march 2021|
| 🔗 [text-generation](https://github.com/discus0434/text-generation) | - | - | ⭐ 19 | 🟡 august 2025|
| 🔗 [chainer_nic](https://github.com/yuyay/chainer_nic) | - | - | ⭐ 17 | 🔴 december 2018|
| 🔗 [unihan-lm](https://github.com/JetRunner/unihan-lm) | - | - | ⭐ 2 | 🔴 november 2020|
| 🔗 [mbart-finetuning](https://github.com/ken11/mbart-finetuning) | - | - | ⭐ 3 | 🔴 october 2021|
| 🔗 [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) | - | - | ⭐ 47 | 🔴 november 2023|
| 🔗 [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) | - | - | ⭐ 72 | 🔴 september 2022|
| 🔗 [Grongish](https://github.com/shogo82148/Grongish) | - | - | ⭐ 25 | 🟡 december 2025|
| 🔗 [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) | - | - | ⭐ 10 | 🔴 january 2020|
| 🔗 [snark](https://github.com/hiraokusky/snark) | - | - | ⭐ 11 | 🔴 march 2020|
| 🔗 [toEmoji](https://github.com/mkan0141/toEmoji) | - | - | ⭐ 4 | 🔴 april 2018|
| 🔗 [termextract](https://github.com/kanjirz50/termextract) | - | - | ⭐ 18 | 🔴 september 2018|
| 🔗 [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) | - | - | ⭐ 1 | 🔴 july 2022|
| 🔗 [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) | - | - | ⭐ 6 | 🔴 june 2017|
| 🔗 [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) | - | - | ⭐ 5 | 🔴 june 2017|
| 🔗 [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) | - | - | ⭐ 5 | 🔴 december 2017|
| 🔗 [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) | - | - | ⭐ 69 | 🔴 september 2022|
| 🔗 [neural_ime](https://github.com/yohokuno/neural_ime) | - | - | ⭐ 67 | 🔴 december 2016|
| 🔗 [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) | - | - | ⭐ 178 | 🔴 september 2017|
| 🔗 [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) | 📥 150k | 📦 174k | ⭐ repo not found | 🔴 november 2015|
| 🔗 [AugLy-jp](https://github.com/chck/AugLy-jp) | 📥 38 | 📦 31k | ⭐ 7 | 🔴 september 2021|
| 🔗 [furigana4epub](https://github.com/Mumumu4/furigana4epub) | 📥 69 | 📦 12k | ⭐ 31 | 🔴 september 2021|
| 🔗 [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) | 📥 39 | 📦 20k | ⭐ 12 | 🔴 march 2025|
| 🔗 [jageocoder](https://github.com/t-sagara/jageocoder) | 📥 3k | 📦 363k | ⭐ 96 | 🟢 march|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 79 | 📦 22k | ⭐ 22 | 🟢 march|
| 🔗 [nksnd](https://github.com/yoriyuki/nksnd) | - | - | ⭐ 26 | 🔴 may 2018|
| 🔗 [JaMIE](https://github.com/racerandom/JaMIE) | - | - | ⭐ 9 | 🟢 march|
| 🔗 [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) | - | - | ⭐ 48 | 🔴 august 2017|
| 🔗 [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) | - | - | ⭐ 19 | 🔴 july 2019|
| 🔗 [5ch-analysis](https://github.com/GINK03/5ch-analysis) | - | - | ⭐ 73 | 🔴 november 2018|
| 🔗 [tweet_extructor](https://github.com/tatHi/tweet_extructor) | - | - | ⭐ 3 | 🔴 august 2022|
| 🔗 [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) | - | - | ⭐ 2 | 🔴 august 2018|
| 🔗 [jinf](https://github.com/hkiyomaru/jinf) | 📥 286 | 📦 57k | ⭐ 4 | 🔴 december 2022|
| 🔗 [kwja](https://github.com/ku-nlp/kwja) | 📥 437 | 📦 58k | ⭐ 142 | 🟡 august 2025|
| 🔗 [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) | - | - | ⭐ 6 | 🔴 december 2022|
| 🔗 [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) | - | - | ⭐ 12 | 🔴 october 2022|
| 🔗 [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) | - | - | ⭐ 2 | 🔴 october 2022|
| 🔗 [cihai](https://github.com/cihai/cihai) | 📥 719 | 📦 214k | ⭐ 93 | 🟢 today|
| 🔗 [marine](https://github.com/6gsn/marine) | 📥 106 | 📦 15k | ⭐ 36 | 🔴 september 2022|
| 🔗 [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) | - | - | ⭐ 32 | 🔴 december 2022|
| 🔗 [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [radicalchar](https://github.com/yamamaya/radicalchar) | - | - | ⭐ 9 | 🔴 december 2022|
| 🔗 [akaza](https://github.com/tokuhirom/akaza) | - | - | ⭐ 250 | 🟢 april|
| 🔗 [posuto](https://github.com/polm/posuto) | 📥 5k | 📦 708k | ⭐ 226 | 🟢 april|
| 🔗 [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) | - | - | ⭐ 268 | 🔴 september 2022|
| 🔗 [ibus-hiragana](https://github.com/esrille/ibus-hiragana) | - | - | ⭐ 78 | 🟢 march|
| 🔗 [furiganapad](https://github.com/esrille/furiganapad) | - | - | ⭐ 19 | 🔴 april 2025|
| 🔗 [chikkarpy](https://github.com/WorksApplications/chikkarpy) | 📥 298 | 📦 61k | ⭐ 55 | 🔴 february 2022|
| 🔗 [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) | - | - | ⭐ 36 | 🔴 may 2022|
| 🔗 [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) | - | - | ⭐ 183 | 🔴 october 2024|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [shuwa](https://github.com/google/shuwa) | - | - | ⭐ 146 | 🔴 december 2022|
| 🔗 [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) | - | - | ⭐ 6 | 🔴 october 2022|
| 🔗 [tra-fugu](https://github.com/tos-kamiya/tra-fugu) | - | - | ⭐ 6 | 🔴 march 2023|
| 🔗 [fugumt](https://github.com/s-taka/fugumt) | - | - | ⭐ 64 | 🔴 february 2021|
| 🔗 [JaSPICE](https://github.com/keio-smilab23/JaSPICE) | 📥 8 | 📦 2k | ⭐ 9 | 🔴 november 2023|
| 🔗 [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) | - | - | ⭐ 48 | 🔴 april 2023|
| 🔗 [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) | 📥 17k | 📦 1M | ⭐ 249 | 🔴 april 2025|
| 🔗 [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) | 📥 23 | 📦 8k | ⭐ 27 | 🔴 february 2024|
| 🔗 [N46Whisper](https://github.com/Ayanaminn/N46Whisper) | - | - | ⭐ 1.7k | 🔴 february 2025|
| 🔗 [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) | - | - | ⭐ 17 | 🔴 may 2024|
| 🔗 [pdf-translator](https://github.com/discus0434/pdf-translator) | - | - | ⭐ 340 | 🔴 may 2024|
| 🔗 [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) | - | - | ⭐ 1 | 🔴 december 2022|
| 🔗 [mozc-devices](https://github.com/google/mozc-devices) | - | - | ⭐ 2.7k | 🟡 november 2025|
| 🔗 [natsume](https://github.com/faruzan0820/natsume) | 📥 7 | 📦 3k | ⭐ repo not found | 🔴 repo not found|
| 🔗 [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) | - | - | ⭐ 42 | 🔴 january 2024|
| 🔗 [ja-law-parser](https://github.com/takuyaa/ja-law-parser) | - | - | ⭐ 25 | 🔴 january 2024|
| 🔗 [dictation-kit](https://github.com/julius-speech/dictation-kit) | - | - | ⭐ 164 | 🔴 april 2019|
| 🔗 [julius4seg](https://github.com/Hiroshiba/julius4seg) | - | - | ⭐ 7 | 🔴 august 2021|
| 🔗 [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) | - | - | ⭐ 1.7k | 🟢 today|
| 🔗 [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) | - | - | ⭐ 64 | 🔴 june 2024|
| 🔗 [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [bertjsc](https://github.com/er-ri/bertjsc) | - | - | ⭐ 14 | 🔴 august 2024|
| 🔗 [llm-leaderboard](https://github.com/wandb/llm-leaderboard) | - | - | ⭐ 92 | 🟡 september 2025|
| 🔗 [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) | - | - | ⭐ 18 | 🟢 last tuesday|
| 🔗 [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) | - | - | ⭐ 11 | 🔴 march 2024|
| 🔗 [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) | - | - | ⭐ 69 | 🔴 october 2023|
| 🔗 [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) | - | - | ⭐ 16 | 🔴 june 2024|
| 🔗 [t5-japanese](https://github.com/sonoisa/t5-japanese) | - | - | ⭐ 118 | 🟡 september 2025|
| 🔗 [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) | - | - | ⭐ 5 | 🔴 april 2024|
| 🔗 [jmteb](https://github.com/sbintuitions/jmteb) | - | - | ⭐ 89 | 🟢 march|
| 🔗 [pydomino](https://github.com/dwangomediavillage/pydomino) | - | - | ⭐ 39 | 🟡 august 2025|
| 🔗 [easynovelassistant](https://github.com/zuntan03/easynovelassistant) | - | - | ⭐ 224 | 🔴 july 2024|
| 🔗 [clip-japanese](https://github.com/sonoisa/clip-japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) | - | - | ⭐ 50 | 🟢 last thursday|
| 🔗 [deep-question-generation](https://github.com/sonoisa/deep-question-generation) | - | - | ⭐ 12 | 🔴 march 2023|
| 🔗 [magpie-nemotron](https://github.com/aratako/magpie-nemotron) | - | - | ⭐ 9 | 🔴 july 2024|
| 🔗 [qlora_ja](https://github.com/sosuke115/qlora_ja) | - | - | ⭐ 1 | 🔴 july 2024|
| 🔗 [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) | - | - | ⭐ 28 | 🟢 april|
| 🔗 [shisa-v2](https://github.com/shisa-ai/shisa-v2) | - | - | ⭐ 28 | 🟡 december 2025|
| 🔗 [llm-translator](https://github.com/hpprc/llm-translator) | - | - | ⭐ 20 | 🔴 january 2025|
| 🔗 [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) | - | - | ⭐ 9 | 🔴 september 2024|
| 🔗 [rag-japanese](https://github.com/akimfromparis/rag-japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [monaka](https://github.com/komiya-lab/monaka) | - | - | ⭐ 5 | 🔴 january 2025|
| 🔗 [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) | - | - | ⭐ 3 | 🔴 september 2024|
| 🔗 [substring-word-finder](https://github.com/toufu-24/substring-word-finder) | - | - | ⭐ 4 | 🟡 november 2025|
| 🔗 [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) | - | - | ⭐ 6 | 🔴 december 2024|
| 🔗 [text2dataset](https://github.com/llm-jp/text2dataset) | - | - | ⭐ 28 | 🔴 january 2025|
| 🔗 [mecab-web-api](https://github.com/bungoume/mecab-web-api) | - | - | ⭐ 40 | 🔴 july 2022|
| 🔗 [mecab_controller](https://github.com/ajatt-tools/mecab_controller) | - | - | ⭐ 19 | 🟢 march|
| 🔗 [vits](https://github.com/zassou65535/vits) | - | - | ⭐ 92 | 🔴 february 2023|
| 🔗 [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) | - | - | ⭐ 48 | 🟡 october 2025|
| 🔗 [kudasai](https://github.com/bikatr7/kudasai) | - | - | ⭐ 26 | 🟡 june 2025|
| 🔗 [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) | - | - | ⭐ 2 | 🔴 september 2023|
| 🔗 [add-dictionary](https://github.com/massao000/add-dictionary) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [j-moshi](https://github.com/nu-dialogue/j-moshi) | - | - | ⭐ 306 | 🟡 june 2025|
| 🔗 [jatts](https://github.com/unilight/jatts) | - | - | ⭐ 44 | 🟢 march|
| 🔗 [tsukasa-speech](https://github.com/respaired/tsukasa-speech) | - | - | ⭐ 64 | 🟡 may 2025|
| 🔗 [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) | - | - | ⭐ 2 | 🔴 february 2021|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 41 | 🟡 december 2025|
| 🔗 [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) | - | - | ⭐ 1 | 🔴 march 2025|
| 🔗 [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) | - | - | ⭐ 41 | 🟢 april|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 41 | 🟡 december 2025|
| 🔗 [manga109api](https://github.com/manga109/manga109api) | 📥 202 | 📦 46k | ⭐ 129 | 🔴 march 2022|
| 🔗 [fastrtc-jp](https://github.com/route250/fastrtc-jp) | - | - | ⭐ 5 | 🟡 may 2025|
| 🔗 [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) | - | - | ⭐ 17 | 🟡 january|
| 🔗 [pocket-researcher](https://github.com/u-masao/pocket-researcher) | - | - | ⭐ 10 | 🔴 april 2025|
| 🔗 [jtransbench](https://github.com/webbigdata-jp/jtransbench) | - | - | ⭐ 13 | 🟡 october 2025|
| 🔗 [easyllasa](https://github.com/zuntan03/easyllasa) | - | - | ⭐ 26 | 🟡 september 2025|
| 🔗 [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) | - | - | ⭐ 115 | 🟡 december 2025|
| 🔗 [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) | - | - | ⭐ 13 | 🟡 november 2025|
| 🔗 [pitchbench](https://github.com/shewiiii/pitchbench) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) | - | - | ⭐ 31 | 🟡 december 2025|
| 🔗 [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) | 📥 4k | 📦 474k | ⭐ 57 | 🟢 march|
| 🔗 [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) | 📥 71 | 📦 38k | ⭐ 6 | 🔴 december 2018|
| 🔗 [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) | - | - | ⭐ 10 | 🟡 august 2025|
| 🔗 [kanjivg-radical](https://github.com/yagays/kanjivg-radical) | - | - | ⭐ 106 | 🔴 august 2018|
| 🔗 [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) | - | - | ⭐ 3 | 🔴 november 2022|
| 🔗 [piper-plus](https://github.com/ayutaz/piper-plus) | - | - | ⭐ 128 | 🟢 last wednesday|
| 🔗 [Japanera](https://github.com/nagataaaas/Japanera) | 📥 4k | 📦 373k | ⭐ 35 | 🟡 june 2025|
| 🔗 [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) | - | - | ⭐ 49 | 🔴 december 2019|
| 🔗 [kyujipy](https://github.com/drturnon/kyujipy) | 📥 52 | 📦 23k | ⭐ 22 | 🟡 january|
| 🔗 [jitenbot](https://github.com/konstantindjairo/jitenbot) | - | - | ⭐ 4 | 🔴 december 2024|
| 🔗 [ja-icd10](https://github.com/yagays/ja-icd10) | - | - | ⭐ 5 | 🔴 july 2021|
| 🔗 [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) | - | - | ⭐ 14 | 🔴 december 2023|
| 🔗 [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) | - | - | ⭐ 13 | 🔴 august 2021|
| 🔗 [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) | - | - | ⭐ 9 | 🔴 march 2025|
| 🔗 [marine-plus](https://github.com/tsukumijima/marine-plus) | 📥 97 | 📦 12k | ⭐ 8 | 🟢 march|
| 🔗 [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) | - | - | ⭐ 7 | 🔴 february 2022|
| 🔗 [yat](https://github.com/yagays/yat) | - | - | ⭐ 7 | 🔴 june 2018|
| 🔗 [igakuqa119](https://github.com/docto-rin/igakuqa119) | - | - | ⭐ 8 | 🟡 january|
| 🔗 [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) | - | - | ⭐ 6 | 🔴 december 2021|
| 🔗 [ibus-jig](https://github.com/y-koj/ibus-jig) | - | - | ⭐ 4 | 🔴 december 2023|
| 🔗 [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) | 📥 26 | 📦 5k | ⭐ 4 | 🔴 november 2024|
| 🔗 [yasumail](https://github.com/terallite/yasumail) | - | - | ⭐ 3 | 🟡 january|
| 🔗 [himotoki](https://github.com/msr2903/himotoki) | 📥 101 | 📦 4k | ⭐ 3 | 🟢 february|
| 🔗 [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) | - | - | ⭐ 0 | 🟡 january|
| 🔗 [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) | - | - | ⭐ 7 | 🔴 march 2025|
| 🔗 [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) | - | - | ⭐ 0 | 🟢 february|
| 🔗 [OneCompression](https://github.com/FujitsuResearch/OneCompression) | - | - | ⭐ 317 | 🟢 march|
| 🔗 [manga-translator](https://github.com/georgescutelnicu/manga-translator) | - | - | ⭐ 26 | 🟢 last tuesday|


## C++

### Morphology analysis
高性能的日语形态素分析库

 * [mecab](https://github.com/taku910/mecab) - 又一个日语形态分析器
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++（一个形态分析工具包）
 * [kytea](https://github.com/neubig/kytea) - 京都文本分析工具包，用于词语分割和发音估计等。
 * [juman](https://github.com/ku-nlp/juman) - 日本语形态分析系统JUMAN


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab](https://github.com/taku910/mecab) | - | - | ⭐ 1.1k | 🔴 february 2025|
| 🔗 [jumanpp](https://github.com/ku-nlp/jumanpp) | - | - | ⭐ 411 | 🟢 last friday|
| 🔗 [kytea](https://github.com/neubig/kytea) | - | - | ⭐ 212 | 🔴 april 2020|
| 🔗 [juman](https://github.com/ku-nlp/juman) | - | - | ⭐ 12 | 🔴 december 2021|

### Parsing
用于日语句法与依存分析的库

 * [cabocha](https://github.com/taku910/cabocha) - 另一个日语依存结构分析器
 * [knp](https://github.com/ku-nlp/knp) - 一个日语解析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [cabocha](https://github.com/taku910/cabocha) | - | - | ⭐ 121 | 🔴 february 2025|
| 🔗 [knp](https://github.com/ku-nlp/knp) | - | - | ⭐ 34 | 🔴 november 2023|

### Others
其他与日语NLP相关的库

 * [jsc](https://github.com/yohokuno/jsc) - 联合源通道模型用于日语假名汉字转换、汉语拼音输入和CJE混合输入。
 * [aquaskk](https://github.com/codefirst/aquaskk) - 没有形态分析的输入法。
 * [mozc](https://github.com/google/mozc) - Mozc - 一款为多平台设计的日语输入法编辑器
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch：一个（精确|前缀|近似）字符串匹配库
 * [resembla](https://github.com/tuem/resembla) - Resembla：基于单词的日语相似句子搜索库
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ 适用于Windows的类似SKK的日语输入法编辑器
 * [mozuku](https://github.com/t3tra-dev/mozuku) - 进行日语文章分析和校正的LSP服务器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jsc](https://github.com/yohokuno/jsc) | - | - | ⭐ 15 | 🔴 december 2012|
| 🔗 [aquaskk](https://github.com/codefirst/aquaskk) | - | - | ⭐ 369 | 🔴 july 2023|
| 🔗 [mozc](https://github.com/google/mozc) | - | - | ⭐ 2.9k | 🟢 last tuesday|
| 🔗 [trimatch](https://github.com/tuem/trimatch) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [resembla](https://github.com/tuem/resembla) | - | - | ⭐ 73 | 🟡 august 2025|
| 🔗 [corvusskk](https://github.com/nathancorvussolis/corvusskk) | - | - | ⭐ 364 | 🟢 today|
| 🔗 [mozuku](https://github.com/t3tra-dev/mozuku) | - | - | ⭐ 414 | 🟢 april|


## Rust crate

### Morphology analysis
用Rust实现的日语形态素分析包

 * [lindera](https://github.com/lindera-morphology/lindera) - 一个形态分析库。
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto：基于点预测的加速分词器
 * [goya](https://github.com/Leko/goya) - 用Rust编写的日语形态分析
 * [vibrato](https://github.com/daac-tools/vibrato) - 颤音：基于维特比加速的分词器
 * [yoin](https://github.com/agatan/yoin) - 一个用纯Rust编写的日语形态分析器
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 安全的Rust绑定，用于mecab词性和形态分析库。
 * [awabi](https://github.com/nakagami/awabi) - 一个使用mecab字典的形态分析器
 * [kanpyo](https://github.com/togatoga/kanpyo) - 用Rust编写的日语形态分析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera](https://github.com/lindera-morphology/lindera) | - | 📦 1.1M | ⭐ 617 | 🟢 yesterday|
| 🔗 [vaporetto](https://github.com/daac-tools/vaporetto) | - | 📦 203k | ⭐ 257 | 🟢 february|
| 🔗 [goya](https://github.com/Leko/goya) | - | 📦 12k | ⭐ 83 | 🔴 december 2021|
| 🔗 [vibrato](https://github.com/daac-tools/vibrato) | - | 📦 62k | ⭐ 406 | 🟢 february|
| 🔗 [yoin](https://github.com/agatan/yoin) | - | 📦 3k | ⭐ 26 | 🔴 october 2017|
| 🔗 [mecab-rs](https://github.com/tsurai/mecab-rs) | - | 📦 40k | ⭐ 71 | 🔴 september 2023|
| 🔗 [awabi](https://github.com/nakagami/awabi) | - | 📦 24k | ⭐ 10 | 🟡 november 2025|
| 🔗 [kanpyo](https://github.com/togatoga/kanpyo) | - | 📦 2.5k | ⭐ 109 | 🟢 february|


### Converter
用于日语文字与表记转换的包

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 用于检查和转换日语字符（平假名、片假名和罗马字）的实用程序库。
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 一个 Rust 库，用于将日语半角假名和全角英数字转换为普通字符。
 * [kana](https://github.com/gbrlsnchs/kana) - 【镜像】用于将罗马字文本转换为平假名或片假名的CLI程序。
 * [kanaria](https://github.com/samunohito/kanaria) - 这个库提供了平假名、片假名、半角和全角之间的相互转换和识别功能。
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - 这是一个将日本地址分割为都道府县/市区町村/町名/其他部分的库。
 * [yosina](https://github.com/yosina-lib/yosina) - Yosina是一个转译库，处理日本书写中使用的字母和符号。
 * [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) - 快速转换日文半角和全角字符的Rust实现，mojimoji。Rust实现的快速转换器，可在日文半角和全角字符之间转换，mojimoji。
 * [haqumei](https://github.com/o24s/haqumei) - 一个日语字形到音素（G2P）库。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) | - | 📦 377k | ⭐ 90 | 🟢 april|
| 🔗 [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) | - | 📦 64k | ⭐ 19 | 🔴 april 2020|
| 🔗 [kana](https://github.com/gbrlsnchs/kana) | - | - | ⭐ 12 | 🔴 january 2023|
| 🔗 [kanaria](https://github.com/samunohito/kanaria) | - | - | ⭐ 21 | 🟢 february|
| 🔗 [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) | - | - | ⭐ 11 | 🟢 today|
| 🔗 [yosina](https://github.com/yosina-lib/yosina) | - | - | ⭐ 24 | 🟢 yesterday|
| 🔗 [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) | - | - | ⭐ 4 | 🔴 november 2022|
| 🔗 [haqumei](https://github.com/o24s/haqumei) | - | - | ⭐ 1 | 🟢 april|


### Search engine library
用于日语全文检索与索引的库

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Tantivy 的 Lindera 分词器。
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - 使用Vibrato的Tantivy分词器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) | - | 📦 183k | ⭐ 70 | 🟡 january|
| 🔗 [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) | - | 📦 1.5k | ⭐ 3 | 🔴 january 2023|


### Others
其他与日语文字和输入法处理相关的包

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
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - 用于文本转语音应用程序的日语文本预处理器（OpenJTalk在Rust语言中的重写）用于文本转语音应用程序的日语文本预处理器（用Rust语言重写的OpenJTalk）
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - 使用软件从法院网站(https://www.courts.go.jp/index.html) 爬取裁判例数据并生成数据列表。
 * [jisho](https://github.com/eagleflo/jisho) - Jisho是一个提供日语-英语词典的CLI工具和Rust库。
 * [kanalizer](https://github.com/voicevox/kanalizer) - 从英语单词推测发音的库。
 * [koharu](https://github.com/mayocream/koharu) - 使用Rust编写的带有LLM的自动漫画翻译工具。
 * [yomine](https://github.com/mcgrizzz/yomine) - 一个日语词汇挖掘工具，旨在帮助语言学习者挖掘新单词和表达方式。
 * [matsuba](https://github.com/mrpicklepinosaur/matsuba) - 轻量级的用Rust编写的日语输入法
 * [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) - 日本語辞書由Rust支持，支持Telegram机器人，AWS Lambda和Cloudflare Workers。支持LLM和搜索RAG。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [daachorse](https://github.com/daac-tools/daachorse) | - | 📦 868k | ⭐ 258 | 🟢 last wednesday|
| 🔗 [find-simdoc](https://github.com/legalforce-research/find-simdoc) | - | 📦 29k | ⭐ 62 | 🔴 march 2025|
| 🔗 [crawdad](https://github.com/daac-tools/crawdad) | - | 📦 67k | ⭐ 37 | 🔴 january 2025|
| 🔗 [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) | - | - | ⭐ 4 | 🔴 march 2023|
| 🔗 [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [vime](https://github.com/algon-320/vime) | - | - | ⭐ 230 | 🔴 november 2022|
| 🔗 [voicevox_core](https://github.com/VOICEVOX/voicevox_core) | - | - | ⭐ 1.1k | 🟢 today|
| 🔗 [akaza](https://github.com/akaza-im/akaza) | - | - | ⭐ 250 | 🟢 april|
| 🔗 [Jotoba](https://github.com/WeDontPanic/Jotoba) | - | - | ⭐ 201 | 🔴 january 2024|
| 🔗 [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) | - | - | ⭐ 56 | 🟢 february|
| 🔗 [niinii](https://github.com/Netdex/niinii) | - | - | ⭐ 14 | 🟢 march|
| 🔗 [cskk](https://github.com/naokiri/cskk) | - | - | ⭐ 80 | 🟢 march|
| 🔗 [japanki](https://github.com/tysonwu/japanki) | - | - | ⭐ 3 | 🔴 october 2023|
| 🔗 [jpreprocess](https://github.com/jpreprocess/jpreprocess) | - | - | ⭐ 54 | 🟢 february|
| 🔗 [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) | - | - | ⭐ 6 | 🟢 april|
| 🔗 [jisho](https://github.com/eagleflo/jisho) | - | - | ⭐ 18 | 🟢 april|
| 🔗 [kanalizer](https://github.com/voicevox/kanalizer) | - | - | ⭐ 27 | 🟢 april|
| 🔗 [koharu](https://github.com/mayocream/koharu) | - | - | ⭐ 3.7k | 🟢 today|
| 🔗 [yomine](https://github.com/mcgrizzz/yomine) | - | - | ⭐ 50 | 🟢 february|
| 🔗 [matsuba](https://github.com/mrpicklepinosaur/matsuba) | - | - | ⭐ 18 | 🔴 march 2023|
| 🔗 [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) | - | - | ⭐ 70 | 🟢 april|


## JavaScript

### Morphology analysis
可在浏览器或Node.js进行日语形态素分析的库

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日语形态分析器的JavaScript实现
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - Rakuten MA - 用纯JavaScript编写的中文和日文形态分析器（词分割器+词性标注器）。
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - 又一个用于nodejs的mecab包装器
 * [juman-bin](https://github.com/thammin/juman-bin) - 一个用户可扩展的日语形态学分析器。日本语形态学分析系统。
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - 使用MeCab的异步日语形态分析器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji.js](https://github.com/takuyaa/kuromoji.js) | 📥 179k/week | 📦 8.8M | ⭐ 972 | 🔴 november 2018|
| 🔗 [rakutenma](https://github.com/rakuten-nlp/rakutenma) | 📥 16/week | 📦 rate limited by upstream service | ⭐ 472 | 🔴 january 2015|
| 🔗 [node-mecab-ya](https://github.com/golbin/mecab-ya) | 📥 86/week | 📦 7.5k | ⭐ 110 | 🔴 repo not found|
| 🔗 [juman-bin](https://github.com/thammin/juman-bin) | 📥 10/week | 📦 317 | ⭐ 3 | 🔴 may 2017|
| 🔗 [node-mecab-async](https://github.com/hecomi/node-mecab-async) | 📥 5.1k/week | 📦 340k | ⭐ 104 | 🔴 october 2017|


### Converter
用于日语表记与读音转换的库

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
 * [japanese.js](https://github.com/hakatashi/japanese.js) - 用于日文文本处理的Util集合。进行平假名化、片假名化和罗马化处理。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuroshiro](https://github.com/hexenq/kuroshiro) | 📥 14k/week | 📦 457k | ⭐ 966 | 🔴 june 2021|
| 🔗 [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) | 📥 13k/week | 📦 432k | ⭐ 68 | 🔴 august 2018|
| 🔗 [hepburn](https://github.com/lovell/hepburn) | 📥 170k/week | 📦 3.9M | ⭐ 137 | 🟡 september 2025|
| 🔗 [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) | 📥 44k/week | 📦 2.3M | ⭐ 59 | 🔴 february 2023|
| 🔗 [jslingua](https://github.com/kariminf/jslingua) | 📥 174/week | 📦 8.6k | ⭐ 53 | 🔴 october 2023|
| 🔗 [WanaKana](https://github.com/WaniKani/WanaKana) | 📥 44k/week | 📦 2.3M | ⭐ 917 | 🟡 september 2025|
| 🔗 [node-romaji-name](https://github.com/jeresig/node-romaji-name) | 📥 444/week | 📦 15k | ⭐ 41 | 🔴 december 2023|
| 🔗 [kyujitai.js](https://github.com/hakatashi/kyujitai.js) | 📥 24/week | 📦 1.1k | ⭐ 23 | 🔴 august 2020|
| 🔗 [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) | - | - | ⭐ 949 | 🟡 july 2025|
| 🔗 [jaconv](https://github.com/kazuhikoarase/jaconv) | - | - | ⭐ 87 | 🟡 june 2025|
| 🔗 [romaji-conv](https://github.com/koozaki/romaji-conv) | - | - | ⭐ 26 | 🟢 february|
| 🔗 [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) | - | - | ⭐ 71 | 🔴 january 2025|
| 🔗 [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [japanese.js](https://github.com/hakatashi/japanese.js) | - | - | ⭐ 167 | 🔴 august 2020|


### Others
其他与日语NLP相关的JavaScript库

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
 * [closewords](https://github.com/otoneko1102/closewords) - 从单词组中搜索最相似的单词的日语（包括汉字）库
 * [japanese-analyzer](https://github.com/cokice/japanese-analyzer) - 日语句子分析器 (日本語文章解析器)
 * [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) - 规范化日语振假名
 * [yama](https://github.com/sapjax/yama) - 在任何网站上获取日语词汇
 * [kaitai](https://github.com/compile10/kaitai) - 一款利用人工智能分析日语句子结构的应用程序。这个工具可以将单词和短语之间的关系可视化，通过交互式图表展示语法关系。
 * [tsukeru-furigana-converter](https://github.com/ln2058/tsukeru-furigana-converter) - 浏览器扩展（Chrome/Edge/Firefox），可按需将振仮名注入日语网页；包括词典工具提示、JLPT过滤和词汇/Anki导出。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bangumi-data](https://github.com/bangumi-data/bangumi-data) | 📥 993/week | 📦 58k | ⭐ 605 | 🟢 today|
| 🔗 [yomichan](https://github.com/FooSoft/yomichan) | - | - | ⭐ 1.1k | 🔴 february 2023|
| 🔗 [proofreading-tool](https://github.com/gecko655/proofreading-tool) | - | - | ⭐ 87 | 🟡 october 2025|
| 🔗 [kanjigrid](https://github.com/minosvasilias/kanjigrid) | - | - | ⭐ 44 | 🔴 november 2018|
| 🔗 [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) | - | - | ⭐ 64 | 🔴 january 2023|
| 🔗 [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) | 📥 99k/week | 📦 5.1M | ⭐ 18 | 🟢 april|
| 🔗 [hatsuon](https://github.com/DJTB/hatsuon) | 📥 7/week | 📦 922 | ⭐ 38 | 🔴 march 2022|
| 🔗 [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) | - | - | ⭐ 10 | 🔴 december 2021|
| 🔗 [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) | 📥 215/week | 📦 6.3k | ⭐ 8 | 🔴 july 2016|
| 🔗 [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) | 📥 3/week | 📦 264 | ⭐ repo not found | 🔴 repo not found|
| 🔗 [oskim](https://github.com/esrille/oskim) | - | - | ⭐ 2 | 🔴 february 2023|
| 🔗 [tweetMapping](https://github.com/wtnv-lab/tweetMapping) | - | - | ⭐ 26 | 🟢 march|
| 🔗 [pitch-accent](https://github.com/shirakaba/pitch-accent) | 📥 4/week | 📦 117 | ⭐ 2 | 🔴 september 2023|
| 🔗 [kana2ipa](https://github.com/amanoese/kana2ipa) | - | - | ⭐ 17 | 🔴 october 2020|
| 🔗 [voicevox](https://github.com/VOICEVOX/voicevox) | - | - | ⭐ 3.1k | 🟢 today|
| 🔗 [kamiya-codec](https://github.com/fasiha/kamiya-codec) | - | - | ⭐ 22 | 🟡 may 2025|
| 🔗 [closewords](https://github.com/otoneko1102/closewords) | - | - | ⭐ 4 | 🟢 march|
| 🔗 [japanese-analyzer](https://github.com/cokice/japanese-analyzer) | - | - | ⭐ 727 | 🟡 december 2025|
| 🔗 [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) | - | - | ⭐ 6 | 🔴 july 2024|
| 🔗 [yama](https://github.com/sapjax/yama) | - | - | ⭐ 8 | 🟢 february|
| 🔗 [kaitai](https://github.com/compile10/kaitai) | - | - | ⭐ 1 | 🟢 last tuesday|
| 🔗 [tsukeru-furigana-converter](https://github.com/ln2058/tsukeru-furigana-converter) | - | - | ⭐ 1 | 🟢 last wednesday|


## Go

### Morphology analysis
用Go实现的轻量日语形态素分析库

 * [kagome](https://github.com/ikawaha/kagome) - 用纯Go编写的自包含日语形态分析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kagome](https://github.com/ikawaha/kagome) | - | - | ⭐ 961 | 🟢 april|


### Others
其他基于Go的日语文本处理库

 * [ojosama](https://github.com/jiro4989/ojosama) - 将文本转换为百万天原萨洛梅小姐风格的口吻。
 * [nihongo](https://github.com/gojp/nihongo) - 日语词典
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - Yomichan的外部词典导入器。
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - 《偶像大师》日语输入法词典（由imas-db.jp提供）
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - 汉字转换为平假名/片假名/罗马字母，在围棋游戏中
 * [go-moji](https://github.com/ktnyt/go-moji) - 一个用于全角/半角转换的Go库
 * [ojichat](https://github.com/greymd/ojichat) - 生成一个似乎是叔叔通过LINE或邮件发送的句子。
 * [name](https://github.com/kuniwak/name) - 日语姓名搜索器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ojosama](https://github.com/jiro4989/ojosama) | - | - | ⭐ 387 | 🟢 april|
| 🔗 [nihongo](https://github.com/gojp/nihongo) | - | - | ⭐ 83 | 🔴 february 2024|
| 🔗 [yomichan-import](https://github.com/FooSoft/yomichan-import) | - | - | ⭐ 87 | 🔴 february 2023|
| 🔗 [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) | - | - | ⭐ 32 | 🟡 january|
| 🔗 [go-kakasi](https://github.com/sarumaj/go-kakasi) | - | - | ⭐ 6 | 🟢 april|
| 🔗 [go-moji](https://github.com/ktnyt/go-moji) | - | - | ⭐ 20 | 🔴 april 2019|
| 🔗 [ojichat](https://github.com/greymd/ojichat) | - | - | ⭐ 1.3k | 🔴 october 2024|
| 🔗 [name](https://github.com/kuniwak/name) | - | - | ⭐ 11 | 🔴 january 2025|


## Java

### Morphology analysis
用于日语形态素分析和词典管理的库

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji是一个自包含且非常易于使用的日语形态分析器，专为搜索而设计。
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - 一个Sudachi词汇表
 * [meval](https://github.com/teru-oka-1933/meval) - 形态素解析器性能评估系统 MevAL


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji](https://github.com/atilika/kuromoji) | - | - | ⭐ 1k | 🔴 september 2019|
| 🔗 [Sudachi](https://github.com/WorksApplications/Sudachi) | - | - | ⭐ 957 | 🟢 last monday|
| 🔗 [SudachiDict](https://github.com/WorksApplications/SudachiDict) | - | - | ⭐ 289 | 🟡 january|
| 🔗 [meval](https://github.com/teru-oka-1933/meval) | - | - | ⭐ 7 | 🔴 august 2019|


### Others
支持日语NLP与OCR的Java库

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 用于从图像中识别日语字符的Java库
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 将日语汉字转换为罗马字（拉丁字母）的Java库和命令行工具。
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Java中的汉字音译为平假名/片假名/罗马字。
 * [Kamite](https://github.com/fauu/Kamite) - 一款桌面语言沉浸式伴侣，适用于学习日语的学习者。
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - React Native异步日语分词原生插件，适用于iOS和Android。
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本分析器使用ElasticSearch的kuromoji日本分词器。
 * [moji4j](https://github.com/andree-surya/moji4j) - 一个Java库，用于在日语平假名、片假名和罗马字之间进行转换。
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - 针对mecab-neologd的日语文本规范化工具
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - 日本的elasticsearch分析插件


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) | - | - | ⭐ 204 | 🔴 may 2021|
| 🔗 [jakaroma](https://github.com/nicolas-raoul/jakaroma) | - | - | ⭐ 70 | 🟡 june 2025|
| 🔗 [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) | - | - | ⭐ 55 | 🔴 april 2016|
| 🔗 [Kamite](https://github.com/fauu/Kamite) | - | - | ⭐ 134 | 🔴 march 2025|
| 🔗 [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) | - | - | ⭐ 38 | 🔴 june 2023|
| 🔗 [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) | - | - | ⭐ 29 | 🔴 march 2012|
| 🔗 [moji4j](https://github.com/andree-surya/moji4j) | - | - | ⭐ 33 | 🔴 june 2022|
| 🔗 [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) | - | - | ⭐ 5 | 🟢 february|
| 🔗 [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) | - | - | ⭐ 220 | 🟢 april|


## Pretrained model

### Word2Vec
将词语转换为向量以学习语义关系的模型

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - 使用Gensim和Mecab的Word2vec（单词到向量）方法来处理日语。
 * [chiVe](https://github.com/WorksApplications/chiVe) - 使用Sudachi和NWJC的日语词嵌入
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - 艾尔莫-日语
 * [embedrank](https://github.com/yagays/embedrank) - EmbedRank的Python实现
 * [aovec](https://github.com/eggplants/aovec) - 易用的青空文库Word2Vec构建器 - 包含所有书籍的Word2Vec构建器和预先构建的模型。
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - 这是AI LAB文章“係り受けに基づく日本語単語埋込（基于依存关系的日语词嵌入）”的存储库（文章网址https://ai-lab.lapras.com/nlp/japanese-word-embedding/）。
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - 又一个日语维基百科实体向量
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 使用最新的日本语Wikipedia转储数据，使用MeCab在IPA词典和最新的Neologd词典中进行形态分析，并基于其结果学习word2vec、fastText和GloVe的词向量表示的脚本。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) | - | - | ⭐ 87 | 🔴 august 2020|
| 🔗 [chiVe](https://github.com/WorksApplications/chiVe) | - | - | ⭐ 173 | 🔴 march 2024|
| 🔗 [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) | - | - | ⭐ 4 | 🔴 october 2019|
| 🔗 [embedrank](https://github.com/yagays/embedrank) | - | - | ⭐ 47 | 🔴 march 2019|
| 🔗 [aovec](https://github.com/eggplants/aovec) | 📥 80 | 📦 83k | ⭐ 3 | 🔴 january 2023|
| 🔗 [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) | - | - | ⭐ 8 | 🔴 august 2019|
| 🔗 [jawikivec](https://github.com/wikiwikification/jawikivec) | - | - | ⭐ 2 | 🔴 november 2018|
| 🔗 [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) | - | - | ⭐ 11 | 🔴 may 2020|


### Transformer based models
使用自注意机制理解上下文并执行高级语言任务的模型

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


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bert-japanese](https://github.com/cl-tohoku/bert-japanese) | - | - | ⭐ 544 | 🔴 march 2024|
| 🔗 [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [bert-japanese](https://github.com/yoheikikuta/bert-japanese) | - | - | ⭐ 498 | 🔴 february 2021|
| 🔗 [SudachiTra](https://github.com/WorksApplications/SudachiTra) | 📥 698 | 📦 166k | ⭐ 79 | 🔴 december 2023|
| 🔗 [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) | - | - | ⭐ 245 | 🔴 june 2023|
| 🔗 [shiba](https://github.com/octanove/shiba) | 📥 16 | 📦 7k | ⭐ 89 | 🔴 november 2023|
| 🔗 [Dialog](https://github.com/reppy4620/Dialog) | - | - | ⭐ 72 | 🔴 october 2020|
| 🔗 [language-pretraining](https://github.com/retarfi/language-pretraining) | - | - | ⭐ 50 | 🔴 may 2023|
| 🔗 [medbertjp](https://github.com/ou-medinfo/medbertjp) | - | - | ⭐ 13 | 🔴 november 2020|
| 🔗 [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) | - | - | ⭐ 23 | 🔴 october 2021|
| 🔗 [t5-japanese](https://github.com/megagonlabs/t5-japanese) | - | - | ⭐ 40 | 🔴 september 2021|
| 🔗 [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) | - | - | ⭐ 35 | 🔴 june 2019|
| 🔗 [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) | - | - | ⭐ 73 | 🔴 may 2022|
| 🔗 [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) | - | - | ⭐ 23 | 🔴 november 2021|
| 🔗 [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) | - | - | ⭐ 16 | 🔴 may 2022|
| 🔗 [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) | - | - | ⭐ 40 | 🔴 august 2020|
| 🔗 [sbert-ja](https://github.com/colorfulscoop/sbert-ja) | - | - | ⭐ 11 | 🔴 august 2021|
| 🔗 [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) | - | - | ⭐ 7 | 🔴 may 2022|
| 🔗 [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) | - | - | ⭐ 324 | 🔴 september 2023|
| 🔗 [text2text-japanese](https://github.com/tanreinama/text2text-japanese) | - | - | ⭐ 33 | 🔴 july 2021|
| 🔗 [gpt-ja](https://github.com/colorfulscoop/gpt-ja) | - | - | ⭐ 3 | 🔴 september 2021|
| 🔗 [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) | - | - | ⭐ 1 | 🔴 may 2022|
| 🔗 [albert-japanese](https://github.com/alinear-corp/albert-japanese) | - | - | ⭐ 33 | 🔴 october 2021|
| 🔗 [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) | - | - | ⭐ 115 | 🔴 november 2018|
| 🔗 [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) | - | - | ⭐ 161 | 🔴 april 2020|
| 🔗 [bert](https://github.com/informatix-inc/bert) | - | - | ⭐ 28 | 🔴 april 2022|
| 🔗 [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) | - | - | ⭐ 16 | 🔴 december 2020|
| 🔗 [luke](https://github.com/studio-ousia/luke) | - | - | ⭐ 727 | 🔴 june 2023|
| 🔗 [GPTSAN](https://github.com/tanreinama/GPTSAN) | - | - | ⭐ 118 | 🔴 september 2023|
| 🔗 [japanese-clip](https://github.com/rinnakk/japanese-clip) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [AcademicBART](https://github.com/EhimeNLP/AcademicBART) | - | - | ⭐ 2 | 🔴 july 2024|
| 🔗 [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) | - | - | ⭐ 9 | 🔴 september 2024|
| 🔗 [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) | - | - | ⭐ 46 | 🔴 march 2023|
| 🔗 [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) | - | - | ⭐ 141 | 🔴 april 2023|
| 🔗 [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) | - | - | ⭐ invalid | 🔴 september 2023|
| 🔗 [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) | - | - | ⭐ 54 | 🟡 december 2025|
| 🔗 [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) | - | - | ⭐ 44 | 🔴 april 2024|


## ChatGPT
使用ChatGPT和API进行日语对话与文本生成的资源

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
 * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - ChatGPT和Copilot等各种生成AI用的“日本语”提示的示例ChatGPT和Copilot等各种生成AI用的“日本语”提示的示例


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) | - | - | ⭐ 15 | 🔴 march 2023|
| 🔗 [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) | - | - | ⭐ 5 | 🔴 march 2023|
| 🔗 [wanna](https://github.com/hirokidaichi/wanna) | 📥 48 | 📦 20k | ⭐ 142 | 🔴 april 2023|
| 🔗 [ChatdollKit](https://github.com/uezo/ChatdollKit) | - | - | ⭐ 1.1k | 🟢 march|
| 🔗 [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) | - | - | ⭐ 1 | 🔴 march 2023|
| 🔗 [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) | - | - | ⭐ 26 | 🔴 may 2023|
| 🔗 [vrchatbot](https://github.com/Geson-anko/vrchatbot) | - | - | ⭐ 29 | 🔴 december 2022|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) | - | - | ⭐ 16 | 🔴 april 2023|
| 🔗 [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) | - | - | ⭐ 1 | 🔴 april 2023|
| 🔗 [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) | - | - | ⭐ 46 | 🔴 december 2023|
| 🔗 [chatvrm](https://github.com/pixiv/chatvrm) | - | - | ⭐ 837 | 🟡 may 2025|
| 🔗 [sftly-replace](https://github.com/kmizu/sftly-replace) | - | - | ⭐ 4 | 🔴 may 2023|
| 🔗 [summarize_arxv](https://github.com/rkmt/summarize_arxv) | - | - | ⭐ 173 | 🔴 may 2023|
| 🔗 [aiavatarkit](https://github.com/uezo/aiavatarkit) | - | - | ⭐ 582 | 🟢 yesterday|
| 🔗 [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) | - | - | ⭐ 280 | 🟢 march|
| 🔗 [character_chat](https://github.com/mutaguchi/character_chat) | - | - | ⭐ 16 | 🔴 june 2023|
| 🔗 [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) | - | - | ⭐ 64 | 🔴 july 2024|
| 🔗 [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) | - | - | ⭐ 428 | 🟢 last tuesday|
| 🔗 [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) | - | - | ⭐ 6 | 🔴 october 2023|
| 🔗 [IgakuQA](https://github.com/jungokasai/IgakuQA) | - | - | ⭐ 49 | 🔴 march 2023|
| 🔗 [japagen](https://github.com/retrieva/japagen) | - | - | ⭐ 1 | 🔴 october 2024|
| 🔗 [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) | - | - | ⭐ 428 | 🟢 last tuesday|


## Dictionary and IME
与日语词典和输入法相关的资源

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
 * [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) - 由azooKey引擎驱动的fcitx5日语输入法由azooKey引擎驱动的fcitx5日语输入法
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
 * [jisho-open](https://github.com/hlorenzi/jisho-open) - JMdict日语-英语词典项目的Web前端，支持学习列表！JMdict日语-英语词典项目的Web前端，支持学习列表！
 * [macskk](https://github.com/mtgto/macskk) - 另一个 macOS SKK 输入法
 * [nandoku](https://github.com/marmooo/nandoku) - 这是一个按年级整理的难读汉字词典。
 * [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) - 一个用于安卓系统的开源日文输入法。
 * [anthywl](https://github.com/tadeokondrak/anthywl) - 使用libanthy为Sway提供的日语输入法
 * [sekka](https://github.com/kiyoka/sekka) - 受SKK启发的又一个日本输入法。
 * [sumibi](https://github.com/kiyoka/sumibi) - 由ChatGPT API提供支持的日语输入法
 * [jinmei-dict](https://github.com/s1r-j/jinmei-dict) - 从词典数据中提取出人名，以读音假名（片假名）作为键，将候选的写字形式整理成列表，并以JSON格式保存。
 * [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) - 紫罗兰 完全离线的日语键盘应用程序
 * [japanesearabic](https://github.com/a-hamdi/japanesearabic) - 日语阿拉伯语词典（日本語・アラビア語辞書）约米坦
 * [o-dic](https://github.com/makotoga/o-dic) - 冲绳字典
 * [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) - SKK表情符号词典
 * [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) - 一个适用于Mozc的个人姓名字典。
 * [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) - 一个从SudachiDict转换为Mozc的字典。
 * [nihongo](https://github.com/sph-mn/nihongo) - 日语语言数据和词典
 * [kagome-dict](https://github.com/ikawaha/kagome-dict) - Kagome v2 的字典库
 * [canna](https://github.com/canna-input/canna) - 卡纳日本输入系统
 * [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) - 京阪式口音（关西方言）词典 - 收录了4,615个日本方言口音词汇。
 * [jitendex](https://github.com/jitendex/jitendex) - 一个免费、离线和开放许可的日语到英语词典。每月更新！
 * [karukan](https://github.com/togatoga/karukan) - Linux的日语输入法系统，神经假名汉字转换引擎+fcitx5输入法。
 * [shitto-mania-dic](https://github.com/junikematsu/shitto-mania-dic) - 嫉妒词典（Shitto-Mania / Jealousy Dictionary）
 * [dvorakjp-roman-table](https://github.com/shinespark/dvorakjp-roman-table) - azooKey，适用于Google日语输入的DvorakJP罗马字表/DvorakJP Roman Table for azooKey，Google日语输入


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) | - | - | ⭐ 2.8k | 🔴 september 2020|
| 🔗 [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) | - | - | ⭐ 125 | 🔴 march 2024|
| 🔗 [jamdict](https://github.com/neocl/jamdict) | 📥 335 | 📦 54k | ⭐ 168 | 🔴 june 2021|
| 🔗 [unidic-py](https://github.com/polm/unidic-py) | 📥 74k | 📦 10M | ⭐ 108 | 🔴 february 2025|
| 🔗 [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) | - | - | ⭐ 100 | 🔴 january 2023|
| 🔗 [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) | - | - | ⭐ 7 | 🔴 april 2021|
| 🔗 [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) | - | - | ⭐ 62 | 🟢 today|
| 🔗 [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) | - | - | ⭐ 40 | 🔴 january 2021|
| 🔗 [JumanDIC](https://github.com/ku-nlp/JumanDIC) | - | - | ⭐ 4 | 🔴 august 2022|
| 🔗 [ipadic-py](https://github.com/polm/ipadic-py) | 📥 24k | 📦 7M | ⭐ 24 | 🔴 october 2021|
| 🔗 [unidic-lite](https://github.com/polm/unidic-lite) | 📥 71k | 📦 10M | ⭐ 49 | 🔴 september 2020|
| 🔗 [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) | - | - | ⭐ 368 | 🔴 january 2023|
| 🔗 [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) | - | - | ⭐ 105 | 🔴 january 2023|
| 🔗 [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) | - | - | ⭐ 83 | 🔴 september 2024|
| 🔗 [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) | - | - | ⭐ 58 | 🔴 december 2016|
| 🔗 [emoticon](https://github.com/tiwanari/emoticon) | - | - | ⭐ 44 | 🔴 may 2020|
| 🔗 [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) | - | - | ⭐ 10 | 🔴 january 2018|
| 🔗 [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) | - | - | ⭐ 2 | 🔴 november 2022|
| 🔗 [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) | - | - | ⭐ 38 | 🟢 today|
| 🔗 [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) | - | - | ⭐ 0 | 🔴 january 2020|
| 🔗 [EJDict](https://github.com/kujirahand/EJDict) | - | - | ⭐ 255 | 🟢 april|
| 🔗 [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) | - | - | ⭐ 26 | 🔴 may 2024|
| 🔗 [genshin-dict](https://github.com/kotofurumiya/genshin-dict) | - | - | ⭐ 126 | 🟢 february|
| 🔗 [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) | - | - | ⭐ 352 | 🟢 last monday|
| 🔗 [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) | - | - | ⭐ 69 | 🟡 september 2025|
| 🔗 [mh-dict-jp](https://github.com/utubo/mh-dict-jp) | - | - | ⭐ 5 | 🔴 april 2025|
| 🔗 [jitenbot](https://github.com/stephenmk/jitenbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) | - | - | ⭐ 87 | 🔴 september 2020|
| 🔗 [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) | - | - | ⭐ 24 | 🔴 december 2024|
| 🔗 [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) | - | - | ⭐ 265 | 🟢 february|
| 🔗 [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) | - | - | ⭐ 127 | 🟡 august 2025|
| 🔗 [Jitendex](https://github.com/stephenmk/Jitendex) | - | - | ⭐ 471 | 🟢 yesterday|
| 🔗 [jiten](https://github.com/obfusk/jiten) | - | - | ⭐ 130 | 🔴 december 2023|
| 🔗 [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) | - | - | ⭐ 56 | 🟢 march|
| 🔗 [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) | - | - | ⭐ 4 | 🟢 march|
| 🔗 [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) | - | - | ⭐ 772 | 🟢 march|
| 🔗 [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) | - | - | ⭐ 72 | 🔴 january 2020|
| 🔗 [jisyo](https://github.com/skk-dict/jisyo) | - | - | ⭐ 28 | 🔴 september 2023|
| 🔗 [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) | - | - | ⭐ 30 | 🔴 march 2018|
| 🔗 [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) | - | - | ⭐ 7 | 🔴 november 2019|
| 🔗 [cl-skkserv](https://github.com/tani/cl-skkserv) | - | - | ⭐ 31 | 🔴 october 2024|
| 🔗 [anthy](https://github.com/xorgy/anthy) | - | - | ⭐ 3 | 🔴 july 2013|
| 🔗 [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) | - | - | ⭐ 43 | 🟢 march|
| 🔗 [azooKey](https://github.com/ensan-hcl/azooKey) | - | - | ⭐ 691 | 🟢 april|
| 🔗 [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) | - | - | ⭐ 891 | 🟢 yesterday|
| 🔗 [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) | - | - | ⭐ 186 | 🟢 february|
| 🔗 [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) | - | - | ⭐ invalid | 🟢 april|
| 🔗 [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) | - | - | ⭐ invalid | 🟢 april|
| 🔗 [libkkc](https://github.com/ueno/libkkc) | - | - | ⭐ invalid | 🔴 august 2024|
| 🔗 [libskk](https://github.com/ueno/libskk) | - | - | ⭐ 100 | 🟢 last friday|
| 🔗 [kanayomi-dict](https://github.com/warihima/kanayomi-dict) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) | - | - | ⭐ 110 | 🔴 september 2017|
| 🔗 [wlsp-classical](https://github.com/yocjyet/wlsp-classical) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [kanji-dict](https://github.com/marmooo/kanji-dict) | - | - | ⭐ 6 | 🟢 march|
| 🔗 [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) | - | - | ⭐ 12 | 🟡 october 2025|
| 🔗 [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) | - | - | ⭐ 6 | 🟢 april|
| 🔗 [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) | - | - | ⭐ 7 | 🟢 last monday|
| 🔗 [ichiran](https://github.com/tshatrov/ichiran) | - | - | ⭐ 391 | 🟡 january|
| 🔗 [mikan](https://github.com/mojyack/mikan) | - | - | ⭐ 24 | 🟡 june 2025|
| 🔗 [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) | - | - | ⭐ 9 | 🟢 yesterday|
| 🔗 [jisho-open](https://github.com/hlorenzi/jisho-open) | - | - | ⭐ 58 | 🟢 february|
| 🔗 [macskk](https://github.com/mtgto/macskk) | - | - | ⭐ 291 | 🟢 april|
| 🔗 [nandoku](https://github.com/marmooo/nandoku) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [anthywl](https://github.com/tadeokondrak/anthywl) | - | - | ⭐ 34 | 🔴 april 2025|
| 🔗 [sekka](https://github.com/kiyoka/sekka) | - | - | ⭐ 23 | 🟢 yesterday|
| 🔗 [sumibi](https://github.com/kiyoka/sumibi) | - | - | ⭐ 45 | 🟢 yesterday|
| 🔗 [jinmei-dict](https://github.com/s1r-j/jinmei-dict) | - | - | ⭐ 7 | 🔴 april 2020|
| 🔗 [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) | - | - | ⭐ 241 | 🟢 yesterday|
| 🔗 [japanesearabic](https://github.com/a-hamdi/japanesearabic) | - | - | ⭐ 19 | 🟡 may 2025|
| 🔗 [o-dic](https://github.com/makotoga/o-dic) | - | - | ⭐ 6 | 🟢 february|
| 🔗 [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) | - | - | ⭐ 140 | 🔴 january 2025|
| 🔗 [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) | - | - | ⭐ 26 | 🟢 april|
| 🔗 [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) | - | - | ⭐ 22 | 🟢 february|
| 🔗 [nihongo](https://github.com/sph-mn/nihongo) | - | - | ⭐ 20 | 🔴 january 2025|
| 🔗 [kagome-dict](https://github.com/ikawaha/kagome-dict) | - | - | ⭐ 15 | 🟢 april|
| 🔗 [canna](https://github.com/canna-input/canna) | - | - | ⭐ 4 | 🟡 august 2025|
| 🔗 [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) | - | - | ⭐ 1 | 🟡 december 2025|
| 🔗 [jitendex](https://github.com/jitendex/jitendex) | - | - | ⭐ 471 | 🟢 yesterday|
| 🔗 [karukan](https://github.com/togatoga/karukan) | - | - | ⭐ 271 | 🟢 february|
| 🔗 [shitto-mania-dic](https://github.com/junikematsu/shitto-mania-dic) | - | - | ⭐ 0 | 🟢 march|
| 🔗 [dvorakjp-roman-table](https://github.com/shinespark/dvorakjp-roman-table) | - | - | ⭐ 56 | 🟢 february|


## Corpus

### Part-of-speech tagging / Named entity recognition
带有词性和命名实体标注的日语语料库

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - 使用维基百科进行日语专有名词提取的数据集
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 用于命名实体识别的日语IOB2标记语料库。
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本语 Twitter 语料库
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - 并行通用依存关系。
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - 谷歌UDT 2.0的日本数据。
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大学网页文档引导语料库
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 注释版富满开拓中心语料库
 * [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) - UD_Japanese-GSD的长单元词版本
 * [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) - 这个Universal Dependencies (UD)日语树库是基于UD文档中描述的UD日语规范的定义。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) | - | - | ⭐ 142 | 🔴 september 2023|
| 🔗 [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) | - | - | ⭐ 61 | 🔴 february 2020|
| 🔗 [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) | - | - | ⭐ 21 | 🔴 march 2016|
| 🔗 [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) | - | - | ⭐ 0 | 🔴 may 2020|
| 🔗 [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) | - | - | ⭐ 28 | 🔴 may 2022|
| 🔗 [KWDLC](https://github.com/ku-nlp/KWDLC) | - | - | ⭐ 84 | 🔴 december 2023|
| 🔗 [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) | - | - | ⭐ 18 | 🔴 december 2023|
| 🔗 [anthy](https://github.com/netsphere-labs/anthy) | - | - | ⭐ 16 | 🔴 february 2023|
| 🔗 [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) | - | - | ⭐ 3 | 🟡 november 2025|
| 🔗 [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) | - | - | ⭐ 27 | 🟡 november 2025|


### Parallel corpus
包含对齐句子的多语平行语料库

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
 * [matcha](https://github.com/ehimenlp/matcha) - 从日本旅游网站MATCHA的文章中，我们构建了一个用于简化日语文本的数据集。
 * [en-ja-el](https://github.com/shigashiyama/en-ja-el) - EnJaEL：En-Ja平行实体链接数据集（版本1.0）EnJaEL：En-Ja平行实体链接数据集（版本1.0）


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [small_parallel_enja](https://github.com/odashi/small_parallel_enja) | - | - | ⭐ 98 | 🔴 september 2019|
| 🔗 [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) | - | - | ⭐ 15 | 🔴 september 2023|
| 🔗 [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) | - | - | ⭐ 15 | 🔴 august 2024|
| 🔗 [JESC](https://github.com/rpryzant/JESC) | - | - | ⭐ 89 | 🔴 november 2017|
| 🔗 [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) | - | - | ⭐ 11 | 🔴 december 2020|
| 🔗 [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) | - | - | ⭐ 5 | 🔴 august 2019|
| 🔗 [jesc_small](https://github.com/yusugomori/jesc_small) | - | - | ⭐ 3 | 🔴 july 2019|
| 🔗 [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) | - | - | ⭐ 6 | 🟡 august 2025|
| 🔗 [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) | - | - | ⭐ 150 | 🟢 february|
| 🔗 [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) | - | - | ⭐ 18 | 🔴 november 2021|
| 🔗 [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) | - | - | ⭐ 4 | 🔴 march 2020|
| 🔗 [matcha](https://github.com/ehimenlp/matcha) | - | - | ⭐ 6 | 🔴 january 2025|
| 🔗 [en-ja-el](https://github.com/shigashiyama/en-ja-el) | - | - | ⭐ 2 | 🔴 january 2025|


### Dialog corpus
用于训练对话系统的会话语料集

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本电影推荐对话数据集
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - 使用爬虫程序从2ch论坛抓取并创建的对话语料库
 * [BSD](https://github.com/tsuruoka-lab/BSD) - 商业场景对话语料库
 * [asdc](https://github.com/megagonlabs/asdc) - 住宿搜索对话语料库
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - 用于seq2seq等的日语对话数据
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - 这个仓库包含了日英双语聊天语料库BPersona-chat，该语料库已发表在AACL-IJCNLP 2022的Eval4NLP 2022研讨会上的论文《聊天翻译错误检测以协助跨语言交流》中。
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 日本日常对话语料库，或日本语日常対話コーパス，是一个高质量的多轮对话数据集，包含五个主题的日常对话：日常生活，学校，旅行，健康和娱乐。
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - LLM构建用的日语聊天数据集
 * [kokorochat](https://github.com/uec-inabalab/kokorochat) - 通过角色扮演收集的日语咨询对话数据集
 * [JMultiWOZ-TC](https://github.com/llm-jp/JMultiWOZ-TC) - 在多轮对话中评估代理的function calling
 * [HOTATE](https://github.com/EhimeNLP/HOTATE) - 本音・建前付き日本語对话数据集
 * [ETCDataset](https://github.com/UEC-InabaLab/ETCDataset) - 情绪转录对话数据集包含了约1,000个对话，每个对话中包含了对话参与者自己描述的情绪文本。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JMRD](https://github.com/ku-nlp/JMRD) | - | - | ⭐ 29 | 🔴 july 2022|
| 🔗 [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) | - | - | ⭐ 99 | 🔴 june 2021|
| 🔗 [BSD](https://github.com/tsuruoka-lab/BSD) | - | - | ⭐ 73 | 🔴 november 2021|
| 🔗 [asdc](https://github.com/megagonlabs/asdc) | - | - | ⭐ 25 | 🔴 august 2023|
| 🔗 [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) | - | - | ⭐ 3 | 🔴 october 2018|
| 🔗 [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) | - | - | ⭐ 5 | 🔴 january 2023|
| 🔗 [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) | - | - | ⭐ 56 | 🔴 march 2023|
| 🔗 [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) | - | - | ⭐ 88 | 🔴 january 2024|
| 🔗 [kokorochat](https://github.com/uec-inabalab/kokorochat) | - | - | ⭐ 20 | 🟡 august 2025|
| 🔗 [JMultiWOZ-TC](https://github.com/llm-jp/JMultiWOZ-TC) | - | - | ⭐ 0 | 🟢 march|
| 🔗 [HOTATE](https://github.com/EhimeNLP/HOTATE) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [ETCDataset](https://github.com/UEC-InabaLab/ETCDataset) | - | - | ⭐ 12 | 🟡 january|

### Others
用于问答或语义推理等任务的日语数据集

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
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - COMET-ATOMIC jaCOMET-ATOMIC ja
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
 * [lawtext](https://github.com/yamachig/lawtext) - 日本法律的纯文本格式简体中文
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
 * [kanji-data](https://github.com/mimneko/kanji-data) - 常用汉字表，有关汉字的数据
 * [openchj-genji](https://github.com/togiso/openchj-genji) - 《源氏物语》形态论情报数据
 * [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) - 这个存储库包含了我们论文《AdParaphrase: 用于分析语言特征以生成吸引人广告文本的改写数据集》的数据。
 * [Jamp_sp](https://github.com/ynklab/Jamp_sp) - 考虑了方面的日语时间推理数据集的构建（Jamp_sp：考虑方面的受控日语时间推理数据集）
 * [jnli-neg](https://github.com/asahi-y/jnli-neg) - 这是用于评估否定理解能力的日语语言推理数据集JNLI-Neg的公开存储库。
 * [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) - 该存储库提供了用于构建燕子语料库第1版的Python实现，这是一个大型的日语网络语料库（冈崎等人，2024年），来自Common Crawl档案。
 * [jalecon](https://github.com/naist-nlp/jalecon) - 一个供非母语读者使用的日语词汇复杂性数据集
 * [multils-japanese](https://github.com/naist-nlp/multils-japanese) - MultiLS-日语词汇复杂度预测和日语词汇简化数据集：注释者简介，未聚合注释和注释指南。
 * [nwjc](https://github.com/masayu-a/nwjc) - NINJAL网络日语语料库
 * [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) - 在AAAI21年会上介绍的《全自动漫画翻译》论文中介绍的数据集在AAAI21年会上介绍的《全自动漫画翻译》论文中介绍的数据集
 * [public-annotations](https://github.com/manga109/public-annotations) - Manga109数据集的各种注释
 * [gimei](https://github.com/willnet/gimei) - 随机日本姓名和地址生成器
 * [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) - 评估日语语言模型安全性行为的测试集
 * [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) - 一个简单的、开源的日语拟声词和拟态词的收集，以JSON格式呈现。附带漫画示例。
 * [kanji](https://github.com/sylhare/kanji) - 要学习的日本汉字部首列表
 * [jethics](https://github.com/language-media-lab/jethics) - 日本语道德理解度评价用数据集JETHICS的概述页面（待更新）
 * [waon](https://github.com/llm-jp/waon) - WAON：用于视觉语言模型的大规模高质量日本图像文本数据集
 * [kuci](https://github.com/ku-nlp/kuci) - 京都大学常识推理数据集（KUCI）
 * [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) - 日本地址解析困难的测试数据集
 * [jlpt-word-list](https://github.com/elzup/jlpt-word-list) - JLPT词汇表中的日语单词列表
 * [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) - 文字图像数据集（平假名73个字符版）
 * [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) - 日本法律相关的多项选择问答数据集
 * [yjcaptions](https://github.com/yahoojapan/yjcaptions) - YJ字幕26k数据集
 * [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) - 日本视觉基因问答数据集
 * [lawhub](https://github.com/lwhb/lawhub) - 用文本格式跟踪日本法律的存储库
 * [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) - 从日本戏剧、动漫和电影字幕中提取的词频列表。
 * [jconj](https://github.com/yamagoya/jconj) - 一个基于表格的日语词汇变位器
 * [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) - 提取维基百科日语中的个人姓名。
 * [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) - 基于日常日语会话语料库的yomichan频率词典
 * [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) - 维基百科双语参考数据（日语）
 * [ajimee-bench](https://github.com/azookey/ajimee-bench) - AJIMEE-Bench（高级日语输入法评估基准）
 * [j-spaw](https://github.com/takamichi-lab/j-spaw) - J-SpAW：用于说话人验证和防欺骗的日语语音语料库
 * [camera3](https://github.com/cyberagentailab/camera3) - CAMERA3：一个用于可控广告文本生成的日语评估数据集
 * [jgpqa](https://github.com/llm-jp/jgpqa) - GPQA数据集的日语翻译
 * [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) - 正在去除田中语料库中的噪音。
 * [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) - 日本情感语料库德岛大学A-2实验室。
 * [osworld-jp](https://github.com/karakuri-ai/osworld-jp) - 用于考虑语言的评估的日语版计算机性能基准测试
 * [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) - 准日本评论 (擬似评论数据)
 * [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) - 精神科初诊病历创建调查数据集
 * [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) - 市镇村合并等导致消失的旧地名和新地名对照表
 * [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) - 日本文本表情数据。
 * [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) - 听错语料库︱CSV＋表模式 管理约1万条数据，使用VS Code＋pre-commit＋Frictionless＋GitHub Actions进行自动验证的日语数据集
 * [kotowaza](https://github.com/septn/kotowaza) - 包含日语谚语（kotowaza）的结构化JSON数据集，其中包括印尼语和英语的含义、例子、JLPT级别和标签。包含日语谚语（kotowaza）的结构化JSON数据集，其中包括印尼语和英语的含义、例子、JLPT级别和标签。
 * [selective-rag-kasensabo](https://github.com/tk-yasuno/selective-rag-kasensabo) - 该实用的Agentic RAG系统的MVP能够以96%的准确率自动判定建设技术标准相关问题的专业性粒度（细/粗），并选择最佳的RAG系统（ColBERT/Naive）。针对2025年11月公布的河川防砂坝技术标准，构建了四种不同的RAG系统，并对200个不同专业性粒度的问题进行了精度和速度比较。
 * [jmle2026-bench](https://github.com/naoto-iwase/jmle2026-bench) - 2026年2月7日至8日第120届日本医师执照考试上的LLM基准
 * [JSTS-Neg](https://github.com/reiko-y/JSTS-Neg) - 这是用于评估否定理解能力的日语意义相似度计算数据集JSTS-Neg的公开存储库。JSTS-Neg是通过扩展包含在JGLUE中的语言推理数据集JSTS而创建的。
 * [business-slide-questions](https://github.com/stockmarkteam/business-slide-questions) - 在这个存储库中，我们提供了针对商业资料（幻灯片）的视觉问答（VQA）基准测试“BusinessSlideVQA”。
 * [WLSP-antonym](https://github.com/masayu-a/WLSP-antonym) - 根据语义原则的词汇列表（WLSP）的反义词关系
 * [YouCook2-JP](https://github.com/nlab-mpg/YouCook2-JP) - YouCook2数据集的日语翻译。
 * [E2U](https://github.com/sociocom/E2U) - 传达关于变化的数据
 * [annotation-2025](https://github.com/Tiny-Colony/annotation-2025) - 这个存储库是为了公开可以比较人工和LLM输出的文本“解释”的数据。
 * [jhpt](https://github.com/nict-astrec-att/jhpt) - 这是一个将历史日语资料的原文文本和现代语言翻译（参考翻译）文本按段落对应的对照数据集。详细信息请参阅论文。
 * [JBE-QA](https://github.com/hancules/JBE-QA) - 日本司法考试问答
 * [j-spaw](https://github.com/takamichi-lab/j-spaw) - J-SpAW：用于说话人验证和防欺骗的日语语音语料库
 * [JMedWiC](https://github.com/EhimeNLP/JMedWiC) - 通过使用掩码语言模型自动提取伪同义和非同义对，并通过人工同义性标注确定标签，我们构建了日本医疗领域的词义一致性判定数据集。
 * [jhpt](https://github.com/nict-astrec-att/jhpt) - 这是一个将历史日语资料的原文文本和现代语言翻译（参考翻译）文本按段落对应的对照数据集。详细信息请参阅论文。
 * [Doppelganger-JC](https://github.com/0017-alt/Doppelganger-JC) - 这是一个数据集，用于在LLMs中对比中日两种语言之间跨语言同形异义词的误用情况。
 * [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) - 为了软件图理解的VLM评估基准（支持日语、英语、韩语）
 * [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) - 在日本人事劳务领域中，LLM的性能评估基准
 * [nijl-manyoshutei](https://github.com/kokubunken/nijl-manyoshutei) - 在本存储库中，我们以CC-BY许可证发布了关西大学收藏的广濑本万叶集的TEI/XML数据等。
 * [kamuskita](https://github.com/matbahasa/kamuskita) - 在马来语学习会上制作的开放式马来语-日语词典《大家的马来语词典》


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) | - | - | ⭐ 77 | 🔴 june 2023|
| 🔗 [kanji-data](https://github.com/davidluzgouveia/kanji-data) | - | - | ⭐ 218 | 🟢 february|
| 🔗 [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) | - | - | ⭐ 103 | 🔴 december 2021|
| 🔗 [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) | - | - | ⭐ 32 | 🔴 march 2017|
| 🔗 [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) | - | - | ⭐ 140 | 🔴 september 2018|
| 🔗 [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) | - | - | ⭐ 108 | 🔴 january 2022|
| 🔗 [JaNLI](https://github.com/verypluming/JaNLI) | - | - | ⭐ 17 | 🔴 may 2023|
| 🔗 [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) | - | - | ⭐ 18 | 🔴 december 2020|
| 🔗 [emoji-ja](https://github.com/yagays/emoji-ja) | - | - | ⭐ invalid | 🔴 invalid|
| 🔗 [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) | - | - | ⭐ invalid | 🔴 invalid|
| 🔗 [ja.text8](https://github.com/Hironsan/ja.text8) | - | - | ⭐ 111 | 🔴 october 2017|
| 🔗 [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) | - | - | ⭐ 31 | 🔴 april 2018|
| 🔗 [japanese](https://github.com/hingston/japanese) | - | - | ⭐ 87 | 🔴 september 2018|
| 🔗 [kanji-frequency](https://github.com/scriptin/kanji-frequency) | - | - | ⭐ 157 | 🟢 march|
| 🔗 [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) | - | - | ⭐ 24 | 🔴 january 2021|
| 🔗 [CoARiJ](https://github.com/chakki-works/CoARiJ) | - | - | ⭐ 94 | 🔴 december 2020|
| 🔗 [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) | - | - | ⭐ 26 | 🟢 april|
| 🔗 [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) | - | - | ⭐ 5 | 🔴 august 2021|
| 🔗 [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) | - | - | ⭐ 78 | 🔴 april 2024|
| 🔗 [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) | - | - | ⭐ 203 | 🔴 december 2021|
| 🔗 [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) | - | - | ⭐ 107 | 🟢 today|
| 🔗 [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) | - | - | ⭐ 178 | 🟢 today|
| 🔗 [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) | - | - | ⭐ 90 | 🔴 july 2018|
| 🔗 [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) | - | - | ⭐ 6 | 🔴 january 2019|
| 🔗 [speechBSD](https://github.com/ku-nlp/speechBSD) | - | - | ⭐ 3 | 🔴 february 2024|
| 🔗 [ita-corpus](https://github.com/mmorise/ita-corpus) | - | - | ⭐ 231 | 🟢 march|
| 🔗 [rohan4600](https://github.com/mmorise/rohan4600) | - | - | ⭐ 70 | 🟢 march|
| 🔗 [anlp-jp-history](https://github.com/whym/anlp-jp-history) | - | - | ⭐ 3 | 🔴 april 2024|
| 🔗 [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) | - | - | ⭐ 21 | 🔴 november 2022|
| 🔗 [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) | - | - | ⭐ 19 | 🔴 january 2021|
| 🔗 [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) | - | - | ⭐ 4 | 🔴 november 2018|
| 🔗 [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) | - | - | ⭐ 6 | 🔴 january 2020|
| 🔗 [wrime](https://github.com/ids-cv/wrime) | - | - | ⭐ 174 | 🟡 september 2025|
| 🔗 [jtubespeech](https://github.com/sarulab-speech/jtubespeech) | - | - | ⭐ 230 | 🔴 march 2023|
| 🔗 [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) | - | - | ⭐ 2 | 🔴 april 2022|
| 🔗 [kokkosho_data](https://github.com/rindybell/kokkosho_data) | - | - | ⭐ 1 | 🔴 july 2019|
| 🔗 [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) | - | - | ⭐ 83 | 🔴 june 2024|
| 🔗 [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) | - | - | ⭐ 31 | 🔴 september 2021|
| 🔗 [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) | - | - | ⭐ 31 | 🔴 february 2021|
| 🔗 [hirakanadic](https://github.com/po3rin/hirakanadic) | 📥 35 | 📦 14k | ⭐ 7 | 🔴 july 2023|
| 🔗 [animedb](https://github.com/anilogia/animedb) | - | - | ⭐ 330 | 🔴 january 2023|
| 🔗 [security_words](https://github.com/SaitoLab/security_words) | - | - | ⭐ 27 | 🔴 august 2023|
| 🔗 [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [honkoku-data](https://github.com/yuta1984/honkoku-data) | - | - | ⭐ 19 | 🟢 april|
| 🔗 [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) | - | - | ⭐ 35 | 🔴 december 2020|
| 🔗 [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) | - | - | ⭐ 1.9k | 🔴 november 2020|
| 🔗 [JSICK](https://github.com/verypluming/JSICK) | - | - | ⭐ 46 | 🔴 may 2023|
| 🔗 [phishurl-list](https://github.com/JPCERTCC/phishurl-list) | - | - | ⭐ 205 | 🟢 march|
| 🔗 [jcms](https://github.com/shigashiyama/jcms) | - | - | ⭐ 9 | 🟢 april|
| 🔗 [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) | - | - | ⭐ 91 | 🔴 march 2023|
| 🔗 [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [topokanji](https://github.com/scriptin/topokanji) | - | - | ⭐ 202 | 🔴 january 2016|
| 🔗 [isbn4groups](https://github.com/uribo/isbn4groups) | - | - | ⭐ 1 | 🔴 june 2024|
| 🔗 [NMeCab](https://github.com/komutan/NMeCab) | - | - | ⭐ 100 | 🔴 march 2024|
| 🔗 [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) | - | - | ⭐ 15 | 🔴 january 2023|
| 🔗 [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) | - | - | ⭐ 3 | 🔴 july 2023|
| 🔗 [data_set](https://github.com/japanese-law-analysis/data_set) | - | - | ⭐ 52 | 🔴 january 2025|
| 🔗 [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) | - | - | ⭐ 4 | 🔴 january 2023|
| 🔗 [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) | - | - | ⭐ 20 | 🟢 march|
| 🔗 [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) | - | - | ⭐ 181 | 🟡 december 2025|
| 🔗 [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) | - | - | ⭐ 3 | 🔴 october 2023|
| 🔗 [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) | - | - | ⭐ 12 | 🔴 march 2025|
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 | 🟡 november 2025|
| 🔗 [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) | - | - | ⭐ 31 | 🔴 march 2024|
| 🔗 [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) | - | - | ⭐ 6 | 🔴 march 2023|
| 🔗 [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) | - | - | ⭐ 21 | 🔴 january 2023|
| 🔗 [camera](https://github.com/CyberAgentAILab/camera) | - | - | ⭐ 26 | 🔴 august 2024|
| 🔗 [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) | - | - | ⭐ 20 | 🔴 may 2021|
| 🔗 [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [copa-japanese](https://github.com/nlp-titech/copa-japanese) | - | - | ⭐ 1 | 🔴 february 2023|
| 🔗 [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) | - | - | ⭐ 12 | 🔴 january 2025|
| 🔗 [ProSub](https://github.com/matbahasa/ProSub) | - | - | ⭐ 5 | 🔴 april 2025|
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 | 🟡 november 2025|
| 🔗 [ramendb](https://github.com/nuko-yokohama/ramendb) | - | - | ⭐ 7 | 🟢 april|
| 🔗 [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) | - | - | ⭐ 3 | 🔴 march 2023|
| 🔗 [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) | - | - | ⭐ 0 | 🔴 march 2021|
| 🔗 [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) | - | - | ⭐ 89 | 🔴 july 2023|
| 🔗 [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) | - | - | ⭐ 0 | 🔴 june 2023|
| 🔗 [meconaudio](https://github.com/elith-co-jp/meconaudio) | - | - | ⭐ 10 | 🔴 october 2023|
| 🔗 [japanese-addresses](https://github.com/geolonia/japanese-addresses) | - | - | ⭐ 761 | 🟡 december 2025|
| 🔗 [aozorasearch](https://github.com/myokoym/aozorasearch) | - | - | ⭐ 22 | 🟢 march|
| 🔗 [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) | - | - | ⭐ 45 | 🔴 october 2023|
| 🔗 [alpaca_ja](https://github.com/shi3z/alpaca_ja) | - | - | ⭐ 86 | 🔴 may 2023|
| 🔗 [instruction_ja](https://github.com/megagonlabs/instruction_ja) | - | - | ⭐ 24 | 🔴 july 2023|
| 🔗 [japanese-family-names](https://github.com/siikamiika/japanese-family-names) | - | - | ⭐ 18 | 🔴 june 2017|
| 🔗 [kanji-data-media](https://github.com/kanjialive/kanji-data-media) | - | - | ⭐ 411 | 🔴 november 2023|
| 🔗 [reazonspeech](https://github.com/reazon-research/reazonspeech) | - | - | ⭐ 381 | 🟢 april|
| 🔗 [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) | - | - | ⭐ 22 | 🔴 january 2024|
| 🔗 [koniwa](https://github.com/koniwa/koniwa) | - | - | ⭐ 60 | 🔴 april 2025|
| 🔗 [JMMLU](https://github.com/nlp-waseda/JMMLU) | - | - | ⭐ 38 | 🟡 october 2025|
| 🔗 [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) | - | - | ⭐ 48 | 🔴 march 2025|
| 🔗 [jqara](https://github.com/hotchpotch/jqara) | - | - | ⭐ 43 | 🟡 september 2025|
| 🔗 [jemhopqa](https://github.com/aiishii/jemhopqa) | - | - | ⭐ 30 | 🔴 april 2025|
| 🔗 [jacred](https://github.com/youmima/jacred) | - | - | ⭐ 8 | 🔴 march 2024|
| 🔗 [jades](https://github.com/naist-nlp/jades) | - | - | ⭐ 0 | 🔴 december 2022|
| 🔗 [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) | - | - | ⭐ 24 | 🔴 december 2023|
| 🔗 [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) | - | - | ⭐ 16 | 🔴 november 2023|
| 🔗 [jacwir](https://github.com/hotchpotch/jacwir) | - | - | ⭐ 8 | 🟡 september 2025|
| 🔗 [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) | - | - | ⭐ 3 | 🔴 november 2024|
| 🔗 [j-unimorph](https://github.com/cl-tohoku/j-unimorph) | - | - | ⭐ 9 | 🟡 january|
| 🔗 [GazeVQA](https://github.com/riken-grp/GazeVQA) | - | - | ⭐ 0 | 🔴 september 2024|
| 🔗 [J-CRe3](https://github.com/riken-grp/J-CRe3) | - | - | ⭐ 10 | 🔴 january 2025|
| 🔗 [jmed-llm](https://github.com/sociocom/jmed-llm) | - | - | ⭐ 57 | 🔴 september 2024|
| 🔗 [lawtext](https://github.com/yamachig/lawtext) | - | - | ⭐ 94 | 🟡 january|
| 🔗 [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) | - | - | ⭐ 15 | 🔴 june 2024|
| 🔗 [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) | - | - | ⭐ 2 | 🔴 september 2018|
| 🔗 [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [JSeM](https://github.com/DaisukeBekki/JSeM) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [niilc-qa](https://github.com/mynlp/niilc-qa) | - | - | ⭐ 18 | 🔴 november 2015|
| 🔗 [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) | - | - | ⭐ 5 | 🔴 september 2023|
| 🔗 [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) | - | - | ⭐ 29 | 🟢 february|
| 🔗 [elaws-history](https://github.com/kissge/elaws-history) | - | - | ⭐ 5 | 🟢 today|
| 🔗 [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) | - | - | ⭐ 18 | 🔴 september 2024|
| 🔗 [hdic](https://github.com/shikeda/hdic) | - | - | ⭐ 41 | 🟢 last tuesday|
| 🔗 [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) | - | - | ⭐ 159 | 🟢 march|
| 🔗 [kanji-data](https://github.com/mimneko/kanji-data) | - | - | ⭐ 19 | 🟢 february|
| 🔗 [openchj-genji](https://github.com/togiso/openchj-genji) | - | - | ⭐ 2 | 🔴 march 2025|
| 🔗 [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) | - | - | ⭐ 1 | 🟡 may 2025|
| 🔗 [Jamp_sp](https://github.com/ynklab/Jamp_sp) | - | - | ⭐ 0 | 🔴 june 2024|
| 🔗 [jnli-neg](https://github.com/asahi-y/jnli-neg) | - | - | ⭐ 0 | 🟡 december 2025|
| 🔗 [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) | - | - | ⭐ 6 | 🔴 november 2024|
| 🔗 [jalecon](https://github.com/naist-nlp/jalecon) | - | - | ⭐ 5 | 🔴 july 2023|
| 🔗 [multils-japanese](https://github.com/naist-nlp/multils-japanese) | - | - | ⭐ 0 | 🟡 january|
| 🔗 [nwjc](https://github.com/masayu-a/nwjc) | - | - | ⭐ 10 | 🔴 april 2022|
| 🔗 [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) | - | - | ⭐ 200 | 🔴 march 2023|
| 🔗 [gimei](https://github.com/willnet/gimei) | - | - | ⭐ 424 | 🟡 january|
| 🔗 [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) | - | - | ⭐ 9 | 🟢 last tuesday|
| 🔗 [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) | - | - | ⭐ 7 | 🟢 april|
| 🔗 [kanji](https://github.com/sylhare/kanji) | - | - | ⭐ 28 | 🟢 april|
| 🔗 [jethics](https://github.com/language-media-lab/jethics) | - | - | ⭐ 2 | 🟡 june 2025|
| 🔗 [waon](https://github.com/llm-jp/waon) | - | - | ⭐ 6 | 🟡 november 2025|
| 🔗 [kuci](https://github.com/ku-nlp/kuci) | - | - | ⭐ 5 | 🔴 february 2024|
| 🔗 [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [jlpt-word-list](https://github.com/elzup/jlpt-word-list) | - | - | ⭐ 68 | 🔴 february 2022|
| 🔗 [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) | - | - | ⭐ 18 | 🔴 april 2020|
| 🔗 [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) | - | - | ⭐ 267 | 🟢 february|
| 🔗 [yjcaptions](https://github.com/yahoojapan/yjcaptions) | - | - | ⭐ 60 | 🔴 november 2016|
| 🔗 [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) | - | - | ⭐ 30 | 🔴 november 2018|
| 🔗 [lawhub](https://github.com/lwhb/lawhub) | - | - | ⭐ 152 | 🔴 november 2020|
| 🔗 [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) | - | - | ⭐ 41 | 🔴 december 2023|
| 🔗 [jconj](https://github.com/yamagoya/jconj) | - | - | ⭐ 35 | 🔴 may 2020|
| 🔗 [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) | - | - | ⭐ 21 | 🔴 december 2022|
| 🔗 [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) | - | - | ⭐ 11 | 🔴 june 2023|
| 🔗 [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) | - | - | ⭐ 5 | 🔴 june 2016|
| 🔗 [ajimee-bench](https://github.com/azookey/ajimee-bench) | - | - | ⭐ 20 | 🔴 january 2025|
| 🔗 [j-spaw](https://github.com/takamichi-lab/j-spaw) | - | - | ⭐ 5 | 🟡 august 2025|
| 🔗 [camera3](https://github.com/cyberagentailab/camera3) | - | - | ⭐ 4 | 🔴 may 2024|
| 🔗 [jgpqa](https://github.com/llm-jp/jgpqa) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) | - | - | ⭐ 2 | 🔴 june 2021|
| 🔗 [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) | - | - | ⭐ 2 | 🔴 september 2024|
| 🔗 [osworld-jp](https://github.com/karakuri-ai/osworld-jp) | - | - | ⭐ 2 | 🟢 april|
| 🔗 [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) | - | - | ⭐ 1 | 🟡 october 2025|
| 🔗 [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) | - | - | ⭐ 1 | 🔴 may 2022|
| 🔗 [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) | - | - | ⭐ 1 | 🔴 march 2021|
| 🔗 [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) | - | - | ⭐ 1 | 🟡 january|
| 🔗 [kotowaza](https://github.com/septn/kotowaza) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [selective-rag-kasensabo](https://github.com/tk-yasuno/selective-rag-kasensabo) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [jmle2026-bench](https://github.com/naoto-iwase/jmle2026-bench) | - | - | ⭐ 10 | 🟢 march|
| 🔗 [JSTS-Neg](https://github.com/reiko-y/JSTS-Neg) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [business-slide-questions](https://github.com/stockmarkteam/business-slide-questions) | - | - | ⭐ 2 | 🟡 may 2025|
| 🔗 [WLSP-antonym](https://github.com/masayu-a/WLSP-antonym) | - | - | ⭐ 0 | 🔴 march 2021|
| 🔗 [YouCook2-JP](https://github.com/nlab-mpg/YouCook2-JP) | - | - | ⭐ 0 | 🟡 august 2025|
| 🔗 [E2U](https://github.com/sociocom/E2U) | - | - | ⭐ 0 | 🟢 march|
| 🔗 [annotation-2025](https://github.com/Tiny-Colony/annotation-2025) | - | - | ⭐ 0 | 🟡 january|
| 🔗 [jhpt](https://github.com/nict-astrec-att/jhpt) | - | - | ⭐ invalid | 🟢 march|
| 🔗 [JBE-QA](https://github.com/hancules/JBE-QA) | - | - | ⭐ 0 | 🟡 november 2025|
| 🔗 [j-spaw](https://github.com/takamichi-lab/j-spaw) | - | - | ⭐ 5 | 🟡 august 2025|
| 🔗 [JMedWiC](https://github.com/EhimeNLP/JMedWiC) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [jhpt](https://github.com/nict-astrec-att/jhpt) | - | - | ⭐ invalid | 🟢 march|
| 🔗 [Doppelganger-JC](https://github.com/0017-alt/Doppelganger-JC) | - | - | ⭐ 1 | 🟡 january|
| 🔗 [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) | - | - | ⭐ 2 | 🟢 march|
| 🔗 [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) | - | - | ⭐ 1 | 🟡 january|
| 🔗 [nijl-manyoshutei](https://github.com/kokubunken/nijl-manyoshutei) | - | - | ⭐ 2 | 🟢 march|
| 🔗 [kamuskita](https://github.com/matbahasa/kamuskita) | - | - | ⭐ 2 | 🟢 april|


## Tutorial
学习日语自然语言处理工具与技术的教程资源

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
 * [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) - NLP2025年的教程“地理信息和语言处理实践入门”的资料和源代码
 * [nlp100v2025](https://github.com/upura/nlp100v2025) - 用Python解决“自然语言处理100道题目2025”
 * [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) - 《主题模型》（机器学习专业系列）笔记
 * [slp2025](https://github.com/ryota-komatsu/slp2025) -音学シンポジウム2025チュートリアル「マルチモーダル大規模言語モデル入門」資料
 * [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) - 印象出版社“IT基础教养 自然语言处理＆图像分析”
 * [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) - 书籍“现场应用生成AI代理实践入门”（講談社サイエンティフィック社）中使用的源代码
 * [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) - 2024年 立教大学研究生院 人工智能科学研究专业 自然语言处理专题
 * [support-genai-book](https://github.com/yoheikikuta/support-genai-book) - 这是从原论文中解读出来的生成人工智能（技术评论社）的支持页面。
 * [ir100](https://github.com/ir100/ir100) - 信息检索100个关键点
 * [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) - 《Kaggle开始大规模语言模型入门 - 自然语言处理实践编程》支持网站


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) | - | - | ⭐ 65 | 🔴 january 2020|
| 🔗 [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) | - | - | ⭐ 205 | 🔴 september 2016|
| 🔗 [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) | - | - | ⭐ 5 | 🔴 may 2022|
| 🔗 [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) | - | - | ⭐ 5 | 🔴 march 2019|
| 🔗 [ginza-examples](https://github.com/poyo46/ginza-examples) | - | - | ⭐ 15 | 🔴 january 2021|
| 🔗 [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) | - | - | ⭐ 0 | 🟡 august 2025|
| 🔗 [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) | - | - | ⭐ 29 | 🔴 january 2022|
| 🔗 [bert-book](https://github.com/stockmarkteam/bert-book) | - | - | ⭐ 263 | 🔴 february 2024|
| 🔗 [janome-tutorial](https://github.com/mocobeta/janome-tutorial) | - | - | ⭐ 31 | 🔴 march 2019|
| 🔗 [handson-language-models](https://github.com/hnishi/handson-language-models) | - | - | ⭐ 3 | 🔴 march 2021|
| 🔗 [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) | - | - | ⭐ 6 | 🔴 june 2021|
| 🔗 [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) | - | - | ⭐ 144 | 🔴 may 2021|
| 🔗 [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) | - | - | ⭐ 234 | 🔴 may 2024|
| 🔗 [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) | - | - | ⭐ 10 | 🔴 may 2023|
| 🔗 [llm-book](https://github.com/ghmagazine/llm-book) | - | - | ⭐ 466 | 🟡 december 2025|
| 🔗 [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) | - | - | ⭐ 113 | 🔴 april 2024|
| 🔗 [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) | - | - | ⭐ 3 | 🔴 june 2024|
| 🔗 [nlpbook](https://github.com/mamorlis/nlpbook) | - | - | ⭐ 14 | 🔴 april 2025|
| 🔗 [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) | - | - | ⭐ 22 | 🔴 march 2024|
| 🔗 [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) | - | - | ⭐ 30 | 🔴 july 2024|
| 🔗 [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) | - | - | ⭐ repo not found | 🔴 august 2024|
| 🔗 [nlp100v2020](https://github.com/upura/nlp100v2020) | - | - | ⭐ 90 | 🔴 april 2025|
| 🔗 [textmining-ja](https://github.com/paithiov909/textmining-ja) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) | - | - | ⭐ 17 | 🟢 february|
| 🔗 [nlp100v2025](https://github.com/upura/nlp100v2025) | - | - | ⭐ 90 | 🔴 april 2025|
| 🔗 [public-annotations](https://github.com/manga109/public-annotations) | - | - | ⭐ 13 | 🔴 april 2025|
| 🔗 [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) | - | - | ⭐ 4 | 🟡 may 2025|
| 🔗 [slp2025](https://github.com/ryota-komatsu/slp2025) | - | - | ⭐ 65 | 🟢 yesterday|
| 🔗 [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) | - | - | ⭐ 4 | 🟡 june 2025|
| 🔗 [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) | - | - | ⭐ 193 | 🔴 invalid|
| 🔗 [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [support-genai-book](https://github.com/yoheikikuta/support-genai-book) | - | - | ⭐ 96 | 🟡 january|
| 🔗 [ir100](https://github.com/ir100/ir100) | - | - | ⭐ 93 | 🟡 december 2025|
| 🔗 [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) | - | - | ⭐ 34 | 🟢 march|


## Research summary
汇总日语自然语言处理相关研究成果和论文的资料

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 一个预训练的BERT模型列表，包括日语的单词/子词分词和词汇构建算法信息。
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 收集和分类有关日语文法错误修正的文献的存储库。
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - 文本语料库列表和更多（主要是日语）
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - 深度学习模型性能最大化的系统指南
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 尝试将日语音标，特别是声调资源整合成一个列表。
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - 开源的日语LLM总结


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) | - | - | ⭐ 132 | 🔴 march 2023|
| 🔗 [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) | - | - | ⭐ 13 | 🔴 april 2025|
| 🔗 [dataset-list](https://github.com/ikegami-yukino/dataset-list) | - | - | ⭐ 118 | 🔴 july 2024|
| 🔗 [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) | - | - | ⭐ 190 | 🔴 january 2023|
| 🔗 [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) | - | - | ⭐ 126 | 🔴 february 2024|
| 🔗 [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) | - | - | ⭐ 1.4k | 🟢 last wednesday|


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
 * [sarumaj](https://github.com/sarumaj) - [github](https://github.com/sarumaj)
 * [ln2058](https://github.com/ln2058) - [github](https://github.com/ln2058)
 * [ajtgjmdjp](https://github.com/ajtgjmdjp) - [github](https://github.com/ajtgjmdjp)
