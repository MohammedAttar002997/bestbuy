import products
import store


MENU = {1: ".List all products in store",
        2: ".Show total amount in store",
        3: ".Make an order",
        4: ".Quit"}




def start(store_data):
    temp_store_list = []
    temp_product_list = store_data.products
    # Looping over the menu to show it for the user
    for num, value in MENU.items():
        print(str(num) + str(value))
    print()
    # Checking user choice
    while True:
        choice = int(input("\nEnter choice (1 - 4): ").strip())
        if choice not in range(10) or choice == "":
            print("Invalid choice. Please enter a valid choice." )
            choice = int(input("Enter choice (1 - 4): ").strip())
        match choice:
            case 1:
                for product in temp_product_list:
                    product.show()
            case 2:
                print(f"Total of {store_data.get_total_quantity()} items in store.")
            case 3:
                print("------")
                index = 0
                for product in temp_product_list:
                    product.show()
                print("------")
                print("When you want to finish order, enter empty text")
                while True:
                    product_num = input("Enter product number: ")
                    product_quantity = input("Enter quantity: ")
                    if product_num.strip() == "" or product_quantity.strip() == "":
                        break
                    if int(product_num.strip()) not in range(1,4):
                        print("Invalid product number. Please enter a valid product number.")
                        break
                    if not temp_product_list[int(product_num)-1].is_active():
                        store_data.remove_product(temp_product_list[int(product_num)-1])
                        temp_product_list = store_data.products
                    temp_store_list.append((temp_product_list[int(product_num)-1], int(product_quantity)))
                # print(temp_store_list)
                order_total = store_data.order(temp_store_list)
                if order_total == 0:
                    print("\nError while making order! Quantity larger than what exists or invalid product number.")
                else:
                    print(f"Order made! Total payment: ${order_total}")
                    temp_store_list = []

            case 4:
                quit("Exiting the program. Goodbye!")


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