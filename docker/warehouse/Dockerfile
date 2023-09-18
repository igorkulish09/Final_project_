# Dockerfile для проекта Warehouse
FROM python:3.11

WORKDIR /app

# Устанавливаем зависимости
COPY warehouse/requirements.txt /app/
RUN pip install -r requirements.txt

# Копируем проект Warehouse в контейнер
COPY warehouse /app/

# Копируем скрипты для запуска
COPY docker/warehouse/docker-entrypoint.sh /docker-entrypoint.sh
COPY docker/warehouse/runserver.sh /runserver.sh
COPY docker/warehouse/wait-for-command.sh /wait-for-command.sh

CMD ["/docker-entrypoint.sh"]
