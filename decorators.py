def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning sir")
        fx(*args, *kwargs)
        print("Thank you")
    return mfx

@greet
def text():
    print("You are welcome")

text()
