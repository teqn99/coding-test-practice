T = int(input())
for tc in range(T):
    N = int(input())
    block_list = list(map(int, input().split()))
    axis = [[0]*100 for _ in range(N)]
    for i in range(N):
        for j in range(block_list[i]):
            axis[i][j] = 1

    maxi = 0
    for i in range(N):
        for j in range(100):
            cnt = 0
            if axis[i][j]:
                for k in range(i+1, N):
                    if axis[k][j] == 0:
                        cnt += 1
                if maxi < cnt:
                    maxi = cnt
    print(f'#{tc+1} {maxi}')