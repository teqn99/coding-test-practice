T = int(input())
for tc in range(T):
    A, B = input().split()
    idx, cnt = 0, 0

    while idx > -1:
        idx = A.find(B, idx)
        if idx > -1:
            cnt += 1
            idx += len(B)

    cnt += len(A)
    cnt -= A.count(B)*len(B)

    print(f'#{tc+1} {cnt}')
