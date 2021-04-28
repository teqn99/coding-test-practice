from collections import deque

N, K = map(int, input().split())
visited = [False for _ in range(100001)]

q = deque()
q.append([N, 0])
visited[N] = True

while q:
    x, y = q.popleft()  # y값은 시간을 나타낼 것
    if x == K:
        break
    if 0 <= x*2 <= 100000 and visited[x*2] == False:  # 순간이동의 경우
        q.append([x*2, y])
        visited[x*2] = True
    for num in (x+1, x-1):
        if 0 <= num <= 100000 and visited[num] == False:  # 걷기의 경우
            q.append([num, y+1])
            visited[num] = True

print(y)

#------------------------------------------------------------------------
# 왜 위에건 안되고 아래건 되는지 생각해보기
#------------------------------------------------------------------------

q = deque()
check = [False]*100001
dist = [-1]*100001

N, K = map(int, input().split())
q.append(N)

dist[N] = 0
check[N] = True

while q:
    x = q.popleft()
    if x == K:
        break
    if x*2 <= 100000 and check[x*2] is False:  # 순간이동의 경우
        q.appendleft(x*2)  # appendleft보다 append를 쓰는 게 시간은 더 빠르다. 그러나 메모리는 더 쓰게 된다.
        dist[x*2] = dist[x]  # 시간
        check[x*2] = True  # 방문
    for num in (x-1, x+1):  # 걷기의 경우
        if 0 <= num <= 100000 and check[num] is False:
            q.append(num)
            dist[num] = dist[x] + 1  # 시간
            check[num] = True  # 방문

print(dist[K])