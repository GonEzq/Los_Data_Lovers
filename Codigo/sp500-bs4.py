from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
# print(soup)

tickers = []
companies = []
industries = []
sub_industries = []
headquarters = []
datas_1st_added = []
years_founded = []

table = soup.find("table", {"id": "constituents"})
rows = table.findAll("tr")[1:]
for row in rows:
    ticker = row.findAll("td")[0].text
    company = row.findAll("td")[1].text
    industry = row.findAll("td")[2].text
    sub_industry = row.findAll("td")[3].text
    headquarter = row.findAll("td")[4].text
    data_1st_added = row.findAll("td")[5].text
    year_founded = row.findAll("td")[7].text

    tickers.append(ticker.replace("\n", ""))
    companies.append(company)
    industries.append(industry)
    sub_industries.append(sub_industry)
    headquarters.append(headquarter.split(', ')[-1])
    datas_1st_added.append(data_1st_added)
    years_founded.append(year_founded.replace(
        "\n", "").split('(')[-1].split(')')[0][-4:])

# print(tickers)
# print(companies)
# print(industries)
# print(sub_industries)
# print(headquarters)
# print(datas_1st_added)
# print(years_founded)

df = pd.DataFrame({"Symbol": tickers, "Company": companies, "Industry": industries,
                   "Sub_Industry": sub_industries, "Headquarter": headquarters, "Data_1st_added": datas_1st_added,
                   "Foundation": years_founded})
print(df)

df.to_csv("List_of_S%26P_500_companies.csv", index=False)
