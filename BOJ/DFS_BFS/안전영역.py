import sys
sys.setrecursionlimit(10**6)


def dfs(i, j, height):
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] > height and visit[ni][nj] != 1:
            visit[ni][nj] = 1
            dfs(ni, nj, height)


input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
for height in range(101):
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j] != 1 and arr[i][j] > height:
                visit[i][j] = 1
                dfs(i, j, height)
                cnt += 1
    result = max(cnt, result)
print(result)