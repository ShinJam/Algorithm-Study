import sys

n = int(sys.stdin.readline())
stick = [64, 32, 16, 8, 4, 2, 1]
result = 0

for i in stick:
    while n-i >= 0:
        n -= i
        result += 1
print(result)
