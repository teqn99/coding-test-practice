"""
- 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 20)
- 첫째 줄에 만들어질 수 있는 가장 큰수를 출력합니다.
"""
# 입력받은 문자열을 리스트로 변환하고, 정수형으로 변경해주어 숫자로 사용한다.
# 리스트를 내림차순 정렬해준 후 연산을 취한다.
# 0이나 1이 아니면 모두 곱셈연산을 사용하고, 0이나 1은 덧셈연산을 사용한다.

number = list(map(int, list(input())))
number.sort(reverse = True)
result = 0

for i in number:
    if i == 0 or i == 1:
        result += i
    else:
        if result == 0:
            result += 1
        result *= i

print(result)