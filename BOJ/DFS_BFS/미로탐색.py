from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, str(input()))) for i in range(n)]
visited = [[0]*m for i in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

print(visited[n-1][m-1] + 1)  # 처음 칸도 칸 수에 추가해줘야하므로 +1을 붙인다.