import copy

n = int(input())
dp = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
if n == 1:
    print(9)
else:
    for j in range(1, n):
        dp_copied = copy.deepcopy(dp)
        for i in range(10):
            if i == 0:
                dp[i] = dp_copied[1]
            elif i == 9:
                dp[i] = dp_copied[8]
            else:
                dp[i] = dp_copied[i-1] + dp_copied[i+1]
    print(sum(dp)%1000000000)