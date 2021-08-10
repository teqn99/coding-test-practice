T = int(input())
for tc in range(T):
    N = int(input())
    carrots = list(map(int, input().split()))
    maxi, maxi_idx = 0, 0
    for i in range(N):
        if maxi < carrots[i]:
            maxi = carrots[i]
            maxi_idx = i
    print(f'#{tc+1} {maxi_idx+1} {maxi}')