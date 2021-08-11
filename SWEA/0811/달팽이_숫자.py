def snail(n):
    A = [[0] * n for _ in range(n)]
    cnt = 1
    i, j, k = 0, -1, 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while cnt <= n*n:
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < n and 0 <= nj < n and A[ni][nj] == 0:
            A[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k+1) % 4
    return A

T = int(input())
for tc in range(T):
    N = int(input())
    result = snail(N)
    print(f'#{tc+1}')
    for a in range(N):
        for b in range(N):
            print(result[a][b], end=' ')
        print()