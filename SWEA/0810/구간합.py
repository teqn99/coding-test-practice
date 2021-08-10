T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    maxi, mini = 0, 1000000
    for i in range(N-M+1):
        temp =  sum(num_list[i:i+M])
        if maxi < temp:
            maxi = temp
        if mini > temp:
            mini = temp
    print(f'#{tc+1} {maxi-mini}')