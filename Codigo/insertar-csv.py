import csv
import sqlite3

archivo = open(
    r'D:\Disco H\SILVANA\2Cursos\LENGUAJES\Python\POLITECNICO\TSCDIA\SCRAPPING\Composicion.csv')

filas = csv.reader(archivo, delimiter=";")

lista = list(filas)
del (lista[0])
tuplaa = tuple(lista)

# insertar

conexion = sqlite3.connect("indice_sp_500.db")
cursor = conexion.cursor()
cursor.executemany(
    "INSERT INTO Composicion ('id_empresa','Simbolo', 'Empresa', 'Industria', 'Sub_Industria', 'Localizacion ', 'Incorp_SP500', 'Fundacion', 'Cant_Empleos','Facturac_Usd_ 2022', 'Costo_Op_Usd_2022', 'Gcia_Bruta_Usd_2022', 'Deuda_Usd_ 2022', 'Valor_de_Mercado') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", tuplaa)

conexion.commit()
conexion.close()
