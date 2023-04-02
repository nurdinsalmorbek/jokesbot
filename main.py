import requests
import random
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good/'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    jokes = soup.find_all('div', class_ = 'text')
    return [joke.text for joke in jokes]

jokes_list = parser(URL)
random.shuffle(jokes_list)
