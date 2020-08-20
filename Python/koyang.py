import requests
from bs4 import BeautifulSoup

headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
response=requests.get("https://www.koyang.top",headers=headers).text
soup=BeautifulSoup(response,"html.parser")
titles=soup.find_all(name='a',class_='article-title')
imgs=soup.find_all(name='img',class_='post_bg')
# for title in titles:
#     print(title['title'])
#     print('https://www.koyang.top'+title['href'])
for img in imgs:
    print("正在下载："+img['data-lazy-src'])
    name=img['alt']
    try:
        with open('C://Program1/Python/bg/%s.jpg'%(name),'wb') as f:
            picture=requests.get(img['data-lazy-src']).content
            f.write(picture)
    except:
        with open('C://Program1/Python/bg/%d.png'%(name),'wb') as f:
            picture = requests.get(img['data-lazy-src']).content
            f.write(picture)