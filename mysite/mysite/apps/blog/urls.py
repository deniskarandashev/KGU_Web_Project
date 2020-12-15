from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.main, name='main'),
    path('<int:article_id>', views.single, name='single'),
    path('<int:plantsforsale_id>', views.firstblock, name='firstblock'),
    path('payment', views.payment, name='payment'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
] 