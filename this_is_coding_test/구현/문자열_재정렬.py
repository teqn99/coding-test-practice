s = list(input())
# 문자열과 숫자를 저장할 리스트를 각각 생성
s_list = []
num_list = []

for i in s:
    if i.isdigit():  # i가 숫자라면 num_list에 저장
        num_list.append(int(i))
    else:  # i가 문자라면 s_list에 저장
        s_list.append(i)

s_list.sort()  # 문자열 리스트 정렬
num = sum(num_list)  # 숫자는 총 합을 계산

print(''.join(s_list) + str(num))  # 형식에 맞게 출력