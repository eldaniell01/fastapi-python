from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from fastapi.security import HTTPBearer

app = FastAPI()
app.title = "Aplicacion de peliculas"
app.version = "0.0.1"

class User(BaseModel):
    email: str
    password: str

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data=validate_token(auth.credentials)
        if data['email'] != 'admin':
            raise HTTPException(status_code=403, detail='error al login')

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=4, max_length=15)
    overview: str = Field(min_length=4, max_length=15)
    year: int = Field(le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=4, max_length=15)
    
    class Config:
        schema_extra ={
            "example": {
                'id': 1,
                'title': "mi pelicula",
                'overview': 'mi pelicula 2',
                'year': 2023,
                'rating': 9.9,
                'category': 'nueva'
            }
        }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'    
    },
    {
        'id': 2,
        'title': 'cabal',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Thriller'    
    } 
]



@app.get('/', tags=['HOME'])
def mensaje():
    return HTMLResponse('<h1>Hola Mundo</h1>')

@app.post('/login', tags=['Login'])
def login(user: User):
    if user.email == 'admin' and user.password =='admin1':
        token=create_token(user.dict())
    return JSONResponse(status_code=200, content=token)

@app.get('/movies', tags=['Peliculas'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def obtener_peliculas() -> List[Movie]:
    return JSONResponse(status_code=200, content=movies)

@app.get('/movies/{id}', tags=['Obtener peliculas'], response_model=Movie)
def obtener(id: int = Path(ge=1, le=10)) -> Movie:
    for item in movies:
        if item ['id'] == id:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])

@app.get('/movies/', tags=['Categorias  '], response_model=List[Movie], status_code=200)
def get_categoria(category: str = Query(min_length=4, max_length=15)) -> List[Movie]:
    for item in movies:
        if item['category'] == category:
            return JSONResponse(content=item)
    return JSONResponse(status_code=404, content=[])

@app.post('/movies', tags=['Registrar pelicula'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(status_code=201, content={'message' : 'se registro la pelicula'})

@app.put('/movies/{id}', tags=['Modificar'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie)-> dict:
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['rating'] = movie.rating
            item['category']= movie.category
            return JSONResponse(status_code=200, content={'message' : 'se modifico la pelicula'})
        
@app.delete('/movies/{id}', tags=['Eliminar'], response_model=dict, status_code=200)
def delete_movie(id : int) -> dict:
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return JSONResponse(status_code=200, content={'message' : 'se elimino la pelicula'})