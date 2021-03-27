n, m = map(int, input().split())
weights = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i, len(weights)):
        if i == j:
            continue  # 1번과 1번을 동시에 들 수 없다.
        if (i + 1, j + 1) not in result or (j + 1, i + 1) not in result:  # 두 명이 서로 같지만 반대로 갖고 있는 경우는 같은 경우로 취급
            if weights[i] != weights[j]:  # 두 사람이 서로 다른 무게의 공을 들어야 하기 때문
                result.append((i + 1, j + 1))  # 구분이 편하게 튜플의 형식으로 append

print(len(result))


# n, m = map(int, input().split())
# weights = list(map(int, input().split()))
# check = 0
#
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return n + func(n - 1)
#
# result = func(n - 1)
# for idx, val in enumerate(weights):
#     for j in weights[idx + 1:]:
#         if val == j:
#             check += 1
#
# print(result - check)
# # 전체 경우의 수를 구하고, 겹치는 수가 있는 만큼 빼는 방법을 사용
# # 시도해본 테스트 케이스들은 잘되었지만 문제가 있는 지는 더 알아봐야 한다.