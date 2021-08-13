T = int(input())
for tc in range(T):
    N, S = input().split()
    dic = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    num_list = list(map(str, input().split()))
    num_list.sort(key=lambda x: dic[x])

    print(N)
    for i in range(int(S)):
        print(num_list[i], end=' ')