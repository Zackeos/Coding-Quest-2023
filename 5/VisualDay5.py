import pygrille
import time

PIXEL_SIZE = 30
GRID_DIMENSIONS = (50, 10)
grid = pygrille.Grid(PIXEL_SIZE, GRID_DIMENSIONS, extras = ["Hello", "World"], framerate = 30, default_colour = "black", border_width = 0)
with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/5/Day5.txt") as f:
    data = f.readlines()

map = [[" " for z in range(50)] for x in range(10)]
# while grid.check_open():
for rectangle in data:
    rectangle = rectangle.split()
    sx = int(rectangle[0])
    sy = int(rectangle[1])
    for y in range(sy, sy+int(rectangle[3])):
        for x in range(sx, sx+int(rectangle[2])):
            if map[y][x] == " ":
                map[y][x] = "#"
                grid[x][y].colour = "red"
            elif map[y][x] == "#":
                map[y][x] = " "
                grid[x][y].colour = "black"
    grid.draw()
    grid.tick()
time.sleep(5)
grid.quit()




for row in map:
    print("".join(row))
