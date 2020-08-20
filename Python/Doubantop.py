import requests
import time
from openpyxl import Workbook
from bs4 import BeautifulSoup

wb = Workbook()
sheet = wb.active
count = 1
for i in range(0,100,25):
    ret = requests.get('https://movie.douban.com/top250?start=%s&filter='%(i))
    bs = BeautifulSoup(ret.text,'html.parser')
    ol = bs.find(name='ol',attrs={'class':'grid_view'})
    li_list = ol.find_all(name='li')
    sheet.title = '好评电影'
    sheet['A1'].value = '序号'
    sheet['B1'].value = '电影名称'
    sheet['C1'].value = '电影评分'
    sheet['D1'].value = '电影链接'
    sheet['E1'].value = '电影图片'
    for li in li_list:
        name = li.find(name='span',attrs={'class':'title'})
        a = li.find(name='a')
        span = li.find(name='span',attrs={'class':'rating_num'})
        img = a.find(name='img')
        count += 1
        sheet['A%s'%(count)].value = count - 1
        sheet['B%s'%(count)].value = name.text
        sheet['C%s'%(count)].value = span.text
        sheet['D%s'%(count)].value = a['href']
        sheet['E%s'%(count)].value = img['src']
    time.sleep(1)
wb.save('好评电影.xlsx')