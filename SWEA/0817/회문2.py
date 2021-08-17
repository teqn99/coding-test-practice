for tc in range(10):
    N = int(input())
    a_list = []
    for i in range(100):
        a_list.append(input())
    maxi = 1

    for i in range(100):
        for j in range(100):
            # 가로
            for k in range(100):
                if a_list[i][j:k+1] == a_list[i][j:k+1][::-1]:
                    if maxi < len(a_list[i][j:k+1]):
                        maxi = len(a_list[i][j:k+1])
    
            # 세로
            s = ''
            for k in range(j, 100):
                s += a_list[k][i]
                if s == s[::-1]:
                    if maxi < len(s):
                        maxi = len(s)

    print(f'#{N} {maxi}')