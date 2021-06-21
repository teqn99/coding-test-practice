city = int(input())
distances = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

result = oil_price[0]*distances[0]
ckpt = oil_price[0]

for i in range(1, len(oil_price)-1):
    if ckpt > oil_price[i]:
        ckpt = oil_price[i]
    result += ckpt*distances[i]

print(result)