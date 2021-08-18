T = int(input())
for tc in range(T):
    makdae = input()
    result = 0
    cnt = 0  # 막대의 개수를 카운트하기 위한 변수
    for i in range(len(makdae)):
        if makdae[i] == '(':  # 막대가 새로 시작되는 경우
            cnt += 1
        else:  # 막대가 끝나거나 레이저인 경우
            if i > 0 and makdae[i-1] == '(' and makdae[i] == ')':
                cnt -= 1  # ()인 경우는 레이저인 경우인데, (를 하면서 cnt += 1을 해줬기 때문에 하나를 빼야 한다.
                result += cnt
            else:  # 막대 하나가 끝난 경우
                cnt -= 1
                result += 1

    print(f'#{tc+1} {result}')
