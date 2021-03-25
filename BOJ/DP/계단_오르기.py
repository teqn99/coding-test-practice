n = int(input())
steps =[0] * 301
for i in range(1, n + 1):
    steps[i] = int(input())

d = [0] * 301
d[1] = steps[1]
d[2] = max(steps[2] + steps[1], steps[2] + steps[0])

for i in range(3, n + 1):
    # 계단을 오르는 방법서 - 맨 위에서 밑을 내려다 보자
    # 1. 한 칸 전에서 올라온 경우, 두 칸 전에서는 올라올 수 없으므로 그 전에 칸은 세 칸 전에서 올라온 경우이다.
    # 2. 두 칸 전에서 올라온 경우
    # 1, 2처럼 두 가지 경우가 있다. 이 두 경우 중 큰 값을 사용하면 최대값을 구할 수 있다.
    d[i] = max(steps[i] + d[i - 2], steps[i] + steps[i - 1] + d[i - 3])

print(d[n])

# 아래의 비슷한 코드로 여러 번 인덱스에러가 발생했다.
# 왜 그런지 생각해보기.. (이유를 모르겠다.)
"""
n = int(input())
steps =[0]
for i in range(n):
    steps.append(int(input()))

d = [0] * 301
d[1] = max(steps[1], steps[0] + steps[1])
d[2] = max(steps[2] + steps[1], steps[2] + steps[0])

for i in range(3, n + 1):
    d[i] = max(steps[i] + d[i - 2], steps[i] + steps[i - 1] + d[i - 3])

print(d[n])
"""