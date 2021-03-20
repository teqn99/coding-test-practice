"""
현재 1부터 N까지의 정수가 한번씩 등장하는 길이 N의 수열이 있다.
여기서 당신은 연속된 K개의 정수를 골라서 한 곳에 잠시  모아둘 수 있다.
시간이 지나면 당신이 고른 K 개의 정수들은 K개중 가장 작은 정수가 된다. 이 시간은 고려하지 않는다.
여기서 이 수열을 모두 같은 수로 만들고자 할 때 최소 몇번 골라야 하는지 구하는 프로그램을 작성하시오.

예를 들어 4개의 수가 [2,3,1,4] 와 같이 있고 K = 3 일때, [2,3.1,4]을 고르게 되면 세수는 2,3,1 중 가장 작은 수인 1로 변하게된다.
이후 [1,1,1,4] 가 된다. 아직 4가 남았으니 [1,1,1,4]를 고르게 되면 [1,1,1,1] 이 되고 총 2번만에 모두 같은수로 만드는데 성공이다.


[입력 형식]
첫 줄에 공백으로 구분된 두 정수 N, K 가 차례로 주어진다.
-        N은 수열의 길이를 나타내는 2 이상 10만 이하의 자연수다.
-        K는 한 번에 연속적으로 골라야 하는 정수의 개수를 나타내는 2 이상 N 이하의 자연수이다.

두 번째 줄에는 공백으로 구분된 N개의 정수가 주어진다.
-        각 정수는 1부터 N까지의 정수중 하나이며, 같은 정수가 두번이상 나타나지 않는다.

[출력 형식]
주어진 수열을 모두 같은 수로 만들고자 할 때 골라야 하는 최소 횟수를 출력한다.
예시
4 3
2 3 1 4
출력
2

예시
37 4
31 36 20 30 1 9 6 13 3 29 11 25 7 8 2 24 34 18 26 15 23 28 37 19 21 4 32 14 16 10 12 27 22 35 5 17 33
출력
12
"""

n, k = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

i = 0
result = 0
check_point = 0
tmp = num_list[0]

while True:
    for j in range(k):
        if (j + i) >= len(num_list) - 1:
            check_point = 1
            break
        num_list[j + i] = tmp

    i += (k - 1)
    result += 1
    if check_point == 1:
        break

print(result)