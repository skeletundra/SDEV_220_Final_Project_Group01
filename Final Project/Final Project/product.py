class Product:

    def __init__(self, id, name, quantity, price):
        self._id = id
        self._name = name
        self._quantity = quantity
        self._price = price
           
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

    # @property #setter
    # def update_quantity(self, quantity):
    #     self._quantity = quantity