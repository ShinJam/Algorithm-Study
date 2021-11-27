from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
ingredient = [list(map(int, input().split())) for _ in range(N)]
plant = [[5] * N for _ in range(N)]
dxy = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

tree = [[deque() for _ in range(N)] for _ in range(N)]
dead_tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    tx, ty, year = list(map(int, input().split()))
    tree[tx - 1][ty - 1].append(year)

for _ in range(K):
    # 봄
    for i in range(N):
        for j in range(N):
            k = len(tree[i][j])
            for m in range(k):
                if plant[i][j] < tree[i][j][m]:
                    for _ in range(m, k):
                        dead_tree[i][j].append(tree[i][j].pop())
                    break
                else:
                    plant[i][j] -= tree[i][j][m]
                    tree[i][j][m] += 1

    # 여름
    for i in range(N):
        for j in range(N):
            k = len(dead_tree[i][j])
            for _ in range(k):
                plant[i][j] += (dead_tree[i][j].pop() // 2)

    # 가을
    for x in range(N):
        for y in range(N):
            k = len(tree[x][y])
            for m in range(k):
                if tree[x][y][m] % 5 == 0:
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].appendleft(1)

            # 겨울
            plant[x][y] += ingredient[x][y]

result = 0
for i in range(N):
    for j in range(N):
        result += len(tree[i][j])
print(result)
