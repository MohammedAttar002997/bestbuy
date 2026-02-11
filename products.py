class Product:


    def __init__(self, name, price, quantity):
        try:
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True
        except Exception as e:
            print(e)


    def get_quantity(self):
        return self.quantity


    def get_price(self):
        return self.price


    def get_name(self):
        return self.name


    def set_quantity(self, quantity):
        if quantity > self.get_quantity():
            print("\nNot enough quantity of this product\n")
        else:
            self.quantity -= quantity


    def is_active(self):
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        if self.active:
            print(f"{self.get_name()}, Price: {self.get_price()}, Quantity: {self.quantity}")
        else:
            print("This product has been sold out")

    def buy(self, quantity):
        total_purchases = quantity * self.price
        self.set_quantity(quantity)
        if self.get_quantity() == 0:
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