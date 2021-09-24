MAX_VALUE = 999999999
T = int(input())
for tc in range(T):
    fee = list(map(int, input().split()))                                    # 1일, 1달, 3달, 1년(12달)
    month = [0]
    month.extend(list(map(int, input().split())))

    dp = [0] * 13                                                            # 0부터 12월까지
    for i in range(1, 13):
        tmp = [0, 0, MAX_VALUE, MAX_VALUE]                                   # 각각 1일권, 1달권, 3달권, 1년권을 사용한 경우 가격을 저장
        tmp[0] = dp[i-1] + month[i] * fee[0]                                 # 1일권의 경우, dp에는 이전 달의 가격이 저장되어 있음.
        tmp[1] = dp[i-1] + fee[1]                                            # 1달권의 경우
        if i >= 3:
            tmp[2] = dp[i-3] + fee[2]                                        # 3달권의 경우
        if i >= 12:
            tmp[3] = fee[3]                                                  # 1년권의 경우

        dp[i] = min(tmp)

        # 다른 방법
        # if i >= 3:
        #     dp[i] = min(dp[i-1] + month[i] * fee[0], dp[i-1] + fee[1], dp[i-3]+fee[2], fee[3])
        # else:
        #     dp[i] = min(dp[i-1]+month[i]*fee[0], dp[i-1]+fee[1], fee[3])

    print(f'#{tc+1} {dp[12]}')
