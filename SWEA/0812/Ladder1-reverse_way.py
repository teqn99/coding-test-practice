for tc in range(10):
    N = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    idx = 99
    dest = ladder[idx].index(2)
    idx -= 1  # 어차피 사다리 맨 밑에서 방향 전환은 없기 때문
    while idx != 0:
        if 0 < dest < 100 and ladder[idx][dest-1] == 1:
            # dest가 사다리 범위안에 존재하면서, 사다리 왼편으로 갈 수 있는 경우라면
            dest -= 1
        elif 0 <= dest < 99 and ladder[idx][dest+1] == 1:
            # dest가 사다리 범위안에 존재하면서, 사다리 오른편으로 갈 수 있는 경우라면
            dest += 1
        else:
            # 왼쪽, 오른쪽 둘 다 못가면 그냥 위로 올라가기
            idx -= 1
        ladder[idx][dest] = 0  # 왼쪽, 오른쪽으로 돌아가는 걸 방지하기 위해 지나온 자리는 0으로 변경

    print(f'#{N} {dest}')