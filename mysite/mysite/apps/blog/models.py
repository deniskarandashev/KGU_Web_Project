from django.db import models

class Post(models.Model):
    title = models.CharField('Title of the note', max_length= 120)
    body = models.TextField('Text of the note')
    date = models.DateTimeField('Date of the publication') 
    img = models.ImageField('Image')

class Heading(models.Model):
    title = models.CharField('Title of the note', max_length= 120)


# созданы в учебных целях

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


# созданы для финального варианта

class HeadArticle(models.Model):
    title = models.CharField('title', max_length= 120)
    body = models.TextField('text')
    date = models.DateTimeField('date') 
    price = models.DecimalField('price', max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Head Article'
        verbose_name_plural = 'Head Articles'

class OtherArticle(models.Model):
    title = models.CharField('title', max_length= 120)
    body = models.TextField('text')
    date = models.DateTimeField('date') 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Other Article'
        verbose_name_plural = 'Other Articles'