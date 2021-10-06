A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 부분집합의 합이 10이 되는 모든 부분집합을 출력하라

for i in range(1, 1<<10):  # i가 한 개의 부분집합 구성을 나타냄
    s = 0                  # i가 나타내는 부분집합의 합
    for j in range(10):
        if i&(1<<j):       # A[j]가 부분집합에 포함된 경우
            s += A[j]
    if s == 10:
        for j in range(10):
            if i & (1 << j):
                print(A[j], end=' ')
        print()