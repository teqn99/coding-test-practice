n = int(input())
chk = 0

for k in range(n):
    num_list = list(map(int, list(str(k))))
    result = 0
    for i, v in enumerate(num_list):
        result += v * (10**(len(num_list)-1-i))
    if result + sum(num_list) == n:
        chk = 1
        break

if chk == 1:
    print(result)
else:
    print(0)