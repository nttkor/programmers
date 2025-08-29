from collections import deque

def solution(places):
    answer = []
    
    # 각 대기실마다 거리두기 확인
    for place in places:
        if check_distancing(place):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer

# 하나의 대기실에 대해 거리두기 확인
def check_distancing(place):
    # 'P' 위치 찾기
    people = []
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                people.append((r, c))
    
    # 각 'P'에 대해 BFS 탐색
    for r, c in people:
        # P의 위치에서 맨해튼 거리가 2 이하인 모든 곳을 탐색
        # 만약 그 위치에 또 다른 P가 있다면 거리두기 위반
        if not bfs(place, r, c):
            return False  # 위반 시 바로 False 반환
            
    return True # 모든 P가 거리두기 준수 시 True 반환

# BFS 실행 함수
def bfs(place, r, c):
    # 큐에 시작점 (행, 열, 거리) 추가
    q = deque([(r, c, 0)])
    # 방문 배열 초기화
    visited = [[False] * 5 for _ in range(5)]
    visited[r][c] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        curr_r, curr_c, dist = q.popleft()
        
        # 거리가 2를 초과하면 더 이상 탐색하지 않음
        if dist > 2:
            continue

        # 거리가 0이 아니면서 P를 만난 경우 (시작점 제외)
        if dist > 0 and place[curr_r][curr_c] == 'P':
            return False  # 거리두기 위반

        # 다음 탐색
        for i in range(4):
            nr = curr_r + dx[i]
            nc = curr_c + dy[i]
            
            # 유효성 검사 및 방문 여부 확인
            if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                # 파티션이 아니면 탐색 계속
                if place[nr][nc] != 'X':
                    visited[nr][nc] = True
                    q.append((nr, nc, dist + 1))
                    
    return True
places = [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
        ]
print(solution(places))