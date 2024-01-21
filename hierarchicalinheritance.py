class animal:
    def __init__(self,name):
        self.name= name

    def show(self):
        print(f"name = {self.name}")


class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name)
        self.breed = breed

    def show(self):
        animal.show(self)
        print("species = dog")
        print(f"breed = {self.breed}")


class cat(animal):
    def __init__(self,name,color):
        animal.__init__(self,name)
        self.color = color

    def show(self):
        animal.show(self)
        print("species = cat")
        print(f"color = {self.color}")


c = cat("luna", "black")
c.show()
d = dog("bolt", "lab")
d.show()
        
