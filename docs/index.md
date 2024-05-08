# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語の自然言語処理に関するPythonライブラリ、学習済みモデル、辞書、およびコーパスの厳選リストです。

[このリスト](https://github.com/taishi-i/awesome-japanese-nlp-resources)には、561件の日本語NLPリポジトリが含まれています。
これらのリポジトリを検索するための[ツール](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)はHugging Face Spacesで利用可能です。
Huggingface に掲載されているモデルは、[こちら](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.md) をご覧ください。

[日本語 NLP 分類データセット](https://huggingface.co/datasets/taishi-i/awesome-japanese-nlp-classification-dataset)を公開しました。


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## The latest additions 🎉

**Python**
 * [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) - Wikipediaの日本語記事を元に、ユーザの質問に回答するGradioベースのRAGのサンプル
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - GPT-4 を用いて、言語モデルの応答を自動評価するスクリプト
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - BERTによる日本語固有表現抽出のファインチューニング用プログラム
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - 日本語T5モデル

**Corpus**
 * [jacwir](https://github.com/hotchpotch/jacwir) - JaCWIR: Japanese Casual Web IR  日本語情報検索評価のための小規模でカジュアルなWebタイトルと概要のデータセット
 * [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) - 日本語学習者のための科学技術業界でよく使われる片仮名と元の単語対照表

**Dictionary**
 * [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) - うちなーぐち辞典（沖縄語辞典）

_Updated on May 09, 2024_

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

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - SudachiPy 0.6以上はSudachi.rsとして開発されています。
 * [Janome](https://github.com/mocobeta/janome) - 純粋なPythonで書かれた日本語形態素解析エンジン
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - mecab-pythonです。mecab-pythonです。オリジナルバージョンはこちらから見つけることができます：http://taku910.github.io/mecab/。
 * [mecab](https://github.com/ikegami-yukino/mecab) - このリポジトリは、Windows 64ビット用のMeCabバイナリのビルドと、MeCab Pythonバインディングの改善に使用されます。
 * [fugashi](https://github.com/polm/fugashi) - 高速でPythonicな日本語トークナイズと形態素解析のためのCython MeCabラッパー。
 * [nagisa](https://github.com/taishi-i/nagisa) - 再帰型ニューラルネットワークに基づく日本語トークナイザー
 * [pyknp](https://github.com/ku-nlp/pyknp) - JUMAN++/KNP用のPythonモジュール
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - KyTeaのPythonラッパー
 * [konoha](https://github.com/himkt/konoha) - Konoha：日本語トークナイザーのシンプルなラッパー
 * [natto-py](https://github.com/buruzaemon/natto-py) - natto-pyは、Pythonプログラミング言語と日本語の品詞や形態素解析器であるMeCabを組み合わせたものです。
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - 楽天MA（Python版）
 * [python-vaporetto](https://github.com/daac-tools/python-vaporetto) - Vaporettoは、高速で軽量なポイントワイズ予測ベースのトークナイザーです。これはVaporettoのPythonラッパーです。
 * [dango](https://github.com/mkartawijaya/dango) - 日本語テキスト用の使いやすいトークナイザー。言語学習者や非言語学者を対象としています。
 * [rhoknp](https://github.com/ku-nlp/rhoknp) - Juman++/KNPのための別のPythonバインディング
 * [python-vibrato](https://github.com/daac-tools/python-vibrato) - Viterbiベースの高速トークナイザー（Pythonラッパー）
 * [jagger-python](https://github.com/lighttransport/jagger-python) - JaggerのPythonバインディング（パターンベースの日本語形態素解析器のC++実装）


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

 * [ginza](https://github.com/megagonlabs/ginza) - ユニバーサル依存関係に基づくspaCyフレームワークを使用した日本語NLPライブラリ
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - もう一つの日本語依存構造解析ツール
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - 現代日本語のためのトークナイザー、POSタガー、レンマ化器、依存構造解析器
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - Camphr - パイプラインコンポーネントを作成するためのNLPライブラリ
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - モダン・コンテンポラリー日本語用のTokenizer、POS-tagger、Lemmatizer、およびDependency-parserには、BERTモデルが使用されます。
 * [depccg](https://github.com/masashi-y/depccg) - スーパータグと依存関係ファクタリングモデルを備えたA* CCGパーサー
 * [bertknp](https://github.com/ku-nlp/bertknp) - BERTに基づく日本語依存構造解析器
 * [esupar](https://github.com/KoichiYasuoka/esupar) - 日本語や他の言語に対応したBERT/RoBERTa/DeBERTaモデルを使用したトークナイザー、POSタガー、依存構造解析器。
 * [yomikata](https://github.com/passaglia/yomikata) - 微調整されたBERTモデルを使用した異音異義語の曖昧性解消ライブラリ。
 * [jdepp-python](https://github.com/lighttransport/jdepp-python) - J.DepPのPythonバインディング（日本語依存構造解析器のC++実装）


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

 * [pykakasi](https://github.com/miurahr/pykakasi) - 日本語の仮名漢字文から仮名ローマ字文に変換する軽量コンバーター。
 * [cutlet](https://github.com/polm/cutlet) - Pythonでの日本語からローマ字への変換ツール
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - 英語アルファベットをカタカナに変換してください。
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - アラビア数字、または「西洋式」の数字を日本の文脈に変換します。
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Python用Mozc：かな漢字変換器
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - ひらがな/カタカナの文字列をモーラ（音節）に分割する日本語テキストパーサー。
 * [text2phoneme](https://github.com/korguchi/text2phoneme) - 日本語文を音素列へ変換するスクリプト
 * [jntajis-python](https://github.com/opencollector/jntajis-python) - 日本国税庁の法人番号システムで定義されたスキームに基づく、高速な文字変換および転写ライブラリ。
 * [wiredify](https://github.com/eggplants/wiredify) - 「ばびぶべぼ」から「ヴァヴィヴヴェヴォ」に変換してください。
 * [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) - MeCabを使用して、日本語の読み仮名とアクセントを取得するためのシンプルなPythonパッケージ（CLI/Python API）。


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

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - mecab-neologd用の日本語テキスト正規化ツール
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - ひらがな、カタカナ、半角、全角のための純粋なPython日本語文字相互変換器
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - 日本語半角と全角の素早い変換ツール
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 日本語のウェブテキスト用の強力なテキストクリーナー
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 複数の前処理を構成して管理するテキスト前処理ツール
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuhoは、日本語の半角カタカナと全角カタカナの間で双方向変換を容易にするPythonモジュールです。
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - もう一つの高速な日本語文字列変換ツール


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

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日本語テキストの文境界曖昧性解消ツール (にほんごぶんきょうかいはんていき)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日本語の文分割器
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 日本語テキストのための別の文レベルのトークナイザー
 * [budoux](https://github.com/google/budoux) - スタンドアロン。小さい。言語に依存しない。BudouXは、機械学習による行の整理ツールであるBudouの後継者です。
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - Python用の日本語文分割ライブラリ
 * [hasami](https://github.com/mkartawijaya/hasami) - 日本語テキストの文分割を実行するツール
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - Rustで書かれたPython用の日本語テキストセグメンター
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日本語文分割ツールの比較


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

 * [oseti](https://github.com/ikegami-yukino/oseti) - 日本語の辞書ベースの感情分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 日本語のネガティブ・ポジティブの分類。日本語の文章のネガティブ・ポジティブを判定します。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日本語テキストの感情分析ツール
 * [asari](https://github.com/Hironsan/asari) - Pythonで実装された日本語感情分析器。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[oseti](https://github.com/ikegami-yukino/oseti)|[![Downloads](https://static.pepy.tech/badge/oseti/week)](https://pepy.tech/project/oseti)|[![Downloads](https://static.pepy.tech/badge/oseti)](https://pepy.tech/project/oseti)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/oseti?style=social)|
|[negapoji](https://github.com/liaoziyang/negapoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/liaoziyang/negapoji?style=social)|
|[pymlask](https://github.com/ikegami-yukino/pymlask)|[![Downloads](https://static.pepy.tech/badge/pymlask/week)](https://pepy.tech/project/pymlask)|[![Downloads](https://static.pepy.tech/badge/pymlask)](https://pepy.tech/project/pymlask)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/pymlask?style=social)|
|[asari](https://github.com/Hironsan/asari)|[![Downloads](https://static.pepy.tech/badge/asari/week)](https://pepy.tech/project/asari)|[![Downloads](https://static.pepy.tech/badge/asari)](https://pepy.tech/project/asari)|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/asari?style=social)|


### Machine translation

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawlの事前学習済みニューラル機械翻訳（NMT）モデルの使用例。
 * [JASS](https://github.com/Mao-KU/JASS) - JASS：ニューラル機械翻訳のための日本語固有のシーケンス・トゥ・シーケンス事前学習（LREC2020）＆言語学的に駆動された低リソースニューラル機械翻訳のためのマルチタスク事前学習（ACM TALLIP）
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 日英機械翻訳の堅牢性に関する現象別評価データセット。このデータセットは、MTNTデータセットをベースに、固有名詞、略語、口語表現、および変異形の4つの言語現象の追加注釈を含んでいます。COLING 2020。
 * [VISA](https://github.com/ku-nlp/VISA) - 視覚シーンに関する機械翻訳のための曖昧な字幕データセット


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MorinoseiMorizo/jparacrawl-finetune?style=social)|
|[JASS](https://github.com/Mao-KU/JASS)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Mao-KU/JASS?style=social)|
|[PheMT](https://github.com/cl-tohoku/PheMT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/PheMT?style=social)|
|[VISA](https://github.com/ku-nlp/VISA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/VISA?style=social)|


### Named entity recognition

 * [namaco](https://github.com/chakki-works/namaco) - 文字ベースの固有表現認識。
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypediaは、Wikipediaからの拡張された固有名詞辞書です。
 * [noyaki](https://github.com/ken11/noyaki) - 文字の範囲ラベル情報をトークン化されたテキストベースのラベル情報に変換します。
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - Code to perform finetuning of the BERT model. BERTモデルのファインチューニングで固有表現抽出用タスクのモデルを作成・使用するサンプルです
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 詳細なアノテーション基準に基づく症例報告コーパスからの固有表現及び関係の抽出精度の推論を行うコード
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlpは、日本語テキストのジオタギングに使用するPythonモジュールです。
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - BERTによる日本語固有表現抽出のファインチューニング用プログラム


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namaco](https://github.com/chakki-works/namaco)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/namaco?style=social)|
|[entitypedia](https://github.com/chakki-works/entitypedia)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/entitypedia?style=social)|
|[noyaki](https://github.com/ken11/noyaki)|[![Downloads](https://static.pepy.tech/badge/noyaki/week)](https://pepy.tech/project/noyaki)|[![Downloads](https://static.pepy.tech/badge/noyaki)](https://pepy.tech/project/noyaki)|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/noyaki?style=social)|
|[bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/bert-japanese-ner-finetuning?style=social)|
|[joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aih-uth/joint-information-extraction-hs?style=social)|
|[pygeonlp](https://github.com/geonlp-platform/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp/week)](https://pepy.tech/project/pygeonlp)|[![Downloads](https://pepy.tech/badge/pygeonlp)](https://pepy.tech/project/pygeonlp)|![GitHub Repo stars](https://img.shields.io/github/stars/geonlp-platform/pygeonlp?style=social)|
|[bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jurabiinc/bert-ner-japanese?style=social)|


### OCR

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - 日本語のマンガを中心に、光学文字認識についての説明。
 * [mokuro](https://github.com/kha-white/mokuro) - ブラウザ内で選択可能なテキストで日本のマンガを読む。
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - インテルのOpenVINOツールキットを使用して、タッチパネルを使って入力テキストを描画する手書き日本語OCRデモ
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - Japanese OCR
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - NDLOCRのアプリケーション
 * [donut](https://github.com/clovaai/donut) - OCRフリー文書理解トランスフォーマー（Donut）および合成文書ジェネレーター（SynthDoG）の公式実装、ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - マンガ翻訳者 - URLから日本のマンガを取得してマンガ画像を翻訳する
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - 現代日本の雑誌を認識するOCRシステム
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - NDLOCR用テキスト認識モジュール
 * [Poricom](https://github.com/blueaxis/Poricom) - 漫画画像の光学文字認識。漫画OCRデスクトップアプリケーション。


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

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE：日本語一般言語理解評価
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - spacy-transformersでカスタムトークナイザーを使用する
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - T5による会話生成
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - MLP、CNN、RNN、BERTアプローチを含む様々なDNNテキスト分類器を調査する。
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - FastAPIとBERTを使用して感情分析サーバーを展開する
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - 日本語とベトナム語のためのマスクされた言語モデルに基づくスコアリング
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - ShibaのためのAllenNLP統合：日本のCANINEモデル
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - 日本語の類似度データセットで事前学習された日本語word2vecモデルを評価するスクリプト
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - 日本語のBERTベースのGECタグ付け
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - 日本語-BPEエンコーダー
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - 日本語-BPEエンコーダー バージョン2
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - 日本語文法誤り訂正ツール
 * [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) - 日本語ステーブル拡散は、任意のテキスト入力に対して写真のようなリアルな画像を生成することができる、日本特有の潜在的なテキストから画像への拡散モデルです。
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - nagisa用のBERTモデル
 * [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) - トレーニング済みのプレフィックスを使用したGPT/GPT-NeoXモデルのプレフィックスチューニングの例コードと推論のためのコード。
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - JGLUEのトレーニングと評価スクリプト、日本語理解ベンチマーク用
 * [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) - トランスフォーマーライブラリの日本語トークナイザー
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP言語モデル評価ハーネス
 * [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) - 異なるトークナイザーは、スクリプト連続言語における下流タスクでどのように機能するか？：日本語のケーススタディ - ACL SRW 2023
 * [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) - 自己回帰言語モデルの少数ショット評価のためのフレームワーク。
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classification
llm-lora-分類
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP言語モデル評価ハーネス
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - このリポジトリには、"rinna/japanese-gpt-neox..." [gpt-neox] モデルをggmlに変換した場合に、Alpaca-LoraアダプターをLoRAチューニングに適応させるために修正されたスクリプトとマージスクリプトが含まれています。
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - このリポジトリは日本語LLMのキャラクターロールプレイに関する性能を評価するために作成しました。
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - このリポジトリは、YuzuAIのラクダリーダーボードをサポートしています。ラクダリーダーボードは、LMSYSのビクーナ評価の日本に特化した類似物です。
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - このツールは、複数のデータセットを横断して日本語の大規模言語モデルを自動評価するものです．
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - このリポジトリには、LLM-jpモデルの教師ありファインチューニングのためのコードが含まれています。
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - LLM勉強会（LLM-jp）で開発しているLLM用のトークナイザー関連をまとめたリポジトリです．
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - 日本語言語モデルの金融評価ハーネス
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - 日本のビクーニャQAベンチマーク


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

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - 日本のフルネームを姓と名に分けるためのツール。
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - 日本語の自然言語処理のPythonライブラリに特化したリソースの厳選リスト
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - python版日本語意味役割付与システム（ASA）
 * [toiro](https://github.com/taishi-i/toiro) - 日本語トークナイザーの比較ツール
 * [ja-timex](https://github.com/yagays/ja-timex) - 自然言語で書かれた時間情報表現を抽出/規格化するルールベースの解析器
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - テキストデータからの特徴選択のためのメトリックのセット
 * [daaja](https://github.com/kajyuuen/daaja) - このリポジトリには、日本語のNLPのためのデータ拡張の実装が含まれています。
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - このリポジトリの目的は、私がウェブサイトで書いた概念実証（PoC）および研究開発（R＆D）の文脈でプロトタイプをケーススタディとして作成することです。主な研究トピックは、表現学習に関連するオートエンコーダー、エネルギーベースモデルの統計的機械学習、敵対的生成ネットワークなどです...
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - 京都コーパス、KWDLC、および注釈付きFKCコーパス用のプロセッサー
 * [nlplot](https://github.com/takapy0210/nlplot) - 自然言語処理の可視化モジュール
 * [rake-ja](https://github.com/kanjirz50/rake-ja) - 日本語の高速自動キーワード抽出アルゴリズム
 * [jel](https://github.com/izuna385/jel) - 日本語エンティティリンカー。
 * [MedNER-J](https://github.com/sociocom/MedNER-J) - 最新版のMedEX/J（日本語疾患名抽出ツール）
 * [zunda-python](https://github.com/ikegami-yukino/zunda-python) - Python用の日本語強調モダリティ解析クライアント「Zunda」。
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/ を入力してください。
 * [showcase](https://github.com/cl-tohoku/showcase) - Matsubayashi＆Inui（2018）の論文で紹介された日本語述語引数構造（PAS）解析器のPyTorch実装にいくつかの改良を加えました。
 * [darts-clone-python](https://github.com/rixwew/darts-clone-python) - ダーツクローンのPythonバインディング
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - 日本の現実的なテキスト推論コーパスの例コード
 * [desuwa](https://github.com/megagonlabs/desuwa) - KNPルールファイルに基づく形態素とフレーズの特徴注釈ツール（純粋なPython）
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - 日本語による対話を通じたレストラン検索システム。
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - 日本語の自然言語処理のサンプルコード
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - Pythonで日本語テキストを扱うための小さなサンプルスクリプト
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - DNormの日本語版
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - EventGraphは、日本語の高度なNLPアプリケーションの開発プラットフォームです。
 * [ishi](https://github.com/ku-nlp/ishi) - 石：日本語の意志分類器
 * [python-npylm](https://github.com/musyoku/python-npylm) - ベイズ階層言語モデルによる教師なし形態素解析
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - 条件付確率場とベイズ階層言語モデルの統合による半教師あり形態素解析
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - 教師なし品詞タグ推定
 * [negima](https://github.com/cocodrips/negima) - Negimaは、定義した品詞ベースのルールを使用して、日本語テキストからフレーズを抽出するためのPythonパッケージです。
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - BertSumを要約モデルとして使用する抽出型要約器
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - 自然言語での日本語数字（漢字、アラビア数字）のパーサー。
 * [kantan](https://github.com/itayperl/kantan) - 部首のパターンで日本語の単語を検索する
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - 日本語の会話コーパスを取得する。
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - 日本語記事の要約ツール。
 * [chirptext](https://github.com/letuananh/chirptext) - ChirpTextはPythonのテキスト処理ツールのコレクションです。
 * [yubin](https://github.com/alvations/yubin) - 日本の住所マンガー
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - 日本語ウィキペディアクリーナー
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - 日本語を音素に変換するためのPythonライブラリ。
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - このリポジトリには、「感情に基づくテキスト分類のための日本語トークナイザーの実験的評価」に関連するコードが含まれています。
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - 約について
This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - 青空文庫からプレーンテキストまたはトークン化されたテキストファイルを生成します。
 * [JLM](https://github.com/jiali-ms/JLM) - 日本語や中国語のような大語彙言語に対応した高速なLSTM言語モデル
 * [NTM](https://github.com/m3yrin/NTM) - 日本語記事のニューラルトピックモデリングのテスト
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - これは、機械学習とディープラーニングの用語に関する英日語辞典です。
 * [text-generation](https://github.com/discus0434/text-generation) - あなた自身のテキストでGPT-2-JAを微調整し、文章を生成し、自動的にツイートするための使いやすいスクリプト。
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - Chainer上のニューラル画像キャプション（NIC）、英語と日本語の画像キャプションデータセットの事前学習済みモデル。
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - 「UnihanLM：Unihanデータベースを用いた粗-細分割の中国語-日本語言語モデル事前学習」の公式リポジトリ、AACL-IJCNLP 2020
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - mBARTモデルのファインチューニングを実行するためのコード。
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - jtubespeech上のxvectorモデル
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - TinySegmenter用の学習モデルを自作するためのツール．
 * [Grongish](https://github.com/shogo82148/Grongish) - 日本語とグロンギ語の相互変換スクリプト
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - WordCloudでの日本語文章をMecab（形態素解析エンジン）を使用せずに形態素解析チックな表示を実現するスクリプト
 * [snark](https://github.com/hiraokusky/snark) - 日本語ワードネットを利用したDBアクセスライブラリ
 * [toEmoji](https://github.com/mkan0141/toEmoji) - 日本語文を絵文字だけの文に変換するなにか
 * [termextract](https://github.com/kanjirz50/termextract) - - 専門用語抽出アルゴリズムの実装の練習
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - Japanese-Dialog-Transformerの応答候補に対して、KenLMによるN-gram言語モデルでスコアリングし、フィルタリング若しくはリランキングを行う。
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - Pythonにおける混合ユニグラムモデルと無限混合ユニグラムモデルの組み合わせ。
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - Pythonにおける隠れマルコフモデル（HMM）と無限隠れマルコフモデル（iHMM）。
 * [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) - PythonにおけるNグラム言語モデル。
 * [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) - 自動音声認識は、Zakuro AIのサポートを受けたpytorchのdeepspeech2モデルを使用しています。
 * [neural_ime](https://github.com/yohokuno/neural_ime) - ニューラルIME：ニューラル入力方式エンジン
 * [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) - ニューラルネットワークはローマ字を正しく日本語に転写できますか？
 * [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) - 日本語用のトークナイザーが指定されました。
 * [AugLy-jp](https://github.com/chck/AugLy-jp) - AugLyにおける日本語テキストのデータ拡張
 * [furigana4epub](https://github.com/Mumumu4/furigana4epub) - MecabとUnidicを使用して日本語のepub書籍にフリガナを追加するためのPythonスクリプト。
 * [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) - 日本語の動詞/形容詞の活用ツール
 * [jageocoder](https://github.com/t-sagara/jageocoder) - 純粋なPythonの日本の住所ジオコーダー
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlpは、日本語テキストのジオタギングに使用するPythonモジュールです。
 * [nksnd](https://github.com/yoriyuki/nksnd) - 新しいかな漢字変換エンジン
 * [JaMIE](https://github.com/racerandom/JaMIE) - 日本語医療情報抽出ツールキット
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - fasttextとword2vecの比較と、実行スクリプト、学習スクリプトです
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - 最小のサーチエンジン/PageRank/tf-idf
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - 5chの過去ログをスクレイピングして、過去流行った単語(ex, 香具師, orz)などを追跡調査
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - Twitter日本語評判分析データセットのためのツイートダウンローダ
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - Juman++とConceptNet5.5に基づいて日本語の単語を集約する。
 * [jinf](https://github.com/hkiyomaru/jinf) - 日本語活用変換ツール
 * [kwja](https://github.com/ku-nlp/kwja) - 日本語の統一された言語解析器
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - マスクされた言語モデルスコアリングに基づく再現パッケージ（ACL2020）。
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - [PyTorch] 日本語のClipCap
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - [PyTorch] 日本語のための Show, Attend and Tell
 * [cihai](https://github.com/cihai/cihai) - CJK（中国語、日本語、韓国語）言語辞書のためのPythonライブラリ
 * [marine](https://github.com/6gsn/marine) - MARINE：マルチタスク学習に基づく日本語アクセント推定
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - Whisper ASRモデルの微調整
 * [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) - BERTとTransformerのデコーダーを使用した日本語チャットボットのPyTorch実装
 * [radicalchar](https://github.com/yamamaya/radicalchar) - 部首文字正規化ライブラリ
 * [akaza](https://github.com/tokuhirom/akaza) - IBus/Linux用のもう一つの日本語IME
 * [posuto](https://github.com/polm/posuto) - 日本の郵便番号データ。
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - 日本語のTacotron2の実装
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - ひらがなIME for IBus
 * [furiganapad](https://github.com/esrille/furiganapad) - ふりがなパッド
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - 日本語類語辞書
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - Mecab + NEologd + Docker + Python3 の入力となります。
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - 日本語埋め込み評価
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPTがYouTuberをやります
 * [shuwa](https://github.com/google/shuwa) - 入力方法のためにGNOMEオンスクリーンキーボードを拡張する
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - このリポジトリは、日本語NLIモデルのコードを提供しており、ファインチューニングされたマスク言語モデルです。
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - FuguMTを使用した日本語-英語翻訳および英語-日本語翻訳のためのツール。
 * [fugumt](https://github.com/s-taka/fugumt) - ぷるーふおぶこんせぷと で公開した機械翻訳エンジンを利用する翻訳環境です。 フォームに入力された文字列の翻訳、PDFの翻訳が可能です。
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - JaSPICE：画像キャプショニングモデルの述語引数構造を使用した自動評価メトリック
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - 日本語ローカライゼーション
 * [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) - OpenJTalkのPythonラッパー
 * [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) - 電子書籍に漢字の読み方を追加することで、日本語の学習をより簡単にすることができます。
 * [N46Whisper](https://github.com/Ayanaminn/N46Whisper) - ささやきベースの日本語字幕生成ツール
 * [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) - Rinna-3.6B、OpenCALM等の日本語対応LLM(大規模言語モデル)用の簡易Webインタフェースです
 * [pdf-translator](https://github.com/discus0434/pdf-translator) - pdf-translatorは、英語のPDFファイルを日本語に翻訳し、元のレイアウトを保持します。
 * [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) - Haystack + Elasticsearch + wikipedia(ja) を用いた、日本語の質問応答システムのサンプル
ヘイスタック + エラスティックサーチ + Wikipedia(ja) を使用した、日本語の質問応答システムのサンプル
 * [mozc-devices](https://github.com/google/mozc-devices) - 自動的にcode.google.com/p/mozc-morseからエクスポートされました。
 * [natsume](https://github.com/faruzan0820/natsume) - 日本語テキストフロントエンド処理ツールキット
 * [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) - 日本語TTS（VITS）の学習と音声合成のGradio WebUI
 * [ja-law-parser](https://github.com/takuyaa/ja-law-parser) - 日本の法律パーサー
 * [dictation-kit](https://github.com/julius-speech/dictation-kit) - Juliusを使用した日本語音声認識キット
 * [julius4seg](https://github.com/Hiroshiba/julius4seg) - Juliusを使ったセグメンテーション支援ツール
 * [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXの音声合成エンジン
 * [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) - LLaVA-JPは、LLaVAメソッドで訓練された日本のVLMです。
 * [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) - 日本の低資源設定での日本語LLM用のオープンソースRAGとLlama Index
 * [bertjsc](https://github.com/er-ri/bertjsc) - BERTを使用した日本語スペルエラー修正ツール
 * [llm-leaderboard](https://github.com/wandb/llm-leaderboard) - 日本のタスクのLLM評価プロジェクト
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - JGLUEのトレーニングと評価スクリプトについて、日本語理解のベンチマークに関して
JGLUEは、日本語理解のベンチマークのためのトレーニングと評価スクリプトについての情報です。
Training and evaluation scripts for JGLUE, a Japanese language understanding benchmark
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - 日本のデータセットで事前学習されたモデルを使用して、LAVISのBLIP2 Q-formerを修正します。
LAVISのBLIP2 Q-formerを日本のデータセットで事前学習されたモデルを用いて修正します。
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - wikipedia 日本語の文を、各種日本語の embeddings や faiss index へと変換するスクリプト等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - 日本語のSimCSEを探索中
 * [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) - Wikipediaの日本語記事を元に、ユーザの質問に回答するGradioベースのRAGのサンプル
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - GPT-4 を用いて、言語モデルの応答を自動評価するスクリプト
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - 日本語T5モデル


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
|[wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/lawofcycles/wikipedia-japanese-open-rag?style=social)|
|[gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/northern-system-service/gpt4-autoeval?style=social)|
|[t5-japanese](https://github.com/sonoisa/t5-japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/sonoisa/t5-japanese?style=social)|


## C++

### Morphology analysis

 * [mecab](https://github.com/taku910/mecab) - もう一つの日本語形態素解析器
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++（形態素解析ツールキット）
 * [kytea](https://github.com/neubig/kytea) - 京都テキスト分析ツールキット：単語分割や発音推定などに使用されます。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab](https://github.com/taku910/mecab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/mecab?style=social)|
|[jumanpp](https://github.com/ku-nlp/jumanpp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/jumanpp?style=social)|
|[kytea](https://github.com/neubig/kytea)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neubig/kytea?style=social)|

### Parsing

 * [cabocha](https://github.com/taku910/cabocha) - もう一つの日本語依存構造解析ツール
 * [knp](https://github.com/ku-nlp/knp) - 日本語パーサー


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[cabocha](https://github.com/taku910/cabocha)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/cabocha?style=social)|
|[knp](https://github.com/ku-nlp/knp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/knp?style=social)|

### Others

 * [jsc](https://github.com/yohokuno/jsc) - 日本語の仮名漢字変換、中国語のピンイン入力、CJE混合入力のための共通ソースチャネルモデル。
 * [aquaskk](https://github.com/codefirst/aquaskk) - 形態素解析を行わない入力方法。
 * [mozc](https://github.com/google/mozc) - Mozc - マルチプラットフォームに対応した日本語入力システムエディター
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch：（完全|接頭辞|近似）文字列マッチングライブラリ
 * [resembla](https://github.com/tuem/resembla) - Resembla：単語ベースの日本語類似文検索ライブラリ
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ Windows用のSKK風日本語入力エディタ


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

 * [lindera](https://github.com/lindera-morphology/lindera) - 形態素解析ライブラリ。
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto：非常に加速されたポイントワイズ予測に基づくトークナイザー
 * [goya](https://github.com/Leko/goya) - Rustで書かれた日本語形態素解析
 * [vibrato](https://github.com/daac-tools/vibrato) - バイブラート：Viterbiベースの高速トークナイザー
 * [yoin](https://github.com/agatan/yoin) - 純粋なRustで書かれた日本語形態素解析器
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 「mecab」の安全なRustバインディング。品詞と形態素解析ライブラリ。
 * [awabi](https://github.com/nakagami/awabi) - MeCab辞書を使用する形態素解析器


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

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 日本語の文字（ひらがな、カタカナ）とローマ字の間の変換とチェックを行うためのユーティリティライブラリ。
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 日本語の半角カナと全角英数字を通常の文字に変換するためのRustライブラリ
 * [kana](https://github.com/gbrlsnchs/kana) - [ミラー] ローマ字テキストをひらがなまたはカタカナに変換するためのCLIプログラム


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[wana_kana_rust](https://github.com/PSeitz/wana_kana_rust)|-|![Crates.io](https://img.shields.io/crates/d/wana_kana)|![GitHub Repo stars](https://img.shields.io/github/stars/PSeitz/wana_kana_rust?style=social)|
|[unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs)|-|![Crates.io](https://img.shields.io/crates/d/unicode-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/gemmarx/unicode-jp-rs?style=social)|
|[kana](https://github.com/gbrlsnchs/kana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gbrlsnchs/kana?style=social)|


### Search engine library

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Tantivy用のLinderaトークナイザー。
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - Vibratoを使用したTantivyトークナイザー。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy)|-|![Crates.io](https://img.shields.io/crates/d/lindera-tantivy)|![GitHub Repo stars](https://img.shields.io/github/stars/lindera-morphology/lindera-tantivy?style=social)|
|[tantivy-vibrato](https://github.com/akr4/tantivy-vibrato)|-|![Crates.io](https://img.shields.io/crates/d/tantivy-vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/akr4/tantivy-vibrato?style=social)|


### Others

 * [daachorse](https://github.com/daac-tools/daachorse) - Rustでコンパクトなダブル配列データ構造を使用したAho-Corasickアルゴリズムの高速実装。
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - 効率的な時間とメモリを使って、類似したドキュメントのすべてのペアを見つける。
 * [crawdad](https://github.com/daac-tools/crawdad) - 文字単位のダブル配列トライを使用した自然言語辞書のRustライブラリ。
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) - 様々なトークナイザーの比較コード
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - ここでは、文字列マッチングのデータ構造のパフォーマンスを比較するためのベンチマークツールが提供されています。
 * [vime](https://github.com/algon-320/vime) - X11アプリケーションの入力方法としてVimを使用する
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXのコア
 * [akaza](https://github.com/akaza-im/akaza) - IBus/Linux用のもう1つの日本語IME
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - 無料でオンラインで自己ホスト可能な、多言語対応の日本語辞書。
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - Google日本語入力用のDvorakJPローマ字テーブル
 * [niinii](https://github.com/Netdex/niinii) - 一覧を使用したテキストの補助読みのための日本語の注釈者
 * [cskk](https://github.com/naokiri/cskk) - 出力: SKK（シンプルかな漢字変換）ライブラリ
 * [japanki](https://github.com/tysonwu/japanki) - CLIでクイズをすることで日本語の単語を学びましょう！ 🇯🇵
 * [jpreprocess](https://github.com/jpreprocess/jpreprocess) - テキスト読み上げアプリケーション用の日本語テキストプリプロセッサ（Rust言語でのOpenJTalkの書き直し）


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

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日本語形態素解析器のJavaScript実装
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - 日本語と中国語の形態素解析器（単語分割器+品詞タガー）である「楽天MA」は、純粋にJavaScriptで書かれています。
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - Nodejs用の別のmecabラッパー
 * [juman-bin](https://github.com/thammin/juman-bin) - 日本語形態素解析システムのユーザー拡張可能な解析器。
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - MeCabを使用した非同期日本語形態素解析器。


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji.js](https://github.com/takuyaa/kuromoji.js)|![npm](https://img.shields.io/npm/dw/kuromoji)|![npm](https://img.shields.io/npm/dt/kuromoji)|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/kuromoji.js?style=social)|
|[rakutenma](https://github.com/rakuten-nlp/rakutenma)|![npm](https://img.shields.io/npm/dw/rakutenma)|![npm](https://img.shields.io/npm/dt/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/rakuten-nlp/rakutenma?style=social)|
|[node-mecab-ya](https://github.com/golbin/mecab-ya)|![npm](https://img.shields.io/npm/dw/mecab-ya)|![npm](https://img.shields.io/npm/dt/mecab-ya)|![GitHub Repo stars](https://img.shields.io/github/stars/golbin/node-mecab-ya?style=social)|
|[juman-bin](https://github.com/thammin/juman-bin)|![npm](https://img.shields.io/npm/dw/juman-bin)|![npm](https://img.shields.io/npm/dt/juman-bin)|![GitHub Repo stars](https://img.shields.io/github/stars/thammin/juman-bin?style=social)|
|[node-mecab-async](https://github.com/hecomi/node-mecab-async)|![npm](https://img.shields.io/npm/dw/mecab-async)|![npm](https://img.shields.io/npm/dt/mecab-async)|![GitHub Repo stars](https://img.shields.io/github/stars/hecomi/node-mecab-async?style=social)|


### Converter

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - ふりがなと送り仮名モードに対応した、日本語の文章をひらがな、カタカナ、ローマ字に変換するための日本語言語ライブラリ。
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - 黒白のためのKuromoji形態素解析器。
 * [hepburn](https://github.com/lovell/hepburn) - ヘボン式ローマ字による、日本語のひらがなとカタカナを相互に変換するためのNode.jsモジュール
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - 日本の数字を数字に変換します。
 * [jslingua](https://github.com/kariminf/jslingua) - テキストを処理するためのJavascriptライブラリ：アラビア語、日本語など。
 * [WanaKana](https://github.com/WaniKani/WanaKana) - ひらがな<-->カタカナ<-->ローマ字の検出と転写のためのJavascriptライブラリ
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - ローマ字表記の日本人名における一般的な問題を正規化し修正する。
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - 日本語のテキストを古風にするためのユーティリティコレクション
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - オープンソースの住所正規化ライブラリ。


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

 * [bangumi-data](https://github.com/bangumi-data/bangumi-data) - 日本のアニメの生データ
 * [yomichan](https://github.com/FooSoft/yomichan) - ChromeとFirefox用の日本語ポップアップ辞書拡張機能。
 * [proofreading-tool](https://github.com/gecko655/proofreading-tool) - テキストリントツールのGUIツール
 * [kanjigrid](https://github.com/minosvasilias/kanjigrid) - 「Remembering the Kanji」第6版で教えられる2200の漢字を表示するウェブアプリ。
 * [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) - 漢字、ふりがな、日本語DBなどのためのモノレポ
 * [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) - 文の敬体(ですます調)、常体(である調)を解析するJavaScriptライブラリ
 * [hatsuon](https://github.com/DJTB/hatsuon) - 日本語のアクセントユーティリティ
 * [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) - 日本語の感情分析。JavaScriptでsentiment_ja。
 * [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) - mecab-ipadicのシード辞書リーダー
 * [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) - 毎日違う日本語の単語。
 * [oskim](https://github.com/esrille/oskim) - 入力方法のためにGNOMEオンスクリーンキーボードを拡張する
 * [tweetMapping](https://github.com/wtnv-lab/tweetMapping) - 東日本大震災発生から24時間以内につぶやかれたジオタグ付きツイートのデジタルアーカイブです。
 * [pitch-accent](https://github.com/shirakaba/pitch-accent) - 日本語のアクセントを予測する
 * [kana2ipa](https://github.com/amanoese/kana2ipa) - 「ひらがな」または「カタカナ」を日本語で発音する際の音声記号(IPA)に変換するコマンド
 * [voicevox](https://github.com/VOICEVOX/voicevox) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXのエディター


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

 * [kagome](https://github.com/ikawaha/kagome) - 純粋なGoで書かれた自己完結型の日本語形態素解析器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kagome](https://github.com/ikawaha/kagome)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikawaha/kagome?style=social)|


### Others

 * [ojosama](https://github.com/jiro4989/ojosama) - テキストを壱百満天原サロメお嬢様風の口調に変換します
 * [nihongo](https://github.com/gojp/nihongo) - 日本語辞書
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - Yomichan用の外部辞書インポーター。
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - アイドルマスターの言葉辞書（imas-db.jpによる日本語IME用）
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - Goで漢字の読み仮名/片仮名/ローマ字に変換
 * [go-moji](https://github.com/ktnyt/go-moji) - 全角/半角変換のためのGoライブラリ
 * [ojichat](https://github.com/greymd/ojichat) - おじさんがLINEやメールで送ってきそうな文を生成する


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

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromojiは、検索用に設計された自己完結型で非常に使いやすい日本語形態素解析器です。
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - すだちの語彙集


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji](https://github.com/atilika/kuromoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/atilika/kuromoji?style=social)|
|[Sudachi](https://github.com/WorksApplications/Sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/Sudachi?style=social)|
|[SudachiDict](https://github.com/WorksApplications/SudachiDict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiDict?style=social)|


### Others

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 画像から日本語文字を識別するためのJavaライブラリ
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 日本語の漢字をローマ字（ラテンアルファベット）に変換するためのJavaライブラリとコマンドラインツール。
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Javaにおける漢字のひらがな/カタカナ/ローマ字への転写
 * [Kamite](https://github.com/fauu/Kamite) - 日本語学習者のためのデスクトップ言語浸透コンパニオン
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - React Native用の非同期日本語トークナイザーネイティブプラグイン（iOSおよびAndroid用）
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本語アナライザーは、ElasticSearch用にkuromoji日本語トークナイザーを使用しています。
 * [moji4j](https://github.com/andree-surya/moji4j) - 日本語のひらがな、カタカナ、ローマ字のスクリプト間を変換するためのJavaライブラリ。
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - mecab-neologd用の日本語テキスト正規化ツール
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - Elasticsearchのための日本語解析プラグイン


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

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - GensimとMecabを使用した日本語のWord2vec（単語からベクトルへのアプローチ）手法。
 * [chiVe](https://github.com/WorksApplications/chiVe) - SudachiとNWJCを使用した日本語の単語埋め込み。
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - エルモ-日本語
 * [embedrank](https://github.com/yagays/embedrank) - EmbedRankのPython実装
 * [aovec](https://github.com/eggplants/aovec) - 簡単な青空文庫のWord2Vecビルダー - 青空文庫の全書籍を対象としたWord2Vecモデルの構築と構築済みモデル
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - これはAI LABの記事「係り受けに基づく日本語単語埋込 (Dependency-based Japanese Word Embeddings)」のリポジトリです。（記事URL https://ai-lab.lapras.com/nlp/japanese-word-embedding/）
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - もう一つの日本語ウィキペディアエンティティベクトル
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 最新の日本語Wikipediaのダンプデータから，MeCabを用いてIPA辞書と最新のNeologd辞書の両方で形態素解析を実施し，その結果に基づいた word2vec，fastText，GloVeの単語分散表現を学習するためのスクリプト


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

 * [bert-japanese](https://github.com/cl-tohoku/bert-japanese) - 日本語テキスト用のBERTモデル。
 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - りんな株式会社が提供する日本語事前学習モデルのコードを入力してください。
 * [bert-japanese](https://github.com/yoheikikuta/bert-japanese) - 日本語テキスト用のSentencePieceを使用したBERT。
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - トランスフォーマー用の日本語トークナイザー
 * [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) - NTT株式会社が提供する日本語事前学習モデルの評価コード。
 * [shiba](https://github.com/octanove/shiba) - CANINE、効率的な文字レベルトランスフォーマーのPytorch実装と事前学習済みの日本語モデル。
 * [Dialog](https://github.com/reppy4620/Dialog) - BERTとTransformerのデコーダーを使用した日本語チャットボットのPyTorch実装
 * [language-pretraining](https://github.com/retarfi/language-pretraining) - 日本語テキストのPyTorch実装のBERTおよびELECTRAモデル。
 * [medbertjp](https://github.com/ou-medinfo/medbertjp) - 日本語の医療分野における事前学習済みBERTモデルの試験。
 * [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) - ILYS青葉チャットボット
 * [t5-japanese](https://github.com/megagonlabs/t5-japanese) - 日本語T5モデルの事前学習のためのコード
 * [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) - PytorchでBERTの日本語学習済みモデルを利用する
 * [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) - ラボロBERT日本語：Webコーパスで事前学習された日本語BERT
 * [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) - 日本語BERT事前学習モデル
 * [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) - 日本語用のaMLPトランスフォーマーモデル
 * [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) - 青空文庫とウィキペディアでトレーニングされた日本語BERTで、UniDicとSudachiPyでプリトークナイズされました。
 * [sbert-ja](https://github.com/colorfulscoop/sbert-ja) - ハギングフェイスモデルハブのSentence BERT日本語モデルをトレーニングするためのコード
 * [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) - 「日本のツイートの感情分析と日本のワクチン接種との比較」の公式微調整コード
 * [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) - 日本語GPT2生成モデル
 * [text2text-japanese](https://github.com/tanreinama/text2text-japanese) - GPT-2ベースのテキスト2テキスト変換モデル
 * [gpt-ja](https://github.com/colorfulscoop/gpt-ja) - HuggingFaceのtransformers用のGPT-2日本語モデル
 * [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) - フレンドリー_JAコーパスを使用してトレーニングされたMTモデルは、標準的な漢字語彙の代わりにラテン語/英語由来のカタカナ語彙を使用することで、日本語を西洋人にとってより簡単/アクセスしやすくすることを目指しています。
 * [albert-japanese](https://github.com/alinear-corp/albert-japanese) - 日本語テキスト用のSentencePieceを使用したBERT。
 * [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) - 日本語WikipediaコーパスでBERTのPre-Trainedモデルを生成するためのリポジトリ
 * [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) - 日本語のDistilBERT事前学習モデルで、Wikipediaで訓練されました。
 * [bert](https://github.com/informatix-inc/bert) - このリポジトリは、日本語コーパスで事前学習されたRoBERTaを使用するためのスニペットを提供しています。私たちのデータセットは、日本語のWikipediaとWebスクロールされた記事で、合計25GBです。リリースされたモデルは、HuggingFaceからのものをベースに構築されています。
 * [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) - ラボロ DistilBERT 日本語
 * [luke](https://github.com/studio-ousia/luke) - LUKE -- 知識ベース埋め込みを用いた言語理解
 * [GPTSAN](https://github.com/tanreinama/GPTSAN) - 汎用スイッチトランスをベースにした日本語モード
 * [japanese-clip](https://github.com/rinnakk/japanese-clip) - 株式会社りんなの日本語クリップ。
 * [AcademicBART](https://github.com/EhimeNLP/AcademicBART) - 私たちは、学術データベースCiNii Articlesの論文要約を用いて、BARTベースの日本語マスク言語モデルを事前学習しました。
 * [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) - 私たちは、学術データベースCiNii Articlesの論文要約を用いて、RoBERTaベースの日本語マスク言語モデルを事前学習しました。
 * [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) - 131 GBの日本語ウェブテキストで事前学習されたDistilBERTモデル。教師モデルは、LINE内で構築されたBERT-baseです。
 * [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) - 日本語に翻訳したStanford Alpacaのデータセットを用いてLLaMAをファインチューニングし作成したLow-Rank AdapterのリンクとGenerateサンプルコード
 * [albert-japanese-tinysegmenter](https://github.com/nknytk/albert-japanese-tinysegmenter) - 日本語のWikipediaリソースで公式ALBERT（https://github.com/google-research/albert）を事前学習するための事前学習済みモデル、コード、ガイダンスを提供します。
 * [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) - 日本のLLaMa実験
日本のLLaMa実験
 * [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) - EasyLightChatAssistantは、KoboldCppで簡単に試すことができる、軽量で検閲や規制のないローカル日本語モデルのLightChatAssistantです。


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

 * [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) - ChatGPTを使ってVRChat上でお喋り出来るようにするプログラム。
 * [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) - AITuberの基礎となる部分を開発しています
 * [wanna](https://github.com/hirokidaichi/wanna) - 自然言語でのシェルコマンド起動ツール
 * [ChatdollKit](https://github.com/uezo/ChatdollKit) - ChatdollKitを使用すると、あなたの3Dモデルをチャットボットに変換できます。
 * [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) - 日本語のChatGPT API用GUI
 * [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) - ChatGPT3.5を搭載した伺かゴースト「AI妹アイちゃん」です。利用には別途ChatGPTのAPIキーが必要です。
 * [vrchatbot](https://github.com/Geson-anko/vrchatbot) - VRChatにAI Botを作るためのリポジトリ
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPTがYouTuberをやります
 * [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) - Nuxt 3を使用して構築されたチャットボックスアプリケーションで、Open AIテキスト補完エンドポイントによって動作します。AIフレンドの異なるパーソナリティを選択できます。デフォルトでは日本語で応答します。このアプリを使用して、日本語のスキルを練習することができます！
 * [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) - このChrome拡張機能は、ChatGPTを使用して選択した日本語テキストをひらがなに翻訳できます。
 * [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) - このサンプルでは、Retrieval Augmented Generation パターンを使用して、独自のデータに対してChatGPT のような体験を作成するためのいくつかのアプローチを示しています。
 * [chatvrm](https://github.com/pixiv/chatvrm) - ChatVRMはブラウザで簡単に3Dキャラクターと会話ができるデモアプリケーションです。
 * [sftly-replace](https://github.com/kmizu/sftly-replace) - 選択したテキストをやさしく置き換えるためのChrome拡張機能
 * [summarize_arxv](https://github.com/rkmt/summarize_arxv) - 図を含むarXiv論文を要約する。
 * [aiavatarkit](https://github.com/uezo/aiavatarkit) - AIベースの会話型アバターを超高速で構築する
 * [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) - このリポジトリは、神戸市役所でのChatGPTの試行利用に向けて作成したフロー等をソリューション化し公開するものです。
 * [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) - Azure OpenAIを活用したアプリケーション実装のリファレンスを目的として、アプリのサンプル（リファレンスアーキテクチャ、サンプルコードとデプロイ手順）を無償提供しています。
 * [character_chat](https://github.com/mutaguchi/character_chat) - OpenAIのAPIを利用して、設定したキャラクターと日本語で会話するチャットスクリプトです。
 * [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) - OpenAIのChatGPT APIをSlack上で利用するためのSlackbotスクリプト (日本語での利用が前提)
 * [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) - ChatGPT の Prompt のサンプルです。
 * [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) - PythonとLangchainを使用して構築された日本語漢字フラッシュカードアプリで、GPT-4の知能が強化されています。
 * [IgakuQA](https://github.com/jungokasai/IgakuQA) - 日本の医師免許試験におけるGPT-4とChatGPTの評価
 * [japagen](https://github.com/retrieva/japagen) - 日本語タスクにおけるLLMを用いた疑似学習データ生成の検討


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

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - 「mecab-ipadic」に基づくウェブ上の言語リソースに基づく新語辞典
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - 日本語アクセント辞書ジェネレーター
 * [jamdict](https://github.com/neocl/jamdict) - Jim Breen氏のJMdict、KanjiDic2、JMnedict、漢字ラジカルマッピングを操作するためのPython 3ライブラリ
 * [unidic-py](https://github.com/polm/unidic-py) - pipを介してインストールするためにパッケージ化されたUnidic。
 * [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) - 日本企業用語辞典（JCLdic）
 * [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) - すだち向け万病辞書
 * [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) - Wikipedia（日本語版）からSKK/MeCab辞書を生成する。
 * [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) - テキストに関連する感情を見つけるための辞書
 * [JumanDIC](https://github.com/ku-nlp/JumanDIC) - このリポジトリには、JUMANとJuman ++の辞書を構築するためのソース辞書ファイルが含まれています。
 * [ipadic-py](https://github.com/polm/ipadic-py) - Pythonから簡単に使用できるようにパッケージ化されたIPAdic。
 * [unidic-lite](https://github.com/polm/unidic-lite) - 簡単なpipインストール用のUniDicの小さなバージョン。
 * [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) - 日本語で絵文字入力をするための IME 追加辞書 orange_book Google 日本語入力などで日本語から絵文字への変換を可能にする IME 拡張辞書
 * [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) - 日英変換・英語略語展開のための IME 追加辞書 orange_book 日本語から英語への和英変換や英語略語の展開を Google 日本語入力や ATOK などで可能にする IME 拡張辞書
 * [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) - ニコニコ大百科とピクシブ百科事典の共通部分のIME辞書
 * [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) - これはGoogleIME用カタカナ語辞書プロジェクトのアーカイブです。日本語の外来語から英語へのGoogle IMEユーザー辞書のプロジェクトアーカイブです。
 * [emoticon](https://github.com/tiwanari/emoticon) - Google日本語入力の顔文字辞書∩(,,Ò‿Ó,,)∩
 * [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) - open source mozc dictionaryをMeCab辞書のフォーマットに変換したものです。
 * [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) - 電音IME: Microsoft IMEなどで利用することを想定した「電音部」関連用語の辞書
 * [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) - Microsoft IMEなどで利用することを想定した「にじさんじ」関連用語の用語辞書です。
 * [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) - Microsoft IMEなどで利用することを想定した、現状判明している全てのポケモンの名前を網羅した用語辞書です。
 * [EJDict](https://github.com/kujirahand/EJDict) - 英和辞書データ（パブリックドメイン）EJDict-hand
 * [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) - 贵樣ばこゐ辞畫を使て正レい日本语を使ラことが出來ゑ。
 * [genshin-dict](https://github.com/kotofurumiya/genshin-dict) - Windows/macOSで利用可能な原神の用語辞書です。
 * [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) - JMdictとJMnedictをJSON形式で入力してください。
 * [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) - 外部の単語をMozcシステム辞書に変換する。
 * [mh-dict-jp](https://github.com/utubo/mh-dict-jp) - MonsterHunterのユーザー辞書を作りたい…
 * [jitenbot](https://github.com/stephenmk/jitenbot) - 日本語の辞書ウェブサイトやアプリからデータをポータブルなファイル形式に変換する
 * [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) - mecab-unidicの言語リソースに基づいたネオログ辞書
 * [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) - ホロライブ（ホロライブプロダクション）に関する辞書ファイルです。./dictionary フォルダ内のテキストファイルを使って、IMEに単語を追加できます。詳細はREADME.mdをご覧ください。
 * [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) - Yomitan/YomichanのためのJMdict、JMnedict、KANJIDIC。
 * [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) - Yomichanの単語に対するJLPTレベルのタグ
 * [Jitendex](https://github.com/stephenmk/Jitendex) - 複数の辞書クライアントと互換性のある、無料でオープンライセンスの日本語-英語辞書
 * [jiten](https://github.com/obfusk/jiten) - JMDict/Kanjidicに基づいた日本語のAndroid/CLI/Web辞書 — 日本語辞典、和英辞典、漢英字典、和独辞典、和蘭辞典
 * [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) - ピクシブ百科事典読谷のため
 * [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) - うちなーぐち辞典（沖縄語辞典）


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
|[uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/nanjakkun/uchinaaguchi_dict?style=social)|


## Corpus

### Part-of-speech tagging / Named entity recognition

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - Wikipediaを用いた日本語の固有表現抽出データセット
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 固有表現認識のための日本語IOB2タグ付きコーパス。
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter コーパス
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - 並列の普遍的な依存関係。
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - Google UDT 2.0からの日本語データ。
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大学ウェブドキュメントリードコーパス
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 注釈付きの普門買取センターのコーパス


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

 * [small_parallel_enja](https://github.com/odashi/small_parallel_enja) - 機械翻訳ベンチマーク用の50k英日並列コーパス。
 * [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) - 日中NMTのためのWebクロールされたコーパス
 * [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) - Courseraのコーパスマイニングとマルチステージファインチューニングによる講義翻訳の改善
 * [JESC](https://github.com/rpryzant/JESC) - 英語と日本語の大規模な平行コーパス
 * [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) - AMIミーティング並列コーパス
 * [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) - このディレクトリには、巨大な日英字幕コーパスが含まれています。生データは、スタンフォード大学のJESCプロジェクトから取得されています。
 * [jesc_small](https://github.com/yusugomori/jesc_small) - 小さな日英字幕コーパス
 * [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) - 禁止用語や単語レベルを考慮した日英対訳コーパスです。
 * [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) - CJKコンピュータサイエンス用語比較 / 中日韓コンピュータサイエンス用語対照 / 日中韓コンピュータサイエンス用語比較 / 韓中日コンピュータサイエンス用語対照
 * [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) - 日英並列コーパスの作成スクリプトとNMTモデルのトレーニングに関するスクリプト
 * [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) - Google vs DeepL（日本語）


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

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本映画のおすすめ対話データセット
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - おーぷん2ちゃんねるをクロールして作成した対話コーパス
 * [BSD](https://github.com/tsuruoka-lab/BSD) - ビジネスシーンの対話コーパス
 * [asdc](https://github.com/megagonlabs/asdc) - 宿泊施設探索対話コーパス
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - seq2seqなどに使用する日本語の対話データ
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - このリポジトリには、AACL-IJCNLP 2022のWorkshop Eval4NLP 2022で発表された「Chat Translation Error Detection for Assisting Cross-lingual Communications」の論文で公開された日英バイリンガルチャットコーパスBPersna-chatが含まれています。
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 「日本語日常対話コーパス」は、日常生活に関する会話を中心に、学校、旅行、健康、エンターテインメントの5つのトピックについての高品質なマルチターン対話データセットです。
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - LLM構築用の日本語チャットデータセット

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

 * [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) - 日本の現実的なテキスト推論コーパス（NLP 2020、LREC 2020）
 * [kanji-data](https://github.com/davidluzgouveia/kanji-data) - 更新されたJLPTレベルとWaniKani情報を含むJSON漢字データセット
 * [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) - 日本語単語類似度データセット
 * [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) - 日本語テキスト簡略化のための言い換えデータベース
 * [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) - チャッキのアスペクトベースの感情分析データセット
 * [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) - JaQuAD: 機械読解のための日本語質問応答データセット（2022年、Skelter Labs）
 * [JaNLI](https://github.com/verypluming/JaNLI) - 日本語の敵対的自然言語推論データセット
 * [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) - エビデンスに基づく説明データセット（AACL-IJCNLP 2020）
 * [emoji-ja](https://github.com/yagays/emoji-ja) - UNICODE絵文字の日本語読み/キーワード/分類辞書
 * [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) - Wikipediaから作成した日本語名寄せデータセット
 * [ja.text8](https://github.com/Hironsan/ja.text8) - 単語埋め込みのための日本語テキスト8コーパス。
 * [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) - 3行要約データセット
 * [japanese](https://github.com/hingston/japanese) - このリポジトリには、リーズ大学コーパスによって頻度順に決定された44,998の最も一般的な日本語単語のリストが含まれています。
 * [kanji-frequency](https://github.com/scriptin/kanji-frequency) - 様々な情報源から収集された漢字使用頻度データ
 * [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) - TEDxJP-10K ASR 評価データセット
 * [CoARiJ](https://github.com/chakki-works/CoARiJ) - 日本の年次報告書のコーパス
 * [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) - 日本語で書かれた技術書を収集した生コーパス/ツール
 * [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) - ITAコーパスのチャンク化された単語注釈
 * [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) - NLPのためのWikipediaテキストの前処理のためのユーティリティスクリプト
 * [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) - 日本語における不適切表現を収集します。自然言語処理の時のデータクリーニング用等に使えると思います。
 * [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) - 参議院の公式ウェブサイトから会派、議員、議案、質問主意書のデータを整理しました。
 * [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) - 国会議案データベース：衆議院
 * [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) - STAIRキャプション：大規模な日本語画像キャプションデータセット
 * [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) - ウィノグラード・スキーマ・チャレンジの日本語翻訳
 * [speechBSD](https://github.com/ku-nlp/speechBSD) - 音声と話者属性情報を含むBSDコーパスの拡張版
 * [ita-corpus](https://github.com/mmorise/ita-corpus) - ITAコーパスの文章リスト
 * [rohan4600](https://github.com/mmorise/rohan4600) - モーラバランス型日本語コーパス
 * [anlp-jp-history](https://github.com/whym/anlp-jp-history) - 言語処理学会年次大会講演の全リスト・機械可読版など
 * [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) - 敬語変換タスクにおける評価用データセット
 * [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) - 日本語における英語の借用語
 * [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) - 日本語ウィキペディアのウィキフィケーションコーパス
 * [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) - これは日本の総理大臣の一般政策演説のコーパスです。
 * [wrime](https://github.com/ids-cv/wrime) - WRIME: 主観と客観の感情分析データセット
 * [jtubespeech](https://github.com/sarulab-speech/jtubespeech) - JTubeSpeech：YouTubeから収集された日本語音声のコーパス
 * [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) - 日本語Wikipediaで使用される頻出単語のリスト
 * [kokkosho_data](https://github.com/rindybell/kokkosho_data) - 車両不具合情報に関するデータセット
 * [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) - デジタル化資料OCRテキスト化事業において作成されたOCR学習用データセット
 * [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) - 全国書誌データから作成した振り仮名のデータセット
 * [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) - JVS（日本語多目的話者）コーパスのラベルの自作
 * [hirakanadic](https://github.com/po3rin/hirakanadic) - 任意の複合語リストから、スダチをひらがなからカタカナに正規化することができます。
 * [animedb](https://github.com/anilogia/animedb) - 約100年に渡るアニメ作品リストデータベース
 * [security_words](https://github.com/SaitoLab/security_words) - サイバーセキュリティに関連する公的な組織の日英対応
 * [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) - 日本の国会議員のデータ
 * [honkoku-data](https://github.com/yuta1984/honkoku-data) - 「みんなで翻刻」は、歴史資料の市民参加型翻刻プラットフォームであり、ここはそのテキストデータの置き場所です。https://honkoku.org で作成された歴史的な日本の文書の転写テキストです。
 * [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) - wikiHowデータセット（日本語版）
 * [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) - 日本語/英語のエンジニア用語リスト
 * [JSICK](https://github.com/verypluming/JSICK) - 日本語の構成的知識を含む文（JSICK）データセット/JSICKストレステストセット
 * [phishurl-list](https://github.com/JPCERTCC/phishurl-list) - JPCERT/CCからのフィッシングURLデータセット
 * [jcms](https://github.com/shigashiyama/jcms) - 多数の専門分野をカバーした日本語コーパス（JCMS）
 * [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) - www.aozora.gr.jpのテキストのみのアーカイブ
 * [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) - friendly_JAは、標準的な漢語辞典の代わりに、ラテン語/英語由来のカタカナ語彙を使用して日本語をより簡単にすることを目的とした、日本語から日本語への並列コーパスです。
 * [topokanji](https://github.com/scriptin/topokanji) - 効果的な学習のためのトポロジカルに並べられた漢字リスト
 * [isbn4groups](https://github.com/uribo/isbn4groups) - ISBN-13における日本語での出版物 (978-4-XXXXXXXXX) に関するデータ等
 * [NMeCab](https://github.com/komutan/NMeCab) - NMeCab: .NET上の日本語形態素解析器について
 * [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) - デジタル化資料から作成したOCRテキストデータのngram頻度統計情報のデータセット
 * [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) - 2023年1月にリニューアルしたNDL Ngram Viewerのソースコード等一式
 * [data_set](https://github.com/japanese-law-analysis/data_set) - 法律・判例関係のデータセット
 * [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) - huggingfaceのデータセットのためのWRIME
 * [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) - NDL古典籍OCR学習用データセット（みんなで翻刻加工データ）
 * [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) - GISと考古学シミュレーター。2023年開発中。
 * [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) - LIWC2015の日本語版
 * [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) - ハグフェイスのデータセット用に、日本のライブドアニュースコーパスを入力してください。
 * [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) - JGLUE：huggingfaceデータセットのための日本語一般言語理解評価
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMoralityは、日本の注釈者の常識的な道徳を反映したクラウドソーシングによって作成されたデータセットです。
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - コメット-アトミック ja
 * [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) - 日本語での対話の常識グラフ
 * [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) - 「日本語毒性スキーマの提案と評価」は、日本語における毒性のスキーマとデータセットを提供します。
 * [camera](https://github.com/CyberAgentAILab/camera) - CAMERA（CyberAgent Multimodal Evaluation for Ad Text GeneRAtion）は、日本の広告テキスト生成データセットです。
 * [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) - 日本語フェイクニュースデータセット
 * [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) - jpn_explainable_qa_dataset
 * [copa-japanese](https://github.com/nlp-titech/copa-japanese) - 日本語のCOPAデータセット
 * [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) - 「意味原理に基づく単語リスト（WLSP）」の単語親しみ度率
 * [ProSub](https://github.com/matbahasa/ProSub) - 代名詞の代替物と呼びかけの言葉に関する言語間比較研究
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMoralityは、日本の注釈者の常識的な道徳を反映したクラウドソーシングによって作成されたデータセットです。
 * [ramendb](https://github.com/nuko-yokohama/ramendb) - なんとかデータベース( https://supleks.jp/ )からのスクレイピングツールと収集データ
 * [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) - huggingfaceデータセットのためのCAMERA（CyberAgent Multimodal Evaluation for Ad Text GeneRAtion）
 * [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) - ファクトチェック文NLIデータセット
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - databricks/dolly-v2-12b の学習データに使用されたdatabricks-dolly-15k.jsonl を日本語に翻訳したデータセットになります。
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELDは、MELDに基づく感情認識音声翻訳のための英日データセットです。
 * [meconaudio](https://github.com/elith-co-jp/meconaudio) - Mecon Audio（メディカル・カンファレンス・オーディオ）は、厚生労働省が主催する先進医療会議の議事録を読み上げるためのデータセットです。
 * [japanese-addresses](https://github.com/geolonia/japanese-addresses) - 全国の町丁目レベル（277,191件）の住所データのオープンデータ
 * [aozorasearch](https://github.com/myokoym/aozorasearch) - グルンガによる青空文庫の全文検索システム。青空文庫全文検索ライブラリ兼Webアプリ。
 * [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) - このリポジトリには、LLM-jpコーパスを再現するためのスクリプトが含まれています。
 * [alpaca_ja](https://github.com/shi3z/alpaca_ja) - alpacaデータセットを日本語化したものです
 * [instruction_ja](https://github.com/megagonlabs/instruction_ja) - 出力
 * [japanese-family-names](https://github.com/siikamiika/japanese-family-names) - 頻度順に並べられた読み付きの上位5000の日本の姓
 * [kanji-data-media](https://github.com/kanjialive/kanji-data-media) - 漢字アライブからの漢字、部首、メディアファイル、フォント、関連リソースに関する日本語データ
 * [reazonspeech](https://github.com/reazon-research/reazonspeech) - 自宅で大規模な日本語音声コーパスを構築する
 * [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) - 青空文庫及びサピエの点字データから作成した振り仮名のデータセット
 * [koniwa](https://github.com/koniwa/koniwa) - 日本語のアノテーション付き声のオープンコレクション
 * [JMMLU](https://github.com/nlp-waseda/JMMLU) - 日本語マルチタスク言語理解ベンチマーク 日本語巨大マルチタスク言語理解ベンチマーク
 * [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) - 青空文庫振り仮名注釈付き音声コーパスのデータセット
 * [jqara](https://github.com/hotchpotch/jqara) - JQaRA: 検索拡張（RAG）を活用した日本語質問応答データセット
 * [jemhopqa](https://github.com/aiishii/jemhopqa) - JEMHopQA（Japanese Explainable Multi-hop Question Answering）は、内部推論を評価できる日本語のマルチホップQAデータセットです。
 * [jacred](https://github.com/youmima/jacred) - 日本語文書レベルの関係抽出データセットのリポジトリ（3月にリリース予定）
 * [jades](https://github.com/naist-nlp/jades) - JADESは、日本語のテキスト簡素化のためのデータセットであり、『JADES: New Text Simplification Dataset in Japanese Targeted at Non-Native Speakers』で説明されています（論文は近日中に公開されます）。
 * [do-not-answer-ja](https://github.com/kunishou/do-not-answer-ja) - 2023年8月にメルボルン大学から公開された安全性評価データセット『Do-Not-Answer』を日本語LLMの評価においても使用できるように日本語に自動翻訳し、さらに日本文化も考慮して修正したデータセット。
 * [oasst1-89k-ja](https://github.com/kunishou/oasst1-89k-ja) - OpenAssistant のオープンソースデータ OASST1 を日本語に翻訳したデータセットになります。
 * [jacwir](https://github.com/hotchpotch/jacwir) - JaCWIR: Japanese Casual Web IR  日本語情報検索評価のための小規模でカジュアルなWebタイトルと概要のデータセット
 * [japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict) - 日本語学習者のための科学技術業界でよく使われる片仮名と元の単語対照表


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
|[jacwir](https://github.com/hotchpotch/jacwir)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/hotchpotch/jacwir?style=social)|
|[japanese-technical-dict](https://github.com/laoshubaby/japanese-technical-dict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/laoshubaby/japanese-technical-dict?style=social)|


## Tutorial

 * [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) - spaCyチュートリアルの英語版と日本語版。spacy-transformers、BERT、GiNZA。
 * [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) - 日本語コーパスを使用してfastTextをトレーニングするチュートリアル
 * [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) - AllenNLP-NER-ja：AllenNLPによる日本語固有表現抽出
 * [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) - ChariotとPyTorchを使用した日本語テキスト分類の実験
 * [ginza-examples](https://github.com/poyo46/ginza-examples) - 日本語NLPライブラリGiNZAのすゝめ
 * [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) - ドキュメント分類にBERTを使用する-日本語
 * [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) - Google Colaboratoryで日本語のBERTを動かす方法です。
 * [bert-book](https://github.com/stockmarkteam/bert-book) - 「BERTによる自然言語処理入門: Transformersを使った実践プログラミング」サポートページ
 * [janome-tutorial](https://github.com/mocobeta/janome-tutorial) - Janome を使ったテキストマイニング入門チュートリアルです。
 * [handson-language-models](https://github.com/hnishi/handson-language-models) - 日本語の言語モデルのハンズオン資料です
 * [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) - Google Colabで日本語テキスト推論を試す
 * [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) - deep-learning-with-pytorchの日本語版リポジトリです。
 * [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) -【2023年版】BERTによるテキスト分類
 * [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) - ディープラーニングによる自然言語処理（共立出版）のサポートページです
 * [llm-book](https://github.com/ghmagazine/llm-book) - 「大規模言語モデル入門」（技術評論社, 2023）のGitHubリポジトリ
 * [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) - NLP2024 チュートリアル３ 作って学ぶ日本語大規模言語モデル - 環境構築手順とソースコード


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

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 日本語の事前学習済みBERTモデルのリストと、単語/サブワードトークン化+語彙構築アルゴリズム情報。
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 文法誤り訂正に関する日本語文献を収集・分類するためのリポジトリ
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - テキストコーパスなどのリスト（主に日本語）
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - ディープラーニングモデルの性能を体系的に最大化するためのプレイブック
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 日本語の音声、特にアクセントに関するリソースを一つのリストにまとめようとしています。
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - オープンソースの日本語LLMまとめ


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
