# News parser from hhtps://newsmaker.md

import requests
from bs4 import BeautifulSoup

# Getting and parsing data
url = f'https://newsmaker.md/rus/novosti/category/read/politika/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Finding news and remember titles
news = soup.find_all('article', class_='evo-post')
titles = []
for i in range(len(news)):
    result = news[i].find('h3', class_='evo-entry-title').find('a')
    title = str(result['title'])
    titles.append(title)

# Print titles
number = 1
for title in titles:
    print(f'\n{number}. {title}')
    number += 1
    input('Continue...')
