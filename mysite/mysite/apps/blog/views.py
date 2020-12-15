from django.shortcuts import render
from blog.models import Article, PlantsForSale, City
from django.http import Http404, HttpResponseRedirect
from django.views.generic.list import ListView
import requests

# Create your views here.
#from django.http import HttpResponse

# def index(request) :
#    return HttpResponse("Это работает!")

# def second(request) :
#    return HttpResponse("Это тоже работает!")

#def index(request):
#    list_articles = Article.objects.order_by('-date') # вывод статей от более новой до старой
#    return render(request, 'blog/test.html', {'list_articles': list_articles} ) # заменить на blog/index.html

def single(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("Article doesn't find")
    return render(request, 'blog/single.html', {'article': a})

def main(request):
    list_plantsforsale = PlantsForSale.objects.order_by('-date')
    return render(request, './main.html', {'list_plantsforsale': list_plantsforsale} ) 


def firstblock(request, plantsforsale_id):
    try:
        i = PlantsForSale.objects.get(id = plantsforsale_id)
    except:
        raise Http404("Article doesn't find")
    return render(request, 'blog/firstblock.html', {'plantsforsale': i})

def payment(request):
    return render(request, 'blog/payment.html', {})

def login(request):
    return render(request, 'account/login.html', {})

def logout(request):
    return render(request, 'account/logout.html', {})
