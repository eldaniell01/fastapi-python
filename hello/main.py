
from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field
from fastapi import Cookie, FastAPI, File, Form, Header, Query, Path, UploadFile, status, HTTPException
from fastapi import Body


app = FastAPI()

#models
class Pelo(Enum):
    black = 'negro'
    white = 'blanco'
    red = 'rojo'
    
class Ciudades(Enum):
    Guatemala ="Guatemala"
    Retalhuleu="Retalhuleu"

class PersonBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=100)
    color_pelo: Optional[Pelo] = Field(default=None)
    
    class Config:
        schema_extra={
            "example":{
                "first_name": "Daniel",
                "last_name": "Montepeque",
                "age": 25,
                "color_pelo": "red",
                "password": "12345869040"
            }
        }
class Person(PersonBase):
    password: str = Field(..., min_length=8)
class Person2(PersonBase):
    pass
class Location(BaseModel):
    city: Ciudades = Field(...)
    state: Ciudades = Field(...)

class Login2(BaseModel):
    user: str = Field(..., max_length=20, example="eldaniell01")
    message: str = Field(default="login completado")

@app.get(
    path='/', 
    status_code=status.HTTP_200_OK
    )
def home():
    return {"hello": "World"}

@app.post(
        path='/person/new', 
        response_model=Person2,
        status_code=status.HTTP_201_CREATED
        )
def create_persona(person: Person = Body(...)):
    return person

#validations

@app.get(
    path='/person/detail',
    status_code=status.HTTP_200_OK
    )
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50, title="Persona", description="nombre de la persona", example="Alvaro"),
    age: int = Query(..., title="Edad", description="this is the person age", example=25),
    
):
    return {name: age}

#validations 
personas =[1, 2, 3, 4]
@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0, example=123)
): 
    if person_id not in personas:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="no existe"
        )
    return {person_id: "existe"}

#validations body

@app.put("/person/{person_id}")
def update(
    person_id: int = Path(
        ..., 
        title="person_id",
        description="this is the person id",
        gt=0,
        example=123
    ),
    person: Person = Body(...)
    #location: Location = Body(...)
):
    #resultado = person.dict()
    #resultado.update(location.dict())
    return person

@app.post(
    path="/login",
    response_model=Login2,
    status_code=status.HTTP_200_OK
)
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return Login2(user=username)

@app.post(
    path="/contact", 
    status_code=status.HTTP_200_OK
)
def contact(
    name: str = Form(
        ..., 
        max_length=20,
        min_length=1
    ),
    name2: str = Form(
        ..., 
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ..., 
        min_length=20
    ), 
    userna: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return userna

@app. post(
    path="/post-image"
)
def imagen(
    image: UploadFile = File(...)
):
    return {
        "Filename":image.filename,
        "Format":image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }