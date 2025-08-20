# 멀티프로세싱을 활용한 n-queen 문제 풀이에서, 각 프로세스가 서로 다른 행 구간을 담당하도록 하고, solve_n_queens_chunk 함수 내에서 백트래킹 알고리즘을 구현해야 합니다.
# 우리가 해야 할 일은 각 프로세스가 백트래킹을 시작하는 행을 나누고, 해당 행에 대해 가능한 퀸 배치를 시도하여 results 리스트에 결과를 저장하도록 하는 것입니다.
# 여기서는 기본적인 백트래킹 알고리즘을 이용해 n-queen 문제를 해결하고, 각 프로세스가 처리할 범위의 시작 행을 기준으로 작업을 분담할 것입니다.
# 다음은 solve_n_queens_chunk 함수 내에 백트래킹 로직을 추가한 코드입니다:

# 주요 설명:
# is_safe 함수: 각 행에 퀸을 놓을 때, 그 위치가 안전한지 체크합니다. 같은 열, 대각선에 퀸이 있는지 검사합니다.
# solve_n_queens 함수: 기본적인 백트래킹 알고리즘을 사용하여 퀸을 놓고, row가 n에 도달하면 유효한 해를 solutions 리스트에 추가합니다.
# solve_n_queens_chunk 함수: 각 프로세스가 담당할 범위의 행을 처리하며, 백트래킹을 수행하여 results에 해결책을 저장합니다.
# 멀티프로세싱: 프로세스 개수에 맞게 작업을 분할하여 각 프로세스가 병렬로 처리합니다.

# 성능:
# n이 커질수록 성능이 개선될 것입니다. 각 프로세스는 독립적으로 작업하므로, 멀티코어 시스템에서 성능 향상이 기대됩니다.

import multiprocessing
import time

def is_safe(board, row, col, n):
    """현재 행과 열에서 퀸을 놓을 수 있는지 확인하는 함수"""
    # 같은 열에 퀸이 있는지 확인
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    """백트래킹을 이용한 n-queens 문제 해결 함수"""
    if row == n:
        # 모든 퀸을 놓았다면, 해결책을 결과에 추가
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n, solutions)
            board[row] = -1  # 백트래킹

def solve_n_queens_chunk(start_row, n, results):
    """주어진 시작 행부터 n-queen 문제를 풀고 결과를 results 리스트에 추가합니다."""
    solutions = []
    # 보드를 초기화 (행마다 -1로 설정)
    board = [-1] * n

    # start_row부터 끝까지 퀸을 배치
    for row in range(start_row, n):
        solve_n_queens(board, row, n, solutions)

    results.append(solutions)

if __name__ == '__main__':
    n = 12  # 체스판 크기
    num_processes = multiprocessing.cpu_count()  # 프로세스 개수
    print(f"사용할 프로세스 개수: {num_processes}, 체스판 크기: {n}")
    
    # 각 프로세스가 처리할 행 범위 설정
    chunk_size = n // num_processes  # 각 프로세스에 할당될 행 수
    manager = multiprocessing.Manager()
    results = manager.list()  # 공유 리스트 생성
    processes = []

    start_time = time.time()

    # 프로세스 생성
    for i in range(num_processes):
        start_row = i * chunk_size
        process = multiprocessing.Process(target=solve_n_queens_chunk, args=(start_row, n, results))
        processes.append(process)
        process.start()

    # 모든 프로세스가 끝날 때까지 대기
    for process in processes:
        process.join()

    # 결과 집계
    total_solutions = 0
    for result in results:
        total_solutions += len(result)

    end_time = time.time()

    print(f"해결 시간: {end_time - start_time:.2f}초")
    print(f"총 경우의 수: {total_solutions}")




