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
            print("Solved in", len(moves), "moves:")
            for move in moves:
                print(f"Move disk from {chr(move[0]+65)} to {chr(move[1]+65)}")
            return

        for i in range(3):
            if not tower[i]:
                continue
            disk = tower[i][-1]
            for j in range(3):
                if i == j:
                    continue
                if not tower[j] or tower[j][-1] > disk:
                    new_tower = [peg[:] for peg in tower]
                    new_tower[j].append(new_tower[i].pop())
                    stack.append((new_tower, moves + [(i, j)]))
