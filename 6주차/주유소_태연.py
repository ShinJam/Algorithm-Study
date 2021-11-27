N = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = 0
min_oil = costs[0]
for locate in range(N - 1):
    if costs[locate] < min_oil:
        min_oil = costs[locate]
    result += (min_oil * roads[locate])

print(result)
