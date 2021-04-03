N = int(input())
schedule = [[0, 0]]
for _ in range(N):
    schedule.append(list(map(int, input().split())))

dp = [0] * (N + 2)
tmp = 0

for i in range(1, len(schedule)):
    tmp = max(tmp, dp[i])
    if i + schedule[i][0] <= N + 1:
        dp[i + schedule[i][0]] = max(tmp + schedule[i][1], dp[i + schedule[i][0]])

print(max(dp))