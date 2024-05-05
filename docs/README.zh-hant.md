# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專用於 Python 庫、預訓練模型、詞典和日語 NLP 語料庫的精選資源列表

[此列表](https://github.com/taishi-i/awesome-japanese-nlp-resources)包括 558 個日語 NLP 存儲庫。 Hugging Face Spaces 上提供了用於搜索這些存儲庫的[工具](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)。
您可以在 Huggingface 上找到的模型，请查看[这里](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md)。

我們已經發布名為 [awesome-japanese-nlp-classification-dataset](https://huggingface.co/datasets/taishi-i/awesome-japanese-nlp-classification-dataset) 的日語 NLP 分類數據集。


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## The latest additions 🎉

**Corpus**
 * [jemhopqa](https://github.com/aiishii/jemhopqa) - JEMHopQA（日本語説明可能なマルチホップ質問応答）は、内部推論を評価できる日本語マルチホップQAデータセットです。
 * [qedatasetjaen](https://github.com/tntc-project/qedatasetjaen) - 這個存儲庫包含了源語言（日語）和目標語言（英語）文檔的詞級翻譯質量估計標籤。
 * [jacred](https://github.com/youmima/jacred) - 用於日文文件級關係提取數據集的存儲庫（計劃在三月份發布）。
用於日文文件級關係提取數據集的存儲庫（計劃在三月份發布）。
 * [jades](https://github.com/naist-nlp/jades) - JADES是一個針對非母語使用者的日文文本簡化數據集，詳細介紹在《JADES:針對非母語使用者的日文新文本簡化數據集》（論文即將發表）。
 * [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) - 2023年8月，墨爾本大學公開了安全性評估數據集『Do-Not-Answer』，該數據集已經被自動翻譯成日語，並且考慮了日本文化進行了修正，以便在日語LLM評估中使用。
 * [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) - OpenAssistant 的開源數據 OASST1 已經被翻譯成日文的數據集。

**ChatGPT**
 * [japagen](https://github.com/retrieva/japagen) - 使用LLM在日語任務中生成虛擬學習數據的研究

**Python**
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - 探索日本SimCSE

_Updated on May 05, 2024_

## Contents
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
 * [Dictionary](#dictionary)
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

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - SudachiPy 0.6*及以上版本已開發為Sudachi.rs。
 * [Janome](https://github.com/mocobeta/janome) - 純Python編寫的日語形態分析引擎
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - mecab-python。mecab-python。您可以在此處找到原始版本：http://taku910.github.io/mecab/。
 * [mecab](https://github.com/ikegami-yukino/mecab) - 這個存儲庫是用於構建Windows 64位MeCab二進制文件和改進MeCab Python綁定的。
 * [fugashi](https://github.com/polm/fugashi) - 一個Cython MeCab包裝器，用於快速、Python式的日語分詞和形態分析。
 * [nagisa](https://github.com/taishi-i/nagisa) - 基於循環神經網絡的日語分詞器
 * [pyknp](https://github.com/ku-nlp/pyknp) - 一個用於 JUMAN++/KNP 的 Python 模組
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - KyTea 的 Python 封裝程式
 * [konoha](https://github.com/himkt/konoha) - 木葉：日本分詞器的簡單封裝
 * [natto-py](https://github.com/buruzaemon/natto-py) - natto-py 將 Python 程式語言與 MeCab 結合，後者是日語詞性和形態分析器。
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - 樂天 MA（Python 版本）
 * [python-vaporetto](https://github.com/daac-tools/python-vaporetto) - Vaporetto 是一個快速且輕量級的基於點預測的分詞器。這是 Vaporetto 的 Python 封裝。
 * [dango](https://github.com/mkartawijaya/dango) - 一個易於使用的日文分詞器，針對語言學習者和非語言學家。
 * [rhoknp](https://github.com/ku-nlp/rhoknp) - 又一個 Juman++/KNP 的 Python 綁定程式
 * [python-vibrato](https://github.com/daac-tools/python-vibrato) - 基於維特比算法的加速分詞器（Python封裝）
 * [jagger-python](https://github.com/lighttransport/jagger-python) - Jagger的Python綁定（基於模式的日語形態分析器的C++實現）


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[SudachiPy](https://github.com/WorksApplications/SudachiPy)|[![Downloads](https://static.pepy.tech/badge/sudachipy/week)](https://pepy.tech/project/sudachipy)|[![Downloads](https://static.pepy.tech/badge/sudachipy)](https://pepy.tech/project/sudachipy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiPy?style=social)|
|[Janome](https://github.com/mocobeta/janome)|[![Downloads](https://static.pepy.tech/badge/janome/week)](https://pepy.tech/project/janome)|[![Downloads](https://static.pepy.tech/badge/janome)](https://pepy.tech/project/janome)|![GitHub Repo stars](https://img.shields.io/github/stars/mocobeta/janome?style=social)|
|[mecab-python3](https://github.com/SamuraiT/mecab-python3)|[![Downloads](https://static.pepy.tech/badge/mecab-python3/week)](https://pepy.tech/project/mecab-python3)|[![Downloads](https://static.pepy.tech/badge/mecab-python3)](https://pepy.tech/project/mecab-python3)|![GitHub Repo stars](https://img.shields.io/github/stars/SamuraiT/mecab-python3?style=social)|
|[mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python)|[![Downloads](https://static.pepy.tech/badge/mecab/week)](https://pepy.tech/project/mecab)|[![Downloads](https://static.pepy.tech/badge/mecab)](https://pepy.tech/project/mecab)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/mecab?style=social)|
|[fugashi](https://github.com/polm/fugashi)|[![Downloads](https://static.pepy.tech/badge/fugashi/week)](https://pepy.tech/project/fugashi)|[![Downloads](https://static.pepy.tech/badge/fugashi)](https://pepy.tech/project/fugashi)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/fugashi?style=social)|
|[nagisa](https://github.com/taishi-i/nagisa)|[![Downloads](https://static.pepy.tech/badge/nagisa/week)](https://pepy.tech/project/nagisa)|[![Downloads](https://static.pepy.tech/badge/nagisa)](https://pepy.tech/project/nagisa)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/nagisa?style=social)|
|[pyknp](https://github.com/ku-nlp/pyknp)|[![Downloads](https://static.pepy.tech/badge/pyknp/week)](https://pepy.tech/project/pyknp)|[![Downloads](https://static.pepy.tech/badge/pyknp)](https://pepy.tech/project/pyknp)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/pyknp?style=social)|
|[Mykytea-python](https://github.com/chezou/Mykytea-python)|[![Downloads](https://static.pepy.tech/badge/kytea/week)](https://pepy.tech/project/kytea)|[![Downloads](https://static.pepy.tech/badge/kytea)](https://pepy.tech/project/kytea)|![GitHub Repo stars](https://img.shields.io/github/stars/chezou/Mykytea-python?style=social)|
|[konoha](https://github.com/himkt/konoha)|[![Downloads](https://static.pepy.tech/badge/konoha/week)](https://pepy.tech/project/konoha)|[![Downloads](https://static.pepy.tech/badge/konoha)](https://pepy.tech/project/konoha)|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/konoha?style=social)|
|[natto-py](https://github.com/buruzaemon/natto-py)|[![Downloads](https://static.pepy.tech/badge/natto-py/week)](https://pepy.tech/project/natto-py)|[![Downloads](https://static.pepy.tech/badge/natto-py)](https://pepy.tech/project/natto-py)|![GitHub Repo stars](https://img.shields.io/github/stars/buruzaemon/natto-py?style=social)|
|[rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python)|[![Downloads](https://static.pepy.tech/badge/rakutenma/week)](https://pepy.tech/project/rakutenma)|[![Downloads](https://static.pepy.tech/badge/rakutenma)](https://pepy.tech/project/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/rakutenma-python?style=social)|
|[python-vaporetto](https://github.com/daac-tools/python-vaporetto)|[![Downloads](https://static.pepy.tech/badge/vaporetto/week)](https://pepy.tech/project/vaporetto)|[![Downloads](https://static.pepy.tech/badge/vaporetto)](https://pepy.tech/project/vaporetto)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/python-vaporetto?style=social)|
|[dango](https://github.com/mkartawijaya/dango)|[![Downloads](https://static.pepy.tech/badge/dango/week)](https://pepy.tech/project/dango)|[![Downloads](https://static.pepy.tech/badge/dango)](https://pepy.tech/project/dango)|![GitHub Repo stars](https://img.shields.io/github/stars/mkartawijaya/dango?style=social)|
|[rhoknp](https://github.com/ku-nlp/rhoknp)|[![Downloads](https://static.pepy.tech/badge/rhoknp/week)](https://pepy.tech/project/rhoknp)|[![Downloads](https://static.pepy.tech/badge/rhoknp)](https://pepy.tech/project/rhoknp)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/rhoknp?style=social)|
|[python-vibrato](https://github.com/daac-tools/python-vibrato)|[![Downloads](https://static.pepy.tech/badge/vibrato/week)](https://pepy.tech/project/vibrato)|[![Downloads](https://static.pepy.tech/badge/vibrato)](https://pepy.tech/project/vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/python-vibrato?style=social)|
|[jagger-python](https://github.com/lighttransport/jagger-python)|[![Downloads](https://pepy.tech/badge/jagger/week)](https://pepy.tech/project/jagger)|[![Downloads](https://pepy.tech/badge/jagger)](https://pepy.tech/project/jagger)|![GitHub Repo stars](https://img.shields.io/github/stars/lighttransport/jagger-python?style=social)|


### Parsing

 * [ginza](https://github.com/megagonlabs/ginza) - 一個基於Universal Dependencies的spaCy框架的日本NLP庫
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - 另一個日本依存結構分析器
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - 現代和當代日語的分詞器、詞性標記器、詞形還原器和依存句法分析器
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - Camphr - 用於創建管道組件的 NLP 庫
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - 使用BERT模型的現代和當代日語分詞器、詞性標記器、詞形還原器和依存句法分析器
 * [depccg](https://github.com/masashi-y/depccg) - 具有超標記和依存因素模型的A* CCG解析器
 * [bertknp](https://github.com/ku-nlp/bertknp) - 基於BERT的日語依存句法分析器
 * [esupar](https://github.com/KoichiYasuoka/esupar) - 使用BERT/RoBERTa/DeBERTa模型的分詞器POS-標記器和依存句法分析器，適用於日語和其他語言。
 * [yomikata](https://github.com/passaglia/yomikata) - 使用微調的BERT模型進行異音詞消歧的程式庫。
 * [jdepp-python](https://github.com/lighttransport/jdepp-python) - J.DepP的Python綁定（日本依存句法分析器的C++實現）


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ginza](https://github.com/megagonlabs/ginza)|[![Downloads](https://static.pepy.tech/badge/ginza/week)](https://pepy.tech/project/ginza)|[![Downloads](https://static.pepy.tech/badge/ginza)](https://pepy.tech/project/ginza)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ginza?style=social)|
|[cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python)|[![Downloads](https://static.pepy.tech/badge/cabocha-python/week)](https://pepy.tech/project/cabocha-python)|[![Downloads](https://static.pepy.tech/badge/cabocha-python)](https://pepy.tech/project/cabocha-python)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/cabocha?style=social)|
|[UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD)|[![Downloads](https://static.pepy.tech/badge/UniDic2UD/week)](https://pepy.tech/project/UniDic2UD)|[![Downloads](https://static.pepy.tech/badge/UniDic2UD)](https://pepy.tech/project/UniDic2UD)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/UniDic2UD?style=social)|
|[camphr](https://github.com/PKSHATechnology-Research/camphr)|[![Downloads](https://static.pepy.tech/badge/camphr/week)](https://pepy.tech/project/camphr)|[![Downloads](https://static.pepy.tech/badge/camphr)](https://pepy.tech/project/camphr)|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/camphr?style=social)|
|[SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic)|[![Downloads](https://static.pepy.tech/badge/SuParUniDic/week)](https://pepy.tech/project/SuParUniDic)|[![Downloads](https://static.pepy.tech/badge/SuParUniDic)](https://pepy.tech/project/SuParUniDic)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/SuPar-UniDic?style=social)|
|[depccg](https://github.com/masashi-y/depccg)|[![Downloads](https://static.pepy.tech/badge/depccg/week)](https://pepy.tech/project/depccg)|[![Downloads](https://static.pepy.tech/badge/depccg)](https://pepy.tech/project/depccg)|![GitHub Repo stars](https://img.shields.io/github/stars/masashi-y/depccg?style=social)|
|[bertknp](https://github.com/ku-nlp/bertknp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/bertknp?style=social)|
|[esupar](https://github.com/KoichiYasuoka/esupar)|[![Downloads](https://static.pepy.tech/badge/esupar/week)](https://pepy.tech/project/esupar)|[![Downloads](https://static.pepy.tech/badge/esupar)](https://pepy.tech/project/esupar)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/esupar?style=social)|
|[yomikata](https://github.com/passaglia/yomikata)|[![Downloads](https://static.pepy.tech/badge/yomikata/week)](https://pepy.tech/project/yomikata)|[![Downloads](https://static.pepy.tech/badge/yomikata)](https://pepy.tech/project/yomikata)|![GitHub Repo stars](https://img.shields.io/github/stars/passaglia/yomikata?style=social)|
|[jdepp-python](https://github.com/lighttransport/jdepp-python)|[![Downloads](https://pepy.tech/badge/jdepp/week)](https://pepy.tech/project/jdepp)|[![Downloads](https://pepy.tech/badge/jdepp)](https://pepy.tech/project/jdepp)|![GitHub Repo stars](https://img.shields.io/github/stars/lighttransport/jdepp-python?style=social)|


### Converter

 * [pykakasi](https://github.com/miurahr/pykakasi) - 輕量級的轉換器，可將日文假名漢字句子轉換為假名羅馬字。
 * [cutlet](https://github.com/polm/cutlet) - Python中的日文轉羅馬字轉換器
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - 將英文字母轉換為片假名
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - 將阿拉伯數字或「西方」風格的數字轉換為日本上下文。
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Python的Mozc：假名漢字轉換器
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - 日文文本解析器，將平假名/片假名字符串分離成音節（拼音）。
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - 將日文轉換為音素序列的腳本
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - 一個快速的字符轉換和音譯庫，基於日本國稅廳的法人番號系統定義的方案。
 * [wiredify](https://github.com/eggplants/wiredify) - 將日文假名從ba-bi-bu-be-bo轉換為va-vi-vu-ve-vo
將日文假名從ba-bi-bu-be-bo轉換為va-vi-vu-ve-vo
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - 使用MeCab獲取日文讀音（yomigana）和重音的簡單Python套件（CLI/Python API）。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[pykakasi](https://github.com/miurahr/pykakasi)|[![Downloads](https://static.pepy.tech/badge/pykakasi/week)](https://pepy.tech/project/pykakasi)|[![Downloads](https://static.pepy.tech/badge/pykakasi)](https://pepy.tech/project/pykakasi)|![GitHub Repo stars](https://img.shields.io/github/stars/miurahr/pykakasi?style=social)|
|[cutlet](https://github.com/polm/cutlet)|[![Downloads](https://static.pepy.tech/badge/cutlet/week)](https://pepy.tech/project/cutlet)|[![Downloads](https://static.pepy.tech/badge/cutlet)](https://pepy.tech/project/cutlet)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/cutlet?style=social)|
|[alphabet2kana](https://github.com/shihono/alphabet2kana)|[![Downloads](https://static.pepy.tech/badge/alphabet2kana/week)](https://pepy.tech/project/alphabet2kana)|[![Downloads](https://static.pepy.tech/badge/alphabet2kana)](https://pepy.tech/project/alphabet2kana)|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/alphabet2kana?style=social)|
|[Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Greatdane/Convert-Numbers-to-Japanese?style=social)|
|[mozcpy](https://github.com/ikegami-yukino/mozcpy)|[![Downloads](https://static.pepy.tech/badge/mozcpy/week)](https://pepy.tech/project/mozcpy)|[![Downloads](https://static.pepy.tech/badge/mozcpy)](https://pepy.tech/project/mozcpy)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/mozcpy?style=social)|
|[jamorasep](https://github.com/tachi-hi/jamorasep)|[![Downloads](https://static.pepy.tech/badge/jamorasep/week)](https://pepy.tech/project/jamorasep)|[![Downloads](https://static.pepy.tech/badge/jamorasep)](https://pepy.tech/project/jamorasep)|![GitHub Repo stars](https://img.shields.io/github/stars/tachi-hi/jamorasep?style=social)|
|[text2phoneme](https://github.com/korguchi/text2phoneme)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/korguchi/text2phoneme?style=social)|
|[jntajis-python](https://github.com/opencollector/jntajis-python)|[![Downloads](https://static.pepy.tech/badge/jntajis-python/week)](https://pepy.tech/project/jntajis-python)|[![Downloads](https://static.pepy.tech/badge/jntajis-python)](https://pepy.tech/project/jntajis-python)|![GitHub Repo stars](https://img.shields.io/github/stars/opencollector/jntajis-python?style=social)|
|[wiredify](https://github.com/eggplants/wiredify)|[![Downloads](https://pepy.tech/badge/wiredify/week)](https://pepy.tech/project/wiredify)|[![Downloads](https://pepy.tech/badge/wiredify)](https://pepy.tech/project/wiredify)|![GitHub Repo stars](https://img.shields.io/github/stars/eggplants/wiredify?style=social)|
|[mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner)|[![Downloads](https://pepy.tech/badge/mecab-text-cleaner/week)](https://pepy.tech/project/mecab-text-cleaner)|[![Downloads](https://pepy.tech/badge/mecab-text-cleaner)](https://pepy.tech/project/mecab-text-cleaner)|![GitHub Repo stars](https://img.shields.io/github/stars/34j/mecab-text-cleaner?style=social)|


### Preprocessor

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - mecab-neologd 的日文文本正規化工具
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - 純Python日文字符互轉器，支援平假名、片假名、半角和全角。
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - 一個快速轉換日文半角和全角字符的轉換器
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 一款強大的日文網頁文本清理工具
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 構成並管理多個前處理的文字前處理工具
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho是一個Python模組，用於在日語中半角片假名和全角片假名之間進行雙向轉換。
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - 另一個快速的日本字符串轉換器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[neologdn](https://github.com/ikegami-yukino/neologdn)|[![Downloads](https://static.pepy.tech/badge/neologdn/week)](https://pepy.tech/project/neologdn)|[![Downloads](https://static.pepy.tech/badge/neologdn)](https://pepy.tech/project/neologdn)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/neologdn?style=social)|
|[jaconv](https://github.com/ikegami-yukino/jaconv)|[![Downloads](https://static.pepy.tech/badge/jaconv/week)](https://pepy.tech/project/jaconv)|[![Downloads](https://static.pepy.tech/badge/jaconv)](https://pepy.tech/project/jaconv)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/jaconv?style=social)|
|[mojimoji](https://github.com/studio-ousia/mojimoji)|[![Downloads](https://static.pepy.tech/badge/mojimoji/week)](https://pepy.tech/project/mojimoji)|[![Downloads](https://static.pepy.tech/badge/mojimoji)](https://pepy.tech/project/mojimoji)|![GitHub Repo stars](https://img.shields.io/github/stars/studio-ousia/mojimoji?style=social)|
|[text-cleaning](https://github.com/ku-nlp/text-cleaning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/text-cleaning?style=social)|
|[HojiChar](https://github.com/HojiChar/HojiChar)|[![Downloads](https://static.pepy.tech/badge/HojiChar/week)](https://pepy.tech/project/HojiChar)|[![Downloads](https://static.pepy.tech/badge/HojiChar)](https://pepy.tech/project/HojiChar)|![GitHub Repo stars](https://img.shields.io/github/stars/HojiChar/HojiChar?style=social)|
|[utsuho](https://github.com/juno-rmks/utsuho)|[![Downloads](https://pepy.tech/badge/utsuho/week)](https://pepy.tech/project/utsuho)|[![Downloads](https://pepy.tech/badge/utsuho)](https://pepy.tech/project/utsuho)|![GitHub Repo stars](https://img.shields.io/github/stars/juno-rmks/utsuho?style=social)|
|[python-habachen](https://github.com/Hizuru3/python-habachen)|[![Downloads](https://pepy.tech/badge/habachen/week)](https://pepy.tech/project/habachen)|[![Downloads](https://pepy.tech/badge/habachen)](https://pepy.tech/project/habachen)|![GitHub Repo stars](https://img.shields.io/github/stars/Hizuru3/python-habachen?style=social)|


### Sentence spliter

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日本語文境界判定工具
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日本語句子分解器
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 另一個針對日文文本的句子級分詞器
 * [budoux](https://github.com/google/budoux) - 獨立的。小巧的。語言中立的。BudouX 是機器學習驅動的斷行整理工具 Budou 的後繼者。
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - Python 的日文句子分割程式庫
 * [hasami](https://github.com/mkartawijaya/hasami) - 一個用於對日文文本進行句子分割的工具
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - 用 Rust 編寫的 Python 日文文本分割器
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日本語句子分割工具比較


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bunkai](https://github.com/megagonlabs/bunkai)|[![Downloads](https://static.pepy.tech/badge/bunkai/week)](https://pepy.tech/project/bunkai)|[![Downloads](https://static.pepy.tech/badge/bunkai)](https://pepy.tech/project/bunkai)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/bunkai?style=social)|
|[japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker)|[![Downloads](https://static.pepy.tech/badge/japanese-sentence-breaker/week)](https://pepy.tech/project/japanese-sentence-breaker)|[![Downloads](https://static.pepy.tech/badge/japanese-sentence-breaker)](https://pepy.tech/project/japanese-sentence-breaker)|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/japanese-sentence-breaker?style=social)|
|[sengiri](https://github.com/ikegami-yukino/sengiri)|[![Downloads](https://static.pepy.tech/badge/sengiri/week)](https://pepy.tech/project/sengiri)|[![Downloads](https://static.pepy.tech/badge/sengiri)](https://pepy.tech/project/sengiri)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/sengiri?style=social)|
|[budoux](https://github.com/google/budoux)|[![Downloads](https://static.pepy.tech/badge/budoux/week)](https://pepy.tech/project/budoux)|[![Downloads](https://static.pepy.tech/badge/budoux)](https://pepy.tech/project/budoux)|![GitHub Repo stars](https://img.shields.io/github/stars/google/budoux?style=social)|
|[ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter)|[![Downloads](https://static.pepy.tech/badge/ja_sentence_segmenter/week)](https://pepy.tech/project/ja_sentence_segmenter)|[![Downloads](https://static.pepy.tech/badge/ja_sentence_segmenter)](https://pepy.tech/project/ja_sentence_segmenter)|![GitHub Repo stars](https://img.shields.io/github/stars/wwwcojp/ja_sentence_segmenter?style=social)|
|[hasami](https://github.com/mkartawijaya/hasami)|[![Downloads](https://static.pepy.tech/badge/hasami/week)](https://pepy.tech/project/hasami)|[![Downloads](https://static.pepy.tech/badge/hasami)](https://pepy.tech/project/hasami)|![GitHub Repo stars](https://img.shields.io/github/stars/mkartawijaya/hasami?style=social)|
|[kuzukiri](https://github.com/alinear-corp/kuzukiri)|[![Downloads](https://static.pepy.tech/badge/kuzukiri/week)](https://pepy.tech/project/kuzukiri)|[![Downloads](https://static.pepy.tech/badge/kuzukiri)](https://pepy.tech/project/kuzukiri)|![GitHub Repo stars](https://img.shields.io/github/stars/alinear-corp/kuzukiri?style=social)|
|[ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/ja-senter-benchmark?style=social)|


### Sentiment analysis

 * [oseti](https://github.com/ikegami-yukino/oseti) - 基於詞典的日語情感分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 日本語文書的正負面分類。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日文文本情感分析器
 * [asari](https://github.com/Hironsan/asari) - 使用Python實現的日語情感分析器。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[oseti](https://github.com/ikegami-yukino/oseti)|[![Downloads](https://static.pepy.tech/badge/oseti/week)](https://pepy.tech/project/oseti)|[![Downloads](https://static.pepy.tech/badge/oseti)](https://pepy.tech/project/oseti)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/oseti?style=social)|
|[negapoji](https://github.com/liaoziyang/negapoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/liaoziyang/negapoji?style=social)|
|[pymlask](https://github.com/ikegami-yukino/pymlask)|[![Downloads](https://static.pepy.tech/badge/pymlask/week)](https://pepy.tech/project/pymlask)|[![Downloads](https://static.pepy.tech/badge/pymlask)](https://pepy.tech/project/pymlask)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/pymlask?style=social)|
|[asari](https://github.com/Hironsan/asari)|[![Downloads](https://static.pepy.tech/badge/asari/week)](https://pepy.tech/project/asari)|[![Downloads](https://static.pepy.tech/badge/asari)](https://pepy.tech/project/asari)|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/asari?style=social)|


### Machine translation

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawl 預訓練神經機器翻譯 (NMT) 模型的使用示例。
 * [JASS](https://github.com/Mao-KU/JASS) - JASS：針對日本特定序列的序列到序列預訓練，用於神經機器翻譯（LREC2020）和基於語言學的多任務預訓練，用於低資源神經機器翻譯（ACM TALLIP）。
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 一個針對日英機器翻譯韌性的現象級評估數據集。該數據集基於MTNT數據集，並附加了四種語言現象的註釋；專有名詞、縮寫名詞、口語表達和變體。COLING 2020。
 * [VISA](https://github.com/ku-nlp/VISA) - 一個用於視覺場景感知機器翻譯的模糊字幕數據集


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MorinoseiMorizo/jparacrawl-finetune?style=social)|
|[JASS](https://github.com/Mao-KU/JASS)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Mao-KU/JASS?style=social)|
|[PheMT](https://github.com/cl-tohoku/PheMT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/PheMT?style=social)|
|[VISA](https://github.com/ku-nlp/VISA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/VISA?style=social)|


### Named entity recognition

 * [namaco](https://github.com/chakki-works/namaco) - 基於字元的命名實體識別。
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia是一個從維基百科擴展出來的命名實體詞典。
 * [noyaki](https://github.com/ken11/noyaki) - 將字符跨度標籤信息轉換為基於分詞文本的標籤信息。
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - 用於BERT模型微調的代碼。這是用於創建和使用用於實體識別任務的模型的BERT模型微調示例。
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 從基於詳細註釋標準的病例報告語料庫中進行固有表達和關係抽取精度推論的代碼。
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp，一個用於對日文文本進行地理標記的Python模塊。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namaco](https://github.com/chakki-works/namaco)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/namaco?style=social)|
|[entitypedia](https://github.com/chakki-works/entitypedia)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/entitypedia?style=social)|
|[noyaki](https://github.com/ken11/noyaki)|[![Downloads](https://static.pepy.tech/badge/noyaki/week)](https://pepy.tech/project/noyaki)|[![Downloads](https://static.pepy.tech/badge/noyaki)](https://pepy.tech/project/noyaki)|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/noyaki?style=social)|
|[bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/bert-japanese-ner-finetuning?style=social)|
|[joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aih-uth/joint-information-extraction-hs?style=social)|
|[pygeonlp](https://github.com/geonlp-platform/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp/week)](https://pepy.tech/project/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp)](https://pepy.tech/project/pygeonlp)|![GitHub Repo stars](https://img.shields.io/github/stars/geonlp-platform/pygeonlp?style=social)|


### OCR

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - 關於日文文字的光學字符識別，主要聚焦於日本漫畫。
 * [mokuro](https://github.com/kha-white/mokuro) - 在瀏覽器中閱讀日本漫畫，並可選擇文字。
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - 手寫日文OCR演示，使用觸控面板繪製輸入文本，使用Intel OpenVINO工具包。
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - 日本語OCR
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - NDLOCR的應用程式
 * [donut](https://github.com/clovaai/donut) - OCR-free文件理解轉換器（Donut）和合成文件生成器（SynthDoG）的官方實施，ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - 漫畫翻譯器 - 從網址獲取日本漫畫以翻譯漫畫圖像
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - 識別現代日本雜誌的OCR系統
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - NDLOCR使用文字識別模組
 * [Poricom](https://github.com/blueaxis/Poricom) - 漫畫圖像的光學字符識別。漫畫OCR桌面應用程式。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[manga-ocr](https://github.com/kha-white/manga-ocr)|[![Downloads](https://static.pepy.tech/badge/manga-ocr/week)](https://pepy.tech/project/manga-ocr)|[![Downloads](https://static.pepy.tech/badge/manga-ocr)](https://pepy.tech/project/manga-ocr)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/manga-ocr?style=social)|
|[mokuro](https://github.com/kha-white/mokuro)|[![Downloads](https://static.pepy.tech/badge/mokuro/week)](https://pepy.tech/project/mokuro)|[![Downloads](https://static.pepy.tech/badge/mokuro)](https://pepy.tech/project/mokuro)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/mokuro?style=social)|
|[handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yas-sim/handwritten-japanese-ocr?style=social)|
|[OCR_Japanease](https://github.com/tanreinama/OCR_Japanease)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/OCR_Japanease?style=social)|
|[ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndlocr_cli?style=social)|
|[donut](https://github.com/clovaai/donut)|[![Downloads](https://static.pepy.tech/badge/donut-python/week)](https://pepy.tech/project/donut-python)|[![Downloads](https://static.pepy.tech/badge/donut-python)](https://pepy.tech/project/donut-python)|![GitHub Repo stars](https://img.shields.io/github/stars/clovaai/donut?style=social)|
|[JMTrans](https://github.com/ttop32/JMTrans)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ttop32/JMTrans?style=social)|
|[Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ducanh841988/Kindai-OCR?style=social)|
|[text_recognition](https://github.com/ndl-lab/text_recognition)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/text_recognition?style=social)|
|[Poricom](https://github.com/blueaxis/Poricom)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/blueaxis/Poricom?style=social)|


### Tool for pretrained models

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE：日本通用語言理解評估
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - 在spacy-transformers中使用自定義分詞器
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - 使用T5生成對話
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - 調查各種DNN文本分類器，包括MLP、CNN、RNN、BERT方法。
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - 使用FastAPI和BERT部署情感分析伺服器
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - 基於遮蔽語言模型的日語和越南語評分
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - Shiba 的 AllenNLP 整合：日本 CANINE 模型
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - 用於評估預先訓練的日語word2vec模型的日語相似性數據集腳本
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - 基於BERT的日語GEC標記
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - 日本語-BPE編碼器
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - 日本語-BPE編碼器版本2
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - 日本語文法錯誤訂正工具
 * [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) - 日本穩定擴散是一種日本特有的潛在文本到圖像擴散模型，能夠生成逼真的照片般的圖像，並接受任何文本輸入。
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - 一個針對nagisa的BERT模型
 * [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) - 前綴調整 GPT/GPT-NeoX 模型的範例代碼以及使用訓練過的前綴進行推論的代碼。
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - JGLUE的訓練和評估腳本，這是一個日語理解基準測試。
 * [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) - Transformers 库的日语分词器
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP 語言模型評估工具
 * [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) - 不同的分詞器在連續書寫語言的下游任務中表現如何？：以日語為例的案例研究 - ACL SRW 2023
 * [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) - 一個用於少樣本評估自回歸語言模型的框架。
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classification
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP 語言模型評估工具
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - 該存儲庫包含已修改的腳本和合併腳本，用於將Alpaca-Lora適配器調整為支持LoRA調諧，假設使用了“rinna/japanese-gpt-neox...” [gpt-neox]模型轉換為ggml。
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - 這個存儲庫是為了評估日本語LLM的角色扮演性能而創建的。
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - 這個儲存庫支援YuzuAI的Rakuda排行榜，該排行榜是日本語言模型的日本專用版本，類似於LMSYS的Vicuna評估。
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - 這個工具可以跨多個數據集對日語大規模語言模型進行自動評估。
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - 此存儲庫包含了LLM-jp模型的監督微調代碼。
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - 這是一個整理了在LLM勉強會（LLM-jp）中開發的與LLM用戶端相關的分詞器的存儲庫。
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - 日語語言模型金融評估工具
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - 日本維卡尼亞QA基準


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[JGLUE](https://github.com/yahoojapan/JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yahoojapan/JGLUE?style=social)|
|[ginza-transformers](https://github.com/megagonlabs/ginza-transformers)|[![Downloads](https://static.pepy.tech/badge/ginza-transformers/week)](https://pepy.tech/project/ginza-transformers)|[![Downloads](https://static.pepy.tech/badge/ginza-transformers)](https://pepy.tech/project/ginza-transformers)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ginza-transformers?style=social)|
|[t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Jinyamyzk/t5_japanese_dialogue_generation?style=social)|
|[japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Masao-Taketani/japanese_text_classification?style=social)|
|[Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/izuna385/Japanese-BERT-Sentiment-Analyzer?style=social)|
|[jmlm_scoring](https://github.com/minhpqn/jmlm_scoring)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/minhpqn/jmlm_scoring?style=social)|
|[allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model)|[![Downloads](https://static.pepy.tech/badge/allennlp-shiba/week)](https://pepy.tech/project/allennlp-shiba)|[![Downloads](https://static.pepy.tech/badge/allennlp-shiba)](https://pepy.tech/project/allennlp-shiba)|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/allennlp-shiba-model?style=social)|
|[evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/evaluate_japanese_w2v?style=social)|
|[gector-ja](https://github.com/jonnyli1125/gector-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jonnyli1125/gector-ja?style=social)|
|[Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-BPEEncoder?style=social)|
|[Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-BPEEncoder_V2?style=social)|
|[transformer-copy](https://github.com/youichiro/transformer-copy)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/youichiro/transformer-copy?style=social)|
|[japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-stable-diffusion?style=social)|
|[nagisa_bert](https://github.com/taishi-i/nagisa_bert)|[![Downloads](https://static.pepy.tech/badge/nagisa_bert/week)](https://pepy.tech/project/nagisa_bert)|[![Downloads](https://static.pepy.tech/badge/nagisa_bert)](https://pepy.tech/project/nagisa_bert)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/nagisa_bert?style=social)|
|[prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/prefix-tuning-gpt?style=social)|
|[JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nobu-g/JGLUE-benchmark?style=social)|
|[jptranstokenizer](https://github.com/retarfi/jptranstokenizer)|[![Downloads](https://static.pepy.tech/badge/jptranstokenizer/week)](https://pepy.tech/project/jptranstokenizer)|[![Downloads](https://static.pepy.tech/badge/jptranstokenizer)](https://pepy.tech/project/jptranstokenizer)|![GitHub Repo stars](https://img.shields.io/github/stars/retarfi/jptranstokenizer?style=social)|
|[jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Stability-AI/lm-evaluation-harness?style=social)|
|[compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hitachi-nlp/compare-ja-tokenizer?style=social)|
|[lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tdc-yamada-ya/lm-evaluation-harness-jp-stable?style=social)|
|[llm-lora-classification](https://github.com/hppRC/llm-lora-classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/llm-lora-classification?style=social)|
|[jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Stability-AI/lm-evaluation-harness?style=social)|
|[rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yukaryavka/rinna_gpt-neox_ggml-lora?style=social)|
|[japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/oshizo/japanese-llm-roleplay-benchmark?style=social)|
|[japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuzu-ai/japanese-llm-ranking?style=social)|
|[llm-jp-eval](https://github.com/llm-jp/llm-jp-eval)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/llm-jp/llm-jp-eval?style=social)|
|[llm-jp-sft](https://github.com/llm-jp/llm-jp-sft)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/llm-jp/llm-jp-sft?style=social)|
|[llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/llm-jp/llm-jp-tokenizer?style=social)|
|[japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/pfnet-research/japanese-lm-fin-harness?style=social)|
|[ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/ja-vicuna-qa-benchmark?style=social)|


### Others

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - 一個將日本全名分為姓氏和名字的工具。
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - 一個精選的資源清單，專門為日語自然語言處理的Python庫而設。
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - Python版日本語意味角色賦予系統（ASA）
 * [toiro](https://github.com/taishi-i/toiro) - 日本語分詞器比較工具
 * [ja-timex](https://github.com/yagays/ja-timex) - 基於規則的解析器，用於提取/規範自然語言中的時間信息表達。
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - 從文本數據中選擇特徵的一組度量標準
 * [daaja](https://github.com/kajyuuen/daaja) - 這個存儲庫包含了針對日語自然語言處理的數據增強實現。
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - 這個存儲庫的目的是在概念證明（PoC）和研究開發（R＆D）的背景下製作原型作為案例研究，這些案例研究已經在我的網站上寫出來。主要研究主題是與表示學習相關的自動編碼器，基於能量模型的統計機器學習，對抗生成網絡...
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - 一個用於KyotoCorpus、KWDLC和AnnotatedFKCCorpus的處理器
 * [nlplot](https://github.com/takapy0210/nlplot) - 自然語言處理的可視化模組
 * [rake-ja](https://github.com/kanjirz50/rake-ja) - 日語快速自動關鍵詞提取演算法
 * [jel](https://github.com/izuna385/jel) - 日本實體連結器。
 * [MedNER-J](https://github.com/sociocom/MedNER-J) - 最新版本的MedEX/J（日本疾病名稱提取器）
 * [zunda-python](https://github.com/ikegami-yukino/zunda-python) - Zunda：Python 的日本增強型情態分析器客戶端。
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/ 

https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
 * [showcase](https://github.com/cl-tohoku/showcase) - 一個PyTorch實現的日本述語-參數結構（PAS）分析器，該分析器在Matsubayashi＆Inui（2018）的論文中提出，並進行了一些改進。
 * [darts-clone-python](https://github.com/rixwew/darts-clone-python) - 飛鏢克隆 Python 綁定
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - 日本寫實文本蘊含語料庫的範例代碼
 * [desuwa](https://github.com/megagonlabs/desuwa) - 基於KNP規則文件的特徵標註器，可將單詞和詞組轉換為形態素（純Python）
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - 通過日語對話的餐廳搜索系統。
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - 日語自然語言處理的樣本程式碼
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - 在Python中處理日文文本的小例子腳本
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - DNorm的日文版本
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - EventGraph是一個針對高階日語自然語言處理應用的開發平台。
 * [ishi](https://github.com/ku-nlp/ishi) - 石：日語意志分類器
 * [python-npylm](https://github.com/musyoku/python-npylm) - 利用貝葉斯階層語言模型進行無監督詞素分析
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - 條件付機率場和貝葉斯階層語言模型的整合，實現半監督形態素分析。
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - 教師無品詞標記推斷
 * [negima](https://github.com/cocodrips/negima) - Negima是一個Python套件，可以通過使用您定義的基於詞性的規則來提取日文文本中的短語。
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - 使用BertSum作為摘要模型的提取式摘要器
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - 一個自然語言中的日本數字（漢字、阿拉伯數字）解析器。
 * [kantan](https://github.com/itayperl/kantan) - 按部首模式查找日語單詞
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - 獲取日語對話語料庫
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - 日本文章摘要器。
 * [chirptext](https://github.com/letuananh/chirptext) - ChirpText 是一個針對 Python 的文本處理工具集合。
 * [yubin](https://github.com/alvations/yubin) - 日本地址 Munger
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - 日本維基百科清潔工具
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - 一個將日文轉換為音素的Python庫。
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - 這個存儲庫包含與“基於情感的文本分類的日語分詞器的實驗評估”相關的代碼。
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - 關於
This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - 從青空文庫生成純文本或標記化文本文件
 * [JLM](https://github.com/jiali-ms/JLM) - 一個快速的LSTM語言模型，適用於日語和中文等大詞彙語言。
 * [NTM](https://github.com/m3yrin/NTM) - 日本文章的神經主題建模測試
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - 這是一個機器學習和深度學習術語的英日詞彙表。
 * [text-generation](https://github.com/discus0434/text-generation) - 易於使用的腳本，可調整GPT-2-JA與您自己的文本，生成句子並自動發推文。
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - 在Chainer上的神經圖像標題（NIC），其預訓練模型適用於英語和日語圖像標題數據集。
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - 「UnihanLM：使用Unihan數據庫進行粗到細的中日語言模型預訓練」的官方存儲庫，AACL-IJCNLP 2020
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - 執行 mBART 模型微調的程式碼。
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - 在jtubespeech上的xvector模型
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - 自製TinySegmenter學習模型的工具。
 * [Grongish](https://github.com/shogo82148/Grongish) - 日本語和格隆基語的相互轉換腳本
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - 使用WordCloud製作日文文章的腳本，實現形態素解析式的顯示，不需使用Mecab（形態素解析引擎）。
 * [snark](https://github.com/hiraokusky/snark) - 利用日本語詞彙網路的資料庫存取程式庫
 * [toEmoji](https://github.com/mkan0141/toEmoji) - 將日文轉換為僅由表情符號組成的文本的工具
 * [termextract](https://github.com/kanjirz50/termextract) - - 專門用語抽出演算法的實現練習
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - 對於Japanese-Dialog-Transformer的回應候選，使用KenLM的N-gram語言模型進行評分，進行過濾或重新排序。
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - Python中的混合Unigram模型和无限混合Unigram模型。 (混合單詞模型和無限混合單詞模型在Python中。)
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - Python中的隱藏馬可夫模型（HMM）和無限隱藏馬可夫模型（iHMM）。
 * [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) - Python中的Ngram語言模型。 (N-gram語言模型)
 * [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) - 使用PyTorch中的deepspeech2模型和Zakuro AI的支援進行自動語音識別。
 * [neural_ime](https://github.com/yohokuno/neural_ime) - 神經輸入法引擎：神經輸入法引擎
 * [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) - 神經網路能正確地將羅馬字轉寫成日文嗎？
 * [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) - 針對日語指定的分詞器
 * [AugLy-jp](https://github.com/chck/AugLy-jp) - 在AugLy上進行日文文本的數據增強
 * [furigana4epub](https://github.com/Mumumu4/furigana4epub) - 一個使用Mecab和Unidic將振仮名添加到日語epub書籍的Python腳本。
 * [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) - 日語動詞/形容詞變化工具
 * [jageocoder](https://github.com/t-sagara/jageocoder) - 純Python日本地址地理編碼器
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp，一個用於對日文文本進行地理標記的Python模塊。
 * [nksnd](https://github.com/yoriyuki/nksnd) - 新的假名漢字轉換引擎
 * [JaMIE](https://github.com/racerandom/JaMIE) - 一個日本醫學信息提取工具箱
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - 這是有關 fasttext 和 word2vec 的比較，以及執行腳本和學習腳本。
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - 最小的搜尋引擎/PageRank/tf-idf
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - 利用網路爬蟲技術，對5ch的歷史紀錄進行擷取，追蹤調查過去流行的詞語（例如：香具師、orz等）。
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - Twitter日語評價分析資料集的推文下載器
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - 基於Juman++和ConceptNet5.5的日語詞匯聚合
 * [jinf](https://github.com/hkiyomaru/jinf) - 一個日語變化轉換器
 * [kwja](https://github.com/ku-nlp/kwja) - 一個統一的日語語言分析器
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - 基於遮蔽語言模型評分的複製套件（ACL2020）。
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - [PyTorch] 日語 ClipCap
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - [PyTorch] 展示、關注和講述日語
 * [cihai](https://github.com/cihai/cihai) - Python CJK（中文、日文、韓文）語言字典庫
 * [marine](https://github.com/6gsn/marine) - MARINE：基於多任務學習的日語口音估計
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - 微調Whisper ASR模型
 * [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) - 使用BERT和Transformer解碼器的日語聊天機器人的PyTorch實現
 * [radicalchar](https://github.com/yamamaya/radicalchar) - 部首文字正規化程式庫
 * [akaza](https://github.com/tokuhirom/akaza) - 又一個針對IBus/Linux的日文輸入法
 * [posuto](https://github.com/polm/posuto) - 日本郵遞區號資料。
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - Tacotron2 日語實現
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - IBus 平假名輸入法
 * [furiganapad](https://github.com/esrille/furiganapad) - 注音輸入板
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - 日語同義詞庫
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - Mecab + NEologd + Docker + Python3
Mecab + NEologd + Docker + Python3
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - 日本嵌入評估
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPT會當YouTuber
 * [shuwa](https://github.com/google/shuwa) - 擴展 GNOME 螢幕鍵盤以支援輸入法
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - 這個存儲庫提供了日語NLI模型的代碼，一個經過微調的遮蔽語言模型。
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - 使用FuguMT進行日英翻譯和英日翻譯的工具
 * [fugumt](https://github.com/s-taka/fugumt) - 這是一個使用在ぷるーふおぶこんせぷと上公開的機器翻譯引擎的翻譯環境。可以翻譯輸入在表格中的文字，以及 PDF 文件的翻譯。
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - JaSPICE：使用謂詞-參數結構自動評估圖像標題模型的評估指標
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - 日本本地化
 * [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) - Python 封裝 OpenJTalk
 * [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) - 在電子書中為每個漢字添加讀音，讓學習日語更容易。
 * [N46Whisper](https://github.com/Ayanaminn/N46Whisper) - 基於耳語的日文字幕生成器
 * [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) - Rinna-3.6B、OpenCALM等的日本語對應LLM(大規模言語模型)用的簡易Web介面是。
 * [pdf-translator](https://github.com/discus0434/pdf-translator) - pdf-translator 將英文 PDF 檔案翻譯成日文，並保留原始的版面配置。
 * [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) - 使用Haystack + Elasticsearch + wikipedia(ja)構建的日語問答系統的示例
 * [mozc-devices](https://github.com/google/mozc-devices) - 自動從code.google.com/p/mozc-morse匯出
 * [natsume](https://github.com/faruzan0820/natsume) - 一個日文文本前端處理工具包
 * [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) - 日本語TTS（VITS）的學習和音訊合成的Gradio WebUI
日本語TTS（VITS）的學習和音訊合成的Gradio WebUI
 * [ja-law-parser](https://github.com/takuyaa/ja-law-parser) - 一個日本法律解析器
 * [dictation-kit](https://github.com/julius-speech/dictation-kit) - 使用Julius的日語口述套件
 * [julius4seg](https://github.com/Hiroshiba/julius4seg) - 使用Julius的分割支援工具
 * [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) - 免費使用的中等品質文字朗讀軟體，VOICEVOX的語音合成引擎
 * [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) - LLaVA-JP 是一個由 LLaVA 方法訓練的日本 VLM。
 * [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) - 用於低資源環境下的日本LLM的開源RAG與Llama指數
 * [bertjsc](https://github.com/er-ri/bertjsc) - 使用BERT（遮罩語言模型）的日語拼寫錯誤修正器。基於BERT的日語校正。
 * [llm-leaderboard](https://github.com/wandb/llm-leaderboard) - 日本任務的llm評估項目
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - 關於JGLUE的培訓和評估腳本，這是一個日語理解基準的項目。
Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - 使用在日本數據集上預訓練的模型，修改LAVIS的BLIP2 Q-former。
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - 將維基百科的日文句子轉換為各種日文嵌入和faiss索引的腳本等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - 探索日本SimCSE


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namedivider-python](https://github.com/rskmoi/namedivider-python)|[![Downloads](https://static.pepy.tech/badge/namedivider-python/week)](https://pepy.tech/project/namedivider-python)|[![Downloads](https://static.pepy.tech/badge/namedivider-python)](https://pepy.tech/project/namedivider-python)|![GitHub Repo stars](https://img.shields.io/github/stars/rskmoi/namedivider-python?style=social)|
|[asa-python](https://github.com/ikegami-yukino/asa-python)|[![Downloads](https://static.pepy.tech/badge/asa/week)](https://pepy.tech/project/asa)|[![Downloads](https://static.pepy.tech/badge/asa)](https://pepy.tech/project/asa)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/asa-python?style=social)|
|[python_asa](https://github.com/Takeuchi-Lab-LM/python_asa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Takeuchi-Lab-LM/python_asa?style=social)|
|[toiro](https://github.com/taishi-i/toiro)|[![Downloads](https://static.pepy.tech/badge/toiro/week)](https://pepy.tech/project/toiro)|[![Downloads](https://static.pepy.tech/badge/toiro)](https://pepy.tech/project/toiro)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/toiro?style=social)|
|[ja-timex](https://github.com/yagays/ja-timex)|[![Downloads](https://static.pepy.tech/badge/ja-timex/week)](https://pepy.tech/project/ja-timex)|[![Downloads](https://static.pepy.tech/badge/ja-timex)](https://pepy.tech/project/ja-timex)|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/ja-timex?style=social)|
|[JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Kensuke-Mitsuzawa/JapaneseTokenizers?style=social)|
|[daaja](https://github.com/kajyuuen/daaja)|[![Downloads](https://static.pepy.tech/badge/daaja/week)](https://pepy.tech/project/daaja)|[![Downloads](https://static.pepy.tech/badge/daaja)](https://pepy.tech/project/daaja)|![GitHub Repo stars](https://img.shields.io/github/stars/kajyuuen/daaja?style=social)|
|[accel-brain-code](https://github.com/accel-brain/accel-brain-code)|[![Downloads](https://static.pepy.tech/badge/pysummarization/week)](https://pepy.tech/project/pysummarization)|[![Downloads](https://static.pepy.tech/badge/pysummarization)](https://pepy.tech/project/pysummarization)|![GitHub Repo stars](https://img.shields.io/github/stars/accel-brain/accel-brain-code?style=social)|
|[JGLUE](https://github.com/yahoojapan/JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yahoojapan/JGLUE?style=social)|
|[kyoto-reader](https://github.com/ku-nlp/kyoto-reader)|[![Downloads](https://static.pepy.tech/badge/kyoto-reader/week)](https://pepy.tech/project/kyoto-reader)|[![Downloads](https://static.pepy.tech/badge/kyoto-reader)](https://pepy.tech/project/kyoto-reader)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/kyoto-reader?style=social)|
|[nlplot](https://github.com/takapy0210/nlplot)|[![Downloads](https://static.pepy.tech/badge/nlplot/week)](https://pepy.tech/project/nlplot)|[![Downloads](https://static.pepy.tech/badge/nlplot)](https://pepy.tech/project/nlplot)|![GitHub Repo stars](https://img.shields.io/github/stars/takapy0210/nlplot?style=social)|
|[rake-ja](https://github.com/kanjirz50/rake-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kanjirz50/rake-ja?style=social)|
|[jel](https://github.com/izuna385/jel)|[![Downloads](https://static.pepy.tech/badge/jel/week)](https://pepy.tech/project/jel)|[![Downloads](https://static.pepy.tech/badge/jel)](https://pepy.tech/project/jel)|![GitHub Repo stars](https://img.shields.io/github/stars/izuna385/jel?style=social)|
|[MedNER-J](https://github.com/sociocom/MedNER-J)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/MedNER-J?style=social)|
|[zunda-python](https://github.com/ikegami-yukino/zunda-python)|[![Downloads](https://static.pepy.tech/badge/zunda-python/week)](https://pepy.tech/project/zunda-python)|[![Downloads](https://static.pepy.tech/badge/zunda-python)](https://pepy.tech/project/zunda-python)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/zunda-python?style=social)|
|[AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/AIO2_DPR_baseline?style=social)|
|[showcase](https://github.com/cl-tohoku/showcase)|[![Downloads](https://static.pepy.tech/badge/showcase-parser/week)](https://pepy.tech/project/showcase-parser)|[![Downloads](https://static.pepy.tech/badge/showcase-parser)](https://pepy.tech/project/showcase-parser)|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/showcase?style=social)|
|[darts-clone-python](https://github.com/rixwew/darts-clone-python)|[![Downloads](https://static.pepy.tech/badge/dartsclone/week)](https://pepy.tech/project/dartsclone)|[![Downloads](https://static.pepy.tech/badge/dartsclone)](https://pepy.tech/project/dartsclone)|![GitHub Repo stars](https://img.shields.io/github/stars/rixwew/darts-clone-python?style=social)|
|[jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/jrte-corpus_example?style=social)|
|[desuwa](https://github.com/megagonlabs/desuwa)|[![Downloads](https://static.pepy.tech/badge/desuwa/week)](https://pepy.tech/project/desuwa)|[![Downloads](https://static.pepy.tech/badge/desuwa)](https://pepy.tech/project/desuwa)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/desuwa?style=social)|
|[HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/HotPepperGourmetDialogue?style=social)|
|[nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/upura/nlp-recipes-ja?style=social)|
|[Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/olsgaard/Japanese_nlp_scripts?style=social)|
|[DNorm-J](https://github.com/sociocom/DNorm-J)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/DNorm-J?style=social)|
|[pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph)|[![Downloads](https://static.pepy.tech/badge/pyknp-eventgraph/week)](https://pepy.tech/project/pyknp-eventgraph)|[![Downloads](https://static.pepy.tech/badge/pyknp-eventgraph)](https://pepy.tech/project/pyknp-eventgraph)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/pyknp-eventgraph?style=social)|
|[ishi](https://github.com/ku-nlp/ishi)|[![Downloads](https://static.pepy.tech/badge/ishi/week)](https://pepy.tech/project/ishi)|[![Downloads](https://static.pepy.tech/badge/ishi)](https://pepy.tech/project/ishi)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/ishi?style=social)|
|[python-npylm](https://github.com/musyoku/python-npylm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/python-npylm?style=social)|
|[python-npycrf](https://github.com/musyoku/python-npycrf)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/python-npycrf?style=social)|
|[unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/unsupervised-pos-tagging?style=social)|
|[negima](https://github.com/cocodrips/negima)|[![Downloads](https://static.pepy.tech/badge/negima/week)](https://pepy.tech/project/negima)|[![Downloads](https://static.pepy.tech/badge/negima)](https://pepy.tech/project/negima)|![GitHub Repo stars](https://img.shields.io/github/stars/cocodrips/negima?style=social)|
|[YouyakuMan](https://github.com/neilctwu/YouyakuMan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neilctwu/YouyakuMan?style=social)|
|[japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python)|[![Downloads](https://static.pepy.tech/badge/japanese-numbers-python/week)](https://pepy.tech/project/japanese-numbers-python)|[![Downloads](https://static.pepy.tech/badge/japanese-numbers-python)](https://pepy.tech/project/japanese-numbers-python)|![GitHub Repo stars](https://img.shields.io/github/stars/takumakanari/japanese-numbers-python?style=social)|
|[kantan](https://github.com/itayperl/kantan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/itayperl/kantan?style=social)|
|[make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/knok/make-meidai-dialogue?style=social)|
|[japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ryuryukke/japanese_summarizer?style=social)|
|[chirptext](https://github.com/letuananh/chirptext)|[![Downloads](https://static.pepy.tech/badge/chirptext/week)](https://pepy.tech/project/chirptext)|[![Downloads](https://static.pepy.tech/badge/chirptext)](https://pepy.tech/project/chirptext)|![GitHub Repo stars](https://img.shields.io/github/stars/letuananh/chirptext?style=social)|
|[yubin](https://github.com/alvations/yubin)|[![Downloads](https://static.pepy.tech/badge/yubin/week)](https://pepy.tech/project/yubin)|[![Downloads](https://static.pepy.tech/badge/yubin)](https://pepy.tech/project/yubin)|![GitHub Repo stars](https://img.shields.io/github/stars/alvations/yubin?style=social)|
|[jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner)|[![Downloads](https://static.pepy.tech/badge/jawiki-cleaner/week)](https://pepy.tech/project/jawiki-cleaner)|[![Downloads](https://static.pepy.tech/badge/jawiki-cleaner)](https://pepy.tech/project/jawiki-cleaner)|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/jawiki-cleaner?style=social)|
|[japanese2phoneme](https://github.com/iory/japanese2phoneme)|[![Downloads](https://static.pepy.tech/badge/japanese2phoneme/week)](https://pepy.tech/project/japanese2phoneme)|[![Downloads](https://static.pepy.tech/badge/japanese2phoneme)](https://pepy.tech/project/japanese2phoneme)|![GitHub Repo stars](https://img.shields.io/github/stars/iory/japanese2phoneme?style=social)
|[anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/arusl/anlp_nlp2021_d3-1?style=social)|
|[aozora_classification](https://github.com/shibuiwilliam/aozora_classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shibuiwilliam/aozora_classification?style=social)|
|[aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/borh/aozora-corpus-generator?style=social)|
|[JLM](https://github.com/jiali-ms/JLM)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jiali-ms/JLM?style=social)|
|[NTM](https://github.com/m3yrin/NTM)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/m3yrin/NTM?style=social)|
|[EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Machine-Learning-Tokyo/EN-JP-ML-Lexicon?style=social)|
|[text-generation](https://github.com/discus0434/text-generation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/discus0434/text-generation?style=social)|
|[chainer_nic](https://github.com/yuyay/chainer_nic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuyay/chainer_nic?style=social)|
|[unihan-lm](https://github.com/JetRunner/unihan-lm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/JetRunner/unihan-lm?style=social)|
|[mbart-finetuning](https://github.com/ken11/mbart-finetuning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/mbart-finetuning?style=social)|
|[xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarulab-speech/xvector_jtubespeech?style=social)|
|[TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shogo82148/TinySegmenterMaker?style=social)|
|[Grongish](https://github.com/shogo82148/Grongish)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shogo82148/Grongish?style=social)|
|[WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aocattleya/WordCloud-Japanese?style=social)|
|[snark](https://github.com/hiraokusky/snark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hiraokusky/snark?style=social)|
|[toEmoji](https://github.com/mkan0141/toEmoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mkan0141/toEmoji?style=social)|
|[termextract](https://github.com/kanjirz50/termextract)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kanjirz50/termextract?style=social)|
|[JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/TUT-SLP-lab/JDT-with-KenLM-scoring?style=social)|
|[mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KentoW/mixture-of-unigram-model?style=social)|
|[hidden-markov-model](https://github.com/KentoW/hidden-markov-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KentoW/hidden-markov-model?style=social)|
|[Ngram-language-model](https://github.com/KentoW/Ngram-language-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KentoW/Ngram-language-model?style=social)|
|[ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/JeanMaximilienCadic/ASRDeepSpeech?style=social)|
|[neural_ime](https://github.com/yohokuno/neural_ime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yohokuno/neural_ime?style=social)|
|[neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Kyubyong/neural_japanese_transliterator?style=social)|
|[tinysegmenter](https://github.com/SamuraiT/tinysegmenter)|[![Downloads](https://static.pepy.tech/badge/tinysegmenter/week)](https://pepy.tech/project/tinysegmenter3)|[![Downloads](https://static.pepy.tech/badge/tinysegmenter3)](https://pepy.tech/project/tinysegmenter3)|![GitHub Repo stars](https://img.shields.io/github/stars/SamuraiT/tinysegmenter3?style=social)|
|[AugLy-jp](https://github.com/chck/AugLy-jp)|[![Downloads](https://static.pepy.tech/badge/AugLy-jp/week)](https://pepy.tech/project/AugLy-jp)|[![Downloads](https://static.pepy.tech/badge/AugLy-jp)](https://pepy.tech/project/AugLy-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/chck/AugLy-jp?style=social)|
|[furigana4epub](https://github.com/Mumumu4/furigana4epub)|[![Downloads](https://static.pepy.tech/badge/furigana4epub/week)](https://pepy.tech/project/furigana4epub)|[![Downloads](https://static.pepy.tech/badge/furigana4epub)](https://pepy.tech/project/furigana4epub)|![GitHub Repo stars](https://img.shields.io/github/stars/Mumumu4/furigana4epub?style=social)|
|[PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou)|[![Downloads](https://static.pepy.tech/badge/PyKatsuyou/week)](https://pepy.tech/project/PyKatsuyou)|[![Downloads](https://static.pepy.tech/badge/PyKatsuyou)](https://pepy.tech/project/PyKatsuyou)|![GitHub Repo stars](https://img.shields.io/github/stars/SmashinFries/PyKatsuyou?style=social)|
|[jageocoder](https://github.com/t-sagara/jageocoder)|[![Downloads](https://static.pepy.tech/badge/jageocoder/week)](https://pepy.tech/project/jageocoder)|[![Downloads](https://static.pepy.tech/badge/jageocoder)](https://pepy.tech/project/jageocoder)|![GitHub Repo stars](https://img.shields.io/github/stars/t-sagara/jageocoder?style=social)|
|[pygeonlp](https://github.com/geonlp-platform/pygeonlp)|[![Downloads](https://static.pepy.tech/badge/pygeonlp/week)](https://pepy.tech/project/pygeonlp)|[![Downloads](https://static.pepy.tech/badge/pygeonlp)](https://pepy.tech/project/pygeonlp)|![GitHub Repo stars](https://img.shields.io/github/stars/geonlp-platform/pygeonlp?style=social)|
|[nksnd](https://github.com/yoriyuki/nksnd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yoriyuki/nksnd?style=social)|
|[JaMIE](https://github.com/racerandom/JaMIE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/racerandom/JaMIE?style=social)|
|[fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/fasttext-vs-word2vec-on-twitter-data?style=social)|
|[minimal-search-engine](https://github.com/GINK03/minimal-search-engine)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/minimal-search-engine?style=social)|
|[5ch-analysis](https://github.com/GINK03/5ch-analysis)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/5ch-analysis?style=social)|
|[tweet_extructor](https://github.com/tatHi/tweet_extructor)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tatHi/tweet_extructor?style=social)|
|[japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/japanese-word-aggregation?style=social)|
|[jinf](https://github.com/hkiyomaru/jinf)|[![Downloads](https://static.pepy.tech/badge/jinf/week)](https://pepy.tech/project/jinf)|[![Downloads](https://static.pepy.tech/badge/jinf)](https://pepy.tech/project/jinf)|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/jinf?style=social)|
|[kwja](https://github.com/ku-nlp/kwja)|[![Downloads](https://static.pepy.tech/badge/kwja/week)](https://pepy.tech/project/kwja)|[![Downloads](https://static.pepy.tech/badge/kwja)](https://pepy.tech/project/kwja)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/kwja?style=social)|
|[mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Ryutaro-A/mlm-scoring-transformers?style=social)|
|[ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Japanese-Image-Captioning/ClipCap-for-Japanese?style=social)|
|[SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Japanese-Image-Captioning/SAT-for-Japanese?style=social)|
|[cihai](https://github.com/cihai/cihai)|[![Downloads](https://static.pepy.tech/badge/cihai/week)](https://pepy.tech/project/cihai)|[![Downloads](https://static.pepy.tech/badge/cihai)](https://pepy.tech/project/cihai)|![GitHub Repo stars](https://img.shields.io/github/stars/cihai/cihai?style=social)|
|[marine](https://github.com/6gsn/marine)|[![Downloads](https://static.pepy.tech/badge/marine/week)](https://pepy.tech/project/marine)|[![Downloads](https://static.pepy.tech/badge/marine)](https://pepy.tech/project/marine)|![GitHub Repo stars](https://img.shields.io/github/stars/6gsn/marine?style=social)|
|[whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarulab-speech/whisper-asr-finetune?style=social)|
|[japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CjangCjengh/japanese_chatbot?style=social)|
|[radicalchar](https://github.com/yamamaya/radicalchar)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yamamaya/radicalchar?style=social)|
|[akaza](https://github.com/tokuhirom/akaza)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tokuhirom/akaza?style=social)|
|[posuto](https://github.com/polm/posuto)|[![Downloads](https://static.pepy.tech/badge/posuto/week)](https://pepy.tech/project/posuto)|[![Downloads](https://static.pepy.tech/badge/posuto)](https://pepy.tech/project/posuto)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/posuto?style=social)|
|[tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CjangCjengh/tacotron2-japanese?style=social)|
|[ibus-hiragana](https://github.com/esrille/ibus-hiragana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/ibus-hiragana?style=social)|
|[furiganapad](https://github.com/esrille/furiganapad)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/furiganapad?style=social)|
|[chikkarpy](https://github.com/WorksApplications/chikkarpy)|[![Downloads](https://static.pepy.tech/badge/chikkarpy/week)](https://pepy.tech/project/chikkarpy)|[![Downloads](https://static.pepy.tech/badge/chikkarpy)](https://pepy.tech/project/chikkarpy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/chikkarpy?style=social)|
|[ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/p-geon/ja-tokenizer-docker-py?style=social)|
|[JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/oshizo/JapaneseEmbeddingEval?style=social)|
|[gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/karakuri-ai/gptuber-by-langchain?style=social)|
|[shuwa](https://github.com/google/shuwa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/shuwa?style=social)|
|[japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CyberAgentAILab/japanese-nli-model?style=social)|
|[tra-fugu](https://github.com/tos-kamiya/tra-fugu)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tos-kamiya/tra-fugu?style=social)|
|[fugumt](https://github.com/s-taka/fugumt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/s-taka/fugumt?style=social)|
|[JaSPICE](https://github.com/keio-smilab23/JaSPICE)|[![Downloads](https://static.pepy.tech/badge/JaSPICE/week)](https://pepy.tech/project/JaSPICE)|[![Downloads](https://static.pepy.tech/badge/JaSPICE)](https://pepy.tech/project/JaSPICE)|![GitHub Repo stars](https://img.shields.io/github/stars/keio-smilab23/JaSPICE?style=social)|
|[Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization?style=social)|
|[pyopenjtalk](https://github.com/r9y9/pyopenjtalk)|[![Downloads](https://static.pepy.tech/badge/pyopenjtalk/week)](https://pepy.tech/project/pyopenjtalk)|[![Downloads](https://static.pepy.tech/badge/pyopenjtalk)](https://pepy.tech/project/pyopenjtalk)|![GitHub Repo stars](https://img.shields.io/github/stars/r9y9/pyopenjtalk?style=social)|
|[yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook)|[![Downloads](https://static.pepy.tech/badge/yomigana-ebook/week)](https://pepy.tech/project/yomigana-ebook)|[![Downloads](https://static.pepy.tech/badge/yomigana-ebook)](https://pepy.tech/project/yomigana-ebook)|![GitHub Repo stars](https://img.shields.io/github/stars/rabbit19981023/yomigana-ebook?style=social)|
|[N46Whisper](https://github.com/Ayanaminn/N46Whisper)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Ayanaminn/N46Whisper?style=social)|
|[japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/noir55/japanese_llm_simple_webui?style=social)|
|[pdf-translator](https://github.com/discus0434/pdf-translator)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/discus0434/pdf-translator?style=social)|
|[japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es?style=social)|
|[mozc-devices](https://github.com/google/mozc-devices)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/mozc-devices?style=social)|
|[natsume](https://github.com/faruzan0820/natsume)|[![Downloads](https://pepy.tech/badge/natsume/week)](https://pepy.tech/project/natsume)|[![Downloads](https://pepy.tech/badge/natsume)](https://pepy.tech/project/natsume)|![GitHub Repo stars](https://img.shields.io/github/stars/faruzan0820/natsume?style=social)|
|[vits-japros-webui](https://github.com/litagin02/vits-japros-webui)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/litagin02/vits-japros-webui?style=social)|
|[ja-law-parser](https://github.com/takuyaa/ja-law-parser)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/ja-law-parser?style=social)|
|[dictation-kit](https://github.com/julius-speech/dictation-kit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/julius-speech/dictation-kit?style=social)|
|[julius4seg](https://github.com/Hiroshiba/julius4seg)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hiroshiba/julius4seg?style=social)|
|[voicevox_engine](https://github.com/VOICEVOX/voicevox_engine)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/VOICEVOX/voicevox_engine?style=social)|
|[LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tosiyuki/LLaVA-JP?style=social)|
|[RAG-Japanese](https://github.com/AkimParis/RAG-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/AkimParis/RAG-Japanese?style=social)|
|[bertjsc](https://github.com/er-ri/bertjsc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/er-ri/bertjsc?style=social)|
|[llm-leaderboard](https://github.com/wandb/llm-leaderboard)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wandb/llm-leaderboard?style=social)|
|[jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nobu-g/jglue-evaluation-scripts?style=social)|
|[BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ZhaoPeiduo/BLIP2-Japanese?style=social)|
|[wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hotchpotch/wikipedia-passages-jawiki-embeddings-utils?style=social)|
|[simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hpprc/simple-simcse-ja?style=social)|


## C++

### Morphology analysis

 * [mecab](https://github.com/taku910/mecab) - 又一個日本語形態分析器
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++（一個形態學分析工具包）
 * [kytea](https://github.com/neubig/kytea) - 京都文本分析工具箱，可用於詞語分割和發音估計等。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab](https://github.com/taku910/mecab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/mecab?style=social)|
|[jumanpp](https://github.com/ku-nlp/jumanpp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/jumanpp?style=social)|
|[kytea](https://github.com/neubig/kytea)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neubig/kytea?style=social)|

### Parsing

 * [cabocha](https://github.com/taku910/cabocha) - 另一個日本依存結構分析器
 * [knp](https://github.com/ku-nlp/knp) - 一個日語解析器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[cabocha](https://github.com/taku910/cabocha)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/cabocha?style=social)|
|[knp](https://github.com/ku-nlp/knp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/knp?style=social)|

### Others

 * [jsc](https://github.com/yohokuno/jsc) - 日文假名漢字轉換、中文拼音輸入和CJE混合輸入的聯合源通道模型。
 * [aquaskk](https://github.com/codefirst/aquaskk) - 沒有形態學分析的輸入法。
 * [mozc](https://github.com/google/mozc) - Mozc - 一款為多平台設計的日本輸入法編輯器
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch：一個（精確|前綴|近似）字串匹配庫
 * [resembla](https://github.com/tuem/resembla) - Resembla：基於單詞的日語相似句子搜索庫
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ Windows 的 SKK-like 日文輸入法編輯器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jsc](https://github.com/yohokuno/jsc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yohokuno/jsc?style=social)|
|[aquaskk](https://github.com/codefirst/aquaskk)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/codefirst/aquaskk?style=social)|
|[mozc](https://github.com/google/mozc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/mozc?style=social)|
|[trimatch](https://github.com/tuem/trimatch)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/trimatch?style=social)|
|[resembla](https://github.com/tuem/resembla)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/resembla?style=social)|
|[corvusskk](https://github.com/nathancorvussolis/corvusskk)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nathancorvussolis/corvusskk?style=social)|


## Rust crate

### Morphology analysis

 * [lindera](https://github.com/lindera-morphology/lindera) - 一個形態學分析庫。
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto：基於點預測的高速分詞器
 * [goya](https://github.com/Leko/goya) - 用 Rust 寫的日語形態分析
 * [vibrato](https://github.com/daac-tools/vibrato) - 顫音：基於維特比加速的分詞器
 * [yoin](https://github.com/agatan/yoin) - 一個用純 Rust 編寫的日語形態分析器
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 安全的 Rust 綁定，用於 mecab 詞性和形態分析庫。
 * [awabi](https://github.com/nakagami/awabi) - 一個使用mecab字典的形態分析器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[lindera](https://github.com/lindera-morphology/lindera)|-|![Crates.io](https://img.shields.io/crates/d/lindera)|![GitHub Repo stars](https://img.shields.io/github/stars/lindera-morphology/lindera?style=social)|
|[vaporetto](https://github.com/daac-tools/vaporetto)|-|![Crates.io](https://img.shields.io/crates/d/vaporetto)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/vaporetto?style=social)|
|[goya](https://github.com/Leko/goya)|-|![Crates.io](https://img.shields.io/crates/d/goya)|![GitHub Repo stars](https://img.shields.io/github/stars/Leko/goya?style=social)|
|[vibrato](https://github.com/daac-tools/vibrato)|-|![Crates.io](https://img.shields.io/crates/d/vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/vibrato?style=social)|
|[yoin](https://github.com/agatan/yoin)|-|![Crates.io](https://img.shields.io/crates/d/yoin)|![GitHub Repo stars](https://img.shields.io/github/stars/agatan/yoin?style=social)|
|[mecab-rs](https://github.com/tsurai/mecab-rs)|-|![Crates.io](https://img.shields.io/crates/d/mecab)|![GitHub Repo stars](https://img.shields.io/github/stars/tsurai/mecab-rs?style=social)|
|[awabi](https://github.com/nakagami/awabi)|-|![Crates.io](https://img.shields.io/crates/d/awabi)|![GitHub Repo stars](https://img.shields.io/github/stars/nakagami/awabi?style=social)|


### Converter

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 檢查和轉換日文字符（平假名、片假名）和羅馬字的實用程式庫
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 一個 Rust 函式庫，可將日文半角ｶﾅ和全角英數轉換為正常字符。
 * [kana](https://github.com/gbrlsnchs/kana) - [鏡像] CLI 程序，可將羅馬字文本轉寫為平假名或片假名。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[wana_kana_rust](https://github.com/PSeitz/wana_kana_rust)|-|![Crates.io](https://img.shields.io/crates/d/wana_kana)|![GitHub Repo stars](https://img.shields.io/github/stars/PSeitz/wana_kana_rust?style=social)|
|[unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs)|-|![Crates.io](https://img.shields.io/crates/d/unicode-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/gemmarx/unicode-jp-rs?style=social)|
|[kana](https://github.com/gbrlsnchs/kana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gbrlsnchs/kana?style=social)|


### Search engine library

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy. 

林德拉分詞器用於Tantivy。
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - 使用 Vibrato 的 Tantivy 分詞器。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy)|-|![Crates.io](https://img.shields.io/crates/d/lindera-tantivy)|![GitHub Repo stars](https://img.shields.io/github/stars/lindera-morphology/lindera-tantivy?style=social)|
|[tantivy-vibrato](https://github.com/akr4/tantivy-vibrato)|-|![Crates.io](https://img.shields.io/crates/d/tantivy-vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/akr4/tantivy-vibrato?style=social)|


### Others

 * [daachorse](https://github.com/daac-tools/daachorse) - 一個在 Rust 中使用緊湊的雙陣列資料結構實現 Aho-Corasick 算法的快速實現。
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - 以時間和記憶體效率找出所有相似文件的配對
 * [crawdad](https://github.com/daac-tools/crawdad) - 使用字符雙陣列嘗試的自然語言字典的 Rust 函式庫。
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) - 各種分詞器的比較代碼
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - 這裡提供基準工具，用於比較字串匹配的資料結構效能。
 * [vime](https://github.com/algon-320/vime) - 使用Vim作為X11應用程式的輸入法
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - 免費使用的中等質量的文字朗讀軟件，VOICEVOX的核心
 * [akaza](https://github.com/akaza-im/akaza) - 又一個針對IBus/Linux的日文輸入法
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - 一個免費的在線自主托管的多語言日語詞典。
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - Google 日本語輸入用 DvorakJP 羅馬字表 / DvorakJP Roman Table for Google Japanese Input
 * [niinii](https://github.com/Netdex/niinii) - 使用一個日語注釋器來輔助閱讀文本，使用「一覧」。
 * [cskk](https://github.com/naokiri/cskk) - SKK（簡易假名漢字轉換）程式庫
 * [japanki](https://github.com/tysonwu/japanki) - 通過在CLI上進行測驗來學習日語詞彙🇯🇵！
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - 用於文本轉語音應用的日文文本預處理器（OpenJTalk在Rust語言中的重寫）


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[daachorse](https://github.com/daac-tools/daachorse)|-|![Crates.io](https://img.shields.io/crates/d/daachorse)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/daachorse?style=social)|
|[find-simdoc](https://github.com/legalforce-research/find-simdoc)|-|![Crates.io](https://img.shields.io/crates/d/find-simdoc)|![GitHub Repo stars](https://img.shields.io/github/stars/legalforce-research/find-simdoc?style=social)|
|[crawdad](https://github.com/daac-tools/crawdad)|-|![Crates.io](https://img.shields.io/crates/d/crawdad)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/crawdad?style=social)|
|[tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/legalforce-research/tokenizer-speed-bench?style=social)|
|[stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/legalforce-research/stringmatch-bench?style=social)|
|[vime](https://github.com/algon-320/vime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/algon-320/vime?style=social)
|[voicevox_core](https://github.com/VOICEVOX/voicevox_core)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/VOICEVOX/voicevox_core?style=social)|
|[akaza](https://github.com/akaza-im/akaza)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/akaza-im/akaza?style=social)
|[Jotoba](https://github.com/WeDontPanic/Jotoba)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WeDontPanic/Jotoba?style=social)|
|[dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shinespark/dvorakjp-romantable?style=social)|
|[niinii](https://github.com/Netdex/niinii)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Netdex/niinii?style=social)|
|[cskk](https://github.com/naokiri/cskk)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/naokiri/cskk?style=social)|
|[japanki](https://github.com/tysonwu/japanki)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tysonwu/japanki?style=social)|
|[jpreprocess](https://github.com/jpreprocess/jpreprocess)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jpreprocess/jpreprocess?style=social)|


## JavaScript

### Morphology analysis

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日本語形態素解析器的JavaScript實現
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - Rakuten MA - 一款純粹使用 JavaScript 編寫的中日文形態分析器（詞分割器 + 詞性標記器）。
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - 另一個用於 Node.js 的 MeCab 封裝程式
 * [juman-bin](https://github.com/thammin/juman-bin) - 一個可擴展的日本語形態素解析器。日本語形態素解析系統。
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - 使用MeCab的非同步日語形態分析器。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji.js](https://github.com/takuyaa/kuromoji.js)|![npm](https://img.shields.io/npm/dw/kuromoji)|![npm](https://img.shields.io/npm/dt/kuromoji)|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/kuromoji.js?style=social)|
|[rakutenma](https://github.com/rakuten-nlp/rakutenma)|![npm](https://img.shields.io/npm/dw/rakutenma)|![npm](https://img.shields.io/npm/dt/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/rakuten-nlp/rakutenma?style=social)|
|[node-mecab-ya](https://github.com/golbin/mecab-ya)|![npm](https://img.shields.io/npm/dw/mecab-ya)|![npm](https://img.shields.io/npm/dt/mecab-ya)|![GitHub Repo stars](https://img.shields.io/github/stars/golbin/node-mecab-ya?style=social)|
|[juman-bin](https://github.com/thammin/juman-bin)|![npm](https://img.shields.io/npm/dw/juman-bin)|![npm](https://img.shields.io/npm/dt/juman-bin)|![GitHub Repo stars](https://img.shields.io/github/stars/thammin/juman-bin?style=social)|
|[node-mecab-async](https://github.com/hecomi/node-mecab-async)|![npm](https://img.shields.io/npm/dw/mecab-async)|![npm](https://img.shields.io/npm/dt/mecab-async)|![GitHub Repo stars](https://img.shields.io/github/stars/hecomi/node-mecab-async?style=social)|


### Converter

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - 日語語言庫，可將日語句子轉換為平假名、片假名或羅馬字，支持振り仮名和送り仮名模式。
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - Kuroshiro 的 Kuromoji 形態分析器。
 * [hepburn](https://github.com/lovell/hepburn) - 使用 Hepburn 羅馬拼音將日文平假名和片假名轉換為羅馬字的 Node.js 模組。
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - 將日本數字轉換為數字
 * [jslingua](https://github.com/kariminf/jslingua) - 處理文本的Javascript庫：阿拉伯語，日語等。
 * [WanaKana](https://github.com/WaniKani/WanaKana) - JavaScript 庫，用於檢測和轉寫平假名 <--> 片假名 <--> 羅馬字。
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - 將基於羅馬字的日本名字進行標準化和修復常見問題。
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - 製作日本古風文本的實用集合
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - 開源的地址規範化程式庫。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuroshiro](https://github.com/hexenq/kuroshiro)|![npm](https://img.shields.io/npm/dw/kuroshiro)|![npm](https://img.shields.io/npm/dt/kuroshiro)|![GitHub Repo stars](https://img.shields.io/github/stars/hexenq/kuroshiro?style=social)|
|[kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji)|![npm](https://img.shields.io/npm/dw/kuroshiro-analyzer-kuromoji)|![npm](https://img.shields.io/npm/dt/kuroshiro-analyzer-kuromoji)|![GitHub Repo stars](https://img.shields.io/github/stars/hexenq/kuroshiro-analyzer-kuromoji?style=social)|
|[hepburn](https://github.com/lovell/hepburn)|![npm](https://img.shields.io/npm/dw/hepburn)|![npm](https://img.shields.io/npm/dt/hepburn)|![GitHub Repo stars](https://img.shields.io/github/stars/lovell/hepburn?style=social)|
|[japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number)|![npm](https://img.shields.io/npm/dw/japanese-numerals-to-number)|![npm](https://img.shields.io/npm/dt/japanese-numerals-to-number)|![GitHub Repo stars](https://img.shields.io/github/stars/twada/japanese-numerals-to-number?style=social)|
|[jslingua](https://github.com/kariminf/jslingua)|![npm](https://img.shields.io/npm/dw/jslingua)|![npm](https://img.shields.io/npm/dt/jslingua)|![GitHub Repo stars](https://img.shields.io/github/stars/kariminf/jslingua?style=social)|
|[WanaKana](https://github.com/WaniKani/WanaKana)|![npm](https://img.shields.io/npm/dw/wanakana)|![npm](https://img.shields.io/npm/dt/wanakana)|![GitHub Repo stars](https://img.shields.io/github/stars/WaniKani/WanaKana?style=social)|
|[node-romaji-name](https://github.com/jeresig/node-romaji-name)|![npm](https://img.shields.io/npm/dw/romaji-name)|![npm](https://img.shields.io/npm/dt/romaji-name)|![GitHub Repo stars](https://img.shields.io/github/stars/jeresig/node-romaji-name?style=social)|
|[kyujitai.js](https://github.com/hakatashi/kyujitai.js)|![npm](https://img.shields.io/npm/dw/kyujitai)|![npm](https://img.shields.io/npm/dt/kyujitai)|![GitHub Repo stars](https://img.shields.io/github/stars/hakatashi/kyujitai.js?style=social)|
|[normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/geolonia/normalize-japanese-addresses?style=social)|


### Others

 * [bangumi-data](https://github.com/bangumi-data/bangumi-data) - 日本動畫的原始數據
 * [yomichan](https://github.com/FooSoft/yomichan) - Chrome和Firefox的日語彈出詞典擴展。
 * [proofreading-tool](https://github.com/gecko655/proofreading-tool) - GUI工具，用於文本校對。
 * [kanjigrid](https://github.com/minosvasilias/kanjigrid) - 一個網頁應用程式，顯示詹姆斯·海西格《漢字憶起》第六版所教授的2200個漢字。
 * [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) - 單一存儲庫用於漢字、假名、日語數據庫等。
 * [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) - 解析敬體（敬語）和常體（平語）的JavaScript程式庫
 * [hatsuon](https://github.com/DJTB/hatsuon) - 日語音高工具
 * [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) - 使用JavaScript進行日語情感分析，sentiment_ja。
 * [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) - mecab-ipadic種子詞典閱讀器
 * [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) - 每天一個不同的日語單詞。
 * [oskim](https://github.com/esrille/oskim) - 擴展 GNOME 螢幕鍵盤以支援輸入法
 * [tweetMapping](https://github.com/wtnv-lab/tweetMapping) - 這是東日本大地震發生後24小時內帶有地理標籤的推文的數字檔案。
 * [pitch-accent](https://github.com/shirakaba/pitch-accent) - 預測日語的音高重音
 * [kana2ipa](https://github.com/amanoese/kana2ipa) - 將「ひらがな」或「カタカナ」轉換為日語發音時的音標(IPA)的指令
 * [voicevox](https://github.com/VOICEVOX/voicevox) - 免費使用的中等品質文字朗讀軟體，VOICEVOX的編輯器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bangumi-data](https://github.com/bangumi-data/bangumi-data)|![npm](https://img.shields.io/npm/dw/bangumi-data)|![npm](https://img.shields.io/npm/dt/bangumi-data)|![GitHub Repo stars](https://img.shields.io/github/stars/bangumi-data/bangumi-data?style=social)|
|[yomichan](https://github.com/FooSoft/yomichan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/FooSoft/yomichan?style=social)|
|[proofreading-tool](https://github.com/gecko655/proofreading-tool)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gecko655/proofreading-tool?style=social)|
|[kanjigrid](https://github.com/minosvasilias/kanjigrid)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/minosvasilias/kanjigrid?style=social)|
|[japanese-toolkit](https://github.com/echamudi/japanese-toolkit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/echamudi/japanese-toolkit?style=social)|
|[analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu)|![npm](https://img.shields.io/npm/dw/analyze-desumasu-dearu)|![npm](https://img.shields.io/npm/dt/analyze-desumasu-dearu)|![GitHub Repo stars](https://img.shields.io/github/stars/textlint-ja/analyze-desumasu-dearu?style=social)|
|[hatsuon](https://github.com/DJTB/hatsuon)|![npm](https://img.shields.io/npm/dw/hatsuon)|![npm](https://img.shields.io/npm/dt/hatsuon)|![GitHub Repo stars](https://img.shields.io/github/stars/DJTB/hatsuon?style=social)|
|[sentiment_ja_js](https://github.com/otodn/sentiment_ja_js)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/otodn/sentiment_ja_js?style=social)|
|[mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed)|![npm](https://img.shields.io/npm/dw/mecab-ipadic-seed)|![npm](https://img.shields.io/npm/dt/mecab-ipadic-seed)|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/mecab-ipadic-seed?style=social)|
|[Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day)|![npm](https://img.shields.io/npm/dw/japanese-wotd)|![npm](https://img.shields.io/npm/dt/japanese-wotd)|![GitHub Repo stars](https://img.shields.io/github/stars/LuanRT/Japanese-Word-Of-The-Day?style=social)|
|[oskim](https://github.com/esrille/oskim)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/oskim?style=social)|
|[tweetMapping](https://github.com/wtnv-lab/tweetMapping)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wtnv-lab/tweetMapping?style=social)|
|[pitch-accent](https://github.com/shirakaba/pitch-accent)|![npm](https://img.shields.io/npm/dw/pitch-accent)|![npm](https://img.shields.io/npm/dt/pitch-accent)|![GitHub Repo stars](https://img.shields.io/github/stars/shirakaba/pitch-accent?style=social)|
|[kana2ipa](https://github.com/amanoese/kana2ipa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/amanoese/kana2ipa?style=social)|
|[voicevox](https://github.com/VOICEVOX/voicevox)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/VOICEVOX/voicevox?style=social)|


## Go

### Morphology analysis

 * [kagome](https://github.com/ikawaha/kagome) - 純Go編寫的自包含日語形態分析器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kagome](https://github.com/ikawaha/kagome)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikawaha/kagome?style=social)|


### Others

 * [ojosama](https://github.com/jiro4989/ojosama) - 將文字轉換為百滿天原薩洛美小姐風格的口吻。
 * [nihongo](https://github.com/gojp/nihongo) - 日本語詞典
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - Yomichan 的外部詞典導入工具。
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - THE IDOLM@STER 日文輸入法詞彙表（由imas-db.jp提供）
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - 在Go中將漢字音譯為平假名/片假名/羅馬字
將漢字音譯為平假名/片假名/羅馬字，在Go中
 * [go-moji](https://github.com/ktnyt/go-moji) - 一個用於全角/半角轉換的 Go 函式庫
 * [ojichat](https://github.com/greymd/ojichat) - 生成一些看起来像叔叔会通过LINE或邮件发送的文本


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ojosama](https://github.com/jiro4989/ojosama)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jiro4989/ojosama?style=social)|
|[nihongo](https://github.com/gojp/nihongo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gojp/nihongo?style=social)|
|[yomichan-import](https://github.com/FooSoft/yomichan-import)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/FooSoft/yomichan-import?style=social)|
|[imas-ime-dic](https://github.com/maruamyu/imas-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/maruamyu/imas-ime-dic?style=social)|
|[go-kakasi](https://github.com/sarumaj/go-kakasi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarumaj/go-kakasi?style=social)|
|[go-moji](https://github.com/ktnyt/go-moji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ktnyt/go-moji?style=social)|
|[ojichat](https://github.com/greymd/ojichat)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/greymd/ojichat?style=social)|


## Java

### Morphology analysis

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji是一個自包含且非常易於使用的日語形態分析器，專為搜索而設計。
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - Sudachi詞彙表


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji](https://github.com/atilika/kuromoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/atilika/kuromoji?style=social)|
|[Sudachi](https://github.com/WorksApplications/Sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/Sudachi?style=social)|
|[SudachiDict](https://github.com/WorksApplications/SudachiDict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiDict?style=social)|


### Others

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 從圖像中識別日文字符的Java庫
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 將日本漢字轉換為羅馬字（拉丁字母）的Java庫和命令行工具
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Java中的漢字轉假名/片假名/羅馬字輸出
 * [Kamite](https://github.com/fauu/Kamite) - 一款桌面式的日語學習輔助工具
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - React Native 的非同步日本語分詞原生插件，適用於 iOS 和 Android。
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本語分析器使用Kuromoji日本語分詞器進行ElasticSearch。
 * [moji4j](https://github.com/andree-surya/moji4j) - 一個Java庫，可在日文平假名、片假名和羅馬字之間進行轉換。
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - mecab-neologd 的日文文本正規化工具
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - 日本的elasticsearch分析插件


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sakarika/kanjitomo-ocr?style=social)|
|[jakaroma](https://github.com/nicolas-raoul/jakaroma)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nicolas-raoul/jakaroma?style=social)|
|[kakasi-java](https://github.com/nicolas-raoul/kakasi-java)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nicolas-raoul/kakasi-java?style=social)|
|[Kamite](https://github.com/fauu/Kamite)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/fauu/Kamite?style=social)|
|[react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/craftzdog/react-native-japanese-tokenizer?style=social)|
|[elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/suguru/elasticsearch-analysis-japanese?style=social)|
|[moji4j](https://github.com/andree-surya/moji4j)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/andree-surya/moji4j?style=social)|
|[neologdn-java](https://github.com/ikegami-yukino/neologdn-java)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/neologdn-java?style=social)|
|[elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/worksapplications/elasticsearch-sudachi?style=social)|


## Pretrained model

### Word2Vec

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - 使用Gensim和Mecab的日語Word2vec（單詞到向量）方法。
 * [chiVe](https://github.com/WorksApplications/chiVe) - 使用Sudachi和NWJC的日語詞嵌入
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - 艾摩日文
 * [embedrank](https://github.com/yagays/embedrank) - EmbedRank 的 Python 實現
 * [aovec](https://github.com/eggplants/aovec) - 簡易青空文庫Word2Vec建構器 - 青空文庫全書籍的Word2Vec建構器+已建構模型
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - 這是 AI LAB 文章「係り受けに基づく日本語単語埋込 (Dependency-based Japanese Word Embeddings)」的儲存庫 (文章網址 https://ai-lab.lapras.com/nlp/japanese-word-embedding/)。
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - 另一個日本維基百科實體向量
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 從最新的日本語Wikipedia傾印數據中，使用MeCab在IPA詞典和最新的Neologd詞典中進行形態素分析，並基於該結果學習word2vec、fastText和GloVe的詞向量表示的腳本。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/philipperemy/japanese-words-to-vectors?style=social)|
|[chiVe](https://github.com/WorksApplications/chiVe)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/chiVe?style=social)|
|[elmo-japanese](https://github.com/cl-tohoku/elmo-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/elmo-japanese?style=social)|
|[embedrank](https://github.com/yagays/embedrank)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/embedrank?style=social)|
|[aovec](https://github.com/eggplants/aovec)|[![Downloads](https://static.pepy.tech/badge/aovec/week)](https://pepy.tech/project/aovec)|[![Downloads](https://static.pepy.tech/badge/aovec)](https://pepy.tech/project/aovec)|![GitHub Repo stars](https://img.shields.io/github/stars/eggplants/aovec?style=social)|
|[dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/lapras-inc/dependency-based-japanese-word-embeddings?style=social)|
|[jawikivec](https://github.com/wikiwikification/jawikivec)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wikiwikification/jawikivec?style=social)|
|[jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kamigaito/jawiki_word_vector_updater?style=social)|


### Transformer based models

 * [bert-japanese](https://github.com/cl-tohoku/bert-japanese) - 日文文本的BERT模型。
 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - 由rinna株式會社提供的生成日語預訓練模型的代碼。
 * [bert-japanese](https://github.com/yoheikikuta/bert-japanese) - 使用SentencePiece的BERT模型進行日文文本處理。
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - Transformer 的日語分詞器
 * [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) - NTT有限公司提供的評估日語預訓練模型的代碼。
 * [shiba](https://github.com/octanove/shiba) - CANINE是一種高效的字符級別轉換器，我們提供了Pytorch實現和預訓練的日語模型。
 * [Dialog](https://github.com/reppy4620/Dialog) - 使用BERT和Transformer解碼器的日本聊天機器人的PyTorch實現
 * [language-pretraining](https://github.com/retarfi/language-pretraining) - PyTorch 實現的 BERT 和 ELECTRA 模型，適用於日文文本。
 * [medbertjp](https://github.com/ou-medinfo/medbertjp) - 在日本醫學領域中，預訓練BERT模型的試驗。
 * [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) - ILYS-aoba聊天機器人
 * [t5-japanese](https://github.com/megagonlabs/t5-japanese) - 預訓練日語T5模型的代碼
 * [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) - 使用Pytorch來使用BERT的日文預訓練模型。
 * [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) - Laboro BERT 日語：使用 Web-Corpus 預訓練的日語 BERT
 * [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) - 日本BERT預訓練模型
 * [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) - 日本語的aMLP Transformer模型
 * [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) - 使用UniDic和SudachiPy預先分詞，並在青空文庫和維基百科上訓練的日語BERT。
 * [sbert-ja](https://github.com/colorfulscoop/sbert-ja) - 用於 Hugging Face Model Hub 的句子 BERT 日語模型訓練代碼
 * [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) - 「日本推文情緒分析與疫苗接種比較」官方微調程式碼
 * [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) - 日本語GPT2生成モデル
 * [text2text-japanese](https://github.com/tanreinama/text2text-japanese) - 基於gpt-2的文本轉換模型
 * [gpt-ja](https://github.com/colorfulscoop/gpt-ja) - HuggingFace 的 transformers 的 GPT-2 日本模型
 * [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) - 使用friendly_JA語料庫訓練的MT模型，嘗試通過使用拉丁/英語衍生的片假名詞彙表，而不是標準的漢日詞彙表，使日語對西方人更加容易/易於理解。
 * [albert-japanese](https://github.com/alinear-corp/albert-japanese) - 使用SentencePiece的BERT模型進行日文文本處理。
 * [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) - 在日語Wikipedia語料庫中生成BERT預訓練模型的存儲庫
 * [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) - 一個在維基百科上訓練的日本DistilBERT預訓練模型。
 * [bert](https://github.com/informatix-inc/bert) - 這個存儲庫提供了使用 RoBERTa 預訓練於日本語語料庫的片段。我們的數據集包括日本維基百科和網頁滾動文章，總共 25GB。釋出的模型是基於 HuggingFace 的模型構建的。
 * [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) - 勞羅 DistilBERT 日文
 * [luke](https://github.com/studio-ousia/luke) - LUKE -- 基於知識嵌入的語言理解
 * [GPTSAN](https://github.com/tanreinama/GPTSAN) - 通用開關變壓器基於日語模式
 * [japanese-clip](https://github.com/rinnakk/japanese-clip) - 日本CLIP由rinna有限公司開發。
 * [AcademicBART](https://github.com/EhimeNLP/AcademicBART) - 我們在學術數據庫CiNii Articles的論文摘要上，預先訓練了一個基於BART的日語遮罩語言模型。
 * [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) - 我們在學術數據庫CiNii Articles的論文摘要上預訓練了一個基於RoBERTa的日語遮罩語言模型。
 * [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) - DistilBERT模型預先在131 GB的日本網頁文本上進行了預訓練。教師模型是LINE內部建立的BERT-base模型。
 * [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) - 使用經過日語翻譯的Stanford Alpaca資料集，進行LLaMA的微調並創建了Low-Rank Adapter，以下是其連結和生成樣本程式碼。
 * [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) - 提供預訓練模型、程式碼和指導文件，以在日本維基百科資源上預訓練官方ALBERT（https://github.com/google-research/albert）。
 * [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) - 日本的LLaMa實驗
 * [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) - EasyLightChatAssistant 是一個輕量級的環境，用於輕鬆測試不受審查或規範的本地日語模型LightChatAssistant，使用KoboldCpp。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bert-japanese](https://github.com/cl-tohoku/bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/bert-japanese?style=social)|
|[japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-pretrained-models?style=social)|
|[bert-japanese](https://github.com/yoheikikuta/bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yoheikikuta/bert-japanese?style=social)|
|[SudachiTra](https://github.com/WorksApplications/SudachiTra)|[![Downloads](https://static.pepy.tech/badge/SudachiTra/week)](https://pepy.tech/project/SudachiTra)|[![Downloads](https://static.pepy.tech/badge/SudachiTra)](https://pepy.tech/project/SudachiTra)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiTra?style=social)|
|[japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nttcslab/japanese-dialog-transformers?style=social)|
|[shiba](https://github.com/octanove/shiba)|[![Downloads](https://static.pepy.tech/badge/shiba-model/week)](https://pepy.tech/project/shiba-model)|[![Downloads](https://static.pepy.tech/badge/shiba-model)](https://pepy.tech/project/shiba-model)|![GitHub Repo stars](https://img.shields.io/github/stars/octanove/shiba?style=social)|
|[Dialog](https://github.com/reppy4620/Dialog)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/reppy4620/Dialog?style=social)|
|[language-pretraining](https://github.com/retarfi/language-pretraining)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/retarfi/language-pretraining?style=social)|
|[medbertjp](https://github.com/ou-medinfo/medbertjp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ou-medinfo/medbertjp?style=social)|
|[ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/ILYS-aoba-chatbot?style=social)|
|[t5-japanese](https://github.com/megagonlabs/t5-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/t5-japanese?style=social)|
|[pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/pytorch_bert_japanese?style=social)|
|[Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/Laboro-BERT-Japanese?style=social)|
|[RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/RoBERTa-japanese?style=social)|
|[aMLP-japanese](https://github.com/tanreinama/aMLP-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/aMLP-japanese?style=social)|
|[bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/akirakubo/bert-japanese-aozora?style=social)|
|[sbert-ja](https://github.com/colorfulscoop/sbert-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/colorfulscoop/sbert-ja?style=social)|
|[BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/PatrickJohnRamos/BERT-Japan-vaccination?style=social)|
|[gpt2-japanese](https://github.com/tanreinama/gpt2-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/gpt2-japanese?style=social)|
|[text2text-japanese](https://github.com/tanreinama/text2text-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/text2text-japanese?style=social)|
|[gpt-ja](https://github.com/colorfulscoop/gpt-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/colorfulscoop/gpt-ja?style=social)|
|[friendly_JA-Model](https://github.com/astremo/friendly_JA-Model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/astremo/friendly_JA-Model?style=social)|
|[albert-japanese](https://github.com/alinear-corp/albert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/alinear-corp/albert-japanese?style=social)|
|[ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Kosuke-Szk/ja_text_bert?style=social)|
|[DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/BandaiNamcoResearchInc/DistilBERT-base-jp?style=social)|
|[bert](https://github.com/informatix-inc/bert)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/informatix-inc/bert?style=social)|
|[Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/Laboro-DistilBERT-Japanese?style=social)|
|[luke](https://github.com/studio-ousia/luke)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/studio-ousia/luke?style=social)|
|[GPTSAN](https://github.com/tanreinama/GPTSAN)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/GPTSAN?style=social)|
|[japanese-clip](https://github.com/rinnakk/japanese-clip)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-clip?style=social)|
|[AcademicBART](https://github.com/EhimeNLP/AcademicBART)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/EhimeNLP/AcademicBART?style=social)|
|[AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/EhimeNLP/AcademicRoBERTa?style=social)|
|[LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/line/LINE-DistilBERT-Japanese?style=social)|
|[Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kunishou/Japanese-Alpaca-LoRA?style=social)|
|[albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nknytk/albert-japanese-tinysegmenter?style=social)|
|[japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/lighttransport/japanese-llama-experiment?style=social)|
|[easylightchatassistant](https://github.com/zuntan03/easylightchatassistant)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/zuntan03/easylightchatassistant?style=social)|


## ChatGPT

 * [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) - 使用ChatGPT的程式，讓您可以在VRChat上聊天。
 * [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) - 我們正在開發AITuber的基礎部分。
 * [wanna](https://github.com/hirokidaichi/wanna) - 具有自然語言的Shell命令啟動器
 * [ChatdollKit](https://github.com/uezo/ChatdollKit) - ChatdollKit 可以讓您將您的 3D 模型製作成聊天機器人。
 * [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) - ChatGPT API 日文版的 GUI
 * [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) - 這是搭載了ChatGPT3.5的伺か鬼「AI妹アイちゃん」。使用需要另外準備ChatGPT的API金鑰。
 * [vrchatbot](https://github.com/Geson-anko/vrchatbot) - 建立VRChat AI Bot的存儲庫
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPT會當YouTuber
 * [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) - 一個使用 Nuxt 3 構建的聊天框應用程序，由 Open AI 文本完成端點提供支持。您可以選擇不同的 AI 朋友個性。默認情況下，它會用日語回答。您可以使用此應用程序練習您的日語技能！
 * [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) - 這個 Chrome 擴充功能可以使用 ChatGPT 將選定的日文文本翻譯成平假名。
 * [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) - 在這個範例中，我們使用檢索增強生成模式，展示了一些創建類似ChatGPT體驗的方法，以應用於自己的數據。
 * [chatvrm](https://github.com/pixiv/chatvrm) - ChatVRM是一個可以在瀏覽器中輕鬆與3D角色對話的演示應用程式。
 * [sftly-replace](https://github.com/kmizu/sftly-replace) - 一個Chrome擴展程序，可以輕鬆替換所選文本
 * [summarize_arxv](https://github.com/rkmt/summarize_arxv) - 用圖表總結arXiv論文
 * [aiavatarkit](https://github.com/uezo/aiavatarkit) - 快速建立基於人工智慧的對話化頭像
 * [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) - 這個存儲庫是為了將在神戶市政府進行的ChatGPT試行使用所創建的流程等進行解決方案化並公開。
 * [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) - 為了提供使用Azure OpenAI進行應用程式實作的參考，我們免費提供應用程式的範例（參考架構、範例程式碼和部署步驟）。
 * [character_chat](https://github.com/mutaguchi/character_chat) - 這是一個使用OpenAI API的聊天腳本，可以與設定的角色用日語進行對話。
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - 用於在Slack上使用OpenAI的ChatGPT API的Slackbot腳本（假設使用日語）
用於在Slack上使用OpenAI的ChatGPT API的Slackbot腳本（假設使用日語）
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - 這是ChatGPT的提示示例。
ChatGPT的提示示例。
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - 一個使用Python和Langchain構建的日語漢字閃卡應用程序，並搭載了GPT-4的智能增強功能。
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - 評估GPT-4和ChatGPT在日本醫學執照考試上的表現
 * [japagen](https://github.com/retrieva/japagen) - 使用LLM在日語任務中生成虛擬學習數據的研究


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Yuchi-Games/VRChatGPT?style=social)|
|[AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/M-gen/AITuberDegikkoMirii?style=social)|
|[wanna](https://github.com/hirokidaichi/wanna)|[![Downloads](https://static.pepy.tech/badge/wanna/week)](https://pepy.tech/project/wanna)|[![Downloads](https://static.pepy.tech/badge/wanna)](https://pepy.tech/project/wanna)|![GitHub Repo stars](https://img.shields.io/github/stars/hirokidaichi/wanna?style=social)|
|[ChatdollKit](https://github.com/uezo/ChatdollKit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/uezo/ChatdollKit?style=social)|
|[ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gyokuro33/ChuanhuChatGPTJapanese?style=social)|
|[AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/manju-summoner/AISisterAIChan?style=social)|
|[vrchatbot](https://github.com/Geson-anko/vrchatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Geson-anko/vrchatbot?style=social)|
|[gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/karakuri-ai/gptuber-by-langchain?style=social)|
|[openai-chatfriend](https://github.com/supershaneski/openai-chatfriend)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/supershaneski/openai-chatfriend?style=social)|
|[chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt?style=social)|
|[azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nohanaga/azure-search-openai-demo?style=social)|
|[chatvrm](https://github.com/pixiv/chatvrm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/pixiv/chatvrm?style=social)|
|[sftly-replace](https://github.com/kmizu/sftly-replace)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kmizu/sftly-replace?style=social)|
|[summarize_arxv](https://github.com/rkmt/summarize_arxv)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rkmt/summarize_arxv?style=social)|
|[aiavatarkit](https://github.com/uezo/aiavatarkit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/uezo/aiavatarkit?style=social)|
|[pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/City-of-Kobe/pva-aoai-integration-solution?style=social)|
|[jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/azure-samples/jp-azureopenai-samples?style=social)|
|[character_chat](https://github.com/mutaguchi/character_chat)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mutaguchi/character_chat?style=social)|
|[chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sifue/chatgpt-slackbot?style=social)|
|[chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/dahatake/chatgpt-prompt-sample-japanese?style=social)|
|[kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/adilmoujahid/kanji-flashcard-app-gpt4?style=social)|
|[IgakuQA](https://github.com/jungokasai/IgakuQA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jungokasai/IgakuQA?style=social)|
|[japagen](https://github.com/retrieva/japagen)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/retrieva/japagen?style=social)|


## Dictionary

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - 基於網絡語言資源的新詞典，適用於mecab-ipadic。
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - 一個日本口音字典生成器
 * [jamdict](https://github.com/neocl/jamdict) - Python 3 庫，用於操作Jim Breen的JMdict、KanjiDic2、JMnedict和漢字-部首映射。
 * [unidic-py](https://github.com/polm/unidic-py) - 透過pip安裝的Unidic打包。
 * [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) - 日本公司用語辭典（JCLdic）
 * [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) - 酸橙專用萬病辭書
 * [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) - 從維基百科（日文版）生成SKK / MeCab詞典
 * [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) - 字典以尋找與文本相關的情感
 * [JumanDIC](https://github.com/ku-nlp/JumanDIC) - 這個存儲庫包含源字典文件，用於構建 JUMAN 和 Juman++ 的字典。
 * [ipadic-py](https://github.com/polm/ipadic-py) - IPAdic打包成Python易於使用的套件。
 * [unidic-lite](https://github.com/polm/unidic-lite) - 一個小型的UniDic版本，方便進行pip安裝。
 * [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) - 日本語輸入表情符號的 IME 附加詞典 orange_book，Google 日本語輸入等可將日本語轉換為表情符號的 IME 擴展詞典。
 * [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) - 日英轉換・英語縮寫展開的 IME 追加詞典 orange_book，可在 Google 日本語輸入法或 ATOK 等輸入法中實現從日語到英語的和英轉換和英語縮寫展開的 IME 擴展詞典。
 * [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) - NicoNico大百科和Pixiv百科全書共同部分的IME詞典
 * [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) - 這是GoogleIME用片假名詞彙字典專案的存檔，從日語外來詞的片假名詞彙轉換為英語。
 * [emoticon](https://github.com/tiwanari/emoticon) - Google日本語輸入的表情符號字典∩(,,Ò‿Ó,,)∩
 * [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) - 這是將開源mozc字典轉換為MeCab字典格式的結果。
 * [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) - 電音IME：針對Microsoft IME等輸入法所設計的「電音部」相關用語詞典。
 * [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) - 這是一個針對 Microsoft IME 等輸入法所設計的「にじさんじ」相關用語詞典。
 * [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) - 這是一個包含目前已知所有寶可夢名稱的用語詞典，旨在供Microsoft IME等輸入法使用。
 * [EJDict](https://github.com/kujirahand/EJDict) - 英日辭典數據（公共領域）EJDict-hand
 * [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) - 利用貴公司提供的輸入法，可以正確地使用日語。
 * [genshin-dict](https://github.com/kotofurumiya/genshin-dict) - 這是可用於 Windows/macOS 的原神詞彙字典。
 * [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) - JMdict和JMnedict的JSON格式
 * [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) - 將外部單詞轉換為Mozc系統詞典
 * [mh-dict-jp](https://github.com/utubo/mh-dict-jp) - 想要創建Monster Hunter的用戶詞典...
 * [jitenbot](https://github.com/stephenmk/jitenbot) - 將日本字典網站和應用程式的資料轉換為可攜式檔案格式。
 * [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) - 基於網絡語言資源的mecab-unidic新詞典
 * [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) - 這是關於Hololive（Hololive Production）的字典文件。您可以使用./dictionary文件夾中的文本文件將單詞添加到IME中。詳情請參閱README.md。
 * [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) - Yomitan/Yomichan的JMdict、JMnedict和KANJIDIC。
 * [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) - Yomichan中單詞的JLPT級別標籤
 * [Jitendex](https://github.com/stephenmk/Jitendex) - 一個免費且開放授權的日英詞典，可與多個詞典客戶端兼容。
 * [jiten](https://github.com/obfusk/jiten) - 基於jmdict/kanjidic的日本Android/CLI/Web字典 - 日語辭典、和英辭典、漢英字典、和德辭典、和蘭辭典
 * [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) - Pixiv 百科全書對於讀谷村的詞典


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neologd/mecab-ipadic-neologd?style=social)|
|[tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/tdmelodic?style=social)|
|[jamdict](https://github.com/neocl/jamdict)|[![Downloads](https://static.pepy.tech/badge/jamdict/week)](https://pepy.tech/project/jamdict)|[![Downloads](https://static.pepy.tech/badge/jamdict)](https://pepy.tech/project/jamdict)|![GitHub Repo stars](https://img.shields.io/github/stars/neocl/jamdict?style=social)|
|[unidic-py](https://github.com/polm/unidic-py)|[![Downloads](https://static.pepy.tech/badge/unidic/week)](https://pepy.tech/project/unidic)|[![Downloads](https://static.pepy.tech/badge/unidic)](https://pepy.tech/project/unidic)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/unidic-py?style=social)|
|[Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/Japanese-Company-Lexicon?style=social)|
|[manbyo-sudachi](https://github.com/yagays/manbyo-sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/manbyo-sudachi?style=social)|
|[jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tokuhirom/jawiki-kana-kanji-dict?style=social)|
|[JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/JIWC-Dictionary?style=social)|
|[JumanDIC](https://github.com/ku-nlp/JumanDIC)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/JumanDIC?style=social)|
|[ipadic-py](https://github.com/polm/ipadic-py)|[![Downloads](https://static.pepy.tech/badge/ipadic/week)](https://pepy.tech/project/ipadic)|[![Downloads](https://static.pepy.tech/badge/ipadic)](https://pepy.tech/project/ipadic)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/ipadic-py?style=social)|
|[unidic-lite](https://github.com/polm/unidic-lite)|[![Downloads](https://static.pepy.tech/badge/unidic-lite/week)](https://pepy.tech/project/unidic-lite)|[![Downloads](https://static.pepy.tech/badge/unidic-lite)](https://pepy.tech/project/unidic-lite)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/unidic-lite?style=social)|
|[emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/peaceiris/emoji-ime-dictionary?style=social)|
|[google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/peaceiris/google-ime-dictionary?style=social)|
|[dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ncaq/dic-nico-intersection-pixiv?style=social)|
|[google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KEINOS/google-ime-user-dictionary-ja-en?style=social)|
|[emoticon](https://github.com/tiwanari/emoticon)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tiwanari/emoticon?style=social)|
|[mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/akirakubo/mecab-mozcdic?style=social)|
|[denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/albno273/denonbu-ime-dic?style=social)|
|[nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Umichang/nijisanji-ime-dic?style=social)|
|[pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Umichang/pokemon-ime-dic?style=social)|
|[EJDict](https://github.com/kujirahand/EJDict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kujirahand/EJDict?style=social)|
|[Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Rinrin0413/Ayashiy-Nipongo-Dic?style=social)|
|[genshin-dict](https://github.com/kotofurumiya/genshin-dict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kotofurumiya/genshin-dict?style=social)|
|[jmdict-simplified](https://github.com/scriptin/jmdict-simplified)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/scriptin/jmdict-simplified?style=social)|
|[mozcdict-ext](https://github.com/reasonset/mozcdict-ext)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/reasonset/mozcdict-ext?style=social)|
|[mh-dict-jp](https://github.com/utubo/mh-dict-jp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/utubo/mh-dict-jp?style=social)|
|[jitenbot](https://github.com/stephenmk/jitenbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/stephenmk/jitenbot?style=social)|
|[mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neologd/mecab-unidic-neologd?style=social)|
|[hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/heppokofrontend/hololive-dictionary?style=social)|
|[jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/themoeway/jmdict-yomitan?style=social)|
|[yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/stephenmk/yomichan-jlpt-vocab?style=social)|
|[Jitendex](https://github.com/stephenmk/Jitendex)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/stephenmk/Jitendex?style=social)|
|[jiten](https://github.com/obfusk/jiten)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/obfusk/jiten?style=social)|
|[pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MarvNC/pixiv-yomitan?style=social)|


## Corpus

### Part-of-speech tagging / Named entity recognition

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - 使用維基百科進行日語固有表現抽取的資料集
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 用於命名實體識別的日語IOB2標記語料庫。
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter 語料庫
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - 平行通用依存句法。
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - 從Google UDT 2.0輸入的日本數據。
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大學網頁文件引導語料庫
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 註釋版的富滿開取中心語料庫


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/stockmarkteam/ner-wikipedia-dataset?style=social)|
|[IOB2Corpus](https://github.com/Hironsan/IOB2Corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/IOB2Corpus?style=social)|
|[TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/TwitterCorpus?style=social)|
|[UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/UD_Japanese-PUD?style=social)|
|[UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/UD_Japanese-GSD?style=social)|
|[KWDLC](https://github.com/ku-nlp/KWDLC)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/KWDLC?style=social)|
|[AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/AnnotatedFKCCorpus?style=social)|


### Parallel corpus

 * [small_parallel_enja](https://github.com/odashi/small_parallel_enja) - 50k 英日平行語料庫，用於機器翻譯基準測試。
 * [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) - 一個用於日中機器翻譯的網絡爬蟲語料庫
 * [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) - Coursera 課程挖掘和多階段微調，以改善講座翻譯
 * [JESC](https://github.com/rpryzant/JESC) - 一個大型的英日平行語料庫
 * [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) - AMI會議平行語料庫
 * [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) - 這個目錄包含一個龐大的日英字幕語料庫。原始數據來自斯坦福大學的JESC項目。
 * [jesc_small](https://github.com/yusugomori/jesc_small) - 小型日英字幕語料庫
 * [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) - 禁止用語或單詞級別考慮的日英對譯語料庫。
 * [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) - 中日韓電腦科學術語對照 / 日中韓的電腦科學用語對照 / 韓中日電腦科學術語對照 / 한중일 컴퓨터 과학 용어 대조
 * [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) - 創建日英平行語料庫和訓練NMT模型的腳本
 * [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) - 谷歌 vs DeepL JE


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[small_parallel_enja](https://github.com/odashi/small_parallel_enja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/odashi/small_parallel_enja?style=social)|
|[Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT?style=social)|
|[CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shyyhs/CourseraParallelCorpusMining?style=social)|
|[JESC](https://github.com/rpryzant/JESC)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rpryzant/JESC?style=social)|
|[AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tsuruoka-lab/AMI-Meeting-Parallel-Corpus?style=social)|
|[giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/DayuanJiang/giant_ja-en_parallel_corpus?style=social)|
|[jesc_small](https://github.com/yusugomori/jesc_small)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yusugomori/jesc_small?style=social)|
|[graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/marmooo/graded-enja-corpus?style=social)|
|[cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/dahlia/cjk-compsci-terms?style=social)|
|[Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/Laboro-ParaCorpus?style=social)|
|[google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Tzawa/google-vs-deepl-je?style=social)|


### Dialog corpus

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本電影推薦對話數據集
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - 透過爬蟲從Open 2ch網站建立的對話語料庫
 * [BSD](https://github.com/tsuruoka-lab/BSD) - 商業場景對話語料庫
 * [asdc](https://github.com/megagonlabs/asdc) - 住宿搜索對話語料庫 (宿泊施設探索對話語料庫)
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - 日語對話資料，適用於seq2seq等。
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - 這個存儲庫包含了在AACL-IJCNLP 2022的Eval4NLP 2022研討會上發表的論文《Chat Translation Error Detection for Assisting Cross-lingual Communications》中所發布的日英雙語聊天語料庫BPersona-chat。
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 日本語日常対話コーパス是一個高品質的多輪對話數據集，包含五個主題的日常對話：生活、學校、旅行、健康和娛樂。
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - LLM構築用的日本語聊天資料集

|Name|downloads/week|total downloads|stars|
-|-|-|-
|[JMRD](https://github.com/ku-nlp/JMRD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/JMRD?style=social)|
|[open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/1never/open2ch-dialogue-corpus?style=social)|
|[BSD](https://github.com/tsuruoka-lab/BSD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tsuruoka-lab/BSD?style=social)|
|[asdc](https://github.com/megagonlabs/asdc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/asdc?style=social)|
|[japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MokkeMeguru/japanese-corpus?style=social)|
|[BPersona-chat](https://github.com/cl-tohoku/BPersona-chat)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/BPersona-chat?style=social)|
|[japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jqk09a/japanese-daily-dialogue?style=social)|
|[llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/masanorihirano/llm-japanese-dataset?style=social)|

### Others

 * [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) - 日本現實文本蘊含語料庫（NLP 2020，LREC 2020）
 * [kanji-data](https://github.com/davidluzgouveia/kanji-data) - 一個包含更新的JLPT級別和WaniKani信息的JSON漢字數據集。
 * [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) - 日本語詞語相似度資料集
 * [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) - 一個用於日文簡化的改述資料庫
 * [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) - 翻譯：chakki的基於方面的情感分析數據集
 * [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) - JaQuAD：日本機器閱讀理解問答資料集（2022年，Skelter Labs）
 * [JaNLI](https://github.com/verypluming/JaNLI) - 日本對抗自然語言推論數據集
 * [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) - 基於證據的解釋數據集（AACL-IJCNLP 2020）
 * [emoji-ja](https://github.com/yagays/emoji-ja) - UNICODE繪文字的日本語讀音/關鍵字/分類詞典
 * [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) - 從維基百科創建的日語名稱對齊數據集
 * [ja.text8](https://github.com/Hironsan/ja.text8) - 用於詞向量嵌入的日文文本8語料庫。
 * [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) - 3行要約資料集
 * [japanese](https://github.com/hingston/japanese) - 這個存儲庫包含由利茲大學語料庫確定頻率排序的44,998個最常見的日語單詞列表。
 * [kanji-frequency](https://github.com/scriptin/kanji-frequency) - 從各種來源收集的漢字使用頻率數據
 * [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) - TEDxJP-10K 語音辨識評估數據集
 * [CoARiJ](https://github.com/chakki-works/CoARiJ) - 日本年報語料庫
 * [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) - 收集了用日語撰寫的技術書籍的生語料庫/工具
 * [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) - ITA語料庫的分塊詞註釋
 * [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) - 用於自然語言處理的預處理維基百科文本的實用腳本
 * [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) - 收集日語中不適當的表達方式。可用於自然語言處理時的數據清理等。
 * [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) - 從參議院官方網站整理了會派、議員、議案、質問主意書的數據。
 * [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) - 國會議案資料庫：衆議院
 * [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) - STAIR字幕：大規模日本圖像字幕數據集
 * [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) - Winograd模式挑戰的日本翻譯
 * [speechBSD](https://github.com/ku-nlp/speechBSD) - 一個包含音訊和說話者屬性信息的BSD語料庫擴展版。
 * [ita-corpus](https://github.com/mmorise/ita-corpus) - ITA語料庫的文章清單
 * [rohan4600](https://github.com/mmorise/rohan4600) - 莫拉平衡型日本語語料庫
 * [anlp-jp-history](https://github.com/whym/anlp-jp-history) - 語言處理學會年度大會演講的完整列表和機器可讀版本等。
 * [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) - 敬語轉換任務中的評估數據集
 * [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) - 日本中的英語借詞
 * [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) - 日本維基百科鏈接化語料庫
 * [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) - 這是日本總理一般政策演說的語料庫。
 * [wrime](https://github.com/ids-cv/wrime) - WRIME：主觀與客觀情感分析資料集
 * [jtubespeech](https://github.com/sarulab-speech/jtubespeech) - JTubeSpeech：從YouTube收集的日語語音語料庫
 * [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) - 在日語Wikipedia中常用的單詞列表
 * [kokkosho_data](https://github.com/rindybell/kokkosho_data) - 車輛不具合情報相關資料集
 * [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) - 在數位化資料OCR文字化業務中所創建的OCR學習用資料集。
 * [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) - 從全國書目資料中創建的假名數據集
 * [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) - JVS（日本語多目的話者）語料庫的自製標籤
 * [hirakanadic](https://github.com/po3rin/hirakanadic) - 允許Sudachi從任何複合詞列表中將平假名轉換為片假名。
 * [animedb](https://github.com/anilogia/animedb) - 約100年的動畫作品清單資料庫
 * [security_words](https://github.com/SaitoLab/security_words) - 與網路安全相關的公共組織的日英對應
 * [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) - 日本國會議員的資料
 * [honkoku-data](https://github.com/yuta1984/honkoku-data) - 這是歷史資料的市民參與型翻刻平台「大家一起翻刻」的文本數據存放處。/ 這些文本是在「大家一起翻刻」（https://honkoku.org）這個為日本歷史文獻提供群眾翻刻的平台上創建的。
 * [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) - wikiHow數據集（日語版）
 * [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) - 日英工程師詞彙表
 * [JSICK](https://github.com/verypluming/JSICK) - 日本語組成知識（JSICK）資料集/JSICK壓力測試集
 * [phishurl-list](https://github.com/JPCERTCC/phishurl-list) - JPCERT/CC 的釣魚網址數據集
 * [jcms](https://github.com/shigashiyama/jcms) - 一個日本多個專業領域的語料庫 (JCMS)
 * [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) - www.aozora.gr.jp 的純文字檔案存檔
 * [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) - friendly_JA 是一個平行的日語對日語語料庫，旨在通過使用拉丁/英語衍生的片假名詞彙表，而不是標準的漢日詞彙表，使日語更容易。
 * [topokanji](https://github.com/scriptin/topokanji) - 有效學習漢字的拓撲排序列表
 * [isbn4groups](https://github.com/uribo/isbn4groups) - 關於ISBN-13中以日語出版的出版物（978-4-XXXXXXXXX）相關的數據等。
 * [NMeCab](https://github.com/komutan/NMeCab) - NMeCab：關於在.NET上的日語形態分析器
 * [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) - 由數位化資料製作的OCR文字資料的ngram頻率統計資訊資料集。
 * [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) - 2023年1月重新設計的NDL Ngram Viewer源代碼等一套
 * [data_set](https://github.com/japanese-law-analysis/data_set) - 法律・判例相關的資料集
 * [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) - WRIME 的 HuggingFace 資料集
 * [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) - NDL古典籍OCR學習用數據集（大家一起翻刻加工數據）
 * [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) - GIS和考古模擬器。2023年開發中。
 * [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) - LIWC2015的日文版本
 * [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) - 日本Livedoor新聞語料庫，用於huggingface數據集。
 * [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) - JGLUE：用於huggingface數據集的日語通用語言理解評估
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality是一個通過眾包創建的數據集，反映了日本標註者的常識道德。
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - COMET-ATOMIC ja
彗星原子 ja
 * [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) - 日語對話常識圖表
 * [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) - 「日本語毒性スキーマの提案と評価」は、日本語の毒性に関するスキーマとデータセットを提供します。
 * [camera](https://github.com/CyberAgentAILab/camera) - CAMERA（CyberAgent多模態評估廣告文本生成）是日本的廣告文本生成數據集。
 * [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) - 日本語假新聞資料庫
 * [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) - jpn可解釋問答數據集
 * [copa-japanese](https://github.com/nlp-titech/copa-japanese) - 日本語的 COPA 資料集
 * [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) - 「按語義原則分類的單詞列表（WLSP）」的詞語熟悉度率
 * [ProSub](https://github.com/matbahasa/ProSub) - 代詞替代和稱呼詞的跨語言研究
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMorality是一個通過眾包創建的數據集，反映了日本標註者的常識道德。
 * [ramendb](https://github.com/nuko-yokohama/ramendb) - 從なんとか資料庫(https://supleks.jp/)的網頁爬蟲工具和收集的資料。
 * [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) - 相機（CyberAgent多模態評估廣告文本生成）用於huggingface數據集
 * [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) - 事實檢查句子NLI數據集
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - 這是將用於databricks/dolly-v2-12b的學習數據中使用的databricks-dolly-15k.jsonl翻譯成日語的數據集。
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELD是基於MELD的情感感知語音翻譯的英日數據集。
 * [meconaudio](https://github.com/elith-co-jp/meconaudio) - Mecon Audio（醫學會議音頻）是厚生勞動省主辦的先進醫療會議議事錄的朗讀數據集。
 * [japanese-addresses](https://github.com/geolonia/japanese-addresses) - 全國的町丁目級別（277,191項）住址數據的開放數據
 * [aozorasearch](https://github.com/myokoym/aozorasearch) - Groonga的青空文庫全文檢索系統。青空文庫全文檢索庫兼Web應用程式。
 * [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) - 此存儲庫包含重現LLM-jp語料庫的腳本。
 * [alpaca_ja](https://github.com/shi3z/alpaca_ja) - 這是將alpaca數據集翻譯成日文的內容。
 * [instruction_ja](https://github.com/megagonlabs/instruction_ja) - 日本語指示データ
 * [japanese-family-names](https://github.com/siikamiika/japanese-family-names) - 按頻率排序的前5000個日本姓氏，附帶讀音。
 * [kanji-data-media](https://github.com/kanjialive/kanji-data-media) - 來自Kanji alive的漢字、部首、媒體文件、字體和相關資源的日語語言數據
 * [reazonspeech](https://github.com/reazon-research/reazonspeech) - 在家建立大规模的日语音频语料库
 * [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) - 從青空文庫和Sapie點字數據創建的假名數據集
從青空文庫及及サピエ的點字數據創建的振り仮名的數據集
 * [koniwa](https://github.com/koniwa/koniwa) - 一個包含日語註釋聲音的開放收藏。
 * [JMMLU](https://github.com/nlp-waseda/JMMLU) - 日本語大規模マルチタスク言語理解ベンチマーク
 * [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) - 青空文庫振り仮名註釋附音訊語料庫的數據集
 * [jqara](https://github.com/hotchpotch/jqara) - JQaRA：具有檢索增強功能的日本問答系統 - 用於檢索增強(RAG)評估的日語問答資料集
 * [jemhopqa](https://github.com/aiishii/jemhopqa) - JEMHopQA（日本語説明可能なマルチホップ質問応答）は、内部推論を評価できる日本語マルチホップQAデータセットです。
 * [jacred](https://github.com/youmima/jacred) - 用於日文文件級關係提取數據集的存儲庫（計劃在三月份發布）。
用於日文文件級關係提取數據集的存儲庫（計劃在三月份發布）。
 * [jades](https://github.com/naist-nlp/jades) - JADES是一個針對非母語使用者的日文文本簡化數據集，詳細介紹在《JADES:針對非母語使用者的日文新文本簡化數據集》（論文即將發表）。
 * [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) - 2023年8月，墨爾本大學公開了安全性評估數據集『Do-Not-Answer』，該數據集已經被自動翻譯成日語，並且考慮了日本文化進行了修正，以便在日語LLM評估中使用。
 * [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) - OpenAssistant 的開源數據 OASST1 已經被翻譯成日文的數據集。



|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jrte-corpus](https://github.com/megagonlabs/jrte-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/jrte-corpus?style=social)|
|[kanji-data](https://github.com/davidluzgouveia/kanji-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/davidluzgouveia/kanji-data?style=social)|
|[JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/JapaneseWordSimilarityDataset?style=social)|
|[simple-jppdb](https://github.com/tmu-nlp/simple-jppdb)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tmu-nlp/simple-jppdb?style=social)|
|[chABSA-dataset](https://github.com/chakki-works/chABSA-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/chABSA-dataset?style=social)|
|[JaQuAD](https://github.com/SkelterLabsInc/JaQuAD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/SkelterLabsInc/JaQuAD?style=social)|
|[JaNLI](https://github.com/verypluming/JaNLI)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/verypluming/JaNLI?style=social)|
|[ebe-dataset](https://github.com/megagonlabs/ebe-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ebe-dataset?style=social)|
|[emoji-ja](https://github.com/yagays/emoji-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/emoji-ja?style=social)|
|[nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/nayose-wikipedia-ja?style=social)|
|[ja.text8](https://github.com/Hironsan/ja.text8)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/ja.text8?style=social)|
|[ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/KodairaTomonori/ThreeLineSummaryDataset?style=social)|
|[japanese](https://github.com/hingston/japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hingston/japanese?style=social)|
|[kanji-frequency](https://github.com/scriptin/kanji-frequency)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/scriptin/kanji-frequency?style=social)|
|[TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laboroai/TEDxJP-10K?style=social)|
|[CoARiJ](https://github.com/chakki-works/CoARiJ)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/CoARiJ?style=social)|
|[technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/textlint-ja/technological-book-corpus-ja?style=social)|
|[ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shirayu/ita-corpus-chuwa?style=social)|
|[wikipedia-utils](https://github.com/singletongue/wikipedia-utils)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/singletongue/wikipedia-utils?style=social)|
|[inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MosasoM/inappropriate-words-ja?style=social)|
|[house-of-councillors](https://github.com/smartnews-smri/house-of-councillors)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/smartnews-smri/house-of-councillors?style=social)|
|[house-of-representatives](https://github.com/smartnews-smri/house-of-representatives)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/smartnews-smri/house-of-representatives?style=social)|
|[STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/STAIR-Lab-CIT/STAIR-captions?style=social)|
|[Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/Winograd-Schema-Challenge-Ja?style=social)|
|[speechBSD](https://github.com/ku-nlp/speechBSD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/speechBSD?style=social)|
|[ita-corpus](https://github.com/mmorise/ita-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mmorise/ita-corpus?style=social)|
|[rohan4600](https://github.com/mmorise/rohan4600)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mmorise/rohan4600?style=social)|
|[anlp-jp-history](https://github.com/whym/anlp-jp-history)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/whym/anlp-jp-history?style=social)|
|[keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/keigo_transfer_task?style=social)|
|[loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jamesohortle/loanwords_gairaigo?style=social)|
|[jawikicorpus](https://github.com/wikiwikification/jawikicorpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wikiwikification/jawikicorpus?style=social)|
|[GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan?style=social)|
|[wrime](https://github.com/ids-cv/wrime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ids-cv/wrime?style=social)|
|[jtubespeech](https://github.com/sarulab-speech/jtubespeech)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarulab-speech/jtubespeech?style=social)|
|[WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/maeda6uiui-backup/WikipediaWordFrequencyList?style=social)|
|[kokkosho_data](https://github.com/rindybell/kokkosho_data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rindybell/kokkosho_data?style=social)|
|[pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/pdmocrdataset-part1?style=social)|
|[huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/huriganacorpus-ndlbib?style=social)|
|[jvs_hiho](https://github.com/Hiroshiba/jvs_hiho)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hiroshiba/jvs_hiho?style=social)|
|[hirakanadic](https://github.com/po3rin/hirakanadic)|[![Downloads](https://static.pepy.tech/badge/hirakanadic/week)](https://pepy.tech/project/hirakanadic)|[![Downloads](https://static.pepy.tech/badge/hirakanadic)](https://pepy.tech/project/hirakanadic)|![GitHub Repo stars](https://img.shields.io/github/stars/po3rin/hirakanadic?style=social)|
|[animedb](https://github.com/anilogia/animedb)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/anilogia/animedb?style=social)|
|[security_words](https://github.com/SaitoLab/security_words)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/SaitoLab/security_words?style=social)|
|[Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sugi2000/Data-on-Japanese-Diet-Members?style=social)|
|[honkoku-data](https://github.com/yuta1984/honkoku-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuta1984/honkoku-data?style=social)|
|[wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Katsumata420/wikihow_japanese?style=social)|
|[engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mercari/engineer-vocabulary-list?style=social)|
|[JSICK](https://github.com/verypluming/JSICK)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/verypluming/JSICK?style=social)|
|[phishurl-list](https://github.com/JPCERTCC/phishurl-list)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/JPCERTCC/phishurl-list?style=social)|
|[jcms](https://github.com/shigashiyama/jcms)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shigashiyama/jcms?style=social)|
|[aozorabunko_text](https://github.com/aozorahack/aozorabunko_text)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aozorahack/aozorabunko_text?style=social)|
|[friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/astremo/friendly_JA-Corpus?style=social)|
|[topokanji](https://github.com/scriptin/topokanji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/scriptin/topokanji?style=social)|
|[isbn4groups](https://github.com/uribo/isbn4groups)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/uribo/isbn4groups?style=social)|
|[NMeCab](https://github.com/komutan/NMeCab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/komutan/NMeCab?style=social)|
|[ndlngramdata](https://github.com/ndl-lab/ndlngramdata)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndlngramdata?style=social)|
|[ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndlngramviewer_v2?style=social)|
|[data_set](https://github.com/japanese-law-analysis/data_set)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/japanese-law-analysis/data_set?style=social)|
|[huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_wrime?style=social)|
|[ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndl-minhon-ocrdataset?style=social)|
|[PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/AsPJT/PAX_SAPIENTICA?style=social)|
|[j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tasukuigarashi/j-liwc2015?style=social)|
|[huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_livedoor-news-corpus?style=social)|
|[huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_JGLUE?style=social)|
|[commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Language-Media-Lab/commonsense-moral-ja?style=social)|
|[comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-waseda/comet-atomic-ja?style=social)|
|[dcsg-ja](https://github.com/nlp-waseda/dcsg-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-waseda/dcsg-ja?style=social)|
|[japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/inspection-ai/japanese-toxic-dataset?style=social)|
|[camera](https://github.com/CyberAgentAILab/camera)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CyberAgentAILab/camera?style=social)|
|[Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-Fakenews-Dataset?style=social)|
|[jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aiishii/jpn_explainable_qa_dataset?style=social)|
|[copa-japanese](https://github.com/nlp-titech/copa-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-titech/copa-japanese?style=social)|
|[WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/masayu-a/WLSP-familiarity?style=social)|
|[ProSub](https://github.com/matbahasa/ProSub)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/matbahasa/ProSub?style=social)|
|[commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Language-Media-Lab/commonsense-moral-ja?style=social)|
|[ramendb](https://github.com/nuko-yokohama/ramendb)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nuko-yokohama/ramendb?style=social)|
|[huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/huggingface-datasets_CAMERA?style=social)|
|[FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-waseda/FactCheckSentenceNLI-FCSNLI-?style=social)|
|[databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kunishou/databricks-dolly-15k-ja?style=social)|
|[EaST-MELD](https://github.com/ku-nlp/EaST-MELD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/EaST-MELD?style=social)|
|[meconaudio](https://github.com/elith-co-jp/meconaudio)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/elith-co-jp/meconaudio?style=social)|
|[japanese-addresses](https://github.com/geolonia/japanese-addresses)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/geolonia/japanese-addresses?style=social)|
|[aozorasearch](https://github.com/myokoym/aozorasearch)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/myokoym/aozorasearch?style=social)|
|[llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/llm-jp/llm-jp-corpus?style=social)|
|[alpaca_ja](https://github.com/shi3z/alpaca_ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shi3z/alpaca_ja?style=social)|
|[instruction_ja](https://github.com/megagonlabs/instruction_ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/instruction_ja?style=social)|
|[japanese-family-names](https://github.com/siikamiika/japanese-family-names)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/siikamiika/japanese-family-names?style=social)|
|[kanji-data-media](https://github.com/kanjialive/kanji-data-media)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kanjialive/kanji-data-media?style=social)|
|[reazonspeech](https://github.com/reazon-research/reazonspeech)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/reazon-research/reazonspeech?style=social)|
|[huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/huriganacorpus-aozora?style=social)|
|[koniwa](https://github.com/koniwa/koniwa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/koniwa/koniwa?style=social)|
|[JMMLU](https://github.com/nlp-waseda/JMMLU)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nlp-waseda/JMMLU?style=social)|
|[hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/hurigana-speech-corpus-aozora?style=social)|
|[jqara](https://github.com/hotchpotch/jqara)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hotchpotch/jqara?style=social)|
|[jemhopqa](https://github.com/aiishii/jemhopqa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aiishii/jemhopqa?style=social)|
|[jacred](https://github.com/youmima/jacred)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/youmima/jacred?style=social)|
|[jades](https://github.com/naist-nlp/jades)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/naist-nlp/jades?style=social)|
|[do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kunishou/do-not-answer-ja?style=social)|
|[oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kunishou/oasst1-89k-ja?style=social)|


## Tutorial

 * [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) - spaCy英文和日文教程。spacy-transformers、BERT、GiNZA。
 * [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) - 使用日語語料庫訓練fastText的教程
 * [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) - AllenNLP-NER-ja：使用AllenNLP進行針對日語的專有名詞識別。
 * [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) - 使用 chariot 和 PyTorch 进行日文文本分类的实验
 * [ginza-examples](https://github.com/poyo46/ginza-examples) - 日本語NLP程式庫GiNZA的推薦
 * [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) - 使用BERT進行文件分類-日文
 * [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) - 這是在 Google Colaboratory 上運行日本語 BERT 的方法。
 * [bert-book](https://github.com/stockmarkteam/bert-book) - 「BERT自然語言處理入門：使用Transformers的實踐編程」支援頁面
 * [janome-tutorial](https://github.com/mocobeta/janome-tutorial) - 這是使用Janome進行文本探勘的入門教程。
 * [handson-language-models](https://github.com/hnishi/handson-language-models) - 這是日語語言模型的實作指南資料。
 * [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) - 嘗試在Google Colab進行日文文本推論。
 * [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) - 這是 deep-learning-with-pytorch 的日文版 repository。
 * [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) -【2023年版】BERTによるテキスト分類
 * [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) - 透過深度學習的自然語言處理（共立出版）支援頁面。
 * [llm-book](https://github.com/ghmagazine/llm-book) - 「大規模言語模型入門」（技術評論社，2023）的GitHub存儲庫
 * [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) - NLP2024 教程三 創建並學習日語大規模語言模型 - 環境構建步驟與源代碼


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[spacy_tutorial](https://github.com/yuibi/spacy_tutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yuibi/spacy_tutorial?style=social)|
|[fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/icoxfog417/fastTextJapaneseTutorial?style=social)|
|[allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/allennlp-NER-ja?style=social)|
|[chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ymym3412/chariot-PyTorch-Japanese-text-classification?style=social)|
|[ginza-examples](https://github.com/poyo46/ginza-examples)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/poyo46/ginza-examples?style=social)|
|[DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nekoumei/DocumentClassificationUsingBERT-Japanese?style=social)|
|[BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/YutaroOgawa/BERT_Japanese_Google_Colaboratory?style=social)|
|[bert-book](https://github.com/stockmarkteam/bert-book)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/stockmarkteam/bert-book?style=social)|
|[janome-tutorial](https://github.com/mocobeta/janome-tutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/mocobeta/janome-tutorial?style=social)|
|[handson-language-models](https://github.com/hnishi/handson-language-models)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hnishi/handson-language-models?style=social)|
|[JapaneseNLI](https://github.com/verypluming/JapaneseNLI)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/verypluming/JapaneseNLI?style=social)|
|[deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Gin5050/deep-learning-with-pytorch-ja?style=social)|
|[bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/bert-classification-tutorial?style=social)|
|[python-nlp-book](https://github.com/python-nlp-book/python-nlp-book)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/python-nlp-book/python-nlp-book?style=social)|
|[llm-book](https://github.com/ghmagazine/llm-book)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ghmagazine/llm-book?style=social)|
|[nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hiroshi-matsuda-rit/nlp2024-tutorial-3?style=social)|


## Research summary

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 一份預先訓練的BERT模型清單，包括日語的單詞/子詞分詞和詞彙構建算法信息。
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 收集和分类有关日语文法错误修正的文献的存储库
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - 文本語料庫列表及更多（主要為日語）
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - 系統地最大化深度學習模型性能的策略手冊
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 嘗試將日語音韻，特別是音高重音資源整合成一個清單。
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - 開源的日本語LLM總結


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/awesome-bert-japanese?style=social)|
|[GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gotutiyan/GEC-Info-ja?style=social)|
|[dataset-list](https://github.com/ikegami-yukino/dataset-list)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/dataset-list?style=social)|
|[tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Valkyrja3607/tuning_playbook_ja?style=social)|
|[japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/olety/japanese-pitch-accent-resources?style=social)|
|[awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/llm-jp/awesome-japanese-llm?style=social)|


## Reference

 * [自然言語処理の餅屋](https://www.jnlp.org/nlp/top)
 * [フリーで使える日本語の主な大規模言語モデルまとめ](https://zenn.dev/hellorusk/articles/ddee520a5e4318)
 * [yasuokaの日記： 日本語係り受け解析器「2020年の総ざらえ」](https://srad.jp/~yasuoka/journal/643631/)
 * [yasuokaの日記： 日本語係り受け解析器「2021年の総ざらえ」](https://srad.jp/~yasuoka/journal/651542/)
 * https://github.com/topics/japanese?l=python
 * https://github.com/topics/japanese-language?l=python
 * https://github.com/search?o=desc&q=corpus+japanese&s=&type=Repositories
 * https://paperswithcode.com/datasets?lang=japanese
 * https://github.com/himkt/awesome-bert-japanese
 * [Awesome-Rust-MachineLearning-日本語向けのrustクレートや記事等をまとめたもの](https://github.com/vaaaaanquish/Awesome-Rust-MachineLearning/blob/main/README.ja.md)


## Contributors

 * [kaisugi](https://github.com/kaisugi) - [website](https://hellorusk.net)
 * [bomin0624](https://github.com/bomin0624) - [twitter](https://twitter.com/bomin0624_c)
 * [passaglia](https://github.com/passaglia) - [twitter](https://twitter.com/SamPassaglia)
