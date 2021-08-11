T = int(input())
for tc in range(T):
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))
    result = 0

    for i in range(N):
        for j in range(N):
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    result += abs(num_list[i][j] - num_list[ni][nj])

    print(f'#{tc+1} {result}')