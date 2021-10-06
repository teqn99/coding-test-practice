import sys
sys.stdin = open('백만개.txt', 'r')


def lomuto(A, p, r):
    i = p-1
    x = A[r]
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def hoare(A, l, r):
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
        # p = hoare(A, l, r)  # 방법 1
        p = lomuto(A, l, r)  # 방법 2
        quick_sort(A, l, p-1)
        quick_sort(A, p+1, r)


def selection_sort(A, N):  # 선택 정렬
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if A[minIdx] > A[j]:
                minIdx = j
        A[i], A[minIdx] = A[minIdx], A[i]


A = list(map(int, input().split()))
quick_sort(A, 0, 999999)
# selection_sort(A, len(A))
print(A[500000])