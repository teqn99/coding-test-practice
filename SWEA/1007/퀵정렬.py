def part(A, l, r):
    i, j = l, r
    x = A[l]
    while i <= j:
        while i <= j and A[i] <= x:
            i += 1
        while i <= j and A[j] >= x:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j


def quick_sort(A, l, r):
    if l < r:
        p = part(A, l, r)
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r)


for tc in range(1, int(input())+1):
    N = int(input())
    num = list(map(int, input().split()))
    quick_sort(num, 0, N-1)

    print(f'#{tc} {num[N//2]}')