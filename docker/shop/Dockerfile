# Dockerfile для проекта Shop
FROM python:3.11

WORKDIR /app

# Устанавливаем зависимости
COPY shop/requirements.txt /app/
RUN pip install -r requirements.txt

# Копируем проект Shop в контейнер
COPY shop /app/

# Копируем скрипты для запуска
COPY docker/shop/docker-entrypoint.sh /docker-entrypoint.sh
COPY docker/shop/runserver.sh /runserver.sh
COPY docker/shop/wait-for-command.sh /wait-for-command.sh

CMD ["/docker-entrypoint.sh"]
