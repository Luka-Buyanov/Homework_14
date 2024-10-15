import pytest

from src.classes import Category, Product


@pytest.fixture
def product_add():
    return Product("Бананчик", "Бананчик", 55.1, 5)

def test_products(product_add) -> None:
    assert product_add.name == "Бананчик"
    assert product_add.description == "Бананчик"
    assert product_add.price == 55.1
    assert product_add.quantity == 5

@pytest.fixture
def category_add():
    return Category("Бананчики и Арбузики", "Много бананчиков и арбузиков", [1, 2])

def test_category(category_add) -> None:
    assert category_add.name == "Бананчики и Арбузики"
    assert category_add.description == "Много бананчиков и арбузиков"
    assert category_add.products == [1, 2]

def test_counters(category_add) -> None:
    assert category_add.category_count == 2
    assert category_add.product_count == 4