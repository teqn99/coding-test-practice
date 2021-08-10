T = int(input())
for tc in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    maxi, mini = num_list[0], num_list[0]
    for i in range(N):
        if num_list[i] > maxi:
            maxi = num_list[i]
        if num_list[i] < mini:
            mini = num_list[i]
    print(f'#{tc+1} {maxi-mini}')