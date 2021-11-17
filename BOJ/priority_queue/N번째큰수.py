import heapq


N = int(input())
heap = []
for i in range(N):
    tmp = list(map(int, input().split()))
    if not heap:
        for t in tmp:
            heapq.heappush(heap, t)
    else:
        for t in tmp:
            if heap[0] < t:
                heapq.heappush(heap, t)
                heapq.heappop(heap)
print(heap[0])