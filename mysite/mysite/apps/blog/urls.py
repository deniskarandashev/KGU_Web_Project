from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>', views.single, name='single'),
    path('payment', views.payment, name='payment')
]