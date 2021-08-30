T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())
    info = list(map(int, input().split()))
    stop = [0] * (N+1)
    for x in info:   # 실제 정류장 번호대로 충전기 표시
        stop[x] = 1

    last = 0   # 마지막 충전 위치
    next = 0   # 이후에 충전할 수 있는 위치
    cnt = 0    # 충전 횟수
    while last + K < N:   # 마지막 충전 후 종점에 도착하면
        for i in range(1, K+1):
            if last + i < N and stop[last+i] == 1:   # 충전소
                next = last + i
        if last == next:   # 중간에 충전소가 없으면
            cnt = 0
            break
        last = next   # 이동가능한 마지막 충전소
        cnt += 1
    print('#{} {}'.format(tc+1, cnt))
    