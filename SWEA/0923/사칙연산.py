def postorder(n):
    global sik
    if sign[n] == 0:
        sik.append(tree[n])
        return
    postorder(sign[n][0])
    postorder(sign[n][1])
    sik.append(tree[n])


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)
    sign = [0] * (N+1)
    for i in range(N):
        node = list(input().split())
        if len(node) == 4:
            tree[int(node[0])] = node[1]
            sign[int(node[0])] = [int(node[2]), int(node[3])]
        else:
            tree[int(node[0])] = node[1]

    sik = []
    postorder(1)

    stack = []
    for i in sik:
        if i.isdigit():
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == '+':
                stack.append(b+a)
            elif i == '-':
                stack.append(b-a)
            elif i == '*':
                stack.append(b*a)
            else:
                stack.append(b//a)

    print(f'#{tc} {stack.pop()}')