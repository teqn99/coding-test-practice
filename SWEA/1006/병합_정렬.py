def merge_sort(arr):
    global cnt
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    if left_arr[-1] > right_arr[-1]:
        cnt += 1

    merged_arr = []
    l = r = 0  # 합병정렬은 왼쪽과 오른쪽 리스트를 각각 인덱스 0부터 비교하면서 합치기 때문
    while l < len(left_arr) and r < len(right_arr):
        if left_arr[l] < right_arr[r]:
            merged_arr.append(left_arr[l])
            l += 1
        else:
            merged_arr.append(right_arr[r])
            r += 1
    merged_arr += left_arr[l:]  # while 조건 때문에 전부 가져오지 못한 경우가 있을 수 있다. (이미 정렬되어있는 상태이기 때문에 바로 더해줌.)
    merged_arr += right_arr[r:]  # while 조건에서 어차피 둘 중 하나가 먼저 끝나게 되면 left나 right 중 하나는 완료된 상태이기 때문에 left와 right를 더해주는 순서는 상관없다.

    return merged_arr


for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    merged = merge_sort(arr)

    print(f'#{tc} {merged[N//2]} {cnt}')