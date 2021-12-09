def solution(record):
    answer = []
    username = {}

    for i in range(len(record)):
        tmp = record[i].split()
        if tmp[0][0] == 'E':  # Enter
            username[tmp[1]] = tmp[2]
            answer.append(tmp)
        elif tmp[0][0] == 'L':  # Leave
            answer.append(tmp)
        else:  # Change
            username[tmp[1]] = tmp[2]

    for i in range(len(answer)):
        if answer[i][0][0] == 'E':  # Enter
            answer[i] = f'{username[answer[i][1]]}님이 들어왔습니다.'
        else:  # Leave
            answer[i] = f'{username[answer[i][1]]}님이 나갔습니다.'

    return answer