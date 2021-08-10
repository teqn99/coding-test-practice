T = int(input())
for tc in range(T):
    N = int(input())
    carrots = list(map(int, input().split()))
    min_sum = dict()
    for i in range(1, N):
        sum_a, sum_b = 0, 0
        for j in range(i):
            sum_a += carrots[j]
        for k in range(i, N):
            sum_b += carrots[k]
        min_sum[i] = abs(sum_a - sum_b)
    min_sum = dict(sorted(min_sum.items(), key=lambda x: x[1]))

    print(f'#{tc+1} {list(min_sum.keys())[0]} {list(min_sum.values())[0]}')