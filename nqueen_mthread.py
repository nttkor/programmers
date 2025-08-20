import threading
import time

def solve_n_queens_partial(board_size, start_row, end_row, result):
    """
    주어진 체스판 범위에서 N-Queen 문제 해결 (백트래킹)

    :param board_size: 체스판 크기 (N)
    :param start_row: 탐색 시작 행
    :param end_row: 탐색 종료 행 (포함)
    :param result: 결과 저장 변수 (공유 자원)
    """
    def is_safe(board, row, col):
        # 현재 위치 (row, col)에 퀸을 놓는 것이 안전한지 확인
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(row, board):
        count = 0
        if row == board_size:
            return 1  # 유효한 배치 발견

        for col in range(board_size):
            if is_safe(board, row, col):
                board[row] = col
                count += backtrack(row + 1, board)
        return count

    local_count = 0
    board = [0] * board_size  # 퀸 위치 저장 (인덱스는 행, 값은 열)
    for col_start in range(board_size):
        if start_row == 0: # 시작 행이 0인 경우 해당 열부터 시작
            board[start_row] = col_start
            local_count += backtrack(start_row + 1, board)

    result[0] += local_count


def solve_n_queens_multithreaded(board_size, num_threads):
    """
    멀티스레드를 사용하여 N-Queen 문제 해결

    :param board_size: 체스판 크기 (N)
    :param num_threads: 사용할 스레드 개수
    """
    threads = []
    results = [0]  # 결과 공유를 위한 리스트 (메인 스레드와 공유)

    rows_per_thread = board_size // num_threads
    for i in range(num_threads):
        start_row = i * rows_per_thread
        end_row = start_row + rows_per_thread - 1
        if i == num_threads - 1:  # 마지막 스레드는 남은 행 모두 처리
            end_row = board_size - 1
        thread = threading.Thread(target=solve_n_queens_partial,
                                  args=(board_size, start_row, end_row, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # 모든 스레드 종료 대기

    return results[0]


if __name__ == "__main__":
    N = 12  # 예시 체스판 크기
    num_threads = 12  # 사용할 스레드 개수
    start_time = time.time()
    print(f"{N}-Queen 문제를 {num_threads}개의 스레드를 사용하여 해결 중...")
    total_solutions = solve_n_queens_multithreaded(N, num_threads)
    end_time = time.time()
    print(f"해결 시간: {end_time - start_time:.2f}초")  
    print(f"{N}-Queen 문제의 해답 개수: {total_solutions}")