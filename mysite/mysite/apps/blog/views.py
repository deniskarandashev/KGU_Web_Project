from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def index(request) :
#    return HttpResponse("Это работает!")

#def second(request) :
#    return HttpResponse("Это тоже работает!")

def index(request) :
    return render(request, 'blog/homepage.html', )