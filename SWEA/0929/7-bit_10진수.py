T = int(input())
for tc in range(T):
    arr = list(map(int, input()))
    result_list = []

    # 7개씩 잘라 b6 ~ b0으로 사용
    for i in range(1, len(arr)+1, 7):
        result = 0
        for j in range(i+6, i-1, -1):
            if j%7 == 0:
                result += int(arr[j-1])*1
            else:
                result += int(arr[j-1])*(2**(7 - j%7))
        result_list.append(result)

    print(f'#{tc+1}', end=' ')
    for i in range(len(result_list)):
        print(result_list[i], end=' ')
    print()


# 다른 풀이
for tc in range(1, int(input()) + 1):
    num = input()
    answer = []

    for i in range(0, len(num), 7):

        decimal = 0
        binary = list(map(int, num[i:i + 7]))

        for j in range(7):
            decimal += binary.pop() * (2 ** j)

        answer.append(str(decimal))

    print(f'#{tc}', *answer)
