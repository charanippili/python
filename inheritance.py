class person:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print(f"{self.name} id number is {self.id}")

class age(person):
    def num(self):
        print("age is above 18")

        
a=person("charan", 569)
a.details()
b=age("sai", 599)
b.details()
b.num()
