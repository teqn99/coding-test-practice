from collections import deque


def bfs():
    global days
    d = days
    q = deque()
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if all_tomatoes[h][i][j] == 1:
                    q.append((h, i, j, d))
    while q:
        c, a, b, d = q.popleft()
        for di, dj, dh in [(-1, 0, 0), (0, -1, 0), (1, 0, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            ni, nj, nh = a + di, b + dj, c + dh
            if 0 <= ni < N and 0 <= nj < M and 0 <= nh < H and all_tomatoes[nh][ni][nj] == 0:
                q.append((nh, ni, nj, d+1))
                all_tomatoes[nh][ni][nj] = 1
    days = d


M, N, H = map(int, input().split())
all_tomatoes = []
for i in range(H):
    tomatoes = [list(map(int, input().split())) for _ in range(N)]
    all_tomatoes.append(tomatoes)
days = 0
bfs()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if all_tomatoes[h][i][j] == 0:
                days = -1
                break
print(days)