FROM python:3.11-bullseye

EXPOSE 80
WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get install -y mecab libmecab-dev mecab-ipadic-utf8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt && \
    python -m unidic download

ENTRYPOINT ["python", "main.py"]
