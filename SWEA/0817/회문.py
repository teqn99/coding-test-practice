T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    str_list = []
    result = ''
    for i in range(N):
        str_list.append(input())

    for i in range(N):
        for j in range(N-M+1):
            if str_list[i][j:j+M] == str_list[i][j:j+M][::-1]:
                result = str_list[i][j:j+M]

    for i in range(N-M+1):
        for j in range(N):
            s = ''
            for k in range(M):
                s += str_list[i+k][j]
            if s == s[::-1]:
                result = s

    print(f'#{tc + 1} {result}')
# T = int(input())
# for tc in range(T):
#     N, M = map(int, input().split())
#     str_list = []
#     result = ''
#     for i in range(N):
#         str_list.append(input())
#
#     for i in range(N):
#         for j in range(N-M+1):
#             if str_list[i][j:j+M] == str_list[i][j:j+M][::-1]:
#                 result = str_list[i][j:j+M]
#
#             for k in range(N):
#                 s = ''
#                 for l in range(M):
#                     s += str_list[j+l][k]
#                 if s == s[::-1]:
#                     result = s
#
#     print(f'#{tc + 1} {result}')