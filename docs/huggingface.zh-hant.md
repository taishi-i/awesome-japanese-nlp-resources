# awesome-japanese-nlp-resources

此頁面列出了註冊在 [Haggingface](https://huggingface.co) 的專用於日本NLP的模型和數據集。目前，列出了137個模型和27個數據集。

[English](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.en.md) | [日本語 (Japanese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.ja.md) | [繁體中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hant.md) | [简体中文 (Chinese) ](https://github.com/taishi-i/awesome-japanese-nlp-resources/blob/main/docs/huggingface.zh-hans.md)


## Contents

 * [Models](#models)
 * [Datasets](#datasets)


## Models

 * [tsmatz/xlm-roberta-ner-japanese](https://huggingface.co/tsmatz/xlm-roberta-ner-japanese) - xlm-roberta-ner-japanese（日語標題：日本語の固有表現抽出のモデル）此模型是xlm-roberta-base的微調版本（預先訓練的跨語言RobertaModel），用於命名實體識別（NER）的標記分類。
 * [jonatasgrosman/wav2vec2-large-xlsr-53-japanese](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-japanese) - 針對日語語音識別進行微調的XLSR-53大型模型，使用Common Voice 6.1、CSS10和JSUT的訓練和驗證數據集對facebook/wav2vec2-large-xlsr-53進行微調。使用此模型時，請確保您的語音輸入以16kHz進行取樣。
 * [cl-tohoku/bert-base-japanese-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-whole-word-masking) - BERT基礎日語（IPA字典，啟用整詞遮罩）
 * [cl-tohoku/bert-base-japanese](https://huggingface.co/cl-tohoku/bert-base-japanese) - BERT基礎日語（IPA字典）
 * [christian-phu/bert-finetuned-japanese-sentiment](https://huggingface.co/christian-phu/bert-finetuned-japanese-sentiment) - bert-finetuned-japanese-sentiment 這個模型是在產品亞馬遜評論日本數據集上對 cl-tohoku/bert-base-japanese-v2 進行微調的版本。
 * [ku-nlp/deberta-v2-base-japanese](https://huggingface.co/ku-nlp/deberta-v2-base-japanese) - 日本DeBERTa V2基礎模型的模型卡描述
這是一個在日本維基百科、CC-100的日本部分和OSCAR的日本部分上預訓練的日本DeBERTa V2基礎模型。
 * [sonoisa/sentence-bert-base-ja-mean-tokens-v2](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens-v2) - 這是一個日本的句子BERT模型。
 * [ku-nlp/deberta-v2-base-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-char-wwm) - 日本角色級DeBERTa V2基本模型的模型卡描述
這是一個在日本維基百科、CC-100的日本部分和OSCAR的日本部分上預訓練的日本DeBERTa V2基本模型。該模型使用角色級的分詞和整詞遮罩進行訓練。
 * [cl-tohoku/bert-base-japanese-char](https://huggingface.co/cl-tohoku/bert-base-japanese-char) - BERT基礎日文（字符分詞）
 * [colorfulscoop/sbert-base-ja](https://huggingface.co/colorfulscoop/sbert-base-ja) - Sentence BERT基礎日本模型 這個儲存庫包含了一個用於日本語的Sentence BERT基礎模型。
 * [kha-white/manga-ocr-base](https://huggingface.co/kha-white/manga-ocr-base) - 漫畫OCR光學字符識別，主要專注於日本漫畫。
 * [megagonlabs/transformers-ud-japanese-electra-base-ginza-510](https://huggingface.co/megagonlabs/transformers-ud-japanese-electra-base-ginza-510) - transformers-ud-japanese-electra-ginza-510（sudachitra-wordpiece，mC4日語）
 * [cyberagent/open-calm-7b](https://huggingface.co/cyberagent/open-calm-7b) - OpenCALM-7B 模型描述 OpenCALM 是一套仅解码器的语言模型，预先在日本数据集上进行了训练，由开发。
 * [staka/fugumt-ja-en](https://huggingface.co/staka/fugumt-ja-en) - 河豚MT
 * [cl-tohoku/bert-base-japanese-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-v3) - BERT基礎日語（使用unidic-lite進行整詞遮罩，CC-100和jawiki-20230102）
 * [rinna/japanese-cloob-vit-b-16](https://huggingface.co/rinna/japanese-cloob-vit-b-16) - rinna / 日本衣物Vit B-16
 * [cl-tohoku/bert-base-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v2) - BERT基礎日語（以字元級別進行分詞，使用整詞遮罩，jawiki-20200831）
 * [sonoisa/t5-base-japanese-title-generation](https://huggingface.co/sonoisa/t5-base-japanese-title-generation) - 從文章生成標題的模型 SEE:
 * [rinna/japanese-roberta-base](https://huggingface.co/rinna/japanese-roberta-base) - japanese-roberta-base 這個存儲庫提供了一個基本大小的日語 RoBERTa 模型。
 * [elyza/ELYZA-japanese-Llama-2-7b-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-instruct) - ELYZA-japanese-Llama-2-7b 模型描述 ELYZA-japanese-Llama-2-7b 是在 Llama2 的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [kit-nlp/bert-base-japanese-sentiment-irony](https://huggingface.co/kit-nlp/bert-base-japanese-sentiment-irony) - BERT基礎日語用於諷刺
 * [sociocom/MedNER-CR-JA](https://huggingface.co/sociocom/MedNER-CR-JA) - 這是一個用於日本醫療文件中的命名實體識別的模型。
 * [jarvisx17/japanese-sentiment-analysis](https://huggingface.co/jarvisx17/japanese-sentiment-analysis) - 日本情感分析 這個模型是從頭開始在chABSA數據集上訓練的。
日本情感分析 這個模型是從頭開始在chABSA數據集上訓練的。
 * [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) - 日本語T5事前學習完成的模型。這是一個在日本語語料庫上預先訓練的T5（文本到文本轉換Transformer）模型。
 * [sonoisa/sentence-luke-japanese-base-lite](https://huggingface.co/sonoisa/sentence-luke-japanese-base-lite) - 這是一個日本句子-LUKE模型。
 * [staka/fugumt-en-ja](https://huggingface.co/staka/fugumt-en-ja) - 河豚MT
 * [pkshatech/simcse-ja-bert-base-clcmlp](https://huggingface.co/pkshatech/simcse-ja-bert-base-clcmlp) - 日本語のSimCSE（BERT-base）日本語のREADME/Japanese README サマリーモデル名：pkshatech/simcse-ja-bert-base-clcmlp これは日本語のSimCSEモデルです。
 * [Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime) - 這個模型是對Luke-japanese-large-lite進行微調的結果。
 * [ku-nlp/deberta-v2-tiny-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese-char-wwm) - 日本角色級DeBERTa V2微型模型的模型卡描述
這是一個在日本維基百科、CC-100的日本部分和OSCAR的日本部分上預訓練的日本DeBERTa V2微型模型。該模型使用字符級的分詞和整詞遮罩進行訓練。
 * [rinna/japanese-gpt-neox-3.6b](https://huggingface.co/rinna/japanese-gpt-neox-3.6b) - japanese-gpt-neox-3.6b 概述 這個存儲庫提供了一個擁有36億個參數的日語GPT-NeoX模型。
 * [elyza/ELYZA-japanese-Llama-2-7b-fast-instruct](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast-instruct) - ELYZA-japanese-Llama-2-7b 模型描述 ELYZA-japanese-Llama-2-7b 是在 Llama2 的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [abeja/gpt-neox-japanese-2.7b](https://huggingface.co/abeja/gpt-neox-japanese-2.7b) - gpt-neox-japanese-2.7b
 * [line-corporation/line-distilbert-base-japanese](https://huggingface.co/line-corporation/line-distilbert-base-japanese) - LINE DistilBERT 日文這是一個在131 GB的日本網頁文本上預先訓練的DistilBERT模型。
 * [line-corporation/japanese-large-lm-3.6b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-3.6b-instruction-sft) - 日語大型語言模型3.6B指令SFT
 * [rinna/japanese-gpt-1b](https://huggingface.co/rinna/japanese-gpt-1b) - japanese-gpt-1b 這個儲存庫提供了一個擁有13億參數的日文GPT模型。
 * [stabilityai/japanese-instructblip-alpha](https://huggingface.co/stabilityai/japanese-instructblip-alpha) - 日本InstructBLIP Alpha模型詳細日本InstructBLIP Alpha是一個視覺語言指導模型，可以為輸入圖像生成日本描述，並可選擇性地輸入文本，如問題。
 * [cyberagent/open-calm-3b](https://huggingface.co/cyberagent/open-calm-3b) - OpenCALM-3B 模型描述
OpenCALM 是一套仅解码器的語言模型，預先在日本數據集上進行了預訓練。
 * [cyberagent/open-calm-large](https://huggingface.co/cyberagent/open-calm-large) - OpenCALM-Large 模型描述
OpenCALM 是一套仅解码器的語言模型套件，使用日本數據集進行預訓練，由開發。
 * [cyberagent/open-calm-1b](https://huggingface.co/cyberagent/open-calm-1b) - OpenCALM-1B 模型描述 OpenCALM 是一套仅解码器的语言模型，预先在日本数据集上进行训练和开发。
 * [cyberagent/open-calm-small](https://huggingface.co/cyberagent/open-calm-small) - OpenCALM-Small 模型描述 OpenCALM 是一套僅解碼器的語言模型，預先在日本數據集上進行了預訓練，由開發。

OpenCALM-Small 模型描述 OpenCALM 是一套僅解碼器的語言模型，預先在日本數據集上進行了預訓練，由開發。
 * [ku-nlp/deberta-v2-tiny-japanese](https://huggingface.co/ku-nlp/deberta-v2-tiny-japanese) - 日本DeBERTa V2微型模型的模型卡描述
 * [stabilityai/japanese-stablelm-instruct-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-instruct-alpha-7b) - 這個存儲庫是公開可訪問的，但您必須接受條件才能訪問其文件和內容。
 * [cl-tohoku/bert-large-japanese-v2](https://huggingface.co/cl-tohoku/bert-large-japanese-v2) - BERT大型日語模型（使用unidic-lite進行整詞遮罩，CC-100和jawiki-20230102）
 * [elyza/ELYZA-japanese-Llama-2-7b-fast](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b-fast) - ELYZA-japanese-Llama-2-7b 模型描述 ELYZA-japanese-Llama-2-7b 是在 Llama2 的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [rinna/japanese-gpt-neox-3.6b-instruction-sft-v2](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft-v2) - japanese-gpt-neox-3.6b-instruction-sft-v2 概述
 * [rinna/japanese-hubert-base](https://huggingface.co/rinna/japanese-hubert-base) - japanese-hubert-base 這是由rinna有限公司訓練的日本HuBERT（Hidden Unit Bidirectional Encoder Representations from Transformers）模型。
 * [cyberagent/open-calm-medium](https://huggingface.co/cyberagent/open-calm-medium) - OpenCALM-Medium 模型描述
OpenCALM 是一套仅解码器的語言模型套件，使用日本數據集預訓練，由開發。
 * [studio-ousia/luke-japanese-base-lite](https://huggingface.co/studio-ousia/luke-japanese-base-lite) - luke-japanese luke-japanese 是 LUKE（基於知識嵌入的語言理解）的日文版本，它是一種預訓練的知識增強上下文化詞語和實體表示方法。
 * [elyza/ELYZA-japanese-Llama-2-7b](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b) - ELYZA-japanese-Llama-2-7b 模型描述 ELYZA-japanese-Llama-2-7b 是在 Llama2 的基础上进行了额外的预训练，以扩展日语能力的模型。
 * [cl-tohoku/bert-large-japanese](https://huggingface.co/cl-tohoku/bert-large-japanese) - BERT大型日語（使用unidic-lite與整詞遮罩，jawiki-20200831）
 * [speechbrain/lang-id-voxlingua107-ecapa](https://huggingface.co/speechbrain/lang-id-voxlingua107-ecapa) - VoxLingua107 ECAPA-TDNN 語言辨識模型模型描述這是一個使用SpeechBrain在VoxLingua107數據集上訓練的口語語言識別模型。
 * [rinna/japanese-gpt2-small](https://huggingface.co/rinna/japanese-gpt2-small) - japanese-gpt2-small 這個儲存庫提供了一個小型的日文 GPT-2 模型。
 * [rinna/bilingual-gpt-neox-4b-instruction-ppo](https://huggingface.co/rinna/bilingual-gpt-neox-4b-instruction-ppo) - bilingual-gpt-neox-4b-instruction-ppo 概述 本存儲庫提供了一個具有38億參數的英日雙語GPT-NeoX模型。
 * [kit-nlp/bert-base-japanese-sentiment-cyberbullying](https://huggingface.co/kit-nlp/bert-base-japanese-sentiment-cyberbullying) - electra-base-cyberbullying 這是一個針對日語的BERT Base模型，用於自動檢測網絡霸凌。
electra-base-cyberbullying 這是一個針對日語的BERT Base模型，用於自動檢測網絡霸凌。
 * [ku-nlp/roberta-base-japanese-char-wwm](https://huggingface.co/ku-nlp/roberta-base-japanese-char-wwm) - ku-nlp/roberta-base-japanese-char-wwm 模型描述 這是一個在日本維基百科和CC-100的日文部分上預訓練的日本RoBERTa基礎模型。該模型使用字符級別的分詞和整詞遮罩進行訓練。
 * [line-corporation/japanese-large-lm-1.7b-instruction-sft](https://huggingface.co/line-corporation/japanese-large-lm-1.7b-instruction-sft) - japanese-large-lm-1.7b-instruction-sft 這個資料庫提供了由LINE Corporation微調和訓練的1.7B參數的日語語言模型。
 * [rinna/bilingual-gpt-neox-4b-8k](https://huggingface.co/rinna/bilingual-gpt-neox-4b-8k) - bilingual-gpt-neox-4b-8k 概述通知：此模型需要 transformers&gt;=4.31.0 才能正常運作。
 * [sonoisa/t5-base-japanese-v1.1](https://huggingface.co/sonoisa/t5-base-japanese-v1.1) - 日本語T5事前學習完成的模型。這是一個在日本語語料庫上預先訓練的T5（文本到文本轉換Transformer）模型。
日本語T5事前學習完成的模型。這是一個在日本語語料庫上預先訓練的T5（文本到文本轉換Transformer）模型。
 * [nlp-waseda/roberta-large-japanese-seq512](https://huggingface.co/nlp-waseda/roberta-large-japanese-seq512) - nlp-waseda/roberta-large-japanese-seq512 模型描述 這是一個在日本維基百科和CC-100的日本部分上預訓練的日本RoBERTa大型模型，最大序列長度為512。
 * [studio-ousia/luke-japanese-large](https://huggingface.co/studio-ousia/luke-japanese-large) - luke-japanese-large是LUKE（具有知識增強的語言理解）的日語版本，它是一種預訓練的知識增強上下文化詞語和實體表示方法。
 * [cl-tohoku/bert-base-japanese-char-v3](https://huggingface.co/cl-tohoku/bert-base-japanese-char-v3) - BERT基礎日語（以字元為單位進行分詞，使用整詞遮罩，CC-100和jawiki-20230102）
 * [stockmark/gpt-neox-japanese-1.4b](https://huggingface.co/stockmark/gpt-neox-japanese-1.4b) - stockmark/gpt-neox-japanese-1.4b 這個存儲庫提供了一個基於1.4B參數的GPT-NeoX模型，該模型在約20B個令牌的日語語料庫上進行了預訓練。
 * [llm-book/bert-base-japanese-v3-jnli](https://huggingface.co/llm-book/bert-base-japanese-v3-jnli) - bert-base-japanese-v3-jnli 是《大規模言語模型入門》第5章介紹的(自然語言推論)模型。
 * [abeja/gpt2-large-japanese](https://huggingface.co/abeja/gpt2-large-japanese) - gpt2-large-japanese 這個儲存庫提供了一個大型的日本語GPT-2模型。
 * [rinna/japanese-stable-diffusion](https://huggingface.co/rinna/japanese-stable-diffusion) - 在獲得這個型號之前還有一個步驟。
 * [nlp-waseda/roberta-base-japanese](https://huggingface.co/nlp-waseda/roberta-base-japanese) - nlp-waseda/roberta-base-japanese 模型描述 這是一個在日本維基百科和CC-100的日文部分上預訓練的日本RoBERTa基礎模型。
 * [cl-tohoku/bert-base-japanese-char-whole-word-masking](https://huggingface.co/cl-tohoku/bert-base-japanese-char-whole-word-masking) - BERT基礎日語（使用字符分詞，啟用整詞遮罩）
 * [turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-blip-ja-stablelm-base-7b-v0) - Heron BLIP 日本穩定LM
 * [stanfordnlp/stanza-ja](https://huggingface.co/stanfordnlp/stanza-ja) - 日本的詩節模型（ja）
 * [llm-book/bert-base-japanese-v3-jsts](https://huggingface.co/llm-book/bert-base-japanese-v3-jsts) - bert-base-japanese-v3-jsts 是在「大規模言語模型入門」第5章中介紹的(意義相似度計算)模型。
 * [Formzu/bert-base-japanese-jsnli](https://huggingface.co/Formzu/bert-base-japanese-jsnli) - bert-base-japanese-jsnli 這個模型是在JSNLI數據集上對cl-tohoku/bert-base-japanese-v2進行微調的版本。
 * [sonoisa/clip-vit-b-32-japanese-v1](https://huggingface.co/sonoisa/clip-vit-b-32-japanese-v1) - 日本語版CLIP模型
 * [llm-book/bert-base-japanese-v3-marc_ja](https://huggingface.co/llm-book/bert-base-japanese-v3-marc_ja) - bert-base-japanese-v3-marc_ja 是在「大規模言語模型入門」第5章中介紹的(情感分析)模型。
 * [AIBunCho/japanese-novel-gpt-j-6b](https://huggingface.co/AIBunCho/japanese-novel-gpt-j-6b) - AIBunCho/japanese-novel-gpt-j-6b 是 AI BunCho 使用的模型。
 * [nlp-waseda/roberta-large-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-large-japanese-with-auto-jumanpp) - nlp-waseda/roberta-large-japanese-with-auto-jumanpp 模型描述
 * [llm-book/bert-base-japanese-v3-unsup-simcse-jawiki](https://huggingface.co/llm-book/bert-base-japanese-v3-unsup-simcse-jawiki) - bert-base-japanese-v3-unsup-simcse-jawiki 是在「大規模言語モデル入門」第8章中介紹的教師無監督SimCSE模型。
 * [cl-tohoku/bert-large-japanese-char-v2](https://huggingface.co/cl-tohoku/bert-large-japanese-char-v2) - BERT大型日語模型（以字元級別進行分詞，使用整詞遮罩，包含CC-100和jawiki-20230102）
 * [larryvrh/mt5-translation-ja_zh](https://huggingface.co/larryvrh/mt5-translation-ja_zh) - 這是google/mt5-large的微調版本，用於將日語翻譯成簡體中文。
 * [studio-ousia/luke-japanese-base](https://huggingface.co/studio-ousia/luke-japanese-base) - luke-japanese是LUKE（基於知識增強的語言理解）的日文版本，它是一種預訓練的知識增強上下文化詞語和實體表示方法。
 * [ku-nlp/deberta-v2-large-japanese-char-wwm](https://huggingface.co/ku-nlp/deberta-v2-large-japanese-char-wwm) - 日本角色級DeBERTa V2大型模型的模型卡描述
這是一個在日本維基百科、CC-100的日本部分和OSCAR的日本部分上預訓練的日本DeBERTa V2大型模型。該模型使用角色級的分詞和整詞遮罩進行訓練。
 * [nlp-waseda/roberta-base-japanese-with-auto-jumanpp](https://huggingface.co/nlp-waseda/roberta-base-japanese-with-auto-jumanpp) - nlp-waseda/roberta-base-japanese-with-auto-jumanpp 模型描述
 * [ku-nlp/bart-large-japanese](https://huggingface.co/ku-nlp/bart-large-japanese) - 日本BART大型模型描述的模型卡
 * [llm-book/bert-base-japanese-v3-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-ner-wikipedia-dataset) - llm-book/bert-base-japanese-v3-ner-wikipedia-dataset 是在「大規模言語模型入門」第6章中介紹的專有名詞識別模型。
 * [tsmatz/mt5_summarize_japanese](https://huggingface.co/tsmatz/mt5_summarize_japanese) - mt5_summarize_japanese（日語標題：日本語の要約のモデル）此模型是針對日本語摘要訓練的google/mt5-small的微調版本。
 * [stockmark/bart-base-japanese-news](https://huggingface.co/stockmark/bart-base-japanese-news) - bart-base-japanese-news（基本大小模型）
 * [ybelkada/japanese-roberta-question-answering](https://huggingface.co/ybelkada/japanese-roberta-question-answering) - RoBERTa基礎日語 - JaQuAD描述一個在JaQuAD上微調的日語問答模型。有關預訓練模型的詳細信息，請參閱RoBERTa基礎日語。
 * [ku-accms/bert-base-japanese-ssuw](https://huggingface.co/ku-accms/bert-base-japanese-ssuw) - ku-accms/bert-base-japanese-ssuw 模型描述 這是一個預訓練的日語BERT基礎模型，用於超短單位詞（SSUW）。
 * [alabnii/jmedroberta-base-sentencepiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece-vocab50000) - alabnii/jmedroberta-base-sentencepiece-vocab50000 模型描述 這是一個基於日本RoBERTa的基礎模型，該模型是在日本科學技術振興機構（JST）收集的醫學科學學術文章上進行預訓練的。該模型釋出在創作共用4.0國際許可證（CC BY-NC-SA 4.0）下。
 * [llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset](https://huggingface.co/llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset) - llm-book/bert-base-japanese-v3-crf-ner-wikipedia-dataset 是在「大規模言語モデル入門」第6章中介紹的固有表現識別模型。
 * [inu-ai/dolly-japanese-gpt-1b](https://huggingface.co/inu-ai/dolly-japanese-gpt-1b) - 更新歷史 2023年5月7日「oasst1-89k-ja」資料集已新增並支援對話系統。
 * [ptaszynski/yacis-electra-small-japanese-cyberbullying](https://huggingface.co/ptaszynski/yacis-electra-small-japanese-cyberbullying) - yacis-electra-small-cyberbullying
 * [nlp-waseda/comet-t5-base-japanese](https://huggingface.co/nlp-waseda/comet-t5-base-japanese) - COMET-T5和Finetuned T5是使用ATOMIC和文本到文本語言建模目標的。
 * [MuneK/bert-large-japanese-v2-finetuned-wrime](https://huggingface.co/MuneK/bert-large-japanese-v2-finetuned-wrime) - bert-large-japanese-v2-finetuned-wrime
 * [ku-nlp/gpt2-medium-japanese-char](https://huggingface.co/ku-nlp/gpt2-medium-japanese-char) - 日本角色級GPT-2中型模型的模型卡描述
這是一個日本角色級GPT-2中型（310M參數）的語言模型，預先在日本維基百科、CC-100的日本部分和OSCAR的日本部分上進行了預訓練。
 * [turing-motors/heron-chat-git-ja-stablelm-base-7b-v0](https://huggingface.co/turing-motors/heron-chat-git-ja-stablelm-base-7b-v0) - Heron GIT 日本穩定LM
 * [izumi-lab/bert-small-japanese-fin](https://huggingface.co/izumi-lab/bert-small-japanese-fin) - BERT小型日本金融這是一個在日本語言文本上預訓練的BERT模型。
 * [nlp-waseda/roberta-large-japanese](https://huggingface.co/nlp-waseda/roberta-large-japanese) - nlp-waseda/roberta-large-japanese 模型描述 這是一個在日本維基百科和CC-100的日文部分上預訓練的日文RoBERTa大型模型。
 * [dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ](https://huggingface.co/dahara1/ELYZA-japanese-Llama-2-7b-fast-instruct-GPTQ) - 模型ID為原始模型elyza/ELYZA-japanese-Llama-2-7b-fast-instruct的模型卡，該模型基於Meta的「Llama 2」，並在日語中進行了額外的預訓練，以及原始的後訓練和加速調整。
 * [studio-ousia/luke-japanese-large-lite](https://huggingface.co/studio-ousia/luke-japanese-large-lite) - luke-japanese-large-lite luke-japanese 是 LUKE（具有知識增強的語言理解）的日語版本，它是一種預訓練的知識增強上下文化詞語和實體表示方法。
 * [alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000) - alabnii/jmedroberta-base-manbyo-wordpiece-vocab50000 模型描述 這是一個基於日本RoBERTa的基礎模型，它是在日本科學技術振興機構（JST）收集的醫學科學學術文章上進行預訓練的。該模型釋出在創作共用4.0國際許可證（CC BY-NC-SA 4.0）下。
 * [Mizuiro-sakura/luke-japanese-base-finetuned-ner](https://huggingface.co/Mizuiro-sakura/luke-japanese-base-finetuned-ner) - 這個模型是通過對luke-japanese-base進行微調，使其能夠用於命名實體識別（NER）。
 * [nlp-waseda/gpt2-small-japanese](https://huggingface.co/nlp-waseda/gpt2-small-japanese) - nlp-waseda/gpt2-small-japanese 這個模型是在日本維基百科和CC-100上預訓練的日本GPT-2模型。
 * [hajime9652/xlnet-japanese](https://huggingface.co/hajime9652/xlnet-japanese) - XLNet日文模型描述。此模型需要Mecab和senetencepiece與XLNetTokenizer。
 * [KoichiYasuoka/bert-base-japanese-upos](https://huggingface.co/KoichiYasuoka/bert-base-japanese-upos) - bert-base-japanese-upos 模型描述
 * [sonoisa/t5-base-english-japanese](https://huggingface.co/sonoisa/t5-base-english-japanese) - 英語+日本語T5事前學習完成模型 這是一個在英語和日語平衡語料庫上預先訓練的T5（文本到文本轉換Transformer）模型。
 * [ken11/albert-base-japanese-v1](https://huggingface.co/ken11/albert-base-japanese-v1) - albert-base-japanese-v1 是一個已經事前學習的日本語ALBERT模型。
 * [alabnii/jmedroberta-base-sentencepiece](https://huggingface.co/alabnii/jmedroberta-base-sentencepiece) - alabnii/jmedroberta-base-sentencepiece 模型描述 這是一個基於日本RoBERTa的基礎模型，它是在日本科學技術振興機構（JST）收集的醫學科學學術文章上進行預訓練的。該模型釋出在創作共用4.0國際許可證（CC BY-NC-SA 4.0）下。
 * [NTQAI/wav2vec2-large-japanese](https://huggingface.co/NTQAI/wav2vec2-large-japanese) - 使用Common Voice、JSUT、TEDxJP和其他一些數據，對日語進行微調的Wav2Vec2-Large-Japanese Fine-tuned facebook/wav2vec2-large-xlsr-53模型。
 * [ku-nlp/deberta-v2-base-japanese-with-auto-jumanpp](https://huggingface.co/ku-nlp/deberta-v2-base-japanese-with-auto-jumanpp) - 日本DeBERTa V2基礎模型的模型卡描述
這是一個在日本維基百科、CC-100的日本部分和OSCAR的日本部分上預訓練的日本DeBERTa V2基礎模型。
 * [uzabase/luke-japanese-wordpiece-base](https://huggingface.co/uzabase/luke-japanese-wordpiece-base) - 這是對studio-ousia/luke-japanese-base進行的修改模型。
 * [izumi-lab/bert-base-japanese-fin-additional](https://huggingface.co/izumi-lab/bert-base-japanese-fin-additional) - 額外預訓練的BERT基礎日本金融這是一個在日本語文本上預訓練的BERT模型。
額外預訓練的BERT基礎日本金融這是一個在日本語文本上預訓練的BERT模型。
 * [KoichiYasuoka/bert-base-japanese-wikipedia-ud-head](https://huggingface.co/KoichiYasuoka/bert-base-japanese-wikipedia-ud-head) - bert-base-japanese-wikipedia-ud-head 模型描述
 * [TeamFnord/manga-ocr](https://huggingface.co/TeamFnord/manga-ocr) - 漫畫OCR光學字符識別，主要專注於日本漫畫。
 * [clu-ling/whisper-large-v2-japanese-5k-steps](https://huggingface.co/clu-ling/whisper-large-v2-japanese-5k-steps) - whisper-large-v2-japanese-5k-steps 這個模型是在日本CommonVoice數據集（v11）上對openai/whisper-large-v2進行微調的版本。
 * [sonoisa/t5-base-japanese-article-generation](https://huggingface.co/sonoisa/t5-base-japanese-article-generation) - 從標題生成文章內容的模型 SEE:
 * [minutillamolinara/bert-japanese_finetuned-sentiment-analysis](https://huggingface.co/minutillamolinara/bert-japanese_finetuned-sentiment-analysis) - bert-japanese_finetuned-sentiment-analysis 這個模型是從頭開始在日本情感極性詞典數據集上進行訓練的。
 * [KoichiYasuoka/deberta-base-japanese-aozora-ud-head](https://huggingface.co/KoichiYasuoka/deberta-base-japanese-aozora-ud-head) - deberta-base-japanese-aozora-ud-head 模型描述
 * [reazon-research/reazonspeech-espnet-next](https://huggingface.co/reazon-research/reazonspeech-espnet-next) - reazonspeech-espnet-next是一個項目，旨在維護免費提供的日語音頻數據集和ML模型。reazonspeech-espnet-next是一個“最新技術”的存儲庫，其中包含由ReazonSpeech團隊訓練的最新ASR模型。
 * [alabnii/jmedroberta-base-manbyo-wordpiece](https://huggingface.co/alabnii/jmedroberta-base-manbyo-wordpiece) - alabnii/jmedroberta-base-manbyo-wordpiece 模型描述 這是一個基於日本RoBERTa的基礎模型，該模型是在日本科學技術振興機構（JST）收集的醫學科學學術文章上進行預訓練的。該模型釋出在創作共用4.0國際許可證（CC BY-NC-SA 4.0）下。
 * [izumi-lab/bert-small-japanese](https://huggingface.co/izumi-lab/bert-small-japanese) - BERT小型日本金融這是一個在日本語言文本上預訓練的BERT模型。
 * [ku-nlp/bart-base-japanese](https://huggingface.co/ku-nlp/bart-base-japanese) - 日本BART基模型的模型卡片描述
這是一個在日本維基百科上預先訓練的日本BART基模型。
 * [izumi-lab/electra-small-japanese-fin-discriminator](https://huggingface.co/izumi-lab/electra-small-japanese-fin-discriminator) - ELECTRA小型日本金融辨識器。這是一個在日本語文本上預訓練的ELECTRA模型。
 * [ku-nlp/deberta-v2-large-japanese](https://huggingface.co/ku-nlp/deberta-v2-large-japanese) - 日本DeBERTa V2大型模型的模型卡描述
這是一個在日本維基百科、CC-100的日本部分和OSCAR的日本部分上預訓練的日本DeBERTa V2大型模型。
 * [oshizo/sbert-jsnli-luke-japanese-base-lite](https://huggingface.co/oshizo/sbert-jsnli-luke-japanese-base-lite) - sbert-jsnli-luke-japanese-base-lite 這是一個句子轉換模型：它將句子和段落映射到一個768維的密集向量空間，可用於聚類或語義搜索等任務。
 * [rinna/japanese-gpt2-xsmall](https://huggingface.co/rinna/japanese-gpt2-xsmall) - 請將以下內容翻譯成繁體中文。

japanese-gpt2-xsmall
請將以下內容翻譯成繁體中文。
 * [Tanrei/GPTSAN-japanese](https://huggingface.co/Tanrei/GPTSAN-japanese) - Tanrei/GPTSAN-日本通用開關變壓器基於日語的語言模型的模型卡具有一些獨特的功能。
Tanrei/GPTSAN-日本通用開關變壓器基於日語的語言模型GPTSAN具有一些獨特的功能。
 * [line-corporation/japanese-large-lm-1.7b](https://huggingface.co/line-corporation/japanese-large-lm-1.7b) - japanese-large-lm-1.7b 這個資料庫提供了由LINE Corporation訓練的1.7B參數的日語語言模型。
 * [jurabi/bert-ner-japanese](https://huggingface.co/jurabi/bert-ner-japanese) - 使用BERT的日本語固有表現抽出模型BertForTokenClassification，從日本語文本中提取固有表現。
 * [rinna/japanese-gpt-neox-3.6b-instruction-sft](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-sft) - japanese-gpt-neox-3.6b-instruction-sft 概述 這個存儲庫提供了一個擁有36億個參數的日語GPT-NeoX模型。
 * [rinna/japanese-gpt-neox-small](https://huggingface.co/rinna/japanese-gpt-neox-small) - japanese-gpt-neox-small 這個儲存庫提供了一個小型的日文 GPT-NeoX 模型。
 * [line-corporation/japanese-large-lm-3.6b](https://huggingface.co/line-corporation/japanese-large-lm-3.6b) - 日本大型語言模型3.6億
 * [rinna/japanese-gpt2-medium](https://huggingface.co/rinna/japanese-gpt2-medium) - japanese-gpt2-medium 這個儲存庫提供了一個中型的日文 GPT-2 模型。
 * [rinna/japanese-clip-vit-b-16](https://huggingface.co/rinna/japanese-clip-vit-b-16) - rinna/japanese-clip-vit-b-16
 * [sonoisa/sentence-bert-base-ja-mean-tokens](https://huggingface.co/sonoisa/sentence-bert-base-ja-mean-tokens) - 這是一個日本的句子BERT模型。
 * [cl-tohoku/bert-base-japanese-v2](https://huggingface.co/cl-tohoku/bert-base-japanese-v2) - BERT基礎日語（使用unidic-lite與整詞遮罩，jawiki-20200831）
 * [rinna/japanese-gpt-neox-3.6b-instruction-ppo](https://huggingface.co/rinna/japanese-gpt-neox-3.6b-instruction-ppo) - japanese-gpt-neox-3.6b-instruction-ppo 概述 本存儲庫提供了一個具有36億參數的日語GPT-NeoX模型。
 * [stabilityai/japanese-stablelm-base-alpha-7b](https://huggingface.co/stabilityai/japanese-stablelm-base-alpha-7b) - 日本穩定LM基礎Alpha-7B「能說日語、浮世繪、江戶時代的鸚鵡」-穩定擴散XL模型描述日本穩定LM基礎Alpha-7B是一個7B參數的僅解碼語言模型，預先在多樣化的日本和英文數據集上進行了預訓練，重點是最大化日語語言建模性能和日語下游任務性能。


## Datasets

 * [mkshing/xlsum_ja](https://huggingface.co/datasets/mkshing/xlsum_ja) - 這是經過篩選的日文子集，接著是PaLM 2filters15-gram overlap*代碼：https://gist.github.com/mkshing/d6371cbfdd50d4f352cee247fd4dd86a訓練範例數：4215（之前：7113）驗證範例數：758（之前：889）測試範例數：766（之前：889）
 * [turing-motors/LLaVA-Instruct-150K-JA](https://huggingface.co/datasets/turing-motors/LLaVA-Instruct-150K-JA) - 數據集詳細信息 數據集類型：日本 LLaVA Instruct 150K 是原始 LLaVA Visual Instruct 150K 數據集的本地化版本。
 * [izumi-lab/llm-japanese-dataset](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset) - llm-japanese-dataset
LLM構築用的日本語指示（聊天）資料集主要用於對於以英語構築的LLM模型等，可以用於在聊天（指示）回應任務中使用LoRA等進行調整。
 * [SkelterLabsInc/JaQuAD](https://huggingface.co/datasets/SkelterLabsInc/JaQuAD) - JaQuAD資料集的資料卡 日本問答資料集（JaQuAD）於2022年發布，是一個為日本機器閱讀理解而創建的人工標註資料集。
JaQuAD資料集的資料卡 日本問答資料集（JaQuAD）於2022年發布，是一個為日本機器閱讀理解而創建的人工標註資料集。
 * [datasets/snow_simplified_japanese_corpus](https://huggingface.co/datasets/snow_simplified_japanese_corpus) - SNOW T15和T23（简化日语语料库）的数据集卡片
 * [zan/lima-ja](https://huggingface.co/datasets/zan/lima-ja) - LIMA-JA數據集的數據集卡片描述
這是日本的LIMA數據集，是從Meta的LIMA模型（Zhou等人，2023年）訓練而來的LIMA數據集的翻譯。
 * [fujiki/japanese_alpaca_data](https://huggingface.co/datasets/fujiki/japanese_alpaca_data) - 「japanese_alpaca_data」的資料集卡片。此資料集基於masa3141在japanese-alpaca-lora上的優秀工作。
 * [Atsushi/fungi_indexed_mycological_papers_japanese](https://huggingface.co/datasets/Atsushi/fungi_indexed_mycological_papers_japanese) - fungi_indexed_mycological_papers_japanese大菌輪「論文3行まとめ」データセット最終更新日：2023/8/26（R3-10914まで）==== 語言日文此資料集僅提供日文版本。
fungi_indexed_mycological_papers_japanese大菌輪「論文3行摘要」資料集最終更新日期：2023/8/26（至R3-10914）==== 語言日文此資料集僅提供日文版本。
 * [taishi-i/nagisa_stopwords](https://huggingface.co/datasets/taishi-i/nagisa_stopwords) - 日本的停用詞列表，用於nagisa
 * [hpprc/janli](https://huggingface.co/datasets/hpprc/janli) - JaNLI數據集摘要的數據集卡片
 * [izumi-lab/llm-japanese-dataset-vanilla](https://huggingface.co/datasets/izumi-lab/llm-japanese-dataset-vanilla) - llm-japanese-dataset-vanilla是用於構建LLM的日語聊天數據集izumi-lab/llm-japanese-dataset，已刪除了日英翻譯數據集等內容。
 * [sudy-super/dialogsum-ja](https://huggingface.co/datasets/sudy-super/dialogsum-ja) - dialogsum-ja這個資料集是dialogsum、CSDS等翻譯成日文的對話摘要資料集。
 * [shunk031/jsnli](https://huggingface.co/datasets/shunk031/jsnli) - JSNLI數據集的數據集卡片摘要 日本語 SNLI(JSNLI) データセット - KUROHASHI-CHU-MURAWAKI LAB より：本データセットは自然言語推論 (NLI) の標準的ベンチマークである SNLI を日本語に翻訳したものです。
JSNLI數據集的數據集卡片摘要 日本語 SNLI(JSNLI) データセット - KUROHASHI-CHU-MURAWAKI LAB より：本數據集是將自然語言推論（NLI）的標準基準SNLI翻譯成日語的結果。
 * [fujiki/guanaco_ja](https://huggingface.co/datasets/fujiki/guanaco_ja) - 這是Guanaco數據集的日語部分。
 * [range3/wiki40b-ja](https://huggingface.co/datasets/range3/wiki40b-ja) - range3/wiki40b-ja 這個資料集包含了從wiki40b資料集中提取的三個parquet檔案，僅包含日文資料。
範圍3/wiki40b-ja
 * [nakayama/hh-rlhf-helpful-base-ja](https://huggingface.co/datasets/nakayama/hh-rlhf-helpful-base-ja) - https://github.com/anthropics/hh-rlhf 的內容中，經由fuguMT翻譯並修正了helpful-base內所記載的英文，排除了無法正確翻譯的部分。

(Note: The provided input seems to be a mix of Japanese and English. I have translated the English part into traditional Chinese.)
 * [larryvrh/WikiMatrix-v1-Ja_Zh-filtered](https://huggingface.co/datasets/larryvrh/WikiMatrix-v1-Ja_Zh-filtered) - 從WikiMatrix v1篩選和修改的日語/中文語言對數據的過濾版本。
處理步驟：基於基本正則表達式的過濾/長度檢查，以刪除異常對。
 * [if001/aozorabunko-clean-sin](https://huggingface.co/datasets/if001/aozorabunko-clean-sin) - 這是 forkhttps://huggingface.co/datasets/globis-university/aozorabunko-cleanfilteredrow["meta"]["文字遣い種別"] == "新字新仮名"
 * [saldra/sakura_japanese_dataset](https://huggingface.co/datasets/saldra/sakura_japanese_dataset) - Sakura_dataset 商用利用可的超小规模高品质日本语数据集。
 * [range3/cc100-ja](https://huggingface.co/datasets/range3/cc100-ja) - range3/cc100-ja 這個資料集包含了從cc100資料集中提取並分割的僅包含日語的parquet檔案。
 * [elyza/ELYZA-tasks-100](https://huggingface.co/datasets/elyza/ELYZA-tasks-100) - ELYZA-tasks-100：日本語instructionモデル評価データセットデータの説明このデータセットは、instruction-tuningを行ったモデルの評価用データセットです。
 * [AhmedSSabir/Japanese-wiki-dump-sentence-dataset](https://huggingface.co/datasets/AhmedSSabir/Japanese-wiki-dump-sentence-dataset) - 具有上下文的清潔日語完整句子的數據集5M（5121625）。
 * [fujiki/japanese_hh-rlhf-49k](https://huggingface.co/datasets/fujiki/japanese_hh-rlhf-49k) - 這是一個稍微不同版本的kunishou/hh-rlhf-49k-ja，沒有ng_translation == 1的例子。
 * [Atsushi/fungi_diagnostic_chars_comparison_japanese](https://huggingface.co/datasets/Atsushi/fungi_diagnostic_chars_comparison_japanese) - fungi_diagnostic_chars_comparison_japanese大菌輪「識別形質まとめ」データセット最終更新日：2023/8/26（R3-10914まで）==== 語言日語此數據集僅提供日語版本。
 * [datasets/covid_tweets_japanese](https://huggingface.co/datasets/covid_tweets_japanese) - COVID-19 日本語Twitterデータセット的資料卡
 * [datasets/bsd_ja_en](https://huggingface.co/datasets/bsd_ja_en) - 商業場景對話的數據集卡
 * [reazon-research/reazonspeech](https://huggingface.co/datasets/reazon-research/reazonspeech) - ReazonSpeech數據集的數據卡片
摘要：ReazonSpeech是從日本電視節目中收集的大型音頻語料庫。
