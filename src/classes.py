from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseProduct(ABC):
    """Абстрактный класс. Определяет для классов метод new_product, необходим для создания нового продукта из словаря"""

    @abstractmethod
    def new_product(self, new_product: dict, list_products: Optional[Any] = None) -> Any:
        """Метод для работы с ценой, как вариант геттер и сеттер"""

        pass


class MixinPrinter:
    """Миксин для печати информации о продукте"""

    name: str # Название продукта
    description: str # Описание продукта
    price: float # Цена продукта
    quantity: int # Количество продукта

    def __init__(self, *args: Any, **kwargs: Any):
        """Метод обеспечивающий печать информации"""

        print(repr(self))

    def __repr__(self) -> str:
        """Возврат информации о продукте в формате строки"""

        return f"{self.__class__.__name__}('{self.name}', '{self.description}', '{self.price}', '{self.quantity}') "


class Product(BaseProduct, MixinPrinter):
    """Класс содержащий в себе один продукт и его свойства: имя, описание, цену и количество"""

    name: str  # Название продукта
    description: str  # Описание продукта
    quantity: int  # Количество продукта

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Метод обеспечивающий инициализацию"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

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
        """Метод строкового представления класса"""

        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        """Метод реализующий сложение двух продуктов"""

        if type(self) == type(other):
            price_self = self.price
            quantity_self = self.quantity
            price_other = other.price
            quantity_other = other.quantity
            return price_self * quantity_self + price_other * quantity_other
        else:
            raise TypeError("Ошибка: классы продуктов не одинаковы! (Не складывайте траву со смартфонами!!!)")

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
        """Метод обеспечивающий инициализацию и общий подсчёт"""

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        """Метод строкового представления класса, также выводящее общего количества товаров в категории"""

        quantity = 0
        for product in self.__products:
            quantity += product.quantity
        return f"{self.name}, количество продуктов: {quantity} шт."

    def add_product(self, product: Any) -> None:
        """Метод добавляющий новый продукт в категорию"""

        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Нельзя добавлять в категории не продукты!")

    @property
    def products(self) -> str:
        """Геттер списка продуктов в виде строк"""

        answer = ""
        for product in self.__products:
            answer += str(product)
        return answer


class Iterator:
    """Класс позволяющий перебирать все товары данной категории"""

    category: Any  # Категория по которой необходимо провести итерацию
    _current_value: int  # Внутренняя переменная для проведения итерации

    def __init__(self, categories: Any):
        """Метод реализующий инициализацию"""

        self.category = categories

    def __iter__(self) -> Any:
        """Метод реализующий итерацию класса"""

        self._current_value = -1
        return self

    def __next__(self) -> Any:
        """Метод реализующий переход к следующей итерации"""

        answer = self.category.products.split("шт.")
        answer.pop()
        print(answer)
        self._current_value += 1
        if self._current_value <= len(answer) - 1:
            return answer[self._current_value]
        else:
            raise StopIteration

    def __len__(self) -> int:
        """Метод реализующий вывод длины атрибута categories"""

        categories = self.category
        return len(categories.products)


class Smartphone(Product):
    """Дочерний класс от Product, содержащий в себе информацию о смартфоне."""

    efficiency: float  # Эффективность смартфона
    model: str  # Модель смартфона
    memory: int  # Память смартфона в гигабайтах
    color: str  # Цвет смартфона

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """Метод обеспечивающий инициализацию"""

        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Дочерний класс от Product, содержащий в себе информацию о траве для газона."""

    country: str  # Страна-производитель
    germination_period: str  # Срок прорастания
    color: str  # Цвет травы

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        """Метод обеспечивающий инициализацию"""

        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
