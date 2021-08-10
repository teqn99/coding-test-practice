T = int(input())
for tc in range(T):
    N = int(input())
    ones = list(map(int, input()))
    long_list = []
    long = 0
    for i in range(N):
        if ones[i] == 1:
            long += 1
            if i == N-1:
                long_list.append(long)
        else:
            long_list.append(long)
            long = 0
    print(long_list)
    result = 0
    for i in range(len(long_list)):
        if result < long_list[i]:
            result = long_list[i]
    print(f'#{tc+1} {result}')