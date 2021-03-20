n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for i in range(n):
    if target < coins[i]:
        break
    target += coins[i]
print(target)
# 알고리즘 짤 때 생각 많이 해보기
# 이건 좀 어려웠다...
