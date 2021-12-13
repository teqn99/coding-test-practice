import sys
sys.setrecursionlimit(10**6)


def dfs_for_rg(i, j, r):
    for di, dj in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and not visited_rg[ni][nj] and \
                (arr[i][j] == arr[ni][nj] or (arr[i][j] == 'R' and arr[ni][nj] == 'G') or (arr[i][j] == 'G' and arr[ni][nj] == 'R')):
            visited_rg[ni][nj] = 1
            dfs_for_rg(ni, nj, r+1)


def dfs(i, j, r):
    for di, dj in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[i][j] == arr[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, r+1)


N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
visited_rg = [[0]*N for _ in range(N)]
result = 0
result_rg = 0

for i in range(N):
    for j in range(N):
        if not visited_rg[i][j]:
            visited_rg[i][j] = 1
            dfs_for_rg(i, j, 0)
            result_rg += 1
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, 0)
            result += 1

print(result, result_rg)