def find_road(i, j):
    if maze[i][j] == 3:
        return 1
    else:
        maze[i][j] = 1
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1:
                if find_road(ni, nj):
                    return 1
        return 0


for tc in range(10):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        if 2 in maze[i]:
            a = i
            b = maze[i].index(2)

    ans = find_road(a, b)
    print(f'#{N} {ans}')


# ============================================================================
# 다른 풀이
from collections import deque


def bfs(maze, x, y):  # x, y: 시작점
    visited = [[0] * 16 for _ in range(16)]
    q = deque()
    q.append([x, y])
    while q:
        cx, cy = q.popleft()
        visited[cy][cx] = 1
        if maze[cy][cx] == '3':  # 도착점 발견한 경우, 1 리턴
            return 1

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 이동 방향 탐색
            nx, ny = cx + dx, cy + dy  # 범위를 벗어날 수 없으므로, 범위는 고려 X
            if not visited[ny][nx] and maze[ny][nx] != '1':
                q.append([nx, ny])

    return 0  # 도착점 찾지 못한 경우 0 리턴


for _ in range(1, 11):
    tc = int(input())
    maze = [input() for _ in range(16)]

    for i in range(16):  # 시작점 탐색
        if maze[i].count('2'):
            sx, sy = maze[i].index('2'), i
            break

    print(f'#{tc} {bfs(maze, sx, sy)}')