T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(N)]

    for k in range(1, M+1):
        for i in range(N):
            for j in range(N):
                if M % k == 0:
                    num_list[i][j] = not num_list[i][j]
                elif (i+j+2) % k == 0:
                    num_list[i][j] = not num_list[i][j]

    cnt = sum(map(sum, num_list))
    print('#{} {}'.format(tc+1, cnt))