T = int(input())
for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    # 버블정렬
    """
    for i : N-1 -> 1  # 구간 끝
        for j : 0 -> i-1  #비교할 왼쪽 원소
            if list[j] > list[j+1]:
                list[j] <-> list[j+1]
    list의 원소 출력
    """
    for i in range(N-1, 0, -1):
        for j in range(i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    print(f'#{tc + 1}', end=' ')
    for x in A:
        print(x, end=' ')
    print()