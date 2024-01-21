details = {"name":"charan", "ID":"20E41A0569", "section":"B", "course":"CSE"}
print(details)
print(details.keys())
print(details.values())
print(details.items())
print(details["name"])
print(details.get("ID"))

for key in details.keys():
    print(f"The corresponding key {key} is {details[key]}")


for key, value in details.items():
    print(f"The corresponding key {key} is {value}")
