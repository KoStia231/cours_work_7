from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Кастомный менеджер пользователя
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **extra_fields):
        """
        Создает и возвращает пользователя с email, именем и паролем.
        """
        if not email:
            raise ValueError('Email must be set')
        if not first_name:
            raise ValueError('First name must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        """
        Создает и возвращает суперпользователя с email, именем и паролем.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, first_name, password, **extra_fields)


class User(AbstractUser):
    username = None

    first_name = models.CharField(verbose_name='имя', max_length=30, unique=True)
    email = models.EmailField(verbose_name='почта', unique=True)
    phone_number = models.IntegerField(verbose_name='Телефон', **NULLABLE)
    telegram_chat_id = models.CharField(verbose_name='id чата тг', max_length=100, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return (f'Имя-{self.first_name}|Почта-{self.email}'
                f'|Телефон-{self.phone_number}')
