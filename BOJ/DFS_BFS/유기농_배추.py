import sys
sys.setrecursionlimit(10**6)  # for dfs


def dfs(i, j):
    baechu[i][j] = 0
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and baechu[ni][nj]:
            dfs(ni, nj)


def bfs(a, b):
    baechu[a][b] = 0
    q = [(a, b)]
    while q:
        i, j = q.pop(0)
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and baechu[ni][nj]:
                q.append((ni, nj))
                baechu[ni][nj] = 0


for tc in range(int(input())):
    M, N, K = map(int, input().split())
    baechu = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        baechu[b][a] = 1
    result = 0
    for i in range(N):
        for j in range(M):
            if baechu[i][j] == 0:
                continue
            # dfs(i, j)  # dfs 풀이법 - recursion depth를 늘려줘야 한다.
            bfs(i, j)  # bfs 풀이법
            result += 1
    print(result)