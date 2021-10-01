def perm(N, R, i):
    if i == R:
        print(p)
    else:
        for j in range(N):
            if not used[j]:
                p[i] = arr[j]
                used[j] = True
                perm(N, R, i+1)
                used[j] = False


N = 5
R = 3
arr = [1, 2, 3, 4, 5]
used = [False]*N
p = [0]*R
perm(N, R, 0)
