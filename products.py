class Product:
    """
        Represents an item available in the store's inventory.

        Attributes:
            name (str): The name of the product.
            price (float): The cost of a single unit of the product.
            quantity (int): The current stock level.
            active (bool): Whether the product is currently available for sale.
        """

    def __init__(self, name, price, quantity):
        """
                Initializes a new Product instance.

                Args:
                    name (str): The name of the product.
                    price (float): The price of the product.
                    quantity (int): Initial stock quantity.
                """
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except Exception as e:
            print(e)


    def get_quantity(self):
        """Returns the current quantity of the product."""
        return self.quantity


    def get_price(self):
        """Returns the price of the product."""
        return self.price


    def get_name(self):
        return self.name


    def set_quantity(self, quantity):
        """
                Reduces the stock quantity by the specified amount.

                Args:
                    quantity (int): The amount to subtract from the current stock.
                """
        self.quantity -= quantity


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        if self.is_active():
            print(f"{self.get_name()}, Price: {self.get_price()}, Quantity: {self.quantity}")
        else:
            print("")

    def buy(self, quantity):
        """
                Processes a purchase of the product.

                Checks if sufficient stock exists, updates the quantity, and
                deactivates the product if stock reaches zero.

                Args:
                    quantity (int): The number of units to buy.

                Returns:
                    float: The total cost of the purchase, or 0 if stock is insufficient.
                """
        if quantity > self.get_quantity():
            # print("\nNot enough quantity of this product\n")
            return 0
        total_purchases = quantity * self.price
        self.set_quantity(quantity)
        if self.get_quantity() == 0:
            print(f"Deactivated")
            self.deactivate()
        return total_purchases


# bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
# mac = Product("MacBook Air M2", price=1450, quantity=100)
#
# print(bose.buy(50))
# print(mac.buy(100))
# print(mac.is_active())
#
# bose.show()
# mac.show()
#
# bose.set_quantity(1000)
# bose.show()