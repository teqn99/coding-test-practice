T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    for i in range(E):
        A, B = map(int, input().split())
        node[A].append(B)

    S, G = map(int, input().split())  # S: 출발 노드, G: 도착 노드
    stack = [S]
    visited = [0]*(V+1)  # 방문한 노드들을 표시
    result = 0

    while stack:
        now = stack.pop()
        visited[now] = 1
        # 방법 1
        if now == G:  # now가 G에 도달한 경우
            result = 1
            break
        for n in node[now]:
            if visited[n] == 0 and (n not in stack):  # n이 방문하지 않은 상태이면서, stack에 없는 경우
                stack.append(n)
        # 방법 2 - 이게 조금 더 빠를 듯 하다.
        # if G in stack:  # G가 stack 안에 있으면, 언젠가는 G에 도달할 것이라는 의미
        #     result = 1
        #     break

    print(f'#{tc+1} {result}')