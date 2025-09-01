import matplotlib
matplotlib.use('Agg')  # GUI 없는 백엔드 사용

import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def tower_to_tuple(tower):
    return tuple(tuple(peg) for peg in tower)

def generate_hanoi_state_graph(n):
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
                    new_key = tower_to_tuple(new_tower)
                    G.add_edge(tower_key, new_key)
                    queue.append(new_tower)
    
    return G

def draw_graph_hierarchically(G, start_node, filename="hanoi_state_graph.png"):
    levels = {start_node: 0}
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        for neighbor in G.neighbors(node):
            if neighbor not in levels:
                levels[neighbor] = levels[node] + 1
                queue.append(neighbor)
    
    level_nodes = {}
    for node, level in levels.items():
        level_nodes.setdefault(level, []).append(node)
    
    pos = {}
    y_gap = 2  # 간격 줄임
    for level, nodes in level_nodes.items():
        x_gap = 2  # 간격 줄임
        for idx, node in enumerate(nodes):
            pos[node] = (idx * x_gap, -level * y_gap)

    plt.figure(figsize=(12, 8))  # 적당한 크기
    
    nx.draw(
        G, pos,
        with_labels=False,
        node_size=2000,
        arrowsize=10,
        alpha=0.7
    )

    nx.draw_networkx_labels(
        G, pos,
        labels={
            node: f"A:{list(node[0])}\nB:{list(node[1])}\nC:{list(node[2])}"
            for node in G.nodes
        },
        font_size=8
    )

    plt.title("Hanoi State Graph (Layered by Move Depth)", fontsize=14)
    plt.axis('off')

    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"✅ 그래프가 {filename}로 저장되었습니다.")

if __name__ == "__main__":
    n = 2  # 디스크 개수, 2 이하 권장
    G = generate_hanoi_state_graph(n)
    start = tower_to_tuple([[i for i in range(n, 0, -1)], [], []])
    draw_graph_hierarchically(G, start)
