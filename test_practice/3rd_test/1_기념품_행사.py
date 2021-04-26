# 50달러당 10달러씩 할인
# goods: 3자매의 구매비용
# 조합을 통해 최소 구매비용을 리턴

# class Solution:
#     def solution(self, goods):
#         dp = [0] * 3
#         # 1차로 50보다 큰 값을 dp에 저장
#         for i in range(len(goods)):
#             if goods[i] >= 50:
#                 dp[i] = goods[i] - 10
#                 goods[i] = 0
#         # 나머지 값들의 계산
#         if sum(goods) >= 50:
#             dp.append(sum(goods) - 10)
#         else:
#             dp.append(sum(goods))
#
#         return sum(dp)

def solution(goods):
    dp = [0] * 3

    # 1차로 50보다 큰 값을 dp에 저장
    for i in range(len(goods)):
        if goods[i] >= 50:
            dp[i] = goods[i] - 10
            goods[i] = 0

    # 나머지 값들의 계산
    if sum(goods) >= 50:
        dp.append(sum(goods) - 10)
    else:
        dp.append(sum(goods))

    print(goods)
    print(dp)
    print(sum(dp))

solution([5,3,15])
