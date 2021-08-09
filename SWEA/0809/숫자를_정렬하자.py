T = int(input())
for i in range(T):
    N = int(input())
    test_list = list(map(int, input().split()))
    test_list.sort()
    print(f'#{i+1}', end=' ')
    for j in test_list:
        print(j, end=' ')
    print()