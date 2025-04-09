from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'Пользователь'),
        ('admin', 'Администратор')
    )

    first_name = models.CharField(verbose_name='имя пользователя', max_length=45, blank=True, null=True)
    last_name = models.CharField(verbose_name='фамилия пользователя', max_length=45, blank=True, null=True)
    phone = models.CharField(verbose_name='телефон для связи', max_length=12, blank=True, null=True)
    email = models.EmailField(verbose_name='электронная почта(логин)', unique=True)
    role = models.CharField(verbose_name='роль пользователя', choices=ROLE_CHOICES, default='user')
    image = models.ImageField(verbose_name='аватарка пользователя', upload_to='media/avatars', blank=True, null=True)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f"{self.email} ({self.role})"
