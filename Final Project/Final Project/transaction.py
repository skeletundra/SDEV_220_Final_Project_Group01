class Transaction:

    def __init__(self, id, customer, items, total_cost, date):
        self._id = id
        self._customer = customer
        self._items = items
        self._total_cost = total_cost
        self._date = date
   
    @property #getter
    def id(self):
        return self._id

    def calculate_total():
        print("total price: $")