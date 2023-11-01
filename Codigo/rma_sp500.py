from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.forex.in.rs/mercado/3283-2/#:~:text=En%20los%20%C3%BAltimos%2010%20a%C3%B1os%2C%20de%202011%20a%202020%2C%20la,fue%20del%2014%2C5%25.&text=%C2%BFCu%C3%A1l%20es%20la%20rentabilidad%20media%20diaria%20del%20s%26p%20500%3F,el%20precio%20de%20cierre%20ajustado."
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
# print(soup)

years = []
prices_average_close = []
prices_open_year = []
prices_high_year = []
prices_low_year = []
prices_close_year = []
changes_percentage = []

table = soup.find("table", {"id": "tablepress-335"})
# print(table)

rows = table.findAll("tr")[1:]
for row in rows:
    year = row.findAll("td")[0].text
    price_average_close = row.findAll("td")[1].text
    price_open_year = row.findAll("td")[2].text
    price_high_year = row.findAll("td")[3].text
    price_low_year = row.findAll("td")[4].text
    price_close_year = row.findAll("td")[5].text
    change_percentage = row.findAll("td")[6].text

    years.append(year)
    prices_average_close.append(price_average_close)
    prices_open_year.append(price_open_year)
    prices_high_year.append(price_high_year)
    prices_low_year.append(price_low_year)
    prices_close_year.append(price_close_year)
    changes_percentage.append(change_percentage)

# print(years)
# print(prices_average_close)
# print(prices_open_year)
# print(prices_high_year)
# print(prices_low_year)
# print(prices_close_year)
# print(changes_percentage)

df = pd.DataFrame({"Year": years, "Price_average_close": prices_average_close, "Price_open_year": prices_open_year,
                   "Price_high_year": prices_high_year, "Price_low_year": prices_low_year, "Price_close_year": prices_close_year,
                   "Change_percentag": changes_percentage})
# print(df)

df.to_csv("Rentabilidad Media Anual S&P 500.csv", index=False)

# print(len(years))
# print(len(prices_average_close))
# print(len(prices_open_year))
# print(len(prices_high_year))
# print(len(prices_low_year))
# print(len(prices_close_year))
# print(len(changes_percentage))
