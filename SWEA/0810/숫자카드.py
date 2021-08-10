T = int(input())
for tc in range(T):
    N = int(input())
    card_list = list(map(int, input()))
    card_list.sort()
    idx, cnt = 0, 0

    for i in range(N):
        if card_list.count(card_list[i]) >= cnt:
            cnt = card_list.count(card_list[i])
            idx = card_list.index(card_list[i])

    print(f'#{tc+1} {card_list[idx]} {cnt}')
