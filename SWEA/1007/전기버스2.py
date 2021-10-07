def change(start, stop, cnt):  # 현재 위치, 최대 범위, 교환 횟수
    global minV
    if cnt > minV:
        return
    if stop >= N:
        if minV > cnt:
            minV = cnt
            return
    for j in range(stop, start, -1):
        if j < N:
            change(j, j + battery[j], cnt+1)


for tc in range(1, int(input())+1):
    battery = list(map(int, input().split()))
    N = battery[0]
    battery[0] = 0
    minV = 987654321

    change(1, 1+battery[1], 0)
    print(f'#{tc} {minV}')


# 다른 풀이
def bus(pos, batt, charge):
    global min_charge
    # base case
    if charge >= min_charge:  # pruning #1: too many charges
        return
    elif batt < 0:  # pruning #2: battery off
        return
    elif pos == Batt[0]:  # Arrived!
        if charge < min_charge:
            min_charge = charge  # New min_charge
        return
    else:
        bus(pos + 1, batt - 1, charge)  # Just-go case
        if Batt[pos] > batt:  # pruning #3: meaningless charge check
            bus(pos + 1, Batt[pos] - 1, charge + 1)
            # Charge-and-go case


T = int(input())
for test in range(1, T + 1):
    Batt = list(map(int, input().split()))
    min_charge = Batt[0]
    bus(1, Batt[1], 0)  # run the bus
    print('#{} {}'.format(test, min_charge))