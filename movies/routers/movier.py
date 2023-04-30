from fastapi import APIRouter
from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from middlewares.jwt_bearer import JWTBearer
from config.database import session, engine, base
from models.movie import Movie as mov
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService
from schemas.movie import Movie
movie_router = APIRouter()



@movie_router.get('/movies', tags=['Peliculas'], response_model=List[Movie], status_code=200, dependencies=[Depends(JWTBearer())])
def obtener_peliculas() -> List[Movie]:
    db = session()
    result = MovieService(db).get_movie()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['Obtener peliculas'], response_model=Movie)
def obtener(id: int = Path(ge=1, le=10)) -> Movie:
    db = session()
    result = MovieService(db).get_movie1(id)
    if not result:
        return JSONResponse(status_code=404, content={'menssage': 'no encontrado'})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get('/movies/', tags=['Categorias  '], response_model=List[Movie], status_code=200)
def get_categoria(category: str = Query(min_length=4, max_length=15)) -> List[Movie]:
    db = session()
    result = MovieService(db).get_category(category)
    if not result:
        return JSONResponse(status_code=404, content={'menssage': 'no encontrado'})
    return JSONResponse(status_code=202, content=jsonable_encoder(result))



@movie_router.put('/movies/{id}', tags=['Modificar'], response_model=dict, status_code=200)
def update_movie(id: int, movie: Movie)-> dict:
    db = session()
    MovieService(db).update_movie(movie)
    return JSONResponse(status_code=200, content={'message' : 'se modifico la pelicula'})
        
@movie_router.delete('/movies/{id}', tags=['Eliminar'], response_model=dict, status_code=200)
def delete_movie(id : int) -> dict:
    db = session()
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={'message' : 'se elimino la pelicula'})

@movie_router.post('/movies', tags=['Registrar pelicula'], response_model=dict, status_code=201)
def create_movie(movie: Movie) -> dict:
    db = session()
    result = MovieService(db).update_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={'menssage': 'no encontrado'})
    MovieService(db).update_movie(id, movie)
    
    return JSONResponse(status_code=201, content={'message' : 'se registro la pelicula'})