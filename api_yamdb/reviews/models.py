from django.contrib.auth.models import AbstractUser

from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)

from reviews.validators import validate_custom_year


class User(AbstractUser):
    """Обычный юзер джанго,
    но с двумя дополнительными полями ("role", "bio").
    """

    ROLE_CHOICES = [
        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin')
    ]

    bio = models.TextField(
        verbose_name='Биография',
        blank=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=10,
        choices=ROLE_CHOICES,
        default='user'
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


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


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    score = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ]
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        default_related_name = 'reviews'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        default_related_name = 'comments'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text
