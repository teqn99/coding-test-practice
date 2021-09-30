for tc in range(int(input())):
    N, M = map(int, input().split())
    M_bin = bin(M)
    a = len(M_bin[2:])
    result = ''
    while a < N:
        a += 1
        result += '0'
    result += M_bin[2:]

    if str(result)[-N:] == '1'*N:
        print(f'#{tc+1} ON')
    else:
        print(f'#{tc+1} OFF')
