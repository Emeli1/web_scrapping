import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')

all_articles = soup.find_all(class_='tm-article-snippet')
parsed_data = []
for article in all_articles:
    link = ('https://habr.com' + article.find('h2').find('a').get('href'))
    response = requests.get(link)
    soup = bs4.BeautifulSoup(response.text, features='lxml')
    for word in KEYWORDS:
        if article.text.lower().find(word) > 0:
            article_time = article.find('time').get('title')
            article_header = article.find('h2').find('span').text
            parsed_data.append({
                'time': article_time,
                'header': article_header,
                'link': link
            })

print(parsed_data)
