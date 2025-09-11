# N x M 격자에서 트리미노(L, 일자)를 놓았을 때의 최대 합 구하기
# https://www.codetree.ai/ko/external-connection/classes/125/lectures/1065/curated-cards/challenge-tromino/description
lines = [
    "3 3",
    "1 2 3",
    "3 2 1",
    "3 1 1"
]

it = iter(lines)
input = lambda : next(it)
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 가능한 모든 블록 모양 (좌표 리스트)
shapes = [
    # --- 일자 블록
    [(0,0), (0,1), (0,2)],
    [(0,0), (1,0), (2,0)],

    # ㄱ L 블록 (회전/대칭 포함 4가지)
    [(0,0), (1,0), (1,1)],
    [(0,0), (1,0), (1,-1)],
    [(0,0), (0,1), (1,0)],
    [(0,0), (0,1), (-1,0)]
]

max_sum = 0

for i in range(N):
    for j in range(M):
        for shape in shapes:
            s = 0
            valid = True
            for dx, dy in shape:
                x, y = i + dx, j + dy
                if 0 <= x < N and 0 <= y < M:
                    s += grid[x][y]
                else:
                    valid = False
                    break
            if valid:
                max_sum = max(max_sum, s)

print(max_sum)