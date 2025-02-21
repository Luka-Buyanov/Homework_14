from typing import Any


class Product:
    """Класс содержащий в себе один продукт и его свойства: имя, описание, цену и количество"""

    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Функция обеспечивающая наследование"""

        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс содержащий в себе одну категорию и её продукты, а также свойства: имя, описание, список продуктов.
    Дополнительно содержит подсчёт всех категорий и всех продуктов в них."""

    category_count = 0  # Счётчик категорий
    product_count = 0  # Счётчик продуктов

    name: str  # Название категории
    description: str  # Описание категории
    products: list[Any]  # Список продуктов

    def __init__(self, name: str, description: str, products: list[Any]):
        """Функция обеспечивающая наследование и общий подсчёт"""

        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
