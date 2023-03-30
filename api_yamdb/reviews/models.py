from django.db import models

from reviews.validators import validate_custom_year


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

    class Meta:
        ordering = ['-id']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

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

    class Meta:
        ordering = ['-id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        'Название произведения',
        blank=False,
        max_length=256,
    )
    year = models.PositiveIntegerField(
        'Год',
        validators=[validate_custom_year]
    )
    description = models.TextField(
        'Описание',
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Произведние'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
