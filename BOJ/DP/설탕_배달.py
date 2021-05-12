sugar = int(input())
dp = [0]
for i in range(sugar):
    dp.append(9999999)

for i in range(3, sugar+1):
    if i >= 5:
        dp[i] = min(dp[i], dp[i-3]+1, dp[i-5]+1)
    else:
        dp[i] = min(dp[i], dp[i-3]+1)

if dp[-1] == 9999999:
    print(-1)
else:
    print(dp[-1])