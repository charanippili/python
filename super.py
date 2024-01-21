class parentclass:
    def parent_method(self):
        print("this is parent class method")

class childclass(parentclass):
    def parent_method(self):
        print("this is child class")
        
    def child_method(self):
        print("this is child class method")
        super().parent_method()   #calls the parent class method

child = childclass()
child.child_method()


class parent:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class children(parent):
    def __init__(self,name,age,id):
        super().__init__(name, age)     #calls parent class method
        self.id = id


c = parent("charan", 21)
c1 = children("cherry", 22, 569)


print(c1.name)
print(c1.age)
print(c1.id)
        
