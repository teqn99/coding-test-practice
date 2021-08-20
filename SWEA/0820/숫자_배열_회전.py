T = int(input())
for tc in range(T):
    N = int(input())
    arr = []
    result = [[] for _ in range(N)]
    for i in range(N):
        arr.append(list(map(int, input().split())))

    # 90도 회전의 경우
    for i in range(1, N+1):
        res = ''
        for j in range(1, N+1):
            res += str(arr[-j][i-1])
        result[i-1].append(res)

    # 180도 회전의 경우
    for i in range(1, N+1):
        res = ''
        for j in range(1, N+1):
            res += str(arr[-i][-j])
        result[i-1].append(res)

    # 270도 회전의 경우
    for i in range(1, N+1):
        res = ''
        for j in range(1, N+1):
            res += str(arr[j-1][-i])
        result[i-1].append(res)

    print(f'#{tc+1}')
    for i in range(N):
        print(' '.join(result[i]))
