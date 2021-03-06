"""
8
0 0 1 1 1 1 1 1
1 0 0 0 0 0 0 1
1 1 1 0 1 1 1 1
1 1 1 0 1 1 1 1
1 0 0 0 0 0 0 1
1 0 1 1 1 1 1 1
1 0 0 0 0 0 0 0
1 1 1 1 1 1 1 0
"""
def f1(i, j, N):
    """
    모든 칸을 방문하는 탐색
    """
    maze[i][j] = 1  # i, j 방문 표시. (진입한 칸을 벽으로 변경)
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
        ni, nj = i + di, j + dj
        # 탐색 방향이 통로이면
        if 0 <= ni < N and 0 <= nj < N and maze[ni][nj]==0:
            f1(ni, nj, N)


def f2(i, j, N):
    """
    출구를 찾으면 중단
    """
    if i == N-1 and j == N-1:  # 출구에 도착한 경우
        return 1
    else:
        maze[i][j] = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:
                if f2(ni, nj, N):  # 출구를 찾고 리턴하면
                    return 1  # 입구까지 리턴 (남겨둔 갈림길을 탐색하지 않는다.)
        return 0  # 탐색 방향에서 출구를 찾지 못한 경우


def f3(i, j ,N):
    """
    입구 -> 출구 경로의 갯수 찾기
    """
    global cnt
    if i == N-1 and j == N-1:
        cnt += 1
        return
    else:
        maze[i][j] = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:
                f3(ni, nj, N)  # 출구를 찾고 리턴하면
        maze[i][j] = 0  # 다른 경로에서의 i, j 진입은 허용


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
f1(0, 0, N)  # 탐색 시작 위치: (0, 0), 미로의 크기: N
print(maze[N-1][N-1])


def f4(i, j, N, c):
    """
    c: 지나온 칸의 개수
    최단거리 찾기 -> 모든 경로를 탐색
    """
    global minV
    if i == N-1 and j == N-1:
        if minV > c+1:  # 기존 경로보다 도착지 포함 경로의 길이가 더 짧으면
            minV = c+1  # c+1: 출발, 도착을 포함한 경로의 길이
        return
    else:
        maze[i][j] = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # 4방향 탐색
            ni, nj = i + di, j + dj
            # 탐색 방향이 통로이면
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] == 0:
                f4(ni, nj, N, c+1)  # 출구를 찾고 리턴하면
        maze[i][j] = 0  # 다른 경로에서의 i, j 진입은 허용


N = int(input())
maze = [list(map(int, input().split())) for _ in range(N)]
minV = N*N
f4(0, 0, N, 0)  # 탐색 시작 위치: (0, 0), 미로의 크기: N
if minV == N*N:  # 경로가 없는 경우
    print(-1)
else:
    print(minV)