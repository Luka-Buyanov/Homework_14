from typing import Any

import pytest

from src.classes import Category, Product
from src.reader import reader


@pytest.fixture
def category_add() -> Any:
    """Фикстура выводящая объект категории"""

    return Category("Бананчики и Арбузики", "Много бананчиков и арбузиков", [1, 2])


@pytest.fixture
def product_add() -> Any:
    """Фикстура выводящая объект продукта"""

    return Product("Бананчик", "Бананчик", 55.1, 5)


def test_products(product_add: Any) -> None:
    """Тест проверяющий корректную инициализацию объектов класса Product"""

    assert product_add.name == "Бананчик"
    assert product_add.description == "Бананчик"
    assert product_add.price == 55.1
    assert product_add.quantity == 5


def test_category(category_add: Any) -> None:
    """Тест проверяющий корректную инициализацию объектов класса Category"""

    assert category_add.name == "Бананчики и Арбузики"
    assert category_add.description == "Много бананчиков и арбузиков"
    assert category_add.add_product == [1, 2]


def test_counters(category_add: Any) -> None:
    """Тест проверяющий корректную работу счётчиков в классе Category"""

    assert category_add.category_count == 2
    assert category_add.product_count == 4


def test_file_read_1() -> None:
    """Тест проверяющий корректную работу чтения из JSON файла второй категории"""

    category_1 = reader()[1]
    assert category_1.name == "Телевизоры"
    assert category_1.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, станет " "вашим другом и помощником"
    )


def test_file_read_2() -> None:
    """Тест проверяющий корректную работу чтения из JSON файла первой категории"""

    category_2 = reader()[0]
    assert category_2.name == "Смартфоны"
    assert category_2.description == (
        "Смартфоны, как средство не только коммуникации, но и получение " "дополнительных функций для удобства жизни"
    )


def test_file_read_counter() -> None:
    """Тест проверяющий корректную работу счётчиков в классе Category после всех операций"""

    category_3 = reader()[1]
    assert category_3.category_count == 8
    assert category_3.product_count == 16
