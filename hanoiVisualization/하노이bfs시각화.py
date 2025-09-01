import matplotlib
matplotlib.use('Agg')  # GUI 없는 백엔드 사용

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def tower_to_tuple(tower):
    """리스트형 타워 상태를 해시 가능한 튜플로 변환"""
    return tuple(tuple(peg) for peg in tower)

def generate_hanoi_state_graph(n):
    """하노이 상태 공간 그래프 생성"""
    initial = [[i for i in range(n, 0, -1)], [], []]
    visited = set()
    G = nx.DiGraph()
    
    queue = deque()
    queue.append(initial)
    
    while queue:
        tower = queue.popleft()
        tower_key = tower_to_tuple(tower)
        
        if tower_key in visited:
            continue
        visited.add(tower_key)
        
        G.add_node(tower_key)
        
        # 가능한 모든 이동 시도
        for i in range(3):  # from 기둥
            if not tower[i]:
                continue
            disk = tower[i][-1]
            for j in range(3):  # to 기둥
                if i == j:
                    continue
                if not tower[j] or tower[j][-1] > disk:
                    new_tower = [peg[:] for peg in tower]
                    new_tower[j].append(new_tower[i].pop())
                    new_key = tower_to_tuple(new_tower)
                    G.add_edge(tower_key, new_key)
                    queue.append(new_tower)
    
    return G

def draw_graph_hierarchically(G, start_node, filename="hanoi_state_graph.png"):
    """계층 구조로 그래프를 그리고 이미지로 저장"""
    # 노드의 레벨 계산 (BFS로 거리 측정)
    levels = {}
    levels[start_node] = 0
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        for neighbor in G.neighbors(node):
            if neighbor not in levels:
                levels[neighbor] = levels[node] + 1
                queue.append(neighbor)
    
    # 레벨별로 배치 위치 설정
    level_nodes = {}
    for node, level in levels.items():
        level_nodes.setdefault(level, []).append(node)
    
    pos = {}
    y_gap = 15  # 10배 확대
    for level, nodes in level_nodes.items():
        x_gap = 15  # 10배 확대
        for idx, node in enumerate(nodes):
            pos[node] = (idx * x_gap, -level * y_gap)

    # 그림 사이즈도 10배 확대
    plt.figure(figsize=(180, 100))  # 인치 단위, 10배 확대

    nx.draw(
        G, pos,
        with_labels=False,
        node_size=6000,       # 노드 크기 확대
        arrowsize=200,        # 화살표 크기 확대
        alpha=0.7
    )

    nx.draw_networkx_labels(
        G, pos,
        labels={
            node: f"A:{list(node[0])}\nB:{list(node[1])}\nC:{list(node[2])}"
            for node in G.nodes
        },
        font_size=60          # 글씨 크기 확대
    )

    plt.title("Hanoi State Graph (Layered by Move Depth)", fontsize=80)
    plt.axis('off')

    # tight_layout() 제거 → 호환성 경고 방지
    plt.savefig(filename, dpi=300)
    print(f"✅ 그래프가 {filename}로 저장되었습니다.")

# =============================
# 실행 부분
# =============================

if __name__ == "__main__":
    n = 2  # 디스크 개수
    G = generate_hanoi_state_graph(n)
    start = tower_to_tuple([[i for i in range(n, 0, -1)], [], []])
    draw_graph_hierarchically(G, start)
