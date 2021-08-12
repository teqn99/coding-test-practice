T = int(input())
for tc in range(T):
    N = int(input())  # 칠할 영역의 개수
    colors = [[0]*10 for _ in range(10)]  # 칠할 영역
    input_list = []
    for i in range(N):
        input_list.append(list(map(int, input().split())))  # 입력

    for i in range(N):
        # x, y의 범위
        x1, y1 = input_list[i][0], input_list[i][1]
        x2, y2 = input_list[i][2], input_list[i][3]
        for j in range(10):
            for k in range(10):
                # 범위안에 들어오면 colors에 color_number를 더해주기
                if j >= x1 and j <= x2 and k >= y1 and k <=y2:
                    colors[j][k] += input_list[i][4]

    result = 0
    for i in range(10):
        for j in range(10):
            # 보라색인 영역은 합이 3인 영역이므로 3인 영역의 개수를 구함.
            if colors[i][j] == 3:
                result += 1

    print(f'#{tc+1} {result}')