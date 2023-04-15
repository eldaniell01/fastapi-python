import mysql.connector

def get_database_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sakila"
    )
    return mydb