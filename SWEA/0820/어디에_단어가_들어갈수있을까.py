T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr_T = [list(x) for x in zip(*arr)]  # transpose
    result = 0

    for i in range(N):
        cnt_A, cnt_B = 0, 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt_A += 1
            else:
                if cnt_A == K:  # 블록 완성
                    result += 1
                cnt_A = 0  # 0이 나온 경우, 이어지는 블록이 끊긴 경우이므로 0으로 초기화

            if arr_T[i][j] == 1:
                cnt_B += 1
            else:
                if cnt_B == K:  # 블록 완성
                    result += 1
                cnt_B = 0  # 0이 나온 경우, 이어지는 블록이 끊긴 경우이므로 0으로 초기화

        # 마지막 부분이 1인 경우 중, 위의 구문에서 result += 1 처리가 안된 부분을 고려
        if cnt_A == K:
            result += 1
        if cnt_B == K:
            result += 1

    print(f'#{tc+1} {result}')