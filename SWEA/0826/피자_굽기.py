T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    for i in range(M):
        cheese[i] = [cheese[i], i+1]                 # cheese라는 리스트를 인덱스도 포함하고 있는 2차원 리스트로 변환
    fire = []
    for i in range(N):
        fire.append(cheese.pop(0))                   # fire는 화덕을 의미, 화덕의 크기(N)만큼 cheese에서 꺼내넣기

    while len(fire) != 1:
        f = fire.pop(0)                              # 맨 앞에 있는 치즈를 확인
        f[0] = f[0] // 2                             # 절반으로 치즈 녹이기 - (1), (2)
        if f[0] == 0:                                # (1) 치즈가 다 녹았다면,
            if len(cheese) > 0:                      # cheese 리스트가 비어있지 않다면,
                fire.append(cheese.pop(0))           # 다 녹은 치즈를 빼고, 새 치즈를 화덕의 마지막 자리에 넣고
            continue                                 # 다시 화덕 돌리기
        fire.append(f)                               # (2) 치즈가 다 녹지 않은 경우이므로, 마지막으로 넣고 회전 다시 시작

    print(f'#{tc+1} {fire[0][1]}')                   # 마지막 남은 치즈의 인덱스를 출력해야 하기 때문