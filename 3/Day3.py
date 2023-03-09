with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/3/Day3.txt") as f:
    data = [[int(j) for j in thing.split()] for thing in f.readlines()]

xwon = 0
owon = 0
draw = 0

def checkwinner(played):
    #check rows
    row1, row2, row3 = [played["1"], played["2"], played["3"]], [played["4"], played["5"], played["6"]], [played["7"], played["8"], played["9"]]
    #check columns
    col1, col2, col3 = [played["1"], played["4"], played["7"]], [played["2"], played["5"], played["8"]], [played["3"], played["6"], played["9"]]
    #check diagonals
    diag1, diag2 = [played["1"], played["5"], played["9"]], [played["7"], played["5"], played["3"]]
    allthings = [row1, row2, row3, col1, col2, col3, diag1, diag2]
    for thing in allthings:
        if thing[0] == None:
            continue
        if thing[0] == thing[1] and thing[1] == thing[2]:
            return thing[0]
    return None



for board in data:
    emptyboard = {"0":None,
             "1": None,
             "2": None,
             "3": None,
             "4": None,
             "5": None,
             "6": None,
             "7": None,
             "8": None,
             "9": None}
    
    for z in range(len(board)):
        
        if z % 2 == 0:
            emptyboard[str(board[z])] = "x"
        else:
            emptyboard[str(board[z])] = "o"
        result = checkwinner(emptyboard)
        if result == None:
            pass
        elif result == "x":
            xwon += 1
            break
        elif result == "o":
            owon += 1
            break
        if z == len(board)-1:
            draw += 1

print(xwon, owon, draw)
print(xwon*owon*draw)