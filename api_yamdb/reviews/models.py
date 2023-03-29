from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(
        max_length=50,
        unique=True,
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=256,
        blank=False,
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
        max_length=50,
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.TextField(
        blank=False,
        max_length=256,
    )
    year = models.PositiveIntegerField
    description = models.TextField(
        'Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        through='TitleGenre',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='category'
    )

    def __str__(self):
        return self.name


class TitleGenre(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )
