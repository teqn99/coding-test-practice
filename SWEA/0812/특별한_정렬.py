T = int(input())
for tc in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    sorted_list = sorted(num_list, reverse=True)  # 내림차순으로 정렬
    result = []
    for i in range(N//2):
        # result에 맨 앞과 맨 뒤에서부터 하나씩 원소를 추가
        result.append(sorted_list[i])
        result.append(sorted_list[-(i+1)])
    if N % 2 == 1:
        # N이 홀수인 경우에만, 위에서 처리하지못한 중앙값을 마지막에 추가
        result.append(N//2)

    res = ' '.join(map(str, result[:10]))
    print(f'#{tc+1} {res}')