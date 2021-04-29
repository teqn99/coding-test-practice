import copy

N, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
time = 0
compare_mat = copy.deepcopy(matrix)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while time != S:
    for i in range(N):
        for j in range(N):
            virus = matrix[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if matrix[nx][ny] == 0 and compare_mat[nx][ny] == 0:
                        compare_mat[nx][ny] = virus
    matrix = copy.deepcopy(compare_mat)
    time += 1

print(matrix[X-1][Y-1])

#-------------------------------------------------------------------------

from collections import deque

n, k = map(int, input().split())
test = []  # 전체 맵 정보 담는 리스트
data = []  # 바이러스 정보를 담는 리스트
for i in range(n):
    test.append(list(map(int, input().split())))
    for j in range(n):
        if test[i][j] != 0:
            data.append((test[i][j], i, j, 0))  # 바이러스 숫자, x위치, y위치, 시간을 입력
S, X, Y = map(int, input().split())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()  # 바이러스는 번호가 낮은 바이러스부터 증식
q = deque(data)

while q:
    virus, x, y, time = q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if test[nx][ny] == 0:
                test[nx][ny] = virus
                q.append((virus, nx, ny, time+1))

print(test[X-1][Y-1])