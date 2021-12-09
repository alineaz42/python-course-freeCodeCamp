

class Item:
    pay_rate = 0.8  # class attribute

    def __init__(self, name: str, price: float = 0, quantity=0):
        # run validation to the received agruments
        assert price >= 0, f"Price {price} is not greater than zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than zero or equal to zero!"
        # assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price*self.quantity


item1 = Item("Phone", 500, 5)
item2 = Item("Laptop")
print((Item.pay_rate))
print((item1.pay_rate))
print((item2.pay_rate))
