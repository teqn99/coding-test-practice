def Calculation(stair_list, stair):
    count, d_count = 0, 0
    delete_queue = []
    # 이동중인사람이나 대기중인사람, 내려가는 사람이있다면 반복
    while stair_list or delete_queue or d_count:
        # 대기하는 사람이 있다면
        while d_count:
            # 최대인원이 다찼다면 정지
            if len(delete_queue) == 3:
                break
            # 내려가는 사람들에게 넣어주기
            delete_queue.append(stair[2])
            # 한명 넣을때마다 대기인원 감소
            d_count -= 1

        # 내려가는 인원이 있을때 동작
        for i in range(len(delete_queue) - 1, -1, -1):
            # 시간을 감소시키고
            delete_queue[i] -= 1
            # 전부 내려갔다면 뺀다
            if delete_queue[i] <= 0:
                delete_queue.pop(i)

        # 이동중인 사람이 있다면
        for i in range(len(stair_list) - 1, -1, -1):
            # 거리를 감소키고
            stair_list[i] -= 1
            # 계단까지 갔다면
            if stair_list[i] <= 0:
                # 빼버리고 대기인원 증가
                stair_list.pop(i)
                d_count += 1
        # 1초 증가
        count += 1
    return count


# 조합찾기
def dfs(idx):
    # 조합이 결정되었다면
    if idx == len(people):
        global min_count
        stair_list1, stair_list2 = [], []
        # 1번계단, 2번계단 분리하기
        for i in range(len(people)):
            if check[i]:
                stair_list1.append(people[i][0])
            else:
                stair_list2.append(people[i][1])
        # 시간 계산하기, 두 계단 중 긴 시간을 가져온다. (긴 시간을 가진 계단 쪽이 늦게 끝나는 곳이기 때문)
        count = max(Calculation(sorted(stair_list1), stairs[0]), Calculation(sorted(stair_list2), stairs[1]))
        # 작은 시간으로 교체
        min_count = min(count, min_count)
        return
    check[idx] = False
    dfs(idx + 1)
    check[idx] = True
    dfs(idx + 1)


for tc in range(1, int(input())+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]
    people = []
    stairs = []
    min_count = 987654321
    for i in range(N):
        for j in range(N):
            if room[i][j] > 1:
                stairs.append([i, j, room[i][j]])  # 계단 좌표, 계단 길이
            elif room[i][j] == 1:
                people.append([i, j])

    for i in range(len(people)):
        distance1 = abs(people[i][0] - stairs[0][0]) + abs(people[i][1] - stairs[0][1])
        distance2 = abs(people[i][0] - stairs[1][0]) + abs(people[i][1] - stairs[1][1])
        people[i][0] = distance1
        people[i][1] = distance2

    check = [0 for _ in range(len(people))]  #1번 계단으로 갈것인지, 2번계단으로 갈것인지
    dfs(0)
    print('#{} {}'.format(tc, min_count + 1))
