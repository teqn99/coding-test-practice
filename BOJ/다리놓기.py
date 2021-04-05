def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    result = factorial(m) // (factorial(m-n)*factorial(n))  # nCm (조합 사용)
    print(result)