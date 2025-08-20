import multiprocessing
import time

def solve_n_queens_chunk(start_row, n, results):
    """주어진 시작 행부터 n-queen 문제를 풀고 결과를 results 리스트에 추가합니다."""
    # 백트래킹 코드는 여기에 구현 (예: [1, 2, 1])
    solutions = []
    # ... (백트래킹 로직) ...
    results.append(solutions)


if __name__ == '__main__':
    n = 8  # 체스판 크기
    num_processes = multiprocessing.cpu_count()  # 프로세스 개수
    chunk_size = n // num_processes  # 각 프로세스에 할당될 행 수
    manager = multiprocessing.Manager()
    results = manager.list() # 공유 리스트 생성
    processes = []
    start_time = time.time()
    for i in range(num_processes):
        start_row = i * chunk_size
        process = multiprocessing.Process(target=solve_n_queens_chunk, args=(start_row, n, results))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_solutions = 0
    for result in results:
        total_solutions += len(result)

    end_time = time.time()
    print(f"해결 시간: {end_time - start_time:.2f}초")
    print(f"총 경우의 수: {total_solutions}")