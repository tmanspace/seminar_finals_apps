# FastAPI Microservices Project

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-orange)
![Docker](https://img.shields.io/badge/Docker-ready-green)

## Описание

Проект включает два микросервиса, разработанных с использованием **FastAPI**:
1. **TODO Application** — управление задачами (создание, обновление, удаление и просмотр списка задач).
2. **Short URL Service** — сокращение длинных ссылок и перенаправление на них.

Оба приложения поддерживают автоматическую документацию API через **Swagger UI** и работают с базой данных **SQLite**.

---

## Функциональные возможности

### TODO Application
- Создание, обновление, удаление и просмотр задач.
- Хранение данных в SQLite.
- Встроенная документация API доступна по адресу `/docs`.

### Short URL Service
- Генерация коротких ссылок для длинных URL.
- Перенаправление по короткой ссылке.
- Статистика использования коротких ссылок.
- Хранение данных в SQLite.
- Документация API доступна по адресу `/docs`.

---

## Установка и запуск

### 1. **Запуск через Docker Hub**

Проект уже опубликован на **Docker Hub**, и вы можете загрузить готовые образы:

#### Запуск TODO-приложения
1. Скачайте образ:
```bash
docker pull timuredu/todo_app:latest
```
2. Запустите контейнер:
```bash
docker run -d --name todo_app_container -p 8000:80 -v ./data:/app/data timuredu/todo_app:latest
```
3. Приложение будет доступно:
* http://localhost:8000
* Документация API: http://localhost:8000/docs

#### Запуск Short URL-приложения
1. Скачайте образ:
```bash
docker pull timuredu/shorturl_app:latest
```
2. Запустите контейнер:
```bash
docker run -d --name shorturl_app_container -p 8001:80 -v ./data:/app/data timuredu/shorturl_app:latest
```
3. Приложение будет доступно:
* http://localhost:8001
* Документация API: http://localhost:8001/docs
---
## 2. Запуск через Docker Compose
1. Склонируйте репозиторий:
```bash
git clone https://github.com/seminar_finals_apps/fastapi-microservices.git
cd fastapi-microservices
```
2. Запустите проект:
```bash
docker-compose up --build
```
3. Сервисы будут доступны:
* TODO-приложение: http://localhost:8000
* Short URL-приложение: http://localhost:8001
---
## API Методы
### TODO-приложение
* POST /items — Создание новой задачи.
* GET /items — Получение списка задач.
* GET /items/{id} — Получение задачи по ID.
* PUT /items/{id} — Обновление задачи по ID.
* DELETE /items/{id} — Удаление задачи.
* Документация доступна на http://localhost:8000/docs.

### Short URL-приложение
* POST /shorten — Создание короткой ссылки для длинного URL.
* GET /{short_id} — Перенаправление по короткой ссылке.
* GET /stats/{short_id} — Получение статистики для короткой ссылки.
* Документация доступна на http://localhost:8001/docs.