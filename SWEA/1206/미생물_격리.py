def calc(dict):
    total = 0
    for rc, val in dict.items():
        total += val[NUM]
    return total


def solve():
    global virus
    for _ in range(M):  # M 시간 뒤의 결과를 구해야 함
        new = {}  # 이동을 마친 바이러스를 넣을 딕셔너리

        # 이동
        for rc, val in virus.items():
            num, direct, _ = val
            next_row = rc[0] + dx[direct - 1]
            next_col = rc[1] + dy[direct - 1]
            if next_row == 0 or next_row == N - 1 or next_col == 0 or next_col == N - 1:
                if direct == 1:
                    direct = 2
                elif direct == 2:
                    direct = 1
                elif direct == 3:
                    direct = 4
                elif direct == 4:
                    direct = 3
                num = num // 2

                if num == 0:
                    continue

            if (next_row, next_col) not in new:
                new[(next_row, next_col)] = [num, direct, num]
            else:
                if num > new[(next_row, next_col)][MAX]:  # max num보다 크면 direct를 교체
                    new[(next_row, next_col)][DIRECT] = direct
                    new[(next_row, next_col)][MAX] = num  # max 교체
                new[(next_row, next_col)][NUM] += num

        virus = new
    return calc(virus)


NUM, DIRECT, MAX = 0, 1, 2  # virus에서 쓰일 각각의 좌표의 의미
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)
for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())  # 격자의 크기 N, 시간 M, 군집의 갯수 K
    virus = {}
    for _ in range(K):
        x, y, n, d = map(int, input().split())  # 가로, 세로, 군집크기, 방향
        virus[(x, y)] = [n, d, n]  # 군집 크기, 방향, max(같은 셀에 모인 군집 중 가장 큰 크기. 현재는 자기 뿐이므로 자기 자신의 크기 n)

    print(f"#{tc} {solve()}")