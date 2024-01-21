questions = [
    ["What is the name of Thor’s hammer?", "Vanir", "Mjolnir", "Aesir", "Norn", 2],
    ["What is Captain America’s shield made of?", "Adamantium", "Vibranium", "Promethium", "Carbonadium", 2],
    ["Before becoming Vision, what is the name of Iron Man’s A.I. butler?", "H.O.M.E.R.", "J.A.R.V.I.S.", "A.L.F.R.E.D.", "M.A.R.V.I.N.", 2],
    ["What is the real name of the Black Panther?", "T’Challa", "M’Baku", "N’Jadaka", "N’Jobu", 1],
    ["Who was the last holder of the Space Stone before Thanos claims it for his Infinity Gauntlet?", "Thor", "Loki", "The Collector", "Tony Stark", 2],
    ["Who does the Mad Titan sacrifice to acquire the Soul Stone?", "Nebula", "Ebony Maw", "Cull Obsidian", "Gamora", 4],
    ["Who is Black Panther’s sister?", "Shuri", "Nakia", "Ramonda", "Okoye", 1],
    ["What is the name of the blue glowing square that Loki uses as a weapon?", "The Infinity Gem", "The Soulstone", "The Forever Cube", "The Tesseract", 4],
    ["What is the name of Thor’s hammer?", "Vanir", "Mjolnir", "Aesir", "Norn", 2],
    ["What is Captain America’s shield made of?", "Adamantium", "Vibranium", "Promethium", "Carbonadium", 2],
    ["What is the real name of the Black Panther?", "T’Challa", "M’Baku", "N’Jadaka", "N’Jobu", 1],
    ["Who was the last holder of the Space Stone before Thanos claims it for his Infinity Gauntlet?", "Thor", "Loki", "The Collector", "Tony Stark", 2]
]

levels=[1000, 2000, 3000, 4000, 5000, 10000, 15000, 20000, 25000, 50000, 75000, 100000]
money=0
for i in range(len(questions)):
    question=questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")
    print(f"{i+1}. {question[0]}")
    print(f"1. {question[1]}                 2. {question[2]}")
    print(f"3. {question[3]}                 4. {question[4]}")
    answer = int(input("enter any one option(1-4) or 0 to quit:"))
    if(answer==0):
        money = levels[i-1]
        break
    elif(answer==question[-1]):
        print(f"correct answer, you won Rs. {levels[i]}")
        if(i==2):
            money=3000
        elif(i==5):
            money=10000
        elif(i==8):
            money=25000
        elif(i==11):
            money=100000
    else:
        print("wrong answer")
        break

print(f"your take home money is {money}")

