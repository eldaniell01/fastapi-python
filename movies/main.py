from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from config.database import session, engine, base
from models.movie import Movie as mov
from middlewares.error_handler import errorhandler
from routers.movier import movie_router
from routers.userl import user_login

app = FastAPI()
app.title = "Aplicacion de peliculas"
app.version = "0.0.1"

app.add_middleware(errorhandler)
app.include_router(movie_router)
app.include_router(user_login)
base.metadata.create_all(bind=engine)





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




