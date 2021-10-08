def find_room(i, j, times, number):
    global maxV
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and num[i][j] + 1 == num[ni][nj]:
            find_room(ni, nj, times+1, number)
        elif 0 <= ni < N and 0 <= nj < N and num[i][j] + 1 != num[ni][nj]:
            if times >= maxV:
                maxV = times
                move_times.add((number, times))


for tc in range(1, int(input())+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    move_times = set()
    maxV = 0

    for i in range(N):
        for j in range(N):
            find_room(i, j, 1, num[i][j])

    a = sorted(list(move_times), key=lambda x: (x[1], -x[0]))
    print(f'#{tc} {a[-1][0]} {a[-1][1]}')