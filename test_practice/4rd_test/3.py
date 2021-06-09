"""
이 문제에서 A0, X, Y, M, n 이 주어진다.
당신은 아래의 규칙에 따라 리스트 A를 만들어야 한다.

A[0] = A0
A[i] = (A[i - 1] * X + Y) MOD M (단, 0 < i < n)

리스트 A에서 절대값의 차가 가장 작은 두 요소의 절대값의 차를 리턴하시오. ( 자세한 내용은 예제 참고 )


참고 / 제약 사항
- 1 <= A0, X, Y, M <= 10000
- 2 <= n <= 10000
"""
def solution(A0, X, Y, M, n):
    A = [0]*n
    results = []
    A[0] = A0
    for i in range(1, n):
        A[i] = (A[i-1]*X+Y) % M

    A.sort()
    for i in range(len(A)):
        if i == len(A)-1:
            break
        result = A[i+1] - A[i]
        results.append(result)

    return min(results)

s = solution(3, 7, 1, 101, 5)
print(s)