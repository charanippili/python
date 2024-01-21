def fun():
    try:
        n=[1,2,3,4]
        i=int(input("enter index value:"))
        return n[i]
    except:
        print("error occured")
        return 0
    finally:
        print("this lines must be executed")

x = fun()
print(x)
