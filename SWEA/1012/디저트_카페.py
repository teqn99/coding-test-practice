def go(si, sj, i, j, length, directions):
    global result
    if length != 0 and i == si and j == sj:
        if length == 2:
            return
        if result < length:
            result = length
        return
    for di, dj in [(1, 1), (1, -1), (-1, -1), (-1, 1)]:
        if (di, dj) in directions:  # 이미 진행했던 방향으로는 진행하지 못한다!! (사각형을 만들어야 하기 때문에)
            if (di, dj) == directions[-1]:  # 하지만, 마지막까지 진행하고 있던 방향으로 다시 가는 건 가능하다!!
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if dessert[ni][nj] not in ate:
                        ate.append(dessert[ni][nj])
                        directions.append((di, dj))
                        go(si, sj, ni, nj, length+1, directions)
                        directions.pop()
                        ate.pop()
                    else:
                        if ni == si and nj == sj:
                            ate.append(dessert[ni][nj])
                            directions.append((di, dj))
                            go(si, sj, ni, nj, length+1, directions)
                            directions.pop()
                            ate.pop()
            else:
                return
        else:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N:
                if dessert[ni][nj] not in ate:
                    ate.append(dessert[ni][nj])
                    directions.append((di, dj))
                    go(si, sj, ni, nj, length+1, directions)
                    directions.pop()
                    ate.pop()
                else:
                    if ni == si and nj == sj:
                        ate.append(dessert[ni][nj])
                        directions.append((di, dj))
                        go(si, sj, ni, nj, length+1, directions)
                        directions.pop()
                        ate.pop()


for tc in range(1, int(input())+1):
    N = int(input())
    dessert = [list(map(int, input().split())) for _ in range(N)]
    ate = []
    result = -1

    for i in range(N):
        for j in range(N):
            ate.append(dessert[i][j])
            go(i, j, i, j, 0, [])
            ate.pop()

    print(f'#{tc} {result}')