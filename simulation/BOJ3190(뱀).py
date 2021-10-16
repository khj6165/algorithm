N = int(input())
K = int(input())
direct = [list(map(int, input().split())) for _ in range(K)]
L = int(input())
snake = [list(input().split()) for _ in range(L)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
D_dir = [3, 2, 0, 1] # 방향 인덱스 저장
L_dir = [2, 3, 1, 0]
time = 0
cur_dir= 3
x, y = 0, 0
head, tail = [0, 0], [0, 0]
scar = []
while True:
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    head[0] = nx
    head[1] = ny
    if nx<0 or nx>=N or ny<0 or ny>=N or (head in scar) or (head == tail):
        break
    x = nx
    y = ny
    scar.append([nx, ny])
    if [nx+1, ny+1] in direct:
        direct.remove([nx+1, ny+1]) # 입력받을때각각 받아라걍
    else:
        tail[0] = scar[0][0]
        tail[1] = scar[0][1]
        del scar[0]
    time += 1

    # 방향 바꾸는지 확인
    if not snake: # 빈 리스트 꼭꼭꼭 확인하기!!!!!!!!!!안하면 오류납니더
        continue
    if time == int(snake[0][0]):
        if snake[0][1] == 'D':
            cur_dir = D_dir[cur_dir]
        else:
            cur_dir = L_dir[cur_dir]
        del snake[0]

print(time+1)