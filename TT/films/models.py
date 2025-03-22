from django.db import models

# Create your models here.
class Movie(models.Model):
	imy = models.CharField('Название фильма', max_length=50)
	opisanie = models.CharField('Краткое описание фильма', max_length=200)
	otziv = models.TextField('Отзыв')




