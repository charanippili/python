with open('sample.txt', 'a') as f:
    f.write("charan is a good boy")
    f.truncate(10)

with open('sample.txt', 'r') as f:
    f.seek(2)
    print(f.read())
    print(f.tell())
    

