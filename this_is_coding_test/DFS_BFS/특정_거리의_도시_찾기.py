from collections import deque

n, m, k, x = map(int, input().split())
path = [[] for _ in range(n+1)]
distance = [-1]*(n+1)
distance[x] = 0
for _ in range(m):
    a, b = map(int, input().split())
    path[a].append(b)

q = deque([x])
while q:
    v = q.popleft()
    for city in path[v]:
        if distance[city] == -1:
            q.append(city)
            distance[city] = distance[v] + 1

check = False
for i in range(n+1):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)