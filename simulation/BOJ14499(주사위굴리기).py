n, m, x, y, k = map(int, input().split())
mymap = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split())) # 동서북남 1234
ud = [0, 0, 0, 0]  # 위, 앞, 아래, 뒤
rl = [0, 0, 0, 0]  # 오른, 아래, 왼, 위

for o in order:
    if o == 1 and 0 <= y + 1 < m:
        y = y + 1
        rl.insert(0, rl.pop())
        ud[0] = rl[3]
        ud[2] = rl[1]
    elif o == 2 and 0 <= y - 1 < m:
        y = y - 1
        rl.append(rl[0])
        del rl[0]
        ud[0] = rl[3]
        ud[2] = rl[1]
    elif o == 3 and 0 <= x - 1 < n:
        x = x - 1
        ud.append(ud[0])
        del ud[0]
        rl[1] = ud[2]
        rl[3] = ud[0]
    elif o == 4 and 0 <= x + 1 < n:
        x = x + 1
        ud.insert(0, ud.pop())
        rl[1] = ud[2]
        rl[3] = ud[0]
    else:
        continue
    # 복사하기
    if mymap[x][y] == 0:  # 지도에 복사하기
        mymap[x][y] = ud[2]
    else:  # 주사위에 복사하기
        ud[2] = mymap[x][y]
        rl[1] = mymap[x][y]
        mymap[x][y] = 0
    print(ud[0])



