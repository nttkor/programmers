def print_tower(tower):
    for i, peg in enumerate(tower):
        print(f"{chr(i+65)}: {peg}")
    print()

def solution(n):
    initial = [[i for i in range(n, 0, -1)], [], []]
    goal = [[], [i for i in range(n, 0, -1)], []]

    stack = []
    stack.append((initial, []))
    visited = set()

    def tower_to_tuple(tower):
        return tuple(tuple(peg) for peg in tower)

    while stack:
        tower, moves = stack.pop()

        t_tuple = tower_to_tuple(tower)
        if t_tuple in visited:
            continue
        visited.add(t_tuple)

        if tower == goal:
            print("Solved in", len(moves), "moves:\n")
            print("Initial state:")
            print_tower(initial)

            current_state = [peg[:] for peg in initial]
            for idx, move in enumerate(moves, 1):
                i, j = move
                disk = current_state[i].pop()
                current_state[j].append(disk)
                print(f"Step {idx}: Move disk from {chr(i+65)} to {chr(j+65)}",*current_state)
                # print_tower(current_state)
            return

        for i in range(3):
            if not tower[i]:
                continue
            disk = tower[i][-1]
            for j in range(3):
                if i == j:
                    continue
                if not tower[j] or tower[j][-1] > disk:  #유효성검사
                    new_tower = [peg[:] for peg in tower]
                    new_tower[j].append(new_tower[i].pop())
                    stack.append((new_tower, moves + [(i, j)]))
solution(3)