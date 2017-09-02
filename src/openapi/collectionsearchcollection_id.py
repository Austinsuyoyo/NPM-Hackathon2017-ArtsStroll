import requests


url = 'https://openapi.npm.gov.tw/v1/rest/collection/search/04010840'
KEY = '04175c5c-33b9-463c-a973-4fd6679d31ae'
params = {'lang': 'cht'}
headers = {"apiKey": "04175c5c-33b9-463c-a973-4fd6679d31ae"}
res = requests.get(url, params=params, headers=headers, verify=False)


data = res.json()

print('Serial_No        ='), data['result'][0]['Serial_No']
print('ArticleSubject   ='), data['result'][0]['ArticleSubject']
print('CateGory         ='), data['result'][0]['CateGory']
print('Slogan           ='), data['result'][0]['Slogan']
print('ArticleMaker     ='), data['result'][0]['ArticleMaker']
print('ArticleContext   ='), data['result'][0]['ArticleContext']
print('ArticleRemarks   ='), data['result'][0]['ArticleRemarks']
print('art_room         ='), data['result'][0]['art_room']
print('imgUrl           ='), data['result'][0]['imgUrl']



