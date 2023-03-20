with open("C:/Users/zacks/Documents/GitHub/Coding-Quest-2023/8/Day8.txt") as f:
    lines = f.readlines()



# parse input data into adjacency matrix
n = len(lines)
graph = [[0] * n for _ in range(n)]
for i in range(n):
    row = list(map(int, lines[i].strip().split()))
    for j in range(n):
        graph[i][j] = row[j]

# run nearest neighbor algorithm
start = 0
visited = set([start])
current = start
distance = 0
while len(visited) < n:
    nearest = min((graph[current][j], j) for j in range(n) if j not in visited)
    distance += nearest[0]
    current = nearest[1]
    visited.add(current)
distance += graph[current][start]

# output result
print(distance)