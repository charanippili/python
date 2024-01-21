class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species = "dog")
        self.breed = breed

    def show(self):
        animal.show(self)
        print(f"breed:{self.breed}")

class lab(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,breed = "lab")
        self.color = color

    def show(self):
        dog.show(self)
        print(f"color:{self.color}")

l = lab("bolt", "white")
l.show()
print(lab.mro())
        
