N = int(input())
bar_list = []
for i in range(N):
    bar_list.append(list(map(int, input().split())))
bar_list = sorted(bar_list, key = lambda x: x[0])

maxi_x, maxi_y = 0, 0
for i in range(len(bar_list)):
    if maxi_x < bar_list[i][0]:
        maxi_x = bar_list[i][0]
    if maxi_y < bar_list[i][1]:
        maxi_y = bar_list[i][1]

grid = [0] * (maxi_x + 1)
for x, y in bar_list:
    grid[x] = y

result = 0
tmp = grid[0]
for i in range(grid.index(maxi_y)+1):
    if tmp < grid[i]:
        tmp = grid[i]
    result += tmp

tmp = grid[-1]
for i in range(len(grid)-1, grid.index(maxi_y), -1):
    if tmp < grid[i]:
        tmp = grid[i]
    result += tmp

print(result)