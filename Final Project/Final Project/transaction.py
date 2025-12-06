class Transaction:

    def __init__(self, id, customer, items, total_cost, date):
        self._id = id
        self._customer = customer
        self._items = items  # list of (Product, quantity)
        self._total_cost = total_cost
        self._date = date
       
    @property #getter
    def id(self):
        return self._id

    @property #getter
    def customer(self):
        return self._customer

    @property #getter
    def items(self):
        return self._items

    @property #getter
    def total_cost(self):
        return self._total_cost

    @property #getter
    def date(self):
        return self._date

    # calculate total for this transaction
    def calculate_total(self):
        total = 0
        for product, qty in self._items:
            total += product.product_price * qty
        self._total_cost = total
        return total
