import math

T = int(input())
for tc in range(T):
    x, y = map(int, input().split())

    z = (4*(x+y))**2 - 4*12*x*y
    h = (4*(x+y) - math.sqrt(z)) / 24
    v = h * (x - 2*h) * (y - 2*h)

    print('#{0} {1:.6f}'.format(tc+1, v))

# ===========================================
# 밑의 풀이는 잘 진행되지 않음.
# 뇌좀 깨우고 다시 생각해볼 것

T = int(input())
for tc in range(T):
    x, y = map(int, input().split())
    m = min(x, y)
    max_v = 0
    h = 1 / 10**5  # step을 1 / 10**5로 설정

    while 1:
        v = h * (x - 2*h) * (y - 2*h)
        if v > max_v:
            max_v = v
        h += 1 / 10**5
        print(v, h)
        if h >= m:
            break

    print('#{0} {1:.6f}'.format(tc+1, max_v))

print(2.7 * (3 - 2.7*2) * (3 - 2.7*2))