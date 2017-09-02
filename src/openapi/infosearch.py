import requests


url = 'https://openapi.npm.gov.tw/v1/rest/info/search/'
KEY = '04175c5c-33b9-463c-a973-4fd6679d31ae'

params = {'lang': 'cht'}
headers = {"apiKey": "04175c5c-33b9-463c-a973-4fd6679d31ae"}
res = requests.get(url, params=params, headers=headers, verify=False)

#print res.text

data = res.json()

print('NPM            ='), data['result'][0]['NPM']
print('Hours          ='), data['result'][0]['Hours']
print('Contact        ='), data['result'][0]['Contact']
print('TicketPrices   ='), data['result'][0]['TicketPrices']
print('Transportation ='), data['result'][0]['Transportation']
