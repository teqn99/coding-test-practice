from collections import deque

n, m = map(int, input().split())
visited = [[0]*n for _ in range(m)]
matrix = [list(input()) for _ in range(m)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
w, b = 0, 0

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            q.append((i, j))
            visited[i][j] = 1
            t = 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < m and 0 <= ny < n:
                        if matrix[nx][ny] == matrix[x][y] and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            t += 1
            if matrix[i][j] == 'W':
                w += t**2
            else:
                b += t**2

print(w, b)