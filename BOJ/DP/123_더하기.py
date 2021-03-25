n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

m = max(num_list)
for i in range(4, m + 1):
    d[i] = d[i - 1] + d[i - 2] + d[i -3]

for i in range(n):
    print(d[num_list[i]])