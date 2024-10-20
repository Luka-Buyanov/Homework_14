from typing import Any, Optional


class Product:
    """Класс содержащий в себе один продукт и его свойства: имя, описание, цену и количество"""

    name: str  # Название продукта
    description: str  # Описание продукта
    quantity: int  # Количество продукта

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Функция обеспечивающая инициализацию"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, new_product: dict, list_products: Optional[Any] = None) -> Any:
        """Метод создающий новый продукт из словаря с данными"""

        if list_products is not None:
            for product in list_products:
                if new_product["name"] == product.name:
                    name = new_product["name"]
                    description = new_product["description"]
                    quantity = product.quantity + new_product["quantity"]
                    if product.price < new_product["price"]:
                        price = new_product["price"]
                    else:
                        price = product.price
                    return cls(name, description, price, quantity)

        name = new_product["name"]
        description = new_product["description"]
        price = new_product["price"]
        quantity = new_product["quantity"]
        return cls(name, description, price, quantity)

    def __str__(self) -> str:
        """Функция строкового представления класса"""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        """Геттер цены"""

        return self.__price

    @price.setter
    def price(self, price: float) -> Any:
        """Сеттер цены"""

        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная!")
        else:
            if price < self.__price:
                print("Вы хотите уменьшить цену? [y/n]")
                answer = input()
                if answer == "y":
                    self.__price = price


class Category:
    """Класс содержащий в себе одну категорию и её продукты, а также свойства: имя, описание, список продуктов.
    Дополнительно содержит подсчёт всех категорий и всех продуктов в них."""

    category_count = 0  # Счётчик категорий
    product_count = 0  # Счётчик продуктов

    name: str  # Название класса
    description: str  # Описание класса

    def __init__(self, name: str, description: str, products: list[Any]):
        """Функция обеспечивающая инициализацию и общий подсчёт"""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Функция строкового представления класса, также выводящее общего количества товаров в категории"""

        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product: Any) -> None:
        """Модуль добавляющий новый продукт в категорию"""

        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер списка продуктов в виде строк"""

        answer = ""
        for product in self.__products:
            answer += str(product)
        return answer
