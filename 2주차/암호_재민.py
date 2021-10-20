import sys
input =sys.stdin.readline

L, C = map(int, input().split())
chars = sorted(input().split())

def case(idx,n, cur=''):
    if n == 0:
        za = set(cur) - {'a', 'e', 'i', 'o', 'u'}
        mo = set(cur) - za
        if len(za) >= 2 and len(mo) >=1:
            print(cur)
        return
    if idx >= C:
        return
    case(idx+1, n-1, cur+chars[idx])
    case(idx+1, n, cur)
case(0, n=L)
