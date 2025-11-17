# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

專用於 Python 庫、預訓練模型、詞典和日語 NLP 語料庫的精選資源列表

- [列出了737個GitHub倉庫的資訊 ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md)
- [列出了2145個Hugging Face倉庫的資訊（模型和數據集） ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) を掲載中
- [發布了一個搜索大量倉庫資訊的工具🔎](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## 🎉 The latest additions

**Python**
 * [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) - 使用OpenReview論文自動發現和分析的日語AI代理程式

_Updated on Nov 18, 2025_

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
 * [wiredify](https://github.com/eggplants/wiredify) - 將日文假名從ba-bi-bu-be-bo轉換為va-vi-vu-ve-vo
將日文假名從ba-bi-bu-be-bo轉換為va-vi-vu-ve-vo
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - 使用MeCab獲取日文讀音（yomigana）和重音的簡單Python套件（CLI/Python API）。
 * [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) - 執行NormalizeNumexp的Python實作，進行數量表達和時間表達的提取和規範化。
 * [Jusho](https://github.com/nagataaaas/Jusho) - 日本郵政編碼數據的簡單封裝
 * [yurenizer](https://github.com/sea-turt1e/yurenizer) - 日文文本正規化工具，解決拼寫不一致。
 * [e2k](https://github.com/Patchethium/e2k) - 一個用於自動將英文轉換為片假名的工具
 * [alkana.py](https://github.com/zomysan/alkana.py) - 一個可以獲取字母串的片假名讀音的工具。
 * [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) - 將英文文字轉換為片假名的程式




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




### Sentiment analysis
分析文字情緒與正負極性的函式庫

 * [oseti](https://github.com/ikegami-yukino/oseti) - 基於詞典的日語情感分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 日本語文書的正負面分類。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日文文本情感分析器
 * [asari](https://github.com/Hironsan/asari) - 使用Python實現的日語情感分析器。




### Machine translation
在不同語言之間自動翻譯文字的函式庫

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawl 預訓練神經機器翻譯 (NMT) 模型的使用示例。
 * [JASS](https://github.com/Mao-KU/JASS) - JASS：針對日本特定序列的序列到序列預訓練，用於神經機器翻譯（LREC2020）和基於語言學的多任務預訓練，用於低資源神經機器翻譯（ACM TALLIP）。
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 一個針對日英機器翻譯韌性的現象級評估數據集。該數據集基於MTNT數據集，並附加了四種語言現象的註釋；專有名詞、縮寫名詞、口語表達和變體。COLING 2020。
 * [VISA](https://github.com/ku-nlp/VISA) - 一個用於視覺場景感知機器翻譯的模糊字幕數據集
 * [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) - 使用本地執行的plamo-2-translate模型進行翻譯的命令行界面。




### Named entity recognition
從文字中擷取人名、地名與組織名的函式庫

 * [namaco](https://github.com/chakki-works/namaco) - 基於字元的命名實體識別。
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypedia是一個從維基百科擴展出來的命名實體詞典。
 * [noyaki](https://github.com/ken11/noyaki) - 將字符跨度標籤信息轉換為基於分詞文本的標籤信息。
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - 用於BERT模型微調的代碼。這是用於創建和使用用於實體識別任務的模型的BERT模型微調示例。
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 從基於詳細註釋標準的病例報告語料庫中進行固有表達和關係抽取精度推論的代碼。
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp，一個用於對日文文本進行地理標記的Python模塊。
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - BERT進行日語固有表現抽取的微調程式
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - 用於日語語言（Hugging Face）資源的調整編碼器和編碼器-解碼器變壓器的示例
用於日語語言（Hugging Face）資源的調整編碼器和編碼器-解碼器變壓器的示例
 * [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) - 透過BERT的微調進行專有名詞提取




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




## C++

### Morphology analysis
高效能的日文形態素分析函式庫

 * [mecab](https://github.com/taku910/mecab) - 又一個日本語形態分析器
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++（一個形態學分析工具包）
 * [kytea](https://github.com/neubig/kytea) - 京都文本分析工具箱，可用於詞語分割和發音估計等。



### Parsing
用於日文語法與依存分析的函式庫

 * [cabocha](https://github.com/taku910/cabocha) - 另一個日本依存結構分析器
 * [knp](https://github.com/ku-nlp/knp) - 一個日語解析器



### Others
其他與日文NLP相關的函式庫

 * [jsc](https://github.com/yohokuno/jsc) - 日文假名漢字轉換、中文拼音輸入和CJE混合輸入的聯合源通道模型。
 * [aquaskk](https://github.com/codefirst/aquaskk) - 沒有形態學分析的輸入法。
 * [mozc](https://github.com/google/mozc) - Mozc - 一款為多平台設計的日本輸入法編輯器
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch：一個（精確|前綴|近似）字串匹配庫
 * [resembla](https://github.com/tuem/resembla) - Resembla：基於單詞的日語相似句子搜索庫
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ Windows 的 SKK-like 日文輸入法編輯器




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




### Converter
用於日文文字與表記轉換的套件

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 檢查和轉換日文字符（平假名、片假名）和羅馬字的實用程式庫
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 一個 Rust 函式庫，可將日文半角ｶﾅ和全角英數轉換為正常字符。
 * [kana](https://github.com/gbrlsnchs/kana) - [鏡像] CLI 程序，可將羅馬字文本轉寫為平假名或片假名。
 * [kanaria](https://github.com/samunohito/kanaria) - 這個程式庫提供了平假名、片假名、半形和全形之間的互相轉換和識別功能。
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - 日本的地址分割成都道府県/市區町村/町名/其他的程式庫
 * [yosina](https://github.com/yosina-lib/yosina) - Yosina 是一個處理日文書寫中使用的字母和符號的音譯庫。




### Search engine library
用於日文全文檢索與索引的函式庫

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy. 

林德拉分詞器用於Tantivy。
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - 使用 Vibrato 的 Tantivy 分詞器。




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




## JavaScript

### Morphology analysis
可於瀏覽器或Node.js進行日文形態素分析的函式庫

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日本語形態素解析器的JavaScript實現
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - Rakuten MA - 一款純粹使用 JavaScript 編寫的中日文形態分析器（詞分割器 + 詞性標記器）。
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - 另一個用於 Node.js 的 MeCab 封裝程式
 * [juman-bin](https://github.com/thammin/juman-bin) - 一個可擴展的日本語形態素解析器。日本語形態素解析系統。
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - 使用MeCab的非同步日語形態分析器。




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




## Go

### Morphology analysis
以Go實作的輕量日文形態素分析函式庫

 * [kagome](https://github.com/ikawaha/kagome) - 純Go編寫的自包含日語形態分析器




### Others
其他以Go為基礎的日文文本處理函式庫

 * [ojosama](https://github.com/jiro4989/ojosama) - 將文字轉換為百滿天原薩洛美小姐風格的口吻。
 * [nihongo](https://github.com/gojp/nihongo) - 日本語詞典
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - Yomichan 的外部詞典導入工具。
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - THE IDOLM@STER 日文輸入法詞彙表（由imas-db.jp提供）
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - 在Go中將漢字音譯為平假名/片假名/羅馬字
將漢字音譯為平假名/片假名/羅馬字，在Go中
 * [go-moji](https://github.com/ktnyt/go-moji) - 一個用於全角/半角轉換的 Go 函式庫
 * [ojichat](https://github.com/greymd/ojichat) - 生成一些看起来像叔叔会通过LINE或邮件发送的文本
 * [name](https://github.com/kuniwak/name) - 日本名稱搜索器




## Java

### Morphology analysis
用於日文形態素分析與辭典管理的函式庫

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromoji是一個自包含且非常易於使用的日語形態分析器，專為搜索而設計。
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - Sudachi詞彙表
 * [meval](https://github.com/teru-oka-1933/meval) - 形態素解析器性能評估系統 MevAL




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
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - 用於在Slack上使用OpenAI的ChatGPT API的Slackbot腳本（假設使用日語）
用於在Slack上使用OpenAI的ChatGPT API的Slackbot腳本（假設使用日語）
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - 這是ChatGPT的提示示例。
ChatGPT的提示示例。
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - 一個使用Python和Langchain構建的日語漢字閃卡應用程序，並搭載了GPT-4的智能增強功能。
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - 評估GPT-4和ChatGPT在日本醫學執照考試上的表現
 * [japagen](https://github.com/retrieva/japagen) - 使用LLM在日語任務中生成虛擬學習數據的研究
  * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - ChatGPT和Copilot等各種生成AI用的“日本語”的Prompt的樣本
ChatGPT和Copilot等各種生成AI用的「日本語」的Prompt的樣本




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
 * [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) - 由azooKey引擎提供支援的fcitx5日文輸入法
由azooKey引擎提供支援的fcitx5日文輸入法
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
 * [en-ja-el](https://github.com/shigashiyama/en-ja-el) - EnJaEL：En-Ja平行實體連結數據集（版本1.0）
EnJaEL：En-Ja平行實體連結數據集（版本1.0）




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
 * [jacwir](https://github.com/hotchpotch/jacwir) - JaCWIR: 日本語休閒網路資訊檢索（Web IR） 日本語情報檢索評估的小型休閒Web標題和摘要資料集
 * [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) - 日本語學習者的科學技術業界常用片假名與原始單字對照表
 * [j-unimorph](https://github.com/cl-tohoku/j-unimorph) - UniMorph的日文數據集
 * [GazeVQA](https://github.com/riken-grp/GazeVQA) - LREC-COLING 2024論文的數據集《針對澄清日語問題的凝視導向視覺問答數據集》
 * [J-CRe3](https://github.com/riken-grp/J-CRe3) - J-CRe3 實驗代碼（上田等人，LREC-COLING，2024）
 * [jmed-llm](https://github.com/sociocom/jmed-llm) - JMED-LLM：大型語言模型的日本醫學評估數據集
 * [lawtext](https://github.com/yamachig/lawtext) - 日本法律的純文本格式
日本法律的純文本格式
 * [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) - OCR處理程式研究開發項目中所建立的OCR學習用數據集。
 * [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) - 話題基礎的語義模糊解決評估集
 * [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) - Jamp：用於評估語言模型泛化能力的受控日語時間推理數據集
 * [JSeM](https://github.com/DaisukeBekki/JSeM) - 日本語意義測試套件（FraCaS對應及擴展）
 * [niilc-qa](https://github.com/mynlp/niilc-qa) - NIILC QA 數據
 * [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) - 請將以下內容翻譯為繁體中文。
日本論文《鏈條思維提示的驗證》的數據集
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
 * [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) - 請將以下內容翻譯成繁體中文。
在AAAI21中介紹的《Towards Fully Automated Manga Translation》論文中介紹的數據集
 * [public-annotations](https://github.com/manga109/public-annotations) - Manga109數據集的各種註釋
 * [gimei](https://github.com/willnet/gimei) - 隨機日本姓名和地址生成器
 * [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) - 評估日語語言模型安全性行為的測試集
 * [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) - 一個簡單的、開源的日語擬聲詞和擬音詞聲音詞彙的JSON格式收集。附帶漫畫示例。
 * [kanji](https://github.com/sylhare/kanji) - 要學習的日本漢字部首列表
 * [jethics](https://github.com/language-media-lab/jethics) - 日本語道徳理解度評価用數據集JETHICS的概述頁面（待更新）




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




## Research summary
彙整日文自然語言處理相關研究成果與論文的資料

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 一份預先訓練的BERT模型清單，包括日語的單詞/子詞分詞和詞彙構建算法信息。
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 收集和分类有关日语文法错误修正的文献的存储库
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - 文本語料庫列表及更多（主要為日語）
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - 系統地最大化深度學習模型性能的策略手冊
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 嘗試將日語音韻，特別是音高重音資源整合成一個清單。
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - 開源的日本語LLM總結




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
