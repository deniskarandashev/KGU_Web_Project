from django.db import models

class Article(models.Model):
    title = models.CharField('название статьи', max_length= 120)
    body = models.TextField('текст статьи')
    date = models.DateTimeField('дата публикации') 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('имя автора', max_length=30)
    comment_text = models.CharField('текст комментария', max_length=220)  

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии' 