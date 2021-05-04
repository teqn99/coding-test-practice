N = int(input())
score_list = []

for _ in range(N):
    score_list.append(list(input().split()))
for i in range(N):
    for j in range(1,4):
        score_list[i][j] = int(score_list[i][j])

sorted_score_list = sorted(score_list, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for score in sorted_score_list:
    print(score[0])