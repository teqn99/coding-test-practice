T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))
    while M:
        M -= 1
        num_list.append(num_list.pop(0))

    print(f'#{tc+1} {num_list[0]}')