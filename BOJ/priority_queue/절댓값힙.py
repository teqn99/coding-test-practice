import sys
import heapq


N = int(input())
arr = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num:  # num이 0이 아닌 경우
        heapq.heappush(arr, [abs(num), num])
    else:  # 0인 경우
        if len(arr) > 0:
            abs_num, origin_num = heapq.heappop(arr)
            print(origin_num)
        else:
            print(0)