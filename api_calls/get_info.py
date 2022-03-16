import json
from pprint import pprint


# read from the file
file = open('./lessons/api_calls/files/file.json', 'r')
data = json.load(file)
file.close()
pprint(data)

# get info from data
stock = data['Data']['Stock']['Close']

name = data['Data']['Name']

print(name, stock)
