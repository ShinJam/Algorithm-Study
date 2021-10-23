import sys


def dfs(depth, stack):
  if len(stack) >= 6:
    print(*stack)
    return

  if depth >= k:
    return

  stack.append(seq[depth])
  dfs(depth + 1, stack)
  stack.pop()
  dfs(depth + 1, stack)


while True:
  seq = list(map(int, sys.stdin.readline().split()))
  k = seq.pop(0)
  if k == 0:
    break

  dfs(0, [])
  print()
