T = int(input())
for tc in range(T):
    P, A, B = map(int, input().split())
    A_cnt, B_cnt = 0, 0

    # A의 탐색 경우
    l, r = 1, P
    while 1:
        A_cnt += 1
        c = (l+r)//2
        if c == A:
            break
        else:
            if A > c:
                l = c
            else:
                r = c

    # B의 탐색 경우
    l, r = 1, P
    while 1:
        B_cnt += 1
        c = (l+r)//2
        if c == B:
            break
        else:
            if B > c:
                l = c
            else:
                r = c

    if A_cnt < B_cnt:
        print(f'#{tc+1} A')
    elif A_cnt == B_cnt:
        print(f'#{tc + 1} 0')
    else:
        print(f'#{tc + 1} B')