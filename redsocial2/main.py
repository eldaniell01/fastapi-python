
from encodings import utf_8
import json
from unittest import result
from uuid import UUID
from datetime import datetime, date
from typing import Optional, List
from pydantic import EmailStr, Field, BaseModel

from fastapi import FastAPI, status, Body

app = FastAPI()


class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr= Field(...)
class Userlogin(UserBase):
    password: str =Field(
        ..., 
        min_length=8,
        max_length=60
    )
class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date: Optional[date] = Field(default=None)

class Userregis(User):
    password: str =Field(
        ..., 
        min_length=8,
        max_length=60
    )
class socialnetwork(BaseModel):
    red_id: UUID = Field(...)
    content: str = Field(
        ..., 
        min_lenght=1,
        max_length=256
    )
    create_con: datetime = Field(default=datetime.now())
    update_con: Optional[datetime] = Field(default=None)
    by: User = Field(...)


@app.post(
    path="/registrar",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="registro de usuario",
    tags=["Users"]
)
def create_user(user: Userregis = Body(...)):
    """_summary_

    Args:
        user (Userregis): _description_
    """
    with open("users.json", "r+", encoding="utf_8") as f:
        resultado = json.loads(f.read())
        user_dic = user.dict()
        user_dic["user_id"] = str(user_dic["user_id"])
        user_dic ["birth_date"] = str(user_dic ["birth_date"])
        resultado.append(user_dic)
        f.seek(0)
        f.write(json.dumps(resultado))
        return user
        

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="logeo de usuario",
    tags=["Users"]
)
def login():
    pass
@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Listado de usuario",
    tags=["Users"]
)
def show_user():
    """_summary_
    """
    with open("users.json", "r", encoding="utf_8") as f:
        resultado = json.loads(f.read())
        return resultado
    
@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="mostrar usuario",
    tags=["Users"]
)
def show_userid():
    pass
@app.delete(
    path="/users/{user_id}/delete",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Eliminación de usuario",
    tags=["Users"]
)
def delete_user():
    pass
@app.put(
    path="/users/{user_id}/update",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="actualización de usuario",
    tags=["Users"]
)
def update_user():
    pass



@app.get(
    path="/",
    response_model=List[socialnetwork],
    status_code=status.HTTP_200_OK,
    summary="mostrar todo",
    tags=["SocialNetwork"]
)
def home():
    """_summary_
    """
    with open("publicacion.json", "r", encoding="utf_8") as f:
        resultado = json.loads(f.read())
        return resultado

@app.post(
    path="/publicar",
    response_model=socialnetwork,
    status_code=status.HTTP_201_CREATED,
    summary="crear publicación",
    tags=["publicacion"]
)
def create_publicacion(publicacion: socialnetwork = Body(...)):
    """_summary_

    Args:
        user (Userregis): _description_
    """
    with open("publicacion.json", "r+", encoding="utf_8") as f:
        resultado = json.loads(f.read())
        publicacion_dic = publicacion.dict()
        publicacion_dic["red_id"] = str(publicacion_dic["red_id"])
        publicacion_dic["create_con"] = str(publicacion_dic ["create_con"])
        publicacion_dic["update_con"] = str(publicacion_dic ["update_con"])
        publicacion_dic["by"]["user_id"] = str(publicacion_dic["by"]["user_id"])
        publicacion_dic["by"]["birth_date"] = str(publicacion_dic["by"]["birth_date"])
        resultado.append(publicacion_dic)
        f.seek(0)
        f.write(json.dumps(resultado))
        return publicacion

@app.get(
    path="/publicar/{red_id}",
    response_model=socialnetwork,
    status_code=status.HTTP_200_OK,
    summary="mostrar publicación",
    tags=["publicacion"]
)
def show_publicacion(user: Userregis = Body(...)):
    """_summary_

    Args:
        user (Userregis): _description_
    """
    with open("users.json", "r+", encoding="utf_8") as f:
        resultado = json.loads(f.read())
        user_dic = user.dict()
        user_dic["user_id"] = str(user_dic["user_id"])
        user_dic ["birth_date"] = str(user_dic ["birth_date"])
        resultado.append(user_dic)
        f.seek(0)
        f.write(json.dumps(resultado))
        return user
    
@app.delete(
    path="/publicar/{red_id}/delete",
    response_model=socialnetwork,
    status_code=status.HTTP_201_CREATED,
    summary="eliminar publicación",
    tags=["publicacion"]
)
def delete_publicacion(user: Userregis = Body(...)):
    """_summary_

    Args:
        user (Userregis): _description_
    """
    with open("users.json", "r+", encoding="utf_8") as f:
        resultado = json.loads(f.read())
        user_dic = user.dict()
        user_dic["user_id"] = str(user_dic["user_id"])
        user_dic ["birth_date"] = str(user_dic ["birth_date"])
        resultado.append(user_dic)
        f.seek(0)
        f.write(json.dumps(resultado))
        return user
    


@app.put(
    path="/publicar/{red_id}/update",
    response_model=socialnetwork,
    status_code=status.HTTP_200_OK,
    summary="actualizar publicación",
    tags=["publicacion"]
)
def update_publicacion(user: Userregis = Body(...)):
    """_summary_

    Args:
        user (Userregis): _description_
    """
    with open("users.json", "r+", encoding="utf_8") as f:
        resultado = json.loads(f.read())
        user_dic = user.dict()
        user_dic["user_id"] = str(user_dic["user_id"])
        user_dic ["birth_date"] = str(user_dic ["birth_date"])
        resultado.append(user_dic)
        f.seek(0)
        f.write(json.dumps(resultado))
        return user