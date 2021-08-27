def in_order(n):
    if n:
        in_order(left[n])
        print(node[n], end='')
        in_order(right[n])


for tc in range(10):
    N = int(input())
    node = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        lst = list(input().split())
        node[int(lst[0])] = lst[1]
        if len(lst) >= 3:
            left[int(lst[0])] = int(lst[2])
            if len(lst) == 4:
                right[int(lst[0])] = int(lst[3])

    print(f'#{tc+1}', end=' ')
    in_order(1)
    print()
