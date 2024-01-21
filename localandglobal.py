x = 10    #global variable

def func():
    #y = 20   #local variable
    global z
    z = 30
    print(x)
    #print(y)
    print(z)

func()
print(x)
#print(y)
print(z)
