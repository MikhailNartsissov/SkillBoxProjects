from requests import get
from re import findall

url = input('Введите адрес страницы для анализа:')
page_data = get(url)
if page_data.status_code == 200:
    print(findall(r'(?<=>).*(?=</h3)', page_data.text))
