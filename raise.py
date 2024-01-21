n=int(input("enter a value between 2 and 10:"))

if(n<2 or n>10):
    raise ValueError("inavlid input given")
