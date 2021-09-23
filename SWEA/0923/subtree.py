T = int(input())
for tc in range(T):
    E, N = map(int, input().split())
    node = [0] * (E+2)  # 0의 위치는 사용하지 않을 것이기 때문, 간선의 개수가 E개이기 때문에 노드의 개수는 E+1개
    nodes = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        a, b = nodes[i], nodes[i+1]
        if node[a] == 0:
            node[a] = [b]
        else:
            node[a].append(b)

    result = [N]
    i = 0
    while 1:
        if len(result) < i+1:
            break
        now_list = node[result[i]]
        if now_list == 0:
            break
        for j in now_list:
            result.append(j)
        i += 1

    print(f'#{tc+1} {len(result)}')