n = int(input())
number = 666
while True:
    if '666' in str(number):
        n -= 1
        if n == 0:
            break
    number += 1

print(number)