from importlib.resources import path
from turtle import title
from enum import Enum
from typing import Optional
from unittest import result
from pydantic import BaseModel, Field
from fastapi import FastAPI, Query, Path
from fastapi import Body


app = FastAPI()

#models
class Pelo(Enum):
    black = 'negro'
    white = 'blanco'
    red = 'rojo'
class Person(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=100)
    age2: int = Field(..., gt=0, le=100)
    color_pelo: Optional[Pelo] = Field(default=None)

class Location(BaseModel):
    city: str
    state: str


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
    age: int = Query(..., title="Edad", description="this is the person age"),
    
):
    return {name: age}

#validations 

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0)
): 
    return {person_id: "existe"}

#validations body

@app.put("/person/{person_id}")
def update(
    person_id: int = Path(
        ..., 
        title="person_id",
        description="this is the person id",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    resultado = person.dict()
    resultado.update(location.dict())
    return resultado