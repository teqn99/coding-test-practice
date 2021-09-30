import sys
sys.stdin = open('1.txt', 'r')


# 코드는 0101의 비율 구조로 이루어져있기 때문에, 0부분을 제외한 101의 비율로 코드를 해독하기 위한 딕셔너리
ratio = {
    '211': 0,
    '221': 1,
    '122': 2,
    '411': 3,
    '132': 4,
    '231': 5,
    '114': 6,
    '312': 7,
    '213': 8,
    '112': 9,
}
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for i in range(N)]
    arr = list(set(arr))  # 열 중복 제거
    N2 = len(arr)

    # temp에 변환된 숫자 저장
    temp = [''] * N2
    for i in range(N2):
        for j in range(M):
            sub = str(bin(int(arr[i][j], 16))[2:])
            while len(sub) < 4:
                sub = '0' + sub
            temp[i] += sub

    # 0으로만 이루어진 행 제거
    cleaned = []
    for x in temp:
        if int(x) != 0:
            cleaned.append(x)

    ans = 0
    visited = []
    for binary in cleaned:
        decode = []
        a = b = c = 0  # 암호 비율
        binary = binary.rstrip('0')  # 뒤에서부터 탐색, 0 제거
        L = len(binary)
        for i in range(L - 1, -1, -1):  # 맨 뒤부터 거꾸로 탐색
            if b == 0 and binary[i] == '1':  # 처음 1을 만났을때 d의 개수 증가
                c += 1
            elif c > 0 and a == 0 and binary[i] == '0':  # 그다음 0 찾으면
                b += 1
            elif b > 0 and binary[i] == '1':
                a += 1
            elif a > 0 and binary[i] == '0':  # 뒤에서부터 101을 찾고 그다음 0일 때 코드 해독하기
                temp = min(a, b, c)  # 비율 일치 시키기
                a //= temp
                b //= temp
                c //= temp
                key = str(a) + str(b) + str(c)
                decode = [ratio[key]] + decode  # 거꾸로 진행 중이었으므로, 추가도 거꾸로 해준다.
                a = b = c = 0  # 사용완료되었으므로 초기화

                # 계산으로 옳은 코드인지 여부 확인
                if len(decode) == 8:
                    if decode not in visited:
                        visited.append(decode)
                        even = 0
                        odd = 0
                        for j in range(8):
                            if j % 2:
                                odd += decode[j]
                            else:
                                even += decode[j]
                        if (even * 3 + odd) % 10 == 0:
                            ans += sum(decode)
                    decode = []

    print(f'#{tc} {ans}')