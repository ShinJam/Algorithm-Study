from itertools import combinations

while True:
    k, *s = map(int, input().split())
    if k == 0:
        break
    case = combinations(s, 6)
    for c in case:
        print(*c)
    print()
