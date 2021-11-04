import sys
import heapq


input = sys.stdin.readline

N = int(input())
l_heap = []
r_heap = []

for i in range(N):
    num = int(input())
    if len(l_heap) == len(r_heap):
        heapq.heappush(l_heap, num*(-1))
    else:
        heapq.heappush(r_heap, num)
    if len(l_heap) > 0 and len(r_heap) > 0 and l_heap[0]*(-1) > r_heap[0]:
        l = heapq.heappop(l_heap)
        r = heapq.heappop(r_heap)
        heapq.heappush(l_heap, r*(-1))
        heapq.heappush(r_heap, l*(-1))

    print(l_heap[0]*(-1))
