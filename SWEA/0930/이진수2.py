for tc in range(int(input())):
    sosu = input()
    num = sosu[2:]
    a = len(num)
    result = ''

    while 1:
        num = str(int(num)*2)
        if len(num) > a:
            result += num[0]
            num = num[1:]
            if len(result) >= 13:
                result = 'overflow'
                break
        else:
            result += '0'

        if int(num) == 0:
            break

    print(f'#{tc+1} {result}')