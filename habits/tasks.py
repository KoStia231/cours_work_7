import logging
from celery import shared_task
from django.utils import timezone
from asgiref.sync import async_to_sync
from habits.models import Habit
from habits.utils import send_habit_reminder

logger = logging.getLogger('habits.tasks')


@shared_task
def check_habit_reminders():
    now = timezone.now()
    today = now.date()

    logger.debug("Starting habit reminders check")
    habits = Habit.objects.filter(is_active=True, autor__isnull=False)

    for habit in habits:
        logger.debug(
            f"Checking habit: {habit.title}, last_performed: {habit.last_performed}, time_action: {habit.time_action}")

        action_time_today = timezone.make_aware(
            timezone.datetime.combine(today, habit.time_action)
        )

        # Условие для следующего выполнения привычки
        if habit.last_performed:
            next_action_date = habit.last_performed + timezone.timedelta(days=habit.execution_interval_day)
            logger.debug(f"Next action date for habit '{habit.title}': {next_action_date}")
            if next_action_date > today:
                logger.debug(f"Skipping habit '{habit.title}' since next action date has not arrived.")
                continue

        # время напоминания
        reminder_time = action_time_today - timezone.timedelta(minutes=5)

        if reminder_time <= now < action_time_today:
            chat_id = habit.autor.telegram_chat_id
            logger.debug(f"Sending reminder for habit '{habit.title}' to chat ID: {chat_id}")
            # оборот асинхрон в синхрон
            async_to_sync(send_habit_reminder)(
                chat_id, habit.title, habit.place, habit.action, habit.time_action, habit.prize
            )
            habit.last_performed = now
            habit.save()
            logger.debug(f"Habit '{habit.title}' marked as performed at {now}")

    logger.debug("Completed habit reminders check")
