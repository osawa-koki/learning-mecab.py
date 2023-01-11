from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List
import MeCab

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set the host and port values
host = "0.0.0.0"
port = 80

class MecabResult(BaseModel):
    surface: str
    feature: str

LIMIT = 100

# Define a route to handle the /api URL
@app.get("/api/mecab")
def mecab(text: str) -> List[MecabResult]:
    mecab = MeCab.Tagger()
    mecab.parse("")
    node = mecab.parseToNode(text)
    results = []
    while node:
        surface = node.surface
        results.append(MecabResult(
            surface=surface,
            feature=node.feature,
        ))
        node = node.next
    results = results[1:-1]
    return results

# Serve static files from the "www" directory and set index.html as the default file
app.mount("/api", app)
app.mount("/", StaticFiles(directory="www", html=True), name="www")

# Run the FastAPI app
if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host=host, port=port, log_level="info")
