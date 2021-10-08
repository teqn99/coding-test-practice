for tc in range(1, int(input())+1):
    won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result_list = [0, 0, 0, 0, 0, 0, 0, 0]
    N = int(input())

    i = 0
    while i < 8:
        if N >= won[i]:
            N -= won[i]
            result_list[i] += 1
        if N < won[i]:
            i += 1

    print(f'#{tc}')
    for i in result_list:
        print(i, end=' ')
    print()