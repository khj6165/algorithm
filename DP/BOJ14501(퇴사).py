n = int(input())
data = [list(map(int, input().split())) for _ in range(n)] # t, p

arr = [0]*(n+1)
maxValue = 0

for i in range(n):
    arr[i] += data[i][1]
    maxValue = max(maxValue, arr[i])
    term = data[i][0]
    if i+term > n:
        continue
    # arr[i] += data[i][1]
    arr[i+term] = max(arr[i+term], maxValue+data[i][1])

print(max(arr))
print(arr)