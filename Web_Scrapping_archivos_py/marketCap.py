import yfinance as yf
import pandas as pd

# Obtener la lista de compañías que integran el S&P 500 desde Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
sp500_data = pd.read_html(url)
sp500_companies = sp500_data[0]

# Se obtienen los tickers de las compañías del S&P 500
sp500_tickers = sp500_companies['Symbol'].tolist()

# Se imprimen los primeros 00 tickers como ejemplo y se comprueba la longitud del arreglo=503
# print(sp500_tickers[:20])
# print(len(sp500_tickers))

# Se crea una nueva variable tipo lista que contendrá el resultado anterior: los tickers
# de todas ls compañías que componen el S&P 500.
companies = sp500_tickers

# Lista para almacenar los datos del market cap
market_caps = []

# Se obtiene el market cap de cada compañía en la lista y almacenan los datos
for company in companies:
    try:
        data = yf.Ticker(company)
        market_cap = data.info['marketCap']
        market_caps.append({'Company': company, 'MarketCap': market_cap})
    except Exception as e:
        print(f"No se pudo obtener el market cap de {company}: {e}")

# Se crea un DataFrame con los datos del market cap
df = pd.DataFrame(market_caps)
print(df)

# Se exporta el DataFrame a csv.

df.to_csv("Capitalización de Mercado 2023 S&P 500.csv", index=False)

# No se pudo obtener el market cap de BRK.B: 'marketCap'
# No se pudo obtener el market cap de BF.B: 'marketCap'
# No se pudo obtener el market cap de PSA.
