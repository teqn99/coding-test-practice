import numpy as np

def rotated(a):  # 오른쪽으로 90도 회전
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]

    return result


def rotated2(a):
    rotate2 = list(zip(*a))  # *: 변수안에 있는 원소들을 뽑아오는 키(?)
    return rotate2


def solution(key, lock):
    m, n = len(key), len(lock)
    padding = np.zeros(shape=(m * 2 + n))

    # 자물쇠 중앙 배치
    for i in range(n):
        for j in range(n):
            padding[m + i][m + j] = lock[i][j]

    # 키와 결합한 자물쇠와 np.ones()를 비교 -> 일치하면 return 'True'

print(rotated([[0,0,0],[1,0,0],[0,1,1]]))