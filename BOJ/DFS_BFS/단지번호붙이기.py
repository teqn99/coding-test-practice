def dfs(i, j):
    global cnt
    apart[i][j] = 0
    cnt += 1
    for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and apart[ni][nj] == 1:
            dfs(ni, nj)


N = int(input())
apart = [list(map(int, list(input()))) for _ in range(N)]
result_list = []
result = 0
for i in range(N):
    for j in range(N):
        if apart[i][j] == 0:
            continue
        cnt = 0
        dfs(i, j)
        result += 1
        result_list.append(cnt)
result_list.sort()
print(result)
for i in result_list:
    print(i)