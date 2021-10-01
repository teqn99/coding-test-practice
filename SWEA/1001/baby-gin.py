def f(i, n):
    global ans
    if i == n:
        print(arr)
        run, tri = 0, 0
        if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
            run += 1
        if arr[0] == arr[1] == arr[2]:
            tri += 1
        if arr[3] + 1 == arr[4] and arr[4]+ 1 == arr[5]:
            run += 1
        if arr[3] == arr[4] == arr[5]:
            tri += 1
        if run + tri == 2:
            ans = 1
    else:
        for j in range(i, n):
            arr[i], arr[j] = arr[j], arr[i]
            f(i+1, n)
            arr[i], arr[j] = arr[j], arr[i]


arr = list(map(int, input()))
ans = 0
f(0, 6)
print(ans)