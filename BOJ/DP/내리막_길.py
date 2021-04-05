import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]  # up, down, 0, 0
dy = [0, 0, 1, -1]  # 0, 0, right, left

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1  # 마지막 지점에 도착한 경우
    if c[x][y] != -1:
        return c[x][y]  # 이미 지나간 지점이라면, 그 지점의 자리에 이미 마지막 지점까지 도달하는 경우의 수가 저장되어 있으므로, 끝까지 가보지 않고 이를 이용한다.
    c[x][y] = 0  # 지나간 지점이라는 체크 표시
    for i in range(4):  # 상,하,좌,우 -> 총 4번 (= len(dx) or = len(dy))
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if a[nx][ny] < a[x][y]:  # 숫자가 더 작은 길로만 갈 수 있으므로 현재 위치보다 작은 값인 경우에만 다음 dfs를 수행한다.
                c[x][y] += dfs(nx, ny)
    return c[x][y]

m, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
c = [[-1]*n for _ in range(m)]
print(a)
print(c)
print(dfs(0, 0))

#------------------------------------------------------------------------

