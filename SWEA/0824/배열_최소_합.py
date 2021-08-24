def backtracing(i, j, N, s):
    global sumV
    global checked
    if i == N-1:
        s += num_list[i][j]
        if s < sumV:
            sumV = s
        s -= num_list[i][j]

    elif s > sumV:  # 부분합이 sumV을 넘을 경우 종료
        return

    else:
        s += num_list[i][j]
        checked.append(j)
        cnt = j
        while cnt > 0:
            cnt -= 1
            if cnt not in checked:
                backtracing(i+1, cnt, N, s)
        cnt = j
        while cnt < N-1:
            cnt += 1
            if cnt not in checked:
                backtracing(i+1, cnt, N, s)
        checked.remove(j)
        s -= num_list[i][j]


T = int(input())
for tc in range(T):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    sumV = 100

    for i in range(N):
        checked = []
        backtracing(0, i, N, 0)

    print(f'#{tc+1} {sumV}')


#-----------------------------------------------------------------------------
# 다른 풀이

def backtracking(i, N, s, visited):
    global sumV
    if i == N:
        if s < sumV:
            sumV = s
    elif s > sumV:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                backtracking(i + 1, N, s + num_list[i][j], visited)
                visited[j] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    sumV = 100
    visited = [0]*N

    backtracking(0, N, 0, visited)
    print(f'#{tc + 1} {sumV}')