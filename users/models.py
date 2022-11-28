from django.contrib.auth.models import AbstractUser
from django.db import models

from ads.models.location import Location


class UserRole:
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    MEMBER = 'member'
    ROLES = [
        (ADMIN, 'администратор'),
        (MEMBER, 'пользователь'),
        (MODERATOR, 'модератор')
    ]


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=UserRole.ROLES, default=UserRole.MEMBER, null=True)
    age = models.SmallIntegerField(null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return self.username
