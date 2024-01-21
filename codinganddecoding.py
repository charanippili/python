str = input("Enter Message:")
words = str.split()
coding = input("1 for coding or 0 for decoding:")
coding = True if(coding=="1") else False
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1 = "123"
            r2 = "456"
            strnew = r1 + word[1:] + word[0] + r2
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
        if(len(word)>=3):
            strnew = word[3:-3]
            strnew = strnew[-1] + strnew[:-1]
            nwords.append(strnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
    
