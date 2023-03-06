with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/1/Day1.txt") as f:
    data = f.readlines()


categories = {}
for item in data:
    stuff = item.split()
    category = stuff[2]
    amount = int(stuff[1])
    if category in categories:
        categories[category] += amount
    else:
        categories[category] = amount

a = 1
for key in categories:
    a = a*(categories[key]%100)
print(a)