def solution(lottos, win_nums):
    answer = []
    cnt = 0
    for i in range(len(lottos)):
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                cnt += 1
    zeros = lottos.count(0)
    cnt_max = cnt + zeros
    win_dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer.append(win_dic[cnt_max])
    answer.append(win_dic[cnt])
    return answer