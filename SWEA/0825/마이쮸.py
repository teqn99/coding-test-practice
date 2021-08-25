from collections import deque

#[줄에 선 횟수, 가져온 마이쮸 총 개수]의 형태
people = {'1': [1, 0], '2': [1, 0], '3': [1, 0], '4': [1, 0], '5': [1, 0], '6': [1, 0], '7': [1, 0], '8': [1, 0], '9': [1, 0], '10': [1, 0]}
queue = deque()
chu = 20  # 마이쮸 20개

num = list(map(str, range(1, 11)))
a = 0
while chu > 0:
    queue.append(num[a])
    a += 1
    poped = queue.popleft()
    chu -= people[str(poped)][0]
    people[str(poped)][1] += people[str(poped)][0]
    people[str(poped)][0] += 1
    queue.append(poped)
    if a > 9:
        a = 0
    print(queue)
    print(chu, people, poped)

# 마지막에 받은 사람
print(poped)