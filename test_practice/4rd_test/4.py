"""
나라마다 통용되는 화폐의 단위와 갯수는 다르다.

화폐 단위의 예)
대한민국: 10원, 50원, 100원, 500원, 1000원, 5000원, 10000원, 50000원
영국: 1페니, 2펜스, 5펜스, 10펜스, 20펜스, 50펜스, 1파운드(100펜스), 2파운트(200펜스)

currencies의 각 요소는 이 나라에서 사용되는 화폐의 단위를 나타낸다.
이 나라의 화폐를 이용하여, wantMoney만큼의 돈을 거슬러주는 모든 방법의 수를 리턴하시오


참고 / 제약 사항
- currencies에 포함되어 있는 요소의 갯수는 1개이상이며 100개이하 이다.
- currencies의 각 요소의 값은 1이상이며 1000이하 이다.
- wantMoney의 값은 1이상이며 1000이하 이다.
"""
from itertools import combinations_with_replacement


def solution(currencies, wantMoney):
    result = list()
    i = 1
    while currencies:
        # if min(currencies)*i > wantMoney:
        #     break
        cwr = list(combinations_with_replacement(currencies, i))
        for j in cwr:
            if sum(j) == wantMoney:
                result.append(j)

        if min(currencies)*i + max(currencies) > wantMoney:
            currencies.remove(max(currencies))
        i += 1

    return len(result)


s = solution([1, 5, 10], 10)
print(s)

s = solution([4, 25, 40], 80)
print(s)

s = solution([1, 21, 24, 31, 35, 37, 47], 57)
print(s)

p = ['c', 'd']
p = p + ['a', 'b']
print(p)