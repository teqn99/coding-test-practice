from itertools import permutations

N = int(input())
num_list = list(map(int, input().split()))
cal = list(map(int, input().split()))
result_list = []
product_list = []
check = 0

for i, v in enumerate(cal):
    if v == 0:
        continue
    if i == 0:  # +
        for _ in range(v):
            product_list.append('+')
    elif i == 1:  # -
        for _ in range(v):
            product_list.append('-')
    elif i == 2:  # *
        for _ in range(v):
            product_list.append('*')
    elif i == 3:  # //
        for _ in range(v):
            product_list.append('//')

cal_list = list(permutations(product_list, N-1))  # 구성할 수 있는 모든 경우의 수

for j in range(len(cal_list)):  # 계산 과정
    result = num_list[0]
    for i in range(1, N):
        if cal_list[j][i-1] == '+':
            result += num_list[i]

        elif cal_list[j][i-1] == '-':
            result -= num_list[i]

        elif cal_list[j][i-1] == '*':
            result *= num_list[i]

        elif cal_list[j][i-1] == '//':
            if result < 0 or num_list[i] < 0:
                if result < 0:
                    check = 1
                    result *= (-1)
            result //= num_list[i]
            if check == 1:
                result *= (-1)
                check = 0
    result_list.append(result)

print(max(result_list))
print(min(result_list))