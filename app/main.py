from typing import List

import MeCab
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class MecabResult(BaseModel):
    surface: str
    feature: str


@app.get("/api/mecab")
def mecab(text: str) -> List[MecabResult]:
    mecab = MeCab.Tagger()
    mecab.parse("")
    node = mecab.parseToNode(text)
    results = []
    while node:
        surface = node.surface
        results.append(
            MecabResult(
                surface=surface,
                feature=node.feature,
            )
        )
        node = node.next
    results = results[1:-1]
    return results


app.mount("/api", app)
app.mount("/", StaticFiles(directory="./www/", html=True), name="www")
