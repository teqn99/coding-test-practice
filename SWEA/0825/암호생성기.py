for tc in range(10):
    N = int(input())
    password = list(map(int, input().split()))
    minus_num = 1

    while 1:
        p = password.pop(0)  # 처음 위치의 숫자 뽑아오기
        p -= minus_num  # minus_num 만큼 빼주기
        if p <= 0:
            p = 0
            password.append(p)
            break
        minus_num += 1  # minus_num 증가
        if minus_num == 6:
            minus_num = 1  # 사이클 종료로 인한 초기화 작업
        password.append(p)  # 마지막 위치로 이동

    print(f'#{N}', end=' ')
    for i in password:
        print(i, end=' ')
    print()