# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/taishi-i/awesome-japanese-nlp-resources)
[![RRs](https://img.shields.io/badge/PRs-welcome-brightgreen)](https://github.com/taishi-i/awesome-japanese-nlp-resources/pulls)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語の自然言語処理に関するPythonライブラリ、学習済みモデル、辞書、およびコーパスの厳選リストです。

- [819件の GitHub リポジトリ情報](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) を掲載中
- [240 件の Hugging Face リポジトリ情報 ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) を掲載中
- [リポジトリ情報を検索するツールをリリース 🔎](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## 🎉 The latest additions

**JavaScript**
 * [yama](https://github.com/sapjax/yama) - 任意のウェブサイトで日本語の語彙を習得します。
 * [kaitai](https://github.com/compile10/kaitai) - AIを使用して日本語の文章構造を分析するためのアプリケーションです。このツールは、単語やフレーズがどのように関連しているかを視覚化し、インタラクティブな図表で文法的な関係を示します。

_Updated on Feb 10, 2026_

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
日本語を単語や形態素に分割し品詞や原形を付与するライブラリ

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
 * [Mecari](https://github.com/zbller/Mecari) - Mecari（グラフニューラルネットワークを用いた日本語形態素解析）


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [SudachiPy](https://github.com/WorksApplications/SudachiPy) | 📥 369k | 📦 59M | ⭐ 425 | 🔴 october 2022|
| 🔗 [Janome](https://github.com/mocobeta/janome) | 📥 36k | 📦 11M | ⭐ 904 | 🟡 october 2025|
| 🔗 [mecab-python3](https://github.com/SamuraiT/mecab-python3) | 📥 186k | 📦 34M | ⭐ 580 | 🟢 november 2025|
| 🔗 [mecab](https://github.com/ikegami-yukino/mecab/tree/master/mecab/python) | 📥 4k | 📦 642k | ⭐ 271 | 🔴 october 2024|
| 🔗 [fugashi](https://github.com/polm/fugashi) | 📥 130k | 📦 13M | ⭐ 506 | 🟡 october 2025|
| 🔗 [nagisa](https://github.com/taishi-i/nagisa) | 📥 47k | 📦 7M | ⭐ 411 | 🟢 december 2025|
| 🔗 [pyknp](https://github.com/ku-nlp/pyknp) | 📥 2k | 📦 3M | ⭐ 92 | 🟢 january|
| 🔗 [Mykytea-python](https://github.com/chezou/Mykytea-python) | 📥 950 | 📦 551k | ⭐ 36 | 🔴 january 2024|
| 🔗 [konoha](https://github.com/himkt/konoha) | 📥 30k | 📦 5M | ⭐ 261 | 🟡 april 2025|
| 🔗 [natto-py](https://github.com/buruzaemon/natto-py) | 📥 196k | 📦 32M | ⭐ 95 | 🔴 november 2023|
| 🔗 [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) | 📥 23 | 📦 27k | ⭐ 23 | 🔴 may 2017|
| 🔗 [python-vaporetto](https://github.com/daac-tools/python-vaporetto) | 📥 368 | 📦 173k | ⭐ 21 | 🟡 june 2025|
| 🔗 [dango](https://github.com/mkartawijaya/dango) | 📥 72 | 📦 25k | ⭐ 25 | 🔴 november 2021|
| 🔗 [rhoknp](https://github.com/ku-nlp/rhoknp) | 📥 10k | 📦 964k | ⭐ 37 | 🟢 january|
| 🔗 [python-vibrato](https://github.com/daac-tools/python-vibrato) | 📥 249 | 📦 115k | ⭐ 43 | 🔴 september 2024|
| 🔗 [jagger-python](https://github.com/lighttransport/jagger-python) | 📥 1k | 📦 293k | ⭐ 12 | 🔴 march 2024|
| 🔗 [Mecari](https://github.com/zbller/Mecari) | - | - | ⭐ 36 | 🟡 september 2025|


### Parsing
文の構造や依存関係を解析して文法関係を明らかにするライブラリ

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
 * [lightblue](https://github.com/daisukebekki/lightblue) - DTS表現を使用した日本語のCCGパーサー
 * [natsume-simple](https://github.com/borh-lab/natsume-simple) - natsume-simpleは日本語の係り受け関係検索システム
 * [jdeppy](https://github.com/matsurih/jdeppy) - J.DepP用のPythonラッパー、高速日本語依存構造解析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ginza](https://github.com/megagonlabs/ginza) | 📥 11k | 📦 2M | ⭐ 833 | 🔴 march 2024|
| 🔗 [cabocha](https://github.com/ikegami-yukino/cabocha/tree/master/python) | 📥 57 | 📦 53k | ⭐ 7 | 🔴 august 2022|
| 🔗 [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) | 📥 574 | 📦 326k | ⭐ 38 | 🟢 december 2025|
| 🔗 [camphr](https://github.com/PKSHATechnology-Research/camphr) | 📥 326 | 📦 267k | ⭐ 338 | 🔴 august 2021|
| 🔗 [SuPar-UniDic](https://github.com/KoichiYasuoka/SuParUniDic) | 📥 463 | 📦 117k | ⭐ 20 | 🔴 repo not found|
| 🔗 [depccg](https://github.com/masashi-y/depccg) | 📥 73 | 📦 45k | ⭐ 98 | 🔴 august 2023|
| 🔗 [bertknp](https://github.com/ku-nlp/bertknp) | - | - | ⭐ 23 | 🔴 october 2021|
| 🔗 [esupar](https://github.com/KoichiYasuoka/esupar) | 📥 522 | 📦 166k | ⭐ 54 | 🟢 january|
| 🔗 [yomikata](https://github.com/passaglia/yomikata) | 📥 26 | 📦 49k | ⭐ 32 | 🔴 october 2023|
| 🔗 [jdepp-python](https://github.com/lighttransport/jdepp-python) | 📥 1k | 📦 278k | ⭐ 4 | 🔴 february 2024|
| 🔗 [lightblue](https://github.com/daisukebekki/lightblue) | - | - | ⭐ 26 | 🟢 yesterday|
| 🔗 [natsume-simple](https://github.com/borh-lab/natsume-simple) | - | - | ⭐ 5 | 🟡 february 2025|
| 🔗 [jdeppy](https://github.com/matsurih/jdeppy) | 📥 17 | 📦 11k | ⭐ 3 | 🔴 february 2022|


### Converter
仮名ローマ字や全半角など文字や表記を変換するライブラリ

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
 * [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) - 数量表現や時間表現の抽出・正規化を行うNormalizeNumexpのPython実装数量表現や時間表現の抽出・正規化を行うNormalizeNumexpのPython実装
 * [Jusho](https://github.com/nagataaaas/Jusho) - 日本の郵便番号データの簡単なラッパー
 * [yurenizer](https://github.com/sea-turt1e/yurenizer) - 日本語テキストの表記の一貫性を解消する日本語テキスト正規化ツール
 * [e2k](https://github.com/Patchethium/e2k) - 自動的な英語から片仮名への変換ツール
 * [alkana.py](https://github.com/zomysan/alkana.py) - アルファベット文字列のカタカナ読みを取得するツール。
 * [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) - 英語文字列をカタカナに変換するプログラム
 * [kanjiconv](https://github.com/sea-turt1e/kanjiconv) - 漢字変換器へひらがな、カタカナ、ローマ字。
 * [kanjize](https://github.com/nagataaaas/kanjize) - Kanjize(カンジャイズ): 漢字数字と整数の簡単な変換ツール


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [pykakasi](https://github.com/miurahr/pykakasi) | 📥 277k | 📦 28M | ⭐ 443 | 🔴 july 2022|
| 🔗 [cutlet](https://github.com/polm/cutlet) | 📥 24k | 📦 1M | ⭐ 372 | 🟡 june 2025|
| 🔗 [alphabet2kana](https://github.com/shihono/alphabet2kana) | 📥 282 | 📦 56k | ⭐ 14 | 🟡 october 2025|
| 🔗 [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) | - | - | ⭐ 50 | 🔴 november 2020|
| 🔗 [mozcpy](https://github.com/ikegami-yukino/mozcpy) | 📥 101 | 📦 11k | ⭐ 46 | 🟡 february 2025|
| 🔗 [jamorasep](https://github.com/tachi-hi/jamorasep) | 📥 24 | 📦 8k | ⭐ 11 | 🟡 may 2025|
| 🔗 [text2phoneme](https://github.com/korguchi/text2phoneme) | - | - | ⭐ 13 | 🔴 may 2023|
| 🔗 [jntajis-python](https://github.com/opencollector/jntajis-python) | 📥 356 | 📦 105k | ⭐ 21 | 🔴 june 2023|
| 🔗 [wiredify](https://github.com/eggplants/wiredify) | 📥 20 | 📦 6k | ⭐ 3 | 🟢 december 2025|
| 🔗 [mecab-text-cleaner](https://github.com/34j/mecab-text-cleaner) | 📥 24 | 📦 4k | ⭐ 7 | 🔴 november 2024|
| 🔗 [pynormalizenumexp](https://github.com/tkscode/pynormalizenumexp) | 📥 57 | 📦 14k | ⭐ 8 | 🔴 april 2024|
| 🔗 [Jusho](https://github.com/nagataaaas/Jusho) | 📥 222 | 📦 52k | ⭐ 11 | 🔴 june 2024|
| 🔗 [yurenizer](https://github.com/sea-turt1e/yurenizer) | 📥 170 | 📦 17k | ⭐ 4 | 🟡 march 2025|
| 🔗 [e2k](https://github.com/Patchethium/e2k) | 📥 305 | 📦 22k | ⭐ 15 | 🟢 november 2025|
| 🔗 [alkana.py](https://github.com/zomysan/alkana.py) | - | - | ⭐ 33 | 🔴 october 2021|
| 🔗 [englishtokanaconverter](https://github.com/actlaboratory/englishtokanaconverter) | - | - | ⭐ 4 | 🟢 december 2025|
| 🔗 [kanjiconv](https://github.com/sea-turt1e/kanjiconv) | 📥 102 | 📦 12k | ⭐ 16 | 🟡 october 2025|
| 🔗 [kanjize](https://github.com/nagataaaas/kanjize) | 📥 8k | 📦 1M | ⭐ 68 | 🟡 june 2025|


### Preprocessor
テキストを正規化し解析に適した形に整えるライブラリ

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - mecab-neologd用の日本語テキスト正規化ツール
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - ひらがな、カタカナ、半角、全角のための純粋なPython日本語文字相互変換器
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - 日本語半角と全角の素早い変換ツール
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 日本語のウェブテキスト用の強力なテキストクリーナー
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 複数の前処理を構成して管理するテキスト前処理ツール
 * [utsuho](https://github.com/juno-rmks/utsuho) - Utsuhoは、日本語の半角カタカナと全角カタカナの間で双方向変換を容易にするPythonモジュールです。
 * [python-habachen](https://github.com/Hizuru3/python-habachen) - もう一つの高速な日本語文字列変換ツール
 * [kairyou](https://github.com/bikatr7/kairyou) - SpaCyを使用して、日本語テキストをNLP/NERで迅速に前処理し、日本語翻訳やその他のNLPタスクに使用します。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [neologdn](https://github.com/ikegami-yukino/neologdn) | 📥 6k | 📦 1M | ⭐ 286 | 🟢 december 2025|
| 🔗 [jaconv](https://github.com/ikegami-yukino/jaconv) | 📥 499k | 📦 59M | ⭐ 340 | 🟢 yesterday|
| 🔗 [mojimoji](https://github.com/studio-ousia/mojimoji) | 📥 84k | 📦 11M | ⭐ 153 | 🔴 january 2024|
| 🔗 [text-cleaning](https://github.com/ku-nlp/text-cleaning) | - | - | ⭐ 12 | 🔴 november 2022|
| 🔗 [HojiChar](https://github.com/HojiChar/HojiChar) | 📥 29k | 📦 706k | ⭐ 124 | 🟢 november 2025|
| 🔗 [utsuho](https://github.com/juno-rmks/utsuho) | 📥 136 | 📦 18k | ⭐ 4 | 🟡 october 2025|
| 🔗 [python-habachen](https://github.com/Hizuru3/python-habachen) | 📥 3k | 📦 2M | ⭐ 6 | 🟡 october 2025|
| 🔗 [kairyou](https://github.com/bikatr7/kairyou) | 📥 143 | 📦 30k | ⭐ 6 | 🟡 june 2025|


### Sentence spliter
文章を文ごとに自動で分割するライブラリ

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日本語テキストの文境界曖昧性解消ツール (にほんごぶんきょうかいはんていき)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日本語の文分割器
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 日本語テキストのための別の文レベルのトークナイザー
 * [budoux](https://github.com/google/budoux) - スタンドアロン。小さい。言語に依存しない。BudouXは、機械学習による行の整理ツールであるBudouの後継者です。
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - Python用の日本語文分割ライブラリ
 * [hasami](https://github.com/mkartawijaya/hasami) - 日本語テキストの文分割を実行するツール
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - Rustで書かれたPython用の日本語テキストセグメンター
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日本語文分割ツールの比較
 * [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) - 日本語文境界判定器、Rustで高速化されたPythonライブラリを使用して、megagonlabs/bunkaiとほぼ完全なAPI互換性を持つ40〜250倍速くなりました。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bunkai](https://github.com/megagonlabs/bunkai) | 📥 436 | 📦 105k | ⭐ 199 | 🔴 august 2023|
| 🔗 [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) | 📥 14 | 📦 5k | ⭐ 14 | 🔴 february 2021|
| 🔗 [sengiri](https://github.com/ikegami-yukino/sengiri) | 📥 73 | 📦 136k | ⭐ 24 | 🟢 november 2025|
| 🔗 [budoux](https://github.com/google/budoux) | 📥 6k | 📦 379k | ⭐ 1.6k | 🟢 last thursday|
| 🔗 [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) | 📥 2k | 📦 177k | ⭐ 73 | 🔴 april 2023|
| 🔗 [hasami](https://github.com/mkartawijaya/hasami) | 📥 145 | 📦 37k | ⭐ 6 | 🔴 february 2021|
| 🔗 [kuzukiri](https://github.com/alinear-corp/kuzukiri) | 📥 67 | 📦 26k | ⭐ 6 | 🟡 june 2025|
| 🔗 [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) | - | - | ⭐ 9 | 🔴 february 2023|
| 🔗 [fast-bunkai](https://github.com/hotchpotch/fast-bunkai) | 📥 263 | 📦 3k | ⭐ 64 | 🟡 october 2025|


### Sentiment analysis
文に含まれる感情や評価を判定するライブラリ

 * [oseti](https://github.com/ikegami-yukino/oseti) - 日本語の辞書ベースの感情分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - 日本語のネガティブ・ポジティブの分類。日本語の文章のネガティブ・ポジティブを判定します。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日本語テキストの感情分析ツール
 * [asari](https://github.com/Hironsan/asari) - Pythonで実装された日本語感情分析器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [oseti](https://github.com/ikegami-yukino/oseti) | 📥 314 | 📦 165k | ⭐ 97 | 🟡 august 2025|
| 🔗 [negapoji](https://github.com/liaoziyang/negapoji) | - | - | ⭐ 151 | 🔴 august 2017|
| 🔗 [pymlask](https://github.com/ikegami-yukino/pymlask) | 📥 56 | 📦 66k | ⭐ 116 | 🔴 july 2024|
| 🔗 [asari](https://github.com/Hironsan/asari) | 📥 165 | 📦 79k | ⭐ 152 | 🔴 october 2022|


### Machine translation
異なる言語間で文章を自動翻訳するライブラリ

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawlの事前学習済みニューラル機械翻訳（NMT）モデルの使用例。
 * [JASS](https://github.com/Mao-KU/JASS) - JASS：ニューラル機械翻訳のための日本語固有のシーケンス・トゥ・シーケンス事前学習（LREC2020）＆言語学的に駆動された低リソースニューラル機械翻訳のためのマルチタスク事前学習（ACM TALLIP）
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 日英機械翻訳の堅牢性に関する現象別評価データセット。このデータセットは、MTNTデータセットをベースに、固有名詞、略語、口語表現、および変異形の4つの言語現象の追加注釈を含んでいます。COLING 2020。
 * [VISA](https://github.com/ku-nlp/VISA) - 視覚シーンに関する機械翻訳のための曖昧な字幕データセット
 * [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) - ローカル実行を使用したplamo-2-translateモデルを利用した翻訳のためのコマンドラインインターフェース。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) | - | - | ⭐ 105 | 🔴 april 2021|
| 🔗 [JASS](https://github.com/Mao-KU/JASS) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [PheMT](https://github.com/cl-tohoku/PheMT) | - | - | ⭐ 17 | 🔴 february 2021|
| 🔗 [VISA](https://github.com/ku-nlp/VISA) | - | - | ⭐ 14 | 🔴 october 2022|
| 🔗 [plamo-translate-cli](https://github.com/pfnet/plamo-translate-cli) | - | - | ⭐ 324 | 🟡 october 2025|


### Named entity recognition
文から人名地名組織名などの固有表現を抽出するライブラリ

 * [namaco](https://github.com/chakki-works/namaco) - 文字ベースの固有表現認識。
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypediaは、Wikipediaからの拡張された固有名詞辞書です。
 * [noyaki](https://github.com/ken11/noyaki) - 文字の範囲ラベル情報をトークン化されたテキストベースのラベル情報に変換します。
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - Code to perform finetuning of the BERT model. BERTモデルのファインチューニングで固有表現抽出用タスクのモデルを作成・使用するサンプルです
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 詳細なアノテーション基準に基づく症例報告コーパスからの固有表現及び関係の抽出精度の推論を行うコード
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlpは、日本語テキストのジオタギングに使用するPythonモジュールです。
 * [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) - BERTによる日本語固有表現抽出のファインチューニング用プログラム
 * [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) - 日本語の言語（Hugging Face）リソースのためにエンコーダーのみとエンコーダーデコーダーのトランスフォーマーを微調整するための例
 * [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) - BERTのファインチューニングによる固有表現抽出


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namaco](https://github.com/chakki-works/namaco) | - | - | ⭐ 40 | 🔴 february 2018|
| 🔗 [entitypedia](https://github.com/chakki-works/entitypedia) | - | - | ⭐ 13 | 🔴 december 2018|
| 🔗 [noyaki](https://github.com/ken11/noyaki) | 📥 169 | 📦 19k | ⭐ 5 | 🔴 august 2022|
| 🔗 [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) | - | - | ⭐ 11 | 🔴 june 2022|
| 🔗 [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) | - | - | ⭐ 1 | 🔴 november 2021|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 236 | 📦 20k | ⭐ 22 | 🟡 october 2025|
| 🔗 [bert-ner-japanese](https://github.com/jurabiinc/bert-ner-japanese) | - | - | ⭐ 5 | 🔴 september 2022|
| 🔗 [huggingface-finetune-japanese](https://github.com/tsmatz/huggingface-finetune-japanese) | - | - | ⭐ 16 | 🔴 october 2023|
| 🔗 [novelanalysisbyner](https://github.com/lychee1223/novelanalysisbyner) | - | - | ⭐ 2 | 🔴 june 2024|


### OCR
画像から文字を読み取りテキスト化するライブラリ

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
 * [owocr](https://github.com/aurorawright/owocr) - 日本語テキストの光学文字認識
 * [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) - Yomitokuは、日本語に特化したAIパワードのドキュメント画像解析パッケージです。
 * [findtextcenternet](https://github.com/lithium0003/findtextcenternet) - センターネットを使用した日本語OCR
 * [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-for-manga) - 漫画用のシンプルなOCR（日本の伝統的なものと日本の縦書き）
 * [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) - 日本語の文章画像に対するOCRの性能を評価
 * [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) - 日本の漫画テキスト認識のために、Manga109sデータセットでPaddleOCR-VLを微調整します。ベースモデルは漫画内の縦書き日本語テキストの読み順に苦労しています。微調整後、モデルは漫画固有のテキストレイアウトを正しく処理します。
 * [MangaOCR](https://github.com/gnurt2041/MangaOCR) - 日本語テキスト用の軽量なOCRモデル、特にマンガ向け
 * [meikiocr](https://github.com/rtr46/meikiocr) - 高速、高精度、日本のビデオゲーム向けのローカルOCR
 * [meikipop](https://github.com/rtr46/meikipop) - Windows、Linux、およびmacOS用のユニバーサル日本語OCRポップアップ辞書


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [manga-ocr](https://github.com/kha-white/manga-ocr) | 📥 3k | 📦 236k | ⭐ 2.5k | 🟡 june 2025|
| 🔗 [mokuro](https://github.com/kha-white/mokuro) | 📥 565 | 📦 88k | ⭐ 1.5k | 🟡 june 2025|
| 🔗 [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) | - | - | ⭐ 38 | 🔴 april 2022|
| 🔗 [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) | - | - | ⭐ 244 | 🔴 april 2021|
| 🔗 [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) | - | - | ⭐ 567 | 🟡 september 2025|
| 🔗 [donut](https://github.com/clovaai/donut) | 📥 415 | 📦 196k | ⭐ 6.8k | 🔴 july 2023|
| 🔗 [JMTrans](https://github.com/ttop32/JMTrans) | - | - | ⭐ 88 | 🔴 january 2021|
| 🔗 [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) | - | - | ⭐ 153 | 🔴 july 2023|
| 🔗 [text_recognition](https://github.com/ndl-lab/text_recognition) | - | - | ⭐ 8 | 🔴 july 2023|
| 🔗 [Poricom](https://github.com/blueaxis/Poricom) | - | - | ⭐ 415 | 🔴 june 2023|
| 🔗 [owocr](https://github.com/aurorawright/owocr) | - | - | ⭐ 188 | 🟢 yesterday|
| 🔗 [yomitoku](https://github.com/kotaro-kinoshita/yomitoku) | 📥 2k | 📦 73k | ⭐ 1.3k | 🟢 january|
| 🔗 [findtextcenternet](https://github.com/lithium0003/findtextcenternet) | - | - | ⭐ 55 | 🟡 august 2025|
| 🔗 [simple-ocr-for-manga](https://github.com/yisusdev2005/simple-ocr-fogi-manga) | - | - | ⭐ 7 | 🔴 repo not found|
| 🔗 [jp-ocr-evaluation](https://github.com/yoshino/jp-ocr-evaluation) | - | - | ⭐ 1 | 🔴 march 2024|
| 🔗 [paddleocr-vl-sft-for-japanese-manga-on-rtx-3060](https://github.com/openvino-book/paddleocr-vl-sft-for-japanese-manga-on-rtx-3060) | - | - | ⭐ 7 | 🟢 december 2025|
| 🔗 [MangaOCR](https://github.com/gnurt2041/MangaOCR) | - | - | ⭐ 34 | 🔴 may 2024|
| 🔗 [meikiocr](https://github.com/rtr46/meikiocr) | 📥 1k | 📦 14k | ⭐ 53 | 🟢 january|
| 🔗 [meikipop](https://github.com/rtr46/meikipop) | - | - | ⭐ 200 | 🟢 january|


### Tool for pretrained models
事前学習済みモデルを活用して精度を高めるライブラリ

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
 * [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) - llm-lora-classificationllm-lora-分類
 * [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) - JP言語モデル評価ハーネス
 * [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) - このリポジトリには、"rinna/japanese-gpt-neox..." [gpt-neox] モデルをggmlに変換した場合に、Alpaca-LoraアダプターをLoRAチューニングに適応させるために修正されたスクリプトとマージスクリプトが含まれています。
 * [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) - このリポジトリは日本語LLMのキャラクターロールプレイに関する性能を評価するために作成しました。
 * [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) - このリポジトリは、YuzuAIのラクダリーダーボードをサポートしています。ラクダリーダーボードは、LMSYSのビクーナ評価の日本に特化した類似物です。
 * [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) - このツールは、複数のデータセットを横断して日本語の大規模言語モデルを自動評価するものです．
 * [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) - このリポジトリには、LLM-jpモデルの教師ありファインチューニングのためのコードが含まれています。
 * [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) - LLM勉強会（LLM-jp）で開発しているLLM用のトークナイザー関連をまとめたリポジトリです．
 * [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) - 日本語言語モデルの金融評価ハーネス
 * [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) - 日本のビクーニャQAベンチマーク
 * [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) - Swallowプロジェクト 大規模言語モデル 評価スクリプト
 * [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) - Swallowプロジェクト 事後学習ずみ大規模言語モデル 評価フレームワーク
 * [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) - 日本語のWikipediaに事前学習されたdoc2vecモデル
 * [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) - 日本語音素レベルBERTのリポジトリ


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 333 | 🟡 march 2025|
| 🔗 [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) | 📥 824 | 📦 173k | ⭐ 16 | 🔴 august 2022|
| 🔗 [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) | - | - | ⭐ 9 | 🔴 january 2020|
| 🔗 [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) | - | - | ⭐ 2 | 🔴 april 2021|
| 🔗 [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) | - | - | ⭐ 5 | 🔴 february 2022|
| 🔗 [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) | 📥 79 | 📦 20k | ⭐ 12 | 🔴 june 2021|
| 🔗 [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) | - | - | ⭐ 12 | 🔴 november 2024|
| 🔗 [gector-ja](https://github.com/jonnyli1125/gector-ja) | - | - | ⭐ 19 | 🔴 june 2021|
| 🔗 [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) | - | - | ⭐ 41 | 🔴 september 2021|
| 🔗 [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) | - | - | ⭐ 41 | 🔴 january 2023|
| 🔗 [transformer-copy](https://github.com/youichiro/transformer-copy) | - | - | ⭐ 29 | 🔴 september 2020|
| 🔗 [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [nagisa_bert](https://github.com/taishi-i/nagisa_bert) | 📥 589 | 📦 55k | ⭐ 4 | 🔴 december 2023|
| 🔗 [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) | - | - | ⭐ 18 | 🟢 february|
| 🔗 [jptranstokenizer](https://github.com/retarfi/jptranstokenizer) | 📥 82 | 📦 27k | ⭐ 5 | 🔴 february 2024|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [compare-ja-tokenizer](https://github.com/hitachi-nlp/compare-ja-tokenizer) | - | - | ⭐ 6 | 🔴 june 2023|
| 🔗 [lm-evaluation-harness-jp-stable](https://github.com/tdc-yamada-ya/lm-evaluation-harness-jp-stable) | - | - | ⭐ 1 | 🔴 june 2023|
| 🔗 [llm-lora-classification](https://github.com/hppRC/llm-lora-classification) | - | - | ⭐ 98 | 🔴 july 2023|
| 🔗 [jp-stable](https://github.com/Stability-AI/lm-evaluation-harness/tree/jp-stable) | - | - | ⭐ 154 | 🔴 november 2023|
| 🔗 [rinna_gpt-neox_ggml-lora](https://github.com/yukaryavka/rinna_gpt-neox_ggml-lora) | - | - | ⭐ 18 | 🔴 may 2023|
| 🔗 [japanese-llm-roleplay-benchmark](https://github.com/oshizo/japanese-llm-roleplay-benchmark) | - | - | ⭐ 40 | 🔴 november 2023|
| 🔗 [japanese-llm-ranking](https://github.com/yuzu-ai/japanese-llm-ranking) | - | - | ⭐ 50 | 🔴 march 2024|
| 🔗 [llm-jp-eval](https://github.com/llm-jp/llm-jp-eval) | - | - | ⭐ 148 | 🟢 december 2025|
| 🔗 [llm-jp-sft](https://github.com/llm-jp/llm-jp-sft) | - | - | ⭐ 62 | 🔴 june 2024|
| 🔗 [llm-jp-tokenizer](https://github.com/llm-jp/llm-jp-tokenizer) | - | - | ⭐ 45 | 🟡 february 2025|
| 🔗 [japanese-lm-fin-harness](https://github.com/pfnet-research/japanese-lm-fin-harness) | - | - | ⭐ 77 | 🟢 january|
| 🔗 [ja-vicuna-qa-benchmark](https://github.com/ku-nlp/ja-vicuna-qa-benchmark) | - | - | ⭐ 33 | 🔴 june 2024|
| 🔗 [swallow-evaluation](https://github.com/swallow-llm/swallow-evaluation) | - | - | ⭐ 23 | 🟡 september 2025|
| 🔗 [swallow-evaluation-instruct](https://github.com/swallow-llm/swallow-evaluation-instruct) | - | - | ⭐ 24 | 🟡 october 2025|
| 🔗 [pretrained_doc2vec_ja](https://github.com/yagays/pretrained_doc2vec_ja) | - | - | ⭐ 25 | 🔴 january 2019|
| 🔗 [pl-bert-ja](https://github.com/kyamauchi1023/pl-bert-ja) | - | - | ⭐ 22 | 🔴 december 2023|


### Others
日本語処理を補助するその他の汎用ライブラリ

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
 * [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) - Haystack + Elasticsearch + wikipedia(ja) を用いた、日本語の質問応答システムのサンプルヘイスタック + エラスティックサーチ + Wikipedia(ja) を使用した、日本語の質問応答システムのサンプル
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
 * [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) - JGLUEのトレーニングと評価スクリプトについて、日本語理解のベンチマークに関してJGLUEは、日本語理解のベンチマークのためのトレーニングと評価スクリプトについての情報です。
 * [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) - 日本のデータセットで事前学習されたモデルを使用して、LAVISのBLIP2 Q-formerを修正します。LAVISのBLIP2 Q-formerを日本のデータセットで事前学習されたモデルを用いて修正します。
 * [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) - wikipedia 日本語の文を、各種日本語の embeddings や faiss index へと変換するスクリプト等。
 * [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) - 日本語のSimCSEを探索中
 * [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) - Wikipediaの日本語記事を元に、ユーザの質問に回答するGradioベースのRAGのサンプル
 * [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) - GPT-4 を用いて、言語モデルの応答を自動評価するスクリプト
 * [t5-japanese](https://github.com/sonoisa/t5-japanese) - 日本語T5モデル
 * [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) - 日本語LLMを評価するためのリポジトリ
 * [jmteb](https://github.com/sbintuitions/jmteb) - JMTEB（日本語大規模テキスト埋め込みベンチマーク）の評価スクリプト
 * [pydomino](https://github.com/dwangomediavillage/pydomino) - 日本語音声に対して音素ラベルをアラインメントするためのツールです
 * [easynovelassistant](https://github.com/zuntan03/easynovelassistant) - 軽量で規制も検閲もない日本語ローカル LLM『LightChatAssistant-TypeB』による、簡単なノベル生成アシスタントです。ローカル特権の永続生成 Generate forever で、当たりガチャを積み上げます。読み上げにも対応。
 * [clip-japanese](https://github.com/sonoisa/clip-japanese) - 日本語CLIPモデル
 * [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) - Rime IMEのための日本語ローマ字入力スキーマ
 * [deep-question-generation](https://github.com/sonoisa/deep-question-generation) - 深層学習を用いたクイズ自動生成（日本語T5モデル）
 * [magpie-nemotron](https://github.com/aratako/magpie-nemotron) - Magpieという手法とNemotron-4-340B-Instructを用いて合成対話データセットを作るコード
 * [qlora_ja](https://github.com/sosuke115/qlora_ja) - 日本語データセットでのqlora instruction tuning学習サンプルコード
 * [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) - Mozc UT Jawiki辞書は、Mozc用に日本語のWikipediaから生成された辞書です。
 * [shisa-v2](https://github.com/shisa-ai/shisa-v2) - 日本語/英語バイリンガルLLM
 * [llm-translator](https://github.com/hpprc/llm-translator) - ミクストラルベースの日英（英日）翻訳モデル
 * [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) - Whisperのデコーダをllm-jp-1.3b-v1.0に置き換えた音声認識モデルを学習させるためのコード
 * [rag-japanese](https://github.com/akimfromparis/rag-japanese) - 日本の低リソース環境でのLLM向けのラマ指数付きのオープンソースRAG
 * [monaka](https://github.com/komiya-lab/monaka) - 日本語パーサー（歴史的な日本語を含む）
 * [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) - 最新のNMT研究に基づいた最先端のオープンソース日本語<-->英語機械翻訳システム。
 * [substring-word-finder](https://github.com/toufu-24/substring-word-finder) - 連続部分文字列の単語判定を行います
 * [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) - このプロジェクトは、さまざまなビジョン言語モデル（VLMs）のパフォーマンスを評価および比較するためのベンチマークツールです。モデルのパフォーマンスを測定するために、LLaVA-Bench-In-the-WildとJapanese HERON Benchの2つのデータセットを使用しています。
 * [text2dataset](https://github.com/llm-jp/text2dataset) - 簡単に大きな英語テキストデータセットを日本語テキストデータセットに変換できます。オープンLLMsを使用してください。
 * [mecab-web-api](https://github.com/bungoume/mecab-web-api) - MeCabを利用した日本語形態素解析WebAPI
 * [mecab_controller](https://github.com/ajatt-tools/mecab_controller) - ふりがな読みを生成するためのMecabラッパー
 * [vits](https://github.com/zassou65535/vits) - VITSによるテキスト読み上げ器&ボイスチェンジャー
 * [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) - 音声認識、文章生成、音声合成を使って対話するチャットボットアプリ
 * [kudasai](https://github.com/bikatr7/kudasai) - 高度な前処理と統合された翻訳技術を活用して、日本語-英語翻訳を効率化する
 * [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) - MeCabの形態素解析結果を可視化するツール
 * [add-dictionary](https://github.com/massao000/add-dictionary) - OpenJTalkのユーザ辞書をGUIで追加するアプリ
 * [j-moshi](https://github.com/nu-dialogue/j-moshi) - J-Moshi: 日本語のフルデュプレックス音声対話システム
 * [jatts](https://github.com/unilight/jatts) - JATTS: 日本語TTS（研究用）
 * [tsukasa-speech](https://github.com/respaired/tsukasa-speech) - フロンティア日本語音声生成ネットワーク
 * [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) - ElasticsearchやGiNZA、患者表現辞書を使った患者表現揺れ吸収する意味構造検索を試したエラスティックサーチやGiNZA、患者表現辞書を使用して患者表現の揺れを吸収する意味構造検索を試してみました。
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 生成自動評価を行うためのPythonツール
 * [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) - Colaboratory上でAsagi(合成データセットを活用した大規模日本語VLM)をお試しするサンプル
 * [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) - このツールは、複数のデータセットにわたって日本語のマルチモーダル大規模言語モデルを自動的に評価します。
 * [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) - 生成自動評価を行うためのPythonツール
 * [manga109api](https://github.com/manga109/manga109api) - Manga109の注釈データを読むためのシンプルなPython API
 * [fastrtc-jp](https://github.com/route250/fastrtc-jp) - fastrtc用の日本語TTSとSTT追加キット
 * [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) - Pythonを使用したWhisperモデルによる音声文字起こしツール
 * [pocket-researcher](https://github.com/u-masao/pocket-researcher) - LLMを活用した自律調査エージェント。手軽に情報収集、概要把握。
 * [jtransbench](https://github.com/webbigdata-jp/jtransbench) - 日本語翻訳スキルを簡単にベンチマークするためのツール
 * [easyllasa](https://github.com/zuntan03/easyllasa) - EasyLlasa は 5～15秒の日本語音声と日本語テキストから日本語音声を生成する TSTS (TextSpeechToSpeech) です。
 * [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) - 氏名漢字カナ突合モデル
 * [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) - OpenReview論文を自動で発見・分析する日本語対応AIエージェント
 * [pitchbench](https://github.com/shewiiii/pitchbench) - 実験的な日本語ピッチアクセントに基づくLLMベンチマーク
 * [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) - ゼロから日本語への英語変換器
 * [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) - VOICEVOXのコア内で用いられているディープラーニングモデルの推論コード
 * [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) - pyopenjtalk-plus: 追加の改善を加えたOpenJTalkのPythonラッパー
 * [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) - 日本語のスペル修正
 * [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) - python 顔文字
 * [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) - このリポジトリには、VILAリポジトリから変更されたllm-jp/llm-jp-3-vila-14bのトレーニングコードが含まれています。
 * [kanjivg-radical](https://github.com/yagays/kanjivg-radical) - kanjivg-radical漢字VGラジカル
 * [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) - このプロジェクトは、Djangoで構築されたWebアプリケーションを使用して日本語ワードネットを可視化します。
 * [piper-plus](https://github.com/ayutaz/piper-plus) - 日本語サポート、WebAssembly、マルチGPUトレーニング、品質向上を備えた強化されたパイパーTTS。
 * [Japanera](https://github.com/nagataaaas/Japanera) - 日本の元号システムのための簡単なツール
 * [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) - BERTを使用した日本語文章要約
 * [kyujipy](https://github.com/drturnon/kyujipy) - 新字体（Shinjitai）から旧字体（Kyujitai）へ、またはその逆に日本語テキストを変換するためのPythonライブラリ
 * [jitenbot](https://github.com/konstantindjairo/jitenbot) - 日本語辞書の個人用コピーを作成するためのWebクローラー
 * [ja-icd10](https://github.com/yagays/ja-icd10) - ICD-10 国際疾病分類の日本語情報を扱うためのPythonパッケージ
 * [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) - 音素レベルの日本語BERTを使用したVITS2
 * [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) - NDCPredictorの機械学習モデル（書誌情報から日本十進分類を推測するfastTextの学習済みモデル）
 * [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) - pfmt-bench-fin-ja: 日本語金融向けの優先マルチターンベンチマーク
 * [marine-plus](https://github.com/tsukumijima/marine-plus) - MARINE：マルチタスク学習ベースの日本語アクセント推定（Windowsもサポート）
 * [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) - Pythonでのさまざまな日本語トークナイザーの速度を比較してください。
 * [yat](https://github.com/yagays/yat) - yat：日本語NLPのためのもう1つのトークナイザーyat：日本語NLPのためのもう1つのトークナイザー
 * [igakuqa119](https://github.com/docto-rin/igakuqa119) - 第119回日本医師免許試験におけるLLMの評価
 * [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) - TransformersのRemBertTokenizerFastを使用した日本語長単位ワードトークナイザー
 * [ibus-jig](https://github.com/y-koj/ibus-jig) - 入力: ibus-jig：GPT-4を使用した日本語入力法
 * [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) - カスタマイズ可能なルールに基づいて日本語テキストからストップワードをフィルタリングするために設計された軽量なPythonライブラリ。
 * [yasumail](https://github.com/terallite/yasumail) - MLトレーニングデータ用の合成日本語ビジネスメールジェネレータ
 * [himotoki](https://github.com/msr2903/himotoki) - Pythonベースの日本語トークナイザー、辞書、形態素解析ツール、ローマ字変換ツール。言語学習用のJMDictに基づいています。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [namedivider-python](https://github.com/rskmoi/namedivider-python) | 📥 423 | 📦 77k | ⭐ 251 | 🟢 november 2025|
| 🔗 [asa-python](https://github.com/ikegami-yukino/asa-python) | 📥 55 | 📦 30k | ⭐ 11 | 🔴 february 2019|
| 🔗 [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) | - | - | ⭐ 22 | 🔴 january 2020|
| 🔗 [toiro](https://github.com/taishi-i/toiro) | 📥 47 | 📦 26k | ⭐ 120 | 🟢 november 2025|
| 🔗 [ja-timex](https://github.com/yagays/ja-timex) | 📥 580 | 📦 88k | ⭐ 140 | 🔴 november 2023|
| 🔗 [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) | - | - | ⭐ 137 | 🔴 march 2019|
| 🔗 [daaja](https://github.com/kajyuuen/daaja) | 📥 53 | 📦 25k | ⭐ 64 | 🔴 february 2023|
| 🔗 [accel-brain-code](https://github.com/accel-brain/accel-brain-code) | 📥 287 | 📦 148k | ⭐ 320 | 🔴 december 2023|
| 🔗 [JGLUE](https://github.com/yahoojapan/JGLUE) | - | - | ⭐ 333 | 🟡 march 2025|
| 🔗 [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) | 📥 753 | 📦 48k | ⭐ 10 | 🔴 june 2024|
| 🔗 [nlplot](https://github.com/takapy0210/nlplot) | 📥 169 | 📦 108k | ⭐ 240 | 🔴 september 2022|
| 🔗 [rake-ja](https://github.com/kanjirz50/rake-ja) | - | - | ⭐ 21 | 🔴 october 2018|
| 🔗 [jel](https://github.com/izuna385/jel) | 📥 18 | 📦 8k | ⭐ 11 | 🔴 july 2021|
| 🔗 [MedNER-J](https://github.com/sociocom/MedNER-J) | - | - | ⭐ 18 | 🔴 may 2022|
| 🔗 [zunda-python](https://github.com/ikegami-yukino/zunda-python) | 📥 11 | 📦 6k | ⭐ 10 | 🔴 november 2019|
| 🔗 [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) | - | - | ⭐ 16 | 🔴 january 2022|
| 🔗 [showcase](https://github.com/cl-tohoku/showcase) | 📥 14 | 📦 7k | ⭐ 6 | 🔴 june 2018|
| 🔗 [darts-clone-python](https://github.com/rixwew/darts-clone-python) | 📥 3k | 📦 9M | ⭐ 20 | 🔴 april 2022|
| 🔗 [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) | - | - | ⭐ 3 | 🔴 november 2021|
| 🔗 [desuwa](https://github.com/megagonlabs/desuwa) | 📥 17 | 📦 10k | ⭐ 6 | 🔴 may 2022|
| 🔗 [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) | - | - | ⭐ 278 | 🔴 may 2016|
| 🔗 [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) | - | - | ⭐ 65 | 🔴 april 2021|
| 🔗 [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) | - | - | ⭐ 26 | 🔴 june 2019|
| 🔗 [DNorm-J](https://github.com/sociocom/DNorm-J) | - | - | ⭐ 9 | 🔴 june 2022|
| 🔗 [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) | 📥 162 | 📦 65k | ⭐ 9 | 🔴 september 2022|
| 🔗 [ishi](https://github.com/ku-nlp/ishi) | 📥 13 | 📦 6k | ⭐ 2 | 🔴 may 2020|
| 🔗 [python-npylm](https://github.com/musyoku/python-npylm) | - | - | ⭐ 34 | 🔴 january 2019|
| 🔗 [python-npycrf](https://github.com/musyoku/python-npycrf) | - | - | ⭐ 11 | 🔴 march 2018|
| 🔗 [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) | - | - | ⭐ 16 | 🔴 october 2017|
| 🔗 [negima](https://github.com/cocodrips/negima) | 📥 18 | 📦 16k | ⭐ 14 | 🔴 august 2018|
| 🔗 [YouyakuMan](https://github.com/neilctwu/YouyakuMan) | - | - | ⭐ 52 | 🔴 september 2020|
| 🔗 [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) | 📥 593 | 📦 2M | ⭐ 21 | 🔴 april 2020|
| 🔗 [kantan](https://github.com/itayperl/kantan) | - | - | ⭐ 8 | 🔴 october 2024|
| 🔗 [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) | - | - | ⭐ 40 | 🔴 september 2017|
| 🔗 [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) | - | - | ⭐ 10 | 🔴 august 2022|
| 🔗 [chirptext](https://github.com/letuananh/chirptext) | 📥 634 | 📦 190k | ⭐ 7 | 🔴 october 2022|
| 🔗 [yubin](https://github.com/alvations/yubin) | 📥 5 | 📦 3k | ⭐ 3 | 🔴 october 2019|
| 🔗 [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) | 📥 86 | 📦 24k | ⭐ 6 | 🔴 february 2021|
| 🔗 [japanese2phoneme](https://github.com/iory/japanese2phoneme) | 📥 12 | 📦 4k | ⭐ 1 | 🔴 february 2022|
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
| 🔗 [Grongish](https://github.com/shogo82148/Grongish) | - | - | ⭐ 25 | 🟢 december 2025|
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
| 🔗 [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) | 📥 135k | 📦 171k | ⭐ repo not found | 🔴 november 2015|
| 🔗 [AugLy-jp](https://github.com/chck/AugLy-jp) | 📥 126 | 📦 30k | ⭐ 7 | 🔴 september 2021|
| 🔗 [furigana4epub](https://github.com/Mumumu4/furigana4epub) | 📥 22 | 📦 12k | ⭐ 29 | 🔴 september 2021|
| 🔗 [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) | 📥 96 | 📦 19k | ⭐ 12 | 🟡 march 2025|
| 🔗 [jageocoder](https://github.com/t-sagara/jageocoder) | 📥 2k | 📦 313k | ⭐ 93 | 🟡 september 2025|
| 🔗 [pygeonlp](https://github.com/geonlp-platform/pygeonlp) | 📥 236 | 📦 20k | ⭐ 22 | 🟡 october 2025|
| 🔗 [nksnd](https://github.com/yoriyuki/nksnd) | - | - | ⭐ 26 | 🔴 may 2018|
| 🔗 [JaMIE](https://github.com/racerandom/JaMIE) | - | - | ⭐ 9 | 🔴 may 2023|
| 🔗 [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) | - | - | ⭐ 48 | 🔴 august 2017|
| 🔗 [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) | - | - | ⭐ 19 | 🔴 july 2019|
| 🔗 [5ch-analysis](https://github.com/GINK03/5ch-analysis) | - | - | ⭐ 75 | 🔴 november 2018|
| 🔗 [tweet_extructor](https://github.com/tatHi/tweet_extructor) | - | - | ⭐ 3 | 🔴 august 2022|
| 🔗 [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) | - | - | ⭐ 2 | 🔴 august 2018|
| 🔗 [jinf](https://github.com/hkiyomaru/jinf) | 📥 122 | 📦 54k | ⭐ 4 | 🔴 december 2022|
| 🔗 [kwja](https://github.com/ku-nlp/kwja) | 📥 253 | 📦 54k | ⭐ 138 | 🟡 august 2025|
| 🔗 [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) | - | - | ⭐ 6 | 🔴 december 2022|
| 🔗 [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) | - | - | ⭐ 12 | 🔴 october 2022|
| 🔗 [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) | - | - | ⭐ 2 | 🔴 october 2022|
| 🔗 [cihai](https://github.com/cihai/cihai) | 📥 514 | 📦 208k | ⭐ 93 | 🟢 yesterday|
| 🔗 [marine](https://github.com/6gsn/marine) | 📥 76 | 📦 15k | ⭐ 36 | 🔴 september 2022|
| 🔗 [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) | - | - | ⭐ 32 | 🔴 december 2022|
| 🔗 [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [radicalchar](https://github.com/yamamaya/radicalchar) | - | - | ⭐ 8 | 🔴 december 2022|
| 🔗 [akaza](https://github.com/tokuhirom/akaza) | - | - | ⭐ 228 | 🟢 today|
| 🔗 [posuto](https://github.com/polm/posuto) | 📥 5k | 📦 645k | ⭐ 225 | 🟢 february|
| 🔗 [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) | - | - | ⭐ 269 | 🔴 september 2022|
| 🔗 [ibus-hiragana](https://github.com/esrille/ibus-hiragana) | - | - | ⭐ 77 | 🟢 november 2025|
| 🔗 [furiganapad](https://github.com/esrille/furiganapad) | - | - | ⭐ 19 | 🟡 april 2025|
| 🔗 [chikkarpy](https://github.com/WorksApplications/chikkarpy) | 📥 330 | 📦 57k | ⭐ 55 | 🔴 february 2022|
| 🔗 [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) | - | - | ⭐ 36 | 🔴 may 2022|
| 🔗 [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) | - | - | ⭐ 183 | 🔴 october 2024|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [shuwa](https://github.com/google/shuwa) | - | - | ⭐ 144 | 🔴 december 2022|
| 🔗 [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) | - | - | ⭐ 5 | 🔴 october 2022|
| 🔗 [tra-fugu](https://github.com/tos-kamiya/tra-fugu) | - | - | ⭐ 6 | 🔴 march 2023|
| 🔗 [fugumt](https://github.com/s-taka/fugumt) | - | - | ⭐ 65 | 🔴 february 2021|
| 🔗 [JaSPICE](https://github.com/keio-smilab23/JaSPICE) | 📥 8 | 📦 2k | ⭐ 9 | 🔴 november 2023|
| 🔗 [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) | - | - | ⭐ 48 | 🔴 april 2023|
| 🔗 [pyopenjtalk](https://github.com/r9y9/pyopenjtalk) | 📥 12k | 📦 1M | ⭐ 242 | 🟡 april 2025|
| 🔗 [yomigana-ebook](https://github.com/rabbit19981023/yomigana-ebook) | 📥 37 | 📦 7k | ⭐ 25 | 🔴 february 2024|
| 🔗 [N46Whisper](https://github.com/Ayanaminn/N46Whisper) | - | - | ⭐ 1.7k | 🟡 february 2025|
| 🔗 [japanese_llm_simple_webui](https://github.com/noir55/japanese_llm_simple_webui) | - | - | ⭐ 17 | 🔴 may 2024|
| 🔗 [pdf-translator](https://github.com/discus0434/pdf-translator) | - | - | ⭐ 337 | 🔴 may 2024|
| 🔗 [japanese_qa_demo_with_haystack_and_es](https://github.com/Shingo-Kamata/japanese_qa_demo_with_haystack_and_es) | - | - | ⭐ 1 | 🔴 december 2022|
| 🔗 [mozc-devices](https://github.com/google/mozc-devices) | - | - | ⭐ 2.7k | 🟢 november 2025|
| 🔗 [natsume](https://github.com/faruzan0820/natsume) | 📥 23 | 📦 3k | ⭐ repo not found | 🔴 repo not found|
| 🔗 [vits-japros-webui](https://github.com/litagin02/vits-japros-webui) | - | - | ⭐ 42 | 🔴 january 2024|
| 🔗 [ja-law-parser](https://github.com/takuyaa/ja-law-parser) | - | - | ⭐ 25 | 🔴 january 2024|
| 🔗 [dictation-kit](https://github.com/julius-speech/dictation-kit) | - | - | ⭐ 164 | 🔴 april 2019|
| 🔗 [julius4seg](https://github.com/Hiroshiba/julius4seg) | - | - | ⭐ 7 | 🔴 august 2021|
| 🔗 [voicevox_engine](https://github.com/VOICEVOX/voicevox_engine) | - | - | ⭐ 1.6k | 🟢 january|
| 🔗 [LLaVA-JP](https://github.com/tosiyuki/LLaVA-JP) | - | - | ⭐ 64 | 🔴 june 2024|
| 🔗 [RAG-Japanese](https://github.com/AkimParis/RAG-Japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [bertjsc](https://github.com/er-ri/bertjsc) | - | - | ⭐ 14 | 🔴 august 2024|
| 🔗 [llm-leaderboard](https://github.com/wandb/llm-leaderboard) | - | - | ⭐ 91 | 🟡 september 2025|
| 🔗 [jglue-evaluation-scripts](https://github.com/nobu-g/jglue-evaluation-scripts) | - | - | ⭐ 18 | 🟢 february|
| 🔗 [BLIP2-Japanese](https://github.com/ZhaoPeiduo/BLIP2-Japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [wikipedia-passages-jawiki-embeddings-utils](https://github.com/hotchpotch/wikipedia-passages-jawiki-embeddings-utils) | - | - | ⭐ 11 | 🔴 march 2024|
| 🔗 [simple-simcse-ja](https://github.com/hpprc/simple-simcse-ja) | - | - | ⭐ 68 | 🔴 october 2023|
| 🔗 [wikipedia-japanese-open-rag](https://github.com/lawofcycles/wikipedia-japanese-open-rag) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [gpt4-autoeval](https://github.com/northern-system-service/gpt4-autoeval) | - | - | ⭐ 16 | 🔴 june 2024|
| 🔗 [t5-japanese](https://github.com/sonoisa/t5-japanese) | - | - | ⭐ 116 | 🟡 september 2025|
| 🔗 [japanese_llm_eval](https://github.com/lightblue-tech/japanese_llm_eval) | - | - | ⭐ 5 | 🔴 april 2024|
| 🔗 [jmteb](https://github.com/sbintuitions/jmteb) | - | - | ⭐ 84 | 🟢 november 2025|
| 🔗 [pydomino](https://github.com/dwangomediavillage/pydomino) | - | - | ⭐ 36 | 🟡 august 2025|
| 🔗 [easynovelassistant](https://github.com/zuntan03/easynovelassistant) | - | - | ⭐ 216 | 🔴 july 2024|
| 🔗 [clip-japanese](https://github.com/sonoisa/clip-japanese) | - | - | ⭐ 13 | 🟡 september 2025|
| 🔗 [rime-jaroomaji](https://github.com/lazyfoxchan/rime-jaroomaji) | - | - | ⭐ 46 | 🟢 last thursday|
| 🔗 [deep-question-generation](https://github.com/sonoisa/deep-question-generation) | - | - | ⭐ 12 | 🔴 march 2023|
| 🔗 [magpie-nemotron](https://github.com/aratako/magpie-nemotron) | - | - | ⭐ 8 | 🔴 july 2024|
| 🔗 [qlora_ja](https://github.com/sosuke115/qlora_ja) | - | - | ⭐ 1 | 🔴 july 2024|
| 🔗 [mozcdic-ut-jawiki](https://github.com/utuhiro78/mozcdic-ut-jawiki) | - | - | ⭐ 26 | 🟢 last tuesday|
| 🔗 [shisa-v2](https://github.com/shisa-ai/shisa-v2) | - | - | ⭐ 28 | 🟢 december 2025|
| 🔗 [llm-translator](https://github.com/hpprc/llm-translator) | - | - | ⭐ 20 | 🔴 january 2025|
| 🔗 [llm-jp-asr](https://github.com/tosiyuki/llm-jp-asr) | - | - | ⭐ 9 | 🔴 september 2024|
| 🔗 [rag-japanese](https://github.com/akimfromparis/rag-japanese) | - | - | ⭐ 10 | 🟡 may 2025|
| 🔗 [monaka](https://github.com/komiya-lab/monaka) | - | - | ⭐ 4 | 🔴 january 2025|
| 🔗 [jp-translate.cloud](https://github.com/matthewbieda/jp-translate.cloud) | - | - | ⭐ 3 | 🔴 september 2024|
| 🔗 [substring-word-finder](https://github.com/toufu-24/substring-word-finder) | - | - | ⭐ 4 | 🟢 november 2025|
| 🔗 [heron-vlm-leaderboard](https://github.com/wandb/heron-vlm-leaderboard) | - | - | ⭐ 6 | 🔴 december 2024|
| 🔗 [text2dataset](https://github.com/llm-jp/text2dataset) | - | - | ⭐ 25 | 🔴 january 2025|
| 🔗 [mecab-web-api](https://github.com/bungoume/mecab-web-api) | - | - | ⭐ 40 | 🔴 july 2022|
| 🔗 [mecab_controller](https://github.com/ajatt-tools/mecab_controller) | - | - | ⭐ 17 | 🟢 january|
| 🔗 [vits](https://github.com/zassou65535/vits) | - | - | ⭐ 91 | 🔴 february 2023|
| 🔗 [akari_chatgpt_bot](https://github.com/akarigroup/akari_chatgpt_bot) | - | - | ⭐ 48 | 🟡 october 2025|
| 🔗 [kudasai](https://github.com/bikatr7/kudasai) | - | - | ⭐ 26 | 🟡 june 2025|
| 🔗 [mecab-visualizer](https://github.com/sophiefy/mecab-visualizer) | - | - | ⭐ 2 | 🔴 september 2023|
| 🔗 [add-dictionary](https://github.com/massao000/add-dictionary) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [j-moshi](https://github.com/nu-dialogue/j-moshi) | - | - | ⭐ 295 | 🟡 june 2025|
| 🔗 [jatts](https://github.com/unilight/jatts) | - | - | ⭐ 44 | 🟡 may 2025|
| 🔗 [tsukasa-speech](https://github.com/respaired/tsukasa-speech) | - | - | ⭐ 60 | 🟡 may 2025|
| 🔗 [symptom-expression-search](https://github.com/po3rin/symptom-expression-search) | - | - | ⭐ 2 | 🔴 february 2021|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 38 | 🟢 december 2025|
| 🔗 [asagi-vlm-colaboratory-sample](https://github.com/kazuhito00/asagi-vlm-colaboratory-sample) | - | - | ⭐ 1 | 🟡 march 2025|
| 🔗 [llm-jp-eval-mm](https://github.com/llm-jp/llm-jp-eval-mm) | - | - | ⭐ 41 | 🟢 january|
| 🔗 [llm-jp-judge](https://github.com/llm-jp/llm-jp-judge) | - | - | ⭐ 38 | 🟢 december 2025|
| 🔗 [manga109api](https://github.com/manga109/manga109api) | 📥 146 | 📦 45k | ⭐ 128 | 🔴 march 2022|
| 🔗 [fastrtc-jp](https://github.com/route250/fastrtc-jp) | - | - | ⭐ 5 | 🟡 may 2025|
| 🔗 [whisper-transcription](https://github.com/fumifumi0831/whisper-transcription) | - | - | ⭐ 15 | 🟢 january|
| 🔗 [pocket-researcher](https://github.com/u-masao/pocket-researcher) | - | - | ⭐ 11 | 🟡 april 2025|
| 🔗 [jtransbench](https://github.com/webbigdata-jp/jtransbench) | - | - | ⭐ 13 | 🟡 october 2025|
| 🔗 [easyllasa](https://github.com/zuntan03/easyllasa) | - | - | ⭐ 25 | 🟡 september 2025|
| 🔗 [kanjikana-model](https://github.com/digital-go-jp/kanjikana-model) | - | - | ⭐ 111 | 🟢 december 2025|
| 🔗 [deep-openreview-research-ja](https://github.com/tb-yasu/deep-openreview-research-ja) | - | - | ⭐ 13 | 🟢 november 2025|
| 🔗 [pitchbench](https://github.com/shewiiii/pitchbench) | - | - | ⭐ 1 | 🟢 december 2025|
| 🔗 [mini-transformer-from-scratch](https://github.com/zuofanf/mini-transformer-from-scratch) | - | - | ⭐ 2 | 🟢 november 2025|
| 🔗 [vv_core_inference](https://github.com/hiroshiba/vv_core_inference) | - | - | ⭐ 31 | 🟢 december 2025|
| 🔗 [pyopenjtalk-plus](https://github.com/tsukumijima/pyopenjtalk-plus) | 📥 3k | 📦 291k | ⭐ 55 | 🟢 november 2025|
| 🔗 [japanese_spelling_correction](https://github.com/phkhanhtrinh23/japanese_spelling_correction) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [py-kaomoji](https://github.com/shibuiwilliam/py-kaomoji) | 📥 47 | 📦 37k | ⭐ 6 | 🔴 december 2018|
| 🔗 [llm-jp-vila](https://github.com/llm-jp/llm-jp-vila) | - | - | ⭐ 10 | 🟡 august 2025|
| 🔗 [kanjivg-radical](https://github.com/yagays/kanjivg-radical) | - | - | ⭐ 105 | 🔴 august 2018|
| 🔗 [japanese-wordnet-visualization](https://github.com/HemingwayLee/japanese-wordnet-visualization) | - | - | ⭐ 3 | 🔴 november 2022|
| 🔗 [piper-plus](https://github.com/ayutaz/piper-plus) | - | - | ⭐ 28 | 🟢 february|
| 🔗 [Japanera](https://github.com/nagataaaas/Japanera) | 📥 2k | 📦 339k | ⭐ 35 | 🟡 june 2025|
| 🔗 [bert-abstractive-text-summarization](https://github.com/iwasakiyuuki/bert-abstractive-text-summarization) | - | - | ⭐ 49 | 🔴 december 2019|
| 🔗 [kyujipy](https://github.com/drturnon/kyujipy) | 📥 49 | 📦 22k | ⭐ 21 | 🟢 january|
| 🔗 [jitenbot](https://github.com/konstantindjairo/jitenbot) | - | - | ⭐ 4 | 🔴 december 2024|
| 🔗 [ja-icd10](https://github.com/yagays/ja-icd10) | - | - | ⭐ 5 | 🔴 july 2021|
| 🔗 [pl-bert-vits2](https://github.com/tonnetonne814/pl-bert-vits2) | - | - | ⭐ 14 | 🔴 december 2023|
| 🔗 [ndc_predictor](https://github.com/ndl-lab/ndc_predictor) | - | - | ⭐ 11 | 🔴 august 2021|
| 🔗 [pfmt-bench-fin-ja](https://github.com/pfnet-research/pfmt-bench-fin-ja) | - | - | ⭐ 9 | 🟡 march 2025|
| 🔗 [marine-plus](https://github.com/tsukumijima/marine-plus) | 📥 38 | 📦 11k | ⭐ 8 | 🟡 october 2025|
| 🔗 [ja-tokenizer-benchmark](https://github.com/polm/ja-tokenizer-benchmark) | - | - | ⭐ 7 | 🔴 february 2022|
| 🔗 [yat](https://github.com/yagays/yat) | - | - | ⭐ 7 | 🔴 june 2018|
| 🔗 [igakuqa119](https://github.com/docto-rin/igakuqa119) | - | - | ⭐ 7 | 🟢 january|
| 🔗 [japanese-luw-tokenizer](https://github.com/koichiyasuoka/japanese-luw-tokenizer) | - | - | ⭐ 6 | 🔴 december 2021|
| 🔗 [ibus-jig](https://github.com/y-koj/ibus-jig) | - | - | ⭐ 4 | 🔴 december 2023|
| 🔗 [jp-stopword-filter](https://github.com/BrambleXu/jp-stopword-filter) | 📥 36 | 📦 5k | ⭐ 3 | 🔴 november 2024|
| 🔗 [yasumail](https://github.com/terallite/yasumail) | - | - | ⭐ 2 | 🟢 january|
| 🔗 [himotoki](https://github.com/msr2903/himotoki) | 📥 434 | 📦 3k | ⭐ 2 | 🟢 yesterday|


## C++

### Morphology analysis
高速な日本語形態素解析を行うライブラリ

 * [mecab](https://github.com/taku910/mecab) - もう一つの日本語形態素解析器
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++（形態素解析ツールキット）
 * [kytea](https://github.com/neubig/kytea) - 京都テキスト分析ツールキット：単語分割や発音推定などに使用されます。
 * [juman](https://github.com/ku-nlp/juman) - 日本語形態素解析システムJUMAN


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab](https://github.com/taku910/mecab) | - | - | ⭐ 1.1k | 🟡 february 2025|
| 🔗 [jumanpp](https://github.com/ku-nlp/jumanpp) | - | - | ⭐ 407 | 🔴 march 2023|
| 🔗 [kytea](https://github.com/neubig/kytea) | - | - | ⭐ 212 | 🔴 april 2020|
| 🔗 [juman](https://github.com/ku-nlp/juman) | - | - | ⭐ 11 | 🔴 december 2021|

### Parsing
日本語の文法構造や係り受けを解析するライブラリ

 * [cabocha](https://github.com/taku910/cabocha) - もう一つの日本語依存構造解析ツール
 * [knp](https://github.com/ku-nlp/knp) - 日本語パーサー


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [cabocha](https://github.com/taku910/cabocha) | - | - | ⭐ 121 | 🟡 february 2025|
| 🔗 [knp](https://github.com/ku-nlp/knp) | - | - | ⭐ 33 | 🔴 november 2023|

### Others
その他の日本語NLP関連ライブラリ

 * [jsc](https://github.com/yohokuno/jsc) - 日本語の仮名漢字変換、中国語のピンイン入力、CJE混合入力のための共通ソースチャネルモデル。
 * [aquaskk](https://github.com/codefirst/aquaskk) - 形態素解析を行わない入力方法。
 * [mozc](https://github.com/google/mozc) - Mozc - マルチプラットフォームに対応した日本語入力システムエディター
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch：（完全|接頭辞|近似）文字列マッチングライブラリ
 * [resembla](https://github.com/tuem/resembla) - Resembla：単語ベースの日本語類似文検索ライブラリ
 * [corvusskk](https://github.com/nathancorvussolis/corvusskk) - ▽▼ Windows用のSKK風日本語入力エディタ
 * [mozuku](https://github.com/t3tra-dev/mozuku) - 日本語文章の解析・校正を行う LSP サーバー。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jsc](https://github.com/yohokuno/jsc) | - | - | ⭐ 15 | 🔴 december 2012|
| 🔗 [aquaskk](https://github.com/codefirst/aquaskk) | - | - | ⭐ 367 | 🔴 july 2023|
| 🔗 [mozc](https://github.com/google/mozc) | - | - | ⭐ 2.8k | 🟢 january|
| 🔗 [trimatch](https://github.com/tuem/trimatch) | - | - | ⭐ 2 | 🟢 last friday|
| 🔗 [resembla](https://github.com/tuem/resembla) | - | - | ⭐ 73 | 🟡 august 2025|
| 🔗 [corvusskk](https://github.com/nathancorvussolis/corvusskk) | - | - | ⭐ 351 | 🟢 january|
| 🔗 [mozuku](https://github.com/t3tra-dev/mozuku) | - | - | ⭐ 400 | 🟢 december 2025|


## Rust crate

### Morphology analysis
Rustで実装された日本語形態素解析ライブラリ

 * [lindera](https://github.com/lindera-morphology/lindera) - 形態素解析ライブラリ。
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto：非常に加速されたポイントワイズ予測に基づくトークナイザー
 * [goya](https://github.com/Leko/goya) - Rustで書かれた日本語形態素解析
 * [vibrato](https://github.com/daac-tools/vibrato) - バイブラート：Viterbiベースの高速トークナイザー
 * [yoin](https://github.com/agatan/yoin) - 純粋なRustで書かれた日本語形態素解析器
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 「mecab」の安全なRustバインディング。品詞と形態素解析ライブラリ。
 * [awabi](https://github.com/nakagami/awabi) - MeCab辞書を使用する形態素解析器
 * [kanpyo](https://github.com/togatoga/kanpyo) - Rustで書かれた日本語形態素解析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera](https://github.com/lindera-morphology/lindera) | - | 📦 849k | ⭐ 592 | 🟢 last tuesday|
| 🔗 [vaporetto](https://github.com/daac-tools/vaporetto) | - | 📦 168k | ⭐ 251 | 🟢 last saturday|
| 🔗 [goya](https://github.com/Leko/goya) | - | 📦 11k | ⭐ 82 | 🔴 december 2021|
| 🔗 [vibrato](https://github.com/daac-tools/vibrato) | - | 📦 55k | ⭐ 397 | 🟢 last saturday|
| 🔗 [yoin](https://github.com/agatan/yoin) | - | 📦 3k | ⭐ 26 | 🔴 october 2017|
| 🔗 [mecab-rs](https://github.com/tsurai/mecab-rs) | - | 📦 39k | ⭐ 66 | 🔴 september 2023|
| 🔗 [awabi](https://github.com/nakagami/awabi) | - | 📦 24k | ⭐ 10 | 🟢 november 2025|
| 🔗 [kanpyo](https://github.com/togatoga/kanpyo) | - | 📦 2.5k | ⭐ 107 | 🟢 january|


### Converter
日本語の文字や仮名を変換するライブラリ

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 日本語の文字（ひらがな、カタカナ）とローマ字の間の変換とチェックを行うためのユーティリティライブラリ。
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 日本語の半角カナと全角英数字を通常の文字に変換するためのRustライブラリ
 * [kana](https://github.com/gbrlsnchs/kana) - [ミラー] ローマ字テキストをひらがなまたはカタカナに変換するためのCLIプログラム
 * [kanaria](https://github.com/samunohito/kanaria) - このライブラリは、ひらがな・カタカナ、半角・全角の相互変換や判別を始めとした機能を提供します。
 * [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) - 日本の住所を都道府県/市区町村/町名/その他に分割するライブラリです
 * [yosina](https://github.com/yosina-lib/yosina) - Yosinaは、日本語の文章で使用される文字や記号を取り扱う転写ライブラリです。
 * [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) - 日本語半角と全角文字の高速変換を行うRust実装、mojimoji。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) | - | 📦 292k | ⭐ 88 | 🟡 march 2025|
| 🔗 [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) | - | 📦 61k | ⭐ 19 | 🔴 april 2020|
| 🔗 [kana](https://github.com/gbrlsnchs/kana) | - | - | ⭐ 12 | 🔴 january 2023|
| 🔗 [kanaria](https://github.com/samunohito/kanaria) | - | - | ⭐ 21 | 🔴 december 2024|
| 🔗 [japanese-address-parser](https://github.com/yuukitoriyama/japanese-address-parser) | - | - | ⭐ 10 | 🟢 november 2025|
| 🔗 [yosina](https://github.com/yosina-lib/yosina) | - | - | ⭐ 20 | 🟡 september 2025|
| 🔗 [mojimoji-rs](https://github.com/europeanplaice/mojimoji-rs) | - | - | ⭐ 4 | 🔴 november 2022|


### Search engine library
日本語全文検索のためのライブラリ

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Tantivy用のLinderaトークナイザー。
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - Vibratoを使用したTantivyトークナイザー。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) | - | 📦 158k | ⭐ 67 | 🟢 january|
| 🔗 [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) | - | 📦 1.5k | ⭐ 3 | 🔴 january 2023|


### Others
日本語処理やIMEを扱う補助ライブラリ

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
 * [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) - 裁判例のデータ一覧を裁判所のホームページ(https://www.courts.go.jp/index.html) をスクレイピングして生成するソフトウェア
 * [jisho](https://github.com/eagleflo/jisho) - Jishoは、日本語-英語辞書を提供するCLIツールおよびRustライブラリです。Jishoは、日本語-英語辞書を提供するCLIツール＆Rustライブラリです。
 * [kanalizer](https://github.com/voicevox/kanalizer) - 英単語から読みを推測するライブラリ。
 * [koharu](https://github.com/mayocream/koharu) - Rustで書かれたLLMを使用した自動漫画翻訳ツール。
 * [yomine](https://github.com/mcgrizzz/yomine) - 言語学習者が新しい単語や表現を見つけるのを手助けするために設計された日本語語彙マイニングツール。
 * [matsuba](https://github.com/mrpicklepinosaur/matsuba) - 軽量な日本語IMEをRustで書かれました。
 * [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) - Rustによる日本語辞書、Telegramボット、AWS Lambda、Cloudflare Workersをサポート。LLMとRAGの検索をサポートします。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [daachorse](https://github.com/daac-tools/daachorse) | - | 📦 642k | ⭐ 241 | 🟢 january|
| 🔗 [find-simdoc](https://github.com/legalforce-research/find-simdoc) | - | 📦 29k | ⭐ 62 | 🟡 march 2025|
| 🔗 [crawdad](https://github.com/daac-tools/crawdad) | - | 📦 59k | ⭐ 36 | 🔴 january 2025|
| 🔗 [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) | - | - | ⭐ 4 | 🔴 march 2023|
| 🔗 [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [vime](https://github.com/algon-320/vime) | - | - | ⭐ 231 | 🔴 november 2022|
| 🔗 [voicevox_core](https://github.com/VOICEVOX/voicevox_core) | - | - | ⭐ 1k | 🟢 last thursday|
| 🔗 [akaza](https://github.com/akaza-im/akaza) | - | - | ⭐ 228 | 🟢 today|
| 🔗 [Jotoba](https://github.com/WeDontPanic/Jotoba) | - | - | ⭐ 199 | 🔴 january 2024|
| 🔗 [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) | - | - | ⭐ 55 | 🟢 last saturday|
| 🔗 [niinii](https://github.com/Netdex/niinii) | - | - | ⭐ 15 | 🟢 last saturday|
| 🔗 [cskk](https://github.com/naokiri/cskk) | - | - | ⭐ 79 | 🟢 january|
| 🔗 [japanki](https://github.com/tysonwu/japanki) | - | - | ⭐ 3 | 🔴 october 2023|
| 🔗 [jpreprocess](https://github.com/jpreprocess/jpreprocess) | - | - | ⭐ 51 | 🟢 yesterday|
| 🔗 [listup_precedent](https://github.com/japanese-law-analysis/listup_precedent) | - | - | ⭐ 5 | 🟡 february 2025|
| 🔗 [jisho](https://github.com/eagleflo/jisho) | - | - | ⭐ 17 | 🟢 january|
| 🔗 [kanalizer](https://github.com/voicevox/kanalizer) | - | - | ⭐ 26 | 🟢 november 2025|
| 🔗 [koharu](https://github.com/mayocream/koharu) | - | - | ⭐ 561 | 🟢 yesterday|
| 🔗 [yomine](https://github.com/mcgrizzz/yomine) | - | - | ⭐ 45 | 🟢 january|
| 🔗 [matsuba](https://github.com/mrpicklepinosaur/matsuba) | - | - | ⭐ 18 | 🔴 march 2023|
| 🔗 [hujiang_dictionary](https://github.com/asutorufa/hujiang_dictionary) | - | - | ⭐ 69 | 🟢 today|


## JavaScript

### Morphology analysis
ブラウザやNode.jsで日本語形態素解析を行うライブラリ

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日本語形態素解析器のJavaScript実装
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - 日本語と中国語の形態素解析器（単語分割器+品詞タガー）である「楽天MA」は、純粋にJavaScriptで書かれています。
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - Nodejs用の別のmecabラッパー
 * [juman-bin](https://github.com/thammin/juman-bin) - 日本語形態素解析システムのユーザー拡張可能な解析器。
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - MeCabを使用した非同期日本語形態素解析器。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji.js](https://github.com/takuyaa/kuromoji.js) | 📥 155k/week | 📦 7.8M | ⭐ 964 | 🔴 november 2018|
| 🔗 [rakutenma](https://github.com/rakuten-nlp/rakutenma) | 📥 12/week | 📦 876 | ⭐ 473 | 🔴 january 2015|
| 🔗 [node-mecab-ya](https://github.com/golbin/mecab-ya) | 📥 152/week | 📦 7.1k | ⭐ 110 | 🔴 repo not found|
| 🔗 [juman-bin](https://github.com/thammin/juman-bin) | 📥 5/week | 📦 291 | ⭐ 3 | 🔴 may 2017|
| 🔗 [node-mecab-async](https://github.com/hecomi/node-mecab-async) | 📥 5.1k/week | 📦 339k | ⭐ 103 | 🔴 october 2017|


### Converter
日本語の表記や発音を変換するライブラリ

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - ふりがなと送り仮名モードに対応した、日本語の文章をひらがな、カタカナ、ローマ字に変換するための日本語言語ライブラリ。
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - 黒白のためのKuromoji形態素解析器。
 * [hepburn](https://github.com/lovell/hepburn) - ヘボン式ローマ字による、日本語のひらがなとカタカナを相互に変換するためのNode.jsモジュール
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - 日本の数字を数字に変換します。
 * [jslingua](https://github.com/kariminf/jslingua) - テキストを処理するためのJavascriptライブラリ：アラビア語、日本語など。
 * [WanaKana](https://github.com/WaniKani/WanaKana) - ひらがな<-->カタカナ<-->ローマ字の検出と転写のためのJavascriptライブラリ
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - ローマ字表記の日本人名における一般的な問題を正規化し修正する。
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - 日本語のテキストを古風にするためのユーティリティコレクション
 * [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) - オープンソースの住所正規化ライブラリ。
 * [jaconv](https://github.com/kazuhikoarase/jaconv) - 日本語文字変換ライブラリ (javascript)
 * [romaji-conv](https://github.com/koozaki/romaji-conv) - ローマ字をひらがなに変換する
 * [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) - 全国の住所データAPI
 * [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) - テキストの単語を絵文字に変換する
 * [japanese.js](https://github.com/hakatashi/japanese.js) - 日本語テキスト処理のためのUtilコレクション。ひらがな化、カタカナ化、ローマ字化。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuroshiro](https://github.com/hexenq/kuroshiro) | 📥 12k/week | 📦 356k | ⭐ 949 | 🔴 june 2021|
| 🔗 [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) | 📥 12k/week | 📦 334k | ⭐ 67 | 🔴 august 2018|
| 🔗 [hepburn](https://github.com/lovell/hepburn) | 📥 103k/week | 📦 3M | ⭐ 137 | 🟡 september 2025|
| 🔗 [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) | 📥 37k/week | 📦 2.1M | ⭐ 59 | 🔴 february 2023|
| 🔗 [jslingua](https://github.com/kariminf/jslingua) | 📥 67/week | 📦 7.2k | ⭐ 52 | 🔴 october 2023|
| 🔗 [WanaKana](https://github.com/WaniKani/WanaKana) | 📥 32k/week | 📦 2M | ⭐ 900 | 🟡 september 2025|
| 🔗 [node-romaji-name](https://github.com/jeresig/node-romaji-name) | 📥 287/week | 📦 12k | ⭐ 41 | 🔴 december 2023|
| 🔗 [kyujitai.js](https://github.com/hakatashi/kyujitai.js) | 📥 17/week | 📦 1.1k | ⭐ 23 | 🔴 august 2020|
| 🔗 [normalize-japanese-addresses](https://github.com/geolonia/normalize-japanese-addresses) | - | - | ⭐ 945 | 🟡 july 2025|
| 🔗 [jaconv](https://github.com/kazuhikoarase/jaconv) | - | - | ⭐ 86 | 🟡 june 2025|
| 🔗 [romaji-conv](https://github.com/koozaki/romaji-conv) | - | - | ⭐ 26 | 🟢 december 2025|
| 🔗 [japanese-addresses-v2](https://github.com/geolonia/japanese-addresses-v2) | - | - | ⭐ 69 | 🔴 january 2025|
| 🔗 [jptext-to-emoji](https://github.com/elzup/jptext-to-emoji) | - | - | ⭐ 2 | 🟢 february|
| 🔗 [japanese.js](https://github.com/hakatashi/japanese.js) | - | - | ⭐ 167 | 🔴 august 2020|


### Others
日本語NLPを扱うその他のJavaScriptライブラリ

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
 * [kamiya-codec](https://github.com/fasiha/kamiya-codec) - 日本語動詞の活用と非活用を基にした神谷妙子の「日本語動詞の手引き」と「日本語形容詞・副詞の手引き」に向けて。
 * [closewords](https://github.com/otoneko1102/closewords) - 最も似た単語を単語群から検索する日本語(漢字含む)対応のライブラリ
 * [japanese-analyzer](https://github.com/cokice/japanese-analyzer) - 日本語文章解析器
 * [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) - 日本語のフリガナを正規化します。
 * [yama](https://github.com/sapjax/yama) - 任意のウェブサイトで日本語の語彙を習得します。
 * [kaitai](https://github.com/compile10/kaitai) - AIを使用して日本語の文章構造を分析するためのアプリケーションです。このツールは、単語やフレーズがどのように関連しているかを視覚化し、インタラクティブな図表で文法的な関係を示します。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bangumi-data](https://github.com/bangumi-data/bangumi-data) | 📥 653/week | 📦 60k | ⭐ 592 | 🟢 today|
| 🔗 [yomichan](https://github.com/FooSoft/yomichan) | - | - | ⭐ 1.1k | 🔴 february 2023|
| 🔗 [proofreading-tool](https://github.com/gecko655/proofreading-tool) | - | - | ⭐ 87 | 🟡 october 2025|
| 🔗 [kanjigrid](https://github.com/minosvasilias/kanjigrid) | - | - | ⭐ 44 | 🔴 november 2018|
| 🔗 [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) | - | - | ⭐ 62 | 🔴 january 2023|
| 🔗 [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) | 📥 81k/week | 📦 4.7M | ⭐ 18 | 🔴 january 2025|
| 🔗 [hatsuon](https://github.com/DJTB/hatsuon) | 📥 15/week | 📦 950 | ⭐ 36 | 🔴 march 2022|
| 🔗 [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) | - | - | ⭐ 10 | 🔴 december 2021|
| 🔗 [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) | 📥 93/week | 📦 5.6k | ⭐ 8 | 🔴 july 2016|
| 🔗 [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) | 📥 2/week | 📦 287 | ⭐ repo not found | 🔴 repo not found|
| 🔗 [oskim](https://github.com/esrille/oskim) | - | - | ⭐ 2 | 🔴 february 2023|
| 🔗 [tweetMapping](https://github.com/wtnv-lab/tweetMapping) | - | - | ⭐ 25 | 🔴 december 2023|
| 🔗 [pitch-accent](https://github.com/shirakaba/pitch-accent) | 📥 1/week | 📦 84 | ⭐ 2 | 🔴 september 2023|
| 🔗 [kana2ipa](https://github.com/amanoese/kana2ipa) | - | - | ⭐ 17 | 🔴 october 2020|
| 🔗 [voicevox](https://github.com/VOICEVOX/voicevox) | - | - | ⭐ 3k | 🟢 last saturday|
| 🔗 [kamiya-codec](https://github.com/fasiha/kamiya-codec) | - | - | ⭐ 20 | 🟡 may 2025|
| 🔗 [closewords](https://github.com/otoneko1102/closewords) | - | - | ⭐ 3 | 🟡 august 2025|
| 🔗 [japanese-analyzer](https://github.com/cokice/japanese-analyzer) | - | - | ⭐ 669 | 🟢 december 2025|
| 🔗 [japanese-furigana-normalize](https://github.com/marvnc/japanese-furigana-normalize) | - | - | ⭐ 6 | 🔴 july 2024|
| 🔗 [yama](https://github.com/sapjax/yama) | - | - | ⭐ 7 | 🟢 january|
| 🔗 [kaitai](https://github.com/compile10/kaitai) | - | - | ⭐ 1 | 🟢 today|


## Go

### Morphology analysis
Goで日本語形態素解析を行う軽量ライブラリ

 * [kagome](https://github.com/ikawaha/kagome) - 純粋なGoで書かれた自己完結型の日本語形態素解析器


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kagome](https://github.com/ikawaha/kagome) | - | - | ⭐ 942 | 🟢 january|


### Others
日本語処理を支援する追加ライブラリ

 * [ojosama](https://github.com/jiro4989/ojosama) - テキストを壱百満天原サロメお嬢様風の口調に変換します
 * [nihongo](https://github.com/gojp/nihongo) - 日本語辞書
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - Yomichan用の外部辞書インポーター。
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - アイドルマスターの言葉辞書（imas-db.jpによる日本語IME用）
 * [go-kakasi](https://github.com/sarumaj/go-kakasi) - Goで漢字の読み仮名/片仮名/ローマ字に変換
 * [go-moji](https://github.com/ktnyt/go-moji) - 全角/半角変換のためのGoライブラリ
 * [ojichat](https://github.com/greymd/ojichat) - おじさんがLINEやメールで送ってきそうな文を生成する
 * [name](https://github.com/kuniwak/name) - 日本語の名前検索者


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [ojosama](https://github.com/jiro4989/ojosama) | - | - | ⭐ 388 | 🟢 january|
| 🔗 [nihongo](https://github.com/gojp/nihongo) | - | - | ⭐ 83 | 🔴 february 2024|
| 🔗 [yomichan-import](https://github.com/FooSoft/yomichan-import) | - | - | ⭐ 85 | 🔴 february 2023|
| 🔗 [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) | - | - | ⭐ 31 | 🟢 january|
| 🔗 [go-kakasi](https://github.com/sarumaj/go-kakasi) | - | - | ⭐ 6 | 🟢 december 2025|
| 🔗 [go-moji](https://github.com/ktnyt/go-moji) | - | - | ⭐ 20 | 🔴 april 2019|
| 🔗 [ojichat](https://github.com/greymd/ojichat) | - | - | ⭐ 1.3k | 🔴 october 2024|
| 🔗 [name](https://github.com/kuniwak/name) | - | - | ⭐ 11 | 🔴 january 2025|


## Java

### Morphology analysis
日本語形態素解析と辞書管理を行うライブラリ

 * [kuromoji](https://github.com/atilika/kuromoji) - Kuromojiは、検索用に設計された自己完結型で非常に使いやすい日本語形態素解析器です。
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - すだちの語彙集
 * [meval](https://github.com/teru-oka-1933/meval) - 形態素解析器性能評価システム MevAL


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kuromoji](https://github.com/atilika/kuromoji) | - | - | ⭐ 1k | 🔴 september 2019|
| 🔗 [Sudachi](https://github.com/WorksApplications/Sudachi) | - | - | ⭐ 930 | 🔴 november 2024|
| 🔗 [SudachiDict](https://github.com/WorksApplications/SudachiDict) | - | - | ⭐ 276 | 🟢 january|
| 🔗 [meval](https://github.com/teru-oka-1933/meval) | - | - | ⭐ 7 | 🔴 august 2019|


### Others
自然言語処理やOCRを支援するJavaライブラリ

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 画像から日本語文字を識別するためのJavaライブラリ
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 日本語の漢字をローマ字（ラテンアルファベット）に変換するためのJavaライブラリとコマンドラインツール。
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Javaにおける漢字のひらがな/カタカナ/ローマ字への転写
 * [Kamite](https://github.com/fauu/Kamite) - 日本語学習者のためのデスクトップ言語浸透コンパニオン
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - React Native用の非同期日本語トークナイザーネイティブプラグイン（iOSおよびAndroid用）
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本語アナライザーは、ElasticSearch用にkuromoji日本語トークナイザーを使用しています。
 * [moji4j](https://github.com/andree-surya/moji4j) - 日本語のひらがな、カタカナ、ローマ字のスクリプト間を変換するためのJavaライブラリ。
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - mecab-neologd用の日本語テキスト正規化ツール
 * [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) - Elasticsearchのための日本語解析プラグイン


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) | - | - | ⭐ 203 | 🔴 may 2021|
| 🔗 [jakaroma](https://github.com/nicolas-raoul/jakaroma) | - | - | ⭐ 67 | 🟡 june 2025|
| 🔗 [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) | - | - | ⭐ 55 | 🔴 april 2016|
| 🔗 [Kamite](https://github.com/fauu/Kamite) | - | - | ⭐ 129 | 🟡 march 2025|
| 🔗 [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) | - | - | ⭐ 38 | 🔴 june 2023|
| 🔗 [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) | - | - | ⭐ 29 | 🔴 march 2012|
| 🔗 [moji4j](https://github.com/andree-surya/moji4j) | - | - | ⭐ 33 | 🔴 june 2022|
| 🔗 [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) | - | - | ⭐ 5 | 🟢 last friday|
| 🔗 [elasticsearch-sudachi](https://github.com/worksapplications/elasticsearch-sudachi) | - | - | ⭐ 218 | 🟢 january|


## Pretrained model

### Word2Vec
単語を数値ベクトルに変換して意味的関係を学習するモデル

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - GensimとMecabを使用した日本語のWord2vec（単語からベクトルへのアプローチ）手法。
 * [chiVe](https://github.com/WorksApplications/chiVe) - SudachiとNWJCを使用した日本語の単語埋め込み。
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - エルモ-日本語
 * [embedrank](https://github.com/yagays/embedrank) - EmbedRankのPython実装
 * [aovec](https://github.com/eggplants/aovec) - 簡単な青空文庫のWord2Vecビルダー - 青空文庫の全書籍を対象としたWord2Vecモデルの構築と構築済みモデル
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - これはAI LABの記事「係り受けに基づく日本語単語埋込 (Dependency-based Japanese Word Embeddings)」のリポジトリです。（記事URL https://ai-lab.lapras.com/nlp/japanese-word-embedding/）
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - もう一つの日本語ウィキペディアエンティティベクトル
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 最新の日本語Wikipediaのダンプデータから，MeCabを用いてIPA辞書と最新のNeologd辞書の両方で形態素解析を実施し，その結果に基づいた word2vec，fastText，GloVeの単語分散表現を学習するためのスクリプト


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) | - | - | ⭐ 87 | 🔴 august 2020|
| 🔗 [chiVe](https://github.com/WorksApplications/chiVe) | - | - | ⭐ 169 | 🔴 march 2024|
| 🔗 [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) | - | - | ⭐ 5 | 🔴 october 2019|
| 🔗 [embedrank](https://github.com/yagays/embedrank) | - | - | ⭐ 48 | 🔴 march 2019|
| 🔗 [aovec](https://github.com/eggplants/aovec) | 📥 273 | 📦 80k | ⭐ 3 | 🔴 january 2023|
| 🔗 [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) | - | - | ⭐ 8 | 🔴 august 2019|
| 🔗 [jawikivec](https://github.com/wikiwikification/jawikivec) | - | - | ⭐ 2 | 🔴 november 2018|
| 🔗 [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) | - | - | ⭐ 11 | 🔴 may 2020|


### Transformer based models
自己注意機構で文脈を理解し高度な言語処理を行うモデル

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
 * [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) - 日本のLLaMa実験日本のLLaMa実験
 * [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) - EasyLightChatAssistantは、KoboldCppで簡単に試すことができる、軽量で検閲や規制のないローカル日本語モデルのLightChatAssistantです。


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [bert-japanese](https://github.com/cl-tohoku/bert-japanese) | - | - | ⭐ 543 | 🔴 march 2024|
| 🔗 [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [bert-japanese](https://github.com/yoheikikuta/bert-japanese) | - | - | ⭐ 498 | 🔴 february 2021|
| 🔗 [SudachiTra](https://github.com/WorksApplications/SudachiTra) | 📥 311 | 📦 159k | ⭐ 79 | 🔴 december 2023|
| 🔗 [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) | - | - | ⭐ 245 | 🔴 june 2023|
| 🔗 [shiba](https://github.com/octanove/shiba) | 📥 25 | 📦 7k | ⭐ 89 | 🔴 november 2023|
| 🔗 [Dialog](https://github.com/reppy4620/Dialog) | - | - | ⭐ 73 | 🔴 october 2020|
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
| 🔗 [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) | - | - | ⭐ 325 | 🔴 september 2023|
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
| 🔗 [japanese-llama-experiment](https://github.com/lighttransport/japanese-llama-experiment) | - | - | ⭐ 54 | 🟢 december 2025|
| 🔗 [easylightchatassistant](https://github.com/zuntan03/easylightchatassistant) | - | - | ⭐ 39 | 🔴 april 2024|


## ChatGPT
ChatGPTやAPIを用いて日本語の対話やテキスト生成を行うためのリソース

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
 * [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) - ChatGPTやCopilotなど各種生成AI用の「日本語]の Prompt のサンプル


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) | - | - | ⭐ 15 | 🔴 march 2023|
| 🔗 [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) | - | - | ⭐ 5 | 🔴 march 2023|
| 🔗 [wanna](https://github.com/hirokidaichi/wanna) | 📥 60 | 📦 20k | ⭐ 141 | 🔴 april 2023|
| 🔗 [ChatdollKit](https://github.com/uezo/ChatdollKit) | - | - | ⭐ 1.1k | 🟢 november 2025|
| 🔗 [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) | - | - | ⭐ 1 | 🔴 march 2023|
| 🔗 [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) | - | - | ⭐ 27 | 🔴 may 2023|
| 🔗 [vrchatbot](https://github.com/Geson-anko/vrchatbot) | - | - | ⭐ 28 | 🔴 december 2022|
| 🔗 [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) | - | - | ⭐ 63 | 🔴 january 2023|
| 🔗 [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) | - | - | ⭐ 16 | 🔴 april 2023|
| 🔗 [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) | - | - | ⭐ 1 | 🔴 april 2023|
| 🔗 [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) | - | - | ⭐ 46 | 🔴 december 2023|
| 🔗 [chatvrm](https://github.com/pixiv/chatvrm) | - | - | ⭐ 817 | 🟡 may 2025|
| 🔗 [sftly-replace](https://github.com/kmizu/sftly-replace) | - | - | ⭐ 4 | 🔴 may 2023|
| 🔗 [summarize_arxv](https://github.com/rkmt/summarize_arxv) | - | - | ⭐ 173 | 🔴 may 2023|
| 🔗 [aiavatarkit](https://github.com/uezo/aiavatarkit) | - | - | ⭐ 526 | 🟢 yesterday|
| 🔗 [pva-aoai-integration-solution](https://github.com/City-of-Kobe/pva-aoai-integration-solution) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [jp-azureopenai-samples](https://github.com/azure-samples/jp-azureopenai-samples) | - | - | ⭐ 279 | 🟡 september 2025|
| 🔗 [character_chat](https://github.com/mutaguchi/character_chat) | - | - | ⭐ 16 | 🔴 june 2023|
| 🔗 [chatgpt-slackbot](https://github.com/sifue/chatgpt-slackbot) | - | - | ⭐ 64 | 🔴 july 2024|
| 🔗 [chatgpt-prompt-sample-japanese](https://github.com/dahatake/chatgpt-prompt-sample-japanese) | - | - | ⭐ 409 | 🟢 last friday|
| 🔗 [kanji-flashcard-app-gpt4](https://github.com/adilmoujahid/kanji-flashcard-app-gpt4) | - | - | ⭐ 6 | 🔴 october 2023|
| 🔗 [IgakuQA](https://github.com/jungokasai/IgakuQA) | - | - | ⭐ 48 | 🔴 march 2023|
| 🔗 [japagen](https://github.com/retrieva/japagen) | - | - | ⭐ 1 | 🔴 october 2024|
| 🔗 [generativeai-prompt-sample-japanese](https://github.com/dahatake/generativeai-prompt-sample-japanese) | - | - | ⭐ 409 | 🟢 last friday|


## Dictionary and IME
日本語辞書や入力メソッドエディタに関するリソース

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
 * [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) - 読谷村のための日本語と中国語の辞書。
 * [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) - マウスオーバーした単語を自動で読み取る汎用辞書ツール
 * [jisyo](https://github.com/skk-dict/jisyo) - かな漢字変換エンジン SKKのための新しい辞書形式
 * [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) - 日本語の読みから Emoji に変換するための SKK 辞書 😂
 * [anthy](https://github.com/netsphere-labs/anthy) - アンシーは日本語のかな漢字変換エンジンです。ローマ字をかなに変換し、かなテキストをかなと漢字の混合テキストに変換します。
 * [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) - AWSサービス名のGoogle日本語入力向けの辞書
 * [cl-skkserv](https://github.com/tani/cl-skkserv) - Common LispによるSKK辞書サーバーとその拡張
 * [anthy](https://github.com/xorgy/anthy) - アンシーのメンテナンス
 * [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) - アンシーユニコード - アナザーアンシー
 * [azooKey](https://github.com/ensan-hcl/azooKey) - Input: azooKey: Swiftで完全に開発された日本語キーボードiOSアプリケーションOutput: azooKey：Swiftで完全に開発された日本語キーボードiOSアプリ
 * [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) - デスクトップ用の日本語入力メソッドazooKey、macOSをサポート
 * [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) - fcitx5用の日本語入力メソッド、azooKeyエンジンによって提供されています。
 * [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) - Mozc UT 場所名辞書は、Mozc用に日本郵便の郵便番号データから変換された辞書です。
 * [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) - Swiftで書かれた仮名漢字変換モジュール
 * [libkkc](https://github.com/ueno/libkkc) - 日本語仮名漢字変換入力方式ライブラリ
 * [libskk](https://github.com/ueno/libskk) - 日本語のSKK入力方式ライブラリ
 * [kanayomi-dict](https://github.com/warihima/kanayomi-dict) - openjtalk形式のユーザー辞書
 * [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) - 漢字データベースの辞書関連データ
 * [wlsp-classical](https://github.com/yocjyet/wlsp-classical) - 古典日本語の分類語彙表データ
 * [kanji-dict](https://github.com/marmooo/kanji-dict) - 漢字の書き順(筆順)・読み方・画数・部首・用例・成り立ちを調べるための漢字辞書です。Unicode 15.1 のすべての漢字 98,682字を収録しています。
 * [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) - (๑ ᴖ ᴑ ᴖ ๑)みょんかおもじ（旧Kaomoji_proj）はMicrosoft社の入力ソフト、Microsoft IME向けの顔文字の辞書を作成するプロジェクトです。
 * [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) - Kotlin かな漢字変換プログラム
 * [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) - jisho.orgを使用した日本語-英語辞書、エントリーの音声付きCSVエクスポート、および辞書サイトのプレビュー。jisho.orgを使用した日本語-英語辞書、エントリーの音声付きCSVエクスポート、および辞書サイトのプレビュー。
 * [ichiran](https://github.com/tshatrov/ichiran) - 日本語のテキスト用言語ツール
 * [mikan](https://github.com/mojyack/mikan) - 日本語の入力方法。
 * [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) - 関西弁日本語の授業で教えられた教材の簡単な参考資料。
 * [jisho-open](https://github.com/hlorenzi/jisho-open) - JMdict日本語英語辞書プロジェクトのWebフロントエンド、学習リストのサポート付き！JMdict日本語英語辞書プロジェクトのWebフロントエンド、学習リストのサポート付き！
 * [macskk](https://github.com/mtgto/macskk) - もうひとつのmacOS SKK入力方式
 * [nandoku](https://github.com/marmooo/nandoku) - 難読漢字を学年別にまとめた辞書です。
 * [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) - Android用のFOSS日本語IME
 * [anthywl](https://github.com/tadeokondrak/anthywl) - Swayのためのlibanthyを使用した日本語入力方法
 * [sekka](https://github.com/kiyoka/sekka) - SKKに触発されたもう1つの日本語入力方式。
 * [sumibi](https://github.com/kiyoka/sumibi) - ChatGPT APIによって強化された日本語入力方法
 * [jinmei-dict](https://github.com/s1r-j/jinmei-dict) - 辞書データから人名だけを抜き出し、読み仮名（カタカナ）をキーとして、候補となる書き文字をリストで保持するようなJSON形式に整形しています。
 * [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) - スミレ 完全オフラインの日本語キーボードアプリ
 * [japanesearabic](https://github.com/a-hamdi/japanesearabic) - 日本語アラビア語辞書（ヨミタン）
 * [o-dic](https://github.com/makotoga/o-dic) - 沖縄辞書
 * [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) - SKK 絵文字辞書
 * [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) - Mozc用の個人名辞書
 * [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) - SudachiDictからMozc用に変換された辞書
 * [nihongo](https://github.com/sph-mn/nihongo) - 日本語の言語データと辞書
 * [kagome-dict](https://github.com/ikawaha/kagome-dict) - かごめv2の辞書ライブラリ
 * [canna](https://github.com/canna-input/canna) - カンナ日本語入力システム
 * [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) - 京阪式アクセント（関西弁）辞書 - 4,615語を収録した日本語方言アクセント辞書


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) | - | - | ⭐ 2.8k | 🔴 september 2020|
| 🔗 [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) | - | - | ⭐ 123 | 🔴 march 2024|
| 🔗 [jamdict](https://github.com/neocl/jamdict) | 📥 215 | 📦 50k | ⭐ 163 | 🔴 june 2021|
| 🔗 [unidic-py](https://github.com/polm/unidic-py) | 📥 75k | 📦 9M | ⭐ 108 | 🟡 february 2025|
| 🔗 [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) | - | - | ⭐ 100 | 🔴 january 2023|
| 🔗 [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) | - | - | ⭐ 7 | 🔴 april 2021|
| 🔗 [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) | - | - | ⭐ 58 | 🟢 yesterday|
| 🔗 [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) | - | - | ⭐ 40 | 🔴 january 2021|
| 🔗 [JumanDIC](https://github.com/ku-nlp/JumanDIC) | - | - | ⭐ 4 | 🔴 august 2022|
| 🔗 [ipadic-py](https://github.com/polm/ipadic-py) | 📥 45k | 📦 6M | ⭐ 24 | 🔴 october 2021|
| 🔗 [unidic-lite](https://github.com/polm/unidic-lite) | 📥 87k | 📦 9M | ⭐ 49 | 🔴 september 2020|
| 🔗 [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) | - | - | ⭐ 365 | 🔴 january 2023|
| 🔗 [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) | - | - | ⭐ 101 | 🔴 january 2023|
| 🔗 [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) | - | - | ⭐ 83 | 🔴 september 2024|
| 🔗 [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) | - | - | ⭐ 58 | 🔴 december 2016|
| 🔗 [emoticon](https://github.com/tiwanari/emoticon) | - | - | ⭐ 43 | 🔴 may 2020|
| 🔗 [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) | - | - | ⭐ 10 | 🔴 january 2018|
| 🔗 [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) | - | - | ⭐ 2 | 🔴 november 2022|
| 🔗 [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) | - | - | ⭐ 35 | 🟢 today|
| 🔗 [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) | - | - | ⭐ 0 | 🔴 january 2020|
| 🔗 [EJDict](https://github.com/kujirahand/EJDict) | - | - | ⭐ 240 | 🟢 november 2025|
| 🔗 [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) | - | - | ⭐ 26 | 🔴 may 2024|
| 🔗 [genshin-dict](https://github.com/kotofurumiya/genshin-dict) | - | - | ⭐ 126 | 🟢 last wednesday|
| 🔗 [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) | - | - | ⭐ 324 | 🟢 today|
| 🔗 [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) | - | - | ⭐ 68 | 🟡 september 2025|
| 🔗 [mh-dict-jp](https://github.com/utubo/mh-dict-jp) | - | - | ⭐ 5 | 🟡 april 2025|
| 🔗 [jitenbot](https://github.com/stephenmk/jitenbot) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [mecab-unidic-neologd](https://github.com/neologd/mecab-unidic-neologd) | - | - | ⭐ 86 | 🔴 september 2020|
| 🔗 [hololive-dictionary](https://github.com/heppokofrontend/hololive-dictionary) | - | - | ⭐ 24 | 🔴 december 2024|
| 🔗 [jmdict-yomitan](https://github.com/themoeway/jmdict-yomitan) | - | - | ⭐ 233 | 🟡 june 2025|
| 🔗 [yomichan-jlpt-vocab](https://github.com/stephenmk/yomichan-jlpt-vocab) | - | - | ⭐ 116 | 🟡 august 2025|
| 🔗 [Jitendex](https://github.com/stephenmk/Jitendex) | - | - | ⭐ 444 | 🟢 yesterday|
| 🔗 [jiten](https://github.com/obfusk/jiten) | - | - | ⭐ 125 | 🔴 december 2023|
| 🔗 [pixiv-yomitan](https://github.com/MarvNC/pixiv-yomitan) | - | - | ⭐ 48 | 🟢 january|
| 🔗 [uchinaaguchi_dict](https://github.com/nanjakkun/uchinaaguchi_dict) | - | - | ⭐ 4 | 🟢 today|
| 🔗 [yomitan-dictionaries](https://github.com/marvnc/yomitan-dictionaries) | - | - | ⭐ 709 | 🟡 august 2025|
| 🔗 [mouse_over_dictionary](https://github.com/kengo700/mouse_over_dictionary) | - | - | ⭐ 72 | 🔴 january 2020|
| 🔗 [jisyo](https://github.com/skk-dict/jisyo) | - | - | ⭐ 28 | 🔴 september 2023|
| 🔗 [skk-jisyo.emoji-ja](https://github.com/ymrl/skk-jisyo.emoji-ja) | - | - | ⭐ 30 | 🔴 march 2018|
| 🔗 [aws_dic_for_google_ime](https://github.com/konyu/aws_dic_for_google_ime) | - | - | ⭐ 7 | 🔴 november 2019|
| 🔗 [cl-skkserv](https://github.com/tani/cl-skkserv) | - | - | ⭐ 31 | 🔴 october 2024|
| 🔗 [anthy](https://github.com/xorgy/anthy) | - | - | ⭐ 3 | 🔴 july 2013|
| 🔗 [anthy-unicode](https://github.com/fujiwarat/anthy-unicode) | - | - | ⭐ 40 | 🟢 january|
| 🔗 [azooKey](https://github.com/ensan-hcl/azooKey) | - | - | ⭐ 629 | 🟢 january|
| 🔗 [azookey-desktop](https://github.com/ensan-hcl/azookey-desktop) | - | - | ⭐ 781 | 🟢 january|
| 🔗 [fcitx5-hazkey](https://github.com/7ka-hiira/fcitx5-hazkey) | - | - | ⭐ 155 | 🟢 yesterday|
| 🔗 [mozcdic-ut-place-names](https://github.com/utuhiro78/mozcdic-ut-place-names) | - | - | ⭐ 20 | 🟢 last tuesday|
| 🔗 [azookeykanakanjiconverter](https://github.com/ensan-hcl/azookeykanakanjiconverter) | - | - | ⭐ 133 | 🟢 last saturday|
| 🔗 [libkkc](https://github.com/ueno/libkkc) | - | - | ⭐ 112 | 🔴 august 2024|
| 🔗 [libskk](https://github.com/ueno/libskk) | - | - | ⭐ 98 | 🟢 last tuesday|
| 🔗 [kanayomi-dict](https://github.com/warihima/kanayomi-dict) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [cjkvi-dict](https://github.com/cjkvi/cjkvi-dict) | - | - | ⭐ 108 | 🔴 september 2017|
| 🔗 [wlsp-classical](https://github.com/yocjyet/wlsp-classical) | - | - | ⭐ 2 | 🟢 november 2025|
| 🔗 [kanji-dict](https://github.com/marmooo/kanji-dict) | - | - | ⭐ 6 | 🟢 today|
| 🔗 [Kaomoji_proj](https://github.com/mtripg6666tdr/Kaomoji_proj) | - | - | ⭐ 11 | 🟡 october 2025|
| 🔗 [kotlin-kana-kanji-converter](https://github.com/KazumaProject/kotlin-kana-kanji-converter) | - | - | ⭐ 5 | 🟢 november 2025|
| 🔗 [alfred-japanese-dictionary](https://github.com/chrisgrieser/alfred-japanese-dictionary) | - | - | ⭐ 6 | 🟢 last friday|
| 🔗 [ichiran](https://github.com/tshatrov/ichiran) | - | - | ⭐ 386 | 🟢 january|
| 🔗 [mikan](https://github.com/mojyack/mikan) | - | - | ⭐ 24 | 🟡 june 2025|
| 🔗 [colloquial-kansai-dictionary](https://github.com/sethclydesdale/colloquial-kansai-dictionary) | - | - | ⭐ 9 | 🟢 december 2025|
| 🔗 [jisho-open](https://github.com/hlorenzi/jisho-open) | - | - | ⭐ 57 | 🟡 june 2025|
| 🔗 [macskk](https://github.com/mtgto/macskk) | - | - | ⭐ 258 | 🟢 yesterday|
| 🔗 [nandoku](https://github.com/marmooo/nandoku) | - | - | ⭐ 1 | 🟢 last friday|
| 🔗 [japanese_android_ime](https://github.com/nelsonapenn/japanese_android_ime) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [anthywl](https://github.com/tadeokondrak/anthywl) | - | - | ⭐ 34 | 🟡 april 2025|
| 🔗 [sekka](https://github.com/kiyoka/sekka) | - | - | ⭐ 24 | 🟡 july 2025|
| 🔗 [sumibi](https://github.com/kiyoka/sumibi) | - | - | ⭐ 34 | 🟢 january|
| 🔗 [jinmei-dict](https://github.com/s1r-j/jinmei-dict) | - | - | ⭐ 6 | 🔴 april 2020|
| 🔗 [japanesekeyboard](https://github.com/kazumaproject/japanesekeyboard) | - | - | ⭐ 200 | 🟢 last tuesday|
| 🔗 [japanesearabic](https://github.com/a-hamdi/japanesearabic) | - | - | ⭐ 17 | 🟡 may 2025|
| 🔗 [o-dic](https://github.com/makotoga/o-dic) | - | - | ⭐ 5 | 🟡 march 2025|
| 🔗 [skk-emoji-jisyo](https://github.com/uasi/skk-emoji-jisyo) | - | - | ⭐ 140 | 🔴 january 2025|
| 🔗 [mozcdic-ut-personal-names](https://github.com/utuhiro78/mozcdic-ut-personal-names) | - | - | ⭐ 24 | 🟢 last tuesday|
| 🔗 [mozcdic-ut-sudachidict](https://github.com/utuhiro78/mozcdic-ut-sudachidict) | - | - | ⭐ 20 | 🟢 february|
| 🔗 [nihongo](https://github.com/sph-mn/nihongo) | - | - | ⭐ 19 | 🔴 january 2025|
| 🔗 [kagome-dict](https://github.com/ikawaha/kagome-dict) | - | - | ⭐ 15 | 🟢 january|
| 🔗 [canna](https://github.com/canna-input/canna) | - | - | ⭐ 3 | 🟡 august 2025|
| 🔗 [kansai-accent-dictionary](https://github.com/nullponull/kansai-accent-dictionary) | - | - | ⭐ 1 | 🟢 december 2025|


## Corpus

### Part-of-speech tagging / Named entity recognition
品詞や固有表現のラベルが付与された日本語コーパス

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - Wikipediaを用いた日本語の固有表現抽出データセット
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 固有表現認識のための日本語IOB2タグ付きコーパス。
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter コーパス
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - 並列の普遍的な依存関係。
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - Google UDT 2.0からの日本語データ。
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大学ウェブドキュメントリードコーパス
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 注釈付きの普門買取センターのコーパス
 * [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) - UD_Japanese-GSDの長単位語バージョン
 * [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) - このUniversal Dependencies（UD）日本語ツリーバンクは、UDドキュメントに記載されているUD日本語規約の定義に基づいています。


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
| 🔗 [UD_Japanese-GSDLUW](https://github.com/UniversalDependencies/UD_Japanese-GSDLUW) | - | - | ⭐ 3 | 🟢 november 2025|
| 🔗 [ud_japanese-bccwj](https://github.com/universaldependencies/ud_japanese-bccwj) | - | - | ⭐ 27 | 🟢 november 2025|


### Parallel corpus
多言語の対応文を収録した翻訳用データセット

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
 * [matcha](https://github.com/ehimenlp/matcha) - 訪日観光客向けメディアMATCHAの記事から、日本語のテキスト平易化のためのデータセットを構築しました。
 * [en-ja-el](https://github.com/shigashiyama/en-ja-el) - EnJaEL：En-Jaパラレルエンティティリンキングデータセット（バージョン1.0）EnJaEL：En-Jaパラレルエンティティリンキングデータセット（バージョン1.0）


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
| 🔗 [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) | - | - | ⭐ 143 | 🟢 january|
| 🔗 [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) | - | - | ⭐ 18 | 🔴 november 2021|
| 🔗 [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) | - | - | ⭐ 4 | 🔴 march 2020|
| 🔗 [matcha](https://github.com/ehimenlp/matcha) | - | - | ⭐ 6 | 🔴 january 2025|
| 🔗 [en-ja-el](https://github.com/shigashiyama/en-ja-el) | - | - | ⭐ 2 | 🔴 january 2025|


### Dialog corpus
会話データを収集して対話モデルの学習に利用するコーパス

 * [JMRD](https://github.com/ku-nlp/JMRD) - 日本映画のおすすめ対話データセット
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - おーぷん2ちゃんねるをクロールして作成した対話コーパス
 * [BSD](https://github.com/tsuruoka-lab/BSD) - ビジネスシーンの対話コーパス
 * [asdc](https://github.com/megagonlabs/asdc) - 宿泊施設探索対話コーパス
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - seq2seqなどに使用する日本語の対話データ
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - このリポジトリには、AACL-IJCNLP 2022のWorkshop Eval4NLP 2022で発表された「Chat Translation Error Detection for Assisting Cross-lingual Communications」の論文で公開された日英バイリンガルチャットコーパスBPersna-chatが含まれています。
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 「日本語日常対話コーパス」は、日常生活に関する会話を中心に、学校、旅行、健康、エンターテインメントの5つのトピックについての高品質なマルチターン対話データセットです。
 * [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) - LLM構築用の日本語チャットデータセット
 * [kokorochat](https://github.com/uec-inabalab/kokorochat) - ロールプレイで収集した日本語のカウンセリング対話データセット


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [JMRD](https://github.com/ku-nlp/JMRD) | - | - | ⭐ 28 | 🔴 july 2022|
| 🔗 [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) | - | - | ⭐ 98 | 🔴 june 2021|
| 🔗 [BSD](https://github.com/tsuruoka-lab/BSD) | - | - | ⭐ 72 | 🔴 november 2021|
| 🔗 [asdc](https://github.com/megagonlabs/asdc) | - | - | ⭐ 25 | 🔴 august 2023|
| 🔗 [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) | - | - | ⭐ 3 | 🔴 october 2018|
| 🔗 [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) | - | - | ⭐ 5 | 🔴 january 2023|
| 🔗 [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) | - | - | ⭐ 54 | 🔴 march 2023|
| 🔗 [llm-japanese-dataset](https://github.com/masanorihirano/llm-japanese-dataset) | - | - | ⭐ 87 | 🔴 january 2024|
| 🔗 [kokorochat](https://github.com/uec-inabalab/kokorochat) | - | - | ⭐ 16 | 🟡 august 2025|


### Others
質問応答や含意認識など特定タスク向けの日本語データセット

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
 * [j-unimorph](https://github.com/cl-tohoku/j-unimorph) - 日本語のUniMorphデータセット
 * [GazeVQA](https://github.com/riken-grp/GazeVQA) - LREC-COLING 2024論文用データセット、曖昧な日本語質問を明確にするための視線基準ビジュアル質問応答データセットLREC-COLING 2024論文用データセット、曖昧な日本語質問を明確にするための視線基準ビジュアル質問応答データセット
 * [J-CRe3](https://github.com/riken-grp/J-CRe3) - J-CRe3実験のコード（上田ら、LREC-COLING、2024）
 * [jmed-llm](https://github.com/sociocom/jmed-llm) - JMED-LLM: 大規模言語モデル向けの日本医学評価データセット
 * [lawtext](https://github.com/yamachig/lawtext) - 日本の法律のプレーンテキスト形式
 * [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) - OCR処理プログラム研究開発事業において作成されたOCR学習用データセット
 * [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) - 話題に基づく語義曖昧性解消評価セット
 * [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) - Jamp: 制御された日本語時間推論データセット、言語モデルの汎化能力を評価するため
 * [JSeM](https://github.com/DaisukeBekki/JSeM) - 日本語意味テストスイート（FraCaSの対応および拡張）
 * [niilc-qa](https://github.com/mynlp/niilc-qa) - NIILC QAデータ
 * [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) - 日本語での「Chain-of-Thought Prompting」の論文検証データセット
 * [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) - これは、さまざまな言語注釈が付けられたWikipediaの記事からなる日本語テキストコーパスです。
 * [elaws-history](https://github.com/kissge/elaws-history) - e-Gov 法令検索で配布されている「全ての法令データ」を定期的にダウンロードし、アーカイブしています
 * [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) - Japanese-RP-BenchはLLMの日本語ロールプレイ能力を測定するためのベンチマークです。
 * [hdic](https://github.com/shikeda/hdic) - HDIC：日本初期の漢字辞書の統合データベース
 * [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) - Awesome Japan Open Data - 日本のオープンデータ情報一覧・まとめ
 * [kanji-data](https://github.com/mimneko/kanji-data) - 常用漢字表他、漢字に関するデータ
 * [openchj-genji](https://github.com/togiso/openchj-genji) - 「源氏物語」形態論情報データ
 * [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) - このリポジトリには、魅力的な広告テキストを生成するための言語的特徴を分析するためのParaphraseデータセットに関する私たちの論文のデータが含まれています。
 * [Jamp_sp](https://github.com/ynklab/Jamp_sp) - アスペクトを考慮した日本語時間推論データセットの構築（Jamp_sp: 制御された日本語時間推論データセットを考慮）
 * [jnli-neg](https://github.com/asahi-y/jnli-neg) - 否定理解能力を評価するための日本語言語推論データセット JNLI-Neg の公開用リポジトリです。
 * [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) - このリポジトリは、Common Crawlアーカイブから大規模な日本語ウェブコーパス（岡崎ら、2024年）であるSwallow Corpus Version 1を構築するためのPython実装を提供しています。
 * [jalecon](https://github.com/naist-nlp/jalecon) - 非母語話者向けの日本語語彙複雑性のデータセット
 * [multils-japanese](https://github.com/naist-nlp/multils-japanese) - MultiLS-日本語の語彙複雑性予測と語彙の簡素化データセット：アノテータープロファイル、非集計注釈、および注釈ガイドライン。
 * [nwjc](https://github.com/masayu-a/nwjc) - NINJALウェブ日本語コーパス
 * [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) - AAAI21で発表された「Towards Fully Automated Manga Translation」論文で紹介されたデータセットAAAI21で発表された「Towards Fully Automated Manga Translation」論文で紹介されたデータセット
 * [public-annotations](https://github.com/manga109/public-annotations) - Manga109データセットのさまざまな注釈
 * [gimei](https://github.com/willnet/gimei) - ランダムな日本人の名前と住所ジェネレーター
 * [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) - 日本語言語モデルの安全性の振る舞いを評価するテストセット
 * [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) - JSON形式で収録された、シンプルでオープンソースな日本語の擬音語や擬態語のコレクション。マンガのサンプル付き。
 * [kanji](https://github.com/sylhare/kanji) - 学習すべき日本語の漢字部首のリスト
 * [jethics](https://github.com/language-media-lab/jethics) - 日本語道徳理解度評価用データセットJETHICSの概説ページ (to be update)
 * [waon](https://github.com/llm-jp/waon) - WAON：ビジョン言語モデル向けの大規模で高品質な日本語画像テキストデータセット
 * [kuci](https://github.com/ku-nlp/kuci) - 京都大学コモンセンス推論データセット（KUCI）
 * [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) - 解析が難しい日本の住所のテストデータセット
 * [jlpt-word-list](https://github.com/elzup/jlpt-word-list) - JLPT語彙からの日本語単語リスト
 * [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) - 文字画像データセット(平仮名73文字版)
 * [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) - 日本の法令に関する多肢選択式QAデータセット
 * [yjcaptions](https://github.com/yahoojapan/yjcaptions) - YJキャプション26kデータセット
 * [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) - 日本のビジュアルジェノムVQAデータセット
 * [lawhub](https://github.com/lwhb/lawhub) - テキスト形式で日本の法律を追跡するリポジトリ
 * [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) - 日本のドラマ、アニメ、映画の字幕から派生した単語の頻度リスト。
 * [jconj](https://github.com/yamagoya/jconj) - テーブルベースの日本語単語活用プログラム
 * [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) - Wikipedia日本語から個人名を抽出します。
 * [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) - 日常日本会話データセットに基づいた読みちゃんの頻度辞書
 * [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) - ウィキペディアバイリンガルリファレンスデータ（日本語）
 * [ajimee-bench](https://github.com/azookey/ajimee-bench) - AJIMEE-Bench（高度な日本語IME評価ベンチマーク）
 * [j-spaw](https://github.com/takamichi-lab/j-spaw) - J-SpAW: スピーカー認証とアンチスプーフィングのための日本語音声コーパス
 * [camera3](https://github.com/cyberagentailab/camera3) - CAMERA3: 日本語における制御可能な広告テキスト生成の評価データセット
 * [jgpqa](https://github.com/llm-jp/jgpqa) - GPQAデータセットの日本語翻訳
 * [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) - Tanaka Corpus のノイズを除去しています。
 * [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) - 日本の感情コーパス 徳島大学 A-2 研究室
 * [osworld-jp](https://github.com/karakuri-ai/osworld-jp) - 言語を考慮した評価のための、日本語版コンピュータユースベンチマーク
 * [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) - Quasi Japanese Reviews (擬似レビューデータ)
 * [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) - 精神科初診カルテ作成アンケート データセット
 * [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) - 市町村合併などにより消滅した旧地名と新地名の対応表
 * [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) - 日本語のテキスト絵文字データ。
 * [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) - 聞き間違えコーパス︱CSV＋テーブルスキーマで約1万件を管理し、VS Code＋pre-commit＋Frictionless＋GitHub Actionsで自動検証を行う日本語データセット


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) | - | - | ⭐ 77 | 🔴 june 2023|
| 🔗 [kanji-data](https://github.com/davidluzgouveia/kanji-data) | - | - | ⭐ 200 | 🔴 december 2019|
| 🔗 [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) | - | - | ⭐ 102 | 🔴 december 2021|
| 🔗 [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) | - | - | ⭐ 32 | 🔴 march 2017|
| 🔗 [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) | - | - | ⭐ 141 | 🔴 september 2018|
| 🔗 [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) | - | - | ⭐ 108 | 🔴 january 2022|
| 🔗 [JaNLI](https://github.com/verypluming/JaNLI) | - | - | ⭐ 17 | 🔴 may 2023|
| 🔗 [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) | - | - | ⭐ 18 | 🔴 december 2020|
| 🔗 [emoji-ja](https://github.com/yagays/emoji-ja) | - | - | ⭐ 82 | 🟡 march 2025|
| 🔗 [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) | - | - | ⭐ 35 | 🔴 march 2020|
| 🔗 [ja.text8](https://github.com/Hironsan/ja.text8) | - | - | ⭐ 111 | 🔴 october 2017|
| 🔗 [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) | - | - | ⭐ 31 | 🔴 april 2018|
| 🔗 [japanese](https://github.com/hingston/japanese) | - | - | ⭐ 83 | 🔴 september 2018|
| 🔗 [kanji-frequency](https://github.com/scriptin/kanji-frequency) | - | - | ⭐ 155 | 🟢 january|
| 🔗 [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) | - | - | ⭐ 24 | 🔴 january 2021|
| 🔗 [CoARiJ](https://github.com/chakki-works/CoARiJ) | - | - | ⭐ 94 | 🔴 december 2020|
| 🔗 [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) | - | - | ⭐ 26 | 🔴 july 2023|
| 🔗 [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) | - | - | ⭐ 5 | 🔴 august 2021|
| 🔗 [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) | - | - | ⭐ 78 | 🔴 april 2024|
| 🔗 [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) | - | - | ⭐ 201 | 🔴 december 2021|
| 🔗 [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) | - | - | ⭐ 105 | 🟢 today|
| 🔗 [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) | - | - | ⭐ 176 | 🟢 today|
| 🔗 [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) | - | - | ⭐ 90 | 🔴 july 2018|
| 🔗 [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) | - | - | ⭐ 6 | 🔴 january 2019|
| 🔗 [speechBSD](https://github.com/ku-nlp/speechBSD) | - | - | ⭐ 3 | 🔴 february 2024|
| 🔗 [ita-corpus](https://github.com/mmorise/ita-corpus) | - | - | ⭐ 222 | 🔴 december 2024|
| 🔗 [rohan4600](https://github.com/mmorise/rohan4600) | - | - | ⭐ 66 | 🔴 february 2023|
| 🔗 [anlp-jp-history](https://github.com/whym/anlp-jp-history) | - | - | ⭐ 3 | 🔴 april 2024|
| 🔗 [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) | - | - | ⭐ 21 | 🔴 november 2022|
| 🔗 [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) | - | - | ⭐ 19 | 🔴 january 2021|
| 🔗 [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) | - | - | ⭐ 4 | 🔴 november 2018|
| 🔗 [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) | - | - | ⭐ 6 | 🔴 january 2020|
| 🔗 [wrime](https://github.com/ids-cv/wrime) | - | - | ⭐ 174 | 🟡 september 2025|
| 🔗 [jtubespeech](https://github.com/sarulab-speech/jtubespeech) | - | - | ⭐ 229 | 🔴 march 2023|
| 🔗 [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) | - | - | ⭐ 2 | 🔴 april 2022|
| 🔗 [kokkosho_data](https://github.com/rindybell/kokkosho_data) | - | - | ⭐ 1 | 🔴 july 2019|
| 🔗 [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) | - | - | ⭐ 75 | 🔴 june 2024|
| 🔗 [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) | - | - | ⭐ 28 | 🔴 september 2021|
| 🔗 [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) | - | - | ⭐ 31 | 🔴 february 2021|
| 🔗 [hirakanadic](https://github.com/po3rin/hirakanadic) | 📥 69 | 📦 13k | ⭐ 7 | 🔴 july 2023|
| 🔗 [animedb](https://github.com/anilogia/animedb) | - | - | ⭐ 328 | 🔴 january 2023|
| 🔗 [security_words](https://github.com/SaitoLab/security_words) | - | - | ⭐ 27 | 🔴 august 2023|
| 🔗 [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) | - | - | ⭐ 3 | 🔴 september 2022|
| 🔗 [honkoku-data](https://github.com/yuta1984/honkoku-data) | - | - | ⭐ 17 | 🟢 yesterday|
| 🔗 [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) | - | - | ⭐ 35 | 🔴 december 2020|
| 🔗 [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) | - | - | ⭐ 1.9k | 🔴 november 2020|
| 🔗 [JSICK](https://github.com/verypluming/JSICK) | - | - | ⭐ 45 | 🔴 may 2023|
| 🔗 [phishurl-list](https://github.com/JPCERTCC/phishurl-list) | - | - | ⭐ 198 | 🟢 november 2025|
| 🔗 [jcms](https://github.com/shigashiyama/jcms) | - | - | ⭐ 9 | 🔴 november 2022|
| 🔗 [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) | - | - | ⭐ 84 | 🔴 march 2023|
| 🔗 [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [topokanji](https://github.com/scriptin/topokanji) | - | - | ⭐ 198 | 🔴 january 2016|
| 🔗 [isbn4groups](https://github.com/uribo/isbn4groups) | - | - | ⭐ 1 | 🔴 june 2024|
| 🔗 [NMeCab](https://github.com/komutan/NMeCab) | - | - | ⭐ 97 | 🔴 march 2024|
| 🔗 [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) | - | - | ⭐ 14 | 🔴 january 2023|
| 🔗 [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) | - | - | ⭐ 3 | 🔴 july 2023|
| 🔗 [data_set](https://github.com/japanese-law-analysis/data_set) | - | - | ⭐ 49 | 🔴 january 2025|
| 🔗 [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) | - | - | ⭐ 4 | 🔴 january 2023|
| 🔗 [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) | - | - | ⭐ 18 | 🟡 february 2025|
| 🔗 [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) | - | - | ⭐ 180 | 🟢 december 2025|
| 🔗 [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) | - | - | ⭐ 2 | 🔴 october 2023|
| 🔗 [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) | - | - | ⭐ 12 | 🟡 march 2025|
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 | 🟢 november 2025|
| 🔗 [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) | - | - | ⭐ 31 | 🔴 march 2024|
| 🔗 [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) | - | - | ⭐ 6 | 🔴 march 2023|
| 🔗 [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) | - | - | ⭐ 21 | 🔴 january 2023|
| 🔗 [camera](https://github.com/CyberAgentAILab/camera) | - | - | ⭐ 26 | 🔴 august 2024|
| 🔗 [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) | - | - | ⭐ 20 | 🔴 may 2021|
| 🔗 [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [copa-japanese](https://github.com/nlp-titech/copa-japanese) | - | - | ⭐ 1 | 🔴 february 2023|
| 🔗 [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) | - | - | ⭐ 12 | 🔴 january 2025|
| 🔗 [ProSub](https://github.com/matbahasa/ProSub) | - | - | ⭐ 5 | 🟡 april 2025|
| 🔗 [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) | - | - | ⭐ 15 | 🟢 november 2025|
| 🔗 [ramendb](https://github.com/nuko-yokohama/ramendb) | - | - | ⭐ 7 | 🟢 yesterday|
| 🔗 [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) | - | - | ⭐ 3 | 🔴 march 2023|
| 🔗 [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) | - | - | ⭐ 0 | 🔴 march 2021|
| 🔗 [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) | - | - | ⭐ 89 | 🔴 july 2023|
| 🔗 [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) | - | - | ⭐ 0 | 🔴 june 2023|
| 🔗 [meconaudio](https://github.com/elith-co-jp/meconaudio) | - | - | ⭐ 9 | 🔴 october 2023|
| 🔗 [japanese-addresses](https://github.com/geolonia/japanese-addresses) | - | - | ⭐ 759 | 🟢 december 2025|
| 🔗 [aozorasearch](https://github.com/myokoym/aozorasearch) | - | - | ⭐ 21 | 🔴 september 2020|
| 🔗 [llm-jp-corpus](https://github.com/llm-jp/llm-jp-corpus) | - | - | ⭐ 43 | 🔴 october 2023|
| 🔗 [alpaca_ja](https://github.com/shi3z/alpaca_ja) | - | - | ⭐ 86 | 🔴 may 2023|
| 🔗 [instruction_ja](https://github.com/megagonlabs/instruction_ja) | - | - | ⭐ 24 | 🔴 july 2023|
| 🔗 [japanese-family-names](https://github.com/siikamiika/japanese-family-names) | - | - | ⭐ 18 | 🔴 june 2017|
| 🔗 [kanji-data-media](https://github.com/kanjialive/kanji-data-media) | - | - | ⭐ 401 | 🔴 november 2023|
| 🔗 [reazonspeech](https://github.com/reazon-research/reazonspeech) | - | - | ⭐ 358 | 🟢 january|
| 🔗 [huriganacorpus-aozora](https://github.com/ndl-lab/huriganacorpus-aozora) | - | - | ⭐ 17 | 🔴 january 2024|
| 🔗 [koniwa](https://github.com/koniwa/koniwa) | - | - | ⭐ 56 | 🟡 april 2025|
| 🔗 [JMMLU](https://github.com/nlp-waseda/JMMLU) | - | - | ⭐ 38 | 🟡 october 2025|
| 🔗 [hurigana-speech-corpus-aozora](https://github.com/ndl-lab/hurigana-speech-corpus-aozora) | - | - | ⭐ 42 | 🟡 march 2025|
| 🔗 [jqara](https://github.com/hotchpotch/jqara) | - | - | ⭐ 42 | 🟡 september 2025|
| 🔗 [jemhopqa](https://github.com/aiishii/jemhopqa) | - | - | ⭐ 29 | 🟡 april 2025|
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
| 🔗 [lawtext](https://github.com/yamachig/lawtext) | - | - | ⭐ 91 | 🟢 january|
| 🔗 [pdmocrdataset-part2](https://github.com/ndl-lab/pdmocrdataset-part2) | - | - | ⭐ 14 | 🔴 june 2024|
| 🔗 [japanesetopicwsd](https://github.com/nut-jnlp/japanesetopicwsd) | - | - | ⭐ 2 | 🔴 september 2018|
| 🔗 [temporalNLI_dataset](https://github.com/tomo-vv/temporalNLI_dataset) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [JSeM](https://github.com/DaisukeBekki/JSeM) | - | - | ⭐ 13 | 🔴 november 2024|
| 🔗 [niilc-qa](https://github.com/mynlp/niilc-qa) | - | - | ⭐ 18 | 🔴 november 2015|
| 🔗 [chain-of-thought-ja-dataset](https://github.com/nlp-waseda/chain-of-thought-ja-dataset) | - | - | ⭐ 5 | 🔴 september 2023|
| 🔗 [WikipediaAnnotatedCorpus](https://github.com/ku-nlp/WikipediaAnnotatedCorpus) | - | - | ⭐ 11 | 🟢 february|
| 🔗 [elaws-history](https://github.com/kissge/elaws-history) | - | - | ⭐ 4 | 🟢 yesterday|
| 🔗 [Japanese-RP-Bench](https://github.com/Aratako/Japanese-RP-Bench) | - | - | ⭐ 17 | 🔴 september 2024|
| 🔗 [hdic](https://github.com/shikeda/hdic) | - | - | ⭐ 40 | 🟢 january|
| 🔗 [awesome-japan-opendata](https://github.com/japan-opendata/awesome-japan-opendata) | - | - | ⭐ 155 | 🟢 last tuesday|
| 🔗 [kanji-data](https://github.com/mimneko/kanji-data) | - | - | ⭐ 10 | 🟢 today|
| 🔗 [openchj-genji](https://github.com/togiso/openchj-genji) | - | - | ⭐ 2 | 🟡 march 2025|
| 🔗 [AdParaphrase](https://github.com/CyberAgentAILab/AdParaphrase) | - | - | ⭐ 1 | 🟡 may 2025|
| 🔗 [Jamp_sp](https://github.com/ynklab/Jamp_sp) | - | - | ⭐ 0 | 🔴 june 2024|
| 🔗 [jnli-neg](https://github.com/asahi-y/jnli-neg) | - | - | ⭐ 0 | 🟢 december 2025|
| 🔗 [swallow-corpus](https://github.com/swallow-llm/swallow-corpus) | - | - | ⭐ 5 | 🔴 november 2024|
| 🔗 [jalecon](https://github.com/naist-nlp/jalecon) | - | - | ⭐ 5 | 🔴 july 2023|
| 🔗 [multils-japanese](https://github.com/naist-nlp/multils-japanese) | - | - | ⭐ 0 | 🟢 january|
| 🔗 [nwjc](https://github.com/masayu-a/nwjc) | - | - | ⭐ 10 | 🔴 april 2022|
| 🔗 [open-mantra-dataset](https://github.com/mantra-inc/open-mantra-dataset) | - | - | ⭐ 198 | 🔴 march 2023|
| 🔗 [gimei](https://github.com/willnet/gimei) | - | - | ⭐ 424 | 🟢 january|
| 🔗 [safety-boundary-test](https://github.com/sbintuitions/safety-boundary-test) | - | - | ⭐ 9 | 🟡 july 2025|
| 🔗 [j-ono-data](https://github.com/ObakeConstructs/j-ono-data) | - | - | ⭐ 6 | 🟢 last wednesday|
| 🔗 [kanji](https://github.com/sylhare/kanji) | - | - | ⭐ 28 | 🟢 december 2025|
| 🔗 [jethics](https://github.com/language-media-lab/jethics) | - | - | ⭐ 2 | 🟡 june 2025|
| 🔗 [waon](https://github.com/llm-jp/waon) | - | - | ⭐ 6 | 🟢 november 2025|
| 🔗 [kuci](https://github.com/ku-nlp/kuci) | - | - | ⭐ 5 | 🔴 february 2024|
| 🔗 [japanese-address-testdata](https://github.com/t-sagara/japanese-address-testdata) | - | - | ⭐ 14 | 🔴 september 2023|
| 🔗 [jlpt-word-list](https://github.com/elzup/jlpt-word-list) | - | - | ⭐ 56 | 🔴 february 2022|
| 🔗 [hiragana_mojigazo](https://github.com/ndl-lab/hiragana_mojigazo) | - | - | ⭐ 18 | 🔴 april 2020|
| 🔗 [lawqa_jp](https://github.com/digital-go-jp/lawqa_jp) | - | - | ⭐ 264 | 🟢 november 2025|
| 🔗 [yjcaptions](https://github.com/yahoojapan/yjcaptions) | - | - | ⭐ 60 | 🔴 november 2016|
| 🔗 [ja-vg-vqa](https://github.com/yahoojapan/ja-vg-vqa) | - | - | ⭐ 30 | 🔴 november 2018|
| 🔗 [lawhub](https://github.com/lwhb/lawhub) | - | - | ⭐ 152 | 🔴 november 2020|
| 🔗 [japanese-subtitles-word-kanji-frequency-lists](https://github.com/chriskempson/japanese-subtitles-word-kanji-frequency-lists) | - | - | ⭐ 39 | 🔴 december 2023|
| 🔗 [jconj](https://github.com/yamagoya/jconj) | - | - | ⭐ 35 | 🔴 may 2020|
| 🔗 [extract_jawp_names](https://github.com/hiroshi-manabe/extract_jawp_names) | - | - | ⭐ 21 | 🔴 december 2022|
| 🔗 [cejc_yomichan_freq_dict](https://github.com/forsakeninfinity/cejc_yomichan_freq_dict) | - | - | ⭐ 9 | 🔴 june 2023|
| 🔗 [wikidict-ja](https://github.com/open-dict-data/wikidict-ja) | - | - | ⭐ 5 | 🔴 june 2016|
| 🔗 [ajimee-bench](https://github.com/azookey/ajimee-bench) | - | - | ⭐ 18 | 🔴 january 2025|
| 🔗 [j-spaw](https://github.com/takamichi-lab/j-spaw) | - | - | ⭐ 5 | 🟡 august 2025|
| 🔗 [camera3](https://github.com/cyberagentailab/camera3) | - | - | ⭐ 4 | 🔴 may 2024|
| 🔗 [jgpqa](https://github.com/llm-jp/jgpqa) | - | - | ⭐ 2 | 🟡 september 2025|
| 🔗 [tanaka-corpus-plus](https://github.com/marmooo/tanaka-corpus-plus) | - | - | ⭐ 2 | 🔴 june 2021|
| 🔗 [emotioncorpusjapanesetokushimaa2lab](https://github.com/kmatsu-tokudai/emotioncorpusjapanesetokushimaa2lab) | - | - | ⭐ 2 | 🔴 september 2024|
| 🔗 [osworld-jp](https://github.com/karakuri-ai/osworld-jp) | - | - | ⭐ 2 | 🟢 november 2025|
| 🔗 [quasi_japanese_reviews](https://github.com/megagonlabs/quasi_japanese_reviews) | - | - | ⭐ 1 | 🔴 july 2023|
| 🔗 [psychiatry-clinical-notes](https://github.com/sociocom/psychiatry-clinical-notes) | - | - | ⭐ 1 | 🟡 october 2025|
| 🔗 [merged-town-names](https://github.com/yuukitoriyama/merged-town-names) | - | - | ⭐ 1 | 🔴 may 2022|
| 🔗 [japanesetextemoticondata](https://github.com/kuroshiba-ginji/japanesetextemoticondata) | - | - | ⭐ 1 | 🔴 march 2021|
| 🔗 [mishearing-corpus](https://github.com/kishiyamat/mishearing-corpus) | - | - | ⭐ 1 | 🟢 january|


## Tutorial
日本語自然言語処理のツールや技術を学ぶためのチュートリアル

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
 * [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) - 日本語情報検索チュートリアル
 * [nlpbook](https://github.com/mamorlis/nlpbook) - 「自然言語処理の教科書」サポートサイト
 * [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) - 作って学ぶ正規表現エンジン
 * [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) - 【2024年版】BERTによるテキスト分類
 * [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) - Google Gemmaの日本語の説明のためのファインチューニング
 * [nlp100v2020](https://github.com/upura/nlp100v2020) - 「言語処理100本ノック 2020」をPythonで解く
 * [textmining-ja](https://github.com/paithiov909/textmining-ja) - Rによる自然言語処理・テキスト分析の練習
 * [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) - NLP2025 のチュートリアル「地理情報と言語処理 実践入門」の資料とソースコード
 * [nlp100v2025](https://github.com/upura/nlp100v2025) - 「言語処理100本ノック 2025」をPythonで解く
 * [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) - 『トピックモデル』(機械学習プロフェッショナルシリーズ)のノート
 * [slp2025](https://github.com/ryota-komatsu/slp2025) -音学シンポジウム2025チュートリアル「マルチモーダル大規模言語モデル入門」資料
 * [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) - インプレス出版「IT基礎教養 自然言語処理＆画像解析」
 * [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) - 書籍「現場で活用するための生成AIエージェント実践入門」（講談社サイエンティフィック社）で利用されるソースコード
 * [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) - 2024年度 立教大学大学院 人工知能科学研究科 自然言語処理特論
 * [support-genai-book](https://github.com/yoheikikuta/support-genai-book) - 原論文から解き明かす生成AI（技術評論社）のサポートページです
 * [ir100](https://github.com/ir100/ir100) - 情報検索100本ノック
 * [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) - 『Kaggle ではじめる大規模言語モデル入門　～自然言語処理〈実践〉プログラミング～』のサポートサイト


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) | - | - | ⭐ 63 | 🔴 january 2020|
| 🔗 [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) | - | - | ⭐ 205 | 🔴 september 2016|
| 🔗 [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) | - | - | ⭐ 5 | 🔴 may 2022|
| 🔗 [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) | - | - | ⭐ 5 | 🔴 march 2019|
| 🔗 [ginza-examples](https://github.com/poyo46/ginza-examples) | - | - | ⭐ 16 | 🔴 january 2021|
| 🔗 [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) | - | - | ⭐ 0 | 🟡 august 2025|
| 🔗 [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) | - | - | ⭐ 29 | 🔴 january 2022|
| 🔗 [bert-book](https://github.com/stockmarkteam/bert-book) | - | - | ⭐ 264 | 🔴 february 2024|
| 🔗 [janome-tutorial](https://github.com/mocobeta/janome-tutorial) | - | - | ⭐ 31 | 🔴 march 2019|
| 🔗 [handson-language-models](https://github.com/hnishi/handson-language-models) | - | - | ⭐ 3 | 🔴 march 2021|
| 🔗 [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) | - | - | ⭐ 6 | 🔴 june 2021|
| 🔗 [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) | - | - | ⭐ 141 | 🔴 may 2021|
| 🔗 [bert-classification-tutorial](https://github.com/hppRC/bert-classification-tutorial) | - | - | ⭐ 235 | 🔴 may 2024|
| 🔗 [python-nlp-book](https://github.com/python-nlp-book/python-nlp-book) | - | - | ⭐ 10 | 🔴 may 2023|
| 🔗 [llm-book](https://github.com/ghmagazine/llm-book) | - | - | ⭐ 460 | 🟢 december 2025|
| 🔗 [nlp2024-tutorial-3](https://github.com/hiroshi-matsuda-rit/nlp2024-tutorial-3) | - | - | ⭐ 112 | 🔴 april 2024|
| 🔗 [japanese-ir-tutorial](https://github.com/mpkato/japanese-ir-tutorial) | - | - | ⭐ 3 | 🔴 june 2024|
| 🔗 [nlpbook](https://github.com/mamorlis/nlpbook) | - | - | ⭐ 14 | 🟡 april 2025|
| 🔗 [kantan-regex-book](https://github.com/makenowjust/kantan-regex-book) | - | - | ⭐ 22 | 🔴 march 2024|
| 🔗 [bert-classification-tutorial-2024](https://github.com/hpprc/bert-classification-tutorial-2024) | - | - | ⭐ 30 | 🔴 july 2024|
| 🔗 [Gemma2_2b_Japanese_finetuning_colab.ipynb](https://github.com/qianniu95/gemma2_2b_finetune_jp_tutorial/blob/main/Gemma2_2b_Japanese_finetuning_colab.ipynb) | - | - | ⭐ repo not found | 🔴 august 2024|
| 🔗 [nlp100v2020](https://github.com/upura/nlp100v2020) | - | - | ⭐ 91 | 🟡 april 2025|
| 🔗 [textmining-ja](https://github.com/paithiov909/textmining-ja) | - | - | ⭐ 3 | 🟡 october 2025|
| 🔗 [nlp2025-tutorial-2](https://github.com/yuiseki/nlp2025-tutorial-2) | - | - | ⭐ 17 | 🟢 january|
| 🔗 [nlp100v2025](https://github.com/upura/nlp100v2025) | - | - | ⭐ 91 | 🟡 april 2025|
| 🔗 [public-annotations](https://github.com/manga109/public-annotations) | - | - | ⭐ 13 | 🟡 april 2025|
| 🔗 [topic-models-ao](https://github.com/anemptyarchive/topic-models-ao) | - | - | ⭐ 4 | 🟡 may 2025|
| 🔗 [slp2025](https://github.com/ryota-komatsu/slp2025) | - | - | ⭐ 62 | 🟢 last wednesday|
| 🔗 [book_impress_it-basic-education-ai](https://github.com/liber-craft-co-ltd/book_impress_it-basic-education-ai) | - | - | ⭐ 4 | 🟡 june 2025|
| 🔗 [genai-agent-advanced-book](https://github.com/masamasa59/genai-agent-advanced-book) | - | - | ⭐ 182 | 🟡 september 2025|
| 🔗 [course2024-nlp](https://github.com/tomonari-masada/course2024-nlp) | - | - | ⭐ repo not found | 🔴 repo not found|
| 🔗 [support-genai-book](https://github.com/yoheikikuta/support-genai-book) | - | - | ⭐ 89 | 🟢 january|
| 🔗 [ir100](https://github.com/ir100/ir100) | - | - | ⭐ 93 | 🟢 december 2025|
| 🔗 [kaggle_llm_book](https://github.com/sinchir0/kaggle_llm_book) | - | - | ⭐ 16 | 🟢 january|


## Research summary
日本語自然言語処理に関する研究成果や論文をまとめた資料

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 日本語の事前学習済みBERTモデルのリストと、単語/サブワードトークン化+語彙構築アルゴリズム情報。
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 文法誤り訂正に関する日本語文献を収集・分類するためのリポジトリ
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - テキストコーパスなどのリスト（主に日本語）
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - ディープラーニングモデルの性能を体系的に最大化するためのプレイブック
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 日本語の音声、特にアクセントに関するリソースを一つのリストにまとめようとしています。
 * [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) - オープンソースの日本語LLMまとめ


|Name|downloads/week|total downloads|stars|last commit|
-|-|-|-|-
| 🔗 [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) | - | - | ⭐ 131 | 🔴 march 2023|
| 🔗 [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) | - | - | ⭐ 12 | 🟡 april 2025|
| 🔗 [dataset-list](https://github.com/ikegami-yukino/dataset-list) | - | - | ⭐ 117 | 🔴 july 2024|
| 🔗 [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) | - | - | ⭐ 190 | 🔴 january 2023|
| 🔗 [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) | - | - | ⭐ 124 | 🔴 february 2024|
| 🔗 [awesome-japanese-llm](https://github.com/llm-jp/awesome-japanese-llm) | - | - | ⭐ 1.3k | 🟢 january|


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
