## 確率過程を可視化するライブラリ

## 環境構築
- pyenvをインストールする(OSにより色々異なるっぽいので調べて下さい)
  - `pyenv install 3.13.2`などを実行してpythonをinstall
- レポジトリをクローンする
  - `git clone git@github.com:hiro476116/stochastic-calculus-library.git` など
  - クローンしたstochastic-calculus-libraryディレクトリ内で`pyenv local 3.13.2`を実行
- 仮想環境を作成する
  - 初めて作成する場合`python -m venv sclenv`を実行
  - `source sclenv/bin/activate`を実行して切り替える
- 必要なモジュールをインストール
  - `pip install -r requirements.txt`


## 実行方法
- stochastic-calculus-library ディレクトリ上で `python -m visualizer.visual` を実行