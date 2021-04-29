# import copy
#
# N, K = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(N)]
# S, X, Y = map(int, input().split())
# time = 0
# compare_mat = copy.deepcopy(matrix)
#
# # 상, 하, 좌, 우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# while time < S:
#     for i in range(N):
#         for j in range(N):
#             virus = matrix[i][j]
#             for k in range(4):
#                 nx = i + dx[k]
#                 ny = j + dy[k]
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if matrix[nx][ny] == 0 and compare_mat[nx][ny] == 0:
#                         compare_mat[nx][ny] = virus
#     matrix = copy.deepcopy(compare_mat)
#     time += 1
#
# print(matrix)
# print(matrix[X-1][Y-1])
# 이 경우는 바이러스가 번호순으로 증식하지 않을 수 있다... -> 틀린 경우
# 바이러스가 번호순으로 증식하는 방법을 적용해야 한다.
#-------------------------------------------------------------------------

from collections import deque

N, K = map(int, input().split())
matrix = []  # 전체 맵 정보 담는 리스트
data = []  # 바이러스 정보를 담는 리스트
for i in range(N):
    matrix.append(list(map(int, input().split())))
    for j in range(N):
        if matrix[i][j] != 0:
            data.append((matrix[i][j], i, j, 0))  # 바이러스 숫자, x위치, y위치, 시간을 입력
S, X, Y = map(int, input().split())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()  # 바이러스는 번호가 낮은 바이러스부터 증식 - while문에서는 이미 정렬해준 순으로 돌기 때문에 sort는 여기서만 필요
q = deque(data)
while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] == 0:
                matrix[nx][ny] = virus
                q.append((virus, nx, ny, time+1))  # q가 한바퀴 돌아야 차례가 오므로 1초가 지나는 경우이다.

print(matrix[X-1][Y-1])