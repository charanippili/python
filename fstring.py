bio="My name is {1} and I am from {0}"
name=input("enter your name:")
country=input("enter your country:")
print(bio.format(country,name))

print(f"hey my name is {name} and i am from {country}")
print("we use fstrings like this: hey my name is {{name}} and i am from {{country}}")
amount=5.4567535
print(f"GST is {amount:.2f} rupees only.")

print(type(f"{2*30}"))
