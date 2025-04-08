from pprint import pprint
import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
all_links = []
response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')

all_articles = soup.find_all(class_='tm-article-snippet')

parsed_data = []

def get_links():
    for article in all_articles:
        link = ('https://habr.com' + article.find('h2').find('a').get('href'))
        all_links.append(link)
    return all_links

def parsed_data():
    links = get_links()
    for link in links:
        response = requests.get(link)
        soup = bs4.BeautifulSoup(response.text, features='lxml')
        content = soup.find('div', class_='tm-article-presenter')
        for word in KEYWORDS:
            if content.text.lower().find(word) >= 0:
                article_time = content.find('time').get('title')
                article_header = content.find('h1').find('span').text
                for item in parsed_data:
                    if link not in parsed_data['link']:
                        parsed_data.append({
                                    'time': article_time,
                                    'header': article_header,
                                    'link': link
                                })
    pprint(data)

if __name__ == '__main__':
    parsed_data()