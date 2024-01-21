from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fx(n):
    time.sleep(3)
    return n*10

print(fx(10))
print("done for 10")
print(fx(5))
print("done for 5")
print(fx(8))
print("done for 8")
#already the data is stored for above 3 values


print(fx(10))
print("done for 10")
print(fx(5))
print("done for 5")



print(fx(9))
print("done for 19")


print(fx(8))
print("done for 8")


#Function caching is a technique for improving the performance
#of a program by storing the results of a function call so that
#you can reuse the results instead of recomputing them every time
#the function is called. This can be particularly useful when a
#function is computationally expensive, or when the inputs to the
#function are unlikely to change frequently.




#In Python, function caching can be achieved using the functools.lru_cache
#decorator. The functools.lru_cache decorator is used to cache the results
#of a function so that you can reuse the results instead of recomputing
#them every time the function is called.



#As you can see, the functools.lru_cache decorator is used to cache
#the results of the fib function. The maxsize parameter is used to
#specify the maximum number of results to cache. If maxsize is set
#to None, the cache will have an unlimited size.





