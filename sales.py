from db import sales_data, products_data, customers_data
from utils import calculate_total_price

class Sale:
    @staticmethod
    def create_sale():
        print("Available Products: ")
        for i, product in enumerate(products_data):
            print(f"{i + 1}. {product['name']} - ${product['price']}")
        
        product_index = int(input("Select product by number: ")) - 1
        product = products_data[product_index]
        
        print("Available Customers: ")
        for i, customer in enumerate(customers_data):
            print(f"{i + 1}. {customer['name']}")
        
        customer_index = int(input("Select customer by number: ")) - 1
        customer = customers_data[customer_index]
        
        quantity = int(input(f"Enter quantity of {product['name']}: "))
        
        total_price = calculate_total_price(product['price'], quantity)
        sale = {"product": product['name'], "customer": customer['name'], "quantity": quantity, "total": total_price}
        sales_data.append(sale)
        
        print(f"Sale recorded for {customer['name']} of {quantity} {product['name']}(s) totaling ${total_price}.")
