from collections import deque

N, K = map(int, input().split())
visited = [[-1, 0] for _ in range(100001)]
q = deque()
q.append(N)

visited[N][0] = 0
visited[N][1] = 1

while q:
    x = q.popleft()
    for num in (x + 1, x - 1, x * 2):
        if 0 <= num <= 100000:
            if visited[num][0] == -1:
                visited[num][0] = visited[x][0] + 1
                visited[num][1] = visited[x][1]
                q.append(num)
            elif visited[num][0] == visited[x][0] + 1:
                visited[num][1] += visited[x][1]

print(visited[K][0])
print(visited[K][1])