from collections import deque

A, B = map(int, input().split())
check = 0

q = deque()
q.append([A, 1])
while q:
    x, y = q.popleft()
    if x == B:
        break
    elif x > B:
        if len(q) == 0:
            check = -1
            break
        continue
    else:
        y += 1
        q.append([x*2, y])
        q.append([x*10 + 1, y])

if check == -1:
    print(-1)
else:
    print(y)