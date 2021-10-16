from itertools import permutations

n = int(input())
data = list(map(int, input().split()))
operator = list(map(int, input().split()))
arr = ['+', '-', '*', '/']
op_list = []
results = []

for i in range(4):
    k = operator[i]
    for j in range(k):
        op_list.append(arr[i])

perm = list(map(''.join, set(permutations(op_list))))
for p in perm:
    string = str(data[0])
    for i in range(len(p)):
        string = string + p[i] + str(data[i+1])
        result = int(eval(string))
        string = str(result)
    results.append(result)

print(max(results))
print(min(results))

