for tc in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    b_list = [[0]*255 for _ in range(N)]

    # 우측으로 90도 기울어진 빌딩맵 생성 (건물이 있는 위치는 1, 없는 곳은 0)
    for i in range(N):
        for j in range(buildings[i]):
            b_list[i][j] = 1

    cnt = 0
    for i in range(2, N-2):
        for j in range(255):
            if b_list[i][j]:
                if b_list[i-1][j] == 0 and b_list[i-2][j] == 0 and b_list[i+1][j] == 0 and b_list[i+2][j] == 0:
                    cnt += 1

    print(f'#{tc+1} {cnt}')
