## Стек
- python3.9
- Django, Django REST Framework
- MySQL
- docker, docker-compose

## Запуск проекта

Собрать и запустить контейнеры:
`docker-compose up --no-deps --build`

Применить миграции:
`docker-compose run api python api/manage.py migrate`

Запустить парсер фида:
`docker-compose run api python api/manage.py parse_feed`

## Документация

`/swagger`

`/swagger_doc`

`/redoc`

## Задачи

- [x] Продумать и реализовать структуру данных для хранения и работы. Предпочтительно реляционная база данных. 
- [x] Написать парсер для фида. Для парсинга XML можно пользоваться готовой библиотекой.
- [x] Создать API с двумя эндпоинтами: POST /products - получение продуктов по категории, GET /product - получение карточки конкретного продукта (включая все офферы).

- [x] Подключение сваггера/любого другого формата автодокументации
- [x] При получении продуктов иметь возможность фильтровать по категории и цене (не менее заданного значения и не более заданного значения)
- [ ] Составить иерархию категорий и отдавать их в виде дерева, эндпоинт GET /categories.
- [x] Добавить эндпоинт для загрузки файла фида на сервер.
- [x] Собрать в Docker.