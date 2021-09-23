# def f(N, V):
#     if 2*V <= N and nodes[V] > nodes[2*V]:
#         nodes[V], nodes[2*V] = nodes[2*V], nodes[V]
#     f(N, 2*V)
#     if 2*V + 1 <= N and nodes[V] > nodes[2*V + 1]:
#         nodes[V], nodes[2*V + 1] = nodes[2*V + 1], nodes[V]
#     f(N, 2*V + 1)
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())
#     nodes = [0]
#     nodes.extend(list(map(int, input().split())))
#
#     f(N, 1)
#     print(nodes)
#     # chk = 1
#     # while chk:
#     #     chk = 0
#     #     for i in range((N+1)//2 + 1):
#     #         if i*2 <= N and nodes[i] > nodes[i*2]:
#     #             nodes[i], nodes[i*2] = nodes[i*2], nodes[i]
#     #             chk = 1
#     #         elif i*2 + 1 <= N and nodes[i] > nodes[i*2 + 1]:
#     #             nodes[i], nodes[i*2 + 1] = nodes[i*2 + 1], nodes[i]
#     #             chk = 1
#     #     print(nodes)
#
#     result = 0
#     res = N // 2
#     while 1:
#         result += nodes[res]
#         if res == 1:
#             break
#         res = res // 2
#
#     print(f'#{tc+1} {result}')


# 다른 풀이
def enq(n):
    global last
    last += 1                                   # 완전 이진 트리 유지 (마지막 정점 추가)
    tree[last] = n
    c = last                                    # 새 정점을 자식으로
    p = c // 2                                  # 부모노드
    while p > 0 and tree[p] > tree[c]:          # 부모가 존재하고, 최소힙 규칙에 어긋나면(= 부모값이 더 크면)
        tree[p], tree[c] = tree[c], tree[p]
        c = p                                   # 부모를 새로운 자식으로
        p = c // 2


T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N+1)
    last = 0                                     # 합의 마지막 정점
    for x in arr:
        enq(x)
    print(tree)

    result = 0
    res = N // 2
    while 1:
        result += tree[res]
        if res == 1:
            break
        res = res // 2

    print(f'#{tc+1} {result}')