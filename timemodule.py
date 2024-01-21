import time

def usingwhile():
    i = 0
    while i<10:
        i = i+1
        print(i)

def usingfor():
    for i in range(1, 10):
        print(i)

init=time.time()
usingwhile()
t = time.time() - init
init = time.time()
usingfor()
t1 = time.time() - init
print(t)
print(t1)

#t = time.localtime()
#time = time.strftime("%H:%M:%S",t)
#print(time)

print("start:",time.time())
time.sleep(4)  #take 4sec to print end statement
print("end:",time.time())
