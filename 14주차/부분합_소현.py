import sys
input = sys.stdin.readline

n, s = map(int, input().split())
data = list(map(int, input().split()))

count = 100000
interval_sum = 0
end = 0

for start in range(n):

    while interval_sum < s and end < n:
        interval_sum += data[end]
        end += 1

    if interval_sum >= s:
        count = min(count, end - start)
    interval_sum -= data[start]

if count == 100000:
    print(0)
else:
    print(count)
