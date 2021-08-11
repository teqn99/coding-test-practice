for tc in range(10):
    N = int(input())
    num_list = []
    for i in range(100):
        num_list.append(list(map(int, input().split())))

    result_list = []
    result_c, result_r = 0, 0  # result_c: 왼위-오아래-대각선, result_r: 오위-왼아래-대각선
    for i in range(100):
        result_i, result_j = 0, 0  # result_i: 가로줄 합, result_j: 세로줄 합
        for j in range(100):
            result_i += num_list[i][j]
            result_j += num_list[j][i]
            if i == j:
                result_c += num_list[i][j]
            if i == 99 - j:
                result_r += num_list[i][j]
        result_list.append(result_i)
        result_list.append(result_j)
    result_list.append(result_c)
    result_list.append(result_r)

    result = 0
    for i in result_list:
        if result < i:
            result = i

    print(f'#{N} {result}')