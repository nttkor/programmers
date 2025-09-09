# 미생물 블록 시뮬레이션

# 블록 클래스 정의
class Block:
    def __init__(self, block_id, cells):
        self.id = block_id  # 블록 ID
        self.cells = cells  # 블록을 구성하는 셀 리스트 [(r,c), ...]
        self.update_bounds()

    def update_bounds(self):
        """블록의 좌하단과 우상단 좌표 계산"""
        if not self.cells:
            self.min_r = self.min_c = self.max_r = self.max_c = 0
            return
        self.min_r = min(r for r,c in self.cells)
        self.min_c = min(c for r,c in self.cells)
        self.max_r = max(r for r,c in self.cells)
        self.max_c = max(c for r,c in self.cells)

    def size(self):
        """블록의 셀 개수 반환"""
        return len(self.cells)

    def overlaps(self, other):
        """다른 블록과 겹치는지 확인"""
        return any((r,c) in other.cells for r,c in self.cells)

    def remove_cells(self, cells_to_remove):
        """특정 셀들을 제거하고 블록 갱신"""
        self.cells = [cell for cell in self.cells if cell not in cells_to_remove]
        self.update_bounds()

    def is_split(self):
        """블록이 쪼개졌는지 판단 (연속된 스퀘어 여부)"""
        if not self.cells:
            return True
        # 맨 아래 줄부터 위로 합쳐보며 연속되지 않으면 split
        grid = set(self.cells)
        min_r = self.min_r
        max_r = self.max_r
        min_c = self.min_c
        max_c = self.max_c
        # 각 줄에 블록 셀 존재 여부 체크
        prev_row_cells = None
        for r in range(min_r, max_r+1):
            row_cells = [c for rr, c in self.cells if rr==r]
            row_cells.sort()
            if not row_cells:
                return True
            if prev_row_cells is not None:
                # 두 줄의 컬럼이 하나라도 겹치면 계속 연결
                if max(prev_row_cells) < min(row_cells) or min(prev_row_cells) > max(row_cells):
                    return True
            prev_row_cells = row_cells
        return False

# 시뮬레이션 클래스
class MicroSimulation:
    def __init__(self, N):
        self.N = N
        self.grid = [[0]*N for _ in range(N)]
        self.blocks = []
        self.next_id = 1

    def insert_block(self, r1, c1, r2, c2):
        """새 블록 투입 및 기존 블록 겹치는 부분 처리"""
        new_cells = []
        # 새 블록 영역 설정
        for r in range(r1, r2):
            for c in range(c1, c2):
                new_cells.append((r,c))
        new_block = Block(self.next_id, new_cells)
        self.next_id += 1

        # 기존 블록 겹치는 셀 제거
        cells_to_remove = set()
        for blk in self.blocks:
            overlapping = [cell for cell in blk.cells if cell in new_cells]
            if overlapping:
                blk.remove_cells(overlapping)
        # 쪼개진 블록 제거
        self.blocks = [blk for blk in self.blocks if not blk.is_split()]

        # 새 블록 추가
        self.blocks.append(new_block)

        # 그리드 갱신
        self.update_grid()

    def update_grid(self):
        """그리드 상태를 블록 리스트 기준으로 갱신"""
        self.grid = [[0]*self.N for _ in range(self.N)]
        for blk in self.blocks:
            for r,c in blk.cells:
                self.grid[r][c] = blk.id

    def move_blocks(self):
        """큰 블록 순서대로 재배치"""
        # 블록 크기 기준 내림차순, ID 오름차순
        self.blocks.sort(key=lambda b: (-b.size(), b.id))
        new_grid = [[0]*self.N for _ in range(self.N)]

        for blk in self.blocks:
            placed = False
            shape = blk.cells
            # 상대 좌표 기준 (0,0)
            min_r = min(r for r,c in shape)
            min_c = min(c for r,c in shape)
            rel_cells = [(r - min_r, c - min_c) for r,c in shape]
            max_r = max(r for r,c in rel_cells)
            max_c = max(c for r,c in rel_cells)

            # 배치 가능한 좌표 탐색
            for r0 in range(self.N - max_r):
                for c0 in range(self.N - max_c):
                    # 겹치는지 확인
                    if all(new_grid[r0+rr][c0+cc]==0 for rr,cc in rel_cells):
                        # 배치
                        for rr,cc in rel_cells:
                            new_grid[r0+rr][c0+cc] = blk.id
                        # 절대좌표 갱신
                        blk.cells = [(r0+rr, c0+cc) for rr,cc in rel_cells]
                        blk.update_bounds()
                        placed = True
                        break
                if placed: break
        self.grid = new_grid

    def calculate_score(self):
        """인접 블록 간 점수 계산"""
        adjacency = {blk.id:set() for blk in self.blocks}
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        block_map = {}
        for blk in self.blocks:
            for r,c in blk.cells:
                block_map[(r,c)] = blk.id

        # 인접 블록 기록
        for blk in self.blocks:
            for r,c in blk.cells:
                for dr,dc in directions:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<self.N and 0<=nc<self.N:
                        other_id = block_map.get((nr,nc),0)
                        if other_id!=0 and other_id!=blk.id:
                            adjacency[blk.id].add(other_id)

        # 점수 계산, 중복 제거
        sizes = {blk.id: blk.size() for blk in self.blocks}
        score = 0
        counted = set()
        for a in adjacency:
            for b in adjacency[a]:
                if (a,b) in counted or (b,a) in counted:
                    continue
                score += sizes[a]*sizes[b]
                counted.add((a,b))
        return score

# 입력 처리 및 시뮬레이션 실행
def main():
    N,Q = map(int,input().split())
    sim = MicroSimulation(N)
    for _ in range(Q):
        r1,c1,r2,c2 = map(int,input().split())
        sim.insert_block(r1,c1,r2,c2)
        sim.move_blocks()
        print(sim.calculate_score())

if __name__ == "__main__":
    main()
