T = int(input())
for tc in range(T):
    tokens = list(input().split())
    stack = []

    for i in tokens:
        if i.isdigit():
            stack.append(int(i))
        else:
            if i == '.':
                if len(stack) == 1:
                    print(f'#{tc + 1} {stack[-1]}')
                else:
                    print(f'#{tc + 1} error')
            elif len(stack) >= 2:
                p1 = stack.pop()
                p2 = stack.pop()
                if i == '+':
                    stack.append(p2+p1)
                elif i == '*':
                    stack.append(p2*p1)
                elif i == '-':
                    stack.append(p2-p1)
                elif i == '/':
                    stack.append(p2//p1)
            else:
                print(f'#{tc + 1} error')
                break
