n = int(input())
size_list = []
for i in range(n):
    sizes = list(map(int, input().split()))
    size_list.append(sizes)

print(size_list)

for i in size_list:
    rank = 1
    for j in size_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')