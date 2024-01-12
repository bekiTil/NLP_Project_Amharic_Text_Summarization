from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from summarizer import SummarizationModel
from model import Model
from nlp import NLP
from fastapi.middleware.cors import CORSMiddleware


class Chat(BaseModel):
    text: str = None
    author: str = "User"


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

nlp = NLP()
summarizer = SummarizationModel()

items = []


@app.get("/")
def root():
    return {"path": "hello world"}


@app.post("/items")
async def create_item(item: Chat):
    items.append(item)
    input_text = item.text
    res = nlp.summary(input_text, summarizer)
    new_item = Chat(text=res, author="Api")
    items.append(new_item)
    return items
