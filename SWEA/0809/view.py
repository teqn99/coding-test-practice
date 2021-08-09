for c in range(10):
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    for i in range(2, N-2):
        if A[i] > A[i-1] and A[i] > A[i-2] and A[i] > A[i+1] and A[i] > A[i+2]:
            cnt += A[i]-max(A[i-1], A[i-2], A[i+1], A[i+2])

    print(f'#{c+1} {cnt}')