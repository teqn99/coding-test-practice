from collections import deque

def dfs(i, j, c, prev):
    global cnt
    if i == N-1 and j == N-1:
        if c < cnt:
            cnt = c
        return
    if c >= cnt:
        return
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            if prev >= arr[ni][nj]:
                dfs(ni, nj, c+1, prev)
            else:
                gap = arr[ni][nj] - prev
                dfs(ni, nj, c+1+gap, arr[ni][nj])
            visited[ni][nj] = 0


def bfs(a, b):
    visited[a][b] = 0
    q = deque()
    q.append((a, b))
    while q:
        i, j = q.popleft()
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N:
                tmp = 1
                if arr[ni][nj] > arr[i][j]:
                    tmp += arr[ni][nj] - arr[i][j]
                if visited[ni][nj] > visited[i][j] + tmp:
                    visited[ni][nj] = visited[i][j] + tmp
                    q.append((ni, nj))


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # visited = [[0]*N for _ in range(N)]                                   # for dfs
    # cnt = 987654321                                                       # for dfs
    # dfs(0, 0, 0, 0)

    visited = [[987654321]*N for _ in range(N)]
    bfs(0, 0)

    # print(f'#{tc} {cnt}')                                                 # for dfs
    print(f'#{tc} {visited[-1][-1]}')
