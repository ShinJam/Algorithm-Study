import sys
input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))


# 시작
max1, max2, max3 = data[0][0], data[0][1], data[0][2]
min1, min2, min3 = data[0][0], data[0][1], data[0][2]

for i in range(1, n):
    max1, max2, max3 = max(max1, max2) + data[i][0], max(max1, max2, max3) + data[i][1], max(max2, max3) + data[i][2]
    min1, min2, min3 = min(min1, min2) + data[i][0], min(min1, min2, min3) + data[i][1], min(min2, min3) + data[i][2]

print(max(max1, max2, max3), min(min1, min2, min3))
