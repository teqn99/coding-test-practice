N = 100
for tc in range(10):
    dump = int(input())
    boxes = list(map(int, input().split()))
    while dump:
        maxi = max(boxes)
        maxi_idx = boxes.index(maxi)

        mini = min(boxes)
        mini_idx = boxes.index(mini)

        boxes[maxi_idx] -= 1
        boxes[mini_idx] += 1

        dump -= 1

    print(f'#{tc+1} {max(boxes)-min(boxes)}')