import os
import sys
os.chdir(os.path.dirname(__file__))
file = open('input.txt','r')
sys.stdin = file
n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(lambda x : int(x)-1, input().split())) for _ in range(m)]
#r = [pos[0] for pos in marbles]
#c = [pos[1] for pos in marbles]

# Please write your code here.
ct = 0
dirs = [(-1,0),(1,0),(0,-1),(0,1)]  #상하좌우
for ct in range(t):
    collisions = dict()
    for pos in marbles:
        y,x = pos
        v = a[y][x]    
        bestv, besty, bestx = 0,0,0
        for dy, dx in dirs:
            ny, nx = y+dy, x+dx
            if 0<= ny < n and 0<= nx < n:
                nv = a[ny][nx]
                if bestv < nv: 
                    bestv, besty, bestx = a[ny][nx],ny,nx
        if bestv>0:
            if (besty,bestx) in collisions:
                collisions[(besty,bestx)] += 1
            else:
                collisions[(besty,bestx)] = 1
    marbles = []
    for key, value in collisions.items():
        if value == 1:
            y,x = key[0], key[1]
            marbles.append((y,x))
print(len(marbles))