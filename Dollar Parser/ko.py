import requests
from bs4 import BeautifulSoup
import time, smtpd

url='https://www.google.com/search?q=1+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80&rlz=1C1CHBD_ruUA876UA876&oq=1&aqs=chrome.0.69i59j69i57j35i39j0j69i60l4.8071j0j7&sourceid=chrome&ie=UTF-8'

class Parser():
    difference = 5
    current_converted_price = 0
    def __init__(self, url):
        self.url = url

    def parsing(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        re = requests.get(self.url, headers=headers)
        html = BeautifulSoup(re.content, 'html.parser')
        global a
        a = html.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    def currensy(self):
        print('Курс долара зараз по відношенню до гривні: ' + a[0].text)
        time.sleep(2)
        with open("C:/Users/Макс/Desktop/Програмування/PythonJJ/Модулі і класи на всі випадки життя/Value.html",'w') as f:
            f.write("Ціна долара : " + str(a[0]))
ko = Parser(url)
on = True
while on==True:
    try:
        ko.parsing()
        ko.currensy()
        Y =input("Дізнатися курс знову натисныть Y , завершити N: ")
        if Y == 'Y' or Y == 'y':
            ko.parsing()
            ko.currensy()
        elif Y=='N' or Y=='n':
            on=False
            break
        else:
            print("Невідома команда")
            on=False
            break
    except:
        on = False
        break
