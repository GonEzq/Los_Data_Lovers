import pandas as pd
import requests

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
r = requests.get(url)

# print(r.text)

dfs = pd.read_html(r.text, attrs={"id": "constituents"})
print(dfs[0])

dfs[0].to_csv("List_of_S%26P_500_companies.csv", index=False)
