from django.db import models


class Fandom(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    phrase = models.TextField(null=True, blank=True)
    poster_link = models.TextField(null=True, blank=True)


class Book(models.Model):
    Category = (
        ('films', 'Фильмы'),
        ('books', 'Книги'),
        ('games', 'Игры'),
        ('anime', 'Аниме'),
        ('cartoons', 'Мультфильмы')
    )

    Genre = (
        ('action', 'Экшен'),
        ('adventure', 'Приключения'),
        ('comedy', 'Комедия'),
        ('drama', 'Драма'),
        ('fantasy', 'Фэнтези'),
        ('horror', 'Ужасы')
    )

    author = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=255)
    desc = models.TextField(null=True, blank=True)
    cover = models.TextField(null=True, blank=True)
    fandoms = models.ForeignKey(Fandom, on_delete=models.CASCADE, null=True, blank=True)
    category = models.CharField(max_length=100, choices=Category, null=True, blank=True)
    genre = models.CharField(max_length=100, choices=Genre, null=True, blank=True)


