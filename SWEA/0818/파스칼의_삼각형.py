T = int(input())
for tc in range(T):
    N = int(input())
    tri = [[1]]
    for i in range(1, N):
        tri.append([0]*(i+1))

    for i in range(1, N):
        for j in range(len(tri[i])):
            if j == 0 or j == len(tri[i])-1:
                tri[i][j] = 1
            else:
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    print(f'#{tc+1}')
    for i in range(N):
        for j in range(len(tri[i])):
            print(tri[i][j], end=' ')
        print()