def find_road(i, j, N):
    if maze[i][j] == 3:  # 출구에 도착한 경우
        return 1
    else:
        maze[i][j] = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                if find_road(ni, nj, N):
                    return 1
        return 0


T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    for a in range(N):
        for b in range(N):
            maze[a][b] = int(maze[a][b])
    for a in range(N):
        if 2 in maze[a]:
            start = (a, maze[a].index(2))
    print(f'#{tc+1} {find_road(start[0], start[1], N)}')
