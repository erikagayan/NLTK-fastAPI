from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


'''URL for database'''
SQLALCHEMY_DATABASE_URL = "sqlite:///./NLTK_fastAPI.db"

'''Engine for db'''
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

'''Session'''
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

'''For create models'''
Base = declarative_base()
