class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size  # Will trigger validation in the setter

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            self._size = None  # Or set a default value
        else:
            self._size = value
            self.condition = "New"

    def cobble(self):
        if self._size is None:
            print("Cannot cobble a shoe with invalid size.")
        else:
            print("Your shoe is as good as new!")
            self.condition = "New"
