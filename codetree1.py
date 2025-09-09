

n = 5
grid = [
[0, 0, 0, 1, 1],
[1, 0, 1, 1, 1],
[0, 1, 0, 1, 0],
[0, 1, 0, 1, 0],
[0, 0, 0, 1, 1]
]
answer = 0
for y in range(n-2):
    for x in range(n-2):
        flat = [] 
        for row in grid[y:y+3]:
            flat += row[x:x+3]
        a = sum(flat)
        answer = max(answer,a)

print(answer)