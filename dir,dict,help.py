class person:
    marks = [1,2,3,4]
    def __init__(self,name,id):
        self.name = name
        self.id = id

p = person("charan", 569)
print(p.__dict__)

print(dir(p.marks))

print(help(person))
