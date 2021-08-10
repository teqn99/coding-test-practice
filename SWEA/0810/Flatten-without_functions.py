N = 100
for tc in range(10):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while dump:
        maxi, maxi_idx = 0, 0
        mini, mini_idx = 100, 0
        for i in range(N):
            if maxi < boxes[i]:
                maxi = boxes[i]
                maxi_idx = i
            if mini > boxes[i]:
                mini = boxes[i]
                mini_idx = i

        boxes[maxi_idx] -= 1
        boxes[mini_idx] += 1

        dump -= 1

    maxi, mini = 0, 100
    for i in range(N):
        if maxi < boxes[i]:
            maxi = boxes[i]
        if mini > boxes[i]:
            mini = boxes[i]

    print(f'#{tc+1} {maxi-mini}')
