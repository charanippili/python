class Person:

    def __init__(self,name,occ):       #parameterized constructor
   #def __init__(self)                 #default constructor
        self.name=name
        self.occ=occ

    def info(self):
        print(f"{self.name} is a {self.occ}")

a=Person("charan", "develepor")
a.info()


      
