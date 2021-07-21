N = int(input())
switch = list(map(int, input().split()))
people_num = int(input())
students = []
for i in range(people_num):
    students.append(list(map(int, input().split())))

    if students[i][0] == 1:  # 남학생의 경우
        # while way =====================
        loc_num = 1
        while students[i][1]*loc_num <= N:
            n = students[i][1]*loc_num - 1
            switch[n] = not switch[n]
            loc_num += 1

        # for way =======================
        # for i in range(students[i][1]-1, N, students[i][1]):
        #     switch[i] = not switch[i]

    else:  # 여학생의 경우
        # 이 부분 indexError 발생...
        # 겉보기에는 아래와 같아보이는 데 분석이 필요하다.
        # n = students[i][1] - 1
        # loc_num = 1
        # switch[n] = not switch[n]

        # while switch[n-loc_num] == switch[n+loc_num] and n-loc_num >= 0 and n+loc_num < N:
        #     switch[n-loc_num] = not switch[n-loc_num]
        #     switch[n+loc_num] = not switch[n+loc_num]
        #     loc_num += 1

        right = students[i][1]
        left = students[i][1] - 2
        switch[students[i][1]-1] = not switch[students[i][1]-1]
        while left >= 0 and right < N and switch[right] == switch[left]:
            switch[right] = not switch[right]
            switch[left] = not switch[left]
            right += 1
            left -= 1

for i in range(N):
    if i%20 == 0 and i != 0:
        print()
    print(int(switch[i]), end = ' ')