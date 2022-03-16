import json
import requests
from pprint import pprint

# make request to api and get the response
url = "https://myallies-breaking-news-v1.p.rapidapi.com/GetCompanyDetailsBySymbol"

querystring = {"symbol":"twtr"}

headers = {
    'x-rapidapi-host': "myallies-breaking-news-v1.p.rapidapi.com",
    'x-rapidapi-key': "099dcd4cd8mshf59e2c82cecb87dp16d00bjsn0094e832c52a"
    }

response = requests.get(url, headers = headers, params = querystring)

pprint(json.loads(response.text))

# write the content on file
file = open('./lessons/api_calls/files/file.json', 'w')
file.write(response.text)
file.close()