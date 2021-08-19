T = int(input())
for tc in range(T):
    s = input()
    stack = [s[0]]

    for i in range(1, len(s)):
        stack.append(s[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()

    print(f'#{tc+1} {len(stack)}')