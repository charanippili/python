class vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,other):
        return vector(self.i+other.i, self.j+other.j, self.k+other.k)



v = vector(2,3,4)
print(v)
v1 = vector(5,6,7)
print(v1)

print(v + v1)
