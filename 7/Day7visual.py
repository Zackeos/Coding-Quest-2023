import pygrille
import time

PIXEL_SIZE = 30
GRID_DIMENSIONS = (20, 20)
grid = pygrille.Grid(PIXEL_SIZE, GRID_DIMENSIONS, extras = ["Hello", "World"], framerate = 30, default_colour = "black", border_width = 0)

fruitstr = "5,5 8,17 5,2 17,14 2,4 17,6 17,17 1,1 2,3 4,9 13,2 12,15 18,15 12,1 17,5 2,14 7,3 17,6 7,13 6,5 5,17 17,12 16,7 15,15 14,14 10,8 15,5 12,12 9,18 7,16 1,3 16,13 12,11 13,6 11,1 5,4 15,8 6,3 5,14 5,3 5,1 17,12 10,14 13,14 18,14 6,14 7,1 15,16 13,4 18,3 9,1 3,13"
fruit = [tuple([int(j) for j in i.split(",")]) for i in fruitstr.split(" ")]
# print(fruit)
moves = "RRRRRRRRRRDDDDDDDDDDUUUUULLLLLLDDDDDDDDDDDDRRRRRRUUUUUUUUUUULLLLLLUUUURRDDRDRDDRDRDRDRDDDDRRRRRRUULLLLLLDLDLDLUUUUUUUULLLLLLLLUUURRRRDDDRRRRRRRRRRRRUUULLDDDRRDDDDDDDDDDLLLLLLLLLLLUUUUUUUUUUUUUUUULLLLLDDDRURRDDDDDDLLDRRRRRRUUUUUUURURRRRRRDDDDDDDDDDDDDLLLLLDRRRRRRRRUUUUUULLLLLLLUUUUUUUUURRRDDDDDDLLLDDRRRRUUUUURRDDDDDDLLLLLLLLLLLLLLLDDDDRRRRUUURUUUUUUUUURRRRRDDDDRRRRRDDDDDDLLLLLLDLLLLLUUUUUUUUURRDDDDDDDDDDDDDLLLLUUUUURRRUUURRDDDDLLDRRRRRRRRRRUUUUUUULLLDDDRDDDLLLDDRRRRRRUUUUUUUUUUUUULLLLDDDDDDDDDDDDDDLLLLUUUUUUUUUUURRRRRRRDDDDDDDLLLLLLDDDDDLDLLLUUUUUULLLLLLLUUUUUUUUURRRRRRRRRDDDDDDDDDDRRRRRRRRUULLLLLLUUUUURRRUUUUULLLLDDLDLLLLLDDDDRRRRRRRRRRRRRUUUUUUUULLLLLLLLLLLDDDDLLLDDDDDDDDDDRRRRRRRRRRRRRRRUUUUUUUUUULLLLLLLLLULLLLLLLUURRRRRRRRRRRRRRRRRDDDDDDDDDDDLLLLLLLLLDDDDLLLLLLLLDRRRRRRRRRUUURRRRRRRRDDDDLLLLLLLLLLLLLLLLLLUUUURRRRRRRULLLLLLLUUUUUUUUUUUURRRRRRRRDDDDDRDDDDDDDDDDDRRRRRDRRRRUULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRULLLLLLLURRRRRRRUULLLLLLLLLLLLLLLLDDDDDDDD"
def nextfruit():
    del fruit[0]

grid.draw()
time.sleep(5)
snaketails = [(0,0)]
score = 0
for move in moves:
    currentfruit = fruit[0]
    grid[currentfruit[0]][currentfruit[1]].colour = "red"
    coordinate = snaketails[-1]
    if move == "U":
        newcord = (coordinate[0], coordinate[1]-1)
    elif move == "D":
        newcord = (coordinate[0], coordinate[1]+1)
    elif move == "L":
        newcord = (coordinate[0]-1, coordinate[1])
    elif move == "R":
        newcord = (coordinate[0]+1, coordinate[1])


    for coord in newcord:
        if coord >19 or coord < 0:
            print(score)
            exit() 
    if newcord in snaketails:
        print(score)
        exit()
    else:
        score+=1
        if currentfruit == newcord:
            grid[currentfruit[0]][currentfruit[1]].colour = "green"
            score += 100
            snaketails.append(newcord)
            nextfruit()
        else:
            removedcolour = snaketails[0]
            grid[removedcolour[0]][removedcolour[1]].colour = "black"
            grid[newcord[0]][newcord[1]].colour = "green"
            del snaketails[0]
            snaketails.append(newcord)
    grid.draw()
    grid.tick()
print(score)



time.sleep(5)