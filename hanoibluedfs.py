def solution(n):
    tower = [[i for i in range(n,0,-1)], [],[]]
    goal = [[], [i for i in range(n,0,-1)],[]]
    t_key = tuple(tower)
    moves = []
    stack = []
    visited = set()
    stack.append((t_key,moves))
    while stack:
        tower, moves = stack.pop()
        t_key = tuple(tuple(v) for v in tower)
        if t_key in visited:
            continue
        visited.add(t_key)
        if tower == goal:
            print("found")
            for idx, move in enumerate(moves):
                i,j=move
                print(idx, i,'->',j)
            return
        for i in range(3):
            if not tower[i]:
                continue
            for j in range(3):
                if i == j:
                    continue
                if not tower[j] or tower[j][-1] > tower[i][-1]: 
                    new_tower = [v[:] for v in tower]
                    new_tower[j].append(new_tower[i].pop())
                    stack.append((new_tower,moves+[(i,j)]))

def main():
    solution(2)
    
if __name__ == '__main__':
    main()