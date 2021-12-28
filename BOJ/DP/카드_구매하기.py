N = int(input())
cards = [0]
arr = list(map(int, input().split()))
cards.extend(arr)
dp = [0]*(1+N)

for i in range(1, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], cards[j] + dp[i-j])
print(dp[N])


