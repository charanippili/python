square = lambda x: x*x
cube = lambda x: x*x*x
avg = lambda x,y,z: (x+y+z)/3

def func(fx, value):
    return 2 + fx(value)

multi = lambda x, y:  f"{x} * {y} = {x*y}"
print(square(2))
print(cube(3))
print(avg(2,3,4))
print(func(square, 4))
print(multi(2,3))

