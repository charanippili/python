from functools import reduce


cube = lambda x: x*x*x
l =[1,2,3,4,5]
cubes = list(map(cube, l))
print(cubes)

big = lambda x: x>2
bigger = list(filter(big, l))
print(bigger)

sum = reduce(lambda x,y: x+y, l)
print(sum)
