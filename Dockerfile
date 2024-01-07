FROM python:3.11
EXPOSE 80
WORKDIR /app/
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH $PATH:/root/.local/bin
RUN apt update && \
    apt install -y mecab libmecab-dev mecab-ipadic-utf8 && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry install --no-dev --no-root
RUN poetry run python -m unidic download
COPY ./ ./
RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
