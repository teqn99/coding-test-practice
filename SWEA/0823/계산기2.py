for tc in range(10):
    N = int(input())
    cal = input()
    stack = []
    tokens = []
    result = []
    
    # 후위 표기법 적용
    for i in range(N):
        if '0' <= cal[i] <= '9':
            tokens.append(int(cal[i]))
        else:
            if cal[i] == '*':
                while stack and stack[-1] == '*':
                    tokens.append(stack.pop())
            else:  # '+'인 경우
                while stack:
                    tokens.append(stack.pop())
            stack.append(cal[i])

    while stack:  # stack이 비어있지 않을 수 있기 때문
        tokens.append(stack.pop())

    # 계산
    for i in tokens:
        if i in range(0, 10):
            result.append(i)
        else:
            if i == "+":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 + p1)
            elif i == "*":
                p1 = result.pop()
                p2 = result.pop()
                result.append(p2 * p1)

    print(f"#{tc+1} {result[-1]}")
