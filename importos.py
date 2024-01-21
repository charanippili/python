import os

if(not os.path.exists("data")):
    os.mkdir("data")

for i in range(0, 101):
    os.rename(f"data/day {i+1}", f"data/Tutorial {i+1}")

