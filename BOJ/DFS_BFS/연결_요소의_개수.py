import sys
sys.setrecursionlimit(10000)


def dfs(i):
    visited[i] = 1
    for j in arr[i]:
        if not visited[j]:
            dfs(j)


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)  # 무방향 간선이기 때문에 양 방향을 다 갈 수 있도록 설정해준다.

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        dfs(i)
print(cnt)