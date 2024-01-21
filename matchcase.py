a=int(input("enter the value of a: "))
match a:
    case 0:
        print("given number is zero")
    case 100:
        print("given number is hundred")
    # case _ if a!=100:
        # print("given number is not equal to 100")
    # case _ if a!=200:
       # print(a," is not equal to 200")
    case _:
        print(a)
