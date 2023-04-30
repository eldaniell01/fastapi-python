from fastapi import APIRouter
from pydantic import BaseModel, Field
from jwt_manager import create_token, validate_token
from fastapi.responses import HTMLResponse, JSONResponse
from schemas.user import User
user_login = APIRouter()


@user_login.post('/login', tags=['Login'])
def login(user: User):
    if user.email == 'admin' and user.password =='admin1':
        token=create_token(user.dict())
    return JSONResponse(status_code=200, content=token)
