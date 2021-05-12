N = int(input())
dp = [0]*(1001)

dp[1] = 1  # 상근
dp[3] = 1
for i in range(4, N+1):
    if dp[i-1] == 1 and dp[i-3] == 1:
        dp[i] = 0
    elif dp[i-1] == 0 and dp[i-3] == 0:
        dp[i] = 1

print('SK' if dp[N] == 1 else 'CY')

#--------------------------------
# 다른 풀이
N = int(input())
if N % 2 == 0:
    print('CY')
else:
    print('SK')