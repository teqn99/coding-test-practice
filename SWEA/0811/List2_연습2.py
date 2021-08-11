T = int(input())
for tc in range(T):
    num_list = list(map(int, input().split()))
    N = len(num_list)
    flag = False
    for i in range(1 << N):  # N개의 원소 포함 여부 표시
        sum_list = []
        for j in range(N+1):
            if i & (1 << j):  # i의 j번 비트가 1이면 num_list[j]원소가 부분집합에 포함
                sum_list.append(num_list[j])
        result = 0
        for k in range(len(sum_list)):
            result += sum_list[k]
            if result == 0:
                flag = True
                break
        if flag == True:
            break
    if flag == True:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')