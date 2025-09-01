from collections import deque
import copy

def solution(n):
    # 초기 타워 상태: A -> B로 이동, C는 보조
    initial = [[i for i in range(n, 0, -1)], [], []]
    goal = [[], [i for i in range(n, 0, -1)], []]  # 우리가 원하는 상태 (모두 B로 이동)
    
    # 큐에 (현재 타워 상태, 이동 기록) 저장
    stack = deque()
    stack.append((initial, []))
    
    visited = set()
    
    def tower_to_tuple(tower):
        return tuple(tuple(peg) for peg in tower)

    while stack:
        tower, moves = stack.pop()

        # 이미 방문한 상태는 스킵
        t_tuple = tower_to_tuple(tower)
        if t_tuple in visited:
            continue
        visited.add(t_tuple)

        # 종료 조건
        if tower == goal:
            print("Solved in", len(moves), "moves:")
            for move in moves:
                print(f"Move disk from {chr(move[0]+65)} to {chr(move[1]+65)}")
            return

        # 가능한 모든 이동 시도
        for i in range(3):
            if not tower[i]:
                continue  # 출발지 비었으면 못 움직임
            disk = tower[i][-1]
            for j in range(3):
                if i == j:
                    continue  # 같은 곳으로 이동 X
                if not tower[j] or tower[j][-1] > disk:
                    # 복사해서 이동 시뮬레이션
                    new_tower = copy.deepcopy(tower)
                    new_tower[j].append(new_tower[i].pop())
                    new_moves = moves + [(i, j)]
                    stack.append((new_tower, new_moves))


def main():
    solution(3)  # n=3 정도로 먼저 테스트 (5는 너무 많음)

if __name__ == '__main__':
    main()
