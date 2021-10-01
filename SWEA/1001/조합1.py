# 10개 중 3개를 고르는 조합
# i < j < k인 경우
# 10C3 = 120가지의 결과가 나올 것
cnt = 0
for i in range(8):
    for j in range(i+1, 9):
        for k in range(j+1, 10):
            print(i, j, k)
            cnt += 1
print(cnt)