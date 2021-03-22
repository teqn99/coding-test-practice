"""
- 첫째 줄에 모험가의 수 N이 주어집니다. (1 <= N <= 100000)
- 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
- 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.
"""
# 멤버의 리스트를 입력받아 정렬한다.
# 정렬된 리스트를 for문으로 검사하며, 사이즈를 재는 변수를 두어 사이즈에 맞는 멤버 수만큼 그룹에 넣어준다.
# 그룹의 길이를 리턴한다.

n = map(int, input())
member_list = list(map(int, input().split()))
group = []
group_size = 0

member_list.sort()
for member in member_list:
    group_size += 1
    if group_size == member:
        group_size = 0
        group.append(member)

print(len(group))