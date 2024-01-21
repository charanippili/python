list=["charan", "ippili", "laksh"]
print(list)
print(type(list))

marks=[1,3,5,7,9]
print(marks[3])
print(marks[4])
print(marks[0:6])
print(marks[-1])

#list[start: end: jumpindex]

numbers=[1,2,3,4,5,6,7,8,9]
print(numbers[1:9:3])

color=["red", "yellow", "green", "black"]
if "red" in color:
    print("yes")
else:
    print("no")

if "aw" in "yellow":
    print("true")
else:
    print("false")

square=[i*i for i in range(5)]

odd=[i for i in range(10) if i%2!=0]

even=[i for i in range(10) if i%2==0]

print(square)
print(odd)
print(even)
