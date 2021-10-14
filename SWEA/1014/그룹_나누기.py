def dfs(i):
    global cnt
    if group[i] == []:
        return
    next = group[i]
    for j in range(len(next)):
        if visited[next[j]] == 0:
            visited[next[j]] = 1
            dfs(next[j])


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    M_list = list(map(int, input().split()))
    group = [[] for i in range(N+1)]
    visited = [0]*(N+1)
    cnt = 0
    for i in range(len(M_list)):
        if i%2 == 0:
            a = M_list[i]
        else:
            group[a].append(M_list[i])
            group[M_list[i]].append(a)

    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')

