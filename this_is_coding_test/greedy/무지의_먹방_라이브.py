# import numpy as np
#
# def muji(food_times, k):
#     food_times = np.array(food_times)
#     i = 0
#     while True:
#         order = sorted(food_times)
#         food_times -= order[i]
#         k -= (len(food_times) - i)
#         i += 1
#         if k <= len(food_times):
#             break
#     if k == 0:
#         return i
#     j = i - 1
#     while True:
#         if food_times[j] > 0:
#             food_times[j] -= 1
#             k -= 1
#         j += 1
#         if j == len(food_times):
#             j = 0
#         if k == 0:
#             break
#
#     while food_times[j] == 0:
#         j += 1
#         if j == len(food_times):
#             j = 0
#     return j + 1
#
# #k = muji([3, 1, 2], 5)
# #k = muji([10, 1, 1, 1], 8)
# k = muji([4, 1, 1, 5], 4)
# print(k)

#---------------------------------------------------------------
# 인터넷 참고한 풀이

def solution(food_times, k):
    food_times_list = []
    totalTime = sum(food_times)

    # 음식의 번호와 음식의 양을 저장
    for i in range(0, len(food_times)):
        food_times_list.append([i, food_times[i]])

    # 전체 먹는 시간보다 k가 크면 계산 불가능 이므로 -1
    if totalTime  <= k:
        return -1

    # 음식 양이 적은 순으로 정렬
    food_times_list.sort(key = lambda x:x[1])

    # 제일 적은 음식을 길이에 곱한 시간 계산
    delTime = food_times_list[0][1]*len(food_times_list)

    # i 사라진 음식의 개수
    i = 1

    # k 가 음식을 사라지게 하는 수보다 클 경우 아래 의 반복문 실행
    while delTime < k:
        k -= delTime
        delTime = (food_times_list[i][1] - food_times_list[i - 1][1]) * (len(food_times_list) - i)
        i += 1

    # 인덱스 순으로 배치
    food_times_list = sorted(food_times_list[i - 1:], key=lambda x: x[0])

    # k번쨰 음식의 인덱스를 출력
    return food_times_list[k % len(food_times_list)][0] + 1  # index가 0부터 시작하므로 +1을 붙인다.

#---------------------------------------------------------------
# 동빈나 참고한 풀이 (...ing)
from collections import deque

def sol(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        q.append([food_times[i], i + 1])

    qu = deque(sorted(q, key = lambda x : x[0]))
    sum_value = 0
    previous = 0
    length = len(food_times)
    print(qu)

    while sum_value + ((qu[0][0] - previous) * length) <= k:
        now = qu.popleft()
        sum_value += now[0]
        length -= 1
        previous = now

    result = sorted(q, key = lambda x : x[1])
    return result[(k - sum_value) % length][1]

k = sol([3, 1, 2], 5)
print(k)