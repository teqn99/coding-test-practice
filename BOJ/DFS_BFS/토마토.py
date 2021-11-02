from collections import deque


def bfs():
    global days
    d = days
    q = deque()
    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                q.append((i, j, d))
    while q:
        a, b, d = q.popleft()
        for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            ni, nj = a + di, b + dj
            if 0 <= ni < N and 0 <= nj < M and tomatoes[ni][nj] == 0:
                q.append((ni, nj, d+1))
                tomatoes[ni][nj] = 1
    days = d


M, N = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(N)]
days = 0
bfs()
for i in range(N):
    for j in range(M):
        if tomatoes[i][j] == 0:
            days = -1
            break
print(days)