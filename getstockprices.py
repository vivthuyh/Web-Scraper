import requests
from bs4 import BeautifulSoup
import pandas as pd

mystocks = ['RIOT', 'NVDA', 'EA', 'NTDOY','SONY','MSFT','RBLX','SGAMY','CCOEY']
stockdata = []

def getData(symbol):
    headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    url = f'https://finance.yahoo.com/quote/{symbol}'

    r = requests.get(url, headers=headers)

    soup= BeautifulSoup(r.text, 'html.parser')

    stock= {
        'company' : soup.find('h1', {'class': 'D(ib) Fz(18px)'}).text,
        'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,
        'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,
        'percent' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text 
    }
    return stock

for item in mystocks:
    stockdata.append(getData(item))
    print('Getting: ', item)


dataframe= pd.DataFrame(stockdata)

dataframe.to_excel('output.xlsx', index=False)

print('Fin.')