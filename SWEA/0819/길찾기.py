for tc in range(10):
    T, N = map(int, input().split())
    input_list = list(map(int, input().split()))
    node = [[] for _ in range(100)]  # 입력받은 순서쌍을 순서쌍의 첫번째 부분은 index, 두번째 부분은 값으로 저장할 2차원 리스트
    for i in range(N*2):
        if i % 2 == 0:  # 입력 부분에서 순서쌍의 앞부분(node의 index가 될 부분)
            A = input_list[i]
        else:
            node[A].append(input_list[i])
    result = 0

    visited = [0]*100  # 방문한 적이 있는 지 표시하기 위한 리스트
    stack = [0]  # 0에서부터 시작하기 때문
    while stack:
        now = stack.pop()
        visited[now] = 1  # 방문 체크
        if now == 99:  # 도착지에 도달한 경우
            result = 1
            break
        for i in node[now]:
            if visited[i] == 0 and i not in stack:  # 방문한 적이 없으면서 stack에 포함되지 않은 경우에만 stack에 새로 추가
                stack.append(i)

    print(f'#{T} {result}')