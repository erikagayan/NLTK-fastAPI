from pydantic import BaseModel
from typing import List, Optional


class TextRequest(BaseModel):
    # defines the structure of the tokenization request.
    text: str


class TokenResponse(BaseModel):
    # defines the structure of the response with tokens
    tokens: List[str]


class TextItemBase(BaseModel):
    # contains the basic data structure of the model.
    text: str
    tokens: Optional[List[str]] = None


class TextItemCreate(TextItemBase):
    # is used to create new records.
    pass


class TextItem(TextItemBase):
    # adding an identifier and is used to read the data.
    id: int

    class Config:
        orm_mode = True
