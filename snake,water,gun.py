import random

def check(comp,user):
    if (comp==user):
        return 0
    if (comp==0 and user==1):
        return -1
    if (comp==1 and user==2):
        return -1
    if (comp==2 and user==0):
        return -1

    return 1

print("WELCOME TO SNAKE WATER GUN GAME")
print("Enter your choice\n 0 for snake\n 1 for water\n 2 for gun")
user = int(input("YOU:"))
comp = random.randint(0,2)

score = check(comp,user)

print("COMPUTER",comp)

if(score ==0):
    print("It's a draw")

if(score == 1):
    print("You won")

else:
    print("You lose")


      
