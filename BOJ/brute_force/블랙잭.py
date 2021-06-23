from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards = sorted(cards)

comb = list(combinations(cards, 3))
result = 0
for i in comb:
    if sum(i) == m:
        result = m
        break
    elif sum(i) < m and sum(i) > result:
        result = sum(i)

print(result)