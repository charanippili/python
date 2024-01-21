import threading
import time


def time(sec):
    print(f"this will printed after {sec} seconds")
    time.sleep(sec)
    return sec

#def main():
    #time1 = time.perf_counter()
t1 = threading.Thread(target=time, args=[5])
t2 = threading.Thread(target=time, args=[3])
t3 = threading.Thread(target=time, args=[1])


t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()

    #time2 = time.perf_counter()
    #print(time2-time1)

#print(main())
print("done")
