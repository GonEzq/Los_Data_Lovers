import yfinance as yf      # usando la librería yfinance
import pandas as pd        # librería pandas


ticker = "CL=F"  # símbolo del título bursátil en website: https://finance.yahoo.com/
# nombre del título bursátil
nombre_ticker = " Petróleo Crudo"
data_start = "2023-01-01"  # fecha de inicio de la serie
data_end = "2023-09-30"    # fecha de cierre de la serie

# Se descarga la serie con el siguiente método de la librería yfinance.

datos = yf.download(ticker, start=data_start, end=data_end)
# print(datos)

# Se guardan los datos en un archivo CSV, para ello se crea una variable para el nombre del archivo.

nombre_archivo = f"{nombre_ticker}_histórico.csv"

datos.to_csv(nombre_archivo)  # genera el dataframe en formato csv.

print(f"Datos del {nombre_ticker} guardados en {nombre_archivo}")
