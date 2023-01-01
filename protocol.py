from typing import Protocol


class Traveller(Protocol):
    @classmethod
    def flymessage(cls):
        ...


class Business:
    def flymessage(self):
        print("Flying business class")


class First:
    def flymessage(self):
        print("Flying first class")


class Economy:
    @classmethod
    def flymessage(self):
        print("Flying economy class")


class Item(Protocol):
    price: int
    units: int


class Product:
    def __init__(self, product_name: str, price: int, units: int):
        self.product_name = product_name
        self.price = price
        self.units = units


class Inventory:
    def __init__(self, inventory_name: str, price: int, units: int):
        self.inventory_name = inventory_name
        self.price = price
        self.units = units


def calculate_value(item: Item) -> int:
    return item.price * item.units


def fly_message(traveller: Traveller):
    traveller.flymessage()


product = Product("Banana", 2, 10)
product_value = calculate_value(product)
print(f"Sold {product.product_name} for value {product_value}")

inventory = Inventory("Banana", 100, 10)
inventory_value = calculate_value(inventory)
print(f"{product.product_name} in stock with a value of {inventory_value}")

business = Business()
fly_message(business)
first = First()
fly_message(first)
economy = Economy()
fly_message(economy)
