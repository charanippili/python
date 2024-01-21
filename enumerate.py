#list
marks=[50, 47, 90, 100, 30]

for index, mark in enumerate(marks):
    print(mark)
    print("1st rank") if index==3 else print("2nd rank") if index==2 else ""



#tuple
colors=("red", "blue", "yellow", "black", "white")

for index, color in enumerate(colors, start=1):
    print(index, color)



#string
name="charan"

for index, alpha in enumerate(name):
    print(f"{index+1}: {alpha}")
    
    
