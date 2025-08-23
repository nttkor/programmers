# 현재 상황을 보면, 멀티프로세싱을 사용해도 CPU 코어가 여러 개 사용되지 않고, 하나의 코어만 99% 사용되고 나머지 코어는 거의 사용되지 않는 문제가 발생하고 있는 것 같습니다. 이는 멀티프로세싱을 활용하더라도 프로세스 간의 작업 분배가 효율적이지 않거나, 각 프로세스의 작업이 대부분 I/O 작업 또는 단일 프로세스에서 CPU 집중 작업을 하고 있을 가능성이 있습니다.

# 가능한 원인:
# 작업 부하의 불균형:
# n-queen 문제처럼 백트래킹은 재귀적으로 깊게 탐색하는 작업입니다. 처음 몇 가지 단계에서 빠르게 해를 찾고 나머지 단계에서 더 많은 탐색이 필요한 경우가 많아서, 모든 프로세스가 같은 양의 작업을 하지 않게 됩니다.
# 예를 들어, 프로세스 하나가 너무 많은 경로를 탐색하고 다른 프로세스는 상대적으로 적은 경로만 탐색하게 되는 일이 발생할 수 있습니다.
# I/O 작업으로 인한 CPU 활용도 감소:
# 멀티프로세싱을 사용할 때, 프로세스들이 I/O 작업에 의해 대기할 경우 CPU 활용도가 높지 않을 수 있습니다. 예를 들어, 프로세스들이 결과를 공유하는 데 시간이 걸린다면 CPU 사용이 제한될 수 있습니다.
# 작은 문제 크기:
# n-queen 문제의 크기 (예: 8x8, 12x12)에서 각 프로세스가 할당된 작업이 너무 적거나, 작업을 나누는 방식에 따라 병렬 처리의 이점이 제한적일 수 있습니다. 특히 작은 문제에서는 멀티프로세싱을 사용하는 것보다 단일 프로세스로 실행할 때 더 효율적일 수 있습니다.

# 해결 방안:
# 작업 분배 최적화:
# 각 프로세스가 맡는 작업량을 균등하게 분배하는 방법을 다시 한 번 점검해야 합니다. 현재 코드에서는 행을 나누는 방식인데, 이를 작업 단위가 균등하도록 나누는 방법을 개선할 필요가 있을 수 있습니다.
# 프로세스 내 작업 최적화:
# 각 프로세스가 n-queen 문제를 푸는 데 불필요한 연산을 하지 않도록 최적화합니다.
# 예를 들어, 각 프로세스가 독립적으로 상태를 초기화하고 결과를 처리하는 방식으로 작업을 단순화할 수 있습니다.

# 프로세스 동기화 최적화:
# multiprocessing에서 **Queue**나 **Manager**를 사용하여 프로세스 간의 상태 동기화를 최적화할 필요가 있습니다. 공유 자원에 대한 접근을 최소화하면 성능이 개선될 수 있습니다.
# 병렬 작업을 증가시키는 방법:
# 더 많은 작업 단위를 나누어 각 프로세스가 더 많은 작업을 처리할 수 있도록 해보세요. 예를 들어, 행 단위로 나누는 대신, 더 작은 범위로 나누어 작업 단위를 세분화할 수 있습니다.
# 개선 방법: 작업 범위 나누기 개선
# 기존의 행 단위 나누기 방식 대신, 작은 작업 단위로 나누어 각 프로세스가 더 많은 작업을 처리하도록 할 수 있습니다. 예를 들어, 열 단위나 부분적인 경로를 나누어 작업을 처리하는 방식입니다.
# 코드 개선 예시:
# 작은 작업 단위로 나누어 각 프로세스가 더 많은 작업을 맡게 함으로써 부하를 고르게 분배하는 방법을 고려할 수 있습니다.
# 또는 프로세스가 동적으로 작업을 받도록 작업 큐를 사용할 수도 있습니다.
# 예시 개선 코드 (작업 범위 세분화):


import multiprocessing
import time
import os
def is_safe(board, row, col, n):
    """현재 행과 열에서 퀸을 놓을 수 있는지 확인하는 함수"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    """백트래킹을 이용한 n-queens 문제 해결 함수"""
    if row == n:
        solutions.append(board[:])  # 모든 퀸을 놓았다면, 해결책을 결과에 추가
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col  # 퀸 배치
            solve_n_queens(board, row + 1, n, solutions)  # 다음 행으로 진행
            board[row] = -1  # 백트래킹
def worker_done(pid):
    """각 프로세스가 종료되었을 때 호출될 함수"""
    print(f"프로세스 PID: {pid} - 작업 완료, 종료")


def solve_n_queens_chunk(start_row, end_row, n, results):
    """주어진 범위 내에서 n-queen 문제를 풀고 결과를 results에 추가"""
    solutions = []
    board = [-1] * n  # 보드 초기화
    print(f"프로세스 PID: {os.getpid()} {multiprocessing.current_process().name} - 시작 행 {start_row}부터 {end_row}까지 처리", time.time()-start_time)
    for row in range(start_row, end_row):
        solve_n_queens(board, row, n, solutions)
    
    # 계산된 해를 결과에 추가
    results.append(solutions)

if __name__ == '__main__':
    n = 13  # 체스판 크기 (12로 변경)
    num_processes = 6  # 프로세스 개수 (예: 6개의 프로세서)
    print(f"사용할 프로세스 개수: {num_processes}")
    
    manager = multiprocessing.Manager()
    results = manager.list()  # 공유 리스트 생성
    processes = []

    start_time = time.time()

    # 각 프로세스에 대해 시작 행과 끝 행을 다르게 설정하여, 각 프로세스가 독립적으로 백트래킹을 하도록 한다.
    rows_per_process = n // num_processes  # 각 프로세스가 맡을 행의 개수
    for i in range(num_processes):
        start_row = i * rows_per_process
        end_row = (i + 1) * rows_per_process if i != num_processes - 1 else n  # 마지막 프로세스는 남은 행을 다 처리
        print(f"프로세스 {i + 1}: 행 {start_row}부터 {end_row}까지 처리", time.time()-start_time)
        process = multiprocessing.Process(target=solve_n_queens_chunk, args=(start_row, end_row, n, results))
        processes.append(process)
        process.start()

    # 모든 프로세스가 끝날 때까지 대기
    for process in processes:
        print(f"프로세스 {process.name} 종료 대기 중...", time.time())
        process.join()
        # 프로세스가 종료될 때마다 종료 메시지 출력
        print(f"프로세스 PID: {process.pid} - 작업 완료, 종료", time.time()-start_time)

    # 결과 집계
    total_solutions = 0
    for result in results:
        total_solutions += len(result)

    end_time = time.time()

    print(f"해결 시간: {end_time - start_time:.2f}초")
    print(f"총 경우의 수: {total_solutions}")
