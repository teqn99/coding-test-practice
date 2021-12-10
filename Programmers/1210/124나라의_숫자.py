def solution(n):
    answer = ''

    while n:
        num = n % 3
        if not num:
            answer += '4'
            n = n // 3 - 1
        else:
            answer += str(num)
            n = n // 3

    return answer[::-1]