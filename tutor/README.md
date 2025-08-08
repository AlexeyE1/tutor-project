# Наставник - Платформа для поиска репетиторов

## 🚀 Быстрый старт

### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 2. Настройка базы данных PostgreSQL

#### Установка PostgreSQL:
- **Windows**: Скачайте с https://www.postgresql.org/download/windows/
- **Linux**: `sudo apt install postgresql postgresql-contrib`

#### Создание базы данных:
```bash
# Подключитесь к PostgreSQL
psql -U postgres

# Создайте базу данных
CREATE DATABASE tutor_db;

# Выйдите
\q
```

### 3. Настройка переменных окружения

Скопируйте файл `env_example.txt` как `.env`:
```bash
cp env_example.txt .env
```

Отредактируйте файл `.env` и заполните свои значения:
```env
# Настройки базы данных PostgreSQL
DB_NAME=tutor_db
DB_USER=postgres
DB_PASSWORD=ваш_пароль_от_postgres
DB_HOST=localhost
DB_PORT=5432

# Секретный ключ Django
SECRET_KEY=django-insecure-y4@z3y6a#o-s(81cze#+@j6@%*%-c4@lvku_sf+-l(dl9^(d1$'

# Настройки отладки
DEBUG=True
```

### 4. Запуск проекта

```bash
# Создайте миграции
python manage.py makemigrations

# Примените миграции
python manage.py migrate

# Создайте суперпользователя
python manage.py createsuperuser

# Запустите сервер
python manage.py runserver
```

### 5. Откройте сайт
- Главная страница: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/

## 📁 Структура проекта

```
tutor/
├── manage.py
├── requirements.txt
├── .env                    # Секретные данные (не в Git)
├── env_example.txt         # Пример файла .env
├── templates/              # Общие шаблоны
│   └── base.html
├── static/                 # Статические файлы
│   ├── css/
│   └── js/
├── media/                  # Загруженные файлы
├── tutor/                  # Настройки проекта
├── main/                   # Главное приложение
├── accounts/               # Пользователи
├── catalog/                # Каталог наставников
└── reviews/                # Отзывы
```

## 🔐 Безопасность

- Файл `.env` содержит секретные данные и не попадает в Git
- Все пароли и ключи хранятся в переменных окружения
- В продакшене используйте сложные пароли и HTTPS

## 🛠️ Разработка

### Добавление новых приложений:
```bash
python manage.py startapp my_app
```

### Создание миграций:
```bash
python manage.py makemigrations my_app
python manage.py migrate
```

### Создание суперпользователя:
```bash
python manage.py createsuperuser
```

## 🚀 Деплой

### Клонирование репозитория
```bash
# Клонируйте репозиторий
git clone https://github.com/ваш_username/tutor-project.git
cd tutor-project

# Установите зависимости
pip install -r requirements.txt

# Создайте и настройте .env файл
cp env_example.txt .env
# Отредактируйте .env файл
```

### Обновление кода
```bash
# Получите последние изменения
git pull origin main

# Обновите зависимости
pip install -r requirements.txt

# Примените миграции
python manage.py migrate
```

### Отправка изменений
```bash
# Добавьте изменения
git add .

# Создайте коммит
git commit -m "Описание ваших изменений"

# Отправьте на GitHub
git push origin main
```

## 📝 Лицензия

MIT License

