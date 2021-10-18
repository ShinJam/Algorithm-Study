import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
alphabets = sorted(sys.stdin.readline().split())
aeiou = set(['a', 'e', 'i', 'o', 'u'])

for case in combinations(alphabets, L):
    s = set(case)
    if 1 <= len(s.intersection(aeiou)) <= L - 2:
        print(''.join(case))
