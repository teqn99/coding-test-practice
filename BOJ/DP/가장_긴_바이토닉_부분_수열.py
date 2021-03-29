n = int(input())
num_list = list(map(int, input().split()))
num_list_reversed = num_list[::-1]

dp_u = [1] * n  # dp_u에는 원래대로 증가하는 부분 수열을 저장
dp_d = [1] * n  # dp_d에는 감소하는 부분 수열을 저장할 생각인데, 기준 범위 이후에 감소하는 부분 수열을 넣으려해보니 식이 잘 안세워짐.
# 그래서 입력 리스트를 뒤집은 리스트를 만들어 주어, 뒤집은 리스트의 증가하는 부분 수열을 저장

for i in range(1, n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp_u[i] = max(dp_u[i], dp_u[j] + 1)
        if num_list_reversed[i] > num_list_reversed[j]:
            dp_d[i] = max(dp_d[i], dp_d[j] + 1)

result = [0] * n
for i in range(n):
    # dp_u와 dp_d를 크로스로 더해서 1씩 빼주면, 바이토닉 부분 수열의 길이를 구할 수 있다.
    # 1씩 빼주는 이유: [1,5,2,1,4,3,4,5,2,1]의 수열에서 dp_u와 dp_d를 통해 각각 1,2,3,4,5 / 5,2,1을 구할 수 있다.
    #               이 경우, 총 길이 8에서 중복된 5를 한 번 빼주면 7이 나온다.
    result[i] = dp_u[i] + dp_d[n - i - 1] - 1

print(max(result))