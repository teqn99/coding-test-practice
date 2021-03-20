"""
- 첫째 줄에 0과 1로만 이루어진 문자열 S가 주어집니다. S의 길이는 100만보다 작습니다.
- 첫째 줄에 다솜이가 해야 하는 행동의 최소 횟수를 출력합니다.
"""
# 입력받은 문자열 값들의 반복되는 수를 줄인다.
# 0과 1의 갯수를 세서, 적은 값을 답으로 리턴한다.

number = list(map(int, list(input())))
print(number)
tmp = -1

for idx, val in enumerate(number):
    if tmp == val:
        number[idx] = -1
    else:
        tmp = val

one = number.count(1)
zero = number.count(0)

print(min(one, zero))