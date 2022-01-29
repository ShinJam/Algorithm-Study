from math import inf

N = int(input())
samples = list(map(int, input().split()))
samples.sort()

l, r = 0, N-1
crit = inf
ret = []
while l<r:
    ck = samples[l] + samples[r]
    if crit > abs(ck):
        crit = abs(ck)
        ret = sorted([samples[l], samples[r]])
    if ck > 0:
        r -= 1
    else:
        l += 1
print(*ret)
