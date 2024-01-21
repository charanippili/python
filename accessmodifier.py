class person:
    def __init__(self,id,name,age):
        self.id = id         #public access modifier
        self._name = name    #protected access modifier
        self.__age = age      #private access modifier

a = person(569,"charan",21)
print(a.id)
print(a._name)
#print(a.__age)      cannot be accessible directly
print(a._person__age)    #can be accessible indirectly
