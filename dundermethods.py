class charan:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i=i+1
        return i

    def __str__(self):
        return "print line1"

    def __repr__(self):
        return "print line2"

    def __call__(self):
        print("call this line")



c = charan("cherry")
print(len(c))
print(c)
print(str(c))
print(repr(c))
c()
