T = int(input())
for tc in range(T):
    N, M, K = map(int, input().split())  # M초에 K개의 붕어빵 만듦
    customers = sorted(list(map(int, input().split())))
    fish, time, flag = 0, 0, 0

    while time <= customers[-1]:
        if time != 0 and time % M == 0:
            fish += K
        if time in customers:
            people = customers.count(time)
            fish -= people
        if fish < 0:
            flag = 1
            break
        time += 1  # customers에 들어오는 수가 0이상이기 때문에, 0의 케이스도 while문안에 포함시켜야 한다..

    if flag:
        print(f'#{tc+1} Impossible')
    else:
        print(f'#{tc+1} Possible')