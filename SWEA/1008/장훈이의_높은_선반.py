def top_check(cnt, sumV):
    global result
    if cnt == N:
        if sumV >= B:
            result = min(result, sumV-B)
        return
    elif sumV-B >= result:
        return
    top_check(cnt+1, sumV)
    top_check(cnt+1, sumV+heights[cnt])


for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    heights = sorted(list(map(int, input().split())))
    result = 987654321

    top_check(0, 0)
    print(f'#{tc} {result}')
