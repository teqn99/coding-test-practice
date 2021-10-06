def f1(i, N):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += A[j]
        if s == 10:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i+1, N)
        bit[i] = 1
        f1(i+1, N)


def f2(i, N, s, rs):
    global cnt
    cnt += 1
    if i == N:
        if s == 50:
            for j in range(N):
                if bit[j]:
                    print(A[j], end=' ')
            print()
    elif s > 50:  # 호출횟수를 줄이기 좋은 부분
        return
    elif s + rs < 50:  # 나머지 애들 합해봐야 50 안넘을 건데 할 필요가 없다..
        return
    else:
        bit[i] = 0
        f2(i+1, N, s, rs-A[i])
        bit[i] = 1
        f2(i+1, N, s+A[i], rs-A[i])


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0]*10
# f1(0, 10)

cnt = 0  # 호출횟수 체크용
f2(0, 10, 0, sum(A))
print(cnt)