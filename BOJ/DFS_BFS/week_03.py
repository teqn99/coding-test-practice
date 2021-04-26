import sys
from collections import deque

N, M = map(int, input().split())
maze = [input() for i in range(N)]

def solution(N, M, maze):
    maze = list(map(lambda x: list(x), maze))
    dist = [[-1]*M for i in range(N)]  # 방문 여부를 확인하기 위해 -1로 초기화

    # 상하좌우
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = deque()
    q.append((0, 0))
    dist[0][0] = 0  # (0, 0)은 출발점이므로 출발점에서부터 거리는 0으로 시작
    cnt = 0

    while q:
        curr = q.popleft()  # (0, 0)
        for i in range(4):
            nx = curr[0] + dx[i]
            ny = curr[1] + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if dist[nx][ny] < 0 and maze[nx][ny] == '1':  # 방문하지 않았고, maze의 값이 1이라 갈 수 있는 곳이라면
                    dist[nx][ny] = dist[curr[0]][curr[1]] + 1
                    q.append((nx, ny))

    cnt = dist[N-1][M-1] + 1
    return cnt


