from .moduls import *
URL = 'https://www.yelp.com/'
subURL = []
User_Agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                            ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
RootDiv = ['div', 'class', 'y-container ']

def main(*args, **kwargs):
    newYelpObject = ParseHTML(URL, RootDiv, User_Agent)
    newYelpObject.GetDivs()

if __name__ == '__main__':
    main(URL, subURL, User_Agent, RootDiv)