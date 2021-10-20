import sys
from math import inf
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))

MIN, MAX = inf, -inf
def dfs(cur, idx, plus, neg, mul, div):
    global MIN, MAX
    if idx == N:
        if cur < MIN:
            MIN = cur
        if cur > MAX:
            MAX = cur
    else:
        if plus:
            dfs(cur + A[idx], idx + 1, plus - 1, neg, mul, div)
        if neg:
            dfs(cur - A[idx], idx + 1, plus, neg - 1, mul, div)
        if mul:
            dfs(cur * A[idx], idx + 1, plus, neg, mul - 1, div)
        if div:
            dfs(int(cur / A[idx]), idx + 1, plus, neg, mul, div - 1)
    
        
dfs(A[0], 1, *ops)

print(MAX, MIN, sep='\n')
