T = int(input())
for tc in range(T):
    N = int(input())
    card = list(input().split())
    if N % 2:  # N이 홀수인 경우
        one = card[ :N//2 + 1]
        two = card[N//2 + 1: ]
    else:
        one = card[ : N//2]
        two = card[N//2 : ]

    result = []
    for i in range(1, N+1):
        if one and i % 2:
            result.append(one.pop(0))
        elif two and not i % 2:
            result.append(two.pop(0))

    print('#{}'.format(tc+1), end=' ')
    for i in range(N):
        print(result[i], end=' ')
    print()