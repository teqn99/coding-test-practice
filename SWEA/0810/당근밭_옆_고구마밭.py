T = int(input())
for tc in range(T):
    N = int(input())
    C = list(map(int, input().split()))

    long, sumV = 1, C[0]  # long: 긴 줄기의 길이, sumV: 긴 줄기에 달린 고구마 개수
    long_list = []  # 2차원 리스트로 [long, sumV]를 담을 리스트
    for i in range(N):
        if i < N-1:
            if C[i] < C[i+1]:
                long += 1
                sumV += C[i+1]
            else:
                long_list.append([long, sumV])
                long = 1
                sumV = C[i+1]
        else:
            long_list.append([long, sumV])

    long_list = sorted(long_list, key=lambda x: x[0])  # 긴 줄기의 길이를 기준으로 오름차순 정렬

    result_list = []  # 결과를 담을 리스트
    maxi, cnt = 0, 0  # maxi: 최대 긴 줄기의 길이, cnt: 최대 긴 줄기의 개수
    for i in range(len(long_list)):
        if maxi < long_list[i][0]:
            maxi = long_list[i][0]
        if long_list[i][0] > 1:
            cnt += 1
    for i in range(len(long_list)):
        if long_list[i][0] == maxi:
            result_list.append(long_list[i])  # 최대 긴 줄기의 리스트만 결과리스트에 추가

    result_list = sorted(result_list, key=lambda x: x[1])  # 고구마 개수를 기준으로 오름차순 정렬
    if maxi == 1:
        print(f'#{tc + 1} {cnt} 0')  # 긴 줄기가 없는 경우, 0 0을 출력해야하는 테스트케이스가 존재
    else:
        print(f'#{tc + 1} {cnt} {result_list[-1][1]}')  # 결과 반환