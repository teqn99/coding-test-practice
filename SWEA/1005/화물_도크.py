for tc in range(1, int(input())+1):
    N = int(input())
    time_list = [list(map(int, input().split())) for _ in range(N)]
    time_list.sort(key=lambda x: (x[1], x[0]))
    result_list = []

    for i in range(N):
        result = []
        for j in range(i, N):
            if j == i:
                result.append(time_list[j])
                continue
            if time_list[j][0] < result[-1][1]:
                continue
            result.append(time_list[j])
        result_list.append(result)

    maxV = 0
    for i in range(N):
        if maxV < len(result_list[i]):
            maxV = len(result_list[i])

    print(f'#{tc} {maxV}')