percentage = {569:70, 572:69, 575:71}
percentage1 = {591:75, 597:70, 598:65, 599:80}

percentage.update(percentage1)

print(percentage)

percentage.clear()
#del percetage
print(percentage)

del percentage1[597]
print(percentage1)

percentage1.pop(599)
print(percentage1)

percentage1.popitem()
print(percentage1)

percentage1.update({599:76})
print(percentage1)
