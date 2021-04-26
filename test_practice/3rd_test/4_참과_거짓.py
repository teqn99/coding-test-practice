"""
스미드 교수는 논리 수업을 가르친다. 어느 날 그는 다음과 같은 문장을 칠판에 썼다.
이 문장들 중 정확히 a개의 문장이 참이다.
이 문장들 중 정확히 b개의 문장이 참이다.
이 문장들 중 정확히 c개의 문장이 참이다.
.
.
.
a, b, c 등은 각각 숫자이다. 그리고 그는 학생들에게 이 중 몇개의 문장이 참인지 물어보았다.

주어진 정수 배열 statements에 Smith 교수가 쓴 숫자들이 적혀있다. 모두 몇 개의 문장이 참인지 리턴하시오.
만약 가능한 답이 두개 이상이라면 그 중 더 큰 숫자를 반환하여라. 가능한 답이 없다면 -1을 리턴하시오.


참고 / 제약 사항
statements는 1개 이상, 50개 이하의 요소를 가지고 있다.
statements의 각 요소는 0 이상, 50 이하이다.
"""
class Solution:
    def solution(self, statements):
        result = []
        maxi = max(statements)
        for i in range(1, maxi + 1):
            if statements.count(i) == i:
                result.append(i)

        if result == []:
            if 0 in statements:
                return -1
            else:
                return 0

        return max(result)

"""
statements에 모든 값들이 다른 값이다 -> 1을 부른 사람이 참을 말한다 -> 1을 부른 사람이 없다 -> 답이 없다...
같은 수만큼의 같은 값들이 존재한다(ex. 3이 3개) -> 같은 값을 부른 사람들이 참이다.
같은 값은 있지만 수가 그 값보다 적다(ex. 3이 2개) -> 같은 값이 답이 될 수 없다
같은 값은 있지만 수가 그 값보다 많다(ex. 3이 4개) -> 같은 값이 답이 될 수 없다
"""
def solution(statements):
    result = []
    maxi = max(statements)
    for i in range(1, maxi + 1):
        if statements.count(i) == i:
            result.append(i)
    if result == []:
        if 0 in statements:
            return -1
        else:
            return 0
    print(result)
    return max(result)

s = solution([1, 1])
print(s)

[0, 1] -> 1

