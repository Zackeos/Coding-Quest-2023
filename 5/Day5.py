with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/5/Day5.txt") as f:
    data = f.readlines()


map = [[" " for z in range(50)] for x in range(10)]

for rectangle in data:
    rectangle = rectangle.split()
    sx = int(rectangle[0])
    sy = int(rectangle[1])
    for y in range(sy, sy+int(rectangle[3])):
        for x in range(sx, sx+int(rectangle[2])):
            if map[y][x] == " ":
                map[y][x] = "#"
            elif map[y][x] == "#":
                map[y][x] = " "
for row in map:
    print("".join(row))

