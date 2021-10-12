from copy import deepcopy as dc


def shoot(N, balls_dc):
    global result
    if N == 0:
        cnt = 0
        for w in range(W):
            for h in range(H):
                if balls_dc[w][h] == 0:
                    cnt += 1
        cnt = W*H - cnt  # 전체에서 0의 개수를 빼면 결과값을 알 수 있다.
        if result > cnt:
            result = cnt
        return
    for w in range(W):
        # 맨 뒤에 있는 0이 아닌 숫자를 찾는 과정 -> h 변수에 자리 킵, num 변수에 숫자 킵
        for h in range(H-1, -1, -1):
            if balls_dc[w][h] != 0:
                num = balls_dc[w][h]
                break
        else:  # 한 행에 모든 수가 0인 경우
            continue
        copied = dc(balls_dc)
        fire(copied, w, h, num)

        # 0이 된 부분들을 모두 뒤로 빼주기
        for i in range(W):
            keep = []
            for j in range(H):
                if copied[i][j] == 0:
                    keep.append(j)
            for j in keep:
                del copied[i][copied[i].index(0)]
            for j in range(len(keep)):
                copied[i].append(0)

        shoot(N-1, copied)


def fire(copied, w, h, num):
    for n in range(num):
        for di, dj in [(-n, 0), (0, -n), (n, 0), (0, n)]:
            ni, nj = w + di, h + dj
            if 0 <= ni < W and 0 <= nj < H:
                next_num = copied[ni][nj]
                copied[ni][nj] = 0
                if n != 0:
                    fire(copied, ni, nj, next_num)


for tc in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    balls = [list(map(int, input().split())) for _ in range(H)]
    balls_rotated = [list(elem) for elem in zip(*balls[::-1])]  # 우측으로 90도 회전
    result = 987654321

    balls_dc = dc(balls_rotated)
    shoot(N, balls_dc)
    if result == 987654321:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {result}')
