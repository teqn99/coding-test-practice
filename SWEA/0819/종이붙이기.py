T = int(input())
for tc in range(T):
    N = int(input()) // 10
    num_list = [0] * 31  # N의 범위가 300까지 이므로, num_list를 N=10일때 num_list[1]의 형식으로 쓰기 위해 길이를 31로 설정
    num_list[1] = 1

    for i in range(2, N + 1):
        if i % 2 == 0:
            num_list[i] = num_list[i - 1] * 2 + 1
        else:
            num_list[i] = num_list[i - 1] * 2 - 1

    print(f'#{tc + 1} {num_list[N]}')