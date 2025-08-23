import heapq
heap = []
for i in range(11,0,-1):
    heapq.heappush(heap,(0,i),key=lambda x:x[1] )
while heap:
    print(heapq.heappop(heap))
    