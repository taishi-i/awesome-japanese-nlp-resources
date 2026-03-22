# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專用於 Python 庫、預訓練模型、詞典和日語 NLP 語料庫的精選資源列表

- [列出了848個GitHub倉庫的資訊 ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md)
- [列出了273個Hugging Face倉庫的資訊（模型和數據集） ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) を掲載中
- 🎉 我們於2026年3月1日正式發布了日語NLP資源調查工具 [awesome-japanese-nlp-survey](https://awesome-japanese-nlp-survey.vercel.app/)！

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## 🎉 The latest additions

**Corpus**
 * [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) - 軟體圖理解的VLM評估基準（日文、英文、韓文對應）
 * [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) - 在日本語人事勞務領域中，LLM的性能評估基準的長篇內容Benchmark

_Updated on Mar 22, 2026_

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
將日文分詞並標註詞性與基本形的函式庫

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
 * [Mecari](https://github.com/zbller/Mecari) - Mecari（使用图神经网络进行日语形态分析）


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [SudachiPy](https://github.com/WorksApplications/SudachiPy) | 📥 326k | 📦 62M | ⭐ 429 | 🔴 october 2022|
| 🔗 [Janome](https://github.com/mocobeta/janome) | 📥 84k | 📦 11M | ⭐ 907 | 🟡 october 2025|
| 🔗 [mecab-python3](https://github.com/SamuraiT/mecab-python3) | 📥 164k | 📦 36M | ⭐ 580 | 🟡 november 2025|
| 🔗 [mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python) | 📥 16k | 📦 679k | ⭐ 272 | 🔴 october 2024|
| 🔗 [fugashi](https://github.com/polm/fugashi) | 📥 106k | 📦 14M | ⭐ 516 | 🟡 october 2025|
| 🔗 [nagisa](https://github.com/taishi-i/nagisa) | 📥 40k | 📦 8M | ⭐ 415 | 🟢 february|
| 🔗 [pyknp](https://github.com/ku-nlp/pyknp) | 📥 2k | 📦 3M | ⭐ 92 | 🟢 january|
| 🔗 [Mykytea-python](https://github.com/chezou/Mykytea-python) | 📥 950 | 📦 556k | ⭐ 36 | 🔴 january 2024|
| 🔗 [konoha](https://github.com/himkt/konoha) | 📥 61k | 📦 6M | ⭐ 261 | 🟢 march|
| 🔗 [natto-py](https://github.com/buruzaemon/natto-py) | 📥 341k | 📦 34M | ⭐ 95 | 🔴 november 2023|
| 🔗 [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) | 📥 13 | 📦 27k | ⭐ 23 | 🔴 may 2017|
| 🔗 [python-vaporetto](https://github.com/daac-tools/python-vaporetto) | 📥 285 | 📦 175k | ⭐ 21 | 🟡 june 2025|
| 🔗 [dango](https://github.com/mkartawijaya/dango) | 📥 58 | 📦 26k | ⭐ 25 | 🔴 november 2021|
| 🔗 [rhoknp](https://github.com/ku-nlp/rhoknp) | 📥 18k | 📦 1M | ⭐ 38 | 🟢 january|
| 🔗 [python-vibrato](https://github.com/daac-tools/python-vibrato) | 📥 304 | 📦 117k | ⭐ 43 | 🔴 september 2024|
| 🔗 [jagger-python](https://github.com/lighttransport/jagger-python) | 📥 2k | 📦 298k | ⭐ 13 | 🔴 march 2024|
| 🔗 [Mecari](https://github.com/zbller/Mecari) | - | - | ⭐ 39 | 🟡 september 2025|


### Parsing
分析日文句法與依存結構的函式庫

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
 * [lightblue](https://github.com/daisukebekki/lightblue) - 一個具有DTS表示的日語CCG解析器
 * [natsume-simple](https://github.com/borh-lab/natsume-simple) - natsume-simple是一個日語的依存關係搜索系統。
 * [jdeppy](https://github.com/matsurih/jdeppy) - Python 封裝器用於 J.DepP，快速的日語依存分析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ginza](https://github.com/megagonlabs/ginza) | 📥 14k | 📦 2M | ⭐ 838 | 🔴 march 2024|
| 🔗 [cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python) | 📥 42 | 📦 54k | ⭐ 7 | 🔴 august 2022|
| 🔗 [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) | 📥 485 | 📦 329k | ⭐ 38 | 🟡 december 2025|
| 🔗 [camphr](https://github.com/PKSHATechnology-Research/camphr) | 📥 225 | 📦 269k | ⭐ 337 | 🔴 august 2021|
| 🔗 [SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic) | 📥 249 | 📦 119k | ⭐ 20 | 🔴 repo not found|
| 🔗 [depccg](https://github.com/masashi-y/depccg) | 📥 52 | 📦 46k | ⭐ 98 | 🔴 august 2023|
| 🔗 [bertknp](https://github.com/ku-nlp/bertknp) | - | - | ⭐ 23 | 🔴 october 2021|
| 🔗 [esupar](https://github.com/KoichiYasuoka/esupar) | 📥 472 | 📦 170k | ⭐ 55 | 🟢 february|
| 🔗 [yomikata](https://github.com/passaglia/yomikata) | 📥 40 | 📦 50k | ⭐ 32 | 🔴 october 2023|
| 🔗 [jdepp-python](https://github.com/lighttransport/jdepp-python) | 📥 2k | 📦 283k | ⭐ 4 | 🔴 february 2024|
| 🔗 [lightblue](https://github.com/daisukebekki/lightblue) | - | - | ⭐ 27 | 🟢 last friday|
| 🔗 [natsume-simple](https://github.com/borh-lab/natsume-simple) | - | - | ⭐ 5 | 🔴 february 2025|
| 🔗 [jdeppy](https://github.com/matsurih/jdeppy) | 📥 20 | 📦 11k | ⭐ 3 | 🔴 february 2022|


### Converter
在假名、羅馬字與全形半形之間轉換的函式庫

 * [pykakasi](https://github.com/miurahr/pykakasi) - 輕量級的轉換器，可將日文假名漢字句子轉換為假名羅馬字。
 * [cutlet](https://github.com/polm/cutlet) - Python中的日文轉羅馬字轉換器
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - 將英文字母轉換為片假名
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - 將阿拉伯數字或「西方」風格的數字轉換為日本上下文。
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Python的Mozc：假名漢字轉換器
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - 日文文本解析器，將平假名/片假名字符串分離成音節（拼音）。
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - 將日文轉換為音素序列的腳本
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - 一個快速的字符轉換和音譯庫，基於日本國稅廳的法人番號系統定義的方案。
 * [wiredify](https://github.com/eggplants/wiredify) - 將日文假名從ba-bi-bu-be-bo轉換為va-vi-vu-ve-vo將日文假名從ba-bi-bu-be-bo轉換為va-vi-vu-ve-vo
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - 使用MeCab獲取日文讀音（yomigana）和重音的簡單Python套件（CLI/Python API）。
 * [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) - 執行NormalizeNumexp的Python實作，進行數量表達和時間表達的提取和規範化。
 * [Jusho](https://github.com/nagataaaas/Jusho) - 日本郵政編碼數據的簡單封裝
 * [yurenizer](https://github.com/sea-turt1e/yurenizer) - 日文文本正規化工具，解決拼寫不一致。
 * [e2k](https://github.com/Patchethium/e2k) - 一個用於自動將英文轉換為片假名的工具
 * [alkana.py](https://github.com/zomysan/alkana.py) - 一個可以獲取字母串的片假名讀音的工具。
 * [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) - 將英文文字轉換為片假名的程式
 * [kanjiconv](https://github.com/sea-turt1e/kanjiconv) - 漢字轉換器到平假名、片假名、羅馬字母。
 * [kanjize](https://github.com/nagataaaas/kanjize) - Kanjize(カンジャイズ): 簡單的漢字數字和整數轉換器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [pykakasi](https://github.com/miurahr/pykakasi) | 📥 321k | 📦 29M | ⭐ 444 | 🔴 july 2022|
| 🔗 [cutlet](https://github.com/polm/cutlet) | 📥 18k | 📦 1M | ⭐ 373 | 🟡 june 2025|
| 🔗 [alphabet2kana](https://github.com/shihono/alphabet2kana) | 📥 234 | 📦 58k | ⭐ 14 | 🟢 february|
| 🔗 [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) | - | - | ⭐ 50 | 🔴 november 2020|
| 🔗 [mozcpy](https://github.com/ikegami-yukino/mozcpy) | 📥 173 | 📦 13k | ⭐ 47 | 🔴 february 2025|
| 🔗 [jamorasep](https://github.com/tachi-hi/jamorasep) | 📥 82 | 📦 9k | ⭐ 11 | 🟢 february|
| 🔗 [text2phoneme](https://github.com/korguchi/text2phoneme) | - | - | ⭐ 13 | 🔴 may 2023|
| 🔗 [jntajis-python](https://github.com/opencollector/jntajis-python) | 📥 2k | 📦 115k | ⭐ 21 | 🟢 march|
| 🔗 [wiredify](https://github.com/eggplants/wiredify) | 📥 32 | 📦 6k | ⭐ 3 | 🟡 december 2025|
| 🔗 [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) | 📥 28 | 📦 4k | ⭐ 7 | 🟢 february|
| 🔗 [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) | 📥 16 | 📦 14k | ⭐ 8 | 🔴 april 2024|
| 🔗 [Jusho](https://github.com/nagataaaas/Jusho) | 📥 145 | 📦 55k | ⭐ 11 | 🔴 june 2024|
| 🔗 [yurenizer](https://github.com/sea-turt1e/yurenizer) | 📥 96 | 📦 18k | ⭐ 4 | 🔴 march 2025|
| 🔗 [e2k](https://github.com/Patchethium/e2k) | 📥 193 | 📦 25k | ⭐ 16 | 🟡 november 2025|
| 🔗 [alkana.py](https://github.com/zomysan/alkana.py) | - | - | ⭐ 34 | 🔴 october 2021|
| 🔗 [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) | - | - | ⭐ 4 | 🟢 february|
| 🔗 [kanjiconv](https://github.com/sea-turt1e/kanjiconv) | 📥 95 | 📦 12k | ⭐ 17 | 🟡 october 2025|
| 🔗 [kanjize](https://github.com/nagataaaas/kanjize) | 📥 17k | 📦 1M | ⭐ 68 | 🟡 june 2025|


### Preprocessor
在分析前進行文字正規化與清理的函式庫

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - mecab-neologd 的日文文本正規化工具
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - 純Python日文字符互轉器，支援平假名、片假名、半角和全角。
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - 一個快速轉換日文半角和全角字符的轉換器
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 一款強大的日文網頁文本清理工具
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 構成並管理多個前處理的文字前處理工具
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuho是一個Python模組，用於在日語中半角片假名和全角片假名之間進行雙向轉換。
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - 另一個快速的日本字符串轉換器
 * [kairyou](https://github.com/bikatr7/kairyou) - 使用SpaCy快速預處理日文文本，以進行日文翻譯或其他NLP任務。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [neologdn](https://github.com/ikegami-yukino/neologdn) | 📥 7k | 📦 1M | ⭐ 287 | 🟡 december 2025|
| 🔗 [jaconv](https://github.com/ikegami-yukino/jaconv) | 📥 556k | 📦 63M | ⭐ 342 | 🟢 february|
| 🔗 [mojimoji](https://github.com/studio-ousia/mojimoji) | 📥 59k | 📦 11M | ⭐ 152 | 🔴 january 2024|
| 🔗 [text-cleaning](https://github.com/ku-nlp/text-cleaning) | - | - | ⭐ 12 | 🔴 november 2022|
| 🔗 [HojiChar](https://github.com/HojiChar/HojiChar) | 📥 24k | 📦 873k | ⭐ 124 | 🟡 november 2025|
| 🔗 [utsuho](https://github.com/juno-rmks/utsuho) | 📥 333 | 📦 19k | ⭐ 4 | 🟢 yesterday|
| 🔗 [python-habachen](https://github.com/Hizuru3/python-habachen) | 📥 9k | 📦 2M | ⭐ 6 | 🟡 october 2025|
| 🔗 [kairyou](https://github.com/bikatr7/kairyou) | 📥 111 | 📦 31k | ⭐ 6 | 🟡 june 2025|


### Sentence spliter
自動偵測句子邊界並分割文字的函式庫

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日本語文境界判定工具
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日本語句子分解器
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 另一個針對日文文本的句子級分詞器
 * [budoux](https://github.com/google/budoux) - 獨立的。小巧的。語言中立的。BudouX 是機器學習驅動的斷行整理工具 Budou 的後繼者。
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - Python 的日文句子分割程式庫
 * [hasami](https://github.com/mkartawijaya/hasami) - 一個用於對日文文本進行句子分割的工具
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - 用 Rust 編寫的 Python 日文文本分割器
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日本語句子分割工具比較
 * [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) - 通過一個使用Rust加速的Python庫，日本語文境界判定器的處理速度提高了40-250倍，並且與megagonlabs/bunkai具有幾乎完美的API兼容性。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bunkai](https://github.com/megagonlabs/bunkai) | 📥 442 | 📦 108k | ⭐ 199 | 🔴 august 2023|
| 🔗 [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) | 📥 15 | 📦 5k | ⭐ 14 | 🔴 february 2021|
| 🔗 [sengiri](https://github.com/ikegami-yukino/sengiri) | 📥 58 | 📦 136k | ⭐ 24 | 🟡 november 2025|
| 🔗 [budoux](https://github.com/google/budoux) | 📥 9k | 📦 430k | ⭐ 1.6k | 🟢 last thursday|
| 🔗 [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) | 📥 2k | 📦 189k | ⭐ 74 | 🔴 april 2023|
| 🔗 [hasami](https://github.com/mkartawijaya/hasami) | 📥 128 | 📦 39k | ⭐ 6 | 🔴 february 2021|
| 🔗 [kuzukiri](https://github.com/alinear-corp/kuzukiri) | 📥 113 | 📦 27k | ⭐ 6 | 🟡 june 2025|
| 🔗 [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) | - | - | ⭐ 9 | 🔴 february 2023|
| 🔗 [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) | 📥 95 | 📦 4k | ⭐ 71 | 🟡 october 2025|


### Sentiment analysis
分析文字情緒與正負極性的函式庫

 * [oseti](https://github.com/ikegami-yukino/oseti) - 基於詞典的日語情感分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 日本語文書的正負面分類。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日文文本情感分析器
 * [asari](https://github.com/Hironsan/asari) - 使用Python實現的日語情感分析器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [oseti](https://github.com/ikegami-yukino/oseti) | 📥 190 | 📦 167k | ⭐ 97 | 🟡 august 2025|
| 🔗 [negapoji](https://github.com/liaoziyang/negapoji) | - | - | ⭐ 151 | 🔴 august 2017|
| 🔗 [pymlask](https://github.com/ikegami-yukino/pymlask) | 📥 23 | 📦 66k | ⭐ 116 | 🔴 july 2024|
| 🔗 [asari](https://github.com/Hironsan/asari) | 📥 109 | 📦 79k | ⭐ 152 | 🔴 october 2022|


### Machine translation
在不同語言之間自動翻譯文字的函式庫

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawl 預訓練神經機器翻譯 (NMT) 模型的使用示例。
 * [JASS](https://github.com/Mao-KU/JASS) - JASS：針對日本特定序列的序列到序列預訓練，用於神經機器翻譯（LREC2020）和基於語言學的多任務預訓練，用於低資源神經機器翻譯（ACM TALLIP）。
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 一個針對日英機器翻譯韌性的現象級評估數據集。該數據集基於MTNT數據集，並附加了四種語言現象的註釋；專有名詞、縮寫名詞、口語表達和變體。COLING 2020。
 * [VISA](https://github.com/ku-nlp/VISA) - 一個用於視覺場景感知機器翻譯的模糊字幕數據集
 * [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) - 使用本地執行的plamo-2-translate模型進行翻譯的命令行界面。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) | - | - | ⭐ 105 | 🔴 april 2021|
| 🔗 [JASS](https://github.com/Mao-KU/JASS) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [PheMT](https://github.com/cl-tohoku/PheMT) | - | - | ⭐ 19 | 🔴 february 2021|
| 🔗 [VISA](https://github.com/ku-nlp/VISA) | - | - | ⭐ 14 | 🔴 october 2022|
| 🔗 [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) | - | - | ⭐ 332 | 🟡 october 2025|


### Named entity recognition
從文字中擷取人名、地名與組織名的函式庫

 * [namaco](https://github.com/chakki-works/namaco) - 基於字元的命名實體識別。
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia是一個從維基百科擴展出來的命名實體詞典。
 * [noyaki](https://github.com/ken11/noyaki) - 將字符跨度標籤信息轉換為基於分詞文本的標籤信息。
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - 用於BERT模型微調的代碼。這是用於創建和使用用於實體識別任務的模型的BERT模型微調示例。
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 從基於詳細註釋標準的病例報告語料庫中進行固有表達和關係抽取精度推論的代碼。
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp，一個用於對日文文本進行地理標記的Python模塊。
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - BERT進行日語固有表現抽取的微調程式
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - 用於日語語言（Hugging Face）資源的調整編碼器和編碼器-解碼器變壓器的示例用於日語語言（Hugging Face）資源的調整編碼器和編碼器-解碼器變壓器的示例
 * [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) - 透過BERT的微調進行專有名詞提取


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namaco](https://github.com/chakki-works/namaco) | - | - | ⭐ 40 | 🔴 february 2018|
| 🔗 [entitypedia](https://github.com/chakki-works/entitypedia) | - | - | ⭐ 13 | 🔴 december 2018|
| 🔗 [noyaki](https://github.com/ken11/noyaki) | 📥 178 | 📦 20k | ⭐ 5 | 🔴 august 2022|
| 🔗 [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) | - | - | ⭐ 11 | 🔴 june 2022|
| 🔗 [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) | - | - | ⭐ 1 | 🔴 november 2021|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 82 | 📦 21k | ⭐ 22 | 🟡 october 2025|
| 🔗 [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) | - | - | ⭐ 5 | 🔴 september 2022|
| 🔗 [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) | - | - | ⭐ 16 | 🔴 october 2023|
| 🔗 [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) | - | - | ⭐ 2 | 🔴 june 2024|


### OCR
從影像中辨識文字並轉換為文字資料的函式庫

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
 * [owocr](https://github.com/aurorawright/owocr) - 日文文本的光學字符識別
 * [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) - Yomitoku是一個專為日語設計的AI驅動的文件圖像分析套件。
 * [findtextcenternet](https://github.com/lithium0003/findtextcenternet) - 使用CenterNet的日文OCR
 * [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) - 一個簡單的漫畫OCR（日本傳統和日本垂直）
 * [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) - 評估對日語文章圖像的OCR性能
 * [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) - 對Manga109s數據集上的PaddleOCR-VL進行微調，以用於日本漫畫文本識別。基礎模型在漫畫中垂直日文文本的閱讀順序方面存在困難。經過微調後，模型能夠正確處理漫畫特定的文本布局。
 * [MangaOCR](https://github.com/gnurt2041/MangaOCR) - 一個針對日文文本的輕量級OCR模型，特別適用於漫畫。
 * [meikiocr](https://github.com/rtr46/meikiocr) - 高速、高精度、適用於日本視頻遊戲的本地OCR
 * [meikipop](https://github.com/rtr46/meikipop) - 通用日語OCR彈出式字典，適用於Windows、Linux和macOS


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [manga-ocr](https://github.com/kha-white/manga-ocr) | 📥 3k | 📦 258k | ⭐ 2.6k | 🟡 june 2025|
| 🔗 [mokuro](https://github.com/kha-white/mokuro) | 📥 471 | 📦 93k | ⭐ 1.6k | 🟢 february|
| 🔗 [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) | - | - | ⭐ 38 | 🔴 april 2022|
| 🔗 [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) | - | - | ⭐ 245 | 🔴 april 2021|
| 🔗 [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) | - | - | ⭐ 650 | 🟡 september 2025|
| 🔗 [donut](https://github.com/clovaai/donut) | 📥 237 | 📦 198k | ⭐ 6.8k | 🔴 july 2023|
| 🔗 [JMTrans](https://github.com/ttop32/JMTrans) | - | - | ⭐ 90 | 🔴 january 2021|
| 🔗 [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) | - | - | ⭐ 153 | 🔴 july 2023|
| 🔗 [text_recognition](https://github.com/ndl-lab/text_recognition) | - | - | ⭐ 8 | 🔴 july 2023|
| 🔗 [Poricom](https://github.com/blueaxis/Poricom) | - | - | ⭐ 417 | 🔴 june 2023|
| 🔗 [owocr](https://github.com/aurorawright/owocr) | - | - | ⭐ 216 | 🟢 yesterday|
| 🔗 [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) | 📥 855 | 📦 83k | ⭐ 1.4k | 🟢 last tuesday|
| 🔗 [findtextcenternet](https://github.com/lithium0003/findtextcenternet) | - | - | ⭐ 57 | 🟡 august 2025|
| 🔗 [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-fogi-manga) | - | - | ⭐ 7 | 🔴 repo not found|
| 🔗 [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) | - | - | ⭐ 1 | 🔴 march 2024|
| 🔗 [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) | - | - | ⭐ 9 | 🟡 december 2025|
| 🔗 [MangaOCR](https://github.com/gnurt2041/MangaOCR) | - | - | ⭐ 35 | 🔴 may 2024|
| 🔗 [meikiocr](https://github.com/rtr46/meikiocr) | 📥 601 | 📦 20k | ⭐ 64 | 🟢 yesterday|
| 🔗 [meikipop](https://github.com/rtr46/meikipop) | - | - | ⭐ 241 | 🟢 last thursday|


### Tool for pretrained models
利用預訓練模型以提升準確度與效率的函式庫

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
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - 燕子項目 大規模語言模型 評估腳本
 * [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) - 燕子項目 事後學習完成的大規模語言模型 評估框架
 * [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) - 預先訓練在日本維基百科上的doc2vec模型
 * [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) - 日語音素級別BERT的存儲庫


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 337 | 🔴 march 2025|
| 🔗 [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) | 📥 3k | 📦 183k | ⭐ 16 | 🔴 august 2022|
| 🔗 [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) | - | - | ⭐ 9 | 🔴 january 2020|
| 🔗 [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) | - | - | ⭐ 2 | 🔴 april 2021|
| 🔗 [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) | - | - | ⭐ 5 | 🔴 february 2022|
| 🔗 [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) | 📥 58 | 📦 20k | ⭐ 12 | 🔴 june 2021|
| 🔗 [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) | - | - | ⭐ 12 | 🔴 november 2024|
| 🔗 [gector-ja](https://github.com/jonnyli1125/gector-ja) | - | - | ⭐ 19 | 🔴 june 2021|
| 🔗 [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) | - | - | ⭐ 41 | 🔴 september 2021|
| 🔗 [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) | - | - | ⭐ 41 | 🔴 january 2023|
| 🔗 [transformer-copy](https://github.com/youichiro/transformer-copy) | - | - | ⭐ 29 | 🔴 september 2020|
| 🔗 [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [nagisa_bert](https://github.com/taishi-i/nagisa_bert) | 📥 39 | 📦 57k | ⭐ 5 | 🟢 february|
| 🔗 [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) | - | - | ⭐ 18 | 🟢 march|
| 🔗 [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) | 📥 71 | 📦 28k | ⭐ 5 | 🔴 february 2024|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) | - | - | ⭐ 6 | 🔴 june 2023|
| 🔗 [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) | - | - | ⭐ 1 | 🔴 june 2023|
| 🔗 [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) | - | - | ⭐ 98 | 🔴 july 2023|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) | - | - | ⭐ 18 | 🔴 may 2023|
| 🔗 [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) | - | - | ⭐ 40 | 🔴 november 2023|
| 🔗 [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) | - | - | ⭐ 50 | 🔴 march 2024|
| 🔗 [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | - | - | ⭐ 149 | 🟢 march|
| 🔗 [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) | - | - | ⭐ 62 | 🔴 june 2024|
| 🔗 [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) | - | - | ⭐ 46 | 🟢 last wednesday|
| 🔗 [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | - | - | ⭐ 77 | 🟢 january|
| 🔗 [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | - | - | ⭐ 33 | 🔴 june 2024|
| 🔗 [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) | - | - | ⭐ 24 | 🟡 september 2025|
| 🔗 [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) | - | - | ⭐ 26 | 🟡 october 2025|
| 🔗 [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) | - | - | ⭐ 25 | 🔴 january 2019|
| 🔗 [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) | - | - | ⭐ 22 | 🔴 december 2023|


### Others
支援日文處理的其他通用函式庫

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
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/ https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
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
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - Mecab + NEologd + Docker + Python3Mecab + NEologd + Docker + Python3
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
 * [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) - 日本語TTS（VITS）的學習和音訊合成的Gradio WebUI日本語TTS（VITS）的學習和音訊合成的Gradio WebUI
 * [ja-law-parser](https://github.com/takuyaa/ja-law-parser) - 一個日本法律解析器
 * [dictation-kit](https://github.com/julius-speech/dictation-kit) - 使用Julius的日語口述套件
 * [julius4seg](https://github.com/Hiroshiba/julius4seg) - 使用Julius的分割支援工具
 * [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) - 免費使用的中等品質文字朗讀軟體，VOICEVOX的語音合成引擎
 * [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) - LLaVA-JP 是一個由 LLaVA 方法訓練的日本 VLM。
 * [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) - 用於低資源環境下的日本LLM的開源RAG與Llama指數
 * [bertjsc](https://github.com/er-ri/bertjsc) - 使用BERT（遮罩語言模型）的日語拼寫錯誤修正器。基於BERT的日語校正。
 * [llm-leaderboard](https://github.com/wandb/llm-leaderboard) - 日本任務的llm評估項目
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - 關於JGLUE的培訓和評估腳本，這是一個日語理解基準的項目。
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - 使用在日本數據集上預訓練的模型，修改LAVIS的BLIP2 Q-former。
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - 將維基百科的日文句子轉換為各種日文嵌入和faiss索引的腳本等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - 探索日本SimCSE
 * [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) - 根據Wikipedia的日文文章，回答用戶問題的Gradio基於RAG的示例。
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - 使用GPT-4來自動評估語言模型的回應腳本
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - 日語T5模型
 * [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) - 用於評估日本語LLM的存儲庫 ・ 評估日本語LLM的存儲庫
 * [jmteb](https://github.com/sbintuitions/jmteb) - JMTEB（日本大规模文本嵌入基准测试）的评估脚本
 * [pydomino](https://github.com/dwangomediavillage/pydomino) - 這是一個用於對日語語音進行音素標籤對齊的工具。
 * [easynovelassistant](https://github.com/zuntan03/easynovelassistant) - 輕量且無規制和審查的日語本地 LLM『LightChatAssistant-TypeB』所提供的簡單小說生成助手。利用本地特權永久生成，堆積中獎的 Gacha。支援朗讀功能。
 * [clip-japanese](https://github.com/sonoisa/clip-japanese) - 日語CLIP模型
 * [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) - Rime IME 的日文羅馬拼音輸入方案
 * [deep-question-generation](https://github.com/sonoisa/deep-question-generation) - 使用深度學習生成的測驗（日語T5模型）
 * [magpie-nemotron](https://github.com/aratako/magpie-nemotron) - 使用Magpie技術和Nemotron-4-340B-Instruct來創建合成對話數據集的代碼
 * [qlora_ja](https://github.com/sosuke115/qlora_ja) - 在日本語數據集中進行qlora指令調整學習的示例代碼
 * [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) - Mozc UT Jawiki 字典是從日文維基百科生成的字典，用於 Mozc。
 * [shisa-v2](https://github.com/shisa-ai/shisa-v2) - 日英雙語法學碩士
 * [llm-translator](https://github.com/hpprc/llm-translator) - 基於Mixtral的Ja-En（En-Ja）翻譯模型
 * [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) - 將Whisper的解碼器替換為llm-jp-1.3b-v1.0版本的語音識別模型的學習代碼。
 * [rag-japanese](https://github.com/akimfromparis/rag-japanese) - 在資源有限的環境中，使用羊駝指數為日本LLM開源的RAG
 * [monaka](https://github.com/komiya-lab/monaka) - 一個日本語解析器（包括歷史日本語）
 * [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) - 一個基於最新的NMT研究的最先進的開源日語<-->英語機器翻譯系統。
 * [substring-word-finder](https://github.com/toufu-24/substring-word-finder) - 連續部分字串的單詞判定。
 * [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) - 這個項目是一個基準工具，用於評估和比較各種視覺語言模型（VLMs）的性能。它使用兩個數據集：LLaVA-Bench-In-the-Wild 和日本 HERON Bench 來衡量模型的性能。
 * [text2dataset](https://github.com/llm-jp/text2dataset) - 使用開放式LLM輕鬆將大型英文文本數據集轉換為日文文本數據集。
 * [mecab-web-api](https://github.com/bungoume/mecab-web-api) - 使用MeCab的日語形態素解析WebAPI
 * [mecab_controller](https://github.com/ajatt-tools/mecab_controller) - Mecab包裝器生成振り仮名讀音。
 * [vits](https://github.com/zassou65535/vits) - VITS提供的文字朗讀器和聲音變換器
 * [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) - 使用語音識別、文章生成和語音合成進行對話的聊天機器人應用程式
 * [kudasai](https://github.com/bikatr7/kudasai) - 利用先進的預處理和集成翻譯技術來優化日英翻譯流程
 * [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) - 使用MeCab進行詞彙分析結果的可視化工具
 * [add-dictionary](https://github.com/massao000/add-dictionary) - 使用GUI添加OpenJTalk用户词典的应用程序
 * [j-moshi](https://github.com/nu-dialogue/j-moshi) - J-Moshi：一個日本全雙工口語對話系統
 * [jatts](https://github.com/unilight/jatts) - JATTS: 日文TTS（用於研究）
 * [tsukasa-speech](https://github.com/respaired/tsukasa-speech) - 一個前沿的日語語音生成網絡
 * [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) - 嘗試使用Elasticsearch、GiNZA和患者表現詞典來吸收患者表現的變化，進行意義結構搜索。
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 生成自動評估的Python工具
 * [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) - 在Colaboratory上嘗試Asagi（使用合成數據集的大規模日語VLM）的示例
 * [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) - 這個工具會自動評估日本多模式大型語言模型在多個數據集上的表現。
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 生成自動評估的Python工具
 * [manga109api](https://github.com/manga109/manga109api) - 簡單的Python API，用於讀取Manga109的標註數據
 * [fastrtc-jp](https://github.com/route250/fastrtc-jp) - 為fastrtc添加日文TTS和STT套件
 * [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) - 使用Python的Whisper模型進行語音轉文字工具
 * [pocket-researcher](https://github.com/u-masao/pocket-researcher) - 利用LLM的自律調查代理人。輕鬆收集信息，了解概要。
 * [jtransbench](https://github.com/webbigdata-jp/jtransbench) - 一個方便測試日文翻譯能力的工具
 * [easyllasa](https://github.com/zuntan03/easyllasa) - EasyLlasa 是一個從5到15秒的日語音頻和日語文本生成日語音頻的TSTS（TextSpeechToSpeech）。
 * [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) - 姓名漢字假名對照模型
 * [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) - 使用OpenReview論文自動發現和分析的日語AI代理程式
 * [pitchbench](https://github.com/shewiiii/pitchbench) - 實驗性的基於日語聲調的LLM基準
 * [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) - 從頭開始的英文到日文轉換器
 * [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) - 在VOICEVOX核心中使用的深度學習模型推論代碼
 * [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) - pyopenjtalk-plus：一個帶有額外改進的OpenJTalk的Python封裝器
 * [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) - 日文拼寫校正
 * [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) - Python 顔文字
 * [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) - 這個存儲庫包含了用於訓練llm-jp/llm-jp-3-vila-14b的代碼，該代碼是從VILA存儲庫修改而來的。
 * [kanjivg-radical](https://github.com/yagays/kanjivg-radical) - 漢字VG-部首
 * [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) - 這個項目使用Django建立的Web應用程式來視覺化日本語ワードネット。
 * [piper-plus](https://github.com/ayutaz/piper-plus) - 增強版的Piper TTS支援日語、WebAssembly、多GPU訓練和品質改進。
 * [Japanera](https://github.com/nagataaaas/Japanera) - 日本年代系統的簡易工具
 * [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) - 使用BERT进行日语句子摘要
 * [kyujipy](https://github.com/drturnon/kyujipy) - 一個Python庫，用於將日文文本從新字體轉換為舊字體，反之亦然。
 * [jitenbot](https://github.com/konstantindjairo/jitenbot) - 用於創建個人副本的網絡爬蟲日本字典
 * [ja-icd10](https://github.com/yagays/ja-icd10) - ICD-10 國際疾病分類的日本語資訊處理的Python套件
 * [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) - VITS2 使用音素級日語 BERT
 * [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) - NDCPredictor的機器學習模型（從書目信息推測日本十進分類的fastText預先訓練模型）
 * [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) - pfmt-bench-fin-ja: 日本金融領域的首選多輪基準
 * [marine-plus](https://github.com/tsukumijima/marine-plus) - MARINE：基於多任務學習的日本口音估計（也支援Windows）
 * [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) - 比較Python中各種日本語分詞器的速度。
 * [yat](https://github.com/yagays/yat) - yat：另一個用於日本自然語言處理的分詞器
 * [igakuqa119](https://github.com/docto-rin/igakuqa119) - 評估第119屆日本醫學執照考試上的LLMs
 * [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) - 使用Transformers的RemBertTokenizerFast進行日語長單位詞分詞器
 * [ibus-jig](https://github.com/y-koj/ibus-jig) - ibus-jig：使用GPT-4的日語輸入法
 * [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) - 一個輕量級的Python庫，旨在根據可定制的規則從日文文本中過濾停用詞。
 * [yasumail](https://github.com/terallite/yasumail) - 用於機器學習訓練數據的合成日本商務電子郵件生成器
 * [himotoki](https://github.com/msr2903/himotoki) - 一個基於Python的日文分詞器、詞典、形態分析器和羅馬拼音工具。基於JMDict用於語言學習。
 * [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) - 一個用於使用大型語言模型（LLMs）合成填充豐富、短發話的日語對話腳本的工具包。該項目旨在通過兩個階段生成數據：種子生成（元數據創建）和對話生成（腳本創建）。
 * [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) - 評估多模式大型語言模型對垂直書寫的日文文本進行評估
 * [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) - 這段程式碼是為了從大型語言模型（LLM）的訓練語料庫中篩選出特別需要注意的個人資訊，也就是「要特別注意的個人資訊」。
 * [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) - 評估多模式大型語言模型對垂直書寫的日文文本進行評估
 * [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) - 從小說文本建立閒聊對話語料庫的方法


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namedivider-python](https://github.com/rskmoi/namedivider-python) | 📥 413 | 📦 81k | ⭐ 251 | 🟡 november 2025|
| 🔗 [asa-python](https://github.com/ikegami-yukino/asa-python) | 📥 45 | 📦 31k | ⭐ 11 | 🔴 february 2019|
| 🔗 [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) | - | - | ⭐ 22 | 🔴 january 2020|
| 🔗 [toiro](https://github.com/taishi-i/toiro) | 📥 61 | 📦 26k | ⭐ 121 | 🟡 november 2025|
| 🔗 [ja-timex](https://github.com/yagays/ja-timex) | 📥 475 | 📦 91k | ⭐ 140 | 🔴 november 2023|
| 🔗 [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) | - | - | ⭐ 137 | 🔴 march 2019|
| 🔗 [daaja](https://github.com/kajyuuen/daaja) | 📥 38 | 📦 25k | ⭐ 64 | 🔴 february 2023|
| 🔗 [accel-brain-code](https://github.com/accel-brain/accel-brain-code) | 📥 160 | 📦 149k | ⭐ 323 | 🔴 december 2023|
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 337 | 🔴 march 2025|
| 🔗 [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) | 📥 362 | 📦 52k | ⭐ 10 | 🔴 june 2024|
| 🔗 [nlplot](https://github.com/takapy0210/nlplot) | 📥 106 | 📦 109k | ⭐ 238 | 🔴 september 2022|
| 🔗 [rake-ja](https://github.com/kanjirz50/rake-ja) | - | - | ⭐ 21 | 🔴 october 2018|
| 🔗 [jel](https://github.com/izuna385/jel) | 📥 18 | 📦 8k | ⭐ 11 | 🔴 july 2021|
| 🔗 [MedNER-J](https://github.com/sociocom/MedNER-J) | - | - | ⭐ 18 | 🔴 may 2022|
| 🔗 [zunda-python](https://github.com/ikegami-yukino/zunda-python) | 📥 10 | 📦 6k | ⭐ 10 | 🔴 november 2019|
| 🔗 [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [showcase](https://github.com/cl-tohoku/showcase) | 📥 10 | 📦 7k | ⭐ 6 | 🔴 june 2018|
| 🔗 [darts-clone-python](https://github.com/rixwew/darts-clone-python) | 📥 3k | 📦 9M | ⭐ 20 | 🔴 april 2022|
| 🔗 [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [desuwa](https://github.com/megagonlabs/desuwa) | 📥 24 | 📦 10k | ⭐ 6 | 🔴 may 2022|
| 🔗 [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) | - | - | ⭐ 277 | 🔴 may 2016|
| 🔗 [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) | - | - | ⭐ 66 | 🔴 april 2021|
| 🔗 [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) | - | - | ⭐ 26 | 🔴 june 2019|
| 🔗 [DNorm-J](https://github.com/sociocom/DNorm-J) | - | - | ⭐ 9 | 🔴 june 2022|
| 🔗 [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) | 📥 29 | 📦 65k | ⭐ 9 | 🔴 september 2022|
| 🔗 [ishi](https://github.com/ku-nlp/ishi) | 📥 13 | 📦 6k | ⭐ 2 | 🔴 may 2020|
| 🔗 [python-npylm](https://github.com/musyoku/python-npylm) | - | - | ⭐ 34 | 🔴 january 2019|
| 🔗 [python-npycrf](https://github.com/musyoku/python-npycrf) | - | - | ⭐ 11 | 🔴 march 2018|
| 🔗 [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) | - | - | ⭐ 16 | 🔴 october 2017|
| 🔗 [negima](https://github.com/cocodrips/negima) | 📥 22 | 📦 16k | ⭐ 14 | 🔴 august 2018|
| 🔗 [YouyakuMan](https://github.com/neilctwu/YouyakuMan) | - | - | ⭐ 52 | 🔴 september 2020|
| 🔗 [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) | 📥 639 | 📦 2M | ⭐ 21 | 🔴 april 2020|
| 🔗 [kantan](https://github.com/itayperl/kantan) | - | - | ⭐ 8 | 🔴 october 2024|
| 🔗 [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) | - | - | ⭐ 40 | 🔴 september 2017|
| 🔗 [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) | - | - | ⭐ 10 | 🔴 august 2022|
| 🔗 [chirptext](https://github.com/letuananh/chirptext) | 📥 2k | 📦 200k | ⭐ 7 | 🔴 october 2022|
| 🔗 [yubin](https://github.com/alvations/yubin) | 📥 5 | 📦 3k | ⭐ 3 | 🔴 october 2019|
| 🔗 [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) | 📥 52 | 📦 24k | ⭐ 6 | 🔴 february 2021|
| 🔗 [japanese2phoneme](https://github.com/iory/japanese2phoneme) | 📥 18 | 📦 4k | ⭐ 1 | 🔴 february 2022|
| 🔗 [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) | - | - | ⭐ 1 | 🔴 march 2022|
| 🔗 [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) | - | - | ⭐ 11 | 🔴 september 2017|
| 🔗 [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) | - | - | ⭐ 8 | 🟡 june 2025|
| 🔗 [JLM](https://github.com/jiali-ms/JLM) | - | - | ⭐ 111 | 🔴 june 2019|
| 🔗 [NTM](https://github.com/m3yrin/NTM) | - | - | ⭐ 13 | 🔴 july 2019|
| 🔗 [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) | - | - | ⭐ 40 | 🔴 march 2021|
| 🔗 [text-generation](https://github.com/discus0434/text-generation) | - | - | ⭐ 19 | 🟡 august 2025|
| 🔗 [chainer_nic](https://github.com/yuyay/chainer_nic) | - | - | ⭐ 17 | 🔴 december 2018|
| 🔗 [unihan-lm](https://github.com/JetRunner/unihan-lm) | - | - | ⭐ 2 | 🔴 november 2020|
| 🔗 [mbart-finetuning](https://github.com/ken11/mbart-finetuning) | - | - | ⭐ 3 | 🔴 october 2021|
| 🔗 [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) | - | - | ⭐ 47 | 🔴 november 2023|
| 🔗 [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) | - | - | ⭐ 72 | 🔴 september 2022|
| 🔗 [Grongish](https://github.com/shogo82148/Grongish) | - | - | ⭐ 25 | 🟡 december 2025|
| 🔗 [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) | - | - | ⭐ 9 | 🔴 january 2020|
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
| 🔗 [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) | 📥 141k | 📦 172k | ⭐ repo not found | 🔴 november 2015|
| 🔗 [AugLy-jp](https://github.com/chck/AugLy-jp) | 📥 56 | 📦 30k | ⭐ 7 | 🔴 september 2021|
| 🔗 [furigana4epub](https://github.com/Mumumu4/furigana4epub) | 📥 27 | 📦 12k | ⭐ 29 | 🔴 september 2021|
| 🔗 [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) | 📥 70 | 📦 20k | ⭐ 12 | 🔴 march 2025|
| 🔗 [jageocoder](https://github.com/t-sagara/jageocoder) | 📥 3k | 📦 339k | ⭐ 95 | 🟡 september 2025|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 82 | 📦 21k | ⭐ 22 | 🟡 october 2025|
| 🔗 [nksnd](https://github.com/yoriyuki/nksnd) | - | - | ⭐ 26 | 🔴 may 2018|
| 🔗 [JaMIE](https://github.com/racerandom/JaMIE) | - | - | ⭐ 9 | 🟢 march|
| 🔗 [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) | - | - | ⭐ 48 | 🔴 august 2017|
| 🔗 [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) | - | - | ⭐ 19 | 🔴 july 2019|
| 🔗 [5ch-analysis](https://github.com/GINK03/5ch-analysis) | - | - | ⭐ 75 | 🔴 november 2018|
| 🔗 [tweet_extructor](https://github.com/tatHi/tweet_extructor) | - | - | ⭐ 3 | 🔴 august 2022|
| 🔗 [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) | - | - | ⭐ 2 | 🔴 august 2018|
| 🔗 [jinf](https://github.com/hkiyomaru/jinf) | 📥 325 | 📦 55k | ⭐ 4 | 🔴 december 2022|
| 🔗 [kwja](https://github.com/ku-nlp/kwja) | 📥 275 | 📦 56k | ⭐ 139 | 🟡 august 2025|
| 🔗 [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) | - | - | ⭐ 6 | 🔴 december 2022|
| 🔗 [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) | - | - | ⭐ 12 | 🔴 october 2022|
| 🔗 [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) | - | - | ⭐ 2 | 🔴 october 2022|
| 🔗 [cihai](https://github.com/cihai/cihai) | 📥 360 | 📦 212k | ⭐ 93 | 🟢 yesterday|
| 🔗 [marine](https://github.com/6gsn/marine) | 📥 39 | 📦 15k | ⭐ 36 | 🔴 september 2022|
| 🔗 [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) | - | - | ⭐ 32 | 🔴 december 2022|
| 🔗 [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [radicalchar](https://github.com/yamamaya/radicalchar) | - | - | ⭐ 9 | 🔴 december 2022|
| 🔗 [akaza](https://github.com/tokuhirom/akaza) | - | - | ⭐ 247 | 🟢 today|
| 🔗 [posuto](https://github.com/polm/posuto) | 📥 5k | 📦 684k | ⭐ 226 | 🟢 march|
| 🔗 [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) | - | - | ⭐ 269 | 🔴 september 2022|
| 🔗 [ibus-hiragana](https://github.com/esrille/ibus-hiragana) | - | - | ⭐ 78 | 🟢 today|
| 🔗 [furiganapad](https://github.com/esrille/furiganapad) | - | - | ⭐ 19 | 🟡 april 2025|
| 🔗 [chikkarpy](https://github.com/WorksApplications/chikkarpy) | 📥 265 | 📦 59k | ⭐ 55 | 🔴 february 2022|
| 🔗 [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) | - | - | ⭐ 36 | 🔴 may 2022|
| 🔗 [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) | - | - | ⭐ 184 | 🔴 october 2024|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [shuwa](https://github.com/google/shuwa) | - | - | ⭐ 145 | 🔴 december 2022|
| 🔗 [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) | - | - | ⭐ 6 | 🔴 october 2022|
| 🔗 [tra-fugu](https://github.com/tos-kamiya/tra-fugu) | - | - | ⭐ 6 | 🔴 march 2023|
| 🔗 [fugumt](https://github.com/s-taka/fugumt) | - | - | ⭐ 64 | 🔴 february 2021|
| 🔗 [JaSPICE](https://github.com/keio-smilab23/JaSPICE) | 📥 6 | 📦 2k | ⭐ 9 | 🔴 november 2023|
| 🔗 [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) | - | - | ⭐ 48 | 🔴 april 2023|
| 🔗 [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) | 📥 17k | 📦 1M | ⭐ 245 | 🟡 april 2025|
| 🔗 [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) | 📥 35 | 📦 7k | ⭐ 26 | 🔴 february 2024|
| 🔗 [N46Whisper](https://github.com/Ayanaminn/N46Whisper) | - | - | ⭐ 1.7k | 🔴 february 2025|
| 🔗 [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) | - | - | ⭐ 17 | 🔴 may 2024|
| 🔗 [pdf-translator](https://github.com/discus0434/pdf-translator) | - | - | ⭐ 338 | 🔴 may 2024|
| 🔗 [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) | - | - | ⭐ 1 | 🔴 december 2022|
| 🔗 [mozc-devices](https://github.com/google/mozc-devices) | - | - | ⭐ 2.7k | 🟡 november 2025|
| 🔗 [natsume](https://github.com/faruzan0820/natsume) | 📥 0 | 📦 3k | ⭐ repo not found | 🔴 repo not found|
| 🔗 [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) | - | - | ⭐ 42 | 🔴 january 2024|
| 🔗 [ja-law-parser](https://github.com/takuyaa/ja-law-parser) | - | - | ⭐ 25 | 🔴 january 2024|
| 🔗 [dictation-kit](https://github.com/julius-speech/dictation-kit) | - | - | ⭐ 164 | 🔴 april 2019|
| 🔗 [julius4seg](https://github.com/Hiroshiba/julius4seg) | - | - | ⭐ 7 | 🔴 august 2021|
| 🔗 [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) | - | - | ⭐ 1.6k | 🟢 march|
| 🔗 [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) | - | - | ⭐ 64 | 🔴 june 2024|
| 🔗 [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [bertjsc](https://github.com/er-ri/bertjsc) | - | - | ⭐ 14 | 🔴 august 2024|
| 🔗 [llm-leaderboard](https://github.com/wandb/llm-leaderboard) | - | - | ⭐ 92 | 🟡 september 2025|
| 🔗 [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) | - | - | ⭐ 18 | 🟢 march|
| 🔗 [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) | - | - | ⭐ 11 | 🔴 march 2024|
| 🔗 [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) | - | - | ⭐ 69 | 🔴 october 2023|
| 🔗 [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) | - | - | ⭐ 16 | 🔴 june 2024|
| 🔗 [t5-japanese](https://github.com/sonoisa/t5-japanese) | - | - | ⭐ 118 | 🟡 september 2025|
| 🔗 [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) | - | - | ⭐ 5 | 🔴 april 2024|
| 🔗 [jmteb](https://github.com/sbintuitions/jmteb) | - | - | ⭐ 87 | 🟢 last monday|
| 🔗 [pydomino](https://github.com/dwangomediavillage/pydomino) | - | - | ⭐ 37 | 🟡 august 2025|
| 🔗 [easynovelassistant](https://github.com/zuntan03/easynovelassistant) | - | - | ⭐ 220 | 🔴 july 2024|
| 🔗 [clip-japanese](https://github.com/sonoisa/clip-japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) | - | - | ⭐ 48 | 🟢 last thursday|
| 🔗 [deep-question-generation](https://github.com/sonoisa/deep-question-generation) | - | - | ⭐ 12 | 🔴 march 2023|
| 🔗 [magpie-nemotron](https://github.com/aratako/magpie-nemotron) | - | - | ⭐ 9 | 🔴 july 2024|
| 🔗 [qlora_ja](https://github.com/sosuke115/qlora_ja) | - | - | ⭐ 1 | 🔴 july 2024|
| 🔗 [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) | - | - | ⭐ 28 | 🟢 march|
| 🔗 [shisa-v2](https://github.com/shisa-ai/shisa-v2) | - | - | ⭐ 28 | 🟡 december 2025|
| 🔗 [llm-translator](https://github.com/hpprc/llm-translator) | - | - | ⭐ 20 | 🔴 january 2025|
| 🔗 [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) | - | - | ⭐ 9 | 🔴 september 2024|
| 🔗 [rag-japanese](https://github.com/akimfromparis/rag-japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [monaka](https://github.com/komiya-lab/monaka) | - | - | ⭐ 4 | 🔴 january 2025|
| 🔗 [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) | - | - | ⭐ 3 | 🔴 september 2024|
| 🔗 [substring-word-finder](https://github.com/toufu-24/substring-word-finder) | - | - | ⭐ 4 | 🟡 november 2025|
| 🔗 [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) | - | - | ⭐ 6 | 🔴 december 2024|
| 🔗 [text2dataset](https://github.com/llm-jp/text2dataset) | - | - | ⭐ 27 | 🔴 january 2025|
| 🔗 [mecab-web-api](https://github.com/bungoume/mecab-web-api) | - | - | ⭐ 40 | 🔴 july 2022|
| 🔗 [mecab_controller](https://github.com/ajatt-tools/mecab_controller) | - | - | ⭐ 19 | 🟢 january|
| 🔗 [vits](https://github.com/zassou65535/vits) | - | - | ⭐ 92 | 🔴 february 2023|
| 🔗 [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) | - | - | ⭐ 48 | 🟡 october 2025|
| 🔗 [kudasai](https://github.com/bikatr7/kudasai) | - | - | ⭐ 26 | 🟡 june 2025|
| 🔗 [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) | - | - | ⭐ 2 | 🔴 september 2023|
| 🔗 [add-dictionary](https://github.com/massao000/add-dictionary) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [j-moshi](https://github.com/nu-dialogue/j-moshi) | - | - | ⭐ 302 | 🟡 june 2025|
| 🔗 [jatts](https://github.com/unilight/jatts) | - | - | ⭐ 44 | 🟢 march|
| 🔗 [tsukasa-speech](https://github.com/respaired/tsukasa-speech) | - | - | ⭐ 63 | 🟡 may 2025|
| 🔗 [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) | - | - | ⭐ 2 | 🔴 february 2021|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 39 | 🟡 december 2025|
| 🔗 [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) | - | - | ⭐ 1 | 🔴 march 2025|
| 🔗 [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) | - | - | ⭐ 41 | 🟢 january|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 39 | 🟡 december 2025|
| 🔗 [manga109api](https://github.com/manga109/manga109api) | 📥 163 | 📦 46k | ⭐ 129 | 🔴 march 2022|
| 🔗 [fastrtc-jp](https://github.com/route250/fastrtc-jp) | - | - | ⭐ 5 | 🟡 may 2025|
| 🔗 [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) | - | - | ⭐ 17 | 🟢 january|
| 🔗 [pocket-researcher](https://github.com/u-masao/pocket-researcher) | - | - | ⭐ 10 | 🟡 april 2025|
| 🔗 [jtransbench](https://github.com/webbigdata-jp/jtransbench) | - | - | ⭐ 13 | 🟡 october 2025|
| 🔗 [easyllasa](https://github.com/zuntan03/easyllasa) | - | - | ⭐ 25 | 🟡 september 2025|
| 🔗 [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) | - | - | ⭐ 114 | 🟡 december 2025|
| 🔗 [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) | - | - | ⭐ 13 | 🟡 november 2025|
| 🔗 [pitchbench](https://github.com/shewiiii/pitchbench) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) | - | - | ⭐ 31 | 🟡 december 2025|
| 🔗 [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) | 📥 11k | 📦 422k | ⭐ 56 | 🟢 march|
| 🔗 [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) | 📥 18 | 📦 37k | ⭐ 6 | 🔴 december 2018|
| 🔗 [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) | - | - | ⭐ 10 | 🟡 august 2025|
| 🔗 [kanjivg-radical](https://github.com/yagays/kanjivg-radical) | - | - | ⭐ 106 | 🔴 august 2018|
| 🔗 [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) | - | - | ⭐ 3 | 🔴 november 2022|
| 🔗 [piper-plus](https://github.com/ayutaz/piper-plus) | - | - | ⭐ 85 | 🟢 today|
| 🔗 [Japanera](https://github.com/nagataaaas/Japanera) | 📥 3k | 📦 359k | ⭐ 35 | 🟡 june 2025|
| 🔗 [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) | - | - | ⭐ 49 | 🔴 december 2019|
| 🔗 [kyujipy](https://github.com/drturnon/kyujipy) | 📥 38 | 📦 23k | ⭐ 22 | 🟢 january|
| 🔗 [jitenbot](https://github.com/konstantindjairo/jitenbot) | - | - | ⭐ 4 | 🔴 december 2024|
| 🔗 [ja-icd10](https://github.com/yagays/ja-icd10) | - | - | ⭐ 5 | 🔴 july 2021|
| 🔗 [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) | - | - | ⭐ 14 | 🔴 december 2023|
| 🔗 [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) | - | - | ⭐ 11 | 🔴 august 2021|
| 🔗 [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) | - | - | ⭐ 9 | 🔴 march 2025|
| 🔗 [marine-plus](https://github.com/tsukumijima/marine-plus) | 📥 55 | 📦 12k | ⭐ 8 | 🟢 today|
| 🔗 [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) | - | - | ⭐ 7 | 🔴 february 2022|
| 🔗 [yat](https://github.com/yagays/yat) | - | - | ⭐ 7 | 🔴 june 2018|
| 🔗 [igakuqa119](https://github.com/docto-rin/igakuqa119) | - | - | ⭐ 8 | 🟢 january|
| 🔗 [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) | - | - | ⭐ 6 | 🔴 december 2021|
| 🔗 [ibus-jig](https://github.com/y-koj/ibus-jig) | - | - | ⭐ 4 | 🔴 december 2023|
| 🔗 [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) | 📥 27 | 📦 5k | ⭐ 4 | 🔴 november 2024|
| 🔗 [yasumail](https://github.com/terallite/yasumail) | - | - | ⭐ 2 | 🟢 january|
| 🔗 [himotoki](https://github.com/msr2903/himotoki) | 📥 85 | 📦 4k | ⭐ 3 | 🟢 february|
| 🔗 [diafill-toolkit](https://github.com/sbintuitions/diafill-toolkit) | - | - | ⭐ 0 | 🟢 january|
| 🔗 [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [jp-llm-corpus-pii-filter](https://github.com/matsuolab/jp-llm-corpus-pii-filter) | - | - | ⭐ 7 | 🔴 march 2025|
| 🔗 [eval_vertical_ja](https://github.com/llm-jp/eval_vertical_ja) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [Novel2DialCorpus](https://github.com/ganbon/Novel2DialCorpus) | - | - | ⭐ 0 | 🟢 february|


## C++

### Morphology analysis
高效能的日文形態素分析函式庫

 * [mecab](https://github.com/taku910/mecab) - 又一個日本語形態分析器
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++（一個形態學分析工具包）
 * [kytea](https://github.com/neubig/kytea) - 京都文本分析工具箱，可用於詞語分割和發音估計等。
 * [juman](https://github.com/ku-nlp/juman) - 日本語形態素解析システム JUMAN


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab](https://github.com/taku910/mecab) | - | - | ⭐ 1.1k | 🔴 february 2025|
| 🔗 [jumanpp](https://github.com/ku-nlp/jumanpp) | - | - | ⭐ 409 | 🔴 march 2023|
| 🔗 [kytea](https://github.com/neubig/kytea) | - | - | ⭐ 212 | 🔴 april 2020|
| 🔗 [juman](https://github.com/ku-nlp/juman) | - | - | ⭐ 12 | 🔴 december 2021|

### Parsing
用於日文語法與依存分析的函式庫

 * [cabocha](https://github.com/taku910/cabocha) - 另一個日本依存結構分析器
 * [knp](https://github.com/ku-nlp/knp) - 一個日語解析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [cabocha](https://github.com/taku910/cabocha) | - | - | ⭐ 121 | 🔴 february 2025|
| 🔗 [knp](https://github.com/ku-nlp/knp) | - | - | ⭐ 33 | 🔴 november 2023|

### Others
其他與日文NLP相關的函式庫

 * [jsc](https://github.com/yohokuno/jsc) - 日文假名漢字轉換、中文拼音輸入和CJE混合輸入的聯合源通道模型。
 * [aquaskk](https://github.com/codefirst/aquaskk) - 沒有形態學分析的輸入法。
 * [mozc](https://github.com/google/mozc) - Mozc - 一款為多平台設計的日本輸入法編輯器
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch：一個（精確|前綴|近似）字串匹配庫
 * [resembla](https://github.com/tuem/resembla) - Resembla：基於單詞的日語相似句子搜索庫
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ Windows 的 SKK-like 日文輸入法編輯器
 * [mozuku](https://github.com/t3tra-dev/mozuku) - 進行日文文章的分析和校對的LSP伺服器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jsc](https://github.com/yohokuno/jsc) | - | - | ⭐ 15 | 🔴 december 2012|
| 🔗 [aquaskk](https://github.com/codefirst/aquaskk) | - | - | ⭐ 368 | 🔴 july 2023|
| 🔗 [mozc](https://github.com/google/mozc) | - | - | ⭐ 2.9k | 🟢 last thursday|
| 🔗 [trimatch](https://github.com/tuem/trimatch) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [resembla](https://github.com/tuem/resembla) | - | - | ⭐ 73 | 🟡 august 2025|
| 🔗 [corvusskk](https://github.com/nathancorvussolis/corvusskk) | - | - | ⭐ 356 | 🟢 last friday|
| 🔗 [mozuku](https://github.com/t3tra-dev/mozuku) | - | - | ⭐ 412 | 🟢 last monday|


## Rust crate

### Morphology analysis
以Rust實作的日文形態素分析套件

 * [lindera](https://github.com/lindera-morphology/lindera) - 一個形態學分析庫。
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto：基於點預測的高速分詞器
 * [goya](https://github.com/Leko/goya) - 用 Rust 寫的日語形態分析
 * [vibrato](https://github.com/daac-tools/vibrato) - 顫音：基於維特比加速的分詞器
 * [yoin](https://github.com/agatan/yoin) - 一個用純 Rust 編寫的日語形態分析器
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 安全的 Rust 綁定，用於 mecab 詞性和形態分析庫。
 * [awabi](https://github.com/nakagami/awabi) - 一個使用mecab字典的形態分析器
 * [kanpyo](https://github.com/togatoga/kanpyo) - 用Rust编写的日语形态分析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera](https://github.com/lindera-morphology/lindera) | - | 📦 966k | ⭐ 609 | 🟢 last thursday|
| 🔗 [vaporetto](https://github.com/daac-tools/vaporetto) | - | 📦 190k | ⭐ 254 | 🟢 february|
| 🔗 [goya](https://github.com/Leko/goya) | - | 📦 11k | ⭐ 83 | 🔴 december 2021|
| 🔗 [vibrato](https://github.com/daac-tools/vibrato) | - | 📦 58k | ⭐ 403 | 🟢 february|
| 🔗 [yoin](https://github.com/agatan/yoin) | - | 📦 3k | ⭐ 26 | 🔴 october 2017|
| 🔗 [mecab-rs](https://github.com/tsurai/mecab-rs) | - | 📦 39k | ⭐ 67 | 🔴 september 2023|
| 🔗 [awabi](https://github.com/nakagami/awabi) | - | 📦 24k | ⭐ 10 | 🟡 november 2025|
| 🔗 [kanpyo](https://github.com/togatoga/kanpyo) | - | 📦 2.5k | ⭐ 109 | 🟢 february|


### Converter
用於日文文字與表記轉換的套件

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 檢查和轉換日文字符（平假名、片假名）和羅馬字的實用程式庫
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 一個 Rust 函式庫，可將日文半角ｶﾅ和全角英數轉換為正常字符。
 * [kana](https://github.com/gbrlsnchs/kana) - [鏡像] CLI 程序，可將羅馬字文本轉寫為平假名或片假名。
 * [kanaria](https://github.com/samunohito/kanaria) - 這個程式庫提供了平假名、片假名、半形和全形之間的互相轉換和識別功能。
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - 日本的地址分割成都道府県/市區町村/町名/其他的程式庫
 * [yosina](https://github.com/yosina-lib/yosina) - Yosina 是一個處理日文書寫中使用的字母和符號的音譯庫。
 * [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) - 快速轉換日文半角和全角字符的Rust實現，mojimoji。Rust實現的快速轉換器，可在日文半角和全角字符之間進行轉換，mojimoji。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) | - | 📦 344k | ⭐ 90 | 🔴 march 2025|
| 🔗 [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) | - | 📦 63k | ⭐ 19 | 🔴 april 2020|
| 🔗 [kana](https://github.com/gbrlsnchs/kana) | - | - | ⭐ 12 | 🔴 january 2023|
| 🔗 [kanaria](https://github.com/samunohito/kanaria) | - | - | ⭐ 21 | 🟢 february|
| 🔗 [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) | - | - | ⭐ 10 | 🟡 november 2025|
| 🔗 [yosina](https://github.com/yosina-lib/yosina) | - | - | ⭐ 23 | 🟢 last thursday|
| 🔗 [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) | - | - | ⭐ 4 | 🔴 november 2022|


### Search engine library
用於日文全文檢索與索引的函式庫

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy. 林德拉分詞器用於Tantivy。
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - 使用 Vibrato 的 Tantivy 分詞器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) | - | 📦 171k | ⭐ 68 | 🟢 january|
| 🔗 [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) | - | 📦 1.5k | ⭐ 3 | 🔴 january 2023|


### Others
其他日文文字與輸入法處理套件

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
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - 裁判例資料列表生成軟體，可透過網址(https://www.courts.go.jp/index.html) 對法院網站進行爬蟲。
 * [jisho](https://github.com/eagleflo/jisho) - Jisho 是一個提供日英詞典的 CLI 工具和 Rust 函式庫。
 * [kanalizer](https://github.com/voicevox/kanalizer) - 從英文單字推測讀音的程式庫。
 * [koharu](https://github.com/mayocream/koharu) - 使用Rust编写的带有LLM的自动漫画翻译工具。
 * [yomine](https://github.com/mcgrizzz/yomine) - 一個旨在幫助語言學習者挖掘新單詞和表達方式的日語詞彙挖掘工具。
 * [matsuba](https://github.com/mrpicklepinosaur/matsuba) - 輕量級的日文輸入法，使用Rust語言編寫
 * [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) - 由Rust製作的日本語辭典，支援Telegram機器人、AWS Lambda和Cloudflare Workers。支援LLM和搜索RAG。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [daachorse](https://github.com/daac-tools/daachorse) | - | 📦 718k | ⭐ 245 | 🟢 january|
| 🔗 [find-simdoc](https://github.com/legalforce-research/find-simdoc) | - | 📦 29k | ⭐ 62 | 🔴 march 2025|
| 🔗 [crawdad](https://github.com/daac-tools/crawdad) | - | 📦 63k | ⭐ 37 | 🔴 january 2025|
| 🔗 [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) | - | - | ⭐ 4 | 🔴 march 2023|
| 🔗 [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [vime](https://github.com/algon-320/vime) | - | - | ⭐ 230 | 🔴 november 2022|
| 🔗 [voicevox_core](https://github.com/VOICEVOX/voicevox_core) | - | - | ⭐ 1.1k | 🟢 last wednesday|
| 🔗 [akaza](https://github.com/akaza-im/akaza) | - | - | ⭐ 247 | 🟢 today|
| 🔗 [Jotoba](https://github.com/WeDontPanic/Jotoba) | - | - | ⭐ 199 | 🔴 january 2024|
| 🔗 [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) | - | - | ⭐ 55 | 🟢 february|
| 🔗 [niinii](https://github.com/Netdex/niinii) | - | - | ⭐ 15 | 🟢 february|
| 🔗 [cskk](https://github.com/naokiri/cskk) | - | - | ⭐ 80 | 🟢 march|
| 🔗 [japanki](https://github.com/tysonwu/japanki) | - | - | ⭐ 3 | 🔴 october 2023|
| 🔗 [jpreprocess](https://github.com/jpreprocess/jpreprocess) | - | - | ⭐ 52 | 🟢 february|
| 🔗 [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) | - | - | ⭐ 5 | 🔴 february 2025|
| 🔗 [jisho](https://github.com/eagleflo/jisho) | - | - | ⭐ 17 | 🟢 february|
| 🔗 [kanalizer](https://github.com/voicevox/kanalizer) | - | - | ⭐ 26 | 🟢 march|
| 🔗 [koharu](https://github.com/mayocream/koharu) | - | - | ⭐ 844 | 🟢 today|
| 🔗 [yomine](https://github.com/mcgrizzz/yomine) | - | - | ⭐ 50 | 🟢 february|
| 🔗 [matsuba](https://github.com/mrpicklepinosaur/matsuba) | - | - | ⭐ 18 | 🔴 march 2023|
| 🔗 [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) | - | - | ⭐ 70 | 🟢 last thursday|


## JavaScript

### Morphology analysis
可於瀏覽器或Node.js進行日文形態素分析的函式庫

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日本語形態素解析器的JavaScript實現
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - Rakuten MA - 一款純粹使用 JavaScript 編寫的中日文形態分析器（詞分割器 + 詞性標記器）。
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - 另一個用於 Node.js 的 MeCab 封裝程式
 * [juman-bin](https://github.com/thammin/juman-bin) - 一個可擴展的日本語形態素解析器。日本語形態素解析系統。
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - 使用MeCab的非同步日語形態分析器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji.js](https://github.com/takuyaa/kuromoji.js) | 📥 77k/week | 📦 8.3M | ⭐ 970 | 🔴 november 2018|
| 🔗 [rakutenma](https://github.com/rakuten-nlp/rakutenma) | 📥 7/week | 📦 906 | ⭐ 472 | 🔴 january 2015|
| 🔗 [node-mecab-ya](https://github.com/golbin/mecab-ya) | 📥 51/week | 📦 7.2k | ⭐ 110 | 🔴 repo not found|
| 🔗 [juman-bin](https://github.com/thammin/juman-bin) | 📥 0/week | 📦 292 | ⭐ 3 | 🔴 may 2017|
| 🔗 [node-mecab-async](https://github.com/hecomi/node-mecab-async) | 📥 1.3k/week | 📦 rate limited by upstream service | ⭐ 103 | 🔴 october 2017|


### Converter
用於日文表記與讀音轉換的函式庫

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - 日語語言庫，可將日語句子轉換為平假名、片假名或羅馬字，支持振り仮名和送り仮名模式。
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - Kuroshiro 的 Kuromoji 形態分析器。
 * [hepburn](https://github.com/lovell/hepburn) - 使用 Hepburn 羅馬拼音將日文平假名和片假名轉換為羅馬字的 Node.js 模組。
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - 將日本數字轉換為數字
 * [jslingua](https://github.com/kariminf/jslingua) - 處理文本的Javascript庫：阿拉伯語，日語等。
 * [WanaKana](https://github.com/WaniKani/WanaKana) - JavaScript 庫，用於檢測和轉寫平假名 <--> 片假名 <--> 羅馬字。
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - 將基於羅馬字的日本名字進行標準化和修復常見問題。
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - 製作日本古風文本的實用集合
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - 開源的地址規範化程式庫。
 * [jaconv](https://github.com/kazuhikoarase/jaconv) - 日本語文字轉換程式庫 (javascript)
 * [romaji-conv](https://github.com/koozaki/romaji-conv) - 將羅馬字轉換為平假名
 * [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) - 全國的地址數據API
 * [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) - 將文字單詞轉換為表情符號
 * [japanese.js](https://github.com/hakatashi/japanese.js) - 用於日文文本處理的Util集合。將平假名化、片假名化和羅馬化。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuroshiro](https://github.com/hexenq/kuroshiro) | 📥 5.2k/week | 📦 406k | ⭐ 960 | 🔴 june 2021|
| 🔗 [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) | 📥 4.9k/week | 📦 382k | ⭐ 67 | 🔴 august 2018|
| 🔗 [hepburn](https://github.com/lovell/hepburn) | 📥 50k/week | 📦 3.3M | ⭐ 137 | 🟡 september 2025|
| 🔗 [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) | 📥 15k/week | 📦 2.2M | ⭐ 59 | 🔴 february 2023|
| 🔗 [jslingua](https://github.com/kariminf/jslingua) | 📥 37/week | 📦 8.1k | ⭐ 53 | 🔴 october 2023|
| 🔗 [WanaKana](https://github.com/WaniKani/WanaKana) | 📥 16k/week | 📦 2.1M | ⭐ 909 | 🟡 september 2025|
| 🔗 [node-romaji-name](https://github.com/jeresig/node-romaji-name) | 📥 86/week | 📦 rate limited by upstream service | ⭐ 41 | 🔴 december 2023|
| 🔗 [kyujitai.js](https://github.com/hakatashi/kyujitai.js) | 📥 7/week | 📦 1.1k | ⭐ 23 | 🔴 august 2020|
| 🔗 [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) | - | - | ⭐ 946 | 🟡 july 2025|
| 🔗 [jaconv](https://github.com/kazuhikoarase/jaconv) | - | - | ⭐ 87 | 🟡 june 2025|
| 🔗 [romaji-conv](https://github.com/koozaki/romaji-conv) | - | - | ⭐ 26 | 🟢 february|
| 🔗 [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) | - | - | ⭐ 71 | 🔴 january 2025|
| 🔗 [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [japanese.js](https://github.com/hakatashi/japanese.js) | - | - | ⭐ 167 | 🔴 august 2020|


### Others
其他與日文NLP相關的JavaScript函式庫

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
 * [kamiya-codec](https://github.com/fasiha/kamiya-codec) - 根據神谷多恵子的《日本動詞手冊》和《日本形容詞和副詞手冊》，開發一個日語動詞變化器和去變化器。
 * [closewords](https://github.com/otoneko1102/closewords) - 從單詞群中搜尋最相似的單詞的日語（包含漢字）庫。
 * [japanese-analyzer](https://github.com/cokice/japanese-analyzer) - 日文句子分析器 (日本語文章解析器)
 * [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) - 標準化日文振假名
 * [yama](https://github.com/sapjax/yama) - 在任何網站上學習日語詞彙
 * [kaitai](https://github.com/compile10/kaitai) - 一個使用人工智慧來分析日語句子結構的應用程式。這個工具可以將詞語和片語之間的關係可視化，並通過互動圖表展示語法關係。
 * [tsukeru-furigana-converter](https://github.com/ln2058/tsukeru-furigana-converter) - 瀏覽器擴充功能（Chrome/Edge/Firefox），可按需將振假名注入日文網頁；包括詞典工具提示、JLPT篩選和詞彙/Anki導出。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bangumi-data](https://github.com/bangumi-data/bangumi-data) | 📥 442/week | 📦 58k | ⭐ 596 | 🟢 today|
| 🔗 [yomichan](https://github.com/FooSoft/yomichan) | - | - | ⭐ 1.1k | 🔴 february 2023|
| 🔗 [proofreading-tool](https://github.com/gecko655/proofreading-tool) | - | - | ⭐ 87 | 🟡 october 2025|
| 🔗 [kanjigrid](https://github.com/minosvasilias/kanjigrid) | - | - | ⭐ 44 | 🔴 november 2018|
| 🔗 [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) | - | - | ⭐ 62 | 🔴 january 2023|
| 🔗 [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) | 📥 34k/week | 📦 4.9M | ⭐ 18 | 🔴 january 2025|
| 🔗 [hatsuon](https://github.com/DJTB/hatsuon) | 📥 5/week | 📦 903 | ⭐ 38 | 🔴 march 2022|
| 🔗 [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) | - | - | ⭐ 10 | 🔴 december 2021|
| 🔗 [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) | 📥 65/week | 📦 6k | ⭐ 8 | 🔴 july 2016|
| 🔗 [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) | 📥 1/week | 📦 274 | ⭐ repo not found | 🔴 repo not found|
| 🔗 [oskim](https://github.com/esrille/oskim) | - | - | ⭐ 2 | 🔴 february 2023|
| 🔗 [tweetMapping](https://github.com/wtnv-lab/tweetMapping) | - | - | ⭐ 26 | 🟢 march|
| 🔗 [pitch-accent](https://github.com/shirakaba/pitch-accent) | 📥 rate limited by upstream service | 📦 85 | ⭐ 2 | 🔴 september 2023|
| 🔗 [kana2ipa](https://github.com/amanoese/kana2ipa) | - | - | ⭐ 17 | 🔴 october 2020|
| 🔗 [voicevox](https://github.com/VOICEVOX/voicevox) | - | - | ⭐ 3.1k | 🟢 march|
| 🔗 [kamiya-codec](https://github.com/fasiha/kamiya-codec) | - | - | ⭐ 22 | 🟡 may 2025|
| 🔗 [closewords](https://github.com/otoneko1102/closewords) | - | - | ⭐ 4 | 🟢 march|
| 🔗 [japanese-analyzer](https://github.com/cokice/japanese-analyzer) | - | - | ⭐ 705 | 🟡 december 2025|
| 🔗 [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) | - | - | ⭐ 6 | 🔴 july 2024|
| 🔗 [yama](https://github.com/sapjax/yama) | - | - | ⭐ 8 | 🟢 february|
| 🔗 [kaitai](https://github.com/compile10/kaitai) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [tsukeru-furigana-converter](https://github.com/ln2058/tsukeru-furigana-converter) | - | - | ⭐ 1 | 🟢 march|


## Go

### Morphology analysis
以Go實作的輕量日文形態素分析函式庫

 * [kagome](https://github.com/ikawaha/kagome) - 純Go編寫的自包含日語形態分析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kagome](https://github.com/ikawaha/kagome) | - | - | ⭐ 956 | 🟢 last tuesday|


### Others
其他以Go為基礎的日文文本處理函式庫

 * [ojosama](https://github.com/jiro4989/ojosama) - 將文字轉換為百滿天原薩洛美小姐風格的口吻。
 * [nihongo](https://github.com/gojp/nihongo) - 日本語詞典
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - Yomichan 的外部詞典導入工具。
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - THE IDOLM@STER 日文輸入法詞彙表（由imas-db.jp提供）
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - 在Go中將漢字音譯為平假名/片假名/羅馬字將漢字音譯為平假名/片假名/羅馬字，在Go中
 * [go-moji](https://github.com/ktnyt/go-moji) - 一個用於全角/半角轉換的 Go 函式庫
 * [ojichat](https://github.com/greymd/ojichat) - 生成一些看起来像叔叔会通过LINE或邮件发送的文本
 * [name](https://github.com/kuniwak/name) - 日本名稱搜索器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ojosama](https://github.com/jiro4989/ojosama) | - | - | ⭐ 387 | 🟢 march|
| 🔗 [nihongo](https://github.com/gojp/nihongo) | - | - | ⭐ 83 | 🔴 february 2024|
| 🔗 [yomichan-import](https://github.com/FooSoft/yomichan-import) | - | - | ⭐ 86 | 🔴 february 2023|
| 🔗 [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) | - | - | ⭐ 32 | 🟢 january|
| 🔗 [go-kakasi](https://github.com/sarumaj/go-kakasi) | - | - | ⭐ 6 | 🟡 december 2025|
| 🔗 [go-moji](https://github.com/ktnyt/go-moji) | - | - | ⭐ 20 | 🔴 april 2019|
| 🔗 [ojichat](https://github.com/greymd/ojichat) | - | - | ⭐ 1.3k | 🔴 october 2024|
| 🔗 [name](https://github.com/kuniwak/name) | - | - | ⭐ 11 | 🔴 january 2025|


## Java

### Morphology analysis
用於日文形態素分析與辭典管理的函式庫

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji是一個自包含且非常易於使用的日語形態分析器，專為搜索而設計。
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - Sudachi詞彙表
 * [meval](https://github.com/teru-oka-1933/meval) - 形態素解析器性能評估系統 MevAL


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji](https://github.com/atilika/kuromoji) | - | - | ⭐ 1k | 🔴 september 2019|
| 🔗 [Sudachi](https://github.com/WorksApplications/Sudachi) | - | - | ⭐ 948 | 🔴 november 2024|
| 🔗 [SudachiDict](https://github.com/WorksApplications/SudachiDict) | - | - | ⭐ 283 | 🟢 january|
| 🔗 [meval](https://github.com/teru-oka-1933/meval) | - | - | ⭐ 7 | 🔴 august 2019|


### Others
支援日文NLP與OCR的Java函式庫

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 從圖像中識別日文字符的Java庫
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 將日本漢字轉換為羅馬字（拉丁字母）的Java庫和命令行工具
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Java中的漢字轉假名/片假名/羅馬字輸出
 * [Kamite](https://github.com/fauu/Kamite) - 一款桌面式的日語學習輔助工具
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - React Native 的非同步日本語分詞原生插件，適用於 iOS 和 Android。
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本語分析器使用Kuromoji日本語分詞器進行ElasticSearch。
 * [moji4j](https://github.com/andree-surya/moji4j) - 一個Java庫，可在日文平假名、片假名和羅馬字之間進行轉換。
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - mecab-neologd 的日文文本正規化工具
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - 日本的elasticsearch分析插件


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) | - | - | ⭐ 204 | 🔴 may 2021|
| 🔗 [jakaroma](https://github.com/nicolas-raoul/jakaroma) | - | - | ⭐ 68 | 🟡 june 2025|
| 🔗 [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) | - | - | ⭐ 55 | 🔴 april 2016|
| 🔗 [Kamite](https://github.com/fauu/Kamite) | - | - | ⭐ 132 | 🔴 march 2025|
| 🔗 [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) | - | - | ⭐ 38 | 🔴 june 2023|
| 🔗 [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) | - | - | ⭐ 29 | 🔴 march 2012|
| 🔗 [moji4j](https://github.com/andree-surya/moji4j) | - | - | ⭐ 33 | 🔴 june 2022|
| 🔗 [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) | - | - | ⭐ 5 | 🟢 february|
| 🔗 [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) | - | - | ⭐ 219 | 🟢 february|


## Pretrained model

### Word2Vec
將單詞轉換為向量以學習語意關係的模型

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - 使用Gensim和Mecab的日語Word2vec（單詞到向量）方法。
 * [chiVe](https://github.com/WorksApplications/chiVe) - 使用Sudachi和NWJC的日語詞嵌入
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - 艾摩日文
 * [embedrank](https://github.com/yagays/embedrank) - EmbedRank 的 Python 實現
 * [aovec](https://github.com/eggplants/aovec) - 簡易青空文庫Word2Vec建構器 - 青空文庫全書籍的Word2Vec建構器+已建構模型
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - 這是 AI LAB 文章「係り受けに基づく日本語単語埋込 (Dependency-based Japanese Word Embeddings)」的儲存庫 (文章網址 https://ai-lab.lapras.com/nlp/japanese-word-embedding/)。
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - 另一個日本維基百科實體向量
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 從最新的日本語Wikipedia傾印數據中，使用MeCab在IPA詞典和最新的Neologd詞典中進行形態素分析，並基於該結果學習word2vec、fastText和GloVe的詞向量表示的腳本。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) | - | - | ⭐ 87 | 🔴 august 2020|
| 🔗 [chiVe](https://github.com/WorksApplications/chiVe) | - | - | ⭐ 171 | 🔴 march 2024|
| 🔗 [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) | - | - | ⭐ 4 | 🔴 october 2019|
| 🔗 [embedrank](https://github.com/yagays/embedrank) | - | - | ⭐ 48 | 🔴 march 2019|
| 🔗 [aovec](https://github.com/eggplants/aovec) | 📥 197 | 📦 82k | ⭐ 3 | 🔴 january 2023|
| 🔗 [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) | - | - | ⭐ 8 | 🔴 august 2019|
| 🔗 [jawikivec](https://github.com/wikiwikification/jawikivec) | - | - | ⭐ 2 | 🔴 november 2018|
| 🔗 [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) | - | - | ⭐ 11 | 🔴 may 2020|


### Transformer based models
使用自注意力機制理解語境並執行高階語言任務的模型

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


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bert-japanese](https://github.com/cl-tohoku/bert-japanese) | - | - | ⭐ 543 | 🔴 march 2024|
| 🔗 [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [bert-japanese](https://github.com/yoheikikuta/bert-japanese) | - | - | ⭐ 498 | 🔴 february 2021|
| 🔗 [SudachiTra](https://github.com/WorksApplications/SudachiTra) | 📥 1k | 📦 162k | ⭐ 79 | 🔴 december 2023|
| 🔗 [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) | - | - | ⭐ 245 | 🔴 june 2023|
| 🔗 [shiba](https://github.com/octanove/shiba) | 📥 25 | 📦 7k | ⭐ 89 | 🔴 november 2023|
| 🔗 [Dialog](https://github.com/reppy4620/Dialog) | - | - | ⭐ 72 | 🔴 october 2020|
| 🔗 [language-pretraining](https://github.com/retarfi/language-pretraining) | - | - | ⭐ 50 | 🔴 may 2023|
| 🔗 [medbertjp](https://github.com/ou-medinfo/medbertjp) | - | - | ⭐ 12 | 🔴 november 2020|
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
| 🔗 [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) | - | - | ⭐ 13 | 🔴 september 2023|
| 🔗 [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) | - | - | ⭐ 54 | 🟡 december 2025|
| 🔗 [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) | - | - | ⭐ 42 | 🔴 april 2024|


## ChatGPT
利用ChatGPT與API進行日文對話與文字生成的資源

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
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - 用於在Slack上使用OpenAI的ChatGPT API的Slackbot腳本（假設使用日語）用於在Slack上使用OpenAI的ChatGPT API的Slackbot腳本（假設使用日語）
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - 這是ChatGPT的提示示例。ChatGPT的提示示例。
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - 一個使用Python和Langchain構建的日語漢字閃卡應用程序，並搭載了GPT-4的智能增強功能。
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - 評估GPT-4和ChatGPT在日本醫學執照考試上的表現
 * [japagen](https://github.com/retrieva/japagen) - 使用LLM在日語任務中生成虛擬學習數據的研究
 * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - ChatGPT和Copilot等各種生成AI用的“日本語”的Prompt的樣本ChatGPT和Copilot等各種生成AI用的「日本語」的Prompt的樣本


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) | - | - | ⭐ 15 | 🔴 march 2023|
| 🔗 [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) | - | - | ⭐ 5 | 🔴 march 2023|
| 🔗 [wanna](https://github.com/hirokidaichi/wanna) | 📥 74 | 📦 20k | ⭐ 141 | 🔴 april 2023|
| 🔗 [ChatdollKit](https://github.com/uezo/ChatdollKit) | - | - | ⭐ 1.1k | 🟢 march|
| 🔗 [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) | - | - | ⭐ 1 | 🔴 march 2023|
| 🔗 [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) | - | - | ⭐ 27 | 🔴 may 2023|
| 🔗 [vrchatbot](https://github.com/Geson-anko/vrchatbot) | - | - | ⭐ 29 | 🔴 december 2022|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) | - | - | ⭐ 16 | 🔴 april 2023|
| 🔗 [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) | - | - | ⭐ 1 | 🔴 april 2023|
| 🔗 [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) | - | - | ⭐ 46 | 🔴 december 2023|
| 🔗 [chatvrm](https://github.com/pixiv/chatvrm) | - | - | ⭐ 831 | 🟡 may 2025|
| 🔗 [sftly-replace](https://github.com/kmizu/sftly-replace) | - | - | ⭐ 4 | 🔴 may 2023|
| 🔗 [summarize_arxv](https://github.com/rkmt/summarize_arxv) | - | - | ⭐ 173 | 🔴 may 2023|
| 🔗 [aiavatarkit](https://github.com/uezo/aiavatarkit) | - | - | ⭐ 562 | 🟢 last friday|
| 🔗 [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) | - | - | ⭐ 280 | 🟢 march|
| 🔗 [character_chat](https://github.com/mutaguchi/character_chat) | - | - | ⭐ 16 | 🔴 june 2023|
| 🔗 [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) | - | - | ⭐ 64 | 🔴 july 2024|
| 🔗 [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) | - | - | ⭐ 426 | 🟢 last monday|
| 🔗 [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) | - | - | ⭐ 6 | 🔴 october 2023|
| 🔗 [IgakuQA](https://github.com/jungokasai/IgakuQA) | - | - | ⭐ 49 | 🔴 march 2023|
| 🔗 [japagen](https://github.com/retrieva/japagen) | - | - | ⭐ 1 | 🔴 october 2024|
| 🔗 [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) | - | - | ⭐ 426 | 🟢 last monday|


## Dictionary and IME
與日文字典與輸入法相關的資源

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
 * [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) - 琉球語辭典（沖繩語辭典）
 * [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) - 讀取：讀取日本和中文詞典對於讀取。
 * [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) - 滑鼠懸停在單字上時，自動讀取的通用辭典工具
 * [jisyo](https://github.com/skk-dict/jisyo) - 為SKK的新辭典格式的假名漢字轉換引擎
 * [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) - 日本語的讀音轉換為 Emoji 的 SKK 字典 😂
 * [anthy](https://github.com/netsphere-labs/anthy) - Anthy是一個日文的假名漢字轉換引擎。它將羅馬字轉換為假名，並將假名文本轉換為混合假名和漢字。
 * [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) - AWS服務名稱的Google日文輸入詞典
 * [cl-skkserv](https://github.com/tani/cl-skkserv) - 使用Common Lisp構建的SKK詞典伺服器及其擴展
 * [anthy](https://github.com/xorgy/anthy) - 安西維護
 * [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) - 安西Unicode - 另一個安西
 * [azooKey](https://github.com/ensan-hcl/azooKey) - azooKey：一個完全使用Swift開發的日本鍵盤iOS應用程式
 * [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) - 日文輸入法azooKey桌面版，支援macOS
 * [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) - 由azooKey引擎提供支援的fcitx5日文輸入法由azooKey引擎提供支援的fcitx5日文輸入法
 * [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) - Mozc UT 地名字典是從日本郵政的郵遞區號數據轉換而來的字典。
 * [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) - 使用Swift编写的假名-汉字转换模块
 * [libkkc](https://github.com/ueno/libkkc) - 日文假名漢字轉換輸入法庫
 * [libskk](https://github.com/ueno/libskk) - 日本 SKK 輸入法庫
 * [kanayomi-dict](https://github.com/warihima/kanayomi-dict) - openjtalk形式的用戶詞典
 * [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) - 漢字資料庫的字典相關資料
 * [wlsp-classical](https://github.com/yocjyet/wlsp-classical) - 古典日本語的分類詞彙表數據
 * [kanji-dict](https://github.com/marmooo/kanji-dict) - 漢字的書寫順序(筆順)、讀音、畫數、部首、用例、起源等資訊的漢字詞典。收錄了Unicode 15.1版本中的所有漢字，共98682個字。
 * [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) - (๑ ᴖ ᴑ ᴖ ๑)みょんかおもじ（舊Kaomoji_proj）是一個為Microsoft公司的輸入軟件Microsoft IME製作表情符號詞典的項目。
 * [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) - Kotlin 假名漢字轉換程式
 * [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) - 使用jisho.org的日英詞典，具有音頻功能，可以導出CSV條目，並預覽詞典網站。
 * [ichiran](https://github.com/tshatrov/ichiran) - 日語文本的語言工具
 * [mikan](https://github.com/mojyack/mikan) - 一種日本輸入法。
 * [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) - 關西方言日語教材的快速參考。
 * [jisho-open](https://github.com/hlorenzi/jisho-open) - JMdict日英詞典項目的Web前端，支持學習列表！
 * [macskk](https://github.com/mtgto/macskk) - 另一個 macOS SKK 輸入法
 * [nandoku](https://github.com/marmooo/nandoku) - 難讀漢字按年級整理的辭典。
 * [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) - 一個用於安卓系統的自由開源軟體日文輸入法。
 * [anthywl](https://github.com/tadeokondrak/anthywl) - 使用libanthy為Sway提供的日文輸入法
 * [sekka](https://github.com/kiyoka/sekka) - 受 SKK 啟發的另一種日本輸入法。
 * [sumibi](https://github.com/kiyoka/sumibi) - 由ChatGPT API提供動力的日文輸入法
 * [jinmei-dict](https://github.com/s1r-j/jinmei-dict) - 從辭書數據中提取出人名，並按照讀音假名（片假名）作為鍵，將候選的寫字形式整理成JSON格式，以列表形式保存。
 * [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) - 菫 完全離線的日文鍵盤應用程式
 * [japanesearabic](https://github.com/a-hamdi/japanesearabic) - 日本語・アラビア語辞書 (Yomitan) قاموس اللغة اليابانية والعربية
 * [o-dic](https://github.com/makotoga/o-dic) - 沖繩辭書
 * [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) - SKK 繪文字辭書
 * [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) - Mozc的個人姓名字典
 * [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) - 從SudachiDict轉換為Mozc的字典
 * [nihongo](https://github.com/sph-mn/nihongo) - 日語語言數據和詞典
 * [kagome-dict](https://github.com/ikawaha/kagome-dict) - Kagome v2 的字典库
 * [canna](https://github.com/canna-input/canna) - 干那日本輸入系統
 * [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) - 京阪式口音（關西方言）詞典 - 收錄了4,615個日本方言口音的詞彙
 * [jitendex](https://github.com/jitendex/jitendex) - 一個免費、離線和開放授權的日語至英語詞典。每月更新！
 * [karukan](https://github.com/togatoga/karukan) - Linux的日文輸入法系統，神經假名漢字轉換引擎 + fcitx5輸入法
 * [shitto-mania-dic](https://github.com/junikematsu/shitto-mania-dic) - 嫉妒辭典（Shitto-Mania / Jealousy Dictionary）


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) | - | - | ⭐ 2.8k | 🔴 september 2020|
| 🔗 [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) | - | - | ⭐ 124 | 🔴 march 2024|
| 🔗 [jamdict](https://github.com/neocl/jamdict) | 📥 205 | 📦 53k | ⭐ 168 | 🔴 june 2021|
| 🔗 [unidic-py](https://github.com/polm/unidic-py) | 📥 57k | 📦 10M | ⭐ 109 | 🔴 february 2025|
| 🔗 [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) | - | - | ⭐ 100 | 🔴 january 2023|
| 🔗 [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) | - | - | ⭐ 7 | 🔴 april 2021|
| 🔗 [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) | - | - | ⭐ 60 | 🟢 last monday|
| 🔗 [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) | - | - | ⭐ 40 | 🔴 january 2021|
| 🔗 [JumanDIC](https://github.com/ku-nlp/JumanDIC) | - | - | ⭐ 4 | 🔴 august 2022|
| 🔗 [ipadic-py](https://github.com/polm/ipadic-py) | 📥 32k | 📦 7M | ⭐ 24 | 🔴 october 2021|
| 🔗 [unidic-lite](https://github.com/polm/unidic-lite) | 📥 69k | 📦 10M | ⭐ 49 | 🔴 september 2020|
| 🔗 [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) | - | - | ⭐ 365 | 🔴 january 2023|
| 🔗 [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) | - | - | ⭐ 102 | 🔴 january 2023|
| 🔗 [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) | - | - | ⭐ 82 | 🔴 september 2024|
| 🔗 [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) | - | - | ⭐ 58 | 🔴 december 2016|
| 🔗 [emoticon](https://github.com/tiwanari/emoticon) | - | - | ⭐ 44 | 🔴 may 2020|
| 🔗 [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) | - | - | ⭐ 10 | 🔴 january 2018|
| 🔗 [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) | - | - | ⭐ 2 | 🔴 november 2022|
| 🔗 [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) | - | - | ⭐ 36 | 🟢 march|
| 🔗 [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) | - | - | ⭐ 0 | 🔴 january 2020|
| 🔗 [EJDict](https://github.com/kujirahand/EJDict) | - | - | ⭐ 250 | 🟡 november 2025|
| 🔗 [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) | - | - | ⭐ 26 | 🔴 may 2024|
| 🔗 [genshin-dict](https://github.com/kotofurumiya/genshin-dict) | - | - | ⭐ 126 | 🟢 february|
| 🔗 [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) | - | - | ⭐ 340 | 🟢 last monday|
| 🔗 [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) | - | - | ⭐ 69 | 🟡 september 2025|
| 🔗 [mh-dict-jp](https://github.com/utubo/mh-dict-jp) | - | - | ⭐ 5 | 🟡 april 2025|
| 🔗 [jitenbot](https://github.com/stephenmk/jitenbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) | - | - | ⭐ 87 | 🔴 september 2020|
| 🔗 [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) | - | - | ⭐ 24 | 🔴 december 2024|
| 🔗 [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) | - | - | ⭐ 252 | 🟢 february|
| 🔗 [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) | - | - | ⭐ 125 | 🟡 august 2025|
| 🔗 [Jitendex](https://github.com/stephenmk/Jitendex) | - | - | ⭐ 459 | 🟢 today|
| 🔗 [jiten](https://github.com/obfusk/jiten) | - | - | ⭐ 129 | 🔴 december 2023|
| 🔗 [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) | - | - | ⭐ 55 | 🟢 march|
| 🔗 [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) | - | - | ⭐ 4 | 🟢 march|
| 🔗 [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) | - | - | ⭐ 740 | 🟢 last wednesday|
| 🔗 [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) | - | - | ⭐ 72 | 🔴 january 2020|
| 🔗 [jisyo](https://github.com/skk-dict/jisyo) | - | - | ⭐ 28 | 🔴 september 2023|
| 🔗 [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) | - | - | ⭐ 30 | 🔴 march 2018|
| 🔗 [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) | - | - | ⭐ 7 | 🔴 november 2019|
| 🔗 [cl-skkserv](https://github.com/tani/cl-skkserv) | - | - | ⭐ 31 | 🔴 october 2024|
| 🔗 [anthy](https://github.com/xorgy/anthy) | - | - | ⭐ 3 | 🔴 july 2013|
| 🔗 [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) | - | - | ⭐ 41 | 🟢 march|
| 🔗 [azooKey](https://github.com/ensan-hcl/azooKey) | - | - | ⭐ 675 | 🟢 yesterday|
| 🔗 [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) | - | - | ⭐ 861 | 🟢 march|
| 🔗 [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) | - | - | ⭐ 178 | 🟢 february|
| 🔗 [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) | - | - | ⭐ 22 | 🟢 march|
| 🔗 [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) | - | - | ⭐ 138 | 🟢 yesterday|
| 🔗 [libkkc](https://github.com/ueno/libkkc) | - | - | ⭐ 112 | 🔴 august 2024|
| 🔗 [libskk](https://github.com/ueno/libskk) | - | - | ⭐ 100 | 🟢 march|
| 🔗 [kanayomi-dict](https://github.com/warihima/kanayomi-dict) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) | - | - | ⭐ 108 | 🔴 september 2017|
| 🔗 [wlsp-classical](https://github.com/yocjyet/wlsp-classical) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [kanji-dict](https://github.com/marmooo/kanji-dict) | - | - | ⭐ 6 | 🟢 march|
| 🔗 [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) | - | - | ⭐ 11 | 🟡 october 2025|
| 🔗 [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) | - | - | ⭐ 5 | 🟡 november 2025|
| 🔗 [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) | - | - | ⭐ 6 | 🟢 february|
| 🔗 [ichiran](https://github.com/tshatrov/ichiran) | - | - | ⭐ 388 | 🟢 january|
| 🔗 [mikan](https://github.com/mojyack/mikan) | - | - | ⭐ 24 | 🟡 june 2025|
| 🔗 [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) | - | - | ⭐ 9 | 🟢 february|
| 🔗 [jisho-open](https://github.com/hlorenzi/jisho-open) | - | - | ⭐ 57 | 🟢 february|
| 🔗 [macskk](https://github.com/mtgto/macskk) | - | - | ⭐ 281 | 🟢 last friday|
| 🔗 [nandoku](https://github.com/marmooo/nandoku) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [anthywl](https://github.com/tadeokondrak/anthywl) | - | - | ⭐ 34 | 🟡 april 2025|
| 🔗 [sekka](https://github.com/kiyoka/sekka) | - | - | ⭐ 24 | 🟡 july 2025|
| 🔗 [sumibi](https://github.com/kiyoka/sumibi) | - | - | ⭐ 39 | 🟢 march|
| 🔗 [jinmei-dict](https://github.com/s1r-j/jinmei-dict) | - | - | ⭐ 7 | 🔴 april 2020|
| 🔗 [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) | - | - | ⭐ 219 | 🟢 yesterday|
| 🔗 [japanesearabic](https://github.com/a-hamdi/japanesearabic) | - | - | ⭐ 18 | 🟡 may 2025|
| 🔗 [o-dic](https://github.com/makotoga/o-dic) | - | - | ⭐ 6 | 🟢 february|
| 🔗 [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) | - | - | ⭐ 141 | 🔴 january 2025|
| 🔗 [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) | - | - | ⭐ 26 | 🟢 march|
| 🔗 [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) | - | - | ⭐ 22 | 🟢 february|
| 🔗 [nihongo](https://github.com/sph-mn/nihongo) | - | - | ⭐ 19 | 🔴 january 2025|
| 🔗 [kagome-dict](https://github.com/ikawaha/kagome-dict) | - | - | ⭐ 15 | 🟢 march|
| 🔗 [canna](https://github.com/canna-input/canna) | - | - | ⭐ 4 | 🟡 august 2025|
| 🔗 [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) | - | - | ⭐ 1 | 🟡 december 2025|
| 🔗 [jitendex](https://github.com/jitendex/jitendex) | - | - | ⭐ 459 | 🟢 today|
| 🔗 [karukan](https://github.com/togatoga/karukan) | - | - | ⭐ 237 | 🟢 february|
| 🔗 [shitto-mania-dic](https://github.com/junikematsu/shitto-mania-dic) | - | - | ⭐ 0 | 🟢 last tuesday|


## Corpus

### Part-of-speech tagging / Named entity recognition
附有詞性與命名實體標註的日文語料庫

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - 使用維基百科進行日語固有表現抽取的資料集
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 用於命名實體識別的日語IOB2標記語料庫。
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter 語料庫
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - 平行通用依存句法。
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - 從Google UDT 2.0輸入的日本數據。
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大學網頁文件引導語料庫
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 註釋版的富滿開取中心語料庫
 * [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) - UD_Japanese-GSD的長單位詞版本
 * [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) - 這個通用依存關係（UD）日語樹庫是基於UD文檔中描述的UD日語慣例定義。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) | - | - | ⭐ 142 | 🔴 september 2023|
| 🔗 [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) | - | - | ⭐ 61 | 🔴 february 2020|
| 🔗 [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) | - | - | ⭐ 21 | 🔴 march 2016|
| 🔗 [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) | - | - | ⭐ 0 | 🔴 may 2020|
| 🔗 [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) | - | - | ⭐ 28 | 🔴 may 2022|
| 🔗 [KWDLC](https://github.com/ku-nlp/KWDLC) | - | - | ⭐ 83 | 🔴 december 2023|
| 🔗 [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) | - | - | ⭐ 18 | 🔴 december 2023|
| 🔗 [anthy](https://github.com/netsphere-labs/anthy) | - | - | ⭐ 15 | 🔴 february 2023|
| 🔗 [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) | - | - | ⭐ 3 | 🟡 november 2025|
| 🔗 [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) | - | - | ⭐ 26 | 🟡 november 2025|


### Parallel corpus
包含對齊句子的多語對譯語料庫

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
 * [matcha](https://github.com/ehimenlp/matcha) - 從訪日觀光客專門媒體MATCHA的文章中，我們建立了一個用於簡化日文文本的數據集。
 * [en-ja-el](https://github.com/shigashiyama/en-ja-el) - EnJaEL：En-Ja平行實體連結數據集（版本1.0）EnJaEL：En-Ja平行實體連結數據集（版本1.0）


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [small_parallel_enja](https://github.com/odashi/small_parallel_enja) | - | - | ⭐ 98 | 🔴 september 2019|
| 🔗 [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) | - | - | ⭐ 15 | 🔴 september 2023|
| 🔗 [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) | - | - | ⭐ 15 | 🔴 august 2024|
| 🔗 [JESC](https://github.com/rpryzant/JESC) | - | - | ⭐ 87 | 🔴 november 2017|
| 🔗 [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) | - | - | ⭐ 11 | 🔴 december 2020|
| 🔗 [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) | - | - | ⭐ 5 | 🔴 august 2019|
| 🔗 [jesc_small](https://github.com/yusugomori/jesc_small) | - | - | ⭐ 3 | 🔴 july 2019|
| 🔗 [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) | - | - | ⭐ 6 | 🟡 august 2025|
| 🔗 [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) | - | - | ⭐ 149 | 🟢 february|
| 🔗 [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) | - | - | ⭐ 18 | 🔴 november 2021|
| 🔗 [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) | - | - | ⭐ 4 | 🔴 march 2020|
| 🔗 [matcha](https://github.com/ehimenlp/matcha) | - | - | ⭐ 6 | 🔴 january 2025|
| 🔗 [en-ja-el](https://github.com/shigashiyama/en-ja-el) | - | - | ⭐ 2 | 🔴 january 2025|


### Dialog corpus
用於訓練對話系統的會話語料集

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本電影推薦對話數據集
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - 透過爬蟲從Open 2ch網站建立的對話語料庫
 * [BSD](https://github.com/tsuruoka-lab/BSD) - 商業場景對話語料庫
 * [asdc](https://github.com/megagonlabs/asdc) - 住宿搜索對話語料庫 (宿泊施設探索對話語料庫)
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - 日語對話資料，適用於seq2seq等。
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - 這個存儲庫包含了在AACL-IJCNLP 2022的Eval4NLP 2022研討會上發表的論文《Chat Translation Error Detection for Assisting Cross-lingual Communications》中所發布的日英雙語聊天語料庫BPersona-chat。
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 日本語日常対話コーパス是一個高品質的多輪對話數據集，包含五個主題的日常對話：生活、學校、旅行、健康和娛樂。
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - LLM構築用的日本語聊天資料集
 * [kokorochat](https://github.com/uec-inabalab/kokorochat) - 透過角色扮演收集的日語諮詢對話數據集
 * [JMultiWOZ-TC](https://github.com/llm-jp/JMultiWOZ-TC) - 在多輪對話中評估代理人的function calling
 * [HOTATE](https://github.com/EhimeNLP/HOTATE) - 本音・建前付き日本語對話數據集
 * [ETCDataset](https://github.com/UEC-InabaLab/ETCDataset) - 情感轉錄對話數據集包含約1,000個對話，每個對話都包含對話者自己記錄的情感文。這是一個日語對話數據集。


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
| 🔗 [kokorochat](https://github.com/uec-inabalab/kokorochat) | - | - | ⭐ 19 | 🟡 august 2025|
| 🔗 [JMultiWOZ-TC](https://github.com/llm-jp/JMultiWOZ-TC) | - | - | ⭐ 0 | 🟢 march|
| 🔗 [HOTATE](https://github.com/EhimeNLP/HOTATE) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [ETCDataset](https://github.com/UEC-InabaLab/ETCDataset) | - | - | ⭐ 11 | 🟢 january|

### Others
針對問答或語意推理等任務的日文資料集

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
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - COMET-ATOMIC ja彗星原子 ja
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
 * [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) - 從青空文庫和Sapie點字數據創建的假名數據集從青空文庫及及サピエ的點字數據創建的振り仮名的數據集
 * [koniwa](https://github.com/koniwa/koniwa) - 一個包含日語註釋聲音的開放收藏。
 * [JMMLU](https://github.com/nlp-waseda/JMMLU) - 日本語大規模マルチタスク言語理解ベンチマーク
 * [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) - 青空文庫振り仮名註釋附音訊語料庫的數據集
 * [jqara](https://github.com/hotchpotch/jqara) - JQaRA：具有檢索增強功能的日本問答系統 - 用於檢索增強(RAG)評估的日語問答資料集
 * [jemhopqa](https://github.com/aiishii/jemhopqa) - JEMHopQA（日本語説明可能なマルチホップ質問応答）は、内部推論を評価できる日本語マルチホップQAデータセットです。
 * [jacred](https://github.com/youmima/jacred) - 用於日文文件級關係提取數據集的存儲庫（計劃在三月份發布）。用於日文文件級關係提取數據集的存儲庫（計劃在三月份發布）。
 * [jades](https://github.com/naist-nlp/jades) - JADES是一個針對非母語使用者的日文文本簡化數據集，詳細介紹在《JADES:針對非母語使用者的日文新文本簡化數據集》（論文即將發表）。
 * [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) - 2023年8月，墨爾本大學公開了安全性評估數據集『Do-Not-Answer』，該數據集已經被自動翻譯成日語，並且考慮了日本文化進行了修正，以便在日語LLM評估中使用。
 * [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) - OpenAssistant 的開源數據 OASST1 已經被翻譯成日文的數據集。
 * [jacwir](https://github.com/hotchpotch/jacwir) - JaCWIR: 日本語休閒網路資訊檢索（Web IR） 日本語情報檢索評估的小型休閒Web標題和摘要資料集
 * [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) - 日本語學習者的科學技術業界常用片假名與原始單字對照表
 * [j-unimorph](https://github.com/cl-tohoku/j-unimorph) - UniMorph的日文數據集
 * [GazeVQA](https://github.com/riken-grp/GazeVQA) - LREC-COLING 2024論文的數據集《針對澄清日語問題的凝視導向視覺問答數據集》
 * [J-CRe3](https://github.com/riken-grp/J-CRe3) - J-CRe3 實驗代碼（上田等人，LREC-COLING，2024）
 * [jmed-llm](https://github.com/sociocom/jmed-llm) - JMED-LLM：大型語言模型的日本醫學評估數據集
 * [lawtext](https://github.com/yamachig/lawtext) - 日本法律的純文本格式日本法律的純文本格式
 * [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) - OCR處理程式研究開發項目中所建立的OCR學習用數據集。
 * [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) - 話題基礎的語義模糊解決評估集
 * [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) - Jamp：用於評估語言模型泛化能力的受控日語時間推理數據集
 * [JSeM](https://github.com/DaisukeBekki/JSeM) - 日本語意義測試套件（FraCaS對應及擴展）
 * [niilc-qa](https://github.com/mynlp/niilc-qa) - NIILC QA 數據
 * [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) - 請將以下內容翻譯為繁體中文。日本論文《鏈條思維提示的驗證》的數據集
 * [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) - 這是一個包含維基百科文章和各種語言標註的日文文本語料庫。
 * [elaws-history](https://github.com/kissge/elaws-history) - 透過 e-Gov 法令檢索平台定期下載並存檔所有法令資料。
 * [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) - Japanese-RP-Bench是用來測量LLM的日語角色扮演能力的基準。
 * [hdic](https://github.com/shikeda/hdic) - HDIC：日本早期漢字詞典集成數據庫
 * [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) - 精彩的日本開放數據-日本的開放數據信息列表和摘要
 * [kanji-data](https://github.com/mimneko/kanji-data) - 常用漢字表，與漢字相關的數據
 * [openchj-genji](https://github.com/togiso/openchj-genji) - 「源氏物語」形態論情報數據
 * [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) - 這個存儲庫包含我們論文《AdParaphrase: 用於分析語言特徵以生成吸引人廣告文本的改寫數據集》的數據。
 * [Jamp_sp](https://github.com/ynklab/Jamp_sp) - 考慮到方面的控制日本時間推論數據集的構建（Jamp_sp：考慮到方面的控制日本時間推論數據集）
 * [jnli-neg](https://github.com/asahi-y/jnli-neg) - 這是用於評估否定理解能力的日語語言推論數據集 JNLI-Neg 的公開存儲庫。
 * [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) - 該存儲庫提供了用於構建Swallow Corpus Version 1的Python實現，這是一個大型的日本網絡語料庫（Okazaki等人，2024年），來自Common Crawl檔案。
 * [jalecon](https://github.com/naist-nlp/jalecon) - 一個針對非母語讀者的日語詞彙複雜度數據集
 * [multils-japanese](https://github.com/naist-nlp/multils-japanese) - MultiLS-日語詞彙複雜度預測和詞彙簡化數據集：標註者檔案、未聚合標註和標註指南。
 * [nwjc](https://github.com/masayu-a/nwjc) - NINJAL 網絡日本語語料庫
 * [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) - 請將以下內容翻譯成繁體中文。在AAAI21中介紹的《Towards Fully Automated Manga Translation》論文中介紹的數據集
 * [public-annotations](https://github.com/manga109/public-annotations) - Manga109數據集的各種註釋
 * [gimei](https://github.com/willnet/gimei) - 隨機日本姓名和地址生成器
 * [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) - 評估日語語言模型安全性行為的測試集
 * [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) - 一個簡單的、開源的日語擬聲詞和擬音詞聲音詞彙的JSON格式收集。附帶漫畫示例。
 * [kanji](https://github.com/sylhare/kanji) - 要學習的日本漢字部首列表
 * [jethics](https://github.com/language-media-lab/jethics) - 日本語道徳理解度評価用數據集JETHICS的概述頁面（待更新）
 * [waon](https://github.com/llm-jp/waon) - WAON：用於視覺語言模型的大規模高質量日本圖像文本數據集
 * [kuci](https://github.com/ku-nlp/kuci) - 京都大學常識推理數據集（KUCI）
 * [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) - 解析困難的日本地址測試數據集
 * [jlpt-word-list](https://github.com/elzup/jlpt-word-list) - JLPT詞彙的日語單詞列表
 * [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) - 文字圖像數據集（平假名73個字符版）
 * [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) - 日本的法令多項選擇問答數據集
 * [yjcaptions](https://github.com/yahoojapan/yjcaptions) - YJ字幕26k數據集
 * [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) - 日本視覺基因組VQA數據集
 * [lawhub](https://github.com/lwhb/lawhub) - 用文本格式跟踪日本法律的存储库
 * [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) - 從日本戲劇、動畫和電影字幕中提取的詞頻列表
 * [jconj](https://github.com/yamagoya/jconj) - 一個基於表格的日文詞彙變化器
 * [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) - 從維基百科日文中提取個人姓名。
 * [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) - 基於日常日語會話語料庫的yomichan頻率詞典
 * [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) - 維基百科雙語參考資料（日文）
 * [ajimee-bench](https://github.com/azookey/ajimee-bench) - AJIMEE-Bench（高級日語輸入法評估基準）
 * [j-spaw](https://github.com/takamichi-lab/j-spaw) - J-SpAW：用於語音識別和防欺騙的日語語音語料庫
 * [camera3](https://github.com/cyberagentailab/camera3) - 相機3：一個用於日文可控廣告文本生成的評估數據集
 * [jgpqa](https://github.com/llm-jp/jgpqa) - GPQA數據集的日文翻譯
 * [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) - 正在去除田中语料库的噪音。
 * [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) - 日本情感語料庫德島大學A-2實驗室。
 * [osworld-jp](https://github.com/karakuri-ai/osworld-jp) - 為了考慮語言的評估，日語版電腦使用基準测试
 * [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) - 擬似日本評論 (擬似レビューデータ)
 * [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) - 精神科初診病歷製作問卷數據集
 * [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) - 市鎮村合併等導致舊地名消失的舊地名與新地名對應表
 * [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) - 日本文本表情符號數據。
 * [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) - 聽錯誤語料庫︱CSV＋表格架構 約1萬條記錄，使用VS Code＋pre-commit＋Frictionless＋GitHub Actions進行自動驗證的日語數據集。
 * [kotowaza](https://github.com/septn/kotowaza) - 結構化的JSON數據集，包含日本諺語（kotowaza）的印尼文和英文含義，例子，JLPT級別和標籤。結構化的JSON數據集，包含日本諺語（kotowaza）的印尼文和英文含義，例子，JLPT級別和標籤。
 * [selective-rag-kasensabo](https://github.com/tk-yasuno/selective-rag-kasensabo) - 建設技術標準相關問題的專業性細度（細/粗）可自動判定96％準確，選擇最佳的RAG系統（ColBERT/Naive）的實用Agentic RAG系統MVP。該系統於2025年11月針對河川防砂壩技術標準建立了四個RAG系統，並對200個不同專業性細度的問題進行了準確度和速度比較。
 * [jmle2026-bench](https://github.com/naoto-iwase/jmle2026-bench) - 2026年2月7日至8日第120屆日本醫學執照考試的LLM基準
 * [JSTS-Neg](https://github.com/reiko-y/JSTS-Neg) - 這是用於評估否定理解能力的日語意義相似度計算數據集JSTS-Neg的公開存儲庫。JSTS-Neg是通過擴展包含在JGLUE中的語言推論數據集JSTS而創建的。
 * [business-slide-questions](https://github.com/stockmarkteam/business-slide-questions) - 在這個存儲庫中，我們提供了針對商業資料（幻燈片）的視覺問答（VQA）基準測試"BusinessSlideVQA"。
 * [WLSP-antonym](https://github.com/masayu-a/WLSP-antonym) - 根據語義原則的詞彙列表（WLSP）的反義詞關係
 * [YouCook2-JP](https://github.com/nlab-mpg/YouCook2-JP) - YouCook2數據集的日文翻譯。
 * [E2U](https://github.com/sociocom/E2U) - 傳播化相關數據
 * [annotation-2025](https://github.com/Tiny-Colony/annotation-2025) - 這個存儲庫是為了公開可以比較人工和LLM輸出的文本“解釋”的數據。
 * [jhpt](https://github.com/nict-astrec-att/jhpt) - 歷史的日本語資料的原文文本和現代語翻譯（參照譯）文本已經按段落對應起來，形成對譯資料集。詳細內容請參考論文。
 * [JBE-QA](https://github.com/hancules/JBE-QA) - 日本司法考试问答
 * [j-spaw](https://github.com/takamichi-lab/j-spaw) - J-SpAW：用於語音識別和防欺騙的日語語音語料庫
 * [JMedWiC](https://github.com/EhimeNLP/JMedWiC) - 利用遮罩語言模型自動提取虛擬的同義和非同義對，通過人工同義性標註來確定標籤，從而構建了日本醫療領域詞義一致性判定數據集。
 * [jhpt](https://github.com/nict-astrec-att/jhpt) - 歷史的日本語資料的原文文本和現代語翻譯（參照譯）文本已經按段落對應起來，形成對譯資料集。詳細內容請參考論文。
 * [Doppelganger-JC](https://github.com/0017-alt/Doppelganger-JC) - 這是一個資料集，用於評估語言模型中中日跨語言同形異義詞的誤用情況。
 * [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) - 軟體圖理解的VLM評估基準（日文、英文、韓文對應）
 * [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) - 在日本語人事勞務領域中，LLM的性能評估基準的長篇內容Benchmark


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) | - | - | ⭐ 77 | 🔴 june 2023|
| 🔗 [kanji-data](https://github.com/davidluzgouveia/kanji-data) | - | - | ⭐ 208 | 🟢 february|
| 🔗 [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) | - | - | ⭐ 102 | 🔴 december 2021|
| 🔗 [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) | - | - | ⭐ 32 | 🔴 march 2017|
| 🔗 [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) | - | - | ⭐ 140 | 🔴 september 2018|
| 🔗 [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) | - | - | ⭐ 110 | 🔴 january 2022|
| 🔗 [JaNLI](https://github.com/verypluming/JaNLI) | - | - | ⭐ 17 | 🔴 may 2023|
| 🔗 [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) | - | - | ⭐ 18 | 🔴 december 2020|
| 🔗 [emoji-ja](https://github.com/yagays/emoji-ja) | - | - | ⭐ 83 | 🔴 march 2025|
| 🔗 [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) | - | - | ⭐ 35 | 🔴 march 2020|
| 🔗 [ja.text8](https://github.com/Hironsan/ja.text8) | - | - | ⭐ 111 | 🔴 october 2017|
| 🔗 [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) | - | - | ⭐ 31 | 🔴 april 2018|
| 🔗 [japanese](https://github.com/hingston/japanese) | - | - | ⭐ 87 | 🔴 september 2018|
| 🔗 [kanji-frequency](https://github.com/scriptin/kanji-frequency) | - | - | ⭐ 156 | 🟢 yesterday|
| 🔗 [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) | - | - | ⭐ 24 | 🔴 january 2021|
| 🔗 [CoARiJ](https://github.com/chakki-works/CoARiJ) | - | - | ⭐ 94 | 🔴 december 2020|
| 🔗 [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) | - | - | ⭐ 26 | 🔴 july 2023|
| 🔗 [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) | - | - | ⭐ 5 | 🔴 august 2021|
| 🔗 [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) | - | - | ⭐ 78 | 🔴 april 2024|
| 🔗 [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) | - | - | ⭐ 204 | 🔴 december 2021|
| 🔗 [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) | - | - | ⭐ 106 | 🟢 yesterday|
| 🔗 [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) | - | - | ⭐ 177 | 🟢 yesterday|
| 🔗 [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) | - | - | ⭐ 90 | 🔴 july 2018|
| 🔗 [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) | - | - | ⭐ 6 | 🔴 january 2019|
| 🔗 [speechBSD](https://github.com/ku-nlp/speechBSD) | - | - | ⭐ 3 | 🔴 february 2024|
| 🔗 [ita-corpus](https://github.com/mmorise/ita-corpus) | - | - | ⭐ 223 | 🟢 march|
| 🔗 [rohan4600](https://github.com/mmorise/rohan4600) | - | - | ⭐ 68 | 🟢 march|
| 🔗 [anlp-jp-history](https://github.com/whym/anlp-jp-history) | - | - | ⭐ 3 | 🔴 april 2024|
| 🔗 [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) | - | - | ⭐ 21 | 🔴 november 2022|
| 🔗 [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) | - | - | ⭐ 19 | 🔴 january 2021|
| 🔗 [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) | - | - | ⭐ 4 | 🔴 november 2018|
| 🔗 [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) | - | - | ⭐ 6 | 🔴 january 2020|
| 🔗 [wrime](https://github.com/ids-cv/wrime) | - | - | ⭐ 174 | 🟡 september 2025|
| 🔗 [jtubespeech](https://github.com/sarulab-speech/jtubespeech) | - | - | ⭐ 229 | 🔴 march 2023|
| 🔗 [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) | - | - | ⭐ 2 | 🔴 april 2022|
| 🔗 [kokkosho_data](https://github.com/rindybell/kokkosho_data) | - | - | ⭐ 1 | 🔴 july 2019|
| 🔗 [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) | - | - | ⭐ 83 | 🔴 june 2024|
| 🔗 [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) | - | - | ⭐ 31 | 🔴 september 2021|
| 🔗 [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) | - | - | ⭐ 31 | 🔴 february 2021|
| 🔗 [hirakanadic](https://github.com/po3rin/hirakanadic) | 📥 51 | 📦 14k | ⭐ 7 | 🔴 july 2023|
| 🔗 [animedb](https://github.com/anilogia/animedb) | - | - | ⭐ 329 | 🔴 january 2023|
| 🔗 [security_words](https://github.com/SaitoLab/security_words) | - | - | ⭐ 27 | 🔴 august 2023|
| 🔗 [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [honkoku-data](https://github.com/yuta1984/honkoku-data) | - | - | ⭐ 17 | 🟢 march|
| 🔗 [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) | - | - | ⭐ 35 | 🔴 december 2020|
| 🔗 [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) | - | - | ⭐ 1.9k | 🔴 november 2020|
| 🔗 [JSICK](https://github.com/verypluming/JSICK) | - | - | ⭐ 45 | 🔴 may 2023|
| 🔗 [phishurl-list](https://github.com/JPCERTCC/phishurl-list) | - | - | ⭐ 204 | 🟢 march|
| 🔗 [jcms](https://github.com/shigashiyama/jcms) | - | - | ⭐ 9 | 🔴 november 2022|
| 🔗 [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) | - | - | ⭐ 88 | 🔴 march 2023|
| 🔗 [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [topokanji](https://github.com/scriptin/topokanji) | - | - | ⭐ 200 | 🔴 january 2016|
| 🔗 [isbn4groups](https://github.com/uribo/isbn4groups) | - | - | ⭐ 1 | 🔴 june 2024|
| 🔗 [NMeCab](https://github.com/komutan/NMeCab) | - | - | ⭐ 98 | 🔴 march 2024|
| 🔗 [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) | - | - | ⭐ 15 | 🔴 january 2023|
| 🔗 [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) | - | - | ⭐ 3 | 🔴 july 2023|
| 🔗 [data_set](https://github.com/japanese-law-analysis/data_set) | - | - | ⭐ 50 | 🔴 january 2025|
| 🔗 [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) | - | - | ⭐ 4 | 🔴 january 2023|
| 🔗 [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) | - | - | ⭐ 20 | 🟢 march|
| 🔗 [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) | - | - | ⭐ 181 | 🟡 december 2025|
| 🔗 [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) | - | - | ⭐ 2 | 🔴 october 2023|
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
| 🔗 [ProSub](https://github.com/matbahasa/ProSub) | - | - | ⭐ 5 | 🟡 april 2025|
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 | 🟡 november 2025|
| 🔗 [ramendb](https://github.com/nuko-yokohama/ramendb) | - | - | ⭐ 7 | 🟢 march|
| 🔗 [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) | - | - | ⭐ 3 | 🔴 march 2023|
| 🔗 [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) | - | - | ⭐ 0 | 🔴 march 2021|
| 🔗 [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) | - | - | ⭐ 89 | 🔴 july 2023|
| 🔗 [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) | - | - | ⭐ 0 | 🔴 june 2023|
| 🔗 [meconaudio](https://github.com/elith-co-jp/meconaudio) | - | - | ⭐ 9 | 🔴 october 2023|
| 🔗 [japanese-addresses](https://github.com/geolonia/japanese-addresses) | - | - | ⭐ 761 | 🟡 december 2025|
| 🔗 [aozorasearch](https://github.com/myokoym/aozorasearch) | - | - | ⭐ 21 | 🟢 yesterday|
| 🔗 [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) | - | - | ⭐ 44 | 🔴 october 2023|
| 🔗 [alpaca_ja](https://github.com/shi3z/alpaca_ja) | - | - | ⭐ 86 | 🔴 may 2023|
| 🔗 [instruction_ja](https://github.com/megagonlabs/instruction_ja) | - | - | ⭐ 24 | 🔴 july 2023|
| 🔗 [japanese-family-names](https://github.com/siikamiika/japanese-family-names) | - | - | ⭐ 18 | 🔴 june 2017|
| 🔗 [kanji-data-media](https://github.com/kanjialive/kanji-data-media) | - | - | ⭐ 406 | 🔴 november 2023|
| 🔗 [reazonspeech](https://github.com/reazon-research/reazonspeech) | - | - | ⭐ 374 | 🟢 january|
| 🔗 [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) | - | - | ⭐ 22 | 🔴 january 2024|
| 🔗 [koniwa](https://github.com/koniwa/koniwa) | - | - | ⭐ 57 | 🟡 april 2025|
| 🔗 [JMMLU](https://github.com/nlp-waseda/JMMLU) | - | - | ⭐ 38 | 🟡 october 2025|
| 🔗 [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) | - | - | ⭐ 48 | 🔴 march 2025|
| 🔗 [jqara](https://github.com/hotchpotch/jqara) | - | - | ⭐ 43 | 🟡 september 2025|
| 🔗 [jemhopqa](https://github.com/aiishii/jemhopqa) | - | - | ⭐ 30 | 🟡 april 2025|
| 🔗 [jacred](https://github.com/youmima/jacred) | - | - | ⭐ 7 | 🔴 march 2024|
| 🔗 [jades](https://github.com/naist-nlp/jades) | - | - | ⭐ 0 | 🔴 december 2022|
| 🔗 [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) | - | - | ⭐ 24 | 🔴 december 2023|
| 🔗 [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) | - | - | ⭐ 16 | 🔴 november 2023|
| 🔗 [jacwir](https://github.com/hotchpotch/jacwir) | - | - | ⭐ 8 | 🟡 september 2025|
| 🔗 [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) | - | - | ⭐ 3 | 🔴 november 2024|
| 🔗 [j-unimorph](https://github.com/cl-tohoku/j-unimorph) | - | - | ⭐ 9 | 🟢 january|
| 🔗 [GazeVQA](https://github.com/riken-grp/GazeVQA) | - | - | ⭐ 0 | 🔴 september 2024|
| 🔗 [J-CRe3](https://github.com/riken-grp/J-CRe3) | - | - | ⭐ 9 | 🔴 january 2025|
| 🔗 [jmed-llm](https://github.com/sociocom/jmed-llm) | - | - | ⭐ 56 | 🔴 september 2024|
| 🔗 [lawtext](https://github.com/yamachig/lawtext) | - | - | ⭐ 92 | 🟢 january|
| 🔗 [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) | - | - | ⭐ 15 | 🔴 june 2024|
| 🔗 [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) | - | - | ⭐ 2 | 🔴 september 2018|
| 🔗 [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [JSeM](https://github.com/DaisukeBekki/JSeM) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [niilc-qa](https://github.com/mynlp/niilc-qa) | - | - | ⭐ 18 | 🔴 november 2015|
| 🔗 [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) | - | - | ⭐ 5 | 🔴 september 2023|
| 🔗 [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) | - | - | ⭐ 29 | 🟢 february|
| 🔗 [elaws-history](https://github.com/kissge/elaws-history) | - | - | ⭐ 5 | 🟢 yesterday|
| 🔗 [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) | - | - | ⭐ 18 | 🔴 september 2024|
| 🔗 [hdic](https://github.com/shikeda/hdic) | - | - | ⭐ 40 | 🟢 last wednesday|
| 🔗 [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) | - | - | ⭐ 159 | 🟢 last tuesday|
| 🔗 [kanji-data](https://github.com/mimneko/kanji-data) | - | - | ⭐ 18 | 🟢 february|
| 🔗 [openchj-genji](https://github.com/togiso/openchj-genji) | - | - | ⭐ 2 | 🔴 march 2025|
| 🔗 [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) | - | - | ⭐ 1 | 🟡 may 2025|
| 🔗 [Jamp_sp](https://github.com/ynklab/Jamp_sp) | - | - | ⭐ 0 | 🔴 june 2024|
| 🔗 [jnli-neg](https://github.com/asahi-y/jnli-neg) | - | - | ⭐ 0 | 🟡 december 2025|
| 🔗 [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) | - | - | ⭐ 5 | 🔴 november 2024|
| 🔗 [jalecon](https://github.com/naist-nlp/jalecon) | - | - | ⭐ 5 | 🔴 july 2023|
| 🔗 [multils-japanese](https://github.com/naist-nlp/multils-japanese) | - | - | ⭐ 0 | 🟢 january|
| 🔗 [nwjc](https://github.com/masayu-a/nwjc) | - | - | ⭐ 10 | 🔴 april 2022|
| 🔗 [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) | - | - | ⭐ 199 | 🔴 march 2023|
| 🔗 [gimei](https://github.com/willnet/gimei) | - | - | ⭐ 424 | 🟢 january|
| 🔗 [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) | - | - | ⭐ 9 | 🟡 july 2025|
| 🔗 [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) | - | - | ⭐ 7 | 🟢 march|
| 🔗 [kanji](https://github.com/sylhare/kanji) | - | - | ⭐ 28 | 🟢 march|
| 🔗 [jethics](https://github.com/language-media-lab/jethics) | - | - | ⭐ 2 | 🟡 june 2025|
| 🔗 [waon](https://github.com/llm-jp/waon) | - | - | ⭐ 6 | 🟡 november 2025|
| 🔗 [kuci](https://github.com/ku-nlp/kuci) | - | - | ⭐ 5 | 🔴 february 2024|
| 🔗 [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [jlpt-word-list](https://github.com/elzup/jlpt-word-list) | - | - | ⭐ 62 | 🔴 february 2022|
| 🔗 [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) | - | - | ⭐ 18 | 🔴 april 2020|
| 🔗 [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) | - | - | ⭐ 265 | 🟢 february|
| 🔗 [yjcaptions](https://github.com/yahoojapan/yjcaptions) | - | - | ⭐ 60 | 🔴 november 2016|
| 🔗 [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) | - | - | ⭐ 30 | 🔴 november 2018|
| 🔗 [lawhub](https://github.com/lwhb/lawhub) | - | - | ⭐ 152 | 🔴 november 2020|
| 🔗 [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) | - | - | ⭐ 39 | 🔴 december 2023|
| 🔗 [jconj](https://github.com/yamagoya/jconj) | - | - | ⭐ 35 | 🔴 may 2020|
| 🔗 [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) | - | - | ⭐ 21 | 🔴 december 2022|
| 🔗 [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) | - | - | ⭐ 11 | 🔴 june 2023|
| 🔗 [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) | - | - | ⭐ 5 | 🔴 june 2016|
| 🔗 [ajimee-bench](https://github.com/azookey/ajimee-bench) | - | - | ⭐ 19 | 🔴 january 2025|
| 🔗 [j-spaw](https://github.com/takamichi-lab/j-spaw) | - | - | ⭐ 5 | 🟡 august 2025|
| 🔗 [camera3](https://github.com/cyberagentailab/camera3) | - | - | ⭐ 4 | 🔴 may 2024|
| 🔗 [jgpqa](https://github.com/llm-jp/jgpqa) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) | - | - | ⭐ 2 | 🔴 june 2021|
| 🔗 [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) | - | - | ⭐ 2 | 🔴 september 2024|
| 🔗 [osworld-jp](https://github.com/karakuri-ai/osworld-jp) | - | - | ⭐ 2 | 🟡 november 2025|
| 🔗 [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) | - | - | ⭐ 1 | 🟡 october 2025|
| 🔗 [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) | - | - | ⭐ 1 | 🔴 may 2022|
| 🔗 [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) | - | - | ⭐ 1 | 🔴 march 2021|
| 🔗 [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) | - | - | ⭐ 1 | 🟢 january|
| 🔗 [kotowaza](https://github.com/septn/kotowaza) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [selective-rag-kasensabo](https://github.com/tk-yasuno/selective-rag-kasensabo) | - | - | ⭐ 1 | 🟡 november 2025|
| 🔗 [jmle2026-bench](https://github.com/naoto-iwase/jmle2026-bench) | - | - | ⭐ 10 | 🟢 march|
| 🔗 [JSTS-Neg](https://github.com/reiko-y/JSTS-Neg) | - | - | ⭐ 1 | 🟢 february|
| 🔗 [business-slide-questions](https://github.com/stockmarkteam/business-slide-questions) | - | - | ⭐ 2 | 🟡 may 2025|
| 🔗 [WLSP-antonym](https://github.com/masayu-a/WLSP-antonym) | - | - | ⭐ 0 | 🔴 march 2021|
| 🔗 [YouCook2-JP](https://github.com/nlab-mpg/YouCook2-JP) | - | - | ⭐ 0 | 🟡 august 2025|
| 🔗 [E2U](https://github.com/sociocom/E2U) | - | - | ⭐ 0 | 🟢 march|
| 🔗 [annotation-2025](https://github.com/Tiny-Colony/annotation-2025) | - | - | ⭐ 0 | 🟢 january|
| 🔗 [jhpt](https://github.com/nict-astrec-att/jhpt) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [JBE-QA](https://github.com/hancules/JBE-QA) | - | - | ⭐ 0 | 🟡 november 2025|
| 🔗 [j-spaw](https://github.com/takamichi-lab/j-spaw) | - | - | ⭐ 5 | 🟡 august 2025|
| 🔗 [JMedWiC](https://github.com/EhimeNLP/JMedWiC) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [jhpt](https://github.com/nict-astrec-att/jhpt) | - | - | ⭐ 3 | 🟢 march|
| 🔗 [Doppelganger-JC](https://github.com/0017-alt/Doppelganger-JC) | - | - | ⭐ 1 | 🟢 january|
| 🔗 [modelvista-3lang](https://github.com/kuramitsulab/modelvista-3lang) | - | - | ⭐ 1 | 🟢 last monday|
| 🔗 [japanese-hr-niah](https://github.com/kufu/japanese-hr-niah) | - | - | ⭐ 1 | 🟢 january|


## Tutorial
學習日文自然語言處理工具與技術的教學資源

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
 * [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) - 日本語資訊檢索教學
 * [nlpbook](https://github.com/mamorlis/nlpbook) - 「自然語言處理教科書」支援網站
 * [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) - 製作並學習正規表達式引擎
 * [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) - 【2024年版】BERT進行文本分類
 * [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) - 將Google Gemma微調為日文指令
 * [nlp100v2020](https://github.com/upura/nlp100v2020) - 用Python解决“自然语言处理100道题目2020”
 * [textmining-ja](https://github.com/paithiov909/textmining-ja) - R進行自然語言處理和文本分析的練習
 * [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) - NLP2025年的教程“地理信息和语言处理实践入门”的资料和源代码
 * [nlp100v2025](https://github.com/upura/nlp100v2025) - 用Python解决「自然语言处理100道练习 2025」
 * [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) - 『主題模型』(機器學習專業系列)的筆記
 * [slp2025](https://github.com/ryota-komatsu/slp2025) -音学シンポジウム2025チュートリアル「マルチモーダル大規模言語モデル入門」資料
 * [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) - 印象出版社「IT基礎教養 自然語言處理＆圖像分析」
 * [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) - 書籍「現場中應用的生成AI代理人實踐入門」（講談社科學社）中使用的源代碼
 * [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) - 2024年度 立教大學大學院 人工智能科學研究科 自然語言處理特論
 * [support-genai-book](https://github.com/yoheikikuta/support-genai-book) - 從原論文中揭示的生成人工智慧（技術評論社）的支援頁面。
 * [ir100](https://github.com/ir100/ir100) - 情報檢索100本敲門
 * [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) - 支援網站：《Kaggle 開始大規模語言模型入門 ～自然語言處理〈實踐〉程式設計～》


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) | - | - | ⭐ 64 | 🔴 january 2020|
| 🔗 [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) | - | - | ⭐ 205 | 🔴 september 2016|
| 🔗 [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) | - | - | ⭐ 5 | 🔴 may 2022|
| 🔗 [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) | - | - | ⭐ 5 | 🔴 march 2019|
| 🔗 [ginza-examples](https://github.com/poyo46/ginza-examples) | - | - | ⭐ 15 | 🔴 january 2021|
| 🔗 [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) | - | - | ⭐ 0 | 🟡 august 2025|
| 🔗 [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) | - | - | ⭐ 29 | 🔴 january 2022|
| 🔗 [bert-book](https://github.com/stockmarkteam/bert-book) | - | - | ⭐ 264 | 🔴 february 2024|
| 🔗 [janome-tutorial](https://github.com/mocobeta/janome-tutorial) | - | - | ⭐ 31 | 🔴 march 2019|
| 🔗 [handson-language-models](https://github.com/hnishi/handson-language-models) | - | - | ⭐ 3 | 🔴 march 2021|
| 🔗 [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) | - | - | ⭐ 6 | 🔴 june 2021|
| 🔗 [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) | - | - | ⭐ 143 | 🔴 may 2021|
| 🔗 [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) | - | - | ⭐ 235 | 🔴 may 2024|
| 🔗 [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) | - | - | ⭐ 10 | 🔴 may 2023|
| 🔗 [llm-book](https://github.com/ghmagazine/llm-book) | - | - | ⭐ 467 | 🟡 december 2025|
| 🔗 [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) | - | - | ⭐ 113 | 🔴 april 2024|
| 🔗 [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) | - | - | ⭐ 3 | 🔴 june 2024|
| 🔗 [nlpbook](https://github.com/mamorlis/nlpbook) | - | - | ⭐ 14 | 🟡 april 2025|
| 🔗 [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) | - | - | ⭐ 22 | 🔴 march 2024|
| 🔗 [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) | - | - | ⭐ 30 | 🔴 july 2024|
| 🔗 [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) | - | - | ⭐ repo not found | 🔴 august 2024|
| 🔗 [nlp100v2020](https://github.com/upura/nlp100v2020) | - | - | ⭐ 90 | 🟡 april 2025|
| 🔗 [textmining-ja](https://github.com/paithiov909/textmining-ja) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) | - | - | ⭐ 17 | 🟢 february|
| 🔗 [nlp100v2025](https://github.com/upura/nlp100v2025) | - | - | ⭐ 90 | 🟡 april 2025|
| 🔗 [public-annotations](https://github.com/manga109/public-annotations) | - | - | ⭐ 13 | 🟡 april 2025|
| 🔗 [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) | - | - | ⭐ 4 | 🟡 may 2025|
| 🔗 [slp2025](https://github.com/ryota-komatsu/slp2025) | - | - | ⭐ 63 | 🟢 last tuesday|
| 🔗 [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) | - | - | ⭐ 4 | 🟡 june 2025|
| 🔗 [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) | - | - | ⭐ 193 | 🟡 september 2025|
| 🔗 [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [support-genai-book](https://github.com/yoheikikuta/support-genai-book) | - | - | ⭐ 91 | 🟢 january|
| 🔗 [ir100](https://github.com/ir100/ir100) | - | - | ⭐ 93 | 🟡 december 2025|
| 🔗 [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) | - | - | ⭐ 27 | 🟢 march|


## Research summary
彙整日文自然語言處理相關研究成果與論文的資料

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 一份預先訓練的BERT模型清單，包括日語的單詞/子詞分詞和詞彙構建算法信息。
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 收集和分类有关日语文法错误修正的文献的存储库
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - 文本語料庫列表及更多（主要為日語）
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - 系統地最大化深度學習模型性能的策略手冊
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 嘗試將日語音韻，特別是音高重音資源整合成一個清單。
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - 開源的日本語LLM總結


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) | - | - | ⭐ 131 | 🔴 march 2023|
| 🔗 [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) | - | - | ⭐ 13 | 🟡 april 2025|
| 🔗 [dataset-list](https://github.com/ikegami-yukino/dataset-list) | - | - | ⭐ 118 | 🔴 july 2024|
| 🔗 [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) | - | - | ⭐ 190 | 🔴 january 2023|
| 🔗 [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) | - | - | ⭐ 126 | 🔴 february 2024|
| 🔗 [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) | - | - | ⭐ 1.4k | 🟢 today|


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
