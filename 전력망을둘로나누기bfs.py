def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start, cut_b):
        visited = [False] * (n + 1)
        cnt = 1
        visited[start] = True
        queue = [start]
        while queue:
            current = queue.pop(0)
            for nxt in graph[current]:
                if nxt == cut_b:
                    continue
                if not visited[nxt]:
                    visited[nxt] = True
                    cnt += 1
                    queue.append(nxt)
        return cnt

    answer = n
    for a, b in wires:
        size = bfs(a, b)
        other = n - size
        answer = min(answer, abs(size - other))

    return answer


# 테스트
links = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(9, links))  # 3
