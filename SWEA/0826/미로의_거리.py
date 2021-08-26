def find_road(i, j, N, cnt):
    global minV
    if maze[i][j] == 3:
        if minV > cnt:
            minV = cnt
        return
    else:
        maze[i][j] = 1
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:
                find_road(ni, nj, N, cnt+1)
        maze[i][j] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    minV = N*N

    for a in range(N):
        for b in range(N):
            if maze[a][b] == 2:
                start = (a, b)
                maze[a][b] = 0

    find_road(start[0], start[1], N, 0)
    if minV == N*N:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} {minV-1}')