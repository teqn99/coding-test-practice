T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    ballons = []
    for i in range(N):
        ballons.append(list(map(int, input().split())))
    maxi = 0

    for i in range(N):
        for j in range(M):
            bomb = ballons[i][j]
            sumV = bomb
            for x in range(i-bomb, i+bomb+1):  # 세로
                if 0 <= x < N and x != i:  # x == i인 경우는 bomb를 구할 때 사용했기 때문
                    sumV += ballons[x][j]
            for y in range(j-bomb, j+bomb+1):  # 가로
                if 0 <= y < M and y != j:  # y == j인 경우는 bomb를 구할 때 사용했기 때문
                    sumV += ballons[i][y]
            if maxi < sumV:
                maxi = sumV

    print(f'#{tc+1} {maxi}')