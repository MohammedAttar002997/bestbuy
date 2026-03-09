import products
import sys
import store


MENU = {1: ".List all products in store",
        2: ".Show total amount in store",
        3: ".Make an order",
        4: ".Quit"}


def print_menu():
    for num, value in MENU.items():
        print(str(num) + str(value))
    print()


def start(store_data):
    """
    Main entry point for the Best Buy Store management system.

    This script handles the user interface, allowing users to view products,
    check stock levels, and place orders through an interactive menu.
    """
    # Looping over the menu to show it for the user

    # Checking user choice
    while True:
        print_menu()
        user_input = input("\nEnter choice (1 - 4): ").strip()
        try:
            choice = int(user_input)
            if choice not in range(1, 5):
                print("Error: Please select a number between 1 and 4.\n")
                continue
        except ValueError:
            print("Error: Invalid input. Please enter a number.")
            continue
        available_products = store_data.get_all_products()
        match choice:
            case 1:
                if not available_products:
                    print("No products available. The store is empty.")
                else:
                    for product in available_products:
                        product.show()
                print()
            case 2:
                print(f"Total of {store_data.get_total_quantity()} items in store.")
            case 3:
                print("------")
                for index, product in enumerate(available_products, 1):
                    print(f"{index}. ", end="")
                    product.show()
                print("------")
                print("When you want to finish order, enter empty text")
                temp_shopping_list = []
                while True:
                    product_num_input = input("Enter product number: ")
                    product_quantity_input = input("Enter quantity: ")
                    available_products = store_data.get_all_products()
                    if product_num_input.strip() == "" and product_quantity_input.strip() == "":
                        break
                    try:
                        product_num = int(product_num_input)
                        product_quantity = int(product_quantity_input)
                    except ValueError:
                        print("Error: Invalid input. Please enter numeric values for product number and quantity.")
                        continue
                    if product_num - 1 not in range(len(available_products)):
                        print("Invalid product number. Please enter a valid product number.")
                        continue
                    selected_product = available_products[product_num - 1]
                    temp_shopping_list.append((selected_product, int(product_quantity)))
                    print(f"Added {product_quantity} of {selected_product.get_name()} to your order.")
                # print(temp_store_list)
                if temp_shopping_list:
                    try:
                        order_total = store_data.order(temp_shopping_list)
                        print(f"Order made! Total payment: ${order_total}")
                    except Exception as e:
                        print(f"\nError while making order: {e}")
                else:
                    print("No items were added to the order.")

            case 4:
                sys.exit("Exiting the program. Goodbye!")

"""
    Initializes the inventory and launches the application.

    Sets up the default product list, creates the Store instance, 
    and passes it to the start function to begin user interaction.
    """
def main():
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)
    start(best_buy)

if __name__ == '__main__':
    main()