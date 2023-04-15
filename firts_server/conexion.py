import mysql.connector

def get_database_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12Intercambios",
        database="sakila"
    )
    return mydb