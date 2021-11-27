N = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))
info = list(zip(costs, dists)) # [(cost, dist)...]

sorted_info = sorted(enumerate(info), key=lambda x: x[1][0])

last = N - 1
cnt = 0
for idx, val in sorted_info:
    cost, dist = val
    for i in range(idx, last):
        cnt += (info[i][1] * cost)
        last = idx
print(cnt)
