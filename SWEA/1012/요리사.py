from itertools import combinations


for tc in range(1, int(input())+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    result = 987654321

    for a in combinations(range(N), N//2):
        A, B = 0, 0
        b = [i for i in range(N) if i not in a]  # a에서 절반만큼을 사용했으면, b에서 나머지 절반만큼을 사용한다.
        for i in range(N//2 - 1):
            for j in range(i+1, N//2):
                A += S[a[i]][a[j]] + S[a[j]][a[i]]
                B += S[b[i]][b[j]] + S[b[j]][b[i]]
        gap = abs(A - B)
        if result > gap:
            result = gap

    print(f'#{tc} {result}')