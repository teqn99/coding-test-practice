n = int(input())
num_list = list(map(int, input().split()))

# d에 수열의 길이를 넣을 것
d = [1] * n  # 항상 부분 수열의 최소의 길이는 1이기 때문에 1로 초기화

for i in range(1, n):
    for j in range(i):
        if num_list[j] > num_list[i]:  # 현재 보고 있는 값보다 앞에 큰 수가 나온 경우가 점점 감소하고 있는 경우이므
            d[i] = max(d[i], d[j] + 1)  # 이전의 큰 수에 +1을 해주면 부분 수열의 길이를 늘리고 있음을 표현할 수 있다.

print(max(d))