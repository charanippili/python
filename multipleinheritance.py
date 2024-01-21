class person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}")

class people:
    def __init__(self, age):
        self.age = age

    def show(self):
        print(f"age is {self.age}")

class intro(person, people):
    def __init__(self,name,age):
        person.__init__(self, name)
        people.__init__(self, age)


c = intro("charan", 22)
print(c.name)
print(c.age)

c.show()
print(intro.mro())
