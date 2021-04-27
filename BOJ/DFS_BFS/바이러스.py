from collections import deque

n = int(input())  # 컴퓨터 개수
m = int(input())  # 연결된 컴퓨터의 쌍의 수
matrix = [[] for _ in range(n+1)]
visited = [0]*(n+1)
visited[1] = 1
for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)

q = deque([1])
while q:
    x = q.popleft()
    for i in range(len(matrix[x])):
        if visited[matrix[x][i]] == 0:
            visited[matrix[x][i]] = 1
            q.append(matrix[x][i])

print(sum(visited)-1)