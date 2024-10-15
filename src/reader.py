import json
from typing import Any

from src.classes import Category, Product


def reader(path: str = "../data/products.json") -> Any:
    """Функция чтения категорий и продуктов из файла JSON"""

    list_categories: list = []
    try:
        with open(path, encoding="utf8") as file:
            data = json.load(file)
    except FileNotFoundError:
        list_categories = []
    else:
        for category in data:
            products = []
            for product in category["products"]:
                products.append(
                    Product(product["name"], product["description"], product["price"], product["quantity"])
                )
            answer = Category(category["name"], category["description"], products)
            list_categories.append(answer)
    return list_categories
