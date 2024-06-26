from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database.engine import SessionLocal, engine
from database.models import Base, TextItem
from schemas import TextRequest, TokenResponse
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.tree import Tree


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/tokenize", response_model=TokenResponse)
def tokenize_text(request: TextRequest, db: Session = Depends(get_db)):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text field is empty")

    tokens = word_tokenize(request.text)
    db_item = TextItem(text=request.text, tokens=str(tokens))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return TokenResponse(tokens=tokens)


@app.post("/pos_tag")
def pos_tag_text(request: TextRequest, db: Session = Depends(get_db)):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text field is empty")

    tokens = word_tokenize(request.text)
    pos_tags = pos_tag(tokens)
    db_item = TextItem(text=request.text, tokens=str(pos_tags))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"pos_tags": pos_tags}
