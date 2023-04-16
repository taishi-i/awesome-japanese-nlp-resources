# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專用於 Python 庫、預訓練模型、詞典和日語 NLP 語料庫的精選資源列表

此列表包括 455 個日語 NLP 存儲庫。 Hugging Face Spaces 上提供了用於搜索這些存儲庫的[工具](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)。

隨時歡迎您的貢獻！請在投稿前閱讀[投稿指南](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/contributing.md)。

GitHub 上不可用的資源將添加到 [wiki](https://github.com/taishi-i/awesome-japanese-nlp-resources/wiki)。


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## The latest additions 🎉

**Corpus**
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - 這裡是用於 databricks/dolly-v2-12b 的學習數據的 databricks-dolly-15k.jsonl 翻譯成日文的數據集.
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELD是基于MELD的情感感應用語音翻譯的日英文數據集.

_Updated on Apr 16, 2023_

## Contents
 * [Python library](#Python-library)
   * [Morphology analysis](#Morphology-analysis)
   * [Parsing](#Parsing)
   * [Converter](#Converter)
   * [Preprocessor](#Preprocessor)
   * [Sentence spliter](#Sentence-spliter)
   * [Sentiment analysis](#Sentiment-analysis)
   * [Machine translation](#Machine-translation)
   * [Named entity recognition](#Named-entity-recognition)
   * [OCR](#OCR)
   * [Tool for pretrained models](#Tool-for-pretrained-models)
   * [Others](#Others)
 * [C++](#c)
   * [Morphology analysis](#morphology-analysis-1)
   * [Parsing](#parsing-1)
   * [Others](#others-1)
 * [Rust crate](#Rust-crate)
   * [Morphology analysis](#morphology-analysis-2)
   * [Converter](#converter-1)
   * [Search engine library](#Search-engine-library)
   * [Others](#Others-2)
 * [JavaScript](#JavaScript)
   * [Morphology analysis](#morphology-analysis-3)
   * [Converter](#converter-2)
   * [Others](#Others-3)
 * [Go](#Go)
   * [Morphology analysis](#morphology-analysis-4)
   * [Others](#Others-4)
 * [Java](#Java)
   * [Morphology analysis](#morphology-analysis-5)
   * [Others](#Others-5)
 * [Pretrained model](#Pretrained-model)
   * [Word2Vec](#Word2Vec)
   * [Transformer based models](#Transformer-based-models)
 * [ChatGPT](#ChatGPT)
 * [Dictionary](#Dictionary)
 * [Corpus](#Corpus)
   * [Part-of-speech tagging / Named entity recognition](#part-of-speech-tagging--named-entity-recognition)
   * [Text classification](#Text-classification)
   * [Parallel corpus](#Parallel-corpus)
   * [Dialog corpus](#Dialog-corpus)
   * [Others](#others-3)
 * [Tutorial](#Tutorial)
 * [Research summary](#Research-summary)
 * [Reference](#Reference)
 * [Contributors](#Contributors)


## Python library

### Morphology analysis

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - 該網站的網站名稱為"Sudachi.rs".
 * [Janome](https://github.com/mocobeta/janome) - 日本形狀分析引擎用純粹的Python寫
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - 您可以在此找到原版:http://taku910.github.io/mecab/
 * [mecab](https://github.com/ikegami-yukino/mecab) - 這裡是一個可以使用Windows 64位 MeCab二進制程式,
 * [fugashi](https://github.com/polm/fugashi) - 該網站的網站是一個非常重要的網站,
 * [nagisa](https://github.com/taishi-i/nagisa) - 基于反復性神經網絡的日本代幣化器
 * [pyknp](https://github.com/ku-nlp/pyknp) - 該網站的使用者應使用:
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - 該網站的使用者必須:
 * [konoha](https://github.com/himkt/konoha) - 野:日本代幣化器的簡單包裝
 * [natto-py](https://github.com/buruzaemon/natto-py) - 該網站將Python程式語言與MeCab結合,
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - 這裡是我們最喜歡的網站.
 * [python-vaporetto](https://github.com/daac-tools/python-vaporetto) - 這是一款基于點性預測的快速輕量令牌.
 * [dango](https://github.com/mkartawijaya/dango) - 簡易使用的日文標記器, 面向學習語言和非語言學家
 * [rhoknp](https://github.com/ku-nlp/rhoknp) - 還有另一項Python對Juman++/KNP的結合
 * [python-vibrato](https://github.com/daac-tools/python-vibrato) - 基于Viterbi的加速令牌化器 (Python包裝)


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[SudachiPy](https://github.com/WorksApplications/SudachiPy)|[![Downloads](https://pepy.tech/badge/sudachipy/week)](https://pepy.tech/project/sudachipy)|[![Downloads](https://pepy.tech/badge/sudachipy)](https://pepy.tech/project/sudachipy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiPy?style=social)|
|[Janome](https://github.com/mocobeta/janome)|[![Downloads](https://pepy.tech/badge/janome/week)](https://pepy.tech/project/janome)|[![Downloads](https://pepy.tech/badge/janome)](https://pepy.tech/project/janome)|![GitHub Repo stars](https://img.shields.io/github/stars/mocobeta/janome?style=social)|
|[mecab-python3](https://github.com/SamuraiT/mecab-python3)|[![Downloads](https://pepy.tech/badge/mecab-python3/week)](https://pepy.tech/project/mecab-python3)|[![Downloads](https://pepy.tech/badge/mecab-python3)](https://pepy.tech/project/mecab-python3)|![GitHub Repo stars](https://img.shields.io/github/stars/SamuraiT/mecab-python3?style=social)|
|[mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python)|[![Downloads](https://pepy.tech/badge/mecab/week)](https://pepy.tech/project/mecab)|[![Downloads](https://pepy.tech/badge/mecab)](https://pepy.tech/project/mecab)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/mecab?style=social)|
|[fugashi](https://github.com/polm/fugashi)|[![Downloads](https://pepy.tech/badge/fugashi/week)](https://pepy.tech/project/fugashi)|[![Downloads](https://pepy.tech/badge/fugashi)](https://pepy.tech/project/fugashi)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/fugashi?style=social)|
|[nagisa](https://github.com/taishi-i/nagisa)|[![Downloads](https://pepy.tech/badge/nagisa/week)](https://pepy.tech/project/nagisa)|[![Downloads](https://pepy.tech/badge/nagisa)](https://pepy.tech/project/nagisa)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/nagisa?style=social)|
|[pyknp](https://github.com/ku-nlp/pyknp)|[![Downloads](https://pepy.tech/badge/pyknp/week)](https://pepy.tech/project/pyknp)|[![Downloads](https://pepy.tech/badge/pyknp)](https://pepy.tech/project/pyknp)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/pyknp?style=social)|
|[Mykytea-python](https://github.com/chezou/Mykytea-python)|[![Downloads](https://pepy.tech/badge/kytea/week)](https://pepy.tech/project/kytea)|[![Downloads](https://pepy.tech/badge/kytea)](https://pepy.tech/project/kytea)|![GitHub Repo stars](https://img.shields.io/github/stars/chezou/Mykytea-python?style=social)|
|[konoha](https://github.com/himkt/konoha)|[![Downloads](https://pepy.tech/badge/konoha/week)](https://pepy.tech/project/konoha)|[![Downloads](https://pepy.tech/badge/konoha)](https://pepy.tech/project/konoha)|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/konoha?style=social)|
|[natto-py](https://github.com/buruzaemon/natto-py)|[![Downloads](https://pepy.tech/badge/natto-py/week)](https://pepy.tech/project/natto-py)|[![Downloads](https://pepy.tech/badge/natto-py)](https://pepy.tech/project/natto-py)|![GitHub Repo stars](https://img.shields.io/github/stars/buruzaemon/natto-py?style=social)|
|[rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python)|[![Downloads](https://pepy.tech/badge/rakutenma/week)](https://pepy.tech/project/rakutenma)|[![Downloads](https://pepy.tech/badge/rakutenma)](https://pepy.tech/project/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/rakutenma-python?style=social)|
|[python-vaporetto](https://github.com/daac-tools/python-vaporetto)|[![Downloads](https://pepy.tech/badge/vaporetto/week)](https://pepy.tech/project/vaporetto)|[![Downloads](https://pepy.tech/badge/vaporetto)](https://pepy.tech/project/vaporetto)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/python-vaporetto?style=social)|
|[dango](https://github.com/mkartawijaya/dango)|[![Downloads](https://pepy.tech/badge/dango/week)](https://pepy.tech/project/dango)|[![Downloads](https://pepy.tech/badge/dango)](https://pepy.tech/project/dango)|![GitHub Repo stars](https://img.shields.io/github/stars/mkartawijaya/dango?style=social)|
|[rhoknp](https://github.com/ku-nlp/rhoknp)|[![Downloads](https://pepy.tech/badge/rhoknp/week)](https://pepy.tech/project/rhoknp)|[![Downloads](https://pepy.tech/badge/rhoknp)](https://pepy.tech/project/rhoknp)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/rhoknp?style=social)|
|[python-vibrato](https://github.com/daac-tools/python-vibrato)|[![Downloads](https://pepy.tech/badge/vibrato/week)](https://pepy.tech/project/vibrato)|[![Downloads](https://pepy.tech/badge/vibrato)](https://pepy.tech/project/vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/daac-tools/python-vibrato?style=social)|


### Parsing

 * [ginza](https://github.com/megagonlabs/ginza) - 使用 spaCy作為基于通用依賴的框架的日本NLP圖書館
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - 另一位日本依賴結構分析器
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - 代號化POS標籤化和依賴分析器,
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - 布管道組件的使用
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - 標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標籤標
 * [depccg](https://github.com/masashi-y/depccg) - 具有超標籤和依賴因素模型的CCG解析器
 * [bertknp](https://github.com/ku-nlp/bertknp) - 基于BERT的日本依賴解析器
 * [esupar](https://github.com/KoichiYasuoka/esupar) - 標籤化POS標籤和依賴分析器,
 * [yomikata](https://github.com/passaglia/yomikata) - 使用精準調節的BERT模型.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ginza](https://github.com/megagonlabs/ginza)|[![Downloads](https://pepy.tech/badge/ginza/week)](https://pepy.tech/project/ginza)|[![Downloads](https://pepy.tech/badge/ginza)](https://pepy.tech/project/ginza)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ginza?style=social)|
|[cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python)|[![Downloads](https://pepy.tech/badge/cabocha-python/week)](https://pepy.tech/project/cabocha-python)|[![Downloads](https://pepy.tech/badge/cabocha-python)](https://pepy.tech/project/cabocha-python)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/cabocha?style=social)|
|[UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD)|[![Downloads](https://pepy.tech/badge/UniDic2UD/week)](https://pepy.tech/project/UniDic2UD)|[![Downloads](https://pepy.tech/badge/UniDic2UD)](https://pepy.tech/project/UniDic2UD)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/UniDic2UD?style=social)|
|[camphr](https://github.com/PKSHATechnology-Research/camphr)|[![Downloads](https://pepy.tech/badge/camphr/week)](https://pepy.tech/project/camphr)|[![Downloads](https://pepy.tech/badge/camphr)](https://pepy.tech/project/camphr)|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/camphr?style=social)|
|[SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic)|[![Downloads](https://pepy.tech/badge/SuParUniDic/week)](https://pepy.tech/project/SuParUniDic)|[![Downloads](https://pepy.tech/badge/SuParUniDic)](https://pepy.tech/project/SuParUniDic)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/SuPar-UniDic?style=social)|
|[depccg](https://github.com/masashi-y/depccg)|[![Downloads](https://pepy.tech/badge/depccg/week)](https://pepy.tech/project/depccg)|[![Downloads](https://pepy.tech/badge/depccg)](https://pepy.tech/project/depccg)|![GitHub Repo stars](https://img.shields.io/github/stars/masashi-y/depccg?style=social)|
|[bertknp](https://github.com/ku-nlp/bertknp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/bertknp?style=social)|
|[esupar](https://github.com/KoichiYasuoka/esupar)|[![Downloads](https://pepy.tech/badge/esupar/week)](https://pepy.tech/project/esupar)|[![Downloads](https://pepy.tech/badge/esupar)](https://pepy.tech/project/esupar)|![GitHub Repo stars](https://img.shields.io/github/stars/KoichiYasuoka/esupar?style=social)|
|[yomikata](https://github.com/passaglia/yomikata)|[![Downloads](https://pepy.tech/badge/yomikata/week)](https://pepy.tech/project/yomikata)|[![Downloads](https://pepy.tech/badge/yomikata)](https://pepy.tech/project/yomikata)|![GitHub Repo stars](https://img.shields.io/github/stars/passaglia/yomikata?style=social)|

### Converter

 * [pykakasi](https://github.com/miurahr/pykakasi) - 輕量轉換器從日本語卡納-坎吉句子到卡納-羅馬文.
 * [cutlet](https://github.com/polm/cutlet) - 在Python中將日文轉換為羅馬吉
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - 將英語字母改成卡塔卡納
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - 轉換阿拉伯數字或"西方"式數字,
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - 該網站的使用者:
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - 這項軟體是日本文本解析器,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[pykakasi](https://github.com/miurahr/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi/week)](https://pepy.tech/project/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi)](https://pepy.tech/project/pykakasi)|![GitHub Repo stars](https://img.shields.io/github/stars/miurahr/pykakasi?style=social)|
|[cutlet](https://github.com/polm/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet/week)](https://pepy.tech/project/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet)](https://pepy.tech/project/cutlet)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/cutlet?style=social)|
|[alphabet2kana](https://github.com/shihono/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana/week)](https://pepy.tech/project/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana)](https://pepy.tech/project/alphabet2kana)|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/alphabet2kana?style=social)|
|[Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Greatdane/Convert-Numbers-to-Japanese?style=social)|
|[mozcpy](https://github.com/ikegami-yukino/mozcpy)|[![Downloads](https://pepy.tech/badge/mozcpy/week)](https://pepy.tech/project/mozcpy)|[![Downloads](https://pepy.tech/badge/mozcpy)](https://pepy.tech/project/mozcpy)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/mozcpy?style=social)|
|[jamorasep](https://github.com/tachi-hi/jamorasep)|[![Downloads](https://pepy.tech/badge/jamorasep/week)](https://pepy.tech/project/jamorasep)|[![Downloads](https://pepy.tech/badge/jamorasep)](https://pepy.tech/project/jamorasep)|![GitHub Repo stars](https://img.shields.io/github/stars/tachi-hi/jamorasep?style=social)|


### Preprocessor

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - 關於日本語文字標準化器
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - 清純的 Python 日本字符互換器
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - 這裡是日本漢字的快速轉換器.
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 能使用日本語文字清潔器
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 如何使用此工具?


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[neologdn](https://github.com/ikegami-yukino/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn/week)](https://pepy.tech/project/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn)](https://pepy.tech/project/neologdn)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/neologdn?style=social)|
|[jaconv](https://github.com/ikegami-yukino/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv/week)](https://pepy.tech/project/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv)](https://pepy.tech/project/jaconv)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/jaconv?style=social)|
|[mojimoji](https://github.com/studio-ousia/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji/week)](https://pepy.tech/project/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji)](https://pepy.tech/project/mojimoji)|![GitHub Repo stars](https://img.shields.io/github/stars/studio-ousia/mojimoji?style=social)|
|[text-cleaning](https://github.com/ku-nlp/text-cleaning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/text-cleaning?style=social)|
|[HojiChar](https://github.com/HojiChar/HojiChar)|[![Downloads](https://pepy.tech/badge/HojiChar/week)](https://pepy.tech/project/HojiChar)|[![Downloads](https://pepy.tech/badge/HojiChar)](https://pepy.tech/project/HojiChar)|![GitHub Repo stars](https://img.shields.io/github/stars/HojiChar/HojiChar?style=social)|


### Sentence spliter

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日本文本的句子界定判定工具 (日本語文境界判定器)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日本語句子破解器
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 還有另一種用於日本文字的句子級代碼化
 * [budoux](https://github.com/google/budoux) - 獨立,小,中立語言. BudouX是Budou的後繼者,
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - 文的日本語句子分割圖書館
 * [hasami](https://github.com/mkartawijaya/hasami) - 在日文文本上進行句子分割的工具
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - 在Rust中寫的Python的日本文本分區器
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日本語句子分割工具的比較


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bunkai](https://github.com/megagonlabs/bunkai)|[![Downloads](https://pepy.tech/badge/bunkai/week)](https://pepy.tech/project/bunkai)|[![Downloads](https://pepy.tech/badge/bunkai)](https://pepy.tech/project/bunkai)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/bunkai?style=social)|
|[japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker)|[![Downloads](https://pepy.tech/badge/japanese-sentence-breaker/week)](https://pepy.tech/project/japanese-sentence-breaker)|[![Downloads](https://pepy.tech/badge/japanese-sentence-breaker)](https://pepy.tech/project/japanese-sentence-breaker)|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/japanese-sentence-breaker?style=social)|
|[sengiri](https://github.com/ikegami-yukino/sengiri)|[![Downloads](https://pepy.tech/badge/sengiri/week)](https://pepy.tech/project/sengiri)|[![Downloads](https://pepy.tech/badge/sengiri)](https://pepy.tech/project/sengiri)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/sengiri?style=social)|
|[budoux](https://github.com/google/budoux)|[![Downloads](https://pepy.tech/badge/budoux/week)](https://pepy.tech/project/budoux)|[![Downloads](https://pepy.tech/badge/budoux)](https://pepy.tech/project/budoux)|![GitHub Repo stars](https://img.shields.io/github/stars/google/budoux?style=social)|
|[ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter)|[![Downloads](https://pepy.tech/badge/ja_sentence_segmenter/week)](https://pepy.tech/project/ja_sentence_segmenter)|[![Downloads](https://pepy.tech/badge/ja_sentence_segmenter)](https://pepy.tech/project/ja_sentence_segmenter)|![GitHub Repo stars](https://img.shields.io/github/stars/wwwcojp/ja_sentence_segmenter?style=social)|
|[hasami](https://github.com/mkartawijaya/hasami)|[![Downloads](https://pepy.tech/badge/hasami/week)](https://pepy.tech/project/hasami)|[![Downloads](https://pepy.tech/badge/hasami)](https://pepy.tech/project/hasami)|![GitHub Repo stars](https://img.shields.io/github/stars/mkartawijaya/hasami?style=social)|
|[kuzukiri](https://github.com/alinear-corp/kuzukiri)|[![Downloads](https://pepy.tech/badge/kuzukiri/week)](https://pepy.tech/project/kuzukiri)|[![Downloads](https://pepy.tech/badge/kuzukiri)](https://pepy.tech/project/kuzukiri)|![GitHub Repo stars](https://img.shields.io/github/stars/alinear-corp/kuzukiri?style=social)|
|[ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/ja-senter-benchmark?style=social)|


### Sentiment analysis

 * [oseti](https://github.com/ikegami-yukino/oseti) - 根據字典的日本語情緒分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 決定日本文檔的負面正面.
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日本文字情感分析器
 * [asari](https://github.com/Hironsan/asari) - 已在Python中實現日本情緒分析器.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[oseti](https://github.com/ikegami-yukino/oseti)|[![Downloads](https://pepy.tech/badge/oseti/week)](https://pepy.tech/project/oseti)|[![Downloads](https://pepy.tech/badge/oseti)](https://pepy.tech/project/oseti)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/oseti?style=social)|
|[negapoji](https://github.com/liaoziyang/negapoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/liaoziyang/negapoji?style=social)|
|[pymlask](https://github.com/ikegami-yukino/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask/week)](https://pepy.tech/project/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask)](https://pepy.tech/project/pymlask)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/pymlask?style=social)|
|[asari](https://github.com/Hironsan/asari)|[![Downloads](https://pepy.tech/badge/asari/week)](https://pepy.tech/project/asari)|[![Downloads](https://pepy.tech/badge/asari)](https://pepy.tech/project/asari)|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/asari?style=social)|


### Machine translation

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - 該計畫的目標是:
 * [JASS](https://github.com/Mao-KU/JASS) - 語言學習與語言翻譯 (JASS) 專門針對日文的神經機器翻譯 (LREC2020) 序列到序列預訓練,
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 這是一套由日語-英語機器翻譯強度的現象評估資料集. 資料集是基于MTNT資料集,並附加了四種語言現象的注解; 屬名詞,縮寫名詞,口頭式表達,和變體. COLING 2020.
 * [VISA](https://github.com/ku-nlp/VISA) - 兩邊都使用了不同的字幕,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MorinoseiMorizo/jparacrawl-finetune?style=social)|
|[JASS](https://github.com/Mao-KU/JASS)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Mao-KU/JASS?style=social)|
|[PheMT](https://github.com/cl-tohoku/PheMT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/PheMT?style=social)|
|[VISA](https://github.com/ku-nlp/VISA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/VISA?style=social)|


### Named entity recognition

 * [namaco](https://github.com/chakki-works/namaco) - 基於字符命名的實體識別.
 * [entitypedia](https://github.com/chakki-works/entitypedia) - 實體百科是維基百科的擴展名稱實體字典.
 * [noyaki](https://github.com/ken11/noyaki) - 轉換字符跨度標籤資訊為代號化文字標籤資訊.
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - 該程式的使用者必須使用 BERT 模型的代碼.
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 基于詳細的注解標準, 能推論案例報告資料庫中固有表達及關係抽取精度的代碼


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namaco](https://github.com/chakki-works/namaco)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/namaco?style=social)|
|[entitypedia](https://github.com/chakki-works/entitypedia)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/entitypedia?style=social)|
|[noyaki](https://github.com/ken11/noyaki)|[![Downloads](https://pepy.tech/badge/noyaki/week)](https://pepy.tech/project/noyaki)|[![Downloads](https://pepy.tech/badge/noyaki)](https://pepy.tech/project/noyaki)|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/noyaki?style=social)|
|[bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/bert-japanese-ner-finetuning?style=social)|
|[joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aih-uth/joint-information-extraction-hs?style=social)|


### OCR

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - 關於日本文字的光學字符識別,
 * [mokuro](https://github.com/kha-white/mokuro) - 閱讀日本漫畫在浏览器內,
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - 手寫的日本OCR演示使用觸控面板繪製輸入文字使用Intel OpenVINO工具包
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - 這裡是日本的OCR,
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - 沒有任何可能的.
 * [donut](https://github.com/clovaai/donut) - 沒有OCR的文件理解變壓器 (Donut) 和合成文件生成器 (SynthDoG) 的官方實施, ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - 翻譯漫畫的方法 - 獲得日本漫畫
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - 認識現代日本雜誌的OCR系統
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - 沒有任何可能的.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[manga-ocr](https://github.com/kha-white/manga-ocr)|[![Downloads](https://pepy.tech/badge/manga-ocr/week)](https://pepy.tech/project/manga-ocr)|[![Downloads](https://pepy.tech/badge/manga-ocr)](https://pepy.tech/project/manga-ocr)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/manga-ocr?style=social)|
|[mokuro](https://github.com/kha-white/mokuro)|[![Downloads](https://pepy.tech/badge/mokuro/week)](https://pepy.tech/project/mokuro)|[![Downloads](https://pepy.tech/badge/mokuro)](https://pepy.tech/project/mokuro)|![GitHub Repo stars](https://img.shields.io/github/stars/kha-white/mokuro?style=social)|
|[handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yas-sim/handwritten-japanese-ocr?style=social)|
|[OCR_Japanease](https://github.com/tanreinama/OCR_Japanease)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/OCR_Japanease?style=social)|
|[ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/ndlocr_cli?style=social)|
|[donut](https://github.com/clovaai/donut)|[![Downloads](https://pepy.tech/badge/donut-python/week)](https://pepy.tech/project/donut-python)|[![Downloads](https://pepy.tech/badge/donut-python)](https://pepy.tech/project/donut-python)|![GitHub Repo stars](https://img.shields.io/github/stars/clovaai/donut?style=social)|
|[JMTrans](https://github.com/ttop32/JMTrans)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ttop32/JMTrans?style=social)|
|[Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ducanh841988/Kindai-OCR?style=social)|
|[text_recognition](https://github.com/ndl-lab/text_recognition)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ndl-lab/text_recognition?style=social)|


### Tool for pretrained models

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - 評估日本語一般語言理解
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - 在空間變壓器中使用自訂令牌
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - 沒有任何可能的.
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - 調查包括MLP,CNN,RNN,BERT方法在內的各種DNN文字分類器.
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - 部署使用FastAPI和BERT的情緒分析伺服器
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - 面具式語言模型為日語和越南語提供分數
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - 關於西巴的AllenNLP整合:日本的 CANINE模型
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - 經驗證書以評估日本類似性數據集中的日本語 word2vec模型
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - 根據BERT的日本語 GEC標籤
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - 沒有任何其他國家的
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - 這裡是我最喜歡的.
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - 語語法誤區修正工具
 * [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) - 日本穩定傳播是一個日本特有的隱藏文字轉圖像傳播模型,
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - 這裡是一個很棒的地方.
 * [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) - 標示代碼用于先調 GPT/GPT-NeoX 模型和訓練先的推論
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - 訓練與評估JGLUE的文本,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[JGLUE](https://github.com/yahoojapan/JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yahoojapan/JGLUE?style=social)|
|[ginza-transformers](https://github.com/megagonlabs/ginza-transformers)|[![Downloads](https://pepy.tech/badge/ginza-transformers/week)](https://pepy.tech/project/ginza-transformers)|[![Downloads](https://pepy.tech/badge/ginza-transformers)](https://pepy.tech/project/ginza-transformers)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/ginza-transformers?style=social)|
|[t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Jinyamyzk/t5_japanese_dialogue_generation?style=social)|
|[japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Masao-Taketani/japanese_text_classification?style=social)|
|[Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/izuna385/Japanese-BERT-Sentiment-Analyzer?style=social)|
|[jmlm_scoring](https://github.com/minhpqn/jmlm_scoring)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/minhpqn/jmlm_scoring?style=social)|
|[allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model)|[![Downloads](https://pepy.tech/badge/allennlp-shiba/week)](https://pepy.tech/project/allennlp-shiba)|[![Downloads](https://pepy.tech/badge/allennlp-shiba)](https://pepy.tech/project/allennlp-shiba)|![GitHub Repo stars](https://img.shields.io/github/stars/shunk031/allennlp-shiba-model?style=social)|
|[evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/evaluate_japanese_w2v?style=social)|
|[gector-ja](https://github.com/jonnyli1125/gector-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jonnyli1125/gector-ja?style=social)|
|[Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-BPEEncoder?style=social)|
|[Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tanreinama/Japanese-BPEEncoder_V2?style=social)|
|[transformer-copy](https://github.com/youichiro/transformer-copy)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/youichiro/transformer-copy?style=social)|
|[japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-stable-diffusion?style=social)|
|[nagisa_bert](https://github.com/taishi-i/nagisa_bert)|[![Downloads](https://pepy.tech/badge/nagisa_bert/week)](https://pepy.tech/project/nagisa_bert)|[![Downloads](https://pepy.tech/badge/nagisa_bert)](https://pepy.tech/project/nagisa_bert)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/nagisa_bert?style=social)|
|[prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/prefix-tuning-gpt?style=social)|
|[JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nobu-g/JGLUE-benchmark?style=social)|

### Others

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - 這種工具可以將日本名字分為姓氏和姓氏.
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - 專為日本人使用的NLPPython圖書館的資源
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - 語版本日本語意義角色赋予系統 (ASA)
 * [toiro](https://github.com/taishi-i/toiro) - 日本代幣化工具的比較工具
 * [ja-timex](https://github.com/yagays/ja-timex) - 根據規則的解析器,
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - 數據集,用于從文字資料中選擇特征
 * [daaja](https://github.com/kajyuuen/daaja) - 這裡有日本人使用的NLP數據增強實施.
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - 該資料庫的目的是在我在網站上所寫的概念證明 (PoC) 和研發 (R&D) 背景下, 製作原型作為案例研究. 主要研究主題是與表示學習相關的自動編碼器,
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - 該系統是為KyotoCorpus,KWDLC和AnnotatedFKCCorpus提供處理器,
 * [nlplot](https://github.com/takapy0210/nlplot) - 顯示模組為自然語言處理
 * [rake-ja](https://github.com/kanjirz50/rake-ja) - 快速自動關鍵字提取算法
 * [jel](https://github.com/izuna385/jel) - 沒有任何證據顯示,
 * [MedNER-J](https://github.com/sociocom/MedNER-J) - 醫療用品的最新版本
 * [zunda-python](https://github.com/ikegami-yukino/zunda-python) - 達:Python的日本增強模式分析器客戶端.
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
 * [showcase](https://github.com/cl-tohoku/showcase) - 該網站的網站使用者將會在此網站上使用PyTorch.
 * [darts-clone-python](https://github.com/rixwew/darts-clone-python) - 子子綁定
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - 沒有任何關於日本的新聞,
 * [desuwa](https://github.com/megagonlabs/desuwa) - 基於KNP規則檔案的形狀和短語的特征注解器 (純Python)
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - 餐廳搜尋系統透過日文對話.
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - 日本語自然語言處理的示範編碼
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - 在Python中使用日本文本的小範例程式碼
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - 這項法律是日本版的,
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - EventGraph是用日文發明高層次NLP應用程式的開發平台.
 * [ishi](https://github.com/ku-nlp/ishi) - 義:日本人的意志分類器
 * [python-npylm](https://github.com/musyoku/python-npylm) - 沒有教師的形式分析,
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - 半教師的形式解析是透過結合條件付設概率場和基層階層語言模型,
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - 沒有教師,
 * [negima](https://github.com/cocodrips/negima) - 請使用您所定義的部分語言規則.
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - 抽取總結器使用BertSum作為總結模型
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - 語言中的日文數字解析器 (漢字,阿拉伯文).
 * [kantan](https://github.com/itayperl/kantan) - 搜尋根基圖案的日文單詞
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - 接收日文對話資料庫
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - 這是一篇日本文章的總結.
 * [chirptext](https://github.com/letuananh/chirptext) - 這裡有許多文本處理工具,
 * [yubin](https://github.com/alvations/yubin) - 沒有任何關於我們.
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - 日本語維基百科清潔器
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - 這是一本將日文轉換成語音的 Python 庫.
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - 這裡包含與"以情感為基礎的文字分類日本代幣化器的實驗評估"中的實驗相關的代碼.
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - 關於
This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - 生成Aozora Bunko的平面或代號化文本檔案
 * [JLM](https://github.com/jiali-ms/JLM) - 快速的LSTM語言模型,
 * [NTM](https://github.com/m3yrin/NTM) - 日本文章的神經主題建模的測試
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - 這是一本英文和日文的詞典,
 * [text-generation](https://github.com/discus0434/text-generation) - 輕鬆使用的程式碼, 能夠將GPT-2-JA與自己的文字調整,
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - 網頁上使用的圖像標語數據集.
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - 官方資料庫"UnihanLM:用Unihan資料庫進行粗略至細致的中日語言模型預訓練",
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - 執行mbart模型的細節調節代碼.
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - 沒有任何關於我們.
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - 該工具是為TinySegmenter製作學習模型的工具.
 * [Grongish](https://github.com/shogo82148/Grongish) - 語言的翻譯方式
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - 沒有使用Mecab (形素解析引擎) 來實現 WordCloud 中日文文字的形素解析式表示的程式.
 * [snark](https://github.com/hiraokusky/snark) - 網站使用者必須使用
 * [toEmoji](https://github.com/mkan0141/toEmoji) - 沒有任何可能的.
 * [termextract](https://github.com/kanjirz50/termextract) - 實踐如何實現抽取術語的算法.
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - 該網站的網站使用了 KenLM 的 N-gram 語言模型來評分,過濾或重新排名日本-對話-變更器的答案候選人.
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - 在Python中混合聯系模型和無限聯系模型的混合.
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - 隱藏馬爾科夫模型 (HMM) 和無限隱藏馬爾科夫模型 (iHMM)
 * [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) - 在Python中使用的語語言模型.
 * [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) - 自動語音識別與深度語音2模型在pytorch中,
 * [neural_ime](https://github.com/yohokuno/neural_ime) - 神經IME:神經輸入方法引擎
 * [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) - 能將羅馬語正確翻譯成日文嗎?
 * [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) - 已指定為日本的代號化器
 * [AugLy-jp](https://github.com/chck/AugLy-jp) - 在日本文本上增加數據
 * [furigana4epub](https://github.com/Mumumu4/furigana4epub) - 增加furigana到使用Mecab和Unidic的日本ePUB書.
 * [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) - 日本語動詞/形容詞曲工具
 * [jageocoder](https://github.com/t-sagara/jageocoder) - 純粹的Python日文地址地理編碼器
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - 這項計畫的目標是:
 * [nksnd](https://github.com/yoriyuki/nksnd) - 沒有任何關於我們.
 * [JaMIE](https://github.com/racerandom/JaMIE) - 日本醫學資訊提取工具組
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - 比較快速文字與word2vec,執行程式,學習程式.
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - 這就是最好的搜尋引擎.
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - 搜尋過去的字母,
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - 推特日文評論資料集的推特下載器
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - 根據Juman++和ConceptNet5.5的日文單詞集成
 * [jinf](https://github.com/hkiyomaru/jinf) - 日本的曲率轉換器
 * [kwja](https://github.com/ku-nlp/kwja) - 日本語的一體語言分析器
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - 基於面罩式語言模型分數 (ACL2020) 的複製包裝.
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - 果版的"果版"是一個很棒的工具.
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - 顯示,參與和告訴日本人
 * [cihai](https://github.com/cihai/cihai) - 語庫為CJK (中文,日文,韓文) 語言字典
 * [marine](https://github.com/6gsn/marine) - 語估計: 基于多項任務的日本口音
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - 沒有任何可能的.
 * [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) - 透過BERT和變壓器解碼器實現日本聊天機
 * [radicalchar](https://github.com/yamamaya/radicalchar) - 沒有任何關於我們.
 * [akaza](https://github.com/tokuhirom/akaza) - 還有另一台日本IME系統
 * [posuto](https://github.com/polm/posuto) - 這裡是日本的郵政編號.
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - 台灣的網路使用者
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - 沒有任何資訊.
 * [furiganapad](https://github.com/esrille/furiganapad) - 這種情況是非常嚴重的,
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - 這裡是日本的同義詞庫,
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - 沒有任何其他可供使用.
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - 這種情況是非常常見的.
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - 這裡有許多人使用GPT,
 * [shuwa](https://github.com/google/shuwa) - 擴展GNOME的畫面鍵盤
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - 這裡提供日本NLI模型的代碼,
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - 透過FuguMT進行日語-英語翻譯和英語-日語翻譯
 * [fugumt](https://github.com/s-taka/fugumt) - 翻譯環境使用公佈於Puru-fūū-fū-fū的機器翻譯引擎.
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - 透過使用前言論結構來進行自動評估
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - 沒有任何可能的.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namedivider-python](https://github.com/rskmoi/namedivider-python)|[![Downloads](https://pepy.tech/badge/namedivider-python/week)](https://pepy.tech/project/namedivider-python)|[![Downloads](https://pepy.tech/badge/namedivider-python)](https://pepy.tech/project/namedivider-python)|![GitHub Repo stars](https://img.shields.io/github/stars/rskmoi/namedivider-python?style=social)|
|[asa-python](https://github.com/ikegami-yukino/asa-python)|[![Downloads](https://pepy.tech/badge/asa/week)](https://pepy.tech/project/asa)|[![Downloads](https://pepy.tech/badge/asa)](https://pepy.tech/project/asa)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/asa-python?style=social)|
|[python_asa](https://github.com/Takeuchi-Lab-LM/python_asa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Takeuchi-Lab-LM/python_asa?style=social)|
|[toiro](https://github.com/taishi-i/toiro)|[![Downloads](https://pepy.tech/badge/toiro/week)](https://pepy.tech/project/toiro)|[![Downloads](https://pepy.tech/badge/toiro)](https://pepy.tech/project/toiro)|![GitHub Repo stars](https://img.shields.io/github/stars/taishi-i/toiro?style=social)|
|[ja-timex](https://github.com/yagays/ja-timex)|[![Downloads](https://pepy.tech/badge/ja-timex/week)](https://pepy.tech/project/ja-timex)|[![Downloads](https://pepy.tech/badge/ja-timex)](https://pepy.tech/project/ja-timex)|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/ja-timex?style=social)|
|[JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Kensuke-Mitsuzawa/JapaneseTokenizers?style=social)|
|[daaja](https://github.com/kajyuuen/daaja)|[![Downloads](https://pepy.tech/badge/daaja/week)](https://pepy.tech/project/daaja)|[![Downloads](https://pepy.tech/badge/daaja)](https://pepy.tech/project/daaja)|![GitHub Repo stars](https://img.shields.io/github/stars/kajyuuen/daaja?style=social)|
|[accel-brain-code](https://github.com/accel-brain/accel-brain-code)|[![Downloads](https://pepy.tech/badge/pysummarization/week)](https://pepy.tech/project/pysummarization)|[![Downloads](https://pepy.tech/badge/pysummarization)](https://pepy.tech/project/pysummarization)|![GitHub Repo stars](https://img.shields.io/github/stars/accel-brain/accel-brain-code?style=social)|
|[JGLUE](https://github.com/yahoojapan/JGLUE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yahoojapan/JGLUE?style=social)|
|[kyoto-reader](https://github.com/ku-nlp/kyoto-reader)|[![Downloads](https://pepy.tech/badge/kyoto-reader/week)](https://pepy.tech/project/kyoto-reader)|[![Downloads](https://pepy.tech/badge/kyoto-reader)](https://pepy.tech/project/kyoto-reader)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/kyoto-reader?style=social)|
|[nlplot](https://github.com/takapy0210/nlplot)|[![Downloads](https://pepy.tech/badge/nlplot/week)](https://pepy.tech/project/nlplot)|[![Downloads](https://pepy.tech/badge/nlplot)](https://pepy.tech/project/nlplot)|![GitHub Repo stars](https://img.shields.io/github/stars/takapy0210/nlplot?style=social)|
|[rake-ja](https://github.com/kanjirz50/rake-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kanjirz50/rake-ja?style=social)|
|[jel](https://github.com/izuna385/jel)|[![Downloads](https://pepy.tech/badge/jel/week)](https://pepy.tech/project/jel)|[![Downloads](https://pepy.tech/badge/jel)](https://pepy.tech/project/jel)|![GitHub Repo stars](https://img.shields.io/github/stars/izuna385/jel?style=social)|
|[MedNER-J](https://github.com/sociocom/MedNER-J)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/MedNER-J?style=social)|
|[zunda-python](https://github.com/ikegami-yukino/zunda-python)|[![Downloads](https://pepy.tech/badge/zunda-python/week)](https://pepy.tech/project/zunda-python)|[![Downloads](https://pepy.tech/badge/zunda-python)](https://pepy.tech/project/zunda-python)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/zunda-python?style=social)|
|[AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/AIO2_DPR_baseline?style=social)|
|[showcase](https://github.com/cl-tohoku/showcase)|[![Downloads](https://pepy.tech/badge/showcase-parser/week)](https://pepy.tech/project/showcase-parser)|[![Downloads](https://pepy.tech/badge/showcase-parser)](https://pepy.tech/project/showcase-parser)|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/showcase?style=social)|
|[darts-clone-python](https://github.com/rixwew/darts-clone-python)|[![Downloads](https://pepy.tech/badge/dartsclone/week)](https://pepy.tech/project/dartsclone)|[![Downloads](https://pepy.tech/badge/dartsclone)](https://pepy.tech/project/dartsclone)|![GitHub Repo stars](https://img.shields.io/github/stars/rixwew/darts-clone-python?style=social)|
|[jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/jrte-corpus_example?style=social)|
|[desuwa](https://github.com/megagonlabs/desuwa)|[![Downloads](https://pepy.tech/badge/desuwa/week)](https://pepy.tech/project/desuwa)|[![Downloads](https://pepy.tech/badge/desuwa)](https://pepy.tech/project/desuwa)|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/desuwa?style=social)|
|[HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/HotPepperGourmetDialogue?style=social)|
|[nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/upura/nlp-recipes-ja?style=social)|
|[Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/olsgaard/Japanese_nlp_scripts?style=social)|
|[DNorm-J](https://github.com/sociocom/DNorm-J)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/DNorm-J?style=social)|
|[pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph)|[![Downloads](https://pepy.tech/badge/pyknp-eventgraph/week)](https://pepy.tech/project/pyknp-eventgraph)|[![Downloads](https://pepy.tech/badge/pyknp-eventgraph)](https://pepy.tech/project/pyknp-eventgraph)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/pyknp-eventgraph?style=social)|
|[ishi](https://github.com/ku-nlp/ishi)|[![Downloads](https://pepy.tech/badge/ishi/week)](https://pepy.tech/project/ishi)|[![Downloads](https://pepy.tech/badge/ishi)](https://pepy.tech/project/ishi)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/ishi?style=social)|
|[python-npylm](https://github.com/musyoku/python-npylm)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/python-npylm?style=social)|
|[python-npycrf](https://github.com/musyoku/python-npycrf)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/python-npycrf?style=social)|
|[unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/musyoku/unsupervised-pos-tagging?style=social)|
|[negima](https://github.com/cocodrips/negima)|[![Downloads](https://pepy.tech/badge/negima/week)](https://pepy.tech/project/negima)|[![Downloads](https://pepy.tech/badge/negima)](https://pepy.tech/project/negima)|![GitHub Repo stars](https://img.shields.io/github/stars/cocodrips/negima?style=social)|
|[YouyakuMan](https://github.com/neilctwu/YouyakuMan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neilctwu/YouyakuMan?style=social)|
|[japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python)|[![Downloads](https://pepy.tech/badge/japanese-numbers-python/week)](https://pepy.tech/project/japanese-numbers-python)|[![Downloads](https://pepy.tech/badge/japanese-numbers-python)](https://pepy.tech/project/japanese-numbers-python)|![GitHub Repo stars](https://img.shields.io/github/stars/takumakanari/japanese-numbers-python?style=social)|
|[kantan](https://github.com/itayperl/kantan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/itayperl/kantan?style=social)|
|[make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/knok/make-meidai-dialogue?style=social)|
|[japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ryuryukke/japanese_summarizer?style=social)|
|[chirptext](https://github.com/letuananh/chirptext)|[![Downloads](https://pepy.tech/badge/chirptext/week)](https://pepy.tech/project/chirptext)|[![Downloads](https://pepy.tech/badge/chirptext)](https://pepy.tech/project/chirptext)|![GitHub Repo stars](https://img.shields.io/github/stars/letuananh/chirptext?style=social)|
|[yubin](https://github.com/alvations/yubin)|[![Downloads](https://pepy.tech/badge/yubin/week)](https://pepy.tech/project/yubin)|[![Downloads](https://pepy.tech/badge/yubin)](https://pepy.tech/project/yubin)|![GitHub Repo stars](https://img.shields.io/github/stars/alvations/yubin?style=social)|
|[jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner)|[![Downloads](https://pepy.tech/badge/jawiki-cleaner/week)](https://pepy.tech/project/jawiki-cleaner)|[![Downloads](https://pepy.tech/badge/jawiki-cleaner)](https://pepy.tech/project/jawiki-cleaner)|![GitHub Repo stars](https://img.shields.io/github/stars/hppRC/jawiki-cleaner?style=social)|
|[japanese2phoneme](https://github.com/iory/japanese2phoneme)|[![Downloads](https://pepy.tech/badge/japanese2phoneme/week)](https://pepy.tech/project/japanese2phoneme)|[![Downloads](https://pepy.tech/badge/japanese2phoneme)](https://pepy.tech/project/japanese2phoneme)|![GitHub Repo stars](https://img.shields.io/github/stars/iory/japanese2phoneme?style=social)
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
|[tinysegmenter](https://github.com/SamuraiT/tinysegmenter)|[![Downloads](https://pepy.tech/badge/tinysegmenter/week)](https://pepy.tech/project/tinysegmenter3)|[![Downloads](https://pepy.tech/badge/tinysegmenter3)](https://pepy.tech/project/tinysegmenter3)|![GitHub Repo stars](https://img.shields.io/github/stars/SamuraiT/tinysegmenter3?style=social)|
|[AugLy-jp](https://github.com/chck/AugLy-jp)|[![Downloads](https://pepy.tech/badge/AugLy-jp/week)](https://pepy.tech/project/AugLy-jp)|[![Downloads](https://pepy.tech/badge/AugLy-jp)](https://pepy.tech/project/AugLy-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/chck/AugLy-jp?style=social)|
|[furigana4epub](https://github.com/Mumumu4/furigana4epub)|[![Downloads](https://pepy.tech/badge/furigana4epub/week)](https://pepy.tech/project/furigana4epub)|[![Downloads](https://pepy.tech/badge/furigana4epub)](https://pepy.tech/project/furigana4epub)|![GitHub Repo stars](https://img.shields.io/github/stars/Mumumu4/furigana4epub?style=social)|
|[PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou)|[![Downloads](https://pepy.tech/badge/PyKatsuyou/week)](https://pepy.tech/project/PyKatsuyou)|[![Downloads](https://pepy.tech/badge/PyKatsuyou)](https://pepy.tech/project/PyKatsuyou)|![GitHub Repo stars](https://img.shields.io/github/stars/SmashinFries/PyKatsuyou?style=social)|
|[jageocoder](https://github.com/t-sagara/jageocoder)|[![Downloads](https://pepy.tech/badge/jageocoder/week)](https://pepy.tech/project/jageocoder)|[![Downloads](https://pepy.tech/badge/jageocoder)](https://pepy.tech/project/jageocoder)|![GitHub Repo stars](https://img.shields.io/github/stars/t-sagara/jageocoder?style=social)|
|[pygeonlp](https://github.com/geonlp-platform/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp/week)](https://pepy.tech/project/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp)](https://pepy.tech/project/pygeonlp)|![GitHub Repo stars](https://img.shields.io/github/stars/geonlp-platform/pygeonlp?style=social)|
|[nksnd](https://github.com/yoriyuki/nksnd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yoriyuki/nksnd?style=social)|
|[JaMIE](https://github.com/racerandom/JaMIE)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/racerandom/JaMIE?style=social)|
|[fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/fasttext-vs-word2vec-on-twitter-data?style=social)|
|[minimal-search-engine](https://github.com/GINK03/minimal-search-engine)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/minimal-search-engine?style=social)|
|[5ch-analysis](https://github.com/GINK03/5ch-analysis)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/GINK03/5ch-analysis?style=social)|
|[tweet_extructor](https://github.com/tatHi/tweet_extructor)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tatHi/tweet_extructor?style=social)|
|[japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/japanese-word-aggregation?style=social)|
|[jinf](https://github.com/hkiyomaru/jinf)|[![Downloads](https://pepy.tech/badge/jinf/week)](https://pepy.tech/project/jinf)|[![Downloads](https://pepy.tech/badge/jinf)](https://pepy.tech/project/jinf)|![GitHub Repo stars](https://img.shields.io/github/stars/hkiyomaru/jinf?style=social)|
|[kwja](https://github.com/ku-nlp/kwja)|[![Downloads](https://pepy.tech/badge/kwja/week)](https://pepy.tech/project/kwja)|[![Downloads](https://pepy.tech/badge/kwja)](https://pepy.tech/project/kwja)|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/kwja?style=social)|
|[mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Ryutaro-A/mlm-scoring-transformers?style=social)|
|[ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Japanese-Image-Captioning/ClipCap-for-Japanese?style=social)|
|[SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Japanese-Image-Captioning/SAT-for-Japanese?style=social)|
|[cihai](https://github.com/cihai/cihai)|[![Downloads](https://pepy.tech/badge/cihai/week)](https://pepy.tech/project/cihai)|[![Downloads](https://pepy.tech/badge/cihai)](https://pepy.tech/project/cihai)|![GitHub Repo stars](https://img.shields.io/github/stars/cihai/cihai?style=social)|
|[marine](https://github.com/6gsn/marine)|[![Downloads](https://pepy.tech/badge/marine/week)](https://pepy.tech/project/marine)|[![Downloads](https://pepy.tech/badge/marine)](https://pepy.tech/project/marine)|![GitHub Repo stars](https://img.shields.io/github/stars/6gsn/marine?style=social)|
|[whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sarulab-speech/whisper-asr-finetune?style=social)|
|[japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CjangCjengh/japanese_chatbot?style=social)|
|[radicalchar](https://github.com/yamamaya/radicalchar)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yamamaya/radicalchar?style=social)|
|[akaza](https://github.com/tokuhirom/akaza)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tokuhirom/akaza?style=social)|
|[posuto](https://github.com/polm/posuto)|[![Downloads](https://pepy.tech/badge/posuto/week)](https://pepy.tech/project/posuto)|[![Downloads](https://pepy.tech/badge/posuto)](https://pepy.tech/project/posuto)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/posuto?style=social)|
|[tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CjangCjengh/tacotron2-japanese?style=social)|
|[ibus-hiragana](https://github.com/esrille/ibus-hiragana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/ibus-hiragana?style=social)|
|[furiganapad](https://github.com/esrille/furiganapad)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/esrille/furiganapad?style=social)|
|[chikkarpy](https://github.com/WorksApplications/chikkarpy)|[![Downloads](https://pepy.tech/badge/chikkarpy/week)](https://pepy.tech/project/chikkarpy)|[![Downloads](https://pepy.tech/badge/chikkarpy)](https://pepy.tech/project/chikkarpy)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/chikkarpy?style=social)|
|[ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/p-geon/ja-tokenizer-docker-py?style=social)|
|[JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/oshizo/JapaneseEmbeddingEval?style=social)|
|[gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/karakuri-ai/gptuber-by-langchain?style=social)|
|[shuwa](https://github.com/google/shuwa)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/shuwa?style=social)|
|[japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/CyberAgentAILab/japanese-nli-model?style=social)|
|[tra-fugu](https://github.com/tos-kamiya/tra-fugu)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tos-kamiya/tra-fugu?style=social)|
|[fugumt](https://github.com/s-taka/fugumt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/s-taka/fugumt?style=social)|
|[JaSPICE](https://github.com/keio-smilab23/JaSPICE)|[![Downloads](https://pepy.tech/badge/JaSPICE/week)](https://pepy.tech/project/JaSPICE)|[![Downloads](https://pepy.tech/badge/JaSPICE)](https://pepy.tech/project/JaSPICE)|![GitHub Repo stars](https://img.shields.io/github/stars/keio-smilab23/JaSPICE?style=social)|
|[Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization?style=social)|


## C++

### Morphology analysis

 * [mecab](https://github.com/taku910/mecab) - 這也是日本的形狀分析器,
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - 曼++ (一種形狀分析工具組)
 * [kytea](https://github.com/neubig/kytea) - 京都文本分析工具包,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab](https://github.com/taku910/mecab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/mecab?style=social)|
|[jumanpp](https://github.com/ku-nlp/jumanpp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/jumanpp?style=social)|
|[kytea](https://github.com/neubig/kytea)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neubig/kytea?style=social)|

### Parsing

 * [cabocha](https://github.com/taku910/cabocha) - 另一位日本依賴結構分析器
 * [knp](https://github.com/ku-nlp/knp) - 日本的解析器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[cabocha](https://github.com/taku910/cabocha)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/cabocha?style=social)|
|[knp](https://github.com/ku-nlp/knp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/knp?style=social)|

### Others

 * [jsc](https://github.com/yohokuno/jsc) - 共同源頻道模型, 提供日文法轉換,中國字輸入和CJE混合輸入.
 * [aquaskk](https://github.com/codefirst/aquaskk) - 沒有形狀分析的輸入方法.
 * [mozc](https://github.com/google/mozc) - Mozc - 一款設計為多平台的日本輸入方法編輯器
 * [trimatch](https://github.com/tuem/trimatch) - :一個 (ExactabordPrefixabordApproximate) 字符串匹配圖書館
 * [resembla](https://github.com/tuem/resembla) - 類似的句子搜尋圖書館


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jsc](https://github.com/yohokuno/jsc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yohokuno/jsc?style=social)|
|[aquaskk](https://github.com/codefirst/aquaskk)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/codefirst/aquaskk?style=social)|
|[mozc](https://github.com/google/mozc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/mozc?style=social)|
|[trimatch](https://github.com/tuem/trimatch)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/trimatch?style=social)|
|[resembla](https://github.com/tuem/resembla)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/resembla?style=social)|


## Rust crate

### Morphology analysis

 * [lindera](https://github.com/lindera-morphology/lindera) - 形狀分析圖書館.
 * [vaporetto](https://github.com/daac-tools/vaporetto) - 非常加速的點性預測基於TOkenizer
 * [goya](https://github.com/Leko/goya) - 日本語形狀分析用寫
 * [vibrato](https://github.com/daac-tools/vibrato) - :基于維特比的加速標記器
 * [yoin](https://github.com/agatan/yoin) - 這是一款用純字寫的日本形狀分析器,
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 安全接器為mecab提供部分語音和形狀分析器圖書館
 * [awabi](https://github.com/nakagami/awabi) - 透過使用mecab字典的形狀分析器


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

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 工具庫,可檢查和轉換日文字符 - - 希拉加納,卡塔卡納和羅馬吉
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 存庫將日本半角卡納和全角英數轉換成正常字體
 * [kana](https://github.com/gbrlsnchs/kana) - 羅馬日文字轉換成黑拉加納或卡塔卡納的 CLI 程式.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[wana_kana_rust](https://github.com/PSeitz/wana_kana_rust)|-|![Crates.io](https://img.shields.io/crates/d/wana_kana)|![GitHub Repo stars](https://img.shields.io/github/stars/PSeitz/wana_kana_rust?style=social)|
|[unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs)|-|![Crates.io](https://img.shields.io/crates/d/unicode-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/gemmarx/unicode-jp-rs?style=social)|
|[kana](https://github.com/gbrlsnchs/kana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gbrlsnchs/kana?style=social)|


### Search engine library

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - 沒有任何關於我們.
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - 塔尼維使用Vibrato的代號化器.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy)|-|![Crates.io](https://img.shields.io/crates/d/lindera-tantivy)|![GitHub Repo stars](https://img.shields.io/github/stars/lindera-morphology/lindera-tantivy?style=social)|
|[tantivy-vibrato](https://github.com/akr4/tantivy-vibrato)|-|![Crates.io](https://img.shields.io/crates/d/tantivy-vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/akr4/tantivy-vibrato?style=social)|


### Others

 * [daachorse](https://github.com/daac-tools/daachorse) - 快速實現使用Aho-Corasick算法,
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - 找到所有相似文件的對,
 * [crawdad](https://github.com/daac-tools/crawdad) - 化自然語言字典庫使用字符式雙陣列試用.
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) - 其他代號化工具的比较代碼
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - 這裡提供了基准工具, 來比較數據結構的性能,
 * [vime](https://github.com/algon-320/vime) - 使用Vim作為X11應用程式的輸入方法
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - 提供免費的中等質量的文字閱讀軟體,
 * [akaza](https://github.com/akaza-im/akaza) - 還有另一台日本IME系統
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - 這是一本免費的網路,自主托管,多語言日文字典.
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - 果日文輸入用DvorakJP羅馬字母表
 * [niinii](https://github.com/Netdex/niinii) - 義大利語語語錄用語錄


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


## JavaScript

### Morphology analysis

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日本形狀分析器的JavaScript實現
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - 拉庫登MA - 單純用JavaScript寫的中文和日文形狀分析器 (字段分辨器+PoS標籤).
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - 還有其他關於Nodejs的Mecab包裝
 * [juman-bin](https://github.com/thammin/juman-bin) - 日本語形式素解析系統.
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - 沒有任何證據顯示,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji.js](https://github.com/takuyaa/kuromoji.js)|![npm](https://img.shields.io/npm/dw/kuromoji)|![npm](https://img.shields.io/npm/dt/kuromoji)|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/kuromoji.js?style=social)|
|[rakutenma](https://github.com/rakuten-nlp/rakutenma)|![npm](https://img.shields.io/npm/dw/rakutenma)|![npm](https://img.shields.io/npm/dt/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/rakuten-nlp/rakutenma?style=social)|
|[node-mecab-ya](https://github.com/golbin/mecab-ya)|![npm](https://img.shields.io/npm/dw/mecab-ya)|![npm](https://img.shields.io/npm/dt/mecab-ya)|![GitHub Repo stars](https://img.shields.io/github/stars/golbin/node-mecab-ya?style=social)|
|[juman-bin](https://github.com/thammin/juman-bin)|![npm](https://img.shields.io/npm/dw/juman-bin)|![npm](https://img.shields.io/npm/dt/juman-bin)|![GitHub Repo stars](https://img.shields.io/github/stars/thammin/juman-bin?style=social)|
|[node-mecab-async](https://github.com/hecomi/node-mecab-async)|![npm](https://img.shields.io/npm/dw/mecab-async)|![npm](https://img.shields.io/npm/dt/mecab-async)|![GitHub Repo stars](https://img.shields.io/github/stars/hecomi/node-mecab-async?style=social)|


### Converter

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - 提供日本語文庫, 能將日本語句子轉換成海拉加納,卡塔卡納或羅馬吉,
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - 沒有任何關於 Kuromoji 的相關貼子!
 * [hepburn](https://github.com/lovell/hepburn) - Node.js模組,可使用赫伯恩的羅曼化將日文語和卡塔卡納文字轉換為羅馬文
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - 轉換日文數字成數字
 * [jslingua](https://github.com/kariminf/jslingua) - 沒有任何關於JavaScript的資料.
 * [WanaKana](https://github.com/WaniKani/WanaKana) - 查找和轉寫海拉加納 <--> 加塔卡納 <--> 羅馬吉的JavaScript庫
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - 規范並解決羅馬吉名字常見問題.
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - 工具集, 使日本文本變得舊式


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


### Others

 * [bangumi-data](https://github.com/bangumi-data/bangumi-data) - 日本動漫的原始數據
 * [yomichan](https://github.com/FooSoft/yomichan) - 顯示了許多新語言,
 * [proofreading-tool](https://github.com/gecko655/proofreading-tool) - 圖文編輯工具,
 * [kanjigrid](https://github.com/minosvasilias/kanjigrid) - 顯示詹姆斯海西格的"記住漢字"第6版中所教的2200個漢字.
 * [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) - 漢字,利根,日文DB等的單字字
 * [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) - 解析句子的敬體和常體.
 * [hatsuon](https://github.com/DJTB/hatsuon) - 日本口音高低,
 * [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) - 情緒分析用JavaScript
 * [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) - 果語彙閱讀器
 * [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) - 這種日本語每天都有不同的字.
 * [oskim](https://github.com/esrille/oskim) - 擴展GNOME的畫面鍵盤
 * [tweetMapping](https://github.com/wtnv-lab/tweetMapping) - 這是一份數位檔案,


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


## Go

### Morphology analysis

 * [kagome](https://github.com/ikawaha/kagome) - 獨立的日本形狀分析器用純高寫


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kagome](https://github.com/ikawaha/kagome)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikawaha/kagome?style=social)|


### Others

 * [ojosama](https://github.com/jiro4989/ojosama) - 接著我們將文字轉換成風的風.
 * [nihongo](https://github.com/gojp/nihongo) - 日本語字典
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - 來自美國的字典輸入商.
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - 該網站的網站是日本語IME的IDOLM@STER字典 (由imas-db.jp提供)
 * [go-moji](https://github.com/ktnyt/go-moji) - 轉換Zenkaku/Hankaku的 Go 圖書館


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ojosama](https://github.com/jiro4989/ojosama)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jiro4989/ojosama?style=social)|
|[nihongo](https://github.com/gojp/nihongo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gojp/nihongo?style=social)|
|[yomichan-import](https://github.com/FooSoft/yomichan-import)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/FooSoft/yomichan-import?style=social)|
|[imas-ime-dic](https://github.com/maruamyu/imas-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/maruamyu/imas-ime-dic?style=social)|
|[go-moji](https://github.com/ktnyt/go-moji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ktnyt/go-moji?style=social)|


## Java

### Morphology analysis

 * [kuromoji](https://github.com/atilika/kuromoji) - 木是一款獨立且易於使用的日本形狀分析器,
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - 蘇達奇的詞典


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji](https://github.com/atilika/kuromoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/atilika/kuromoji?style=social)|
|[Sudachi](https://github.com/WorksApplications/Sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/Sudachi?style=social)|
|[SudachiDict](https://github.com/WorksApplications/SudachiDict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiDict?style=social)|


### Others

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 圖片中識別日文字符的Java圖書館
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 翻譯日本漢字為羅馬吉 (拉丁字母) 的Java圖書館和命令行工具
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - 漢字翻譯為海拉加納/卡塔卡納/羅馬吉,
 * [Kamite](https://github.com/fauu/Kamite) - 台式電腦學習日文的語言沉浸伴侶
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - 合式日本代碼化原生插件
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本分析器使用kuromoji日本代號化器進行彈性搜尋
 * [moji4j](https://github.com/andree-surya/moji4j) - 這是一本Java圖書館,
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - 關於日本語文字標準化器


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


## Pretrained model

### Word2Vec

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - 語言的語言與語言的語言.
 * [chiVe](https://github.com/WorksApplications/chiVe) - 包含南大和NWJC的日文字
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - 沒有任何關於我們.
 * [embedrank](https://github.com/yagays/embedrank) - 嵌入Rank的 Python 實現
 * [aovec](https://github.com/eggplants/aovec) - 簡單的 Word2Vec Builder - 藍天文庫所有書的 Word2Vec Builder+已建模
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - 這是AI LAB文章"係り受けに基づく日本語単語埋込 (依存性基於日語字嵌入) "的資料庫.
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - 還有另一種日本維基百科實體向量
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 透過MeCab在IPA字典和最新Neologd字典中進行形體解析, 並學習 word2vec,fastText,GloVe的字體分散表達,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/philipperemy/japanese-words-to-vectors?style=social)|
|[chiVe](https://github.com/WorksApplications/chiVe)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/chiVe?style=social)|
|[elmo-japanese](https://github.com/cl-tohoku/elmo-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/elmo-japanese?style=social)|
|[embedrank](https://github.com/yagays/embedrank)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/embedrank?style=social)|
|[aovec](https://github.com/eggplants/aovec)|[![Downloads](https://pepy.tech/badge/aovec/week)](https://pepy.tech/project/aovec)|[![Downloads](https://pepy.tech/badge/aovec)](https://pepy.tech/project/aovec)|![GitHub Repo stars](https://img.shields.io/github/stars/eggplants/aovec?style=social)|
|[dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/lapras-inc/dependency-based-japanese-word-embeddings?style=social)|
|[jawikivec](https://github.com/wikiwikification/jawikivec)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/wikiwikification/jawikivec?style=social)|
|[jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/kamigaito/jawiki_word_vector_updater?style=social)|


### Transformer based models

 * [bert-japanese](https://github.com/cl-tohoku/bert-japanese) - 這裡是日本的部落格.
 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - 提供由 rinna Co., Ltd 提供的日本預先訓練型號的產品代碼.
 * [bert-japanese](https://github.com/yoheikikuta/bert-japanese) - 還有日本文本的句子片.
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - 這種情況是非常常見的.
 * [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) - 該系統的使用者必須記錄在網站上,
 * [shiba](https://github.com/octanove/shiba) - 實現Pytorch並預先訓練日本模型,
 * [Dialog](https://github.com/reppy4620/Dialog) - 透過BERT和變壓器解碼器實現日本聊天機
 * [language-pretraining](https://github.com/retarfi/language-pretraining) - 該網站的網站使用者必須記錄在網站上,
 * [medbertjp](https://github.com/ou-medinfo/medbertjp) - 已受過預先訓練的BERT模型在日本醫學領域進行試驗.
 * [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) - 沒有任何關於我們.
 * [t5-japanese](https://github.com/megagonlabs/t5-japanese) - 預先訓練日本T5型號的編碼
 * [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) - 該網站的使用者必須使用
 * [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) - 網站內存與網站內存的使用
 * [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) - 日本BERT訓練模型
 * [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) - 必須要使用這些語言.
 * [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) - 經由 UniDic & SudachiPy 協助 MeCab 預先標示,
 * [sbert-ja](https://github.com/colorfulscoop/sbert-ja) - 訓練句子 BERT的代碼 抱擁臉型號中心的日本模型
 * [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) - 官方微調代碼"日本推特情緒分析與日本疫苗的比較"
 * [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) - 日本GPT2世代模型
 * [text2text-japanese](https://github.com/tanreinama/text2text-japanese) - 基于gpt-2的文本2文本轉換模型
 * [gpt-ja](https://github.com/colorfulscoop/gpt-ja) - 這種情況是很常見的.
 * [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) - 試圖讓西方人更容易/更容易使用日文, 透過使用拉丁/英語衍生的卡塔卡納詞彙,
 * [albert-japanese](https://github.com/alinear-corp/albert-japanese) - 還有日本文本的句子片.
 * [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) - 網站的網站是一個網站,
 * [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) - 這位在維基百科上受過訓練的日本DistilBERT模特.
 * [bert](https://github.com/informatix-inc/bert) - 這裡提供使用 RoBERTa 在日本語資料庫中預先訓練的片段. 我們的資料集包括日本語維基百科和網頁覽文章,總共25GB. 發布的模型是建立在 HuggingFace 的基於.
 * [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) - 拉博羅蒸酒
 * [luke](https://github.com/studio-ousia/luke) - 語言理解與知識基礎嵌入
 * [GPTSAN](https://github.com/tanreinama/GPTSAN) - 基於日語語言模式的通用轉換器
 * [japanese-clip](https://github.com/rinnakk/japanese-clip) - 日本的Rina Co., Ltd.
 * [AcademicBART](https://github.com/EhimeNLP/AcademicBART) - 我們在學術資料庫 CiNii Articles 的紙上進行了基于 BART 的日文蒙面語言模型的預訓練.
 * [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) - 我們在學術資料庫CiNii Articles的紙上摘要上進行了基于RoBERTa的日本化面具語言模型的預訓練.
 * [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) - 經由日本網頁文本的131GB進行預先訓練.
 * [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) - 透過Stanford Alpaca的數據集翻譯成日文,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[bert-japanese](https://github.com/cl-tohoku/bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/bert-japanese?style=social)|
|[japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/rinnakk/japanese-pretrained-models?style=social)|
|[bert-japanese](https://github.com/yoheikikuta/bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yoheikikuta/bert-japanese?style=social)|
|[SudachiTra](https://github.com/WorksApplications/SudachiTra)|[![Downloads](https://pepy.tech/badge/SudachiTra/week)](https://pepy.tech/project/SudachiTra)|[![Downloads](https://pepy.tech/badge/SudachiTra)](https://pepy.tech/project/SudachiTra)|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiTra?style=social)|
|[japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nttcslab/japanese-dialog-transformers?style=social)|
|[shiba](https://github.com/octanove/shiba)|[![Downloads](https://pepy.tech/badge/shiba-model/week)](https://pepy.tech/project/shiba-model)|[![Downloads](https://pepy.tech/badge/shiba-model)](https://pepy.tech/project/shiba-model)|![GitHub Repo stars](https://img.shields.io/github/stars/octanove/shiba?style=social)|
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


## ChatGPT

 * [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) - 透過網路通訊,
 * [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) - 我們正在研發AITuber的基礎部分.
 * [wanna](https://github.com/hirokidaichi/wanna) - 牌命令發射器使用自然語言
 * [ChatdollKit](https://github.com/uezo/ChatdollKit) - 聊天工具讓你將你的3D模型變成聊天機
 * [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) - 關於日本語的GUI
 * [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) - 這款服務器是搭載ChatGPT 3.5的"AI妹妹艾".
 * [vrchatbot](https://github.com/Geson-anko/vrchatbot) - 提供一個可供使用的資料庫.
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - 這裡有許多人使用GPT,
 * [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) - 透過 Open AI 文字完成終點建立的 Nuxt 3 聊天盒應用程式.您可以選擇您的 AI 朋友的不同性格.預設會用日文回應.您可以使用此應用程式練習您的尼宏技能!
 * [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) - 這項 Chrome 擴展可以使用 ChatGPT 將選定的日文翻譯成海拉加納.
 * [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) - 這樣的情況是, 透過使用Retrieval Augmented Generation模式,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Yuchi-Games/VRChatGPT?style=social)|
|[AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/M-gen/AITuberDegikkoMirii?style=social)|
|[wanna](https://github.com/hirokidaichi/wanna)|[![Downloads](https://pepy.tech/badge/wanna/week)](https://pepy.tech/project/wanna)|[![Downloads](https://pepy.tech/badge/wanna)](https://pepy.tech/project/wanna)|![GitHub Repo stars](https://img.shields.io/github/stars/hirokidaichi/wanna?style=social)|
|[ChatdollKit](https://github.com/uezo/ChatdollKit)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/uezo/ChatdollKit?style=social)|
|[ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gyokuro33/ChuanhuChatGPTJapanese?style=social)|
|[AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/manju-summoner/AISisterAIChan?style=social)|
|[vrchatbot](https://github.com/Geson-anko/vrchatbot)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Geson-anko/vrchatbot?style=social)|
|[gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/karakuri-ai/gptuber-by-langchain?style=social)|
|[openai-chatfriend](https://github.com/supershaneski/openai-chatfriend)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/supershaneski/openai-chatfriend?style=social)|
|[chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt?style=social)|
|[azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nohanaga/azure-search-openai-demo?style=social)|


## Dictionary

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - 基于網路上的語言資源的新詞彙
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - 這是一台日本口音字典生成器,
 * [jamdict](https://github.com/neocl/jamdict) - 該網站的使用者必須在使用者之前,
 * [unidic-py](https://github.com/polm/unidic-py) - 裝置使用管道.
 * [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) - 該公司的經驗與經驗
 * [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) - 這裡是我最愛的部落格.
 * [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) - 來自維基百科的SKK/MeCab字典
 * [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) - 字典找到與文字相關的情感
 * [JumanDIC](https://github.com/ku-nlp/JumanDIC) - 這裡包含了源字典檔案,
 * [ipadic-py](https://github.com/polm/ipadic-py) - 提供了IPAdic包裝,
 * [unidic-lite](https://github.com/polm/unidic-lite) - 這是一款小型版本的UniDic,
 * [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) - 提供日本語圖形字母輸入的IME, 附加字典 orange_book Google 日本語輸入等, 允許將日文轉換為圖形字母的IME擴展字典
 * [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) - 增加日英文轉換及英語簡略展開的IME字典 orange_book 擴展IME字典,可使用Google日語輸入,ATOK等來將日語轉換及英語簡略展開
 * [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) - 尼古尼科百科和皮克西布百科的共同部分IME字典
 * [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) - 該網站的網站是GoogleIME使用カタカナ語詞典計畫的檔案.
 * [emoticon](https://github.com/tiwanari/emoticon) -  (), (), ()
 * [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) - 這項計畫是為將開源Mozc字典轉換成MeCab字典格式.
 * [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) - 微軟IME等應用程式使用的"電訊部"相關詞彙.
 * [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) - 這是一本由微軟 IME等應用程式所設計的""相關詞彙詞典.
 * [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) - 這裡是微軟 IME等網站所使用的,目前已知的所有波克蒙名稱的詞典.
 * [EJDict](https://github.com/kujirahand/EJDict) - 義語-日語字典資料 (公開領域)
 * [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) - 們使用貴貌的詞畫來使用正當的日文.
 * [genshin-dict](https://github.com/kotofurumiya/genshin-dict) - 這是一本可用於Windows/macOS的原始詞典.
 * [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) - 在 JSON格式中使用 JMdict 和 JMnedict
 * [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) - 將外部詞語轉換成Mozc系統字典


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neologd/mecab-ipadic-neologd?style=social)|
|[tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/PKSHATechnology-Research/tdmelodic?style=social)|
|[jamdict](https://github.com/neocl/jamdict)|[![Downloads](https://pepy.tech/badge/jamdict/week)](https://pepy.tech/project/jamdict)|[![Downloads](https://pepy.tech/badge/jamdict)](https://pepy.tech/project/jamdict)|![GitHub Repo stars](https://img.shields.io/github/stars/neocl/jamdict?style=social)|
|[unidic-py](https://github.com/polm/unidic-py)|[![Downloads](https://pepy.tech/badge/unidic/week)](https://pepy.tech/project/unidic)|[![Downloads](https://pepy.tech/badge/unidic)](https://pepy.tech/project/unidic)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/unidic-py?style=social)|
|[Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/Japanese-Company-Lexicon?style=social)|
|[manbyo-sudachi](https://github.com/yagays/manbyo-sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yagays/manbyo-sudachi?style=social)|
|[jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tokuhirom/jawiki-kana-kanji-dict?style=social)|
|[JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sociocom/JIWC-Dictionary?style=social)|
|[JumanDIC](https://github.com/ku-nlp/JumanDIC)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/JumanDIC?style=social)|
|[ipadic-py](https://github.com/polm/ipadic-py)|[![Downloads](https://pepy.tech/badge/ipadic/week)](https://pepy.tech/project/ipadic)|[![Downloads](https://pepy.tech/badge/ipadic)](https://pepy.tech/project/ipadic)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/ipadic-py?style=social)|
|[unidic-lite](https://github.com/polm/unidic-lite)|[![Downloads](https://pepy.tech/badge/unidic-lite/week)](https://pepy.tech/project/unidic-lite)|[![Downloads](https://pepy.tech/badge/unidic-lite)](https://pepy.tech/project/unidic-lite)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/unidic-lite?style=social)|
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


## Corpus

### Part-of-speech tagging / Named entity recognition

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - 來自日本的語言
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 沒有任何關於"日本"的消息.
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter 科普
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - 沒有任何可能的.
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - 來自Google UDT 2.0的日語數據.
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大學網站文件引導資料庫
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 註解: 福山凱多里中心資料庫


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

 * [small_parallel_enja](https://github.com/odashi/small_parallel_enja) - 沒有任何關於日本語的相關報導.
 * [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) - 網頁搜尋日本與中國的 NMT
 * [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) - 學習者可使用Coursera Corpus Mining及多階段精準調整,
 * [JESC](https://github.com/rpryzant/JESC) - 這裡有許多英語與日文,
 * [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) - 其他國家的會議
 * [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) - 這份目錄包含一大批日語-英語字幕資料庫.
 * [jesc_small](https://github.com/yusugomori/jesc_small) - 字幕提供日語-英語字幕
 * [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) - 沒有任何關於""的相關資訊.
 * [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) - 韓國電腦科學術語對比.
 * [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) - 建立日語與英語並行資料庫及訓練NMT模型的脚本
 * [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) - 這裡有許多不同的網站,


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

 * [JMRD](https://github.com/ku-nlp/JMRD) - 這裡是日本電影推薦資料集.
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - 透過覽與編輯,
 * [BSD](https://github.com/tsuruoka-lab/BSD) - 商界對話資料庫
 * [asdc](https://github.com/megagonlabs/asdc) - 住宿搜尋對話資料庫 (宿泊施設探索対話コーパス)
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - 這裡是日本語的對話數據,
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - 這份資料庫包含了在AACL-IJCNLP 2022年研討會Eval4NLP 2022上發表的日本英雙語聊天資料庫BPersona-chat.
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 日本日日對話,或日本語日常對話コーパス, 是一個高品質的多轉對話資料集, 包含關於五個主題的日常對話:日常生活,學校,旅行,健康和娛樂.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[JMRD](https://github.com/ku-nlp/JMRD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/JMRD?style=social)|
|[open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/1never/open2ch-dialogue-corpus?style=social)|
|[BSD](https://github.com/tsuruoka-lab/BSD)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tsuruoka-lab/BSD?style=social)|
|[asdc](https://github.com/megagonlabs/asdc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/megagonlabs/asdc?style=social)|
|[japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MokkeMeguru/japanese-corpus?style=social)|
|[BPersona-chat](https://github.com/cl-tohoku/BPersona-chat)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/BPersona-chat?style=social)|
|[japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jqk09a/japanese-daily-dialogue?style=social)|

### Others

 * [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) - 沒有任何關於日本實際文本含義資料庫的相關資料.
 * [kanji-data](https://github.com/davidluzgouveia/kanji-data) - 具有更新的JLPT水平和 WaniKani資訊的JSON漢字數據集
 * [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) - 日本語字類相似性資料集
 * [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) - 簡化日本文本的翻譯資料庫
 * [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) - 查基的以觀點為基礎的情緒分析資料集
 * [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) - 該網站的網站是日本語版的網站,
 * [JaNLI](https://github.com/verypluming/JaNLI) - 日本對抗性自然語言推論資料集
 * [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) - 根據證據的解釋資料集 (AACL-IJCNLP 2020)
 * [emoji-ja](https://github.com/yagays/emoji-ja) - 單字字母的日文閱讀/關鍵字/分類字典
 * [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) - 來自維基百科的日語名稱集資料集
 * [ja.text8](https://github.com/Hironsan/ja.text8) - 沒有任何關於日本語的資訊.
 * [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) - 這就是我想要的.
 * [japanese](https://github.com/hingston/japanese) - 這份報告包含了利兹大學校內資料庫所決定的44998個最常見的日文單詞,
 * [kanji-frequency](https://github.com/scriptin/kanji-frequency) - 來自各種來源收集的漢字使用頻率數據
 * [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) - 沒有任何關於我們的消息.
 * [CoARiJ](https://github.com/chakki-works/CoARiJ) - 日本年度報告集
 * [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) - 關於日本的技術資料庫/工具
 * [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) - 部分字段註解 ITA 資料
 * [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) - 維基百科文字預先處理的實用程式程式
 * [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) - 收集日本語中的不當表達.
 * [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) - 參加會議的會員,議員,議案及提問主題資料.
 * [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) - 國會法案資料庫:國會議院
 * [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) - 照片來自 果版
 * [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) - 維諾格拉德方案挑戰的日文翻譯
 * [speechBSD](https://github.com/ku-nlp/speechBSD) - 具有音訊和音箱屬性資訊的 BSD 資料庫的擴展
 * [ita-corpus](https://github.com/mmorise/ita-corpus) - 沒有任何關於我,
 * [rohan4600](https://github.com/mmorise/rohan4600) - 沒有任何關於日本的新聞.
 * [anlp-jp-history](https://github.com/whym/anlp-jp-history) - 語言處理學會年會演講的完整列表,
 * [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) - 語言翻譯任務中的評估資料集
 * [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) - 日本語中的英文借用詞
 * [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) - 日本語維基百科維基資料庫
 * [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) - 這是日本總理的一般政策演講.
 * [wrime](https://github.com/ids-cv/wrime) - 沒有任何證據顯示,
 * [jtubespeech](https://github.com/sarulab-speech/jtubespeech) - JTubeSpeech:來自YouTube的日語語彙集
 * [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) - 常用日本語維基百科的單詞列表
 * [kokkosho_data](https://github.com/rindybell/kokkosho_data) - 沒有任何關於車輛故障的資料集.
 * [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) - 數字化資料是OCR文本化事業所製作的學習資料集,
 * [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) - 來自國家雜誌資料的數據集.
 * [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) - 這裡是日本的第一間廣告公司,
 * [hirakanadic](https://github.com/po3rin/hirakanadic) - 允許Sudachi從任何複合詞列表中將海拉根改為卡塔卡納
 * [animedb](https://github.com/anilogia/animedb) - 數據庫裡的動畫作品,
 * [security_words](https://github.com/SaitoLab/security_words) - 網路安全與公共組織相關的日英回應
 * [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) - 數據來自日本國會議員,
 * [honkoku-data](https://github.com/yuta1984/honkoku-data) - 歷史資料的公民參與型翻刻平台『みんなで翻刻』的文字資料置き場です。/在日本歷史文獻群眾轉錄平台Minna de Honkoku (https://honkoku.org) 上創建的抄錄文本.
 * [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) - 關於我們:
 * [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) - 工程師的日語/英語詞彙列表
 * [JSICK](https://github.com/verypluming/JSICK) - 包含組成知識的日本語句子 (JSICK) 資料集/JSICK壓力測試集
 * [phishurl-list](https://github.com/JPCERTCC/phishurl-list) - 魚網址資料集來自JPCERT/CC
 * [jcms](https://github.com/shigashiyama/jcms) - 許多專業領域的日本資料庫 (JCMS)
 * [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) - 只有文字檔案的 www.aozora.gr.jp
 * [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) - friendly_JA是一份平行日語與日語資料庫,旨在使用拉丁/英語衍生卡塔卡納詞彙,
 * [topokanji](https://github.com/scriptin/topokanji) - 具體的學習目的,
 * [isbn4groups](https://github.com/uribo/isbn4groups) - 關於ISBN-13中的日文出版物 (978-4-XXXXXXXXX) 的數據等
 * [NMeCab](https://github.com/komutan/NMeCab) - 關於.NET上的日本形狀分析器
 * [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) - 數位化資料的數據集
 * [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) - 該網站的源代碼為
 * [data_set](https://github.com/japanese-law-analysis/data_set) - 沒有任何證據顯示,
 * [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) - 關於 huggingface數據集的 WRIME
 * [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) - 數據庫裡的數據是數據庫中使用的數據,
 * [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) - 該網站的網站是一個非常有趣的網站.
 * [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) - 沒有任何相關資訊.
 * [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) - 日本直播新聞資料庫
 * [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) - 關於日本的一般語言理解
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - 反映日本注解者的常識道德.
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - 沒有任何證據顯示
 * [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) - 關於日本的對話
 * [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) - 提供日本毒性方案的方案和數據集.
 * [camera](https://github.com/CyberAgentAILab/camera) - 網路代理多模式評估廣告文字基因分析 (CAMERA) 是日本的廣告文字生成數據集.
 * [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) - 沒有任何關於日本的新聞.
 * [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) - 沒有任何關於我們.
 * [copa-japanese](https://github.com/nlp-titech/copa-japanese) - 這裡是日本的COPA資料集.
 * [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) - 字母熟悉率為"用語意原理列表 (WLSP) "
 * [ProSub](https://github.com/matbahasa/ProSub) - 跨語言研究代名詞和地址詞
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - 反映日本注解者的常識道德.
 * [ramendb](https://github.com/nuko-yokohama/ramendb) - 沒有任何方法可以取資料.
 * [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) - 網路代理多模式評估廣告文字基因編輯 (CAMERA)
 * [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) - 實際檢查句子NLI數據集
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - 這裡是用於 databricks/dolly-v2-12b 的學習數據的 databricks-dolly-15k.jsonl 翻譯成日文的數據集.
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELD是基于MELD的情感感應用語音翻譯的日英文數據集.


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
|[hirakanadic](https://github.com/po3rin/hirakanadic)|[![Downloads](https://pepy.tech/badge/hirakanadic/week)](https://pepy.tech/project/hirakanadic)|[![Downloads](https://pepy.tech/badge/hirakanadic)](https://pepy.tech/project/hirakanadic)|![GitHub Repo stars](https://img.shields.io/github/stars/po3rin/hirakanadic?style=social)|
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


## Tutorial

 * [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) - 接著我們開始使用""這個詞,
 * [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) - 訓練快速文字的教程
 * [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) - 關於日本語的特有的表達抽取
 * [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) - 經驗使用車輛和PyTorch對日本文字的分類
 * [ginza-examples](https://github.com/poyo46/ginza-examples) - 這裡是日本NLP圖書館的首頁.
 * [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) - 文件分類使用BERT-日文
 * [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) - 這就是如何動手使用日本語BERT.
 * [bert-book](https://github.com/stockmarkteam/bert-book) - 接著我們將會看到更多的資訊.
 * [janome-tutorial](https://github.com/mocobeta/janome-tutorial) - 這是一本關於使用 Janome 來開發文字的教學.
 * [handson-language-models](https://github.com/hnishi/handson-language-models) - 這裡是日本語語言模型的漢字資料.
 * [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) - 試用使用 Google Colab 來測試日本語文字推理.
 * [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) - 這裡是pytorch的日本語版資料庫.
 * [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) -【2023年版】BERTによるテキスト分類


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

## Research summary

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 已接受預先訓練的日本語 BERT 模型列表,
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 收集和分類有關文法誤區的日文文獻的資料庫
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - 文本庫列表及其他資料 (主要是日文)
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - 如何在深度學習模式中最大限度地提高性能.
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 嘗試將日本語音調,尤其是音高口音資源整合到一份名單中,


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/himkt/awesome-bert-japanese?style=social)|
|[GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gotutiyan/GEC-Info-ja?style=social)|
|[dataset-list](https://github.com/ikegami-yukino/dataset-list)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/dataset-list?style=social)|
|[tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Valkyrja3607/tuning_playbook_ja?style=social)|
|[japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/olety/japanese-pitch-accent-resources?style=social)|


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
