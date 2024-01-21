class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0], int(string.split("-")[1]))

a = person("charan", 18)
print(a.name)
print(a.age)

string = "vishnu-21"
b = person.fromstr(string)
print(b.name)
print(b.age)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def tostr(cls, string):
        name, age = string.split(",")
        return cls(name, int(age))

c = Person.tostr("yogendra, 21")
print(c.name)
print(c.age)
