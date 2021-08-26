for tc in range(10):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    # table 리스트를 transpose
    for i in range(N):
        for j in range(N):
            if i < j:
                table[i][j], table[j][i] = table[j][i], table[i][j]

    # transpose 해준 상태이기 때문에 j값을 기준으로 조건에 맞게 이동
    for i in range(N):
        for j in range(N):
            if j < N-1 and table[i][j] == 1 and table[i][j+1] == 0:
                table[i][j], table[i][j+1] = table[i][j+1], table[i][j]
            elif j == N-1 and table[i][j] == 1:
                table[i][j] = 0
            elif j > 0 and table[i][j] == 2 and table[i][j-1] == 0:
                table[i][j], table[i][j-1] = table[i][j-1], table[i][j]
            elif j == 0 and table[i][j] == 2:
                table[i][j] = 0

    # 마지막으로 순회하며 cnt값 검사
    cnt = 0
    for i in range(N):
        for j in range(N-1):
            if table[i][j] == 1 and table[i][j+1] == 2:
                cnt += 1

    print(f'#{tc+1} {cnt}')
