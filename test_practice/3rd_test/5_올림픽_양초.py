"""
생각 경시 대회를 축하하기 위해서 전통적으로 초에 불을 붙인다.
대회 첫째날밤에는 하나의 초에 불을 붙인다. 저녁이 끝나면 불을 끈다.
다음날마다 전날보다 불을 붙이는 초의 개수를 하나씩 늘려서 (1을 기준으로) n번째날 밤에는 n개의 초에 불을 붙인다 (아침에는 모든 초의 불을 끈다).
매일밤 불을 붙일때마다 초의 높이는 1씩 줄어든다. 높이가 0이 되면 더 이상 사용할 수 없다.

주어진 candles의 i번째 요소는 i번째 양초의 높이는 나타낸다.
새로운 양초를 구입하지 않고 최대 며칠밤을 축하할 수 있는지 구하여라.
예를 들어, 높이 2의 초 3개를 가지고 있다면, 첫째날 초 하나를 밝히고, 나머지 두개를 둘째날 밝히고, 셋째날에 모든 초를 밝혀 3일동안 축하할 수 있다.


참고 / 제약 사항
candles는 1개 이상, 50개 이하의 요소를 가진다.
candles의 각 요소는 1 이상, 100 이하이다.
"""
class Solution:
    def solution(self, candles):
        cnt = 0
        while True:
            candles.sort(reverse=True)
            if 0 in candles[:cnt + 1] or cnt >= len(candles):
                break
            for i in range(cnt + 1):
                candles[i] -= 1
            cnt += 1  # cnt: cnt번째 날임을 의미
        return cnt


def solution(candles):
    for i in range(len(candles)):  # i: (i + 1)번째 날임을 의미
        candles.sort(reverse=True)
        if 0 in candles[:i+1]:
            return i
        for j in range(i + 1):
            candles[j] -= 1
    return i + 1
s = solution([1,1,1,1,1,1,1,1,1,1])
print(s)
s = solution([5,2,2,1])
print(s)
s = solution([2,2,2,4])
print(s)


def solution2(candles):
    cnt = 0
    while True:
        candles.sort(reverse=True)
        if 0 in candles[:cnt+1] or cnt >= len(candles):
            break
        for i in range(cnt + 1):
            candles[i] -= 1
        cnt += 1  # cnt: cnt번째 날임을 의미
    return cnt
s = solution2([1,1,1,1,1,1,1,1,1,1])
print(s)
s = solution2([5,2,2,1])
print(s)
s = solution2([2,2,2,4])
print(s)