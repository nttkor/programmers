from collections import deque  # BFS를 위해 deque를 import

# -----------------------------
# 블록 정보 클래스 정의
# -----------------------------
class Block:
    def __init__(self, id, cells):
        self.id = id        # 블록 고유 ID
        self.cells = cells  # 블록을 구성하는 (r, c) 좌표 리스트
        self.size = len(cells)  # 블록 셀의 개수

# -----------------------------
# BFS로 블록 탐색
# -----------------------------
def bfs(grid, visited, start_r, start_c, N):
    q = deque()  # BFS 큐 생성
    q.append((start_r, start_c))  # 시작 좌표 추가
    visited[start_r][start_c] = True  # 방문 표시
    cells = [(start_r, start_c)]  # 블록 셀 기록 리스트
    block_id = grid[start_r][start_c]  # 탐색할 블록 ID
    
    # 상하좌우 이동 방향
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    while q:  # BFS 반복
        r, c = q.popleft()  # 큐에서 좌표 꺼냄
        for i in range(4):  # 상하좌우 탐색
            nr, nc = r + dr[i], c + dc[i]  # 이동 좌표 계산
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if grid[nr][nc] == block_id:  # 같은 블록이면
                    visited[nr][nc] = True  # 방문 표시
                    q.append((nr, nc))  # 큐에 추가
                    cells.append((nr, nc))  # 블록 셀에 추가
    return Block(block_id, cells)  # Block 객체 반환

# -----------------------------
# 미생물 투입
# -----------------------------
def insert_micro(grid, new_block_id, r1, c1, r2, c2):
    for r in range(r1, r2):  # 주어진 사각형 영역의 행 반복
        for c in range(c1, c2):  # 열 반복
            grid[r][c] = new_block_id  # 블록 ID로 채움

# -----------------------------
# 블록 찾기 (BFS 기반)
# -----------------------------
def find_blocks(grid, N):
    visited = [[False]*N for _ in range(N)]  # 방문 배열 초기화
    blocks = []  # 블록 리스트
    for r in range(N):  # 모든 행 순회
        for c in range(N):  # 모든 열 순회
            if grid[r][c] != 0 and not visited[r][c]:  # 비어있지 않고 방문하지 않은 셀
                block = bfs(grid, visited, r, c, N)  # BFS로 블록 탐색
                blocks.append(block)  # 리스트에 추가
    return blocks  # 모든 블록 반환

# -----------------------------
# 블록 재배치
# -----------------------------
def move_blocks(grid, N, blocks):
    new_grid = [[0]*N for _ in range(N)]  # 새 용기 생성
    # 블록 크기 큰 순, 크기 같으면 ID 작은 순 정렬
    blocks.sort(key=lambda b: (-b.size, b.id))
    
    for block in blocks:  # 모든 블록 순회
        placed = False  # 배치 여부 플래그
        for r_off in range(N):  # x 좌표 작은 위치 우선
            for c_off in range(N):  # y 좌표 작은 위치
                valid = True  # 배치 가능한지 체크
                for r, c in block.cells:  # 블록의 모든 셀 확인
                    nr, nc = r_off + r, c_off + c  # 새로운 좌표 계산
                    if nr >= N or nc >= N or new_grid[nr][nc] != 0:  # 범위 벗어나거나 겹치면
                        valid = False
                        break  # 배치 불가
                if valid:  # 배치 가능하면
                    for r, c in block.cells:  # 모든 셀 새 위치에 배치
                        new_grid[r_off + r][c_off + c] = block.id
                    placed = True  # 배치 완료
                    break  # 내부 루프 종료
            if placed:  # 배치 완료되면 외부 루프 종료
                break
    return new_grid  # 새 용기 반환

# -----------------------------
# 점수 계산
# -----------------------------
def calculate_score(grid, N):
    visited = [[False]*N for _ in range(N)]  # 방문 배열 초기화
    score = 0  # 점수 초기화
    
    for r in range(N):  # 모든 행 순회
        for c in range(N):  # 모든 열 순회
            if grid[r][c] != 0 and not visited[r][c]:  # 비어있지 않고 방문하지 않은 셀
                block = bfs(grid, visited, r, c, N)  # BFS로 블록 탐색
                neighbors = set()  # 인접 블록 ID 집합
                dr = [1, -1, 0, 0]  # 상하좌우
                dc = [0, 0, 1, -1]
                for br, bc in block.cells:  # 블록의 모든 셀
                    for i in range(4):  # 상하좌우 확인
                        nr, nc = br + dr[i], bc + dc[i]
                        if 0 <= nr < N and 0 <= nc < N:  # 범위 체크
                            nid = grid[nr][nc]
                            if nid != 0 and nid != block.id:  # 다른 블록이면
                                neighbors.add(nid)  # 인접 집합에 추가
                for nid in neighbors:  # 인접 블록 순회
                    neighbor_size = sum(1 for r2 in range(N) for c2 in range(N) if grid[r2][c2]==nid)
                    score += block.size * neighbor_size  # 점수 계산
    return score  # 최종 점수 반환

# -----------------------------
# 메인 시뮬레이션
# -----------------------------
def simulate(N, Q, queries):
    grid = [[0]*N for _ in range(N)]  # 초기 용기
    results = []  # 실험 결과 리스트
    
    for i, (r1, c1, r2, c2) in enumerate(queries):
        new_id = i + 1  # 블록 ID
        insert_micro(grid, new_id, r1, c1, r2, c2)  # 1. 블록 투입
        blocks = find_blocks(grid, N)  # 2. 블록 탐색
        grid = move_blocks(grid, N, blocks)  # 3. 블록 재배치
        score = calculate_score(grid, N)  # 4. 점수 계산
        results.append(score)  # 결과 저장
    
    return results  # 모든 실험 결과 반환

# -----------------------------
# 입력 예시 테스트
# -----------------------------
if __name__ == "__main__":
    N = 8  # 그리드 크기
    Q = 4  # 실험 횟수
    queries = [  # 각 실험의 좌하, 우상 좌표
        (2, 2, 5, 6),
        (2, 3, 5, 8),
        (2, 0, 5, 3),
        (1, 1, 6, 6)
    ]
    results = simulate(N, Q, queries)  # 시뮬레이션 실행
    for r in results:  # 결과 출력
        print(r)
