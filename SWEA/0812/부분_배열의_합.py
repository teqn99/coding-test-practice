T = int(input())
for tc in range(T):
    N, n, m = map(int, input().split())
    num_list = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))
    maxi = 0

    for i in range(N-n+1):
        for j in range(N-m+1):
            sumV = 0
            part_list = [row[j:j+m] for row in num_list[i:i+n]]  # 정해진 부분을 새 리스트로 가져오기
            for k in range(len(part_list)):
                sumV += sum(part_list[k])  # 부분 리스트의 총 합을 sumV에 저장
            if maxi < sumV:
                maxi = sumV  # 최대값 비교

    print(f'#{tc+1} {maxi}')