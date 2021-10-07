def is_safe(k, i):
    for m in range(N):
        # 좌우는 확인할 필요가 없다.
        if visited[m][i] == 1:  # 상하 확인
            return
        if 0 <= k+m < N and 0 <= i+m < N:  # 오른쪽 아래 대각선 확인
            if visited[k+m][i+m] == 1:
                return
        if 0 <= k-m < N and 0 <= i+m < N:  # 오른쪽 위 대각선 확인
            if visited[k-m][i+m] == 1:
                return
        if 0 <= k+m < N and 0 <= i-m < N:  # 왼쪽 아래 대각선 확인
            if visited[k+m][i-m] == 1:
                return
        if 0 <= k-m < N and 0 <= i-m < N:  # 왼쪽 위 대각선 확인
            if visited[k-m][i-m] == 1:
                return
    return True  # 퀸을 놓을 수 있는 자리라는 것을 확인


def queen(k):
    global cnt
    if k == N:
        cnt += 1
        return
    for i in range(N):
        if not visited[k][i]:
            if is_safe(k, i):
                visited[k][i] = 1
                queen(k+1)
                visited[k][i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    cnt = 0

    queen(0)
    print(f'#{tc} {cnt}')