a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

#One important thing to note is that, in Python, strings
#and integers are immutable, which means that once they are
#created, their value cannot be changed. This means that,
#for strings and integers, is and == will always return the same result



#For mutable objects such as lists and dictionaries,
#is and == can behave differently. In general, you should
#use == when you want to compare the values of two objects,
#and use is when you want to check if two objects are the
#same object in memory.

c = 5
d = 5

print(c ==d)
print(c is d)


