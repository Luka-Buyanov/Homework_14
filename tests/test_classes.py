from typing import Any

import pytest

from src.classes import Category, Iterator, LawnGrass, Order, Product, Smartphone
from src.reader import reader

product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

smartphone1 = Smartphone(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
)
smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
smartphone4 = Smartphone(
    "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 10, 95.5, "S23 Ultra", 256, "Серый"
)

grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])

order1 = Order(smartphone4, 5)

category_empty = Category("Пустая категория", "Категория без продуктов", [])


@pytest.fixture
def category_add() -> Any:
    """Фикстура выводящая объект категории"""

    return Category("Бананчики и Арбузики", "Много бананчиков и арбузиков", [product1, product2])


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
    assert category_add.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 " "руб. Остаток: 8 шт."
    )


def test_counters(category_add: Any) -> None:
    """Тест проверяющий корректную работу счётчиков в классе Category"""

    assert category_add.category_count == 4
    assert category_add.product_count == 6


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
    assert category_3.category_count == 10
    assert category_3.product_count == 18


def test_append_product(category_add: Any, capsys: Any) -> None:
    """Тест проверяющий функцию добавления нового продукта в категорию и проверяющий выводы в консоль"""

    category_add.add_product(product3)
    assert category_add.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.Iphone 15, 210000.0 "
        "руб. Остаток: 8 шт.Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    captured = capsys.readouterr()
    assert captured.out == "Добавлен новый товар в категорию!\nОбработка добавления товара завершена.\n"


def test_new_product() -> None:
    """Тест проверяющий создание нового продукта из списка настроек"""

    dictionary_options = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    assert Product.new_product(dictionary_options).name == "Samsung Galaxy S23 Ultra"
    assert Product.new_product(dictionary_options).description == "256GB, Серый цвет, 200MP камера"
    assert Product.new_product(dictionary_options).price == 180000.0
    assert Product.new_product(dictionary_options).quantity == 5


def test_current_product() -> None:
    """Тест проверяющий работу создателя продукта если продукт с таким названием уже есть"""

    dictionary_options = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    test_value = Product.new_product(dictionary_options, [product1, product2, product3])
    assert test_value.name == "Samsung Galaxy S23 Ultra"
    assert test_value.description == "256GB, Серый цвет, 200MP камера"
    assert test_value.price == 180000.0
    assert test_value.quantity == 10


def test_less_price() -> None:
    """Тест проверяющий работу создателя продукта если продукт с таким именем уже существует и у нового меньшая цена"""

    dictionary_options = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 70000.0,
        "quantity": 5,
    }
    test_value = Product.new_product(dictionary_options, [product1, product2, product3])
    assert test_value.name == "Samsung Galaxy S23 Ultra"
    assert test_value.description == "256GB, Серый цвет, 200MP камера"
    assert test_value.price == 180000.0
    assert test_value.quantity == 10


def test_zero_price(capsys: Any) -> None:
    """Тест проверяющий работу создателя продукта при передаче нулевой цены"""

    product1.price = 0
    assert product1.price == 180000.0
    captured = capsys.readouterr()
    assert captured.out == "Цена не должна быть нулевая или отрицательная!\n"


def test_add_products() -> None:
    """Тест проверяющий корректность работы функции сложения двух продуктов"""

    assert product1 + product2 == 2580000.0


def test_str_product() -> None:
    """Тест проверяющий корректность вывода строкового представления продукта"""

    assert str(product1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category(category_add: Any) -> None:
    """Тест проверяющий корректность вывода строкового представления категории"""

    assert str(category_add) == "Бананчики и Арбузики, количество продуктов: 13 шт."


def test_iterator(category_add: Any) -> None:
    """Тест проверяющий корректность работы итератора"""

    answer = []
    for i in Iterator(category_add):
        answer.append(i)
    assert answer == ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 ", "Iphone 15, 210000.0 руб. Остаток: 8 "]


def test_addition_not_same_classes() -> None:
    """Тест сложения объектов разных типов (смартфонов с травой)"""

    with pytest.raises(TypeError) as error:
        smartphone1 + grass1
    assert str(error.value) == "Ошибка: классы продуктов не одинаковы! (Не складывайте траву со " "смартфонами!!!)"


def test_add_not_product() -> None:
    """Тест добавления в категорию объекта не являющегося продуктом"""

    with pytest.raises(TypeError) as error:
        category_smartphones.add_product("Not a product")
    assert str(error.value) == "Нельзя добавлять в категории не продукты!"


def test_smartphone() -> None:
    """Тест корректной инициализации класса Smartphone"""

    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.quantity == 5
    assert smartphone1.price == 180000.0
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.efficiency == 95.5


def test_grass() -> None:
    """Тест корректной инициализации класса Grass"""

    assert grass1.name == "Газонная трава"
    assert grass1.description == "Элитная трава для газона"
    assert grass1.price == 500.0
    assert grass1.quantity == 20
    assert grass1.country == "Россия"
    assert grass1.germination_period == "7 дней"
    assert grass1.color == "Зеленый"


def test_repr() -> None:
    """Тест проверяющий работу Миксина"""

    assert repr(product1) == (
        "Product('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', " "'180000.0', '5') "
    )


def test_order_counter() -> None:
    """Тест счётчика товаров в классе order"""

    assert order1.quantity_counter() == "Заказано 5шт. товара."


def test_category_counter(category_add: Any) -> None:
    """Тест счётчика товаров в классе category"""

    assert category_add.quantity_counter() == "В категории 13шт. товара"


def test_order(capsys: Any) -> None:
    """Тест проверяющий работу вывода заказа в строковом формате и проверяющий выводы в консоль"""

    order1 = Order(smartphone4, 5)
    assert str(order1) == "Заказано: Samsung Galaxy S23 Ultra - 5шт. на сумму 900000.0руб."
    captured = capsys.readouterr()
    assert captured.out == "Товар добавлен в заказ!\nОбработка добавления товара завершена.\n"


def test_zero_quantity_product() -> None:
    """Тест проверяющий инициализацию продукта с нулевым количеством"""

    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен!"):
        Product("Бракованный товар", "Неверное количество", 1000.0, 0)


def test_zero_category_products() -> None:
    """Тест проверяющий подсчёт средней цены при нулевом количестве товаров"""

    assert category_empty.middle_price() == 0


def test_category_middle_price() -> None:
    """Тест проверяющий подсчёт средней цены"""

    assert category_smartphones.middle_price() == "Средняя цена товаров в категории: 30000.0руб."
