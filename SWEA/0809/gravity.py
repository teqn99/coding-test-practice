T = int(input())
for tx in range(1, T+1):
    max_v = 0
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        count = 0
        for j in range(i+1, N):
            if A[i] > A[j]:
                count += 1
        if max_v < count:
            max_v = count
    print(f'#{tx} {max_v}')