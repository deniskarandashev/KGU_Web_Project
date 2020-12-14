from django.contrib import admin
from blog.models import Article, Comment, PlantsForSale, InfoArticle, City

admin.site.register(Article)
admin.site.register(Comment)

admin.site.register(PlantsForSale)
admin.site.register(InfoArticle)

admin.site.register(City)