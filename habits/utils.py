import telegram
from config.settings import TELEGRAM_BOT_TOKEN


async def send_habit_reminder(chat_id, habit_title, habit_place, habit_action, habit_time_action, habit_prize):
    try:
        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
        message = (f'Напоминание: пора выполнить привычку "{habit_title}" через 5 минут!'
                   f'Нужно сделать {habit_action} в этом месте {habit_place}, в это время {habit_time_action}'
                   f', а вот награда{habit_prize}')
        await bot.send_message(chat_id=chat_id, text=message)
        print(f"Message sent to chat ID: {chat_id} for habit: {habit_title}")
    except telegram.error.TelegramError as e:
        print(f"Ошибка отправки сообщения: {e}")
