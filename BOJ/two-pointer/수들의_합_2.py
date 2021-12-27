N, M = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
left, right = 0, 1

while right <= N and left <= right:
    if sum(arr[left:right]) == M:
        cnt += 1
        right += 1
    elif sum(arr[left:right]) > M:
        left += 1
    else:
        right += 1

print(cnt)