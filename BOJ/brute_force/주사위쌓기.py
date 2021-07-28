dice_num = int(input())
dice_list = []
result_list = [0]*dice_num
for i in range(dice_num):
    dice_list.append(list(map(int, input().split())))
rotate = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}

sum_result = []
for i in range(6):
    # 1층 주사위
    max_list = []
    dice = [1, 2, 3, 4, 5, 6]
    bottom = dice_list[0][i]
    top = dice_list[0][rotate[i]]
    dice.remove(bottom)
    dice.remove(top)
    max_list.append(max(dice))
    for j in range(1, dice_num):
        # 나머지 위층 주사위
        dice = [1, 2, 3, 4, 5, 6]
        bottom = top
        dice.remove(bottom)
        top = dice_list[j][rotate[dice_list[j].index(top)]]
        dice.remove(top)
        max_list.append(max(dice))
    # sum_result에 max합을 저장
    sum_result.append(sum(max_list))

print(max(sum_result))