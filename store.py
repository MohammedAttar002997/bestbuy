import products


class Store:
    """
        Manages a collection of products and handles customer transactions.

        Attributes:
            products (list[products.Product]): A list of product objects currently
                held in the store's inventory.
        """
    def __init__(self,available_products):
        """
                Initializes the store with a starting list of products.

                Args:
                    available_products (list): A list of Product instances.
                """
        print(available_products)
        self.products = available_products
        print(self.products)


    def add_product(self, product):
        """Adds a single product instance to the store's inventory."""
        self.products.append(product)


    def remove_product(self, product):
        """Removes a specific product instance from the store's inventory."""
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        """
                Calculates the sum of quantities for all products in the store.

                Returns:
                    int: Total number of individual items in stock.
                """
        total_quantity = 0
        for one_product in self.products:
            total_quantity += one_product.quantity
        return total_quantity


    def get_all_products(self) -> list[products.Product]:
        """
                Retrieves all products that are currently marked as active.

                Returns:
                    list: A list of active Product objects.
                """
        active_products = []
        for product_in_store in self.products:
            if product_in_store.active:
                active_products.append(product_in_store)
        return active_products


    def order(self,shopping_list) -> float:
        """
                Processes a bulk order of multiple products.

                Iterates through a list of tuples, calling the buy method for each
                item to update stock and calculate costs.

                Args:
                    shopping_list (list[tuple]): A list of tuples where each tuple
                        contains (Product, quantity).

                Returns:
                    float: The total cost of all successfully purchased items.
                """
        total_price = 0
        for product,quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
