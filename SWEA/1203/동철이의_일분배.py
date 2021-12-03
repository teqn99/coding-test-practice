def max_percent(i, prod):
    global result
    if i == N:
        if result < prod:
            result = prod
        return
    if prod <= result:
        return
    for idx in range(N):
        if not visit[idx]:
            visit[idx] = 1
            max_percent(i+1, prod*pos[i][idx]*0.01)
            visit[idx] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    pos = [list(map(int, input().split())) for _ in range(N)]
    visit = [0]*N
    result = 0

    max_percent(0, 1)
    print('#{} {:6f}'.format(tc, result*100))
