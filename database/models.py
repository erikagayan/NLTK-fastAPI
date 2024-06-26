from database.engine import Base
from sqlalchemy import Column, Integer, String, Text


class TextItem(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    tokens = Column(Text, nullable=True)  # JSON serialized token list

    def __repr__(self):
        return f"<TextItem(id={self.id}, text={self.text[:50]}, tokens={self.tokens[:50]})>"
