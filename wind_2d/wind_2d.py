import sys
import os
os.chdir(os.path.dirname(__file__))
file = open('input1.txt','r')
sys.stdin = file
n, m, q = map(int, input().split())

# Create 2D array for building state
a = [list(map(int, input().split())) for _ in range(n)]

# Process wind queries
winds = [tuple(x-1 for x in map(int, input().split())) for _ in range(q)]

# Please write your code here.
for r1,c1,r2,c2 in winds:
    s1 = [i for i in a[r1][c1:c2]]
    s2 = [a[j][c2] for j in range(r1,r2)]
    s3 = [i for i in a[r2][c2:c1:-1]]
    s4 = [a[j][c1] for j in range(r2,r1,-1)]
    s = [s4[-1]]+s1[1:] + s2 + s3 + s4[:-1]
    
    idx = 0
    for j in range(c1, c2):       # 위쪽
        a[r1][j] = s[idx]; idx += 1
    for i in range(r1, r2):       # 오른쪽
        a[i][c2] = s[idx]; idx += 1
    for j in range(c2, c1, -1):   # 아래쪽
        a[r2][j] = s[idx]; idx += 1
    for i in range(r2, r1, -1):   # 왼쪽
        a[i][c1] = s[idx]; idx += 1

    tem = [[0]*m row in a]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    for i in range(r1+1, r2):        # 내부 행
        for j in range(c1+1, c2):    # 내부 열
            s, cnt = 0,0
            for dy,dx in dirs:
                ny, nx = dy+i,dx+j
                s += a[ny][nx]
                cnt += 1
            tem[i][j] = s//cnt
            


    print(s)
file.close()