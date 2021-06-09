N = int(input())
P = list(map(int, input().split()))
P = sorted(P)
result_list = []
cnt = 0

for i in range(N):
    cnt += P[i]
    result_list.append(cnt)

print(sum(result_list))