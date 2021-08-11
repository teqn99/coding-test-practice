"""
나선 방향 돌아가는 2차원 리스트 만들기
예시)
 1  2  3  4  5
16 17 18 19  6
15 24 25 20  7
14 23 22 21  8
13 12 11 10  9
"""

A = [[0] * 5 for _ in range(5)]
N = 5
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
cnt = 1  # ni, nj에 cnt를 쓰려고 함 -> 유효한 범위인가?
i, j, k = 0, -1, 0
while cnt <= N*N:
    ni, nj = i + di[k], j + dj[k]
    if 0 <= ni < N and 0 <= nj < N and A[ni][nj] == 0:
        A[ni][nj] = cnt
        cnt += 1
        i, j = ni, nj
    else:
        k = (k+1) % 4
print(A)
