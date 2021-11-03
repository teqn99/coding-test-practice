import sys
sys.setrecursionlimit(10**6)


def dfs(i, j):
    global flag
    if not arr[i][j]:
        return
    visited[i][j] = 1
    flag += 1
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            flag = 0
            if visited[i][j] == 0:
                dfs(i, j)
                if flag > 0:
                    cnt += 1
    print(cnt)
