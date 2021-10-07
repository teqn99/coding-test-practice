def min_price(i, sum_price):
    global result
    if i == N:
        if result > sum_price:
            result = sum_price
        return
    elif sum_price > result:
        return
    for idx in range(N):
        if not visited[idx]:
            visited[idx] = 1
            min_price(i+1, sum_price + price[i][idx])
            visited[idx] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    price = [list(map(int, input().split())) for i in range(N)]
    visited = [0]*N
    result = 987654321

    min_price(0, 0)
    print(f'#{tc} {result}')
