a = True
print(a)
print(a:=False)

l = [1,2,3,4,5]
while (n:=len(l))>0:
    print(l.pop())


names = ["charan", "akshith", "manoj", "shivtej"]
if (name:=input("enter your name:")) in names:
    print(f"hello {name}")
else:
    print("name not found")


foods = []
while(food:=input("enter your favourite food:"))!= "quit":
    foods.append(food)

print(foods)
