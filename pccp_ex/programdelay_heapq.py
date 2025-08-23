import heapq

def solution(program):
    answer = [0 for _ in range(11)]
    
    # 시작 시간, 레벨 기준 정렬 (우선 시작 시간, 그 다음 레벨 우선)
    program.sort(key=lambda x: (x[1], x[0]))

    wait_heap = []  # 실행 대기 큐 (레벨 기준 min-heap)
    time = 0        # 현재 시간
    i = 0           # program 리스트 인덱스

    while i < len(program) or wait_heap:
        # 현재 시간에 시작 가능한 프로그램을 모두 대기 큐에 삽입
        while i < len(program) and program[i][1] <= time:
            level, start, duration = program[i]
            heapq.heappush(wait_heap, (level, start, duration))
            i += 1

        if wait_heap:
            level, start, duration = heapq.heappop(wait_heap)
            # 대기 시간은 현재 시간 - 시작 시간
            answer[level] += time - start
            time += duration  # 현재 시간 갱신
            answer[0] = time  # 마지막 실행 완료 시간 갱신
        else:
            # 실행할 수 있는 프로그램이 없으면 다음 프로그램까지 시간 점프
            if i < len(program):
                time = program[i][1]

    return answer
programs = [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]
print(solution(programs))