T = int(input())
for tc in range(T):
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))
    maxi = 0

    for i in range(N):
        garo = sum(num_list[i])
        for j in range(N):
            sero = 0
            for k in range(N):
                sero += num_list[k][j]
            sero -= num_list[i][j]
            if maxi < garo + sero:
                maxi = garo + sero

    print(f'#{tc+1} {maxi}')