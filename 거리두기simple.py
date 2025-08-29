def solution(places):
    answer = []
    for room in places:
        # 각 대기실마다 거리두기 준수 여부 확인
        is_safe = True
        for r in range(5):
            for c in range(5):
                if room[r][c] == 'P':
                    # 맨해튼 거리 1, 2인 지점 확인
                    if not check_person(room, r, c):
                        is_safe = False
                        break
            if not is_safe:
                break
        
        if is_safe:
            answer.append(1)
        else:
            answer.append(0)
    return answer

def check_person(room, r, c):
    # 맨해튼 거리 1 검사 (상하좌우)
    moves_1 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in moves_1:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            if room[nr][nc] == 'P':
                return False

    # 맨해튼 거리 2 검사 (상하좌우 2칸, 대각선)
    moves_2 = [(0, 2), (0, -2), (2, 0), (-2, 0)]  # 상하좌우 2칸
    for dr, dc in moves_2:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            if room[nr][nc] == 'P':
                # 중간에 파티션이 있는지 확인
                if room[r + dr // 2][c + dc // 2] == 'O':
                    return False

    moves_diag = [(-1, -1), (-1, 1), (1, -1), (1, 1)] # 대각선
    for dr, dc in moves_diag:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            if room[nr][nc] == 'P':
                # 두 경로 중 하나라도 O인지 확인
                if room[r + dr][c] == 'O' or room[r][c + dc] == 'O':
                    return False

    return True