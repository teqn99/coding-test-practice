for tc in range(10):
    N = int(input())
    s = input()
    tokens = []
    stack = []
    result = []

    # 후위표기법 적용
    for i in range(N):
        if s[i].isdigit():
            tokens.append(int(s[i]))
        else:
            if s[i] == ')':
                chk = ''
                while chk != '(':  # '('를 찾을 때까지
                    chk = stack.pop()
                    tokens.append(chk)
                tokens.pop()  # tokens의 마지막에 '('가 들어가버렸으므로
                continue
            elif s[i] == '*':
                while stack and stack[-1] == '*' and stack[-1] != "(":  # '('는 '*'로 뽑아낼 수 없다.:
                    tokens.append(stack.pop())
            elif s[i] == '+':
                while stack and stack[-1] != "(":  # '('는 '+'로 뽑아낼 수 없다.
                    tokens.append(stack.pop())
            stack.append(s[i])

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

    print(f'#{tc+1} {result[-1]}')