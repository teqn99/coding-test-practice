# u와 v를 나누는 함수
def divide(w):
    cnt = 0
    u, v = '', ''

    for i in range(len(w)):
        if w[i] == '(':
            cnt += 1
            u += w[i]
        else:
            cnt -= 1
            u += w[i]
        if cnt == 0:
            break

    v = w[i+1:]
    return u, v


# u가 올바른 괄호 문자열인지 확인하는 함수
def right(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p)
        else:
            if not stack:
                return False
            stack.pop()

    return True


def solution(w):
    # 과정 1
    if w == '':
        return ''

    # 과정 2
    u, v = divide(w)

    # 과정 3
    if right(u):
        # 과정 3-1
        return u + solution(v)

    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'

        # 과정 4-4
        for p in u[1: len(u)-1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 과정 4-5
        return answer