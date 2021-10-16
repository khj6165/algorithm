from itertools import combinations

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

nn = list(i for i in range(1, n+1))
ans = 999999
comb = list(combinations(nn, n//2))
length = len(comb)
for i in range(length//2):
    s, l = 0, 0
    start = list(combinations(comb[i], 2))
    link = list(combinations(comb[length-i-1], 2))
    for j in range(len(start)):
        s = s + data[start[j][0]-1][start[j][1]-1] + data[start[j][1]-1][start[j][0]-1]
        l = l + data[link[j][0]-1][link[j][1]-1] + data[link[j][1]-1][link[j][0]-1]
    ans = min(ans, abs(s-l))

print(ans)
