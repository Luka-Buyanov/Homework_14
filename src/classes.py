class Product:
    name: str
    description: str
    price: str
    quantity: int

    def __init__ (self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    name: str
    description: str
    products: list[object]

    category_count = 0
    products_count = 0

    def __init__(self, name, description, products, category_count, products_count):
        self.name = name
        self.description = description
        self.products = products
        category_count += 1
        products_count += len(products)