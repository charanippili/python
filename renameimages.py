import os

# os.rename("C:/Users/chara/Desktop/cluttered/fnndnd.txt", "C:/Users/chara/Desktop/cluttered/charan.txt")

files = os.listdir("C:/Users/chara/Desktop/cluttered")

i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"C:/Users/chara/Desktop/cluttered/{file}", f"C:/Users/chara/Desktop/cluttered/{i}.png")
        i = i+1