
# myList = [
#     "4 3 1",
#     "1 2 2 3",
#     "3 5 10 15",
#     "3 8 11 2",
#     "4 5 4 4",
#     "2 2",
#     "3 4",
#     "4 2",
# ]

myList = [
    "4 3 3",
    "1 2 2 3",
    "3 5 10 15",
    "3 8 11 2",
    "4 5 4 4",
    "2 2",
    "3 4",
    "4 2",
]

def myinput():
    return myList.pop(0)

n, m, t = map(int, myinput().split())

# Create n x n grid
a = [list(map(int, myinput().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(lambda x : int(x)-1, myinput().split())) for _ in range(m)]
#r = [pos[0] for pos in marbles]
#c = [pos[1] for pos in marbles]
ct = 0
dirs = [(-1,0),(1,0),(0,-1),(0,1)]  #상하좌우

while ct < t:
    move = dict()
    for pos in marbles:
        nextMarble=[]
        nextPos = []
        for dr, dc in dirs:
            nr, nc = pos[0]+dr, pos[1]+dc
            if 0<= nr < n and 0<= nc < n: 
                nextPos.append([(nr,nc),a[nr][nc]])
        nextPos.sort(key=lambda x:x[1], reverse=True)
        move[nextPos[0][0]] = nextPos[0][1]
    marbles = []
    for k,v in move.items():
        r,c = k[0],k[1]
        marbles.append((r,c))
    ct+=1
cnt = 0
print(len(marbles))
