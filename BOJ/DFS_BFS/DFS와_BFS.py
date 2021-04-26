from collections import deque
def dfs(v):
    print(v, end=" ")
    visited_dfs[v] = 1
    for i in range(1, n+1):
        if matrix[v][i] == 1 and visited_dfs[i] == 0:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    while q:
        x = q.popleft()
        if visited_bfs[x] == 0:
            visited_bfs[x] = 1
            print(x, end=" ")
            for i in range(1, n+1):
                if matrix[x][i] == 1 and visited_bfs[i] == 0:
                    q.append(i)


n, m, v = map(int, input().split())
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)
matrix = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

dfs(v)
print()
bfs(v)