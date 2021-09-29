for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num = []
    for i in range(N):
        num.append(input())
    num_list = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    for i in range(N):
        code = ''
        j = M
        while j > 0:
            temp = num[i][j:j-7:-1][::-1]
            if temp in num_list:
                code += str(num_list.index(temp))
                j -= 7
                continue
            j -= 1
        if code != '':
            break

    code = code[::-1]
    sum_hol = 0
    sum_jjak = 0
    for i in range(len(code)):
        if i%2 == 0:
            sum_hol += int(code[i])
        else:
            sum_jjak += int(code[i])

    result = sum_hol*3 + sum_jjak
    if result % 10 == 0:
        print(f'#{tc} {sum(map(int, list(code)))}')
    else:
        print(f'#{tc} 0')