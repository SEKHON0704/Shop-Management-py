from menu import display_menu
from product import Product
from customer import Customer
from sales import Sale
from db import load_data, save_data

def main():
    load_data()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == "1":
            Product.add_product()
        elif choice == "2":
            Customer.add_customer()
        elif choice == "3":
            Sale.create_sale()
        elif choice == "4":
            save_data()
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
