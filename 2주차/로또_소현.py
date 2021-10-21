import sys
from itertools import combinations

while True:
    s = list(map(int, sys.stdin.readline().split()))

    if s[0] == 0:
        break

    for i in combinations(s[1:], 6):
        com = list(i)
        print(" ".join(map(str, com)))
    print()
