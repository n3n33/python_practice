import heapq
import sys

N = int(input())
heap = []

for _ in range(N): # dummy variable
    nums = list(map(int, sys.stdin.readline().split()))
    # 우선순위 큐의 길이를 N만큼 유지 top에 N번쨰 큰수 있음
    if not heap:
        for num in nums:
            heapq.heappush(heap,num) 
    else:
        for num in nums:
            if heap[0] < num:
                heapq.heappush(heap,num) 
                heapq.heappop(heap)
                
print(heap[0])
