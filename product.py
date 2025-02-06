from db import products_data
from utils import validate_price

class Product:
    @staticmethod
    def add_product():
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        if validate_price(price):
            product = {"name": name, "price": price}
            products_data.append(product)
            print(f"Product {name} added successfully.")
        else:
            print("Invalid price!")

