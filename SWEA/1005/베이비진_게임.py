def check(a):
    run = 0
    tri = 0

    for i in range(len(a)):
        if a.count(a[i]) >= 3:
            tri += 1
        if a.count(a[i]) >= 1 and a.count(a[i]+1) >= 1 and a.count(a[i]+2) >= 1:
            run += 1

    return run, tri


def baby(run_a, tri_a, run_b, tri_b):
    global result
    if run_a > 0 or tri_a > 0:
        if run_b > 0 or tri_b > 0:
            result = 0
        else:
            result = 1
    elif run_b > 0 or tri_b > 0:
        result = 2


for tc in range(1, int(input())+1):
    cards = list(map(int, input().split()))
    one, two = [], []
    result = 0  # draw
    run_a, tri_a, run_b, tri_b = 0, 0, 0, 0

    for i in range(0, 12, 2):
        one.append(cards[i])
        if i >= 4:  # 카드가 3개 이상인 경우부터 check
            run_a, tri_a = check(one)
            baby(run_a, tri_a, run_b, tri_b)
            if result != 0:
                break
        two.append(cards[i+1])
        if i >= 4:  # 카드가 3개 이상인 경우부터 check
            run_b, tri_b = check(two)
            baby(run_a, tri_a, run_b, tri_b)
            if result != 0:
                break

    print(f'#{tc} {result}')