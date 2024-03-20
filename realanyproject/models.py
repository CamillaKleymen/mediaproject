from django.db import models


class CategoryModel(models.Model):
    category_title = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Media category'
        verbose_name_plural = 'Media categories'
class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    movie = models.FileField(upload_to='Movie/Genre/movies')

class Music(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    song = models.FileField(upload_to='Song/Genre/songs')


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    book = models.FileField(upload_to='Book/Genre/book')
