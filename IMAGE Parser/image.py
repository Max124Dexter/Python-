import httplib2

img = 'https://www.5.ua/media/pictures/original/117971.jpg'
h = httplib2.Http('.cache')
response, content = h.request(img)
out = open('C:/Users/Макс/Desktop/Програмування/PythonJJ/Парсери/IMAGE Parser/img.jpg', 'wb')
out.write(content)
out.close()