def move(times, i, j, number):
    if times >= 6:
        result_set.add(number)
        return
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            move(times + 1, ni, nj, number + str(board[ni][nj]))


for tc in range(1, int(input())+1):
    board = [list(map(int, input().split())) for _ in range(4)]
    result_set = set()
    for i in range(4):
        for j in range(4):
            move(0, i, j, str(board[i][j]))

    print(f'#{tc} {len(result_set)}')