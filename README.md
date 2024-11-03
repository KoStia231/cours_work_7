## Мини проект с напоминаниями о привычках

## Дока вот 

* http://localhost:8000/swagger/
---
## Запуск Celery worker
````
celery -A config worker --loglevel=info
````

## Запуск Celery Beat
```
celery -A config beat --loglevel=info
```
---
### Что-бы бот работал нужно узнать свой чат id
### Я использовал в своем боте отдельно вот этот подход 
```python
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    chat_id = message.chat.id
    await message.answer(f"Бот запущен. Ваш chat_id: {chat_id}")
```

