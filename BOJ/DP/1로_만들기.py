n = int(input())
dp = [0]*n
dp[0] = n
for i in range(1, n):
    if dp[i-1] % 3 == 0 and dp[i-1] % 2 == 0:
        dp[i] = min(dp[i-1]//3, dp[i-1]//2)
        print(1)
    elif dp[i-1] % 3 == 0:
        dp[i] = dp[i-1]//3
        print(2)
    elif dp[i-1] % 2 == 0:
        dp[i] = dp[i-1]//2
        print(3)
    else:
        dp[i] = dp[i-1]-1
        print(4)
print(dp)