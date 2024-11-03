from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseCategory(ABC):
    """Абстрактный класс. Определяет для классов метод подсчёта количества продуктов"""

    @abstractmethod
    def quantity_counter(self, *args: Any, **kwargs: Any) -> str:
        """Метод реализующий подсчёт товаров в категории или продукте"""

        pass


class BaseProduct(ABC):
    """Абстрактный класс. Определяет для классов метод new_product, необходим для создания продукта из словаря"""

    @abstractmethod
    def new_product(self, *args: Any, **kwargs: Any) -> Any:
        """Метод для работы с ценой, как вариант геттер и сеттер"""

        pass


class MixinPrinter:
    """Миксин для печати информации о продукте"""

    name: str  # Название продукта
    description: str  # Описание продукта
    price: float  # Цена продукта
    quantity: int  # Количество продукта

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

        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен!")
        else:
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


class Category(BaseCategory):
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

        try:
            quantity = product.quantity
            1 / quantity
        except ZeroDivisionError:
            raise ZeroQuantityAddError()
        except AttributeError:
            raise TypeError("Нельзя добавлять в категории не продукты!")
        else:
            print("Добавлен новый товар в категорию!")
            if isinstance(product, Product):
                self.__products.append(product)
                Category.product_count += 1
            else:
                raise TypeError("Нельзя добавлять в категории не продукты!")
        finally:
            print("Обработка добавления товара завершена.")

    @property
    def products(self) -> str:
        """Геттер списка продуктов в виде строк"""

        answer = ""
        for product in self.__products:
            answer += str(product)
        return answer

    def quantity_counter(self) -> str:
        """Метод выводящий количество товара."""

        quantity_summ = 0
        for products in self.__products:
            quantity_summ += products.quantity
        return f"В категории {quantity_summ}шт. товара"

    def middle_price(self) -> Any:
        """Метод подсчёта средней цены всех товаров в категории"""

        price_summ = 0
        str_quantity = self.quantity_counter()
        index = str_quantity.find("шт.")
        quantity = int(str_quantity[12:index])
        try:
            for products in self.__products:
                price_summ += products.price
            middle_price = price_summ / quantity
        except ZeroDivisionError:
            return 0
        else:
            return f"Средняя цена товаров в категории: {middle_price}руб."


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


class Order(BaseCategory):
    """Класс содержащий информацию о заказе."""

    product: Product  # Заказанный продукт
    quantity: int  # Количество заказанного продукта
    summ: float  # Сумма заказа

    def __init__(self, product: Product, buy_quantity: int):
        """Метод обеспечивающий инициализацию"""

        self.product = product
        try:
            quantity = product.quantity
            1 / quantity
        except ZeroDivisionError:
            raise ZeroQuantityAddError()
        except AttributeError:
            raise TypeError("Нельзя добавлять в заказ не продукты!")
        else:
            print("Товар добавлен в заказ!")
            self.quantity = buy_quantity
            self.summ = buy_quantity * self.product.price
            self.product.quantity -= buy_quantity
            print("Обработка добавления товара завершена.")

    def __str__(self) -> str:
        """Метод выводящий строковое представление заказа"""

        return f"Заказано: {self.product.name} - {self.quantity}шт. на сумму {self.summ}руб."

    def quantity_counter(self) -> str:
        """Метод выводящий количество товара."""

        return f"Заказано {self.quantity}шт. товара."


class ZeroQuantityAddError(Exception):
    """Класс выводящий ошибку при добавлении товара с нулевым количеством"""

    def __init__(self) -> None:
        """Метод обеспечивающий инициализацию и проверку условия"""

        self.end_message = "Нельзя добавлять товары с нулевым количеством!"

    def __str__(self) -> Any:
        """Метод выводящий строковое представление результата добавления"""

        return self.end_message
