from importlib.resources import path
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Query, Path
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

#validations

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50, title="Persona", description="nombre de la persona"),
    age: int = Query(..., title="Edad", description="this is the person age")
):
    return {name: age}

#validations 

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0)
): 
    return {person_id: "existe"}