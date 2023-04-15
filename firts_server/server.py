from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from conexion import get_database_connection

app = FastAPI()

app.title = 'Mi primer servidor'
app.version = "0.0.1"

@app.get('/', tags=['Home'])
async def root():
    db = get_database_connection()
    cursor = db.cursor()
    cursor.execute("select * from actor limit 10")
    result = cursor.fetchall()
    
    films = []
    for row in result:
        fecha = datetime.strftime(row[3], '%d/%m/%Y %H:%M:%S')
        
        film = {
            "actor_id": row[0],
            "first_name" : str(row[1]),
            "last_name": str(row[2]),
            "last_update": fecha
        }
        films.append(film)
    db.close()
    
    return JSONResponse(content={"films": films})