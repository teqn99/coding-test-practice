import copy

for tc in range(10):
    N = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))

    for i in range(100):
        ladder_copied = copy.deepcopy(ladder)
        idx = 0
        if ladder_copied[0][i] == 1:
            dest = i
            idx += 1
            while idx != 99:
                ladder_copied[idx][dest] = 0  # 왼쪽, 오른쪽으로 돌아가는 걸 방지하기 위해 지나온 자리는 0으로 변경
                if 0 < dest < 100 and ladder_copied[idx][dest-1] == 1:
                    # dest가 사다리 범위안에 존재하면서, 사다리 왼편으로 갈 수 있는 경우라면
                    dest -= 1
                elif 0 <= dest < 99 and ladder_copied[idx][dest+1] == 1:
                    # dest가 사다리 범위안에 존재하면서, 사다리 오른편으로 갈 수 있는 경우라면
                    dest += 1
                else:
                    # 왼쪽, 오른쪽 둘 다 못가면 그냥 내려가기
                    idx += 1
        if ladder_copied[idx][dest] == 2:
            break

    print(f'#{N} {i}')  # 출발점을 찾아야 하기 때문에 i를 출력