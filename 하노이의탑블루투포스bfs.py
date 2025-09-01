from collections import deque
import copy

def solution(n):
    # 초기 상태: A에 n개의 디스크, B와 C는 비어 있음
    initial = [[i for i in range(n, 0, -1)], [], []]
    goal = [[], [i for i in range(n, 0, -1)], []]  # 모두 B로 옮기는 게 목표

    queue = deque()
    queue.append((initial, []))  # (현재 상태, 이동 기록)
    
    visited = set()

    def tower_to_tuple(tower):
        return tuple(tuple(peg) for peg in tower)  # 리스트 → 튜플 변환

    while queue:
        tower, moves = queue.popleft()  # BFS이므로 queue 사용

        t_tuple = tower_to_tuple(tower)
        if t_tuple in visited:
            continue
        visited.add(t_tuple)

        # 목표 상태에 도달하면 출력 후 종료
        if tower == goal:
            print("Solved in", len(moves), "moves:")
            for move in moves:
                print(f"Move disk from {chr(move[0] + 65)} to {chr(move[1] + 65)}")
            return

        # 가능한 모든 (from, to) 움직임 시도
        for i in range(3):  # from 기둥
            if not tower[i]:
                continue  # 비어있으면 이동 불가
            disk = tower[i][-1]
            for j in range(3):  # to 기둥
                if i == j:
                    continue
                if not tower[j] or tower[j][-1] > disk:
                    new_tower = copy.deepcopy(tower)
                    new_tower[j].append(new_tower[i].pop())  # 디스크 이동
                    new_moves = moves + [(i, j)]
                    queue.append((new_tower, new_moves))  # BFS이므로 큐에 추가

def main():
    solution(3)  # 작은 값부터 테스트 (3 → 7 moves)

if __name__ == '__main__':
    main()
