n = int(input())
e = []
for i in range(n):
    e.append(list(map(int, input().split())))
e = sorted(e, key=lambda x: x[0])

dp = [[] for _ in range(n)]
dp[0].append(e[0][1])
for i in range(1, n):
    for j in range(0, i):
        if dp[j][-1] < e[i][1]:
            if len(dp[i]) - 1 < len(dp[j]):
                dp[i] = dp[j] + [e[i][1]]
    if not dp[i]:
        dp[i].append(e[i][1])

maxi = 0
for i in range(n):
    maxi = max(maxi, len(dp[i]))
print(n-maxi)