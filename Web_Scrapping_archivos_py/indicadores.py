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

# Lista para almacenar los datos de las ganancias globales
ganancia_global = []

# Se obtiene la ganancia de cada compañía en la lista y almacenan los datos
for company in companies:
    try:
        data = yf.Ticker(company)
        ganancia_empresa = data.info['grossProfits']
        ganancia_global.append(
            {'Company': company, 'Ganancia Bruta U$S': ganancia_empresa})
    except Exception as e:
        print(f"No se pudo obtener la deuda 2022 de {company}: {e}")

# Se crea un DataFrame con los datos de la ganancia bruta total
df = pd.DataFrame(ganancia_global)
print(df)

# Se exporta el DataFrame a csv.

df.to_csv("Ganancia Bruta Total 2022 S&P 500.csv", index=False)

# Ingresos 2022 'totalRevenue'
# No se pudo obtener el ingreso 2022 de BRK.B: 'totalRevenue'
# No se pudo obtener el ingreso 2022 de BF.B: 'totalRevenue'
# No se pudo obtener el ingreso 2022 de CAT: 'totalRevenue'
# No se pudo obtener el ingreso 2022 de DAL: 'totalRevenue'
# No se pudo obtener el ingreso 2022 de FAST: 'totalRevenue'
# No se pudo obtener el ingreso 2022 de WBA: 'totalRevenue'

# Stock de Deuda 2022 'totalDebt'
# No se pudo obtener la deuda 2022 de BRK.B: 'totalDebt'
# No se pudo obtener la deuda 2022 de BF.B: 'totalDebt'
# No se pudo obtener la deuda 2022 de CAT: 'totalDebt'
# No se pudo obtener la deuda 2022 de DAL: 'totalDebt'
# No se pudo obtener la deuda 2022 de FAST: 'totalDebt'
# No se pudo obtener la deuda 2022 de FDX: 'totalDebt'
# No se pudo obtener la deuda 2022 de INTU: 'totalDebt'
# No se pudo obtener la deuda 2022 de RF: 'totalDebt'
# No se pudo obtener la deuda 2022 de WBA: 'totalDebt'
# No se pudo obtener la deuda 2022 de WDC: 'totalDebt'

# Ganancia Bruta Total 2022
# No se pudo obtener la deuda 2022 de BRK.B: 'grossProfits'
# No se pudo obtener la deuda 2022 de BF.B: 'grossProfits'
# No se pudo obtener la deuda 2022 de CAH: 'grossProfits'
# No se pudo obtener la deuda 2022 de CTAS: 'grossProfits'
# No se pudo obtener la deuda 2022 de CAG: 'grossProfits'
# No se pudo obtener la deuda 2022 de STZ: 'grossProfits'
# No se pudo obtener la deuda 2022 de DRI: 'grossProfits'
# No se pudo obtener la deuda 2022 de EL: 'grossProfits'
# No se pudo obtener la deuda 2022 de GEN: 'grossProfits'
# No se pudo obtener la deuda 2022 de KLAC: 'grossProfits'
# No se pudo obtener la deuda 2022 de LRCX: 'grossProfits'
# No se pudo obtener la deuda 2022 de LW: 'grossProfits'
# No se pudo obtener la deuda 2022 de MDT: 'grossProfits'
# No se pudo obtener la deuda 2022 de MCHP: 'grossProfits'
# No se pudo obtener la deuda 2022 de MSFT: 'grossProfits'
# No se pudo obtener la deuda 2022 de NKE: 'grossProfits'
# No se pudo obtener la deuda 2022 de PANW: 'grossProfits'
# No se pudo obtener la deuda 2022 de PAYX: 'grossProfits'
# No se pudo obtener la deuda 2022 de STX: 'grossProfits'
# No se pudo obtener la deuda 2022 de SJM: 'grossProfits'
# No se pudo obtener la deuda 2022 de SYY: 'grossProfits'
# No se pudo obtener la deuda 2022 de TTWO: 'grossProfits'
# No se pudo obtener la deuda 2022 de TPR: 'grossProfits'
# No se pudo obtener la deuda 2022 de ULTA: 'grossProfits'
# No se pudo obtener la deuda 2022 de VFC: 'grossProfits'
# No se pudo obtener la deuda 2022 de WDC: 'grossProfits'
