import yfinance as yf
import pandas as pd

# Para obtener la lista de compañías que integran el S&P 500 desde Wikipedia

url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_data = pd.read_html(url)
sp500_companies = sp500_data[0]

# Se obtienen los tickers de las compañías del S&P 500
sp500_tickers = sp500_companies['Symbol'].tolist()

# Se crea una nueva variable tipo lista que contendrá el resultado anterior: los tickers
# de todas ls compañías que componen el S&P 500.

companies = sp500_tickers

# Se crea una lista para almacenar los datos de la empleabilidad de las empresas del índice.

total_empleos = []

# Se obtiene la cantidad de empleos de cada compañía en la lista y se almacenan los datos
for company in companies:
    try:
        data = yf.Ticker(company)
        cantidad_empleos = data.info['fullTimeEmployees']
        total_empleos.append(
            {'Company': company, 'Cant. Empleos': cantidad_empleos})
    except Exception as e:
        print(f"No se pudo obtener la cantidad de empleos de {company}: {e}")

# Se crea un DataFrame con los datos del empleo
df = pd.DataFrame(total_empleos)
print(df)

# Se exporta el DataFrame a csv.

df.to_csv("Cantidad de empleos 2023 S&P 500.csv", index=False)

# No se pudo obtener la cantidad de empleos de AZO: 'fullTimeEmployees'
# No se pudo obtener la cantidad de empleos de BRK.B: 'fullTimeEmployees'
# No se pudo obtener la cantidad de empleos de BF.B: 'fullTimeEmployees'
# No se pudo obtener la cantidad de empleos de CAT: 'fullTimeEmployees'
# No se pudo obtener la cantidad de empleos de V: 'fullTimeEmployees'