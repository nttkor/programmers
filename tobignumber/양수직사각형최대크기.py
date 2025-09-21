# 입력 형식:
# 첫 줄에 n(행 수), m(열 수)
# 다음 n줄에 걸쳐 각 행의 정수 m개가 공백으로 구분되어 주어짐
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def maximal_positive_rectangle(grid):
    """
    2D 그리드에서 '양수(>0)'로만 이루어진 가장 큰 직사각형의 넓이를 구한다.
    아이디어:
      1) 각 행을 내려가며, 열별로 '양수가 연속된 높이'를 누적해 height 히스토그램을 만든다.
      2) 매 행마다 만들어진 height에 대해 '히스토그램 최대 직사각형'을
         단조 증가 스택(모노토닉 스택)으로 O(m)에 계산하고, 최대값을 갱신한다.
      3) 모든 행을 처리한 뒤, 한 번이라도 양수 직사각형이 없으면 -1을 반환한다.

    반환:
      - 최대 넓이(양수 면적이 있으면)
      - 없으면 -1
    주의:
      - 이 함수는 외부 스코프의 n, m(입력에서 읽은 값)을 그대로 사용한다.
        grid의 크기와 n, m이 일치한다고 가정한다.
    """

    # height[j]: "현재 행까지" 위로 연속해서 양수가 몇 칸 쌓였는지(막대 높이)
    # 예: grid[i][j] > 0이면 이전 높이에 +1, 아니면 0으로 리셋
    height = [0] * m

    # 지금까지 찾은 최대 직사각형 넓이
    max_area = 0

    # 모든 행을 위에서 아래로 처리
    for i in range(n):
        # 1) 현재 행 i를 반영해서 히스토그램(height) 갱신
        for j in range(m):
            # 양수면 높이 누적(+1), 0 또는 음수면 누적 끊기(0)
            height[j] = height[j] + 1 if grid[i][j] > 0 else 0

        # 2) 갱신된 height를 히스토그램으로 보고,
        #    단조 증가 스택으로 최대 직사각형 넓이를 계산
        # 스택에는 '인덱스 j'를 저장한다.
        # 스택이 유지하는 불변식: height[stack[0]] <= height[stack[1]] <= ...
        stack = []

        # j를 0..m-1까지 돌고, 마지막에 j==m에서 curr_height=0(센티널)로 모두 정산
        for j in range(m + 1):
            # 센티널: 마지막 j==m일 때 '가상의 높이 0'을 던져 스택 비우기 유도
            curr_height = height[j] if j < m else 0

            # 현재 막대의 높이가 스택 top보다 작아지는 순간,
            # top에 있던 막대(=그 높이)로 만들 수 있는 '최대 폭'이 확정된다.
            # → pop 하면서 면적을 계산하고 max 갱신.
            while stack and curr_height < height[stack[-1]]:
                # h: 확정할 직사각형의 '높이'
                h = height[stack.pop()]

                # 폭 w 계산:
                # - 스택이 비었으면, 왼쪽에 자신보다 낮은 막대가 없었음 → 0..(j-1)까지 전부 확장 가능 → w = j
                # - 스택이 남아있으면, 스택 top이 '바로 왼쪽의 더 낮은 막대' → (stack[-1]+1)..(j-1)까지 확장 → w = j - stack[-1] - 1
                w = j if not stack else j - stack[-1] - 1

                # 면적 갱신
                max_area = max(max_area, h * w)

            # 현재 인덱스를 스택에 push (단, height가 단조 증가/같음이 되도록 위 while에서 충분히 pop한 뒤)
            stack.append(j)

    # 한 번도 양수 직사각형이 없었다면 0 그대로 → -1 반환
    return max_area if max_area > 0 else -1

# 결과 출력
print(maximal_positive_rectangle(grid))