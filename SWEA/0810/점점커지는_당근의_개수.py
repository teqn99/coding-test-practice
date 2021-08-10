T = int(input())
for tc in range(T):
    N = int(input())
    carrots = list(map(int, input().split()))
    long_list = []
    long = 1
    for i in range(N):
        if i < N-1:
            if carrots[i] < carrots[i+1]:
                long += 1
            else:
                long_list.append(long)
                long = 1
        else:
            long_list.append(long)
    result = 0
    for i in range(len(long_list)):
        if result < long_list[i]:
            result = long_list[i]
    print(f'#{tc+1} {result}')