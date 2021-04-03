def solution(new_id):
    # 1단계
    new_id = new_id.lower()

    # 2단계
    new_id = list(new_id)
    for i in range(len(new_id)):
        if not(new_id[i].isalpha()) and not(new_id[i].isdigit()) and new_id[i] not in ['-','_','.']:
            new_id[i] = ''
        # if문에 isalpha랑 isdigit랑 따로 하지 말고 -> isalnum을 써라! (생각도 몬함)
    new_id = ''.join(new_id)

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')

    # 4단계
    if len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 5단계
    if new_id == '':
        new_id = 'a'

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

s = solution('...!@BaT#*..y.abcdefghijklm')
print(s)