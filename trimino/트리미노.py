# N x M 격자에서 트리미노(L, 일자)를 놓았을 때의 최대 합 구하기
import os
import sys
os.chdir(os.path.dirname(__file__))
myinput = []
with open('input.txt', 'r') as file:
    sys.stdin = file
# it = iter(myinput)
# input = lambda: next(it)

    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

# 가능한 모든 블록 모양 (좌표 리스트)
shapes = [
    # 일자 블록
    [(0,0),(0,1),(0,2)],
    [(0,0),(1,0),(2,0)],

    # L자 블록 8가지 회전/대칭
    [(0,0),(1,0),(1,1)],
    [(0,0),(1,0),(1,-1)],
    [(0,0),(0,1),(1,1)],
    [(0,0),(0,1),(-1,1)],
    [(0,0),(0,-1),(1,-1)],
    [(0,0),(0,-1),(-1,-1)],
    [(0,0),(-1,0),(-1,1)],
    [(0,0),(-1,0),(-1,-1)]
]

max_sum = 0

for i in range(n):
    for j in range(m):
        for shape in shapes:
            s = 0
            valid = True
            for dx, dy in shape:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m:
                    s += grid[x][y]
                else:
                    valid = False
                    break
            if valid:
                max_sum = max(max_sum, s)

print(max_sum)
