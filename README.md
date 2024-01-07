# learning-mecab.py

🛖🛖🛖 MeCabを使って形態素解析を行うPythonプログラムです！  

[![ci](https://github.com/osawa-koki/learning-mecab.py/actions/workflows/ci.yml/badge.svg)](https://github.com/osawa-koki/learning-mecab.py/actions/workflows/ci.yml)

## 実行方法

DevContainerに入り、以下のコマンドを実行します！  

```shell
./entrypoint.sh --reload
```

## 本番用実行

以下のコマンドを実行します！  

```shell
docker build -t learning-mecab-py .
docker run --rm -d -p 8000:8000 --name learning-mecab-py learning-mecab-py
```
