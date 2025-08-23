def solution(n, wires):
    # 그래프 만들기
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # DFS 함수: cut_b로는 안 넘어가도록
    def dfs(current, cut_b, parent=-1):
        cnt = 1
        for nxt in graph[current]:
            if nxt == cut_b:    # 끊은 간선으로는 못감
                continue
            if nxt != parent:   # 부모 노드 피하기
                cnt += dfs(nxt, cut_b, current)
        return cnt

    # 모든 간선 끊어보기
    answer = n
    for a, b in wires:
        size = dfs(a, b)           # a에서 시작
        other = n - size           # 반대쪽 크기
        answer = min(answer, abs(size - other))

    return answer


# 테스트
links = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(9, links))  # 3
