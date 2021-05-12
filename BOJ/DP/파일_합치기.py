"""
풀이 1
- 식 구성을 어떻게 할지 모르겠다...
"""
# def solution(test):
#     dp = [0]*(len(test)+1)
#
#     dp[1] = test[0] + test[1]
#     for i in range(2, len(test)):
#         dp[i] = min(dp[i-1] + test[i], test[i-1] + test[i])
##         dp[i] = min(test[i-1] + test[i], test[i-1] + test[i])
#
#     return sum(dp)
#
#
# T = int(input())
# for _ in range(T):
#     K = int(input())
#     test_list = list(map(int, input().split()))
#     print(solution(test_list))
#

"""
참고용
"""
import sys
read = sys.stdin.readline

for _ in range(int(read())):
    n = int(read())
    num = list(map(int, read().split()))

    dp = list(list(0 for _ in range(n)) for _ in range(n))
    #if n=5
    for k in range(1, n):  #k=1,2,3,4
        for i in range(n-k):  #i=0,1,2,3,4 when k=1
            X, Y = i, i+k
            dp[X][Y] = 2147000000
            for j in range(k):
                tmp = dp[X+1+j][Y] + dp[X][Y-k+j]
                dp[X][Y] = min(dp[X][Y], tmp)
            dp[X][Y] += sum(num[X: Y+1])
    print(dp[0][-1])