with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/6/Day6.txt") as f:
    data = f.readlines()
asteroids = [[int(i) for i in y.split()] for y in data]

map = [[" " for x in range(100)] for y in range(100)]


def change(ast,coord, time):
    return (coord[0]+ast[2]*time,coord[1]+ast[3]*time)

for asteroid in asteroids:
    t = 0
    nextcoord = (asteroid[0], asteroid[1])
    for x in range(3660):
        nextcoord = change(asteroid, nextcoord, 1)
        if nextcoord[0] < 100 and nextcoord[0] >= 0 and nextcoord[1] < 100 and nextcoord[1] >= 0 and t>3600:
            
            map[nextcoord[1]][nextcoord[0]] = "#"
        t+= 1


for y in range(len(map)):
    for x in range(len(map[y])):
        if map[y][x] == " ":
            print(x,y)


    