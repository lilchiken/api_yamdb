from django.contrib.auth.models import AbstractUser
from django.db import models


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
