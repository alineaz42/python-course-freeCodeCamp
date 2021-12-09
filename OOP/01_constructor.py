

class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # run validation to the received agruments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero or equal to zero!"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity


# item1 = Item(5, 500, -5)
item1 = Item("Phone", 500, 5)
# print(item1.name)
total_price = item1.calculate_total_price()
print(item1.name)
print(total_price)
# print(item1.calculate_total_price())
# print(item1.calculate_total_price(item1.price, item1.quantity))
# item2 = Item("Laptop")
# item2.has_numpad = False
# print(type(item2))
