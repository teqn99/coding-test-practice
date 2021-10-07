def binary_search(num, left, right, flag):
    if left > right:  # 못찾고 끝까지 간 경우
        return 0
    mid = (left + right) // 2
    if A[mid] == num:  # 찾은 경우
        return 1
    elif A[mid] > num:  # 왼쪽 부분의 경우
        if flag == 1:
            return 0
        return binary_search(num, left, mid - 1, 1)
    elif A[mid] < num:  # 오른쪽 부분의 경우
        if flag == 2:
            return 0
        return binary_search(num, mid + 1, right, 2)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    ans = 0

    for num in B:
        if num in A:
            ans += binary_search(num, 0, N-1, 0)

    print(f'#{tc} {ans}')