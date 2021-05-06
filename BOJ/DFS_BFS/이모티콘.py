"""
1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
3. 화면에 있는 이모티콘 중 하나를 삭제한다.
모든 연산은 1초가 걸린다.
"""
# from collections import deque
#
# S = int(input())
# clipboard = 0
#
# q = deque()
# q.append((1, 0))
#
# while q:
#     smile, time = q.popleft()
#     if smile == S:
#         break
#
#     time += 1
#
#     if clipboard > 0:
#         q.append((clipboard+smile, time))  # 2번 연산
#     clipboard = smile  # 1번 연산
#     q.append((clipboard, time))
#     if smile > 0:
#         q.append((smile-1, time))  # 3번 연산
#
# print(time)

"""
풀이 2
"""
from collections import deque

N = int(input())
time = dict()
time[(1, 0)] = 0

q = deque()
q.append((1, 0))  # screen, clipboard

while q:
    s, c = q.popleft()
    if s == N:
        print(time[(s, c)])
        break

    if (s, s) not in time:
        time[(s, s)] = time[(s, c)] + 1
        q.append((s, s))  # 1

    if (s+c, c) not in time and s+c <= N:
        time[(s+c, c)] = time[(s, c)] + 1
        q.append((s+c, c))  # 2

    if (s-1, c) not in time and s-1 > 0:
        time[(s-1, c)] = time[(s, c)] + 1
        q.append((s-1, c))  # 3
