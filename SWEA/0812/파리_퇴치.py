T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    paris = []
    for i in range(N):
        paris.append(list(map(int, input().split())))
    maxi = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            sumV = 0
            print(paris[i:i+M])
            attack = [row[j:j+M] for row in paris[i:i+M]]  # 파리채가 칠 수 있는 범위로 부분집합 생성
            for k in range(len(attack)):
                sumV += sum(attack[k])  # 부분집합의 합 계산
            if maxi < sumV:
                maxi = sumV  # 최대값 비교 및 갱신
                
    print(f'#{tc+1} {maxi}')