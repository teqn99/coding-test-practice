# Brute Force 문제
"""
우선 시작점을 정한다.
원이므로 배열에다가 n을 더한 weak_point 배열을 새롭게 만들어준다.
그 다음 시작점에서부터, 가능한 모든 순열(dist의 조합)을 permutations()를 통해 계산하고,
모든 weak point를 커버할 수 있는지 확인하며 최소값을 갱신해 나간다.
"""
from itertools import permutations

def solution(n, weak, dist):
    INF = 987654321
    answer = INF
    weak_point = weak + [w + n for w in weak]
    L = len(weak)

    # 시작점
    for (idx, start) in enumerate(weak):
        # 가능한 모든 케이스의 순열
        for p in permutations(dist):
            count = 1
            pos = start
            for d in p:
                pos += d
                if pos >= weak_point[idx + L - 1]:
                    answer = min(answer, count)
                else:
                    pos = [w for w in weak_point if w > pos][0]
                    count += 1

    return -1 if answer == INF else answer

#------------------------------------------------------------------------------------

def solution2(n, weak, dist):
    answer = 0
    wall = [0] * n
    for i in range(len(wall)):
        if i in weak:
            wall[i] = 1
    print(wall)

    check_list = []
    for i in dist:
        k = 0
        while k < len(wall):
            j = k + i
            if j >= len(wall):
                j = k - len(wall) + i
            if sum(wall[k:j + 1]) == 2:
                check_list.append(i)
                break
            k += 1
        print(k)

    print(check_list)

    return answer

#------------------------------------------------------------------------------------

def solution3(n, weak, dist):
    answer = 0
    for i in range(len(weak)):
        weak.append(weak[i] + n)
    print(weak)

    return answer
