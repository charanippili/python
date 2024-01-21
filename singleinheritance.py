class animal:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("I am barking")

class dog(animal):
    def __init__(self,name,colour):
        animal.__init__(self,name,breed = "lab")
        self.colour = colour

    def make_sound(self):
        print("bow bow!!!")

d = dog("puppy", "black")
d.make_sound()

a = animal("puppy", "lab")
a.make_sound()

