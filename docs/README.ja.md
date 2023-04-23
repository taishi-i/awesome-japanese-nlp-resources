# awesome-japanese-nlp-resources

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

日本語の自然言語処理に関するPythonライブラリ、学習済みモデル、辞書、およびコーパスの厳選リストです。

このリストには、456件の日本語NLPリポジトリが含まれています。
これらのリポジトリを検索するための[ツール](https://huggingface.co/spaces/taishi-i/awesome-japanese-nlp-resources-search)はHugging Face Spacesで利用可能です。

あなたの貢献をいつでも歓迎します！
貢献する前に、[ガイドライン](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/contributing.md)をお読みください。

GitHubに存在しないリソースは、[Wiki](https://github.com/taishi-i/awesome-japanese-nlp-resources/wiki)に追加されます。


[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/README.zh-hans.md)


## The latest additions 🎉

**Corpus**
 * [meconaudio](https://github.com/elith-co-jp/meconaudio) - Mecon Audio(Medical Conference Audio)は厚生労働省主催の先進医療会議の議事録の読み上げデータセットです。

_Updated on Apr 24, 2023_

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

 * [sudachi.rs](https://github.com/WorksApplications/sudachi.rs) - 開発者は,Sudachi.rsとして,Sudachi.Py 0.6*以上を開発しています.
 * [Janome](https://github.com/mocobeta/janome) - 純粋な Python で書かれた日本語形状分析エンジン
 * [mecab-python3](https://github.com/SamuraiT/mecab-python3) - mecab-python. mecab-python. オリジナルバージョンはこちらから:http://taku910.github.io/mecab/
 * [mecab](https://github.com/ikegami-yukino/mecab) - このリポジトリは,Windows 64ビット MeCab バイナリを構築し,MeCab Python バイディングを改善するためのものです.
 * [fugashi](https://github.com/polm/fugashi) - サイトン・メカブ・ラッパーで 迅速なパイトン式日本語トークネージ化と形状分析
 * [nagisa](https://github.com/taishi-i/nagisa) - 繰り返し発生するニューラルネットワークに基づく日本のトークナイザー
 * [pyknp](https://github.com/ku-nlp/pyknp) - JUMAN++/KNP の Python モジュール
 * [Mykytea-python](https://github.com/chezou/Mykytea-python) - KyTea の Python パッケージ
 * [konoha](https://github.com/himkt/konoha) - コーノハ: 日本のトークナイザーの一般的なパッケージ
 * [natto-py](https://github.com/buruzaemon/natto-py) - natto-pyは Python プログラミング言語と MeCab を組み合わせ,日本語の部分言語と形状解析器です.
 * [rakutenma-python](https://github.com/ikegami-yukino/rakutenma-python) - Rakuten MA (Python version)
 * [python-vaporetto](https://github.com/daac-tools/python-vaporetto) - Vaporettoは,速くて軽い点向予測ベースのトークナイザーです. これはPythonのラップアップです.
 * [dango](https://github.com/mkartawijaya/dango) - 日本語のテキストのトークナイザーで,言語学習者や非言語学者に向け
 * [rhoknp](https://github.com/ku-nlp/rhoknp) - また,Juman++/KNP の Python 結合
 * [python-vibrato](https://github.com/daac-tools/python-vibrato) - バイタービベースの加速トークナイザー (Python ウェッパー)


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

 * [ginza](https://github.com/megagonlabs/ginza) - 汎用依存関係に基づくフレームワークとして spaCy を使用した日本NLPライブラリ
 * [cabocha](https://github.com/ikegami-yukino/cabocha) - 日本人の依存構造分析器
 * [UniDic2UD](https://github.com/KoichiYasuoka/UniDic2UD) - 代引体 POS タガー レンマティザー 依存性解析器 現代の日本語
 * [camphr](https://github.com/PKSHATechnology-Research/camphr) - パイプラインの部品を作成するためのNLPライブラリ
 * [SuPar-UniDic](https://github.com/KoichiYasuoka/SuPar-UniDic) - ローケナイザー POSタッガー BERTモデルによる現代・現代日本語用レマティザーと依存性解析器
 * [depccg](https://github.com/masashi-y/depccg) - A* CCG パッサー 超タグと依存因数モデル
 * [bertknp](https://github.com/ku-nlp/bertknp) - BERT をベースにした日本語の依存解析器
 * [esupar](https://github.com/KoichiYasuoka/esupar) - 日本語および他の言語のためのBERT/RoBERTa/DeBERTaモデルを持つトークナイザー POS-タッガーおよび依存性解析器
 * [yomikata](https://github.com/passaglia/yomikata) - 精細なBERTモデルを使用した異称解明ライブラリ.


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

 * [pykakasi](https://github.com/miurahr/pykakasi) - 日本語カナ・カンジ文からカナ・ローマ語への軽量変換器.
 * [cutlet](https://github.com/polm/cutlet) - Python で日本語からロマジへの変換
 * [alphabet2kana](https://github.com/shihono/alphabet2kana) - 英語アルファベットをカタカナに変換する
 * [Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese) - アラビア数字や"西洋"の数字を 日本語文脈に変換します
 * [mozcpy](https://github.com/ikegami-yukino/mozcpy) - Python の Mozc: カナ-カンジ変換
 * [jamorasep](https://github.com/tachi-hi/jamorasep) - Japanese text parser to separate Hiragana/Katakana string into morae (syllables).


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[pykakasi](https://github.com/miurahr/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi/week)](https://pepy.tech/project/pykakasi)|[![Downloads](https://pepy.tech/badge/pykakasi)](https://pepy.tech/project/pykakasi)|![GitHub Repo stars](https://img.shields.io/github/stars/miurahr/pykakasi?style=social)|
|[cutlet](https://github.com/polm/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet/week)](https://pepy.tech/project/cutlet)|[![Downloads](https://pepy.tech/badge/cutlet)](https://pepy.tech/project/cutlet)|![GitHub Repo stars](https://img.shields.io/github/stars/polm/cutlet?style=social)|
|[alphabet2kana](https://github.com/shihono/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana/week)](https://pepy.tech/project/alphabet2kana)|[![Downloads](https://pepy.tech/badge/alphabet2kana)](https://pepy.tech/project/alphabet2kana)|![GitHub Repo stars](https://img.shields.io/github/stars/shihono/alphabet2kana?style=social)|
|[Convert-Numbers-to-Japanese](https://github.com/Greatdane/Convert-Numbers-to-Japanese)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Greatdane/Convert-Numbers-to-Japanese?style=social)|
|[mozcpy](https://github.com/ikegami-yukino/mozcpy)|[![Downloads](https://pepy.tech/badge/mozcpy/week)](https://pepy.tech/project/mozcpy)|[![Downloads](https://pepy.tech/badge/mozcpy)](https://pepy.tech/project/mozcpy)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/mozcpy?style=social)|
|[jamorasep](https://github.com/tachi-hi/jamorasep)|[![Downloads](https://pepy.tech/badge/jamorasep/week)](https://pepy.tech/project/jamorasep)|[![Downloads](https://pepy.tech/badge/jamorasep)](https://pepy.tech/project/jamorasep)|![GitHub Repo stars](https://img.shields.io/github/stars/tachi-hi/jamorasep?style=social)|


### Preprocessor

 * [neologdn](https://github.com/ikegami-yukino/neologdn) - 日本語テキスト標準化器 mecab-neologd
 * [jaconv](https://github.com/ikegami-yukino/jaconv) - Pure-Python Japanese character interconverter for Hiragana, Katakana, Hankaku, and Zenkaku
 * [mojimoji](https://github.com/studio-ousia/mojimoji) - A fast converter between Japanese hankaku and zenkaku characters
 * [text-cleaning](https://github.com/ku-nlp/text-cleaning) - 日本語のウェブテキストのための強力なテキストクリーナー
 * [HojiChar](https://github.com/HojiChar/HojiChar) - 複数の前処理を構成して管理するテキスト前処理ツール


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[neologdn](https://github.com/ikegami-yukino/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn/week)](https://pepy.tech/project/neologdn)|[![Downloads](https://pepy.tech/badge/neologdn)](https://pepy.tech/project/neologdn)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/neologdn?style=social)|
|[jaconv](https://github.com/ikegami-yukino/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv/week)](https://pepy.tech/project/jaconv)|[![Downloads](https://pepy.tech/badge/jaconv)](https://pepy.tech/project/jaconv)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/jaconv?style=social)|
|[mojimoji](https://github.com/studio-ousia/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji/week)](https://pepy.tech/project/mojimoji)|[![Downloads](https://pepy.tech/badge/mojimoji)](https://pepy.tech/project/mojimoji)|![GitHub Repo stars](https://img.shields.io/github/stars/studio-ousia/mojimoji?style=social)|
|[text-cleaning](https://github.com/ku-nlp/text-cleaning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/text-cleaning?style=social)|
|[HojiChar](https://github.com/HojiChar/HojiChar)|[![Downloads](https://pepy.tech/badge/HojiChar/week)](https://pepy.tech/project/HojiChar)|[![Downloads](https://pepy.tech/badge/HojiChar)](https://pepy.tech/project/HojiChar)|![GitHub Repo stars](https://img.shields.io/github/stars/HojiChar/HojiChar?style=social)|


### Sentence spliter

 * [Bunkai](https://github.com/megagonlabs/bunkai) - 日本語の文の文界判定器 (日本語文境界判定器)
 * [japanese-sentence-breaker](https://github.com/hppRC/japanese-sentence-breaker) - 日本語文断片
 * [sengiri](https://github.com/ikegami-yukino/sengiri) - 日本語のテキストのための別の文レベルトークナイザー
 * [budoux](https://github.com/google/budoux) - 独立型.小さい.言語中立.BudouXはBudouの後継者.機械学習によるラインブレイクオーガナイザーツール.
 * [ja_sentence_segmenter](https://github.com/wwwcojp/ja_sentence_segmenter) - Python の日本語文段落ライブラリ
 * [hasami](https://github.com/mkartawijaya/hasami) - 日本語の文の文分割を行うツール
 * [kuzukiri](https://github.com/alinear-corp/kuzukiri) - Rust で書かれた Python の日本語テキストセグメンタ
 * [ja-senter-benchmark](https://github.com/hkiyomaru/ja-senter-benchmark) - 日本語の文区分ツール比較


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

 * [oseti](https://github.com/ikegami-yukino/oseti) - 日本語に対する感情分析
 * [negapoji](https://github.com/liaoziyang/negapoji) - Japanese negative positive classification.日本語文書のネガポジを判定。
 * [pymlask](https://github.com/ikegami-yukino/pymlask) - 日本語のテキストの感情分析器
 * [asari](https://github.com/Hironsan/asari) - Pythonで実装された日本語感情分析器.


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[oseti](https://github.com/ikegami-yukino/oseti)|[![Downloads](https://pepy.tech/badge/oseti/week)](https://pepy.tech/project/oseti)|[![Downloads](https://pepy.tech/badge/oseti)](https://pepy.tech/project/oseti)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/oseti?style=social)|
|[negapoji](https://github.com/liaoziyang/negapoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/liaoziyang/negapoji?style=social)|
|[pymlask](https://github.com/ikegami-yukino/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask/week)](https://pepy.tech/project/pymlask)|[![Downloads](https://pepy.tech/badge/pymlask)](https://pepy.tech/project/pymlask)|![GitHub Repo stars](https://img.shields.io/github/stars/ikegami-yukino/pymlask?style=social)|
|[asari](https://github.com/Hironsan/asari)|[![Downloads](https://pepy.tech/badge/asari/week)](https://pepy.tech/project/asari)|[![Downloads](https://pepy.tech/badge/asari)](https://pepy.tech/project/asari)|![GitHub Repo stars](https://img.shields.io/github/stars/Hironsan/asari?style=social)|


### Machine translation

 * [jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune) - JParaCrawlで訓練されたニューラルマシン翻訳 (NMT) モデルの例の使用.
 * [JASS](https://github.com/Mao-KU/JASS) - JASS: ニューラルマシン翻訳 (LREC2020) の日本語特有のシーケンス・トゥ・シーケンス・プレトレーニングと,低資源ニューラルマシン翻訳 (ACM TALLIP) の言語駆動マルチタスク・プレトレーニング
 * [PheMT](https://github.com/cl-tohoku/PheMT) - 日本語・英語機械翻訳の信頼性に関する現象的な評価データセット.データセットはMTNTデータセットに基づいており,四つの言語現象の追加注釈があります. 適名詞,略名詞,口語表現,変数. COLING 2020.
 * [VISA](https://github.com/ku-nlp/VISA) - 視覚的なシーン認識機械翻訳のための曖昧な字幕データセット


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jparacrawl-finetune](https://github.com/MorinoseiMorizo/jparacrawl-finetune)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/MorinoseiMorizo/jparacrawl-finetune?style=social)|
|[JASS](https://github.com/Mao-KU/JASS)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/Mao-KU/JASS?style=social)|
|[PheMT](https://github.com/cl-tohoku/PheMT)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/cl-tohoku/PheMT?style=social)|
|[VISA](https://github.com/ku-nlp/VISA)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/VISA?style=social)|


### Named entity recognition

 * [namaco](https://github.com/chakki-works/namaco) - 文字に基づくエンティティ識別
 * [entitypedia](https://github.com/chakki-works/entitypedia) - Entitypediaはウィキペディアのエンティティ名詞の拡張辞書です.
 * [noyaki](https://github.com/ken11/noyaki) - 文字の範囲のラベル情報をトークン化されたテキストベースのラベル情報に変換する.
 * [bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning) - Code to perform finetuning of the BERT model. BERTモデルのファインチューニングで固有表現抽出用タスクのモデルを作成・使用するサンプルです
 * [joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs) - 詳細なアノテーション基準に基づく症例報告コーパスからの固有表現及び関係の抽出精度の推論を行うコード


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[namaco](https://github.com/chakki-works/namaco)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/namaco?style=social)|
|[entitypedia](https://github.com/chakki-works/entitypedia)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/chakki-works/entitypedia?style=social)|
|[noyaki](https://github.com/ken11/noyaki)|[![Downloads](https://pepy.tech/badge/noyaki/week)](https://pepy.tech/project/noyaki)|[![Downloads](https://pepy.tech/badge/noyaki)](https://pepy.tech/project/noyaki)|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/noyaki?style=social)|
|[bert-japanese-ner-finetuning](https://github.com/ken11/bert-japanese-ner-finetuning)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ken11/bert-japanese-ner-finetuning?style=social)|
|[joint-information-extraction-hs](https://github.com/aih-uth/joint-information-extraction-hs)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/aih-uth/joint-information-extraction-hs?style=social)|


### OCR

 * [Manga OCR](https://github.com/kha-white/manga-ocr) - 日本語の文字の光学文字認識について,主に日本語マンガを中心に
 * [mokuro](https://github.com/kha-white/mokuro) - 日本語マンガはブラウザ内で選択可能なテキストで読む.
 * [handwritten-japanese-ocr](https://github.com/yas-sim/handwritten-japanese-ocr) - 手書きの日本語OCRデモで,インテル OpenVINO ツールキットを使用して入力テキストを画すタッチパネルを使用
 * [OCR_Japanease](https://github.com/tanreinama/OCR_Japanease) - 日本語OCR
 * [ndlocr_cli](https://github.com/ndl-lab/ndlocr_cli) - NDLOCRのアプリケーション
 * [donut](https://github.com/clovaai/donut) - OCR フリー ドキュメント理解トランスフォーマー (ドーナット) と合成文書生成器 (シンスドッグ) の正式導入 ECCV 2022
 * [JMTrans](https://github.com/ttop32/JMTrans) - manga translator - get japanese manga from url to translate manga image
 * [Kindai-OCR](https://github.com/ducanh841988/Kindai-OCR) - 現代日本誌の認識のためのOCRシステム
 * [text_recognition](https://github.com/ndl-lab/text_recognition) - NDLOCR用テキスト認識モジュール


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

 * [JGLUE](https://github.com/yahoojapan/JGLUE) - JGLUE: 日本語一般理解評価
 * [ginza-transformers](https://github.com/megagonlabs/ginza-transformers) - スペーストランスフォーマーにカスタムトークナイザーを使用する
 * [t5_japanese_dialogue_generation](https://github.com/Jinyamyzk/t5_japanese_dialogue_generation) - T5による会話生成
 * [japanese_text_classification](https://github.com/Masao-Taketani/japanese_text_classification) - MLP,CNN,RNN,BERTアプローチを含む様々なDNNテキスト分類法を調査する.
 * [Japanese-BERT-Sentiment-Analyzer](https://github.com/izuna385/Japanese-BERT-Sentiment-Analyzer) - FastAPI と BERT で センチメント アナリティクス サーバ を 展開 する
 * [jmlm_scoring](https://github.com/minhpqn/jmlm_scoring) - 日本語とベトナム語における仮面言語モデルに基づくスコア
 * [allennlp-shiba-model](https://github.com/shunk031/allennlp-shiba-model) - シーバのためのAllenNLP統合:日本の CANINEモデル
 * [evaluate_japanese_w2v](https://github.com/shihono/evaluate_japanese_w2v) - プリトレーニングされた日本語 word2vecモデルを日本語類似性データセットで評価するスクリプト
 * [gector-ja](https://github.com/jonnyli1125/gector-ja) - 日本語用GECタグ付け
 * [Japanese-BPEEncoder](https://github.com/tanreinama/Japanese-BPEEncoder) - 日本語BPEエンコーダ
 * [Japanese-BPEEncoder_V2](https://github.com/tanreinama/Japanese-BPEEncoder_V2) - Japanese-BPEEncoder Version 2
 * [transformer-copy](https://github.com/youichiro/transformer-copy) - 日本語文法誤り訂正ツール
 * [japanese-stable-diffusion](https://github.com/rinnakk/japanese-stable-diffusion) - 日本式安定拡散は,日本語特有の潜性テキスト・トゥ・イメージ拡散モデルで,テキスト入力条件で写真リアルな画像を生成できる.
 * [nagisa_bert](https://github.com/taishi-i/nagisa_bert) - A BERT model for nagisa
 * [prefix-tuning-gpt](https://github.com/rinnakk/prefix-tuning-gpt) - プレフィックス調節 GPT/GPT-NeoX モデルと訓練されたプレフィックスによる推論の例コード
 * [JGLUE-benchmark](https://github.com/nobu-g/JGLUE-benchmark) - 日本語理解基準であるJGLUEのための訓練と評価スクリプト


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

 * [namedivider-python](https://github.com/rskmoi/namedivider-python) - 日本語の名前を家族名と名前に分割するツールです
 * [asa-python](https://github.com/ikegami-yukino/asa-python) - 日本語向けNLPのPythonライブラリに専念した資源のキュレーションリスト
 * [python_asa](https://github.com/Takeuchi-Lab-LM/python_asa) - python版日本語意味役割付与システム（ASA）
 * [toiro](https://github.com/taishi-i/toiro) - 日本語トークナイザー比較ツール
 * [ja-timex](https://github.com/yagays/ja-timex) - 自然言語で書かれた時間情報表現を抽出/規格化するルールベースの解析器
 * [JapaneseTokenizers](https://github.com/Kensuke-Mitsuzawa/JapaneseTokenizers) - テキストデータから機能選択のための指標のセット
 * [daaja](https://github.com/kajyuuen/daaja) - このリポジトリには,日本語向けNLPのデータ拡張の実装があります.
 * [accel-brain-code](https://github.com/accel-brain/accel-brain-code) - このリポジトリの目的は,私のウェブサイトで書いた概念証明 (PoC) と研究開発 (R&D) の文脈で事例研究としてプロトタイプを作成することです.主な研究テーマは,表現学習に関連するオートエンコーダー,エネルギーベースのモデルのための統計機械学習,対抗生成ネットワークです.
 * [kyoto-reader](https://github.com/ku-nlp/kyoto-reader) - 京都コーパス,KWDLC,およびAnnotatedFKCCorpusのプロセッサ
 * [nlplot](https://github.com/takapy0210/nlplot) - 自然言語処理のための可視化モジュール
 * [rake-ja](https://github.com/kanjirz50/rake-ja) - 日本語のための高速自動キーワード抽出アルゴリズム
 * [jel](https://github.com/izuna385/jel) - 日本人エンティティ・リンクラー
 * [MedNER-J](https://github.com/sociocom/MedNER-J) - MedEX/J (日本語病名抽出機) の最新バージョン
 * [zunda-python](https://github.com/ikegami-yukino/zunda-python) - ズンダ: Python の日本語拡張モダリティアナリストクライアント.
 * [AIO2_DPR_baseline](https://github.com/cl-tohoku/AIO2_DPR_baseline) - https://www.nlp.ecei.tohoku.ac.jp/projects/aio/
 * [showcase](https://github.com/cl-tohoku/showcase) - 日本語Predicate-Argument Structure (PAS) アナライザーによるPyTorch実装が,松下一郎と井上一郎 (2018) の論文でいくつか改善された.
 * [darts-clone-python](https://github.com/rixwew/darts-clone-python) - ダーツクローンパイソン 結合
 * [jrte-corpus_example](https://github.com/megagonlabs/jrte-corpus_example) - Example codes for Japanese Realistic Textual Entailment Corpus
 * [desuwa](https://github.com/megagonlabs/desuwa) - KNPルールファイル (純粋Python) をベースにしたモルフェームやフレーズへの特徴注記
 * [HotPepperGourmetDialogue](https://github.com/Hironsan/HotPepperGourmetDialogue) - レストラン検索システム 日本語での対話
 * [nlp-recipes-ja](https://github.com/upura/nlp-recipes-ja) - 日本語における自然言語処理のサンプルコード
 * [Japanese_nlp_scripts](https://github.com/olsgaard/Japanese_nlp_scripts) - Python で日本語のテキストと作業するための小さな例脚本
 * [DNorm-J](https://github.com/sociocom/DNorm-J) - 日本語版のDNorm
 * [pyknp-eventgraph](https://github.com/ku-nlp/pyknp-eventgraph) - イベントグラフは,日本語での高レベルのNLPアプリケーションの開発プラットフォームです.
 * [ishi](https://github.com/ku-nlp/ishi) - 日本語の意思分類器
 * [python-npylm](https://github.com/musyoku/python-npylm) - ベイズ階層言語モデルによる教師なし形態素解析
 * [python-npycrf](https://github.com/musyoku/python-npycrf) - 条件付確率場とベイズ階層言語モデルの統合による半教師あり形態素解析
 * [unsupervised-pos-tagging](https://github.com/musyoku/unsupervised-pos-tagging) - 教師なし品詞タグ推定
 * [negima](https://github.com/cocodrips/negima) - Negimaは,あなたが定義した部分言語ベースのルールを用いて,日本語の文のフレーズを抽出するための Python パッケージです.
 * [YouyakuMan](https://github.com/neilctwu/YouyakuMan) - 抽出要約器は,BertSum を要約モデルとして使用する
 * [japanese-numbers-python](https://github.com/takumakanari/japanese-numbers-python) - 自然言語で日本語の数字 (関吉,アラビア語) の解析器.
 * [kantan](https://github.com/itayperl/kantan) - 日本語の単語を根源パターンで検索
 * [make-meidai-dialogue](https://github.com/knok/make-meidai-dialogue) - Get Japanese dialogue corpus
 * [japanese_summarizer](https://github.com/ryuryukke/japanese_summarizer) - 日本語の記事の要約書
 * [chirptext](https://github.com/letuananh/chirptext) - ChirpTextは,Python用のテキスト処理ツールの一覧です.
 * [yubin](https://github.com/alvations/yubin) - Japanese Address Munger
 * [jawiki-cleaner](https://github.com/hppRC/jawiki-cleaner) - 日本語ウィキペディア クリーンヤー
 * [japanese2phoneme](https://github.com/iory/japanese2phoneme) - 日本語を音符に変換する Python ライブラリです
 * [anlp_nlp2021_d3-1](https://github.com/arusl/anlp_nlp2021_d3-1) - このリポジトリには",感情に基づくテキスト分類のための日本のトークナイザー実験評価"の実験に関連するコードが含まれています.
 * [aozora_classification](https://github.com/shibuiwilliam/aozora_classification) - について
This project aims to classify Japanese sentence to how well similar to some Japanese classical writers, such as Soseki Natsume, Ogai Mori, Ryunosuke Akutagawa and so on.
 * [aozora-corpus-generator](https://github.com/borh/aozora-corpus-generator) - Aozora Bunko から シンプル テキスト ファイル を 生成 する
 * [JLM](https://github.com/jiali-ms/JLM) - 日本語や中国語のような大きな語彙言語のための速いLSTM言語モデル
 * [NTM](https://github.com/m3yrin/NTM) - 日本語記事のニューラルトピックモデリングのテスト
 * [EN-JP-ML-Lexicon](https://github.com/Machine-Learning-Tokyo/EN-JP-ML-Lexicon) - これは機械学習とディープラーニングの用語の 英語と日本語の辞書です
 * [text-generation](https://github.com/discus0434/text-generation) - 簡単に使いやすいスクリプトで GPT-2-JAを自分のテキストと調整し,文を作ったり,自動的にツイートしたりできます
 * [chainer_nic](https://github.com/yuyay/chainer_nic) - ニューラル画像キャプション (NIC) のチェーンで,英語と日本語の画像キャプションデータセットでプリトレーニングされたモデル
 * [unihan-lm](https://github.com/JetRunner/unihan-lm) - "UnihanLM: Unihanデータベースによる粗略な対細な中日本語模範予習"の公式資料庫,AACL-IJCNLP 2020
 * [mbart-finetuning](https://github.com/ken11/mbart-finetuning) - mBARTモデルを微調整するコード
 * [xvector_jtubespeech](https://github.com/sarulab-speech/xvector_jtubespeech) - xvector model on jtubespeech
 * [TinySegmenterMaker](https://github.com/shogo82148/TinySegmenterMaker) - TinySegmenter用の学習モデルを自作するためのツール．
 * [Grongish](https://github.com/shogo82148/Grongish) - 日本語とグロンギ語の相互変換スクリプト
 * [WordCloud-Japanese](https://github.com/aocattleya/WordCloud-Japanese) - WordCloudでの日本語文章をMecab（形態素解析エンジン）を使用せずに形態素解析チックな表示を実現するスクリプト
 * [snark](https://github.com/hiraokusky/snark) - 日本語ワードネットを利用したDBアクセスライブラリ
 * [toEmoji](https://github.com/mkan0141/toEmoji) - 日本語文を絵文字だけの文に変換するなにか
 * [termextract](https://github.com/kanjirz50/termextract) - - 専門用語抽出アルゴリズムの実装の練習
 * [JDT-with-KenLM-scoring](https://github.com/TUT-SLP-lab/JDT-with-KenLM-scoring) - Japanese-Dialog-Transformerの応答候補に対して、KenLMによるN-gram言語モデルでスコアリングし、フィルタリング若しくはリランキングを行う。
 * [mixture-of-unigram-model](https://github.com/KentoW/mixture-of-unigram-model) - Python でのユニグラムモデルとユニグラムモデルの無限混合の混合.
 * [hidden-markov-model](https://github.com/KentoW/hidden-markov-model) - Hidden Markov Model (HMM) and Infinite Hidden Markov Model (iHMM) in Python. (隠れマルコフモデルと無限隠れマルコフモデル)
 * [Ngram-language-model](https://github.com/KentoW/Ngram-language-model) - Python での Ngram 言語 モデル
 * [ASRDeepSpeech](https://github.com/JeanMaximilienCadic/ASRDeepSpeech) - ディープスピーチ2モデルによる自動音声認識 pytorchでZakuro AIのサポート
 * [neural_ime](https://github.com/yohokuno/neural_ime) - Neural IME: ニューラル入力メソッド エンジン
 * [neural_japanese_transliterator](https://github.com/Kyubyong/neural_japanese_transliterator) - ニューラルネットワークは ローマジを日本語に 正しく書き換えるのか?
 * [tinysegmenter](https://github.com/SamuraiT/tinysegmenter) - 日本語向けに指定されたトークナイザー
 * [AugLy-jp](https://github.com/chck/AugLy-jp) - 日本語テキストのデータ拡張
 * [furigana4epub](https://github.com/Mumumu4/furigana4epub) - ファイリガナを日本語版ePUBブックに追加するためのPythonスクリプト.
 * [PyKatsuyou](https://github.com/SmashinFries/PyKatsuyou) - 日本語動詞/形容詞の曲線ツール
 * [jageocoder](https://github.com/t-sagara/jageocoder) - 純粋なPythonの日本語アドレスジオコーダー
 * [pygeonlp](https://github.com/geonlp-platform/pygeonlp) - pygeonlp,日本のテキストを地理的に表示するための Python モジュールです.
 * [nksnd](https://github.com/yoriyuki/nksnd) - New kana-kanji conversion engine
 * [JaMIE](https://github.com/racerandom/JaMIE) - 日本 の 医療 情報の 抽出 ツール キット
 * [fasttext-vs-word2vec-on-twitter-data](https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data) - fasttextとword2vecの比較と、実行スクリプト、学習スクリプトです
 * [minimal-search-engine](https://github.com/GINK03/minimal-search-engine) - 最小のサーチエンジン/PageRank/tf-idf
 * [5ch-analysis](https://github.com/GINK03/5ch-analysis) - 5chの過去ログをスクレイピングして、過去流行った単語(ex, 香具師, orz)などを追跡調査
 * [tweet_extructor](https://github.com/tatHi/tweet_extructor) - Twitter日本語評判分析データセットのためのツイートダウンローダ
 * [japanese-word-aggregation](https://github.com/hkiyomaru/japanese-word-aggregation) - Juman++とConceptNet5.5をベースにした日本語の総括
 * [jinf](https://github.com/hkiyomaru/jinf) - 日本製の曲線変換機
 * [kwja](https://github.com/ku-nlp/kwja) - 日本語のための統一言語分析器
 * [mlm-scoring-transformers](https://github.com/Ryutaro-A/mlm-scoring-transformers) - マスク式言語モデルスコア (ACL2020) をベースにした複製パッケージ
 * [ClipCap-for-Japanese](https://github.com/Japanese-Image-Captioning/ClipCap-for-Japanese) - [PyTorch] 日本語版のクリップキャップ
 * [SAT-for-Japanese](https://github.com/Japanese-Image-Captioning/SAT-for-Japanese) - [PyTorch] 日本人のために ショー,アテンション,そしてトール
 * [cihai](https://github.com/cihai/cihai) - CJK (中国語,日本語,韓国語) 言語辞書のための Python ライブラリ
 * [marine](https://github.com/6gsn/marine) - 複数のタスクをこなす 基礎的な日本語アクセント
 * [whisper-asr-finetune](https://github.com/sarulab-speech/whisper-asr-finetune) - Finetuning Whisper ASR model
 * [japanese_chatbot](https://github.com/CjangCjengh/japanese_chatbot) - A PyTorch 日本語チャットボットの実装 BERTとトランスフォーマー解読機を使用
 * [radicalchar](https://github.com/yamamaya/radicalchar) - 部首文字正規化ライブラリ
 * [akaza](https://github.com/tokuhirom/akaza) - IBus/Linux のもう1つの日本語IME
 * [posuto](https://github.com/polm/posuto) - Japanese postal code data.
 * [tacotron2-japanese](https://github.com/CjangCjengh/tacotron2-japanese) - 日本語のタコトロン2の導入
 * [ibus-hiragana](https://github.com/esrille/ibus-hiragana) - ひらがなIME for IBus
 * [furiganapad](https://github.com/esrille/furiganapad) - ふりがなパッド
 * [chikkarpy](https://github.com/WorksApplications/chikkarpy) - 日本語同義語図書館
 * [ja-tokenizer-docker-py](https://github.com/p-geon/ja-tokenizer-docker-py) - メカブ + ネオログド + ドッカー + パイソン3
 * [JapaneseEmbeddingEval](https://github.com/oshizo/JapaneseEmbeddingEval) - JapaneseEmbeddingEval
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPTがYouTuberをやります
 * [shuwa](https://github.com/google/shuwa) - GNOME の画面キーボードを入力方法に拡張する
 * [japanese-nli-model](https://github.com/CyberAgentAILab/japanese-nli-model) - このリポジトリは,日本語NLIモデル,微調整された仮面言語モデルのコードを提供します.
 * [tra-fugu](https://github.com/tos-kamiya/tra-fugu) - FuguMT を使って日本語-英語翻訳と英語-日本語翻訳のツール
 * [fugumt](https://github.com/s-taka/fugumt) - ぷるーふおぶこんせぷと で公開した機械翻訳エンジンを利用する翻訳環境です。 フォームに入力された文字列の翻訳、PDFの翻訳が可能です。
 * [JaSPICE](https://github.com/keio-smilab23/JaSPICE) - JaSPICE: 画像字幕モデルのためのプレディケート-アーグメント構造を使用する自動評価メトリック
 * [Retrieval-based-Voice-Conversion-WebUI-JP-localization](https://github.com/yantaisa11/Retrieval-based-Voice-Conversion-WebUI-JP-localization) - jp-localization


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

 * [mecab](https://github.com/taku910/mecab) - もう"つの日本語形状分析機
 * [jumanpp](https://github.com/ku-nlp/jumanpp) - Juman++ (形状解析ツールキット)
 * [kytea](https://github.com/neubig/kytea) - 単語の分割と発音推定などのための京都テキスト分析ツールキット


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[mecab](https://github.com/taku910/mecab)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/mecab?style=social)|
|[jumanpp](https://github.com/ku-nlp/jumanpp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/jumanpp?style=social)|
|[kytea](https://github.com/neubig/kytea)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/neubig/kytea?style=social)|

### Parsing

 * [cabocha](https://github.com/taku910/cabocha) - 日本人の依存構造分析器
 * [knp](https://github.com/ku-nlp/knp) - 日本語解析機


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[cabocha](https://github.com/taku910/cabocha)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/taku910/cabocha?style=social)|
|[knp](https://github.com/ku-nlp/knp)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ku-nlp/knp?style=social)|

### Others

 * [jsc](https://github.com/yohokuno/jsc) - 日本語カナ・カンジ変換,中国語ピニン入力,CJE混合入力のための共同ソースチャネルモデル.
 * [aquaskk](https://github.com/codefirst/aquaskk) - 形状分析なしの入力方法
 * [mozc](https://github.com/google/mozc) - Mozc - 多プラットフォーム向けに設計された日本語入力方法エディタ
 * [trimatch](https://github.com/tuem/trimatch) - Trimatch: (Exact の前置き の前置き の 近い) 文字列 の 対応 図書 庫
 * [resembla](https://github.com/tuem/resembla) - Resembla: 単語をベースにした日本語類似文検索ライブラリ


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[jsc](https://github.com/yohokuno/jsc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/yohokuno/jsc?style=social)|
|[aquaskk](https://github.com/codefirst/aquaskk)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/codefirst/aquaskk?style=social)|
|[mozc](https://github.com/google/mozc)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/google/mozc?style=social)|
|[trimatch](https://github.com/tuem/trimatch)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/trimatch?style=social)|
|[resembla](https://github.com/tuem/resembla)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/tuem/resembla?style=social)|


## Rust crate

### Morphology analysis

 * [lindera](https://github.com/lindera-morphology/lindera) - 形状分析図書館
 * [vaporetto](https://github.com/daac-tools/vaporetto) - Vaporetto: 非常加速点向型予測型TOケナイザー
 * [goya](https://github.com/Leko/goya) - 日本語形状分析 で書かれた
 * [vibrato](https://github.com/daac-tools/vibrato) - vibrato: ビテルビベースの加速トークナイザー
 * [yoin](https://github.com/agatan/yoin) - 純正なで書かれた日本語形状分析器
 * [mecab-rs](https://github.com/tsurai/mecab-rs) - 安全な 鉄鋼の結合 メカブ 部分の音声と形状分析器のライブラリ
 * [awabi](https://github.com/nakagami/awabi) - メカブ辞書を使用する形状分析器


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

 * [wana_kana_rust](https://github.com/PSeitz/wana_kana_rust) - 日本語文字 - ヒラガナ,カタカナ - とロマジの間のチェックと変換のためのユーティリティライブラリ
 * [unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs) - 日本語の半角カナと全角英数を正規文字に変換するRustライブラリ
 * [kana](https://github.com/gbrlsnchs/kana) - [Mirror] CLI program for transliterating romaji text to either hiragana or katakana


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[wana_kana_rust](https://github.com/PSeitz/wana_kana_rust)|-|![Crates.io](https://img.shields.io/crates/d/wana_kana)|![GitHub Repo stars](https://img.shields.io/github/stars/PSeitz/wana_kana_rust?style=social)|
|[unicode-jp-rs](https://github.com/gemmarx/unicode-jp-rs)|-|![Crates.io](https://img.shields.io/crates/d/unicode-jp)|![GitHub Repo stars](https://img.shields.io/github/stars/gemmarx/unicode-jp-rs?style=social)|
|[kana](https://github.com/gbrlsnchs/kana)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gbrlsnchs/kana?style=social)|


### Search engine library

 * [lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy) - Lindera tokenizer for Tantivy.
 * [tantivy-vibrato](https://github.com/akr4/tantivy-vibrato) - バイブラトを使ったタンティヴィのトークナイザー


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[lindera-tantivy](https://github.com/lindera-morphology/lindera-tantivy)|-|![Crates.io](https://img.shields.io/crates/d/lindera-tantivy)|![GitHub Repo stars](https://img.shields.io/github/stars/lindera-morphology/lindera-tantivy?style=social)|
|[tantivy-vibrato](https://github.com/akr4/tantivy-vibrato)|-|![Crates.io](https://img.shields.io/crates/d/tantivy-vibrato)|![GitHub Repo stars](https://img.shields.io/github/stars/akr4/tantivy-vibrato?style=social)|


### Others

 * [daachorse](https://github.com/daac-tools/daachorse) - Aho-Corasick アルゴリズムをRustでコンパクトなダブルアレイデータ構造を用いて迅速に実装する.
 * [find-simdoc](https://github.com/legalforce-research/find-simdoc) - 類似した文書のすべてのペアを時間とメモリ効率的に検索
 * [crawdad](https://github.com/daac-tools/crawdad) - 文字の2つの配列を試す自然言語辞書です
 * [tokenizer-speed-bench](https://github.com/legalforce-research/tokenizer-speed-bench) - 異なるトークネライザーによる比較コード
 * [stringmatch-bench](https://github.com/legalforce-research/stringmatch-bench) - 文字列マッチングのためのデータ構造のパフォーマンスを比較するためのベンチマークツールを提供します.
 * [vime](https://github.com/algon-320/vime) - X11 アプリの入力方法として Vim を使用する
 * [voicevox_core](https://github.com/VOICEVOX/voicevox_core) - 無料で使える中品質なテキスト読み上げソフトウェア、VOICEVOXのコア
 * [akaza](https://github.com/akaza-im/akaza) - IBus/Linux のもう1つの日本語IME
 * [Jotoba](https://github.com/WeDontPanic/Jotoba) - 無料のオンライン,自主ホスト,多言語の日本語辞書です.
 * [dvorakjp-romantable](https://github.com/shinespark/dvorakjp-romantable) - Google 日本語入力用DvorakJPローマ字テーブル / DvorakJP Roman Table for Google Japanese Input
 * [niinii](https://github.com/Netdex/niinii) - 日本語語語音補強器,イチランを用いたテキストの読み取り支援


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

 * [kuromoji.js](https://github.com/takuyaa/kuromoji.js) - 日本語形状解析器のJavaScript実装
 * [rakutenma](https://github.com/rakuten-nlp/rakutenma) - Rakuten MA - 純粋にJavaScriptで書かれた中国語と日本語のための形状分析器 (ワードセグメンタ + PoS タガー).
Resources
 * [node-mecab-ya](https://github.com/golbin/node-mecab-ya) - ニュージャージュのメカビラップ
 * [juman-bin](https://github.com/thammin/juman-bin) - 日本語用拡張可能な形態解析器. 日本語形態素解析システム
 * [node-mecab-async](https://github.com/hecomi/node-mecab-async) - 異動式日本語形状分析機 メカブを使ってる


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji.js](https://github.com/takuyaa/kuromoji.js)|![npm](https://img.shields.io/npm/dw/kuromoji)|![npm](https://img.shields.io/npm/dt/kuromoji)|![GitHub Repo stars](https://img.shields.io/github/stars/takuyaa/kuromoji.js?style=social)|
|[rakutenma](https://github.com/rakuten-nlp/rakutenma)|![npm](https://img.shields.io/npm/dw/rakutenma)|![npm](https://img.shields.io/npm/dt/rakutenma)|![GitHub Repo stars](https://img.shields.io/github/stars/rakuten-nlp/rakutenma?style=social)|
|[node-mecab-ya](https://github.com/golbin/mecab-ya)|![npm](https://img.shields.io/npm/dw/mecab-ya)|![npm](https://img.shields.io/npm/dt/mecab-ya)|![GitHub Repo stars](https://img.shields.io/github/stars/golbin/node-mecab-ya?style=social)|
|[juman-bin](https://github.com/thammin/juman-bin)|![npm](https://img.shields.io/npm/dw/juman-bin)|![npm](https://img.shields.io/npm/dt/juman-bin)|![GitHub Repo stars](https://img.shields.io/github/stars/thammin/juman-bin?style=social)|
|[node-mecab-async](https://github.com/hecomi/node-mecab-async)|![npm](https://img.shields.io/npm/dw/mecab-async)|![npm](https://img.shields.io/npm/dt/mecab-async)|![GitHub Repo stars](https://img.shields.io/github/stars/hecomi/node-mecab-async?style=social)|


### Converter

 * [kuroshiro](https://github.com/hexenq/kuroshiro) - 日本語の文をヒラガナ,カタカナ,ロマジに変換する日本語ライブラリ.
 * [kuroshiro-analyzer-kuromoji](https://github.com/hexenq/kuroshiro-analyzer-kuromoji) - キュロシロの キュロモジ形状分析器
 * [hepburn](https://github.com/lovell/hepburn) - 日本語ヒラガナとカタカナ文字をヘプバーン語化を使ってロマジに変換するNode.jsモジュール
 * [japanese-numerals-to-number](https://github.com/twada/japanese-numerals-to-number) - 日本数字を数に変換する
 * [jslingua](https://github.com/kariminf/jslingua) - Javascript libraries to process text: Arabic, Japanese, etc.
 * [WanaKana](https://github.com/WaniKani/WanaKana) - ハイラガナ <--> カタカナ <--> ロマジ を 検知 し て 書き換える JavaScript 図書館
 * [node-romaji-name](https://github.com/jeresig/node-romaji-name) - ローマジをベースにした日本語の名前に関する一般的な問題を正し,正常化します.
 * [kyujitai.js](https://github.com/hakatashi/kyujitai.js) - 日本語のテキストを古典化するためのユーティリティコレクション


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

 * [bangumi-data](https://github.com/bangumi-data/bangumi-data) - Raw data for Japanese Anime
 * [yomichan](https://github.com/FooSoft/yomichan) - 日本語ポップアップ辞書拡張 Chrome と Firefox のために
 * [proofreading-tool](https://github.com/gecko655/proofreading-tool) - GUIで動作する文書校正ツール GUI テキストリントツール
 * [kanjigrid](https://github.com/minosvasilias/kanjigrid) - ジェームズ・ハイジグの"漢字を覚えておく" 6版で教えられている 2200文字を表示するウェブアプリ.
 * [japanese-toolkit](https://github.com/echamudi/japanese-toolkit) - 漢字,フリガナ,日本語DB,その他のためのモノレポ
 * [analyze-desumasu-dearu](https://github.com/textlint-ja/analyze-desumasu-dearu) - 文の敬体(ですます調)、常体(である調)を解析するJavaScriptライブラリ
 * [hatsuon](https://github.com/DJTB/hatsuon) - 日本語アクセント
 * [sentiment_ja_js](https://github.com/otodn/sentiment_ja_js) - 日本語での感情分析. JavaScript で sentiment_ja
 * [mecab-ipadic-seed](https://github.com/takuyaa/mecab-ipadic-seed) - メカブ・アイパッド 種子辞書リーダー
 * [Japanese-Word-Of-The-Day](https://github.com/LuanRT/Japanese-Word-Of-The-Day) - 日々違う日本語だ
 * [oskim](https://github.com/esrille/oskim) - GNOME の画面キーボードを入力方法に拡張する
 * [tweetMapping](https://github.com/wtnv-lab/tweetMapping) - 東日本大震災発生から24時間以内につぶやかれたジオタグ付きツイートのデジタルアーカイブです。


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

 * [kagome](https://github.com/ikawaha/kagome) - 純粋なゴで書かれた自立した日本語形状分析器


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kagome](https://github.com/ikawaha/kagome)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ikawaha/kagome?style=social)|


### Others

 * [ojosama](https://github.com/jiro4989/ojosama) - テキストを壱百満天原サロメお嬢様風の口調に変換します
 * [nihongo](https://github.com/gojp/nihongo) - 日本語辞書
 * [yomichan-import](https://github.com/FooSoft/yomichan-import) - 外部辞書輸入者 ヨミチャン
 * [imas-ime-dic](https://github.com/maruamyu/imas-ime-dic) - 日本語IMEのIDOLM@STERワード辞書 (imas-db.jpによる)
 * [go-moji](https://github.com/ktnyt/go-moji) - ゼンカク/ハンカク変換のための Go ライブラリ


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[ojosama](https://github.com/jiro4989/ojosama)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/jiro4989/ojosama?style=social)|
|[nihongo](https://github.com/gojp/nihongo)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/gojp/nihongo?style=social)|
|[yomichan-import](https://github.com/FooSoft/yomichan-import)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/FooSoft/yomichan-import?style=social)|
|[imas-ime-dic](https://github.com/maruamyu/imas-ime-dic)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/maruamyu/imas-ime-dic?style=social)|
|[go-moji](https://github.com/ktnyt/go-moji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/ktnyt/go-moji?style=social)|


## Java

### Morphology analysis

 * [kuromoji](https://github.com/atilika/kuromoji) - 検索のために設計された,自立で,非常に簡単に使用できる日本語形状分析機です
 * [Sudachi](https://github.com/WorksApplications/Sudachi) -　A Japanese Tokenizer for Business
 * [SudachiDict](https://github.com/WorksApplications/SudachiDict) - スーダチ語辞書


|Name|downloads/week|total downloads|stars|
-|-|-|-
|[kuromoji](https://github.com/atilika/kuromoji)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/atilika/kuromoji?style=social)|
|[Sudachi](https://github.com/WorksApplications/Sudachi)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/Sudachi?style=social)|
|[SudachiDict](https://github.com/WorksApplications/SudachiDict)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/WorksApplications/SudachiDict?style=social)|


### Others

 * [kanjitomo-ocr](https://github.com/sakarika/kanjitomo-ocr) - 画像から日本語の文字を識別するためのJavaライブラリ
 * [jakaroma](https://github.com/nicolas-raoul/jakaroma) - 日本語の漢字をローマ字に変換するJavaライブラリとコマンドラインツール
 * [kakasi-java](https://github.com/nicolas-raoul/kakasi-java) - Kanji transliteration to hiragana/katakana/romaji, in Java
 * [Kamite](https://github.com/fauu/Kamite) - 日本語学習者のためのデスクトップ言語浸透パートナー
 * [react-native-japanese-tokenizer](https://github.com/craftzdog/react-native-japanese-tokenizer) - Async 日本語トークナイザー Native Plugin for React iOSとAndroid向けネイティブ
 * [elasticsearch-analysis-japanese](https://github.com/suguru/elasticsearch-analysis-japanese) - 日本解析器はElasticSearchの日本語トークナイザー"kuromoji"を使用しています.
 * [moji4j](https://github.com/andree-surya/moji4j) - 日本語のヒラガナ,カタカナ,ロマジ文字を変換するJavaライブラリ.
 * [neologdn-java](https://github.com/ikegami-yukino/neologdn-java) - 日本語テキスト標準化器 mecab-neologd


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

 * [japanese-words-to-vectors](https://github.com/philipperemy/japanese-words-to-vectors) - Word2vec (ワード・トゥ・ベクター) 方法.
 * [chiVe](https://github.com/WorksApplications/chiVe) - 日本語の単語埋め込みとSudachiとNWJC
 * [elmo-japanese](https://github.com/cl-tohoku/elmo-japanese) - elmo-japanese
 * [embedrank](https://github.com/yagays/embedrank) - EmbedRank の Python 実装
 * [aovec](https://github.com/eggplants/aovec) - Easy aozorabunko Word2Vec Builder - 青空文庫全書籍のWord2Vecビルダー+構築済みモデル
 * [dependency-based-japanese-word-embeddings](https://github.com/lapras-inc/dependency-based-japanese-word-embeddings) - これはAI LABの記事"係り受けに基づく日本語単語埋込 (依存性に基づく日本語単語埋め込み) "の資料庫です (記事のURL https://ai-lab.lapras.com/nlp/japanese-word-embedding/)
 * [jawikivec](https://github.com/wikiwikification/jawikivec) - 日本語ウィキペディアのエンティティベクトル
 * [jawiki_word_vector_updater](https://github.com/kamigaito/jawiki_word_vector_updater) - 最新の日本語Wikipediaのダンプデータから，MeCabを用いてIPA辞書と最新のNeologd辞書の両方で形態素解析を実施し，その結果に基づいた word2vec，fastText，GloVeの単語分散表現を学習するためのスクリプト


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

 * [bert-japanese](https://github.com/cl-tohoku/bert-japanese) - BERT models for Japanese text.
 * [japanese-pretrained-models](https://github.com/rinnakk/japanese-pretrained-models) - 日本製の予備訓練モデル製造コードは rinna Co., Ltdから提供されています
 * [bert-japanese](https://github.com/yoheikikuta/bert-japanese) - 文の日本語は,BERTで,SentencePieceで
 * [SudachiTra](https://github.com/WorksApplications/SudachiTra) - Japanese tokenizer for Transformers
 * [japanese-dialog-transformers](https://github.com/nttcslab/japanese-dialog-transformers) - NTT Ltd が提供する日本の予備訓練モデル評価コード
 * [shiba](https://github.com/octanove/shiba) - パイトーチの実装と,前もって訓練された日本モデル CANINE,効率的な文字レベルトランスフォーマー
 * [Dialog](https://github.com/reppy4620/Dialog) - A PyTorch 日本語チャットボットの実装 BERTとトランスフォーマー解読機を使用
 * [language-pretraining](https://github.com/retarfi/language-pretraining) - 日本語のテキストのためのPyTorch実装のBERTとELECTRAモデル
 * [medbertjp](https://github.com/ou-medinfo/medbertjp) - 日本語での医療分野での予備訓練された BERTモデルの試験
 * [ILYS-aoba-chatbot](https://github.com/cl-tohoku/ILYS-aoba-chatbot) - ILYS-aoba-chatbot
 * [t5-japanese](https://github.com/megagonlabs/t5-japanese) - 日本製のT5モデルを予備訓練するコード
 * [pytorch_bert_japanese](https://github.com/yagays/pytorch_bert_japanese) - PytorchでBERTの日本語学習済みモデルを利用する
 * [Laboro-BERT-Japanese](https://github.com/laboroai/Laboro-BERT-Japanese) - 日本語: Web-Corpus で予備訓練された日本語 BERT
 * [RoBERTa-japanese](https://github.com/tanreinama/RoBERTa-japanese) - 日本人BERT 訓練を受けたモデル
 * [aMLP-japanese](https://github.com/tanreinama/aMLP-japanese) - aMLP Transformer Model for Japanese
 * [bert-japanese-aozora](https://github.com/akirakubo/bert-japanese-aozora) - 日本語BERTはAozora BunkoとWikipediaで訓練され,UniDic&SudachiPyでMeCabによってプリトークン化されています
 * [sbert-ja](https://github.com/colorfulscoop/sbert-ja) - 訓練コード 文 BERT ハグリングフェイスの日本語モデル
 * [BERT-Japan-vaccination](https://github.com/PatrickJohnRamos/BERT-Japan-vaccination) - "日本のツイートの感情分析と 日本でのワクチンとの比較"の公式の調整コード
 * [gpt2-japanese](https://github.com/tanreinama/gpt2-japanese) - 日本GPT2世代モデル
 * [text2text-japanese](https://github.com/tanreinama/text2text-japanese) - gpt-2 ベースの text2text 変換モデル
 * [gpt-ja](https://github.com/colorfulscoop/gpt-ja) - GPT-2 Japanese model for HuggingFace's transformers
 * [friendly_JA-Model](https://github.com/astremo/friendly_JA-Model) - フレンドリー_JAコープスを使って訓練されたMTモデル.標準の中日語辞書ではなくラテン語/英語から派生したカタカナ辞書を使って,日本語を西洋人により簡単に/より簡単に利用できるようにしようとしています.
 * [albert-japanese](https://github.com/alinear-corp/albert-japanese) - 文の日本語は,BERTで,SentencePieceで
 * [ja_text_bert](https://github.com/Kosuke-Szk/ja_text_bert) - 日本語WikipediaコーパスでBERTのPre-Trainedモデルを生成するためのリポジトリ
 * [DistilBERT-base-jp](https://github.com/BandaiNamcoResearchInc/DistilBERT-base-jp) - 訓練を受けたモデルです 訓練を受けたモデルは
 * [bert](https://github.com/informatix-inc/bert) - このリポジトリは,日本語コープスでRoBERTaを事前に訓練したスニペットを使用する.私たちのデータセットは,日本語ウィキペディアとウェブスクロールされた記事から構成されています.合計25GBです.リリースされたモデルはHuggingFaceから構築されています.
 * [Laboro-DistilBERT-Japanese](https://github.com/laboroai/Laboro-DistilBERT-Japanese) - ラボロ・ディスティルバート 日本語
 * [luke](https://github.com/studio-ousia/luke) - LUKE -- 知識に基づく埋め込みによる言語理解
 * [GPTSAN](https://github.com/tanreinama/GPTSAN) - 一般用途 スイッチトランスフォーマー ベース 日本語モード
 * [japanese-clip](https://github.com/rinnakk/japanese-clip) - 日本製のCLIP リンナ株式会社
 * [AcademicBART](https://github.com/EhimeNLP/AcademicBART) - 専門データベース CiNii Articles の論文の抽象文に BART ベースの日本語仮面言語モデルをプリトレーニングしました
 * [AcademicRoBERTa](https://github.com/EhimeNLP/AcademicRoBERTa) - 専門データベース CiNii Articlesから抽象的な論文を紙に書き込みました
 * [LINE-DistilBERT-Japanese](https://github.com/line/LINE-DistilBERT-Japanese) - DistilBERTモデルは,日本語のウェブテキストの 131 GB で予備訓練されています.教師モデルは,LINEで内部で構築されたBERTベースです.
 * [Japanese-Alpaca-LoRA](https://github.com/kunishou/Japanese-Alpaca-LoRA) - 日本語に翻訳したStanford Alpacaのデータセットを用いてLLaMAをファインチューニングし作成したLow-Rank AdapterのリンクとGenerateサンプルコード


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

 * [VRChatGPT](https://github.com/Yuchi-Games/VRChatGPT) - ChatGPTを使ってVRChat上でお喋り出来るようにするプログラム。
 * [AITuberDegikkoMirii](https://github.com/M-gen/AITuberDegikkoMirii) - AITuberの基礎となる部分を開発しています
 * [wanna](https://github.com/hirokidaichi/wanna) - 自然言語のシェルコマンドランチャー
 * [ChatdollKit](https://github.com/uezo/ChatdollKit) - ChatdollKit は 3D モデル を チャットボット に 変え ます
 * [ChuanhuChatGPTJapanese](https://github.com/gyokuro33/ChuanhuChatGPTJapanese) - ChatGPT API の GUI は 日本語 で
 * [AISisterAIChan](https://github.com/manju-summoner/AISisterAIChan) - ChatGPT3.5を搭載した伺かゴースト「AI妹アイちゃん」です。利用には別途ChatGPTのAPIキーが必要です。
 * [vrchatbot](https://github.com/Geson-anko/vrchatbot) - VRChatにAI Botを作るためのリポジトリ
 * [gptuber-by-langchain](https://github.com/karakuri-ai/gptuber-by-langchain) - GPTがYouTuberをやります
 * [openai-chatfriend](https://github.com/supershaneski/openai-chatfriend) - Open AI Text completion endpointで動力されるNuxt 3を使用して構築されたチャットボックスアプリケーション.AI友人の異なる性格を選択できます.デフォルトでは日本語で応答します.このアプリを使用してニホンゴスキルを練習できます!
 * [chrome-ext-translate-to-hiragana-with-chatgpt](https://github.com/franzwong/chrome-ext-translate-to-hiragana-with-chatgpt) - このChrome拡張子は,チャットGPTを使用して,日本語のテキストをヒラガナに翻訳することができます.
 * [azure-search-openai-demo](https://github.com/nohanaga/azure-search-openai-demo) - このサンプルでは、Retrieval Augmented Generation パターンを使用して、独自のデータに対してChatGPT のような体験を作成するためのいくつかのアプローチを示しています。


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

 * [mecab-ipadic-neologd](https://github.com/neologd/mecab-ipadic-neologd) - ウェブ上の言語資源をベースにした新語辞書 mecab-ipadic
 * [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic) - 日本語アクセント辞書生成器
 * [jamdict](https://github.com/neocl/jamdict) - Jim Breen の JMdict, KanjiDic2, JMnedict,カンジ・ラジカルマッピングを操作するための Python 3 ライブラリ
 * [unidic-py](https://github.com/polm/unidic-py) - ユニディックがパイプで設置される
 * [Japanese-Company-Lexicon](https://github.com/chakki-works/Japanese-Company-Lexicon) - 日本語辞書社 (JCLdic)
 * [manbyo-sudachi](https://github.com/yagays/manbyo-sudachi) - Sudachi向け万病辞書
 * [jawiki-kana-kanji-dict](https://github.com/tokuhirom/jawiki-kana-kanji-dict) - ウィキペディア (日本語版) から SKK/MeCab辞書を作成する
 * [JIWC-Dictionary](https://github.com/sociocom/JIWC-Dictionary) - テキストに関連する感情を見つけるための辞書
 * [JumanDIC](https://github.com/ku-nlp/JumanDIC) - このリポジトリには,JUMAN と Juman++ の辞書を作成するためのソース辞書ファイルが含まれています.
 * [ipadic-py](https://github.com/polm/ipadic-py) - IPAdic は Python から簡単に使用できるようにパッケージ化されています
 * [unidic-lite](https://github.com/polm/unidic-lite) - 簡単なパイプインストールのためのUniDicの小型バージョンです.
 * [emoji-ime-dictionary](https://github.com/peaceiris/emoji-ime-dictionary) - 日本語で絵文字入力をするための IME 追加辞書 orange_book Google 日本語入力などで日本語から絵文字への変換を可能にする IME 拡張辞書
 * [google-ime-dictionary](https://github.com/peaceiris/google-ime-dictionary) - 日英変換・英語略語展開のための IME 追加辞書 orange_book 日本語から英語への和英変換や英語略語の展開を Google 日本語入力や ATOK などで可能にする IME 拡張辞書
 * [dic-nico-intersection-pixiv](https://github.com/ncaq/dic-nico-intersection-pixiv) - ニコニコ大百科とピクシブ百科事典の共通部分のIME辞書
 * [google-ime-user-dictionary-ja-en](https://github.com/KEINOS/google-ime-user-dictionary-ja-en) - GoogleIME用カタカナ語辞書プロジェクトのアーカイブです。Google IMEユーザー辞書のプロジェクトアーカイブ.
 * [emoticon](https://github.com/tiwanari/emoticon) - Google日本語入力の顔文字辞書∩(,,Ò‿Ó,,)∩
 * [mecab-mozcdic](https://github.com/akirakubo/mecab-mozcdic) - open source mozc dictionaryをMeCab辞書のフォーマットに変換したものです。
 * [denonbu-ime-dic](https://github.com/albno273/denonbu-ime-dic) - 電音IME: Microsoft IMEなどで利用することを想定した「電音部」関連用語の辞書
 * [nijisanji-ime-dic](https://github.com/Umichang/nijisanji-ime-dic) - Microsoft IMEなどで利用することを想定した「にじさんじ」関連用語の用語辞書です。
 * [pokemon-ime-dic](https://github.com/Umichang/pokemon-ime-dic) - Microsoft IMEなどで利用することを想定した、現状判明している全てのポケモンの名前を網羅した用語辞書です。
 * [EJDict](https://github.com/kujirahand/EJDict) - 英語・日本語辞書データ (パブリック・ドメイン) EJDict-hand
 * [Ayashiy-Nipongo-Dic](https://github.com/Rinrin0413/Ayashiy-Nipongo-Dic) - 贵樣ばこゐ辞畫を使て正レい日本语を使ラことが出來ゑ。
 * [genshin-dict](https://github.com/kotofurumiya/genshin-dict) - Windows/macOSで使える原神の単語辞書です
 * [jmdict-simplified](https://github.com/scriptin/jmdict-simplified) - JSON形式のJMdictとJMnedict
 * [mozcdict-ext](https://github.com/reasonset/mozcdict-ext) - 外部の単語をMozcシステム辞書に変換する


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

 * [ner-wikipedia-dataset](https://github.com/stockmarkteam/ner-wikipedia-dataset) - Wikipediaを用いた日本語の固有表現抽出データセット
 * [IOB2Corpus](https://github.com/Hironsan/IOB2Corpus) - 日本語 IOB2 は名前のエンティティ認識のコープスをタグしました
 * [TwitterCorpus](https://github.com/tmu-nlp/TwitterCorpus) - 首都大日本語 Twitter コーパス
 * [UD_Japanese-PUD](https://github.com/megagonlabs/UD_Japanese-PUD) - Parallel Universal Dependencies.
 * [UD_Japanese-GSD](https://github.com/megagonlabs/UD_Japanese-GSD) - Google UDT 2.0 から日本語データ
 * [KWDLC](https://github.com/ku-nlp/KWDLC) - 京都大学ウェブ文書 リードコープス
 * [AnnotatedFKCCorpus](https://github.com/ku-nlp/AnnotatedFKCCorpus) - 解説されたフマン・カイトリセンターコープス


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

 * [small_parallel_enja](https://github.com/odashi/small_parallel_enja) - 機械翻訳基準の英語と日本語の50k対等コープス
 * [Web-Crawled-Corpus-for-Japanese-Chinese-NMT](https://github.com/zhang-jinyi/Web-Crawled-Corpus-for-Japanese-Chinese-NMT) - 日本語・中国語NMTのウェブクロールコープス
 * [CourseraParallelCorpusMining](https://github.com/shyyhs/CourseraParallelCorpusMining) - コルセラ コルプスマイニングと講義の翻訳を改善するための多段階精細調整
 * [JESC](https://github.com/rpryzant/JESC) - 英語と日本語の大きな並列コープス
 * [AMI-Meeting-Parallel-Corpus](https://github.com/tsuruoka-lab/AMI-Meeting-Parallel-Corpus) - AMI 会議の並行資料集
 * [giant_ja-en_parallel_corpus](https://github.com/DayuanJiang/giant_ja-en_parallel_corpus) - このディレクトリには,巨大な日本語・英語字幕コープスが含まれています. 原始データはスタンフォード大学JESCプロジェクトから得られました.
 * [jesc_small](https://github.com/yusugomori/jesc_small) - 日本語・英語字幕の小庫
 * [graded-enja-corpus](https://github.com/marmooo/graded-enja-corpus) - 禁止用語や単語レベルを考慮した日英対訳コーパスです。
 * [cjk-compsci-terms](https://github.com/dahlia/cjk-compsci-terms) - CJK computer science terms comparison / 中日韓電腦科學術語對照 / 日中韓のコンピュータ科学の用語対照 / 한·중·일 전산학 용어 대조
 * [Laboro-ParaCorpus](https://github.com/laboroai/Laboro-ParaCorpus) - 日本語・英語の並列コープスを作成し,NMTモデルを訓練するためのスクリプト
 * [google-vs-deepl-je](https://github.com/Tzawa/google-vs-deepl-je) - google-vs-deepl-je


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

 * [JMRD](https://github.com/ku-nlp/JMRD) - Japanese Movie Recommendation Dialogue dataset
 * [open2ch-dialogue-corpus](https://github.com/1never/open2ch-dialogue-corpus) - おーぷん2ちゃんねるをクロールして作成した対話コーパス
 * [BSD](https://github.com/tsuruoka-lab/BSD) - ビジネス・シーン・ダイアログ・コープス
 * [asdc](https://github.com/megagonlabs/asdc) - 宿泊施設 検索対話コーパス
 * [japanese-corpus](https://github.com/MokkeMeguru/japanese-corpus) - 日本語の対話データ for seq2seq etc
 * [BPersona-chat](https://github.com/cl-tohoku/BPersona-chat) - このリポジトリには,AACL-IJCNLP 2022のワークショップEval4NLP 2022で言語間コミュニケーションを支援するためのチャット翻訳エラー検出に関する論文に掲載された日本語・英語双語チャットコープスBPersona-chatが含まれています.
 * [japanese-daily-dialogue](https://github.com/jqk09a/japanese-daily-dialogue) - 日本語日常対話コーパス (日々の会話) は,日々の生活,学校,旅行,健康,娯楽など5つのトピックに関する日常会話を含む高品質の多回転対話データセットです.


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

 * [jrte-corpus](https://github.com/megagonlabs/jrte-corpus) - 日本語現実的なテキストエンタイルメントコープス (NLP 2020, LREC 2020)
 * [kanji-data](https://github.com/davidluzgouveia/kanji-data) - 更新されたJLPTレベルと WaniKani情報を含むJSON漢字データセット
 * [JapaneseWordSimilarityDataset](https://github.com/tmu-nlp/JapaneseWordSimilarityDataset) - 日本語語類似性データセット
 * [simple-jppdb](https://github.com/tmu-nlp/simple-jppdb) - 日本語の文簡化のためのパラフレーズデータベース
 * [chABSA-dataset](https://github.com/chakki-works/chABSA-dataset) - chakkiのアスペクトベース・センチメンタル・アナリティスデータセット
 * [JaQuAD](https://github.com/SkelterLabsInc/JaQuAD) - JaQuAD: 日本語質問回答データセット (2022年,Skelter Labs)
 * [JaNLI](https://github.com/verypluming/JaNLI) - 日本語対抗性自然言語推論データセット
 * [ebe-dataset](https://github.com/megagonlabs/ebe-dataset) - 証拠に基づく説明データセット (AACL-IJCNLP 2020)
 * [emoji-ja](https://github.com/yagays/emoji-ja) - UNICODE絵文字の日本語読み/キーワード/分類辞書
 * [nayose-wikipedia-ja](https://github.com/yagays/nayose-wikipedia-ja) - Wikipediaから作成した日本語名寄せデータセット
 * [ja.text8](https://github.com/Hironsan/ja.text8) - 日本語テキスト8コープス
 * [ThreeLineSummaryDataset](https://github.com/KodairaTomonori/ThreeLineSummaryDataset) - 3行要約データセット
 * [japanese](https://github.com/hingston/japanese) - このリポートには,リーズ大学コープスによって決定された頻度順に最も一般的な44,998の日本語のリストが含まれています.
 * [kanji-frequency](https://github.com/scriptin/kanji-frequency) - 様々な情報源から収集された漢字の使用頻度データ
 * [TEDxJP-10K](https://github.com/laboroai/TEDxJP-10K) - TEDxJP-10K ASR Evaluation Dataset
 * [CoARiJ](https://github.com/chakki-works/CoARiJ) - 日本 の 年次 報告 集
 * [technological-book-corpus-ja](https://github.com/textlint-ja/technological-book-corpus-ja) - 日本語で書かれた技術書を収集した生コーパス/ツール
 * [ita-corpus-chuwa](https://github.com/shirayu/ita-corpus-chuwa) - ITAコープスの単語の注釈
 * [wikipedia-utils](https://github.com/singletongue/wikipedia-utils) - NLPのためのウィキペディアテキストの事前処理のためのユーティリティスクリプト
 * [inappropriate-words-ja](https://github.com/MosasoM/inappropriate-words-ja) - 日本語における不適切表現を収集します。自然言語処理の時のデータクリーニング用等に使えると思います。
 * [house-of-councillors](https://github.com/smartnews-smri/house-of-councillors) - 参議院の公式ウェブサイトから会派、議員、議案、質問主意書のデータを整理しました。
 * [house-of-representatives](https://github.com/smartnews-smri/house-of-representatives) - 国会議案データベース：衆議院
 * [STAIR-captions](https://github.com/STAIR-Lab-CIT/STAIR-captions) - STAIRキャプション: 大規模な日本語画像キャプションデータセット
 * [Winograd-Schema-Challenge-Ja](https://github.com/ku-nlp/Winograd-Schema-Challenge-Ja) - ワイングラッド・スキーマ・チャレンジの日本語訳
 * [speechBSD](https://github.com/ku-nlp/speechBSD) - 音声とスピーカー属性情報を含む BSD コルプスの拡張
 * [ita-corpus](https://github.com/mmorise/ita-corpus) - ITAコーパスの文章リスト
 * [rohan4600](https://github.com/mmorise/rohan4600) - モーラバランス型日本語コーパス
 * [anlp-jp-history](https://github.com/whym/anlp-jp-history) - 言語処理学会年次大会講演の全リスト・機械可読版など
 * [keigo_transfer_task](https://github.com/cl-tohoku/keigo_transfer_task) - 敬語変換タスクにおける評価用データセット
 * [loanwords_gairaigo](https://github.com/jamesohortle/loanwords_gairaigo) - 日本語における英語の借用語
 * [jawikicorpus](https://github.com/wikiwikification/jawikicorpus) - 日本語ウィキペディアウィキペディア資料集
 * [GeneralPolicySpeechOfPrimeMinisterOfJapan](https://github.com/yuukimiyo/GeneralPolicySpeechOfPrimeMinisterOfJapan) - これは日本語のコープスです 日本首相の一般政策演説のテキストです
 * [wrime](https://github.com/ids-cv/wrime) - WRIME: 主観と客観の感情分析データセット
 * [jtubespeech](https://github.com/sarulab-speech/jtubespeech) - JTubeSpeech: YouTubeから集めた日本語語語集
 * [WikipediaWordFrequencyList](https://github.com/maeda6uiui-backup/WikipediaWordFrequencyList) - 日本語Wikipediaで使用される頻出単語のリスト
 * [kokkosho_data](https://github.com/rindybell/kokkosho_data) - 車両不具合情報に関するデータセット
 * [pdmocrdataset-part1](https://github.com/ndl-lab/pdmocrdataset-part1) - デジタル化資料OCRテキスト化事業において作成されたOCR学習用データセット
 * [huriganacorpus-ndlbib](https://github.com/ndl-lab/huriganacorpus-ndlbib) - 全国書誌データから作成した振り仮名のデータセット
 * [jvs_hiho](https://github.com/Hiroshiba/jvs_hiho) - JVS (Japanese versatile speech) コーパスの自作のラベル
 * [hirakanadic](https://github.com/po3rin/hirakanadic) - 単語のリストからヒラガナからカタカナに標準化する
 * [animedb](https://github.com/anilogia/animedb) - 約100年に渡るアニメ作品リストデータベース
 * [security_words](https://github.com/SaitoLab/security_words) - サイバーセキュリティに関連する公的な組織の日英対応
 * [Data-on-Japanese-Diet-Members](https://github.com/sugi2000/Data-on-Japanese-Diet-Members) - 日本の国会議員のデータ
 * [honkoku-data](https://github.com/yuta1984/honkoku-data) - 歴史資料の市民参加型翻刻プラットフォーム『みんなで翻刻』のテキストデータ置き場です。 / 文献文献は,日本の歴史文書のためのクラウドソーシング文献プラットフォームであるミナ・デ・ホンコク (https://honkoku.org) で作成されました.
 * [wikihow_japanese](https://github.com/Katsumata420/wikihow_japanese) - wikiHow dataset (Japanese version)
 * [engineer-vocabulary-list](https://github.com/mercari/engineer-vocabulary-list) - 日本語/英語のエンジニア語彙リスト
 * [JSICK](https://github.com/verypluming/JSICK) - 日本語文の組成知識 (JSICK) データセット/JSICKストレスのテストセット
 * [phishurl-list](https://github.com/JPCERTCC/phishurl-list) - JPCERT/CC からのフィッシング URL データセット
 * [jcms](https://github.com/shigashiyama/jcms) - 日本語コープス・オブ・マルチ・スペシャライズド・ドメイン (JCMS)
 * [aozorabunko_text](https://github.com/aozorahack/aozorabunko_text) - テキストのみのアーカイブ www.aozora.gr.jp
 * [friendly_JA-Corpus](https://github.com/astremo/friendly_JA-Corpus) - friendly_JAは,標準の中日語辞書ではなく,ラテン語/英語から派生したカタカナ辞書を使って,日本語をより簡単にすることを目的とした,日本語と日本語の並列コープスです.
 * [topokanji](https://github.com/scriptin/topokanji) - 効果的な学習のために,トポロジカルに順序付けられた漢字のリスト
 * [isbn4groups](https://github.com/uribo/isbn4groups) - ISBN-13における日本語での出版物 (978-4-XXXXXXXXX) に関するデータ等
 * [NMeCab](https://github.com/komutan/NMeCab) - NMeCab: .NETの日本語形状解析器について
 * [ndlngramdata](https://github.com/ndl-lab/ndlngramdata) - デジタル化資料から作成したOCRテキストデータのngram頻度統計情報のデータセット
 * [ndlngramviewer_v2](https://github.com/ndl-lab/ndlngramviewer_v2) - 2023年1月にリニューアルしたNDL Ngram Viewerのソースコード等一式
 * [data_set](https://github.com/japanese-law-analysis/data_set) - 法律・判例関係のデータセット
 * [huggingface-datasets_wrime](https://github.com/shunk031/huggingface-datasets_wrime) - huggingface データセットの WRIME
 * [ndl-minhon-ocrdataset](https://github.com/ndl-lab/ndl-minhon-ocrdataset) - NDL古典籍OCR学習用データセット（みんなで翻刻加工データ）
 * [PAX_SAPIENTICA](https://github.com/AsPJT/PAX_SAPIENTICA) - GIS & Archaeological Simulator. 2023 in development.
 * [j-liwc2015](https://github.com/tasukuigarashi/j-liwc2015) - 日本語版 LIWC2015
 * [huggingface-datasets_livedoor-news-corpus](https://github.com/shunk031/huggingface-datasets_livedoor-news-corpus) - 日本語 ライブドアニュースコープス 抱擁顔データセット
 * [huggingface-datasets_JGLUE](https://github.com/shunk031/huggingface-datasets_JGLUE) - JGLUE: 抱擁顔データセットの日本語一般言語理解評価
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMoralityは,日本の注釈者の常識的な道徳を反映したクラウドソーシングで作成されたデータセットです.
 * [comet-atomic-ja](https://github.com/nlp-waseda/comet-atomic-ja) - COMET-ATOMIC ja
 * [dcsg-ja](https://github.com/nlp-waseda/dcsg-ja) - 日本語での対話の共通感覚グラフ
 * [japanese-toxic-dataset](https://github.com/inspection-ai/japanese-toxic-dataset) - "日本毒性計画提案と評価"は,日本語の毒性に関する計画とデータセットを提供します.
 * [camera](https://github.com/CyberAgentAILab/camera) - CAMERA (CyberAgent Multimodal Evaluation for Ad Text GeneRAtion) は,日本の広告テキスト生成データセットである.
 * [Japanese-Fakenews-Dataset](https://github.com/tanreinama/Japanese-Fakenews-Dataset) - 日本語フェイクニュースデータセット
 * [jpn_explainable_qa_dataset](https://github.com/aiishii/jpn_explainable_qa_dataset) - jpn_explainable_qa_dataset
 * [copa-japanese](https://github.com/nlp-titech/copa-japanese) - COPA Dataset in Japanese
 * [WLSP-familiarity](https://github.com/masayu-a/WLSP-familiarity) - "セマンティック原理による単語リスト (WLSP) "の単語熟悉度
 * [ProSub](https://github.com/matbahasa/ProSub) - 代名詞とアドレス用語に関する言語間研究
 * [commonsense-moral-ja](https://github.com/Language-Media-Lab/commonsense-moral-ja) - JCommonsenseMoralityは,日本の注釈者の常識的な道徳を反映したクラウドソーシングで作成されたデータセットです.
 * [ramendb](https://github.com/nuko-yokohama/ramendb) - なんとかデータベース( https://supleks.jp/ )からのスクレイピングツールと収集データ
 * [huggingface-datasets_CAMERA](https://github.com/shunk031/huggingface-datasets_CAMERA) - CAMERA (CYBERAgent Multimodal Evaluation for Ad Text GeneRAtion) は,ハグシングフェイスデータセットの利用について
 * [FactCheckSentenceNLI-FCSNLI-](https://github.com/nlp-waseda/FactCheckSentenceNLI-FCSNLI-) - フォクトチェックNLIデータセット
 * [databricks-dolly-15k-ja](https://github.com/kunishou/databricks-dolly-15k-ja) - databricks/dolly-v2-12b の学習データに使用されたdatabricks-dolly-15k.jsonl を日本語に翻訳したデータセットになります。
 * [EaST-MELD](https://github.com/ku-nlp/EaST-MELD) - EaST-MELDは,MELDをベースとした感情意識のスピーチ翻訳のための英語・日本語データセットです.
 * [meconaudio](https://github.com/elith-co-jp/meconaudio) - Mecon Audio(Medical Conference Audio)は厚生労働省主催の先進医療会議の議事録の読み上げデータセットです。


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
|[meconaudio](https://github.com/elith-co-jp/meconaudio)|-|-|![GitHub Repo stars](https://img.shields.io/github/stars/elith-co-jp/meconaudio?style=social)|


## Tutorial

 * [spacy_tutorial](https://github.com/yuibi/spacy_tutorial) - インターフェースや コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ,コンピュータ
 * [fastTextJapaneseTutorial](https://github.com/icoxfog417/fastTextJapaneseTutorial) - 日本語コープスで速読のトレーニングのチュートリアル
 * [allennlp-NER-ja](https://github.com/shunk031/allennlp-NER-ja) - AllenNLP-NER-ja: AllenNLP による日本語を対象とした固有表現抽出
 * [chariot-PyTorch-Japanese-text-classification](https://github.com/ymym3412/chariot-PyTorch-Japanese-text-classification) - 日本語のテキスト分類実験 カーツとPyTorchを用いる
 * [ginza-examples](https://github.com/poyo46/ginza-examples) - 日本語NLPライブラリGiNZAのすゝめ
 * [DocumentClassificationUsingBERT-Japanese](https://github.com/nekoumei/DocumentClassificationUsingBERT-Japanese) - 文書分類 ベルト語-日本語
 * [BERT_Japanese_Google_Colaboratory](https://github.com/YutaroOgawa/BERT_Japanese_Google_Colaboratory) - Google Colaboratoryで日本語のBERTを動かす方法です.
 * [bert-book](https://github.com/stockmarkteam/bert-book) - 「BERTによる自然言語処理入門: Transformersを使った実践プログラミング」サポートページ
 * [janome-tutorial](https://github.com/mocobeta/janome-tutorial) - Janome を使ったテキストマイニング入門チュートリアルです。
 * [handson-language-models](https://github.com/hnishi/handson-language-models) - 日本語の言語モデルのハンズオン資料です
 * [JapaneseNLI](https://github.com/verypluming/JapaneseNLI) - Google Colabで日本語テキスト推論を試す
 * [deep-learning-with-pytorch-ja](https://github.com/Gin5050/deep-learning-with-pytorch-ja) - ディープラーニングの日本語版リポジトリです.
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

 * [awesome-bert-japanese](https://github.com/himkt/awesome-bert-japanese) - 日本語のための事前訓練された BERT モデルのリスト,単語/サブワードトークネージ + 語彙構築アルゴリズム情報
 * [GEC-Info-ja](https://github.com/gotutiyan/GEC-Info-ja) - 文法誤り訂正に関する日本語文献を収集・分類するためのリポジトリ
 * [dataset-list](https://github.com/ikegami-yukino/dataset-list) - テキストコーポスやその他 (主に日本語) のリスト
 * [tuning_playbook_ja](https://github.com/Valkyrja3607/tuning_playbook_ja) - ディープラーニングモデルの性能を体系的に最大化するためのプレイブック
 * [japanese-pitch-accent-resources](https://github.com/olety/japanese-pitch-accent-resources) - 日本語音の音声,特に音声のアクセントを1つのリストにまとめようとしています


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
