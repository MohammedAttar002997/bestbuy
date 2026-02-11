import products


class Store:
    def __init__(self,available_products):
        print(available_products)
        self.products = available_products
        print(self.products)


    def add_product(self, product) :
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        return len(self.products)


    def get_all_products(self) -> list[products.Product]:
        active_products = []
        for product_in_store in self.products:
            if product_in_store.active:
                active_products.append(product_in_store)
        return active_products


    def order(self,shopping_list) -> float:
        print(shopping_list)
        total_price = 0
        for product,quantity in shopping_list:
            total_price = total_price + (product.price * quantity)
        return total_price

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
my_products = best_buy.get_all_products()
print(my_products)
print(best_buy.get_total_quantity())
print(best_buy.order([(my_products[0], 1), (my_products[1], 3)]))