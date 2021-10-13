def dfs(i, cnt):
    global result
    if result < cnt:
        result = cnt
    for j in graph[i]:
        if not visited[j]:
            visited[j] = 1
            dfs(j, cnt+1)
            visited[j] = 0


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    result = 0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print(f'#{tc} {result}')