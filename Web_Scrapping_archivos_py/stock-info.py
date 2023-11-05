import yfinance as yf


appl = yf.Ticker("APPL")
stockinfo = appl.info

for line in stockinfo.items():
    print(":", line)

# Devuelve los datos más relevantes de cada compañía disponible en website: Yahoo Finance.
