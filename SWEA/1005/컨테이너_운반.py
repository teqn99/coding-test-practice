for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))
    weights.sort(reverse=True)
    trucks = list(map(int, input().split()))
    trucks.sort(reverse=True)
    result = 0

    for i in range(N):
        if len(trucks) == 0:
            break
        if weights[i] <= trucks[0]:
            result += weights[i]
            trucks.pop(0)

    print(f'#{tc} {result}')
