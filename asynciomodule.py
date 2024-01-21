import time
import asyncio



async def fun1():
    time.sleep(2)
    return "hello"

async def fun2():
    time.sleep(2)
    return "async"

async def fun3():
    time.sleep(3)
    return "world"

async def main():
    a=await fun1()
    print(a)
    b=await fun2()
    print(b)
    c=await fun3()
    print(c)
    L = await asyncio.gather(
      fun1(),
      fun2(),
      fun3(),
      )
    print(L)

asyncio.run(main())

