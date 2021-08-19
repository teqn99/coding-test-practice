T = int(input())
for tc in range(T):
    s = input()
    stack = []
    ans = 1
    for i in s:
        if i in ['(', '{']:
            stack.append(i)
        elif i == ')':
            if len(stack) > 0 and stack.pop() == '(':
                continue
            else:
                ans = 0
                break
        elif i == '}':
            if len(stack) > 0 and stack.pop() == '{':
                continue
            else:
                ans = 0
                break

    if len(stack) > 0:
        ans = 0
        
    print(f'#{tc + 1} {ans}')
