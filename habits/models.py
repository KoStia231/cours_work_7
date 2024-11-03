from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):

    class IsPublicHabit(models.TextChoices):
        OPEN = 'O', 'Открытая привычка'
        PRIVATE = 'P', 'Приватная привычка'

    is_public = models.CharField(
        max_length=1, default=IsPublicHabit.PRIVATE, choices=IsPublicHabit, verbose_name='публичная/приватная'
    )

    autor = models.ForeignKey('users.User', on_delete=models.SET_NULL, verbose_name='Автор привычки', null=True)
    title = models.CharField(max_length=100, verbose_name='Название привычки')
    place = models.CharField(max_length=100, verbose_name='Место')
    duration = models.PositiveIntegerField(verbose_name='Продолжительность в минутах')
    time_action = models.TimeField(max_length=25, verbose_name='Время, когда надо выполнить привычку')
    action = models.CharField(max_length=100, verbose_name='Действие, которое надо сделать')
    prize = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная-True/Полезная-False')
    last_performed = models.DateField(verbose_name='Дата последнего выполнения', **NULLABLE)
    execution_interval_day = models.PositiveIntegerField(default=1, verbose_name='Интервал выполнения (дни)')
    is_active = models.BooleanField(default=True, verbose_name='Активна/Не активна')
    related = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name='Связанная с другой привычкой', **NULLABLE
    )

    def __str__(self):
        return (f'{self.id}|{self.title}|{self.action}|{self.time_action}|'
                f'{self.place}|{self.duration}|{self.is_pleasant}')

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
