from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

class Translate(BaseModel):
    czech: str
    english: str

class WordRequest(BaseModel):
    word: str

origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/cz_to_en/{word}")
def read_item(word: str):
    word = word.replace('+', ' ')
    with open('C:\\aa_programovani\\webove-aplikace-slovnik\\backend\\slovnik_cz_en.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if word in line:
                english, czech = line.strip().split('=')
                return {"english": english, "czech": czech}
    return {"message": "Slovo nenalezeno"}

@app.get("/en_to_cz/{word}")
def test(word: str):
    word = word.replace('+', ' ')
    with open('C:\\aa_programovani\\webove-aplikace-slovnik\\backend\\slovnik_cz_en.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if word in line:
                english, czech = line.strip().split('=')
                return {"english": english, "czech": czech}
    return {"message": "Slovo nenalezeno"}

@app.post("/translate")
def translate(data: dict):
    fpath = 'slovnik_cz_en.txt'
    if not os.path.exists(fpath):
        print('File does not exist')
    else:    
        with open(fpath, 'r', encoding='utf-8') as f:
            _word = data.get("word")
            for line in f:
                if _word in line:
                    english, czech = line.strip().split('=', 1)
                    return {"english": english, "czech": czech}
        return {"message": "Slovo nenalezeno"}