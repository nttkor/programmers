# Block 클래스
class Block:
    def __init__(self, block_id, cells):
        self.id = block_id
        self.cells = cells
        self.size = len(cells)

    # 다른 블록과 인접한지 확인 (상하좌우)
    def is_adjacent(self, other):
        for r1, c1 in self.cells:
            for r2, c2 in other.cells:
                if abs(r1 - r2) + abs(c1 - c2) == 1:
                    return True
        return False

# MicroSimulation 클래스
class MicroSimulation:
    def __init__(self, N):
        self.N = N
        self.grid = [[0] * N for _ in range(N)]
        self.blocks = []
        self.next_id = 1

    # 블록 투입
    def insert_block(self, r1, c1, r2, c2):
        new_cells = []
        for r in range(r1, r2):
            for c in range(c1, c2):
                # 기존 블록 제거
                if self.grid[r][c] != 0:
                    self.remove_block_by_id(self.grid[r][c])
                self.grid[r][c] = self.next_id
                new_cells.append((r, c))
        self.blocks.append(Block(self.next_id, new_cells))
        self.next_id += 1

    # 특정 블록 제거
    def remove_block_by_id(self, block_id):
        self.blocks = [b for b in self.blocks if b.id != block_id]
        for r in range(self.N):
            for c in range(self.N):
                if self.grid[r][c] == block_id:
                    self.grid[r][c] = 0

    # 블록 재배치
    def move_blocks(self):
        new_grid = [[0]*self.N for _ in range(self.N)]
        # 크기 큰 순으로 재배치
        for block in sorted(self.blocks, key=lambda b: (-b.size, b.id)):
            placed = False
            for r0 in range(self.N):
                for c0 in range(self.N):
                    if self.can_place(new_grid, block, r0, c0):
                        self.place_block(new_grid, block, r0, c0)
                        placed = True
                        break
                if placed: break
        self.grid = new_grid

    # 블록 배치 가능 확인
    def can_place(self, grid, block, r0, c0):
        for r, c in block.cells:
            nr, nc = r0 + r, c0 + c
            if nr >= self.N or nc >= self.N or grid[nr][nc] != 0:
                return False
        return True

    # 블록 배치
    def place_block(self, grid, block, r0, c0):
        new_cells = []
        for r, c in block.cells:
            nr, nc = r0 + r, c0 + c
            grid[nr][nc] = block.id
            new_cells.append((nr, nc))
        block.cells = new_cells

    # 점수 계산
    def calculate_score(self):
        score = 0
        visited_pairs = set()
        for i, a in enumerate(self.blocks):
            for j, b in enumerate(self.blocks):
                if i >= j: continue
                if a.is_adjacent(b):
                    pair = (min(a.id, b.id), max(a.id, b.id))
                    if pair not in visited_pairs:
                        score += a.size * b.size
                        visited_pairs.add(pair)
        return score

# -------------------------------
# 입력 처리 및 시뮬레이션 실행
# -------------------------------
import sys

def main():
    input_lines = sys.stdin.read().splitlines()
    N, Q = map(int, input_lines[0].split())
    sim = MicroSimulation(N)

    for line in input_lines[1:1+Q]:
        r1, c1, r2, c2 = map(int, line.split())
        sim.insert_block(r1, c1, r2, c2)
        sim.move_blocks()
        print(sim.calculate_score())

if __name__ == "__main__":
    main()
