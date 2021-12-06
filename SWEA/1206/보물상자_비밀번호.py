for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    cnt = N // 4
    num = input()
    result_list = set()

    i = cnt
    while i:
        i -= 1
        numbers = [num[:cnt], num[cnt:2 * cnt], num[2 * cnt:3 * cnt], num[3 * cnt:4 * cnt]]
        num = num[-1] + num[:-1]
        for idx in range(len(numbers)):
            result_list.add(numbers[idx])
    result_list = sorted(list(result_list), reverse=True)

    result = 0
    hex_dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    l = len(result_list[K-1])
    for n in range(l):
        result += 16 ** (l-n-1) * hex_dic[result_list[K-1][n]]
    print(f'#{tc} {result}')