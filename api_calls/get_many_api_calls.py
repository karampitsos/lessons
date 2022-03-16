import json
import requests
from pprint import pprint
from typing import Dict

# make request to api and get the response
def get_data(symbol: str) -> Dict: 

    url = "https://myallies-breaking-news-v1.p.rapidapi.com/GetCompanyDetailsBySymbol"

    querystring = {"symbol": symbol}

    headers = {
        'x-rapidapi-host': "myallies-breaking-news-v1.p.rapidapi.com",
        'x-rapidapi-key': "099dcd4cd8mshf59e2c82cecb87dp16d00bjsn0094e832c52a"
        }

    response = requests.get(url, headers = headers, params = querystring)

    pprint(json.loads(response.text))

    return json.loads(response.text)

stocks = ['aapl','abnb','twtr']

# save the requests
for stock in stocks:
    data = get_data(stock)
    file = open(f'./lessons/api_calls/files/file_{stock}.json', 'w')
    file.write(json.dumps(data))
    file.close()


