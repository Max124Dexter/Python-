"""Парсер Тексту"""
import requests as r
from bs4 import BeautifulSoup as BS
import os

url= 'https://stopgame.ru/'
agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

def Parsing():
    try:
        req = r.get(url, headers=agent)
        html = BS(req.content, 'html.parser')
        for em in html.select('.section-news-lent'):
            title = em.findAll('p')
            f = open('C:/Users/Макс/Desktop/Програмування/PythonJJ/Парсери/TEXT Parser/text.txt', 'w')
            f.write(title[0].text)
            print(title[0].text)
            f.close()
    except:
        print('PARSING ERROR')

Parsing()


