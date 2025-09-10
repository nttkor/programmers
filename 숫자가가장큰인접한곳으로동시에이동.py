
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

# myList = [
#     "4 3 3",
#     "1 2 2 3",
#     "3 5 10 15",
#     "3 8 11 2",
#     "4 5 4 4",
#     "2 2",
#     "3 4",
#     "4 2",
# ]

myList = [
    "13 31 20",
    "14 89 62 87 59 35 7 7 30 91 5 66 18",
    "21 68 17 95 90 16 55 96 55 34 46 60 65",
    "41 17 3 52 85 68 28 38 45 18 23 3 86",
    "12 18 19 98 53 56 51 81 80 40 29 45 4",
    "93 87 43 68 12 13 75 38 59 94 96 32 5",
    "49 7 42 92 54 85 18 4 56 94 66 99 53",
    "38 11 87 34 23 9 86 56 85 40 2 90 35",
    "84 44 58 20 74 70 35 92 83 77 29 79 68",
    "9 66 69 37 63 98 27 25 94 91 60 71 22",
    "58 34 72 86 50 53 91 61 30 73 51 62 33",
    "41 20 14 59 52 38 23 28 52 60 83 84 55",
    "45 88 37 84 28 6 8 28 89 91 88 58 84",
    "86 17 90 83 50 57 6 41 96 42 49 34 50",
    "1 9",
    "11 6",
    "2 6",
    "6 13",
    "6 3",
    "10 9",
    "12 4",
    "6 8",
    "4 9",
    "2 4",
    "2 7",
    "8 2",
    "13 7",
    "6 6",
    "8 8",
    "9 6",
    "3 6",
    "10 12",
    "11 8",
    "11 4",
    "12 13",
    "7 6",
    "4 7",
    "7 7",
    "5 8",
    "13 11",
    "6 4",
    "1 2",
    "3 1",
    "4 1",
    "3 5"
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
        if nextPos[0][0] in move:
            move[nextPos[0][0]] += 1
        else:
            move[nextPos[0][0]] = 1 
    marbles = []
    for k,v in move.items():
        if v ==1 :
            r,c = k[0],k[1]
            marbles.append((r,c))
    ct+=1
cnt = 0
print(len(marbles))
