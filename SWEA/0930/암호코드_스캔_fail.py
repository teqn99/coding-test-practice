import sys
sys.stdin = open('1.txt', 'r')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num = []
    for i in range(N):
        num.append(list(input().strip()))
    num_list = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

    for i in range(N):
        if num[i] == ['0']*M:
            num[i] = []
            continue
        for j in range(M):
            temp = str(bin(int(num[i][j], 16))[2:])
            while len(temp) < 4:
                temp = '0' + temp
            num[i][j] = temp
        num[i] = ''.join(num[i])

    code_list = []
    for i in range(N):
        if num[i] == []:
            continue
        long = len(num[i])
        idx = 1
        while long >= idx*56:
            code = ''
            end = num[i].rindex('1')
            start = end - 56*idx + 1
            if start < 0:
                break
            for j in range(8):
                if j == 0:
                    temp = num[i][start:start + 7*idx:idx]
                else:
                    temp = num[i][start + (7*idx*j):start + (7*idx*j) + 7*idx:idx]
                if temp in num_list:
                    code += str(num_list.index(temp))
            if len(code) == 8:
                code_list.append(code)

            if '1' in num[i][:start]:
                long_a = len(num[i][:start])
                idx_a = 1
                start_a = start
                while long_a >= idx_a * 56:
                    code = ''
                    end_a = num[i][:start_a].rindex('1')
                    start_a = end_a - 56 * idx_a + 1
                    if start_a < 0:
                        break
                    for j in range(8):
                        if j == 0:
                            temp = num[i][start_a:start_a + 7 * idx_a:idx_a]
                        else:
                            temp = num[i][start_a + (7 * idx_a * j):start_a + (7 * idx_a * j) + 7 * idx_a:idx_a]
                        if temp in num_list:
                            code += str(num_list.index(temp))
                    if len(code) == 8:
                        code_list.append(code)
                    idx_a += 1
                    if '1' not in num[i][:start_a]:
                        break
            idx += 1

    code_list = list(set(code_list))
    all_result = 0
    for i in range(len(code_list)):
        sum_hol = 0
        sum_jjak = 0
        for k in range(len(code_list[i])):
            if k % 2 == 0:
                sum_hol += int(code_list[i][k])
            else:
                sum_jjak += int(code_list[i][k])
        result = sum_hol*3 + sum_jjak
        if result % 10 == 0:
            all_result += sum(map(int, list(code_list[i])))
        else:
            continue

    print(f'#{tc} {all_result}')