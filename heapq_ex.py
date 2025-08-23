import heapq
#from queue import PriorityQueue
def solution(ability, number):
    answer = 0
    heapq.heapify(ability)
    cnt = 0
    while cnt < number:
        a = heapq.heappop(ability)
        b = heapq.heappop(ability)
        heapq.heappush(ability, a+b)
        heapq.heappush(ability, a+b)
        cnt += 1

    cnt = 0
    num = len(ability)
    for v in ability:
        answer += v
    return answer
a = [10, 3, 7, 2]
print(solution(a,2))