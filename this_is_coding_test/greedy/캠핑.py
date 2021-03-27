LPV_list = []
# 입력
while True:
    LPV_list.append(list(map(int, input().split())))
    if LPV_list[-1] == [0, 0, 0]:
        break

# 계산 후 출력
for i in range(len(LPV_list) - 1):
    result_modulo = min(LPV_list[i][2] % LPV_list[i][1], LPV_list[i][0])  # V % P와 L 중 작은 값
    result_divide = (LPV_list[i][2] // LPV_list[i][1]) * LPV_list[i][0]  # (V // P) * L
    result = result_divide + result_modulo
    print(f'Case {i + 1}: {result}')