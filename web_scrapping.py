import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
text = []
response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')

all_articles = soup.find_all(class_='tm-article-snippet')
articles_list = []
for article in all_articles:
    for word in KEYWORDS:
        if article.text.lower().find(word) > 0 <= 1:
            data = article.find('time').get('title')
            header = article.find('h2').find('span').text
            link = article.find('h2').find('a').get('href')
            if link not in articles_list:
                articles_list.append(f'{data}-{header}-{'https://habr.com' + link}')
print(articles_list)
