from django.db import models

class Article(models.Model):
    title = models.CharField('название статьи', max_length= 120)
    body = models.TextField('текст статьи')
    date = models.DateTimeField('дата публикации') 

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('имя автора', max_length=30)
    comment_text = models.CharField('текст комментария', max_length=220)   