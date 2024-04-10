FROM python:3.10.9


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip


WORKDIR /myshop

COPY requirements.txt /myshop/

# Встановлюємо залежності проекту
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо код проекту в контейнер
COPY . /myshop  /

# Встановлюємо команду для запуску сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
