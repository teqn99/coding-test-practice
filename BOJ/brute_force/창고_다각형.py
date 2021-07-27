N = int(input())
bar_list = []
for i in range(N):
    bar_list.append(list(map(int, input().split())))

bar_list = sorted(bar_list, key = lambda x: x[0])
print(bar_list)

maxi_x, maxi_y = 0, 0
maxi_idx = 0
for i in range(len(bar_list)):
    if maxi_x < bar_list[i][0]:
        maxi_x = bar_list[i][0]
    if maxi_y < bar_list[i][1]:
        maxi_y = bar_list[i][1]
        maxi_idx = i
print(maxi_idx)

grid = [0] * (maxi_x + 1)
for x, y in bar_list:
    grid[x] = y
print(grid)

result = 0
tmp = grid[0]
for i in range(grid.index(maxi_y)+1):
    if tmp < grid[i]:
        tmp = grid[i]
    result += tmp

print(result)
print('here')

tmp = grid[-1]
for i in range(len(grid)-1, grid.index(maxi_y), -1):
    if tmp < grid[i]:
        tmp = grid[i]
    result += tmp

print(result)
print('here')











tmp = bar_list[0]
for i in range(maxi_idx+1):
    if tmp[1] < bar_list[i+1][1]:
        result += (bar_list[i+1][0] - tmp[0]) * tmp[1]
        tmp = bar_list[i+1]
        print(result)
    else:
        tmp = bar_list[i]


tmp = bar_list[len(bar_list)-1]
for i in range(len(bar_list)-1, maxi_idx, -1):
    if tmp[1] < bar_list[i-1][1]:
        result += (bar_list[i-1][0] - tmp[0]) * tmp[1]
        tmp = bar_list[i-1]
        print(result)
    else:
        tmp = bar_list[i]



# print(result)

# for j in range(len(bar_list), maxi_x, -1):
#     if tmp[1] > bar_list[j+1][1]:
#         result += (bar_list[j+1][0] - tmp[0]) * tmp[1]
#         tmp = bar_list[j+1]
#         print(result)
#         if tmp[1] == maxi_y:
#             break
#     else:
#         tmp = bar_list[j]