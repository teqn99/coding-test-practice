for tc in range(int(input())):
    N, hex = input().split()
    result = ''

    for i in range(int(N)):
        temp = str(bin(int(hex[i], 16)))
        a = len(temp[2:])
        while a < 4:
            a += 1
            result += '0'
        result += temp[2:]

    print(f'#{tc+1} {result}')
