T = int(input())
for tc in range(T):
    s_list = []
    maxi = 0
    for i in range(5):
        s_list.append(input())
        if maxi < len(s_list[i]):
            maxi = len(s_list[i])
    result = ''

    for i in range(maxi):
        for j in range(5):
            if i >= len(s_list[j]):
                continue
            else:
                result += s_list[j][i]

    print(f'#{tc+1} {result}')