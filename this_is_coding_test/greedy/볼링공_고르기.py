n, m = map(int, input().split())
weights = list(map(int, input().split()))
result = []

for i in range(n):
    for j in range(i, len(weights)):
        if i == j:
            continue  # 1번과 1번을 동시에 들 수 없다.
        if (i + 1, j + 1) not in result or (j + 1, i + 1) not in result:  # 두명이 서로 같지만 반대로 갖고 있는 경우는 같은 경우로 취급
            if weights[i] != weights[j]:  # 두 사람이 서로 다른 무게의 공을 들어야 하기 때문
                result.append((i + 1, j + 1))  # 구분이 편하게 튜플의 형식으로 append

print(len(result))