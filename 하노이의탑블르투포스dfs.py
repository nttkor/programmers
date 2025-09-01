# 현재 탑의 상태를 출력하는 함수
def print_tower(tower):
    for i, peg in enumerate(tower):
        print(f"{chr(i+65)}: {peg}")  # A, B, C 기둥 이름으로 출력
    print()

def solution(n):
    # 초기 상태: 첫 번째 기둥에 n부터 1까지 디스크가 쌓여 있음
    initial = [[i for i in range(n, 0, -1)], [], []]

    # 목표 상태: 두 번째 기둥에 n부터 1까지 디스크가 쌓여 있음
    goal = [[], [i for i in range(n, 0, -1)], []]

    # 스택에는 (현재 상태, 지금까지의 이동 경로)를 튜플로 저장
    stack = []
    stack.append((initial, []))

    # 방문한 상태를 저장하기 위한 집합 (중복 상태 방지)
    visited = set()

    while stack:
        # 스택에서 상태 하나를 꺼냄
        tower, moves = stack.pop()

        # 리스트는 해시 불가능하므로 튜플로 변환하여 방문 여부 확인
        t_tuple = tuple(tuple(peg) for peg in tower)
        if t_tuple in visited:
            continue
        visited.add(t_tuple)

        # 목표 상태에 도달했으면 결과 출력
        if tower == goal:
            print("Solved in", len(moves), "moves:\n")
            print("Initial state:")
            print_tower(initial)

            # 이동 과정을 하나씩 재현하며 출력
            current_state = [peg[:] for peg in initial]
            for idx, move in enumerate(moves, 1):
                i, j = move  # i번 기둥에서 j번 기둥으로 이동
                disk = current_state[i].pop()  # 디스크 하나를 꺼냄
                current_state[j].append(disk)  # 대상 기둥에 올림
                print(f"Step {idx}: Move disk from {chr(i+65)} to {chr(j+65)}", *current_state)
                # print_tower(current_state)  # 상태를 자세히 보고 싶을 때 사용
            return

        # 모든 가능한 이동 시도
        for i in range(3):  # 출발 기둥
            if not tower[i]:
                continue  # 기둥이 비었으면 건너뜀
            disk = tower[i][-1]  # 가장 위에 있는 디스크 선택
            for j in range(3):  # 도착 기둥
                if i == j:
                    continue  # 같은 기둥으로 이동은 불필요
                # 도착 기둥이 비었거나, 위 디스크보다 작은 디스크만 이동 가능
                if not tower[j] or tower[j][-1] > disk:
                    # 새로운 상태 복사 (원본 훼손 방지)
                    new_tower = [peg[:] for peg in tower]
                    # 디스크 이동
                    new_tower[j].append(new_tower[i].pop())
                    # 새로운 상태와 이동 경로를 스택에 추가
                    stack.append((new_tower, moves + [(i, j)]))

# 실행: 디스크 2개
solution(2)
