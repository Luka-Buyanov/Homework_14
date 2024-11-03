# Интернет магазин
Это проект интернет магазина работающего с классами в python.
Создаётся в рамках домашнего задания 4 курса "Python - разработчик" от Skypro.

## Содержание
- [Используемые версии](#используемые-версии)
- [Использование](#использование)
- [Тестирование](#тестирование)
- [Сделано](#сделано)
- [To do](#to-do)

## Используемые версии
- python = "^3.13"
- black = "^24.8.0"
- isort = "^5.13.2"
- flake8 = "^7.1.1"
- mypy = "^1.11.2"
- pytest = "^8.3.3"
- requests = "^2.32.3"
- python-dotenv = "^1.0.1"
- pytest-cov = "^5.0.0"

## Использование
Скачать и открыть в pycharm.

## Тестирование
В проекте имеются инструменты для проверки:
- black
- isort
- flake 8
- mypy

Для их использования введите команду:

``
(название инструмента) .
``

В проекте написаны тесты к классам и функциям проекта.
Для их запуска используется pytest. Также в проекте содержится отчёт о покрытии тестами.

## Сделано
Созданы классы Category, Product, Order и Iterator, а также подклассы из Product - Smartphone и LawnGrass. Дополнительно реализованы абстрактные классы и миксин. Содержащие в себе:
- Category:
- - Название категории
- - Описание категории
- - Список продуктов (приватный)
- - Счётчик категорий
- - Счётчик продуктов
- Product:
- - Название продукта
- - Описание продукта
- - Цена продукта (приватная)
- - Количество продукта
- Iterator:
- - Объект итерации
- - Внутренний объект для работы итератора
- Smartphone:
- - Производительность смартфона
- - Модель смартфона
- - Объём памяти в гигабайтах
- - Цвет смартфона
- LawnGrass:
- - Страна-производитель
- - Срок прорастания
- - Цвет газонной травы
- Order
- - Заказанный товар
- - Количество товара в заказе
- - Общая сумма заказа

Также создана функция читающая данные для классов из файла формата JSON.

## To do
- [x] Создать логику проекта
- [x] Реализовать классы проекта
- [x] Реализовать функцию чтения из файла формата JSON
- [x] Написать тесты для функциональности проекта
- [x] Сделать некоторые атрибуты приватными и создать для них геттеры и сеттеры
- [x] Добавить модули для добавления нового продукта в категорию и создания нового продукта из списка с данными
- [x] Написать тесты для новых функциональности проекта
- [x] Модифицировать классы для возможности их строкового оформления
- [x] Добавить вспомогательный класс для возможности итерации
- [x] Написать тесты для новых функциональности проекта
- [x] Добавить подклассы Smartphone и LawnGrass
- [x] Модифицировать модули сложения продуктов и добавления товара в категорию для защиты от некорректной операции
- [x] Написать тесты для новых функциональностей
- [x] Реализовать абстрактные классы и миксин
- [x] Реализовать класс для заказов
- [x] Написать тесты для новых функциональностей
- [ ] Продолжать работу по поступающим заданиям