T = int(input())
for tc in range(T):
    N = int(input())
    num_list = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))
    result = sum(num_list[0])
    result_list = []

    for i in range(1, N):
        if sum(num_list[i]) != sum(num_list[i-1]):  # 행의 합이 달라지면 새로운 사각형이 시작되는 것이므로
            result_list.append(result)  # result_list에 기존 result 추가 후 0으로 초기화
            result = 0
        result += sum(num_list[i])  # 다시 sum을 구해서 result에 합해주기

    print(f'#{tc+1} {max(result_list)}')
