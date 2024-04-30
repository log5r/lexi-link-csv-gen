# LexiLinkCsvGen

## これはなんですか

いまんところ [WordHolic](https://www.langholic.com/wordholic) でインポートするCSVを作るツール。  

## 使い方

1. 覚えたい文章のカードをtoml形式（後述）で置く
2. TOMLライブラリをインストールする。
   * `pip install toml`
3. ディレクトリパスと出力先パスを確認する。
4. Pythonプログラムを実行する。
   * `main.py <path_to_toml_dir> <path_to_csv>`

### 単語カードの書式ってどんな想定？
こういうのが入ったtoml
```toml
ja-JP = "ほら、バスが駅にやってきたぞ。"
en-US = "Look, the bus has arrived at the station."
fr-FR = "Regarde, le bus est arrivé à la station."
zh-CN = "看，公交车到站了。"
ko-KR = "봐, 버스가 역에 도착했어."
```

## Q&A

### Q. 動かないが？

A. ごめんなさい。でも、そんな難しいプログラムじゃないから自分で直して使ってください。
