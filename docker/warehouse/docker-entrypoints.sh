#!/bin/bash

# Виконуємо міграції бази даних під час запуску контейнера Shop
python manage.py migrate

# Інші дії, необхідні для підготовки середовища
docker-compose exec warehouse python manage.py createsuperuser


# Запускаємо команду запуску сервера Django
exec "$@"
