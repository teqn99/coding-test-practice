# def f(i, j, N, M, c):
#     global minV
#     if park[i][j] == 'L':
#         if minV > c:
#             minV = c
#         return
#     else:
#         park[i][j] = 'N'
#         for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#             ni, nj = i + di, j + dj
#             if 0 <= ni < N and 0 <= nj < M and park[ni][nj] in 'L':
#                 f(ni, nj, N, M, c+1)
#         park[i][j] = 'L'
#
#
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     park = []
#     for i in range(N):
#         park.append(list(input()))
#
#     distances = []
#     for i in range(N):
#         for j in range(M):
#             if park[i][j] == 'W':
#                 minV = N*M
#                 f(i, j, N, M, 0)
#                 distances.append(minV)
#
#     print(f'#{tc+1} {sum(distances)}')


# --------------------------------
from collections import deque  # deque 안쓰고 q를 리스트로 사용하면 시간초과,,,


def bfs(N, M):
    while q:
        x, y = q.popleft()
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] != -1:  # W이거나, 이미 지나간 길인 경우
                continue
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:  # L이면서, 지나지 않은 경우
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1  # 누적으로 거리 계산


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    visited = [[-1] * M for _ in range(N)]
    park = []
    q = deque()
    for i in range(N):
        park.append(input())
        for j in range(M):
            if park[i][j] == 'W':  # W에서부터 출발하여 각 L로의 거리를 찾는 방법이 더 간편
                q.append((i, j))
                visited[i][j] = 0

    bfs(N, M)
    
    result = 0
    for i in range(N):
        for j in range(M):
            result += visited[i][j]  # W는 어차피 0이기 때문
            
    print(f'#{tc+1} {result}')


# -----------------------------------------------------------------
from collections import deque  # deque 안쓰고 q를 리스트로 사용하면 시간초과,,,


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    visited = [[-1]*M for _ in range(N)]
    park = []
    q = deque()
    for i in range(N):
        park.append(input())
        for j in range(M):
            if park[i][j] == 'W':  # W에서부터 출발하여 각 L로의 거리를 찾는 방법이 더 간편
                q.append((i, j))
                visited[i][j] = 0

    result = 0
    while q:
        x, y = q.popleft()
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            nx, ny = x + di, y + dj
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:  # L이면서, 지나지 않은 경우
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1  # 누적으로 거리 계산
                result += visited[nx][ny]

    print(f'#{tc+1} {result}')