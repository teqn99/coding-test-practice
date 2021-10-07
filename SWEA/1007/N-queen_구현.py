# 시간초과

def game(idx):
    global cnt
    for j in range(N):
        board[idx][j] = 1
        if idx == N-1:
            sero = sero_check([])
            cross_check(0, N, 0, 0)
            if flag == 1:
                cross = 1
            else:
                cross = 0
            if sero + cross == 2:
                cnt += 1
        if idx+1 < N:
            game(idx+1)
        board[idx][j] = 0


def sero_check(idx_list):
    for i in range(N):
        for j in range(N):
            if j not in idx_list:
                if board[i][j] == 1:
                    idx_list.append(j)
                    break
    if len(idx_list) == N:  # 세로라인에 걸리는게 없는 경우
        return 1
    else:  # 그렇지 않은 경우
        return 0


def cross_check(start, end, idx, temp):
    global flag
    if idx == N:
        if temp == 1:
            flag = 1
        return
    for i in range(start, end):
        for j in range(N):
            if board[i][j] == 1:
                temp += 1
                if j > 0 and j < N:
                    cross_check(start, j, idx+1, temp)  # 왼쪽 대각 아래
                    cross_check(j+1, end, idx+1, temp)  # 오른쪽 대각 아래
                elif j == 0:
                    cross_check(j+1, end, idx+1, temp)  # 오른쪽 대각 아래
                else:
                    cross_check(start, j, idx+1, temp)  # 왼쪽 대각 아래


for tc in range(1, int(input())+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    cnt = 0
    flag = 0

    game(0)
    print(f'#{tc} {cnt}')