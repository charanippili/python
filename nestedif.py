a=int(input("enter a number: "))
if(a<0):
    print("your number is negative")
elif(a>0):
    if(a<=30):
        print("your number is between 0 and 30")
    elif(a>30 and a<=70):
        print("your number is between 30 and 70")
    else:
        print("your number is greater than 70")
else:
    print("given number is zero")
    
