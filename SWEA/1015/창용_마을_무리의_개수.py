def dfs(i):
    if visited[i] == 1:
        return
    visited[i] = 1
    for j in range(len(people[i])):
        dfs(people[i][j])


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    people = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        people[a].append(b)
        people[b].append(a)
    visited = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')