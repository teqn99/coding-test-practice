def dfs(i, j, cnt, long):
    global result
    if cnt >= result:
        return
    if arr[i][j] == 3:
        result = min(result, cnt)
        return
    for di, dj in ([-1, 0], [0, -1], [1, 0], [0, 1]):
        ni, nj = i + di, j + dj
        if 0 <= ni < M and 0 <= nj < N and not visited[ni][nj] and long > 0:
            visited[ni][nj] = 1
            dfs(ni, nj, cnt, long-1)
            if arr[ni][nj] == 1:
                dfs(ni, nj, cnt+1, L)
            visited[ni][nj] = 0


for tc in range(1, int(input())+1):
    M, N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    visited = [[0]*N for _ in range(M)]

    result = 987654321
    visited[M-1][0] = 1
    dfs(M-1, 0, 0, L)

    if result == 987654321:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {result}')