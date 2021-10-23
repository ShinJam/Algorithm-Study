# combinations
import sys
from itertools import combinations

L, C = map(int, input().split())
alpha = sorted(input().split())
words = combinations(alpha, L)

for word in words:
    cnt_vow = 0
    for i in word:
        if i in "aeiou":
            cnt_vow += 1

    if cnt_vow >= 1 and L - cnt_vow >= 2:
        print(''.join(word))


# dfs
def dfs(depth, stack, vowel):
    if len(stack) >= l:
        if (vowel >= 1) and (l - vowel >= 2):
            print(''.join(stack))
        return

    if depth >= c:
        return

    stack.append(seq[depth])
    if seq[depth] in 'aeiou':
        dfs(depth+1, stack, vowel + 1)
    else:
        dfs(depth+1, stack, vowel)

    stack.pop()
    dfs(depth+1, stack, vowel)


if __name__ == "__main__":
    l, c = map(int, sys.stdin.readline().split())
    seq = sorted(sys.stdin.readline().split())

    dfs(0, [], 0)
