import pygrille
import time

PIXEL_SIZE = 7
GRID_DIMENSIONS = (100, 100)
grid = pygrille.Grid(PIXEL_SIZE, GRID_DIMENSIONS, extras = ["Hello", "World"], framerate = 60, default_colour = "black", border_width = 0)

with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/6/NewAsteroids.txt") as f:
    data = f.readlines()
asteroids = [[int(i) for i in y.split()] for y in data]


def change(ast,coord, time):
    return (coord[0]+ast[2]*time,coord[1]+ast[3]*time)
coords = []
for asteroid in asteroids:
    for coord in coords:
        grid[coord[0]][coord[1]].colour = "green"
    coords = []
    nextcoord = (asteroid[0], asteroid[1])
    for x in range(60):
        nextcoord = change(asteroid, nextcoord, 1)
        if nextcoord[0] < 100 and nextcoord[0] >= 0 and nextcoord[1] < 100 and nextcoord[1] >= 0:
            grid[nextcoord[0]][nextcoord[1]].colour = "red"
            coords.append((nextcoord[0], nextcoord[1]))
    grid.draw()
    grid.tick()


    
    

time.sleep(5)


# for y in range(len(map)):
#     for x in range(len(map[y])):
#         if map[y][x] == " ":
#             print(x,y)


    