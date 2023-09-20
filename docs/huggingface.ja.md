# awesome-japanese-nlp-resources

このページは、Huggingfaceに登録されている日本語NLPに特化したモデルとデータセットの一覧です。現在、137のモデルと27のデータセットが掲載されています。

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)


## Contents

 * [Models](#models)
 * [Datasets](#datasets)


## Models

 * [tsmatz/xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - xlm-roberta-ner-japanese（日本語キャプション：日本語の固有表現抽出のモデル）このモデルは、名前付きエンティティ認識（NER）トークン分類のためにトレーニングされた、事前学習済みのクロスリンガルRobertaModelであるxlm-roberta-baseの微調整バージョンです。
 * [jonatasgrosman/wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 日本語音声認識のためのファインチューニングされたXLSR-53大型モデル。Common Voice 6.1、CSS10、JSUTのトレーニングと検証データを使用して、日本語のファインチューニングを行ったfacebook/wav2vec2-large-xlsr-53モデルです。このモデルを使用する際には、音声入力が16kHzでサンプリングされていることを確認してください。
 * [cl-tohoku/bert-base-japanese-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-whole-word-masking) - BERTベース日本語（IPA辞書、全単語マスキング有効）
 * [cl-tohoku/bert-base-japanese](https://huggingface.co/cl-tohoku/bert-base-japanese) - BERTベース日本語（IPA辞書）
 * [christian-phu/bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - bert-finetuned-japanese-sentiment
このモデルは、商品のアマゾンレビューの日本語データセット上でcl-tohoku/bert-base-japanese-v2のファインチューニングを行ったバージョンです。
 * [ku-nlp/deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 日本語DeBERTa V2ベースモデルのモデルカード
説明：これは日本語DeBERTa V2ベースモデルであり、日本語のWikipedia、CC-100の日本語部分、およびOSCARの日本語部分で事前学習されています。
 * [sonoisa/sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - これは日本語のSentence-BERTモデルです。
 * [ku-nlp/deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 日本語の文字レベルDeBERTa V2ベースモデルのモデルカード説明
これは、日本語のDeBERTa V2ベースモデルであり、日本語のWikipedia、CC-100の日本語部分、およびOSCARの日本語部分で事前学習されています。このモデルは文字レベルのトークン化と全単語マスキングで訓練されています。
 * [cl-tohoku/bert-base-japanese-char](https://huggingface.co/cl-tohoku/bert-base-japanese-char) - BERTベース日本語（文字トークン化）
 * [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) - Sentence BERTベースの日本語モデル このリポジトリには、日本語のSentence BERTベースモデルが含まれています。
 * [kha-white/manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 日本語のテキストに対するマンガOCR（光学文字認識）で、主な焦点は日本のマンガです。
 * [megagonlabs/transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - transformers-ud-japanese-electra-ginza-510（sudachitra-wordpiece、mC4 Japanese）
 * [cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - OpenCALM-7Bモデルの説明
OpenCALMは、日本のデータセットで事前にトレーニングされたデコーダー専用の言語モデルのスイートです。
 * [staka/fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - FuguMT
 * [cl-tohoku/bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3) - 入力: BERTベース日本語（unidic-lite with whole word masking、CC-100、jawiki-20230102）
出力:
 * [rinna/japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16) - rinna / japanese-cloob-vit-b-16
りんな/日本のクローブビタミンB-16
 * [cl-tohoku/bert-base-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2) - BERTベース日本語（文字レベルのトークン化と全単語マスキング、jawiki-20200831）
 * [sonoisa/t5-base-japanese-title-generation](https://huggingface.co/sonoisa/t5-base-japanese-title-generation) - 記事本文からタイトルを生成するモデル SEE:
 * [rinna/japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - 入力: japanese-roberta-base このリポジトリは、ベースサイズの日本語RoBERTaモデルを提供します。
 * [elyza/ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - ELYZA-japanese-Llama-2-7b モデルの説明
ELYZA-japanese-Llama-2-7b は、Llama2をベースにして日本語の能力を拡張するために追加の事前学習を行ったモデルです。
 * [kit-nlp/bert-base-japanese-sentiment-irony](https://huggingface.co/kit-nlp/bert-base-japanese-sentiment-irony) - BERTベースの日本語アイロニー
 * [sociocom/MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - これは日本の医療文書の固有表現認識のためのモデルです。
 * [jarvisx17/japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - japanese-sentiment-analysis このモデルはchABSAデータセットを使ってゼロからトレーニングされました。
 * [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 日本語T5事前学習済みモデルは、日本語のコーパスで事前学習されたT5（テキストからテキストへの転送トランスフォーマー）モデルです。
 * [sonoisa/sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - これは日本語の文章-LUKEモデルです。
 * [staka/fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - FuguMT
 * [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) - 入力: Japanese SimCSE (BERT-base) 日本語のREADME/Japanese README サマリーモデル名: pkshatech/simcse-ja-bert-base-clcmlp これは日本語のSimCSEモデルです。
 * [Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - このモデルはLuke-japanese-large-liteをファインチューニングしたものです。
 * [ku-nlp/deberta-v2-tiny-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm) - 日本語の文字レベルDeBERTa V2 tinyモデルのモデルカード説明
これは、日本語のDeBERTa V2 tinyモデルであり、日本語のWikipedia、CC-100の日本語部分、およびOSCARの日本語部分で事前学習されています。このモデルは文字レベルのトークン化と全単語マスキングで訓練されています。
 * [rinna/japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) - japanese-gpt-neox-3.6b 概要 このリポジトリは、36億パラメータの日本語GPT-NeoXモデルを提供します。
 * [elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - ELYZA-japanese-Llama-2-7b モデルの説明 ELYZA-japanese-Llama-2-7b は、 Llama2 をベースとして日本語能力を拡張するために追加事前学習を行ったモデルです。
 * [abeja/gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - gpt-neox-japanese-2.7b
 * [line-corporation/line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - LINE DistilBERT Japanese これは、131 GBの日本語ウェブテキストで事前学習されたDistilBERTモデルです。
 * [line-corporation/japanese-large-lm-3.6b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft) - japanese-large-lm-3.6b-instruction-sft
日本語-大規模-LM-3.6b-指示-SFT
 * [rinna/japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - japanese-gpt-1b このリポジトリは、13億パラメータの日本語GPTモデルを提供します。
 * [stabilityai/japanese-instructblip-alpha](https://huggingface.co/stabilityai/japanese-instructblip-alpha) - 日本語 InstructBLIP アルファモデルの詳細 日本語 InstructBLIP アルファは、入力画像やオプションで質問などの入力テキストに対して、日本語の説明を生成することができるビジョン言語命令従属モデルです。
 * [cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - OpenCALM-3Bモデルの説明
OpenCALMは、日本のデータセットで事前にトレーニングされたデコーダー専用の言語モデルのスイートです。
 * [cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large) - OpenCALM-Largeモデルの説明
OpenCALMは、日本のデータセットで事前にトレーニングされたデコーダー専用の言語モデルのスイートです。
 * [cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) - OpenCALM-1Bモデルの説明
OpenCALMは、日本のデータセットで事前にトレーニングされたデコーダー専用の言語モデルのスイートです。
 * [cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - OpenCALM-Smallモデルの説明
OpenCALMは、日本のデータセットで事前にトレーニングされたデコーダー専用の言語モデルのスイートです。
 * [ku-nlp/deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 日本語DeBERTa V2 tinyモデルのモデルカードの説明
 * [stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b) - このリポジトリは一般公開されていますが、ファイルやコンテンツにアクセスするためには条件を受け入れる必要があります。
 * [cl-tohoku/bert-large-japanese-v2](https://huggingface.co/cl-tohoku/bert-large-japanese-v2) - 入力: BERT large 日本語 (unidic-lite with whole word masking, CC-100 and jawiki-20230102)
出力:
 * [elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - ELYZA-japanese-Llama-2-7b モデルの説明 ELYZA-japanese-Llama-2-7b は、 Llama2 をベースとして日本語能力を拡張するために追加事前学習を行ったモデルです。
 * [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - japanese-gpt-neox-3.6b-instruction-sft-v2 概要
 * [rinna/japanese-hubert-base](https://huggingface.co/rinna/japanese-hubert-base) - 入力: japanese-hubert-base これは、りんな株式会社によって訓練された日本語HuBERT（Hidden Unit Bidirectional Encoder Representations from Transformers）モデルです。
 * [cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - OpenCALM-Mediumモデルの説明
OpenCALMは、日本のデータセットで事前にトレーニングされたデコーダー専用の言語モデルのスイートです。
 * [studio-ousia/luke-japanese-base-lite](https://huggingface.co/studio-ousia/luke-japanese-base-lite) - luke-japaneseは、LUKE（Language Understanding with Knowledge-based Embeddings）の日本語版であり、単語とエンティティの知識を強化したコンテキスト化された事前学習モデルです。
 * [elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - ELYZA-japanese-Llama-2-7b モデルの説明 ELYZA-japanese-Llama-2-7b は、 Llama2 をベースとして日本語能力を拡張するために追加事前学習を行ったモデルです。
 * [cl-tohoku/bert-large-japanese](https://huggingface.co/cl-tohoku/bert-large-japanese) - 入力: BERT large 日本語（unidic-lite with whole word masking, jawiki-20200831）
出力:
 * [speechbrain/lang-id-voxlingua107-ecapa](https://huggingface.co/speechbrain/lang-id-voxlingua107-ecapa) - VoxLingua107 ECAPA-TDNN話者言語識別モデル
モデルの説明：このモデルは、SpeechBrainを使用してVoxLingua107データセットでトレーニングされた話者言語識別モデルです。
 * [rinna/japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - japanese-gpt2-small このリポジトリは、小規模な日本語のGPT-2モデルを提供します。
 * [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) - bilingual-gpt-neox-4b-instruction-ppo
概要：このリポジトリは、38億パラメータの英日バイリンガルGPT-NeoXモデルを提供します。
 * [kit-nlp/bert-base-japanese-sentiment-cyberbullying](https://huggingface.co/kit-nlp/bert-base-japanese-sentiment-cyberbullying) - electra-base-cyberbullying
これは、自動的なサイバーいじめ検出のためにファインチューニングされた日本語のBERTベースモデルです。
 * [ku-nlp/roberta-base-japanese-char-wwm](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) - 入力: ku-nlp/roberta-base-japanese-char-wwm モデルの説明 これは、日本語のRoBERTaベースモデルであり、日本語のWikipediaとCC-100の日本語部分で事前学習されています。このモデルは、文字レベルのトークン化と全単語マスキングで訓練されています。
 * [line-corporation/japanese-large-lm-1.7b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft) - japanese-large-lm-1.7b-instruction-sft
このリポジトリは、LINE株式会社によって微調整および訓練された1.7Bパラメータの日本語言語モデルを提供しています。
 * [rinna/bilingual-gpt-neox-4b-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k) - bilingual-gpt-neox-4b-8k 概要 注意事項：このモデルを正しく動作させるには、transformers&gt;=4.31.0が必要です。
 * [sonoisa/t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 日本語T5事前学習済みモデルは、日本語のコーパスで事前学習されたT5（テキストからテキストへの転送トランスフォーマー）モデルです。
 * [nlp-waseda/roberta-large-japanese-seq512](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512) - nlp-waseda/roberta-large-japanese-seq512 モデルの説明 これは、日本語のWikipediaとCC-100の日本語部分で事前学習されたRoBERTaの大規模なモデルで、最大シーケンス長は512です。
 * [studio-ousia/luke-japanese-large](https://huggingface.co/studio-ousia/luke-japanese-large) - luke-japanese-largeは、LUKE（言語理解と知識ベースの埋め込みを利用した）の日本語版です。LUKEは、単語やエンティティの知識を強化したコンテキスト化された事前学習モデルです。
 * [cl-tohoku/bert-base-japanese-char-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v3) - BERTベース日本語（文字レベルのトークン化、全単語マスキング、CC-100およびjawiki-20230102）
 * [stockmark/gpt-neox-japanese-1.4b](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b) - stockmark/gpt-neox-japanese-1.4b
このリポジトリは、約20Bトークンの日本語コーパスで事前学習された1.4Bパラメータを持つGPT-NeoXベースのモデルを提供しています。
 * [llm-book/bert-base-japanese-v3-jnli](https://huggingface.co/llm-book/bert-base-japanese-v3-jnli) - bert-base-japanese-v3-jnli 「大規模言語モデル入門」の第5章で紹介している(自然言語推論)のモデルです。
 * [abeja/gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - gpt2-large-japanese このリポジトリは、大規模な日本語のGPT-2モデルを提供します。
 * [rinna/japanese-stable-diffusion](https://huggingface.co/rinna/japanese-stable-diffusion) - このモデルを手に入れる前に、もう一歩進んでください。
 * [nlp-waseda/roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - nlp-waseda/roberta-base-japanese モデルの説明 これは、日本語のWikipediaとCC-100の日本語部分で事前学習された日本語RoBERTaベースモデルです。
 * [cl-tohoku/bert-base-japanese-char-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-char-whole-word-masking) - BERTベース日本語（文字トークン化、全単語マスキング有効）
 * [turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0) - ヘロンBLIP日本語ステーブルLM
 * [stanfordnlp/stanza-ja](https://huggingface.co/stanfordnlp/stanza-ja) - 日本語のスタンザモデル
 * [llm-book/bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - bert-base-japanese-v3-jsts 「大規模言語モデル入門」の第5章で紹介している(意味類似度計算)のモデルです。
 * [Formzu/bert-base-japanese-jsnli](https://huggingface.co/Formzu/bert-base-japanese-jsnli) - 入力: bert-base-japanese-jsnli このモデルは、JSNLIデータセット上でcl-tohoku/bert-base-japanese-v2の微調整バージョンです。
 * [sonoisa/clip-vit-b-32-japanese-v1](https://huggingface.co/sonoisa/clip-vit-b-32-japanese-v1) - 日本語版CLIPモデル
 * [llm-book/bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - bert-base-japanese-v3-marc_ja 「大規模言語モデル入門」の第5章で紹介している(感情分析)のモデルです。
 * [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) - AIBunCho/japanese-novel-gpt-j-6bは、AI BunChoで利用しているモデルです。
 * [nlp-waseda/roberta-large-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp) - モデルの説明：nlp-waseda/roberta-large-japanese-with-auto-jumanpp
 * [llm-book/bert-base-japanese-v3-unsup-simcse-jawiki](https://huggingface.co/llm-book/bert-base-japanese-v3-unsup-simcse-jawiki) - bert-base-japanese-v3-unsup-simcse-jawikiは、「大規模言語モデル入門」の第8章で紹介されている教師なしSimCSEのモデルです。
 * [cl-tohoku/bert-large-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-large-japanese-char-v2) - BERT large 日本語（文字レベルのトークン化、全単語マスキング、CC-100およびjawiki-20230102）
 * [larryvrh/mt5-translation-ja_zh](https://huggingface.co/larryvrh/mt5-translation-ja_zh) - これは、日本語を簡体字中国語に翻訳するためのgoogle/mt5-largeの微調整版です。
 * [studio-ousia/luke-japanese-base](https://huggingface.co/studio-ousia/luke-japanese-base) - luke-japaneseは、LUKE（Knowledge-based Embeddingsを使用した言語理解）の日本語版です。LUKEは、単語やエンティティの事前学習済みの知識強化コンテキスト表現です。
luke-japaneseは、LUKE（Knowledge-based Embeddingsを使用した言語理解）の日本語版です。LUKEは、単語やエンティティの事前学習済みの知識強化コンテキスト表現です。
 * [ku-nlp/deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 日本語の文字レベルDeBERTa V2 largeモデルのモデルカード説明
これは、日本語のDeBERTa V2 largeモデルであり、日本語のWikipedia、CC-100の日本語部分、およびOSCARの日本語部分で事前学習されています。このモデルは文字レベルのトークン化と全単語マスキングで訓練されています。
 * [nlp-waseda/roberta-base-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) - nlp-waseda/roberta-base-japanese-with-auto-jumanpp モデルの説明
 * [ku-nlp/bart-large-japanese](https://huggingface.co/ku-nlp/bart-large-japanese) - 日本のBART大規模モデルのモデルカードの説明
 * [llm-book/bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - llm-book/bert-base-japanese-v3-ner-wikipedia-datasetは、「大規模言語モデル入門」の第6章で紹介されている固有表現認識のモデルです。
 * [tsmatz/mt5_summarize_japanese](https://huggingface.co/tsmatz/mt5_summarize_japanese) - mt5_summarize_japanese（日本語キャプション：日本語の要約のモデル）このモデルは、日本語の要約のためにトレーニングされたgoogle/mt5-smallの微調整バージョンです。
 * [stockmark/bart-base-japanese-news](https://huggingface.co/stockmark/bart-base-japanese-news) - bart-base-japanese-news（ベースサイズのモデル）
 * [ybelkada/japanese-roberta-question-answering](https://huggingface.co/ybelkada/japanese-roberta-question-answering) - RoBERTaベース日本語 - JaQuADディスクリプション
JaQuADで微調整された日本語の質問応答モデルです。事前学習モデルの詳細については、RoBERTaベース日本語を参照してください。
 * [ku-accms/bert-base-japanese-ssuw](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) - 入力: ku-accms/bert-base-japanese-ssuw モデルの説明 これは、スーパーショートユニットワード（SSUW）用の事前学習済みの日本語BERTベースモデルです。
 * [alabnii/jmedroberta-base-sentencepiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece-vocab50000) - alabnii/jmedroberta-base-sentencepiece-vocab50000 モデルの説明 これは、日本の科学技術振興機構（JST）によって収集された医学科学の学術論文で事前学習された日本語RoBERTaベースモデルです。このモデルはクリエイティブ・コモンズ4.0国際ライセンス（CC BY-NC-SA 4.0）の下で公開されています。
 * [llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset) - llm-book/bert-base-japanese-v3-crf-ner-wikipedia-datasetは、「大規模言語モデル入門」の第6章で紹介されている固有表現認識のモデルです。
 * [inu-ai/dolly-japanese-gpt-1b](https://huggingface.co/inu-ai/dolly-japanese-gpt-1b) - 更新履歴 2023年5月7日「oasst1-89k-ja」データセットを追加して対話システムに対応しました。
 * [ptaszynski/yacis-electra-small-japanese-cyberbullying](https://huggingface.co/ptaszynski/yacis-electra-small-japanese-cyberbullying) - yacis-electra-small-cyberbullying
yacis-electra-small-cyberbullying
 * [nlp-waseda/comet-t5-base-japanese](https://huggingface.co/nlp-waseda/comet-t5-base-japanese) - COMET-T5とFinetuned T5は、ATOMICを使用してテキストからテキストへの言語モデリングを行っています。
 * [MuneK/bert-large-japanese-v2-finetuned-wrime](https://huggingface.co/MuneK/bert-large-japanese-v2-finetuned-wrime) - bert-large-japanese-v2-finetuned-wrime
 * [ku-nlp/gpt2-medium-japanese-char](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char) - モデルカード：日本語の文字レベルGPT-2 Mediumモデルの説明
このモデルは、日本語の文字レベルGPT-2 Medium（310Mパラメータ）言語モデルであり、日本語のWikipedia、CC-100の日本語部分、およびOSCARの日本語部分で事前学習されています。
 * [turing-motors/heron-chat-git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0) - ヘロンGIT日本語安定版LM
 * [izumi-lab/bert-small-japanese-fin](https://huggingface.co/izumi-lab/bert-small-japanese-fin) - BERT small 日本の金融
これは、日本語のテキストで事前学習されたBERTモデルです。
 * [nlp-waseda/roberta-large-japanese](https://huggingface.co/nlp-waseda/roberta-large-japanese) - nlp-waseda/roberta-large-japanese モデルの説明 これは、日本語のWikipediaとCC-100の日本語部分で事前学習された日本語RoBERTaの大規模モデルです。
 * [dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ](https://huggingface.co/dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ) - モデルIDオリジナルモデルelyza/ELYZA-japanese-Llama-2-7b-fast-instructは、Metaの「Llama 2」をベースにしており、日本語での追加の事前トレーニング、元のポストトレーニング、および高速化チューニングを経験しています。
 * [studio-ousia/luke-japanese-large-lite](https://huggingface.co/studio-ousia/luke-japanese-large-lite) - luke-japanese-large-liteは、LUKE（言語理解と知識ベースの埋め込みを利用した）の日本語版です。LUKEは、単語やエンティティの文脈に即した事前学習済みの知識強化型埋め込み表現です。
 * [alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000) - alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000 モデルの説明 これは、日本の科学技術振興機構（JST）が収集した医学の学術論文を元に事前学習された日本語RoBERTaベースモデルです。このモデルはクリエイティブ・コモンズ4.0国際ライセンス（CC BY-NC-SA 4.0）の下で公開されています。
 * [Mizuiro-sakura/luke-japanese-base-finetuned-ner](https://huggingface.co/Mizuiro-sakura/luke-japanese-base-finetuned-ner) - このモデルはluke-japanese-baseをファインチューニングして、固有表現抽出（NER）に用いれるようにしたものです。
 * [nlp-waseda/gpt2-small-japanese](https://huggingface.co/nlp-waseda/gpt2-small-japanese) - nlp-waseda/gpt2-small-japanese
このモデルは、日本語のWikipediaとCC-100で事前学習された日本語GPT-2です。
 * [hajime9652/xlnet-japanese](https://huggingface.co/hajime9652/xlnet-japanese) - XLNet-japaneseモデルの説明。このモデルは、MecabとsenetencepieceをXLNetTokenizerと共に必要とします。
 * [KoichiYasuoka/bert-base-japanese-upos](https://huggingface.co/KoichiYasuoka/bert-base-japanese-upos) - 入力: bert-base-japanese-upos モデルの説明
 * [sonoisa/t5-base-english-japanese](https://huggingface.co/sonoisa/t5-base-english-japanese) - 入力: 英語+日本語T5事前学習済みモデル これは、英語と日本語のバランスの取れたコーパスで事前学習されたT5（テキストからテキストへの転送トランスフォーマー）モデルです。
 * [ken11/albert-base-japanese-v1](https://huggingface.co/ken11/albert-base-japanese-v1) - albert-base-japanese-v1は、日本語事前学習済みのALBERTモデルです。
 * [alabnii/jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - alabnii/jmedroberta-base-sentencepiece モデルの説明 これは、日本の科学技術振興機構（JST）によって収集された医学科学の学術論文で事前学習された日本語RoBERTaベースモデルです。このモデルはクリエイティブ・コモンズ4.0国際ライセンス（CC BY-NC-SA 4.0）の下で公開されています。
 * [NTQAI/wav2vec2-large-japanese](https://huggingface.co/NTQAI/wav2vec2-large-japanese) - Common Voice、JSUT、TEDxJPなどのデータを使用して、Wav2Vec2-Large-Japanese Fine-tuned facebook/wav2vec2-large-xlsr-53を日本語でファインチューニングしました。
 * [ku-nlp/deberta-v2-base-japanese-with-auto-jumanpp](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-with-auto-jumanpp) - 日本語DeBERTa V2ベースモデルのモデルカード
説明：このモデルは、日本語Wikipedia、CC-100の日本語部分、およびOSCARの日本語部分で事前学習された日本語DeBERTa V2ベースモデルです。
 * [uzabase/luke-japanese-wordpiece-base](https://huggingface.co/uzabase/luke-japanese-wordpiece-base) - studio-ousia/luke-japanese-baseに対して次の変更を加えたモデルです。
 * [izumi-lab/bert-base-japanese-fin-additional](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional) - 追加の事前学習済みBERTベースの日本語金融モデルです。このモデルは日本語のテキストで事前学習されたBERTモデルです。
 * [KoichiYasuoka/bert-base-japanese-wikipedia-ud-head](https://huggingface.co/KoichiYasuoka/bert-base-japanese-wikipedia-ud-head) - 入力: bert-base-japanese-wikipedia-ud-head モデルの説明
 * [TeamFnord/manga-ocr](https://huggingface.co/TeamFnord/manga-ocr) - 日本語のテキストに対するマンガOCR（光学文字認識）で、主な焦点は日本のマンガです。
 * [clu-ling/whisper-large-v2-japanese-5k-steps](https://huggingface.co/clu-ling/whisper-large-v2-japanese-5k-steps) - whisper-large-v2-japanese-5k-steps
このモデルは、日本語のCommonVoiceデータセット（v11）でopenai/whisper-large-v2の微調整バージョンです。
 * [sonoisa/t5-base-japanese-article-generation](https://huggingface.co/sonoisa/t5-base-japanese-article-generation) - タイトルから記事本文を生成するモデル SEE:
 * [minutillamolinara/bert-japanese_finetuned-sentiment-analysis](https://huggingface.co/minutillamolinara/bert-japanese_finetuned-sentiment-analysis) - bert-japanese_finetuned-sentiment-analysis このモデルは、日本の感情極性辞書データセットを元にゼロからトレーニングされました。
 * [KoichiYasuoka/deberta-base-japanese-aozora-ud-head](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-aozora-ud-head) - モデルの説明：deberta-base-japanese-aozora-ud-head
 * [reazon-research/reazonspeech-espnet-next](https://huggingface.co/reazon-research/reazonspeech-espnet-next) - reazonspeech-espnet-next
ReazonSpeechは、日本語のオーディオデータセットとMLモデルを自由に利用できるようにするプロジェクトです。reazonspeech-espnet-nextは、ReazonSpeechチームによって訓練された最新のASRモデルが含まれる「最先端」のリポジトリです。
 * [alabnii/jmedroberta-base-manbyo-wordpiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece) - alabnii/jmedroberta-base-manbyo-wordpiece モデルの説明 これは、日本科学技術振興機構（JST）が収集した医学科学の学術論文を元に事前学習された日本語RoBERTaベースモデルです。このモデルはクリエイティブ・コモンズ4.0国際ライセンス（CC BY-NC-SA 4.0）の下で公開されています。
 * [izumi-lab/bert-small-japanese](https://huggingface.co/izumi-lab/bert-small-japanese) - BERT small Japanese finance
これは、日本語のテキストで事前学習されたBERTモデルです。
 * [ku-nlp/bart-base-japanese](https://huggingface.co/ku-nlp/bart-base-japanese) - 日本語BARTベースモデルのモデルカード
モデルの説明：これは日本語Wikipediaで事前学習された日本語BARTベースモデルです。
 * [izumi-lab/electra-small-japanese-fin-discriminator](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator) - ELECTRA小規模日本語金融判別器。これは、日本語のテキストで事前学習されたELECTRAモデルです。
 * [ku-nlp/deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 日本語DeBERTa V2大規模モデルのモデルカード説明
これは、日本語DeBERTa V2大規模モデルであり、日本語のWikipedia、CC-100の日本語部分、およびOSCARの日本語部分で事前学習されています。
 * [oshizo/sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - sbert-jsnli-luke-japanese-base-lite
これはsentence-transformersモデルです：文や段落を768次元の密なベクトル空間にマッピングし、クラスタリングや意味的な検索などのタスクに使用することができます。
 * [rinna/japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 以下の内容を日本語に翻訳してください。

"Hello, how are you today? I hope you're doing well. I wanted to ask if you have any plans for the weekend. It would be great to catch up and spend some time together. Let me know what you think. Have a great day!"
 * [Tanrei/GPTSAN-japanese](https://huggingface.co/Tanrei/GPTSAN-japanese) - タンレイ/GPTSAN-日本語一般目的スイッチトランスフォーマーベースの日本語言語モデルGPTSANにはいくつかのユニークな特徴があります。
 * [line-corporation/japanese-large-lm-1.7b](https://huggingface.co/line-corporation/japanese-large-lm-1.7b) - 入力: japanese-large-lm-1.7b このリポジトリは、LINE株式会社によって訓練された1.7Bパラメータの日本語言語モデルを提供しています。
 * [jurabi/bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - BERTによる日本語固有表現抽出のモデル BertForTokenClassificationを用いて、日本語の文から固有表現を抽出します。
 * [rinna/japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft) - japanese-gpt-neox-3.6b-instruction-sft
概要：このリポジトリは、36億パラメータの日本語GPT-NeoXモデルを提供します。
 * [rinna/japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - 入力: japanese-gpt-neox-small このリポジトリは、小規模な日本語のGPT-NeoXモデルを提供します。
 * [line-corporation/japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) - japanese-large-lm-3.6b
 * [rinna/japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - このリポジトリは、中規模の日本語GPT-2モデルを提供しています。
 * [rinna/japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - rinna / japanese-clip-vit-b-16
 * [sonoisa/sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - これは日本語のSentence-BERTモデルです。
 * [cl-tohoku/bert-base-japanese-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-v2) - 入力: BERTベース日本語（unidic-lite with whole word masking, jawiki-20200831）
出力:
 * [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - japanese-gpt-neox-3.6b-instruction-ppo
概要：このリポジトリは、36億パラメータの日本語GPT-NeoXモデルを提供します。
 * [stabilityai/japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) - Japanese-StableLM-Base-Alpha-7B「日本語、浮世絵、江戸時代を話すことができるオウム」- Stable Diffusion XLモデルの説明 japanese-stablelm-base-alpha-7bは、日本語の言語モデリング性能と日本語の下流タスクの性能を最大化することに焦点を当てた、多様な日本語と英語のデータセットで事前学習された7Bパラメータのデコーダー専用言語モデルです。


## Datasets

 * [mkshing/xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - これは、XL-Sumのフィルタリングされた日本語のサブセットで、PaLM 2filters15-gram overlap*コードに続くものです：https://gist.github.com/mkshing/d6371cbfdd50d4f352cee247fd4dd86a
例の数：
トレーニング：4215（以前：7113）
検証：758（以前：889）
テスト：766（以前：889）
 * [turing-motors/LLaVA-Instruct-150K-JA](https://huggingface.co/datasets/turing-motors/LLaVA-Instruct-150K-JA) - データセットの詳細 データセットタイプ：日本語LLaVA Instruct 150Kは、元のLLaVA Visual Instruct 150Kデータセットのローカライズバージョンです。
 * [izumi-lab/llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - llm-japanese-dataset LLM構築用の日本語インストラクション(チャット)データセット主に，英語で構築されたLLMモデルなどに対して，チャット(Instruction)応答タスクに関してLoRAなどでチューニングするために使用できます．
 * [SkelterLabsInc/JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - JaQuADデータセットのデータセットカード
JaQuADデータセットの概要
JaQuAD（Japanese Question Answering Dataset）は、2022年にリリースされた日本語の機械読解のために作成された人手によるアノテーションされたデータセットです。
 * [datasets/snow_simplified_japanese_corpus](https://huggingface.co/datasets/snow_simplified_japanese_corpus) - SNOW T15とT23（簡易日本語コーパス）のデータセットカード
 * [zan/lima-ja](https://huggingface.co/datasets/zan/lima-ja) - LIMA-JAデータセットのデータセットカード
説明：これは日本語のLIMAデータセットであり、MetaのLIMAモデル（Zhou et al.、2023）で訓練されたLIMAデータセットを翻訳したものです。
 * [fujiki/japanese_alpaca_data](https://huggingface.co/datasets/fujiki/japanese_alpaca_data) - 「japanese_alpaca_data」のデータセットカード
このデータセットは、masa3141さんの素晴らしい作品である「japanese-alpaca-lora」に基づいています。
 * [Atsushi/fungi_indexed_mycological_papers_japanese](https://huggingface.co/datasets/Atsushi/fungi_indexed_mycological_papers_japanese) - fungi_indexed_mycological_papers_japanese大菌輪「論文3行まとめ」データセット最終更新日：2023/8/26（R3-10914まで）==== 言語 日本語 このデータセットは日本語のみで利用可能です。
 * [taishi-i/nagisa_stopwords](https://huggingface.co/datasets/taishi-i/nagisa_stopwords) - 渚のための日本語のストップワード
 * [hpprc/janli](https://huggingface.co/datasets/hpprc/janli) - JaNLIデータセットの概要のためのデータセットカード
 * [izumi-lab/llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - llm-japanese-dataset-vanillaは、izumi-lab/llm-japanese-datasetから抜き出した日本語のチャットデータセットです。日英翻訳のデータセットなどは含まれていません。
 * [sudy-super/dialogsum-ja](https://huggingface.co/datasets/sudy-super/dialogsum-ja) - dialogsum-jaこのデータセットはdialogsum、CSDSなどを翻訳した日本語対話要約データセットです。
 * [shunk031/jsnli](https://huggingface.co/datasets/shunk031/jsnli) - Dataset Card for JSNLI Dataset Summary 日本語 SNLI(JSNLI) データセット - KUROHASHI-CHU-MURAWAKI LAB より：本データセットは自然言語推論 (NLI) の標準的ベンチマークである SNLI を日本語に翻訳したものです。
 * [fujiki/guanaco_ja](https://huggingface.co/datasets/fujiki/guanaco_ja) - これはグアナコデータセットの日本語部分です。
 * [range3/wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - range3 / wiki40b-ja
このデータセットは、日本語のデータのみを抽出したwiki40bデータセットの3つのparquetファイルで構成されています。
 * [nakayama/hh-rlhf-helpful-base-ja](https://huggingface.co/datasets/nakayama/hh-rlhf-helpful-base-ja) - https://github.com/anthropics/hh-rlhf の内容のうち、helpful-base内のchosenに記載されている英文をfuguMTで翻訳、うまく翻訳できていないものを除外、修正したものです。
 * [larryvrh/WikiMatrix-v1-Ja_Zh-filtered](https://huggingface.co/datasets/larryvrh/WikiMatrix-v1-Ja_Zh-filtered) - WikiMatrix v1からの日本語/中国語言語ペアデータのフィルタリングおよび修正版。処理手順：異常なペアを除去するための基本的な正規表現に基づくフィルタリング/長さのチェック。
 * [if001/aozorabunko-clean-sin](https://huggingface.co/datasets/if001/aozorabunko-clean-sin) - これはフォークですhttps://huggingface.co/datasets/globis-university/aozorabunko-cleanfilteredrow["meta"]["文字遣い種別"] == "新字新仮名"
 * [saldra/sakura_japanese_dataset](https://huggingface.co/datasets/saldra/sakura_japanese_dataset) - Sakura_dataset 商用利用可能な超小規模高品質日本語データセット。
 * [range3/cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - range3/cc100-ja
このデータセットは、日本語のみが抽出され、シャードされたcc100データセットのパーケットファイルから成り立っています。
 * [elyza/ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - ELYZA-tasks-100: 日本語instructionモデル評価データセット Data Description 本データセットはinstruction-tuningを行ったモデルの評価用データセットです。
 * [AhmedSSabir/Japanese-wiki-dump-sentence-dataset](https://huggingface.co/datasets/AhmedSSabir/Japanese-wiki-dump-sentence-dataset) - データセット5M（5121625）は、コンテキストを含むクリーンな日本語の完全な文章です。
 * [fujiki/japanese_hh-rlhf-49k](https://huggingface.co/datasets/fujiki/japanese_hh-rlhf-49k) - これは、ng_translation == 1の例を除いた、kunishou/hh-rlhf-49k-jaの少し異なるバージョンです。
 * [Atsushi/fungi_diagnostic_chars_comparison_japanese](https://huggingface.co/datasets/Atsushi/fungi_diagnostic_chars_comparison_japanese) - fungi_diagnostic_chars_comparison_japanese大菌輪「識別形質まとめ」データセット最終更新日：2023/8/26（R3-10914まで）
言語：日本語
このデータセットは日本語のみで利用可能です。
 * [datasets/covid_tweets_japanese](https://huggingface.co/datasets/covid_tweets_japanese) - COVID-19 日本語Twitterデータセットのデータセットカード
 * [datasets/bsd_ja_en](https://huggingface.co/datasets/bsd_ja_en) - ビジネスシーンの対話のためのデータセットカード
 * [reazon-research/reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - ReazonSpeechデータセットのデータセットカード
要約：ReazonSpeechは、日本のテレビ番組から収集された大規模な音声コーパスです。
