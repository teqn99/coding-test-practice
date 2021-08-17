T = int(input())
for tc in range(T):
    bus_list = [0] * 5001
    result = ''
    N = int(input())
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            bus_list[j] += 1
    P = int(input())
    for i in range(P):
        idx = int(input())
        result += str(bus_list[idx])
        result += ' '

    print(f'#{tc+1} {result}')