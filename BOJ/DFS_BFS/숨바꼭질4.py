"""
메모리 초과
"""
# from collections import deque
# import copy
#
# N, K = map(int, input().split())
# q = deque()
# q.append((N, 0, [N]))
#
# while q:
#     x, y, z = q.popleft()
#     if x == K:
#         break
#     if 0 <= x <= 100000:
#         z_plus, z_minus, z_2 = copy.deepcopy(z), copy.deepcopy(z), copy.deepcopy(z)
#         z_plus.append(x+1)
#         z_minus.append(x-1)
#         z_2.append(2*x)
#
#         q.append((x+1, y+1, z_plus))
#         q.append((x-1, y+1, z_minus))
#         q.append((2*x, y+1, z_2))
#
# print(y)
# for i, v in enumerate(z):
#     if i != len(z)-1:
#         print(v, end=' ')
#     else:
#         print(v)

"""
방법 2
- 메모리 초과
"""
# from collections import deque
# import sys
# sys.setrecursionlimit(1000000000)
#
# N, K = map(int, input().split())
# MAX_SIZE = 100000
# log_path = [0]*(MAX_SIZE+1)
# visited = [0]*(MAX_SIZE+1)
#
# q = deque()
# q.append((N, 0))
# visited[N] = 1
#
# while q:
#     x, y = q.popleft()  # y: time
#     if x == K:
#         break
#     for curr in (x+1, x-1, 2*x):
#         if 0 <= curr <= 100000 and visited[curr] == 0:
#             q.append((curr, y+1))
#             visited[curr] = 1
#             log_path[curr] = x
#
# print(y)
#
# def print_recur(n, m):
#     if n != m:
#         print_recur(n, log_path[m])
#     print(m, end=' ')
# print_recur(N, K)

"""
방법 3
- 메모리 초과
"""
# from collections import deque
# import sys
# sys.setrecursionlimit(1000000000)
#
# N, K = map(int, input().split())
# MAX_SIZE = 100000
# log_path = [0]*(MAX_SIZE+1)
# visited = [0]*(MAX_SIZE+1)
# time = [0]*(MAX_SIZE+1)
#
# q = deque()
# q.append(N)
# visited[N] = 1
#
# while q:
#     x = q.popleft()
#     if x == K:
#         break
#     for curr in (x+1, x-1, 2*x):
#         if 0 <= curr <= 100000 and visited[curr] == 0:
#             q.append(curr)
#             time[curr] = time[x] + 1
#             visited[curr] = 1
#             log_path[curr] = x
#
# print(time[K])
# def print_recur(n, m):
#     if n != m:
#         print_recur(n, log_path[m])
#     print(m, end=' ')
# print_recur(N, K)

"""
방법 4
- 해결!!
"""
from collections import deque

N, K = map(int,input().split())
MAX_SIZE = 100000
visited = [0]*(MAX_SIZE+1)
path = [0]*(MAX_SIZE+1)

def solve(visited, n, k):
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(visited[x])
            p = []
            while x != n:
                p.append(x)
                x = path[x]
            p.append(n)
            p.reverse()
            print(' '.join(map(str, p)))
            return

        for curr in (x+1, x-1, x*2):
            if 0 <= curr < (MAX_SIZE+1) and visited[curr] == 0:
                visited[curr] = visited[x]+1
                path[curr] = x
                queue.append(curr)

solve(visited, N, K)