T = int(input())
for tc in range(T):
    N, M, L = map(int, input().split())
    nodes = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        nodes[a] = b

    for i in range(N-M, 0, -1):
        nodes[i] = nodes[2*i]
        if N+1 > 2*i + 1:
            nodes[i] += nodes[2*i + 1]

    print(f'#{tc+1} {nodes[L]}')