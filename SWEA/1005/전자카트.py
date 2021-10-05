from itertools import permutations

for tc in range(1, int(input())+1):
    N = int(input())
    num = [list(map(int, input().split())) for _ in range(N)]
    items = [i for i in range(2, N+1)]
    route = list(permutations(items, N-1))
    print(route)
    result = 987654321

    for i in range(len(route)):
        temp = 0
        for j in range(N):
            if j == 0:
                temp += num[0][route[i][j]-1]
            elif j == N-1:
                temp += num[route[i][j-1]-1][0]
            else:
                temp += num[route[i][j-1]-1][route[i][j]-1]
        if result > temp:
            result = temp

    print(f'#{tc} {result}')