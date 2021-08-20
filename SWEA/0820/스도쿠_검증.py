T = int(input())
for tc in range(T):
    sudoku = []
    result = 1
    for i in range(9):
        sudoku.append(list(map(int, input().split())))
    sudoku_T = [list(x) for x in zip(*sudoku)]  # transpose

    # 정방향 스도쿠
    for i in range(9):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            try:
                num.remove(sudoku[i][j])
            except:
                result = 0
                break
        if len(num) > 0:
            result = 0
            break

    # 전치된 스도쿠
    for i in range(9):
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9):
            try:
                num.remove(sudoku_T[i][j])
            except:
                result = 0
                break
        if len(num) > 0:
            result = 0
            break

    # 3*3 사이즈 정사각행렬 스도쿠
    for i in [3, 6, 9]:
        arr = sudoku[i-3:i]
        for j in [3, 6, 9]:
            num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for k in range(3, 0, -1):
                try:
                    num.remove(arr[0][j-k])
                    num.remove(arr[1][j-k])
                    num.remove(arr[2][j-k])
                except:
                    result = 0
                    break
            if len(num) > 0:
                result = 0
                break

    print(f'#{tc+1} {result}')