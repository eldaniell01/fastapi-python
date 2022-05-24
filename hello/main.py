from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi import Body


app = FastAPI()

#models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    color_pelo: Optional[str] = None

@app.get('/')
def home():
    return {"hello": "World"}

@app.post('/person/new')
def create_persona(person: Person = Body(...)):
    return person