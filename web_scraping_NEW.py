import json
from pprint import pprint
import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
all_links = []
parsed_data = []
response = requests.get('https://habr.com/ru/articles/')
try:
    soup = bs4.BeautifulSoup(response.text, features='lxml')

    all_articles = soup.find_all(class_='tm-article-snippet')

    def get_links():
        for article in all_articles:
            link = ('https://habr.com' + article.find('h2').find('a').get('href'))
            all_links.append(link)
        return all_links

    def parsed_info():
        links = get_links()
        for link in links:
            response = requests.get(link)
            try:
                soup = bs4.BeautifulSoup(response.text, features='lxml')
                content = soup.find('div', class_='tm-article-presenter')
                content_for_parse = content.text.lower()
                for word in KEYWORDS:
                    if content_for_parse.find(word) >= 0:
                        article_time = content.find('time').get('title')
                        article_header = content.find('h1').find('span').text
                        parsed_data.append({
                            'word': word,
                            'time': article_time,
                            'header': article_header,
                            'link': link
                        })
            except:
                print("Ошибка при связи с сервером")
        pprint(f'Найдено статей: {len(parsed_data)}')
        with open('parsing_data.json', 'w', encoding='utf-8') as f:
            json.dump(parsed_data, f, ensure_ascii=False, indent=4)
        return parsed_data
except:
    print("Ошибка при связи с сервером")


if __name__ == '__main__':
    parsed_info()