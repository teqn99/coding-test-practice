import heapq

n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]
indegree = [0 for i in range(n + 1)]
heap = []
result = []

#Graph Information
for i in range(m):
    A, B = map(int, input().split())
    arr[A].append(B)
    indegree[B] += 1  # 각각의 차수를 저장함. ( 이런 형태를 외우자)

#Make First heap
for i in range(1, m + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

#Make Topological Sort Loop
while heap:  # heap 빌때까지 시행
    temp = heapq.heappop(heap)
    result.append(temp)
    for j in arr[temp]:
        indegree[j] -= 1
        if indegree[j] == 0:
            heapq.heappush(heap, j)

for i in result:
    print(i, end=' ')