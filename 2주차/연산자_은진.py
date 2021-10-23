import sys

n = int(input())
seq = list(map(int, sys.stdin.readline().split()))
oper = list(map(int, sys.stdin.readline().split()))
res = [-int(10e9), int(10e9)]


def dfs(depth, num):
  if depth >= n:
    res[0] = max(res[0], num)
    res[1] = min(res[1], num)
    return

  for i in range(4):
    if oper[i] == 0:
      continue
    oper[i] -= 1

    if i == 0:
      dfs(depth + 1, num + seq[depth])
    elif i == 1:
      dfs(depth + 1, num - seq[depth])
    elif i == 2:
      dfs(depth + 1, num * seq[depth])
    elif i == 3:
      dfs(depth + 1, int(num / seq[depth]))

    oper[i] += 1


dfs(1, seq[0])
print(res[0])
print(res[1])
