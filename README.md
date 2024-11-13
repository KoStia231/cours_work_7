## Мини проект с напоминаниями о привычках

## Дока вот 

* http://localhost:8000/swagger/
---
## Запуск контейнера 
- Внимательно прочитать .env.example
- Создать .env.prod
- запустить одной командой из корня проекта

##### Команда запуска
```bash
docker-compose up --build 
```
###### Больше ничего не нужно делать, миграции будут применены база данных будет заполнена фикстурой сама
###### [entrypoint.sh](entrypoint.sh) это костыль чтобы не было ошибок при билде контейнера

---
## Запуск без контейнера
### Для настроек проекта нужно использовать переменные окружения

###### пример файла .env

```
.env.example
```

### Установить все зависимости

```python
pip install - r requirements.txt
```

### Применить все миграции

```python
python manage.py migrate 
```

### Создать админа

```python
python manage.py admin_reg
```


###### Файл для создания админа находится по пути

###### users/management/commands/admin_reg.py

---
### Запуск сервера

```python
python manage.py runserver 
```


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

