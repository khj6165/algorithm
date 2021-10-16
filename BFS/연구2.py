from itertools import combinations
from collections import deque

def spread(active_v):
    global virus_x, virus_y
    # 초기화
    visited = [[False] * n for _ in range(n)]
    table = [[999] * n for _ in range(n)]

    queue = deque()
    # 바이러스의 시작지점이 여러개
    for i in range(m):
        ex = virus_x[active_v[i]-1]
        ey = virus_y[active_v[i]-1]
        queue.append([ex, ey])
        visited[ex][ey] = True
        table[ex][ey] = 0

    while(queue):
        x, y = queue.popleft()
        # 상하좌우 퍼지게하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 벗어나는 경우, 벽일 경우 제외하고 방문하지 않은 곳 방문
            if nx >= 0 and nx < n and 0 <= ny and ny < n and data[nx][ny] != 1 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True
                table[nx][ny] = table[x][y]+1

    # 한번도 방문하지 않은 곳 있는지 확인
    ret = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] != 1:
                if table[i][j] == 999:
                    return 999
                else:
                    ret = max(ret, table[i][j])
    return ret

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
virus_x = []
virus_y = []
virus = []
active = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
result = 999

for i in range(n):
    for j in range(n):
        if data[i][j] == 2:
            cnt += 1
            virus_x.append(i)
            virus_y.append(j)
            virus.append(cnt)

active = combinations(virus, m)
for i in active:
    time = spread(list(i))
    result = min(time, result)

if result == 999:
    print(-1)
else:
    print(result)