def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

a=average(1,2,3,4,5,6,8,9,10)
print(a)

def name(**name):
    print("hello",name["fname"], name["mname"], name["lname"])

name(fname="ippili",mname="charan",lname="naidu")


def details(*name):
    print("hello",name[0], name[1], name[2])


details("john", "peter", "son")

