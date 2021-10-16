from collections import deque
import sys

def bfs1():
    # 택시가 출발지점까지 도달하는 거리 계산
    q = deque()
    q.append([x-1, y-1])
    check[x-1][y-1] = True
    dist[x-1][y-1] = 0

    while q:
        curx, cury = q.popleft()
        # 상하좌우
        for i in range(4):
            nextx = curx + dx[i]
            nexty = cury + dy[i]
            if nextx>=0 and nextx<n and nexty>=0 and nexty<n and data[nextx][nexty] == 0 and not check[nextx][nexty]:
                q.append([nextx, nexty])
                check[nextx][nexty] = True
                dist[nextx][nexty] = dist[curx][cury] + 1


def bfs2():
    # 초기화
    check = [[False] * n for _ in range(n)]  # 방문여부 저장
    dist = [[0] * n for _ in range(n)]  # 최단 거리 저장
    global charge
    # 출발지점에서 도착지점까지 도달하는 거리 계산
    q = deque()
    q.append([sx-1, sy-1])
    check[sx-1][sy-1] = True
    dist[sx-1][sy-1] = 0

    while q:
        curx, cury = q.popleft()
        # 상하좌우
        for i in range(4):
            nextx = curx + dx[i]
            nexty = cury + dy[i]
            if nextx>=0 and nextx<n and nexty>=0 and nexty<n and data[nextx][nexty] == 0 and not check[nextx][nexty]:
                q.append([nextx, nexty])
                check[nextx][nexty] = True
                dist[nextx][nexty] = dist[curx][cury] + 1
                if nextx == x-1 and nexty == y-1:
                    charge = dist[nextx][nexty]
                    return True
    return False


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 입력 받을 변수
n, m, fuel = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
passenger = [list(map(int, input().split())) for _ in range(m)]
passenger.sort()  # 시작 행, 렬 빠른 순으로 정렬
flag = 0
for _ in range(m):
    # 초기화
    check = [[False] * n for _ in range(n)]  # 방문여부 저장
    dist = [[0] * n for _ in range(n)]  # 최단 거리 저장

    # bfs1을 통해 도달 가능한 승객들의 최단거리 파악.
    bfs1()

    # 1. 남은 승객들 중 최단거리인 승객 찾기
    minvalue = 999
    for p in passenger:
        if not check[p[0]-1][p[1]-1]:  # 도달할 수 없는 곳에 승객이 있을 경우
            print(-1)
            sys.exit()
        minvalue = min(dist[p[0]-1][p[1]-1], minvalue)

    if fuel < minvalue:  # -1 출력
        flag = 1
        break
    fuel -= minvalue

    # 2. 고른 승객의 도착지점과의 거리를 구한다.
    charge = 0
    for i in range(len(passenger)):
        if dist[passenger[i][0]-1][passenger[i][1]-1] == minvalue:
            sx, sy, x, y = passenger[i][0], passenger[i][1], passenger[i][2], passenger[i][3]
            if bfs2():
                del passenger[i]
                break
            else:
                print(-1)
                sys.exit()
    if fuel < charge:
        flag = 1
        break
    fuel += charge  # 충전

if flag == 1:
    print(-1)
else:
    print(fuel)
