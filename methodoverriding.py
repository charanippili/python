class shape:
    def __init__(self,l,b):
        self.length = l
        self.breadth = b

    def area(self):
        return self.length*self.breadth

class circle(shape):
    def __init__(self,r):
        self.radius = r
        super().__init__(r,r)

    def area(self):
        return 3.14* super().area()

c = circle(4)
print(c.area())

rectangle = shape(2,3)
print(rectangle.area())
