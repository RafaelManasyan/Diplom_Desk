import os.path

from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import MEDIA_ROOT


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор')
    )

    first_name = models.CharField(verbose_name='имя пользователя', max_length=45)
    last_name = models.CharField(verbose_name='фамилия пользователя', max_length=45)
    phone = models.CharField(verbose_name='телефон для связи', max_length=12)
    email = models.EmailField(verbose_name='электронная почта(логин)', unique=True)
    role = models.CharField(verbose_name='роль пользователя', choices=ROLE_CHOICES, default='user')
    image = models.ImageField(verbose_name='аватарка пользователя', upload_to='media/avatars', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.role})"
