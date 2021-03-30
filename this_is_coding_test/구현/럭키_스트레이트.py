n = list(input())
left = []
right = []

for i in range(len(n)):
    if i < len(n) // 2:
        left.append(n[i])
    else:
        right.append(n[i])

left = list(map(int, left))
right = list(map(int, right))

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')