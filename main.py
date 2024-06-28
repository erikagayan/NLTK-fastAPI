from sqlalchemy.orm import Session
from database.models import Base, TextItem
from schemas import TextRequest, TokenResponse
from database.engine import SessionLocal, engine
from fastapi import FastAPI, HTTPException, Depends

from nltk import ne_chunk
from nltk.tree import Tree
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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


@app.post("/ner")
def ner_text(request: TextRequest, db: Session = Depends(get_db)):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text field is empty")

    tokens = word_tokenize(request.text)
    pos_tags = pos_tag(tokens)
    chunks = ne_chunk(pos_tags, binary=False)
    entities = []

    for chunk in chunks:
        if isinstance(chunk, Tree):
            entities.append({"label": chunk.label(), "chunk": " ".
                            join(c[0] for c in chunk.leaves())})

    db_item = TextItem(text=request.text, tokens=str(entities))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"entities": entities}
