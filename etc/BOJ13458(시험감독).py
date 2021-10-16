import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

ans = n

for i in a:
    i -= b
    if i <= 0:
        continue
    if i % c == 0:
        ans += i//c
    else:
        ans += i//c + 1
print(ans)