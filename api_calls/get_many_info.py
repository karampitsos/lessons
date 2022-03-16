import json
from pprint import pprint
from typing import Dict
import os
import pandas as pd


def read_from_file(file: str) -> Dict:
    file = open(f'files/{file}', 'r')
    data = json.load(file)
    file.close()
    return data

def get_info(data: Dict) -> Dict:
    stock = data['Data']['Stock']['Close']

    name = data['Data']['Name']

    output = {'name': name, 'stock': stock}

    return output

stocks = []

with os.scandir('files/') as entries:
    for entry in entries:
        file = entry.name
        data = read_from_file(file)
        stock = get_info(data)
        stocks.append(stock)

df = pd.DataFrame(stocks)

df.to_csv('file.csv', index = False)
print(df)


