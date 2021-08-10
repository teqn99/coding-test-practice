T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    carrots = [0]
    carrots.extend(list(map(int, input().split())))
    result = 0

    for i in range(1, N+1):
        div = carrots[i] // M  # 몫을 구함으로 수레를 몇 번 움직여야 하는 지 알 수 있다.
        carrots[i] = carrots[i] % M  # 나머지가 생기면 최소 1번만큼 수레를 더 움직여야 하기 때문에 이 값을 저장
        result += 2 * div * i
        if i != N:
            carrots[i+1] += carrots[i]  # for문에 의해 i가 다음으로 넘어가므로, 다음으로 남은 당근 전이
        else:
            result += 2 * i

    print(f'#{tc+1} {result}')