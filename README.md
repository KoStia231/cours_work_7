Мини проект с напоминаниями о привычках
дока вот 
http://localhost:8000/swagger/

запуск Celery worker
````
celery -A config worker --loglevel=info
````

запуск Celery Beat
```
celery -A config beat --loglevel=info
```
