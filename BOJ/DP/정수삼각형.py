N = int(input())
tri_list = []
for i in range(N):
    tri_list.append(list(map(int, input().split())))

k = 2
for i in range(N):
    for j in range(k):
        if j == 0:
            tri_list[i][j] =  tri_list[i][j] + tri_list[i - 1][j]
        elif i == j:
            tri_list[i][j] = tri_list[i][j] + tri_list[i - 1][j - 1]
        else:
            tri_list[i][j] = max(tri_list[i - 1][j - 1], tri_list[i - 1][j]) + tri_list[i][j]
    k += 1

print(max(tri_list[N-1]))