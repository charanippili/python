s1 = {1,2,3,4,5}
s2 = {2,5,6,7,8}

s3 = s1.union(s2)
print(s3)
s1.update(s2)      #another method
print(s1)

s4=s1.intersection(s2)
print(s4)
s1.intersection_update(s2)   #another method
print(s1)

c1={"hyderabad", "delhi", "mumbai", "banglore"}
c2={"hyderabad", "kolkata", "jaipur","delhi", "banglore"}

c3=c1.symmetric_difference(c2)
print(c3)
c1.symmetric_difference_update(c2)  #another method
print(c1)


c4=c1.difference(c2)
print(c4)
c1.difference_update(c2)   #another method
print(c1)

c5 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
c6 = {"Delhi", "Madrid"}

print(c5.isdisjoint(c6))
print(c5.issuperset(c6))
print(c6.issubset(c5))
c6.add("hyderabad")
print(c6)
#c5.remove("hyderabad")  returns error 
c5.discard("hyderabad")  #does not return error
print(c5)

c5.pop()
print(c5)

#del c6 returns error
c6.clear()   #does not returns error
print(c6)

