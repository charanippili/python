class Person:
    def __init__(self,value):
        self._value = value

    def number(self):
        print(f"value  is {self._value}")

    @property
    def five_number(self):
        return self._value

    @five_number.setter
    def five_number(self, new_value):
        self._value = new_value*5


a = Person(10)
a.number()
a.five_number=10
print(a.five_number)
