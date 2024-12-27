# TODO Application

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/framework-FastAPI-orange)

## Описание

**TODO Application** — это простое и удобное приложение для управления задачами, реализованное на базе **FastAPI**. Оно предоставляет API для создания, просмотра, обновления и удаления задач, с хранением данных в базе **SQLite**.

---

## Функциональные возможности

- **CRUD-операции для задач**:
  - Создание задач.
  - Получение списка всех задач.
  - Обновление задачи.
  - Удаление задачи.
- **Поддержка базы данных SQLite**.
- **Интерактивная документация API**:
  - Доступна по адресу `/docs`.
- **Простая установка и запуск с Docker**.
- **Готовый образ на Docker Hub**:
  - Доступен для загрузки по адресу: [timuredu/todo_app](https://hub.docker.com/r/timuredu/todo_app).

---

## Установка и запуск

### 1. **Запуск с использованием Docker Hub**

1. Убедитесь, что у вас установлен Docker.
2. Скачайте образ:
   ```bash
   docker pull timuredu/todo_app:latest
3. Запустите приложение:
    ```bash
   docker run -d --name todo_app_container -p 8000:80 -v ./data:/app/data timuredu/todo_app:latest
4. Перейдите по адресу:

* Документация API: http://localhost:8000/docs

## Примеры использования

### Создание задачи

`POST http://localhost:8000/items`

Пример тела запроса:
```json
{
  "title": "Купить продукты",
  "description": "Молоко, яйца, хлеб",
  "completed": false
}
```
Ответ:
```json
{
  "id": 3,
  "title": "Купить продукты",
  "description": "Молоко, яйца, хлеб",
  "completed": false
}
```

### Получение списка задач

`GET /items`

Ответ:

```json
[
  {
    "title": "Hello",
    "description": "world",
    "completed": false,
    "id": 1
  },
  {
    "id": 3,
    "title": "Купить продукты",
    "description": "Молоко, яйца, хлеб",
    "completed": false
  }
]
```

### Обновление задачи
`PUT /items/{item_id}`

Пример запроса:
`http://localhost:8000/items/3`
```json
{
  "title": "Купить продукты",
  "description": "Молоко, яйца, хлеб",
  "completed": true
}
```

Ответ:

```json
{
  "id": 3,
  "title": "Купить продукты",
  "description": "Молоко, яйца, хлеб",
  "completed": true
}
```

### Удаление задачи
`DELETE /items/{item_id}`

Пример запроса:

`http://localhost:8000/items/2`
Ответ:

```json
{
  "message": "Item deleted successfully"
}
```
