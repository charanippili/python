def average(n):
    '''given some numbers and their sum is divided by no. of given numbers'''
    average=sum(n)/len(n)
    return average
n=list(map(int,input().split()))
print(average(n))
print(average.__doc__)


        
