from typing import ItemsView


class Item:
    def __init__(self, name="Unknown", price=0, quantity=0):
        # print("I am created here")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self, price, quantity):
        return price*quantity


item1 = Item("Phone", 500, 5)
print(item1.name)
# print(item1.calculate_total_price())
# print(item1.calculate_total_price(item1.price, item1.quantity))
item2 = Item("Laptop")
print(item1.price)
print(item1.quantity)
print(item2.name)
print(item2.price)
print(item2.quantity)
# print(type(item2))
