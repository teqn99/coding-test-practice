def inorder(n, V):
    global cnt
    if n <= V:  # 유효한 노드이면
        inorder(n*2, V)  # 왼쪽 자식 이동
        cnt += 1
        tree[n] = cnt  # 값 기록
        inorder(n*2 + 1, V)  # 오른쪽 자식 이동


T = int(input())
for tc in range(T):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 0
    inorder(1, N)
    print(f'#{tc+1} {tree[1]} {tree[N//2]}')