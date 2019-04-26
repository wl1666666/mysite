#这个py文件是为了爬取豆瓣网电影数据，可先单独运行将数据添加进数据库
import requests
from bs4 import BeautifulSoup
import re
from .models import Gallery

movie_name=[]    #电影名称
movie_director=[]  #导演
movie_quote=[]   #电影简介
movie_image=[]  #电影图片
movies=[]   #电影信息集合

#获取Top前25的电影
def getmovies():
    url='https://movie.douban.com/top250?'
    result=requests.get(url,timeout=10)
    soup=BeautifulSoup(result.text,'html.parser')

    #电影名称
    title=soup.find_all('div',class_='hd')
    for each in title:
        temp=each.a.span.text
        movie_name.append(temp)
    #导演
    director=soup.find_all('div',class_='bd')
    for each in director:
        temp=each.p.text
        if temp=='豆瓣':
            continue
        movie_director.append(temp.replace(" ",""))
    #简介
    quote=soup.find_all('p',class_='quote')
    for each in quote:
        temp=each.span.text
        movie_quote.append(temp)
    #图片
    reg='src="https:.+.jpg"'
    imgre=re.compile(reg)
    movie_image=imgre.findall(result.text)

    return (movie_name,movie_director,movie_quote,movie_image)


#下方代码用来获取每部电影对应的图片
'''
(name,director,quote,image)=getmovies()
for i in range(len(image)):
    temp=requests.get(image[i][5:-1])
    with open(r'D:\picture\%s.jpg' % i,'wb') as f:
        f.write(temp.content)

print('success')
'''