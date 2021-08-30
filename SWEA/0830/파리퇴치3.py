T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    paris = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    plus_dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    multiple_dir = [[-1, 1], [-1, -1], [1, 1], [1, -1]]
    for i in range(N):
        for j in range(N):
            plus = paris[i][j]
            multiple = paris[i][j]
            for k in range(1, M):
                for x, y in plus_dir:
                    if 0 <= i+x*k < N and 0 <= j+y*k < N:
                        plus += paris[i+x*k][j+y*k]
                for x, y in multiple_dir:
                    if 0 <= i+x*k < N and 0 <= j+y*k < N:
                        multiple += paris[i+x*k][j+y*k]
            if result < plus:
                result = plus
            if result < multiple:
                result = multiple

    print('#{} {}'.format(tc+1, result))