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