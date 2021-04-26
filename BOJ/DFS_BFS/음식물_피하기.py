from collections import deque

n, m, k = map(int, input().split())
visited = [[0]*m for _ in range(n)]
matrix = [[0]*m for _ in range(n)]
for _ in range(k):
    a, b = map(int, input().split())
    matrix[a-1][b-1] = 1
result_list = []

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()


def bfs():
    q.append((i, j))
    visited[i][j] = 1
    t = 1
    while q:
        x, y = q.popleft()
        for h in range(4):
            nx = x + dx[h]
            ny = y + dy[h]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    t += 1
    return t


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and matrix[i][j] == 1:
            result = bfs()
            result_list.append(result)

print(max(result_list))