class Details:
    name = "Charan"
    age = 21
    number = 8919550268
    def info(self):
        print(f"{self.name} age is {self.age} and phone number:{self.number}")

a = Details()
b = Details()
c = Details()

b.name = "Tirupathi rao"
b.age = 55
b.number = 8367234747

c.name = "Srilatha"
c.age = 50
c.number = 9000234747

a.info()
b.info()
c.info()
