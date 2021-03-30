n = list(input())
# 가운데를 기준으로 왼쪽과 오른쪽의 값들을 나눌 리스트를 생성
left = []
right = []

for i in range(len(n)):
    if i < len(n) // 2:  # 반으로 나눠서 왼쪽편에 저장할 값들
        left.append(n[i])
    else:  # 반으로 나눠서 오른편에 저장할 값들
        right.append(n[i])

left = list(map(int, left))
right = list(map(int, right))

if sum(left) == sum(right):
    print('LUCKY')
else:
    print('READY')