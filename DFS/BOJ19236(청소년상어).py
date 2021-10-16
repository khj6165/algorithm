import sys
from copy import deepcopy

input = sys.stdin.readline
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

def dfs(x, y, d, cnt):
    global ans, data, fish
    # 물고기 이동
    move_fish(x, y)
    # 상어 이동
    while True:  # 현재 방향으로 1 ~ 3칸 이동
        nx, ny = x + dx[d], y + dy[d]
        if not 0<=nx<4 or not 0<=ny<4:  # 상어가 이동할 수 없으면 종료한다
            ans = max(ans, cnt)
            return
        if not data[nx][ny]:  # 물고기가 없으면 다음 이동으로
            x, y = nx, ny  # 위치갱신
            continue
        # 물고기가 존재하고 이동할 수 있는 위치임.
        temp_data, temp_fish = deepcopy(data), deepcopy(fish)
        temp1, temp2 = fish[data[nx][ny][0]], data[nx][ny]  #새로운 칸에 있는 물고기의 위치[x, y], [물고기번호, 방향]
        fish[data[nx][ny][0]], data[nx][ny] = [], []  # 물고기 잡아먹음
        dfs(nx, ny, temp2[1], cnt + temp2[0])
        data, fish = temp_data, temp_fish
        fish[data[nx][ny][0]], data[nx][ny] = temp1, temp2
        x, y = nx, ny

def move_fish(sx, sy):
    for i in range(1, 17):
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            for _ in range(9):
                nx, ny = x + dx[data[x][y][1]], y + dy[data[x][y][1]]
                if not 0<=nx<4 or not 0<=ny<4 or (nx == sx and ny == sy):  # 범위를 벗어나거나, 상어가 있는 위치이면
                    data[x][y][1] = (data[x][y][1] % 8) + 1  # 방향 한칸 바꿔서
                    continue
                if data[nx][ny]:  # 이동칸에 물고기가 존재하면
                    fish[data[nx][ny][0]] = [x, y]  # 새로갈 자리의 물고기 위치를 현재위치로 옮김
                data[nx][ny], data[x][y] = data[x][y], data[nx][ny]  # 지도정보 교환
                fish[i] = [nx, ny]  # 현재 물고기를 새로운 위치로 옮김
                break  # 다음물고기로 넘어감


data = [[] for _ in range(4)]  # 4x4지도에 물고기 번호와 방향 저장
fish = [[] for _ in range(17)]  # 16마리 물고기의 위치, 방향정보 저장
fish[0] = [0, 0]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(0, 7, 2):
        data[i].append([temp[j], temp[j+1]])  # [물고기번호, 방향] 4x4
        fish[temp[j]] = [i, j//2]  # 물고기 번호 인덱스에 [x, y] 위치 저장

ans = 0
d, cnt = data[0][0][1], data[0][0][0]   # 상어의 초기 방향, 먹은 물고기
fish[data[0][0][0]], data[0][0] = [], []  # 잡아먹힌 물고기정보와 지도정보 초기화
dfs(0, 0, d, cnt)  # 상어의 위치 방향, 먹은 물고기 인자로 넘겨주기
print(ans)
#0. 초기 상어 (0,0) 물고기 먹고 방향가짐
#1. 물고기 이동함수(구현)
#2. 상어 이동(여러 후보) 이동할수없는 칸이 있으면 종료. -> 1.물고기 이동
