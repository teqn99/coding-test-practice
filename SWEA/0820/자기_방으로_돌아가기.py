T = int(input())
for tc in range(T):
    n = int(input())
    rooms = [0] * 400
    for i in range(n):
        a, b = map(int, input().split())
        start = (min(a, b) - 1) // 2
        end = (max(a, b) - 1) // 2

        for j in range(start, end + 1):
            rooms[j] += 1

    print(f'#{tc + 1} {max(rooms)}')