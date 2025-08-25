'''
getWidth 함수를 작성하세요.
'''

def getWidth(myTree) :
    '''
    myTree의 너비가 가장 넓은 레벨과 그 레벨의 너비를 반환하는 함수를 작성하세요.
    가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플로 반환해야 합니다.
    
    반환값 형식 : (l, w)
    '''
    if myTree is None:
        return (0, 0)

    # level -> [min_pos, max_pos]
    level_span = {}
    pos = [0]  # 중위순회 열 인덱스 (클로저에서 갱신)

    def inorder(node, level):
        if node is None:
            return
        inorder(node.left, level + 1)
        pos[0] += 1  # 현재 노드의 열 좌표
        if level in level_span:
            if pos[0] < level_span[level][0]:
                level_span[level][0] = pos[0]
            if pos[0] > level_span[level][1]:
                level_span[level][1] = pos[0]
        else:
            level_span[level] = [pos[0], pos[0]]
        inorder(node.right, level + 1)

    inorder(myTree, 1)

    best_level, best_w = 0, 0
    for l, (mn, mx) in level_span.items():
        w = mx - mn + 1
        if w > best_w or (w == best_w and l < best_level):
            best_level, best_w = l, w

    return (best_level, best_w)

'''
트리의 너비
이번 실습에서는 트리의 너비가 가장 넓은 레벨과, 그 레벨의 너비를 구하는 프로그램을 작성합니다.
트리의 모든 정점들을 격자 무늬의 칸에 넣어서 정리해야 합니다.
이 때 일정한 규칙에 따라 정리해야 하는데, 같은 레벨(깊이)의 정점은 같은 행에 위치해야 하며 한 열에는 하나의 정점만 위치해야 합니다.
또, 한 정점의 왼쪽 서브 트리의 모든 정점들은 자신보다 왼쪽 열에, 오른쪽 서브 트리의 모든 정점들은 자신보다 오른쪽 열에 위치해야 합니다.
트리의 너비는 같은 레벨의 정점들 중에서 가장 오른쪽에 있는 정점의 열에서 가장 왼쪽에 있는 정점의 열을 뺀 값에 1을 더한 결과입니다.
트리가 입력되는 형식과 규칙은 이전의 실습들과 동일하고, Tree 클래스 또한 이전 실습들과 동일합니다.
단, 본 실습에서는 Tree.py 파일에서 클래스를 직접 수정할 수 있습니다.

지시사항
트리를 입력하면 너비가 가장 넓은 레벨과 그 레벨의 너비가 출력되어야 합니다.
getWidth 함수가 트리에서 가장 넓은 레벨 l과 그 레벨의 너비 w를 튜플 형태로 반환하면 됩니다.

입력
첫 번째 줄에 노드의 개수를 의미하는 
n
n이 입력됩니다.

두 번째 줄 부터 
n
n개의 줄에 걸쳐 노드들의 관계가 세 개의 정수로 구분되어 주어집니다.

(n≤1000)
(n≤1000)

x
y
 
z
x y z꼴의 입력은, 
x
x번 노드의 왼쪽 자식이 
y
y, 오른쪽 자식이 
z
z라는 의미입니다.

입력 예시
5
1 2 3
2 4 5
3 -1 -1
4 -1 -1
5 -1 -1
Copy
출력 예시
2 4
Copy
설명
레벨 2의 너비가 4로 가장 큽니다.


'''