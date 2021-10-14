from collections import deque

yeonsan = [1, 1, 2, 10]


def bfs(c, N, M):
    global minV
    q = deque()
    q.append((c, N))
    while q:
        cnt, now = q.popleft()
        if now == M:
            if cnt < minV:
                minV = cnt
            return
        for y in range(4):
            if y == 0:
                tmp = now + yeonsan[y]
            elif y == 1 or y == 3:
                tmp = now - yeonsan[y]
            elif y == 2:
                tmp = now * yeonsan[y]
            if 0 < tmp <= 1000000 and visited[tmp] == 0:
                q.append((cnt+1, tmp))
                visited[tmp] = 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    visited = [0]*1000001
    minV = 987654321
    bfs(0, N, M)
    print(f'#{tc} {minV}')