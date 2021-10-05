for tc in range(1, int(input())+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    dp = [[987654321]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0:
                if j == 0:
                    dp[i][j] = num[i][j]
                    continue
                dp[i][j] = dp[i][j-1] + num[i][j]
            if j == 0:
                dp[i][j] = dp[i-1][j] + num[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + num[i][j]

    print(f'#{tc} {dp[-1][-1]}')