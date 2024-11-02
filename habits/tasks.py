import telegram
from celery import shared_task
from django.conf import settings
from django.utils import timezone

from .models import Habit


def send_habit_reminder(chat_id, habit_title):
    try:
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
        message = f'Напоминание: пора выполнить привычку "{habit_title}" через 5 минут!'
        bot.send_message(chat_id=chat_id, text=message)
    except telegram.error.TelegramError as e:
        print(f"Ошибка отправки сообщения: {e}")


@shared_task
def check_habit_reminders():
    now = timezone.now()
    today = now.date()
    habits = Habit.objects.all()

    for habit in habits:
        # Расчет время выполнения привычки сегодня
        action_time_today = timezone.make_aware(
            timezone.datetime.combine(today, habit.time_action)
        )

        # Если привычка повторяется каждые N дней или часов, добавляет их к `last_performed`
        if habit.last_performed:
            next_action_date = habit.last_performed + timezone.timedelta(
                days=habit.execution_interval_day or 0,
                hours=habit.execution_interval_hour or 0
            )
            # Пропуск, если привычку не нужно выполнять сегодня
            if next_action_date.date() > today:
                continue

        # напоминание за 5 минут до времени действия
        reminder_time = action_time_today - timezone.timedelta(minutes=5)

        # Проверка на необходимость отправки напоминания
        if reminder_time <= now < action_time_today:
            chat_id = habit.autor.telegram_chat_id
            if chat_id:
                send_habit_reminder(chat_id, habit.title)
                habit.last_performed = now
                habit.save()
