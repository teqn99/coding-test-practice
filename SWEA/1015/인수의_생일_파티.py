from collections import deque


def bfs(start, adjM):
    dist = [987654321]*(N+1)
    dist[start] = 0
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        for i in range(1, N+1):
            if adjM[a][i] == 0:
                continue
            tmp = dist[a] + adjM[a][i]
            if tmp < dist[i]:
                dist[i] = tmp
                q.append(i)
    return dist


for tc in range(1, int(input())+1):
    N, M, X = map(int, input().split())
    home = [[0]*(N+1) for _ in range(N+1)]
    back = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        x, y, c = map(int, input().split())
        home[x][y] = c
        back[y][x] = c

    g = bfs(X, back)    # go to X
    b = bfs(X, home)    # go back to home
    # go가 back adjM을 사용하고, back이 home adjM을 사용했다.
    # -> 원래 생각대로라면 for i in range(1, N+1)을 통해 bfs(i, home)등을 사용해야 하지만, 시간 초과 발생
    # -> 그래서 반대로 생각해보았다. -> X부터 출발해서 반대로 생각해보면 모든 경우의 최단 시간을 찾을 수 있을 것

    maxV = 0
    for i in range(len(g)):
        for j in range(len(b)):
            if i == j and i > 0:
                if maxV < g[i]+b[j]:
                    maxV = g[i]+b[j]
    print(f'#{tc} {maxV}')