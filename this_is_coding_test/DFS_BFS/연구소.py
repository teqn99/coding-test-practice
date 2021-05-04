"""
1. 3개의 추가 설치 벽을 만들 수 있는 경우 찾기
2. 위의 각 경우마다 바이러스 퍼뜨리기
3. 바이러스를 퍼뜨린 후, clean한 지역 갯수 세기
4. 계산된 값을 result_list에 추가
5. 모든 경우를 반복한 후, max(result_list)를 리턴
"""

import copy
from collections import deque

N, M = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
result_list = []


def spread(mapp, n, m):  # 0인 지역에 바이러스를 퍼뜨리는 방법
    q = deque()
    copy_list = copy.deepcopy(mapp)

    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if copy_list[i][j] == 2:  # 바이러스는 2에서부터 퍼져나가므로
                q.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if copy_list[nx][ny] == 0:
                    copy_list[nx][ny] = 2
                    q.append([nx, ny])

    cnt = 0
    for i in copy_list:
        cnt += i.count(0)  # clean한 0인 지역 갯수 세기

    return cnt


def wall(x, mapp, res, n, m):  # 추가로 설치할 수 있는 벽은 총 3개
    if x == 3:
        result = spread(mapp, n, m)
        res.append(result)
        return

    for i in range(n):
        for j in range(m):
            if mapp[i][j] == 0:
                mapp[i][j] = 1
                wall(x+1, mapp, res, n, m)
                mapp[i][j] = 0


wall(0, map_list, result_list, N, M)
print(result_list)
print(max(result_list))