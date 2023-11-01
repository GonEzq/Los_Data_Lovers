import mysql.connector
import os
import requests
from bs4 import BeautifulSoup
import csv


connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    #port = "3306", #puerto por defauld, es necesario especificar si se cambia el puerto en algun momento

)

if connection.is_connected():
        print("Conexión exitosa")

    # Crear y eliminar la base de datos
cursor = connection.cursor()
delete_database_query = "DROP DATABASE IF EXISTS LISTA DE EMPRESAS DEL  SP500"
cursor.execute(delete_database_query)
create_database_query = "CREATE DATABASE LISTA DE EMPRESAS DEL  SP500"
cursor.execute(create_database_query)
cursor.close()

 # Reconectar a la nueva base de datos
connection = mysql.connector.connect(
        host='Localhost',
        port=3306,
        user='root',
        password='',
        database='LISTA DE EMPRESAS DEL  SP500'
    )
if connection.is_connected():
    print("Conexión a la base de datos LISTA DE EMPRESAS DEL  SP500 correcta")

# except Exception as ex:
#     print("conexion")

# # Cursor para recorrer la base
# cursor = connection.cursor()
