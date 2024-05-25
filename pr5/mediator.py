class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price

    def view_items(self):
        for item in self.items:
            print(item.name)

    def get_total_price(self):
        return self.total_price
class ShoppingCartMediator:
    def __init__(self):
        self.cart = Cart()

    def add_to_cart(self, item):
        self.cart.add_item(item)

    def remove_from_cart(self, item):
        self.cart.remove_item(item)

    def view_cart(self):
        self.cart.view_items()

    def calculate_total_price(self):
        return self.cart.get_total_price()
def main():
    mediator = ShoppingCartMediator()

    item1 = Item("Товар 1", 10)
    item2 = Item("Товар 2", 20)

    mediator.add_to_cart(item1)
    mediator.add_to_cart(item2)

    mediator.view_cart()

    print("Общая стоимость:", mediator.calculate_total_price())

    mediator.remove_from_cart(item1)

    mediator.view_cart()

    print("Общая стоимость после удаления:", media-tor.calculate_total_price())

if __name__ == "__main__":
    main()
