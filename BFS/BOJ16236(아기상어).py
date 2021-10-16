from collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    q = deque()
    q.append([x, y])
    check[x][y] = True
    dist[x][y] = 0

    while q:
        curx, cury = q.popleft()
        for i in range(4):
            nextx = curx + dx[i]
            nexty = cury + dy[i]
            if 0<=nextx<n and 0<=nexty<n and not check[nextx][nexty] and data[nextx][nexty] <= level:  # 이동 조건
                dist[nextx][nexty] = dist[curx][cury] + 1
                q.append([nextx, nexty])
                check[nextx][nexty] = True


for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            x, y = i, j
            data[i][j] = 0
level = 2
cnt = 2  # 레벨업까지 먹어야할 물고기수
time = 0
while True:
    # 초기화
    check = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    # 먹을수있는 물고기 있는 최단거리로 이동
    # 1. 먹을 수 있는 가까운 물고기 탐색
    bfs()
    minvalue = 999
    for i in range(n):
        for j in range(n):
            if data[i][j] < level and check[i][j] and data[i][j] != 0:  # 차례로 1)레벨이 다높음 2)도달할수없음 3)물고기가 없음
                if minvalue > dist[i][j]:
                    minvalue = dist[i][j]
                    x, y = i, j

    if minvalue == 999:  # 먹을수있는 물고기가 없다
        break
    data[x][y] = 0
    time += minvalue
    cnt -= 1

    if cnt == 0:
        level += 1
        cnt = level

print(time)



