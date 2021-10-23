import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alpha = sorted(list(map(str, sys.stdin.readline().split())))

moum = ['a', 'e', 'i', 'o', 'u']

for i in combinations(alpha, L):
    count = 0
    for johap in i:
        if johap in moum:
            count += 1

    if (count >= 1) and (len(i) - count >= 2):
        print(''.join(i))
