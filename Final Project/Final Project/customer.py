class Customer:

    def __init__(self, id, name):
        self._name = name
        self._id = id
   
    @property #getter
    def name(self):
        return self._name

    @property #getter
    def id(self):
        return self._id