#!/bin/bash

# Виконуємо міграції бази даних під час запуску контейнера Shop
python manage.py migrate

# Інші дії, необхідні для підготовки середовища
docker-compose exec shop python manage.py createsuperuser

docker-compose up shop


# Запускаємо команду запуску сервера Django
exec "$@"