T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    maxV = 0
    paris = [list(map(int, input().split())) for _ in range(N)]

    # 파리채 모양으로 2차원 리스트 생성
    paris_killer = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            if i == j:
                paris_killer[i][j] = 1
            elif i + j == M - 1:
                paris_killer[i][j] = 1

    # 파리채를 이용해서 파리를 잡는 과정
    for i in range(N-M+1):
        for j in range(N-M+1):
            sumV = 0
            # 파리의 범위 내에서 파리채를 순회시킴.
            for a in range(M):
                for b in range(M):
                    if paris_killer[a][b] == 1:  # 파리채가 뚫린 부분이 아닌 경우 (잡을 수 있는 경우)
                        sumV += paris[i+a][j+b]
            if maxV < sumV:
                maxV = sumV

    print(f'#{tc+1} {maxV}')