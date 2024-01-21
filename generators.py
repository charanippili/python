def my_generator():
    for i in range(10):
        yield i


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#another method will print all the values without permission
#for j in gen:
#  print(j)



#Benefits of Generators


#Generators offer several benefits over other types of sequences,
#such as lists, tuples, and sets. One of the main benefits of generators
#is that they allow you to generate the values on-the-fly, rather than
#having to create and store the entire sequence in memory. This makes
#generators a powerful tool for working with large or complex data sets,
#as you can generate the values as you need them, rather than having
#to store them all in memory at once.

#Another benefit of generators is that they are lazy, which means that
#the values are generated only when they are requested. This allows you
#to generate the values in a more efficient and memory-friendly manner,
#as you don't have to generate all the values up front.

