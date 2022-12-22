import os
os.system('clear')

# import requests
# from bs4 import BeautifulSoup

# url = 'https://www.banki.ru/products/currency/cash/nizhniy_novgorod/'
# page = requests.get(url)
# soup = BeautifulSoup(page.text, 'html.parser')
# mass = soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-right-default')
# print(mass)
# string = str(soup.find_all(class_='table-flex__cell table-flex__cell--without-padding padding-right-default'))
# print(string[string.find('>')+1:string.find('</div>'):].replace(',','.'))



import requests
res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
req = 'UZS'
print(res['Valute'][req]['Name'], res['Valute'][req]['Value'])
