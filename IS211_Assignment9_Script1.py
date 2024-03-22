import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_Nobel_Memorial_Prize_laureates_in_Economic_Sciences'


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table', {'class': 'wikitable'})


df = pd.read_html(str(table))[0]


df.columns = df.columns.droplevel(0)  # Drop the top level of multi-index
df['Year'] = df['Year'].str.replace(r"\[.*\]", "")  # Remove any references within the year


df.to_csv('nobel_prize_laureates.csv', index=False)