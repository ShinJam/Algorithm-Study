import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
findDict = {}

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if not findDict.get(a):
        findDict[a] = []
    if not findDict.get(b):
        findDict[b] = []
    findDict[b].append(a)

answer = []
MAX = 0
for k in range(1, N + 1):
    if findDict.get(k):
        if len(findDict[k]) == 0:
            total = 1
        else:
            visited = [False] * (N + 1)
            que = deque()
            que.append(k)
            visited[k] = True
            total = 0

            while que:
                Computer = que.popleft()
                total += 1
                for c in findDict[Computer]:
                    if not visited[c]:
                        que.append(c)
                        visited[c] = True
    else:
        total = 0

    if MAX < total:
        MAX = total
        answer = [k]
    elif MAX == total:
        answer.append(k)

print(*answer)
