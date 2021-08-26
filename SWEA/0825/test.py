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

# ==================================================
# 완성 풀이 2
"""
0 < h < min(X, Y) / 2
A = (X - 2h) * (Y - 2h) * h

h 초기값: min(X, Y) / 4로 설정
delta = h / 2

A1 = (X - 2(h+delta))(Y - 2(h+delta))(h+delta)
A2 = (X - 2(h-delta))(Y - 2(h-delta))(h-delta)

|A1 - A2| < 원하는 범위 인지를 확인하는 것이 중요!!
->
    if abs(A1 - A2) < 1/(10**8):  # (= 1e-8)
        같은 걸로 칠게!
    elif A1 > A2:
        h += delta
    elif A1 < A2:
        h -= delta
    else:
    
    
a = 1e-6
b = 1e6  # 10**6과 동일
print(f'{a:.6f')
"""
T = int(input())
for tc in range(1, T+1):
    X, Y = map(int, input().split())
    h = min(X, Y) / 4                      # 0 < h < min(X, Y) / 2 -> h의 중간값은 min(X, Y) / 4이다.
    d = h / 2
    ans = 0

    while True:
        A1 = (X - 2 * (h + d)) * (Y - 2 * (h + d)) * (h + d)
        A2 = (X - 2 * (h - d)) * (Y - 2 * (h - d)) * (h - d)
        if abs(A1 - A2) < 1e-8:
            ans = A1
            break
        elif A1 > A2:
            h += d
        elif A1 < A2:
            h -= d
        d /= 2

    print(f'#{tc} {ans:.6f}')