arr=list(map(int,input("enter the scores: ").split()))
print(arr)

arr1=list(set(arr))
print(arr1)
arr1.reverse()
print(arr1)
print("highest score among all is: ",arr1[0])
