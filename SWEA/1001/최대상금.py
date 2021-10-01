def f(info, change):
    if change == 0:
        temp = ''.join(info)
        if temp not in result_list:
            result_list.append(temp)
    else:
        for i in range(len(info)):
            for j in range(len(info)):
                if j == i:
                    continue
                info[i], info[j] = info[j], info[i]
                temp = ''.join(info)
                if [temp, change] not in check_list:
                    check_list.append([temp, change])
                    f(info, change-1)
                info[i], info[j] = info[j], info[i]


for tc in range(1, int(input())+1):
    info, change = map(int, input().split())
    info = list(str(info))
    result_list = []
    check_list = []

    f(info, change)

    maxV = 0
    for i in result_list:
        if maxV < int(i):
            maxV = int(i)

    print(f'#{tc} {maxV}')


# 다른 풀이
for tc in range(1, int(input())+1):
    a, b = input().split()
    b = int(b)
    num = set([a])
    print(num)
    tmp = set()
    for i in range(b):
        while num:
            s = list(num.pop())
            print(s)
            for j in range(len(a)):
                for k in range(j+1,len(a)):
                    s[j], s[k] = s[k], s[j]
                    tmp.add(''.join(s))
                    s[j], s[k] = s[k], s[j]
        num, tmp = tmp, num

    value = 0
    for i in num:
        if value < int(i):
            value = int(i)

    print(f'#{tc} {value}')


# 다른 풀이
def dfs(exchange):
    global ans
    if exchange == 0:
        ans = max(int(''.join(nums)), ans)
        return

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            if not visited.get((''.join(nums), reward - exchange + 1), 0):
                visited[(''.join(nums), reward - exchange + 1)] = 1
                dfs(exchange - 1)
            nums[i], nums[j] = nums[j], nums[i]


T = int(input())
for tc in range(1, T + 1):
    nums, exchange = input().split()
    nums = list(nums)
    reward = int(exchange)

    ans = 0
    visited = {}
    dfs(reward)
    print("#{} {}".format(tc, ans))