T = int(input())
for tc in range(T):
    A = list(range(1, 13))
    N, K = map(int, input().split())
    result = 0

    for i in range(1 << 12):  # 12개의 원소를 갖는 부분집합의 개수
        result_list = []
        for j in range(13):
            if i & (1 << j):  # # i의 j번 비트가 1이면 원소가 부분집합에 포함
                result_list.append(A[j])

        # result_list의 길이가 N이면서 합이 K인 경우만 답이 될 수 있다.
        sum_result = 0
        for k in range(len(result_list)):
            sum_result += result_list[k]
        if sum_result == K:
            if len(result_list) == N:
                result += 1

    print(f'#{tc+1} {result}')