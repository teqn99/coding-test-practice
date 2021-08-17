T = int(input())
for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))[::-1]  # 뒤집어서 반대로 탐색하기
    maxi = prices[0]  # 현재 기준 가장 큰 값
    result = 0

    for i in range(1, N):
        if maxi > prices[i]:  # maxi가 여전히 큰 값이라면, 팔아서 이득을 취해야 함,
            result += (maxi - prices[i])
        else:  # maxi보다 큰 값이 나왔다면, maxi를 업데이트
            maxi = prices[i]

    print(f'#{tc+1} {result}')
