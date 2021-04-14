# 처음 막대 길이 64
# x: 찾고자 하는 길이
# 막대는 반으로만 자를 수 있음
# 막대길이의 합이 x보다 크다면 다음을 반복
# 1. 가장 짧은 길이의 막대를 반으로 부순다.
# 2. 잘라진 막대(2개) 중 하나를 버려도 남은 막대들(전체막대)의 길이의 합이 x보다 크다면 하나를 버린다. 크지 않다면 버리지 않는다.
# 3. 마지막으로 남은 막대들의 길이의 합을 x랑 비교한다.
# 마지막에 남은 막대들의 개수를 반환

class Solution:
    def solution(self, x):
        bar = [64]
        if x == 64:
            return 1

        while True:
            if sum(bar) > x:
                bar[-1] = bar[-1] // 2
                if sum(bar) > x:
                    continue
                elif sum(bar) == x:
                    return len(bar)
                else:
                    bar.append(bar[-1])

def solution(x):
    bar = [64]
    if x == 64:
        return 1

    while True:
        if sum(bar) > x:
            bar[-1] = bar[-1] // 2
            if sum(bar) > x:
                continue
            elif sum(bar) == x:
                return len(bar)
            else:
                bar.append(bar[-1])


s = solution(32)
print(s)