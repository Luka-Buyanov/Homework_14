class Product:
    name: str
    description: str
    price: str
    quantity: int


class Category:
    name: str
    description: str
    products: list[object]
