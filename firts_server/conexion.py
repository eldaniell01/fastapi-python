import mysql.connector

def get_database_connection():
    """get_database_connection _summary_

    optine la conexion a la base de datos
    mediante el host, usuario, password y el nombre de la base de datos 
    que se quiere conectar

    Returns:
        conexion a la base de datos
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sakila"
    )
    return mydb