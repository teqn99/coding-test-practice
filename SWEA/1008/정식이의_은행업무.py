for tc in range(1, int(input())+1):
    two = list(input())
    three = list(input())
    two_cases = []
    three_cases = []

    for i in range(len(two)):
        two[i] = '0' if two[i] == '1' else '1'
        two_cases.append(int(''.join(two), 2))
        two[i] = '0' if two[i] == '1' else '1'

    for i in range(len(three)):
        if three[i] == '0':
            three[i] = '1'
            three_cases.append(int(''.join(three), 3))
            three[i] = '2'
            three_cases.append(int(''.join(three), 3))
            three[i] = '0'
        elif three[i] == '1':
            three[i] = '0'
            three_cases.append(int(''.join(three), 3))
            three[i] = '2'
            three_cases.append(int(''.join(three), 3))
            three[i] = '1'
        elif three[i] == '2':
            three[i] = '0'
            three_cases.append(int(''.join(three), 3))
            three[i] = '1'
            three_cases.append(int(''.join(three), 3))
            three[i] = '2'

    ans = ''
    for i in two_cases:
        for j in three_cases:
            if i == j:
                ans = i
                break
        if ans != '':
            break
    print(f'#{tc} {ans}')