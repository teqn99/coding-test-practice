T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    chargers = list(map(int, input().split()))
    cnt, ckpt = 0, 0  # cnt: 결과, ckpt: 남은 주행가능거리를 계산하기 위한 값
    K_copied = K

    for i in range(M):
        if i == M-1:
            if N - ckpt > K_copied:
                cnt += 1

        elif chargers[i] - ckpt <= K_copied:
            if chargers[i + 1] - ckpt > K_copied:
                K_copied = K
                cnt += 1
            else:
                K_copied -= (chargers[i] - ckpt)
            ckpt = chargers[i]

        else:
            cnt = 0
            break

    print(f'#{tc+1} {cnt}')