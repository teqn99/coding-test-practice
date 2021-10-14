from itertools import product, permutations, combinations_with_replacement

N, M = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]
N_dice = [1]*N

if M == 1:
    M_list = list(product(dice, repeat=N))
elif M == 2:
    M_list = list(combinations_with_replacement(dice, N))
else:
    M_list = list(permutations(dice, N))

for i in range(len(M_list)):
    for j in range(N):
        print(M_list[i][j], end=' ')
    print()