def bfs(s, V):
    q = []
    visited = [0]*(V+1)
    q.append(s)                                     # 시작점 enqueue
    visited[s] = 1                                  # 시작점 visited 표시

    while q:                                        # 큐가 비어 있지 않으면
        t = q.pop(0)                                # 꺼내서 t에 저장
        for i in adj_list[t]:                       # t에 인접이고 미방문인 모든 i에 대해
            if visited[i] == 0:
                q.append(i)                         # enqueue(i)
                visited[i] = visited[t] + 1         # i visited로 표시

    return visited


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    for i in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    S, G = map(int, input().split())
    cnt = 0

    v = bfs(S, V)
    if v[G] == 0:
        print(f'#{tc+1} {v[G]}')
    else:
        print(f'#{tc+1} {v[G]-1}')