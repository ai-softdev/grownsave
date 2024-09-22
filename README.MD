

# Grow'n Save MVP Project

## Описание
Это MVP проект, разделенный на три основных компонента: backend, front-end и AI сервисы.

## User Flow Diagram
![User Flow Diagram](grown-userflow.drawio.png)
![User Flow](User%20flow%20(Grow'n%20Save!).png)
## Database Structure
![Database Structure](database.drawio.png)
## Ссылка на дизайн: https://www.figma.com/design/PJ4a78cS8Mxu4xZJrctVrg/1?node-id=19-869&node-type=frame&t=LXZ9Cjfbo923IbRT-0
## Ссылки на документацию компонентов

### Backend
Документация и API для backend части доступна по ссылке:
[Backend API Docs](https://api-grownsave.ai-softdev.com/docs)

### Front-End
front-end часть доступна по ссылке:
[Front-End MVP](https://grownsave.ai-softdev.com/)

### AI
Документация для AI сервисов доступна по ссылке:
[AI Docs](https://ai-grownsave.ai-softdev.com/docs)

## Запуск проекта

## Требования
- Docker
- Docker Compose
- Windows или другая ОС с поддержкой Docker

## Установка и запуск

### 1. Клонирование репозитория
Клонируйте репозиторий на свою локальную машину:
```bash
git clone https://github.com/ai-softdev.com/grownsave.git
```

### 2. Запуск Docker
Если вы используете Windows, убедитесь, что Docker запущен.

### 3. Сборка и запуск контейнеров
Выполните следующую команду для сборки и запуска контейнеров в фоновом режиме:
```bash
docker-compose up --build -d
```

### 4. Автогенерация ревизии Alembic
Создайте новую ревизию для миграций базы данных с помощью Alembic:
```bash
docker exec -it back alembic revision --autogenerate
```

### 5. Применение миграций Alembic
Примените созданные миграции:
```bash
docker exec -it back alembic upgrade head
```

### 6. Заполнение базы данных
Запустите скрипт для начального заполнения базы данных:
```bash
docker exec -it back python seeder.py
```

### 7. Остановка контейнеров
Чтобы остановить контейнеры, выполните следующую команду:
```bash
docker-compose down
```


## Примечания
- Убедитесь, что у вас установлены последние версии Docker и Docker Compose.
- Все команды выполняются из директории `ai`.

## Лицензия
Этот проект лицензирован на условиях [MIT License](LICENSE).


## Лицензия
Этот проект лицензирован на условиях [MIT License](LICENSE).
