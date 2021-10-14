def func(i, target, now):
    global cnt
    if i == target:
        if now < cnt:
            cnt = now
        return
    if now >= cnt:
        return
    for j in range(N+1):
        if i == j:
            continue
        if visited[j] == 0 and adjM[i][j] > 0:
            visited[j] = 1
            func(j, target, now+adjM[i][j])
            visited[j] = 0


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    adjM = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    for i in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w

    cnt = 987654321
    visited[0] = 1
    func(0, N, 0)
    print(f'#{tc} {cnt}')