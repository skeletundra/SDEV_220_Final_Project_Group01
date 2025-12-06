class Product:

    def __init__(self, id, name, quantity, price):
        self._id = id
        self._name = name
        self._quantity = int(quantity)
        self._price = float(price)
           
    @property #getter
    def product_id(self):
        return self._id

    @property #getter
    def product_name(self):
        return self._name

    @property #getter
    def product_quantity(self):
        return self._quantity

    @property #getter
    def product_price(self):
        return self._price

    # setter to update quantity
    def update_quantity(self, quantity):
        self._quantity = int(quantity)
