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


# 다른 풀이
code_dic = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}


def validate(n):
    temp = 0
    check = 0
    for i, x in enumerate(n):
        ix = int(x)
        temp += ix
        if i % 2:
            check += ix
            if i == 7:
                return temp if not check % 10 else 0
        else:
            check += ix * 3


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    codes = [input() for _ in range(N)]

    for i in range(N):
        if '1' in codes[i]:  # 유효한 코드가 포함되어 있으면
            j = codes[i].rindex('1')
            code_bin = codes[i][j - 55:j + 1]
            break

    code = ''
    for i in range(8):  # 10진수로 변환
        code += code_dic[code_bin[i * 7:i * 7 + 7]]

    print(f'#{tc} {validate(code)}')
