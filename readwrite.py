f = open('C:/Users/chara/Desktop/details.txt', 'r')

#lines=["i am good\n", "i am bad\n", "i am fine\n"]
#f.writelines(lines)
#f.close()

while True:
    text=f.readline()
    if not text:
        break
    print(text)

