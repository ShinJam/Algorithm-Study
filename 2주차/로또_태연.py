import sys
from itertools import combinations


while True:
    N, *array = sys.stdin.readline().split()
    if N == '0':
        break

    for case in combinations(array, 6):
        print(' '.join(case))
    print()
