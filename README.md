# NLTK FastAPI Project


## Project Description
This project is a REST API developed using FastAPI and NLTK to perform various text processing operations. The API allows text tokenization, partitioning, and named entity recognition. It is intended to be used as a backend by frontend applications and other services that require natural language processing.


## Technologies
- Python
- FastAPI
- NLTK
- SQLAlchemy
- Pydantic
- Uvicorn
- Flake8
- PyTest


## Installation
1. git clone https://github.com/erikagayan/NLTK-fastAPI.git
2. cd NLTK_FastAPI_Project
3. python -m venv venv
4. source venv/bin/activate
5. pip install -r requirements.txt

### In python console:
```python
import nltk
nltk.download()
```
End click download in menu

Then test if everything is working
```python
from nltk.corpus import brown
brown.words()
```
You should get: ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]

6. uvicorn main:app --reload


## Examples of use
Open **NLTK_fastAPI.postman_collection** file in postman and test sentences