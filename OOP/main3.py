

class Item:
    def __init__(self, name: str, price: float, quantity: float):
        # print("I am created here")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity


item1 = Item(5, 500, 5)
# print(item1.name)
total_price = item1.calculate_total_price()
print(item1.name)
print(total_price)
# print(item1.calculate_total_price())
# print(item1.calculate_total_price(item1.price, item1.quantity))
item2 = Item("Laptop")
item2.has_numpad = False
# print(type(item2))
