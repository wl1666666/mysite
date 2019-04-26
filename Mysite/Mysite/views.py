from django.shortcuts import render
from getmovies.models import Gallery
from getmovies.Movie import getmovies

def show(request):
    #先判断模板中数据是否为空，若为空则添加电影信息
    if Gallery.objects.filter().count()==0:
        (name, director, quote, image) = getmovies()
        for i in range(len(name)):
            addition = Gallery(description=quote[i], director=director[i], title=name[i], image=r'images/%s.jpg' % i)
            addition.save()

    gallerys = Gallery.objects

    return render(request,'home.html',{'gallerys':gallerys})
