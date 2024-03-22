import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_NBA_champions'


response = requests.get(url)


soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table', {'class': ['wikitable', 'sortable']})


df = pd.read_html(str(table))[0]


if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(1)
else:
    df.columns = df.columns


df = df.replace(to_replace=r'\[.*\]', value='', regex=True)


df.to_csv('nba_champions.csv', index=False)
