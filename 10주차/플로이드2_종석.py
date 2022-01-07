# 어렵네요.. 못품 ㅠ

n = int(input())
m = int(input())
bus_info = [list(map(int , input().split())) for _ in range(m)]
node_dict = {}
lst = [[float('inf')] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        node_dict[(i+1, j+1)] = []
for i in range(n):
    lst[i][i] = 0

for a, b, c in bus_info:
    lst[a-1][b-1] = min(lst[a-1][b-1], c)
    if a not in node_dict[(a, b)]:
        node_dict[(a, b)].append(a)
    if b not in node_dict[(a, b)]:
        node_dict[(a, b)].append(b)

print(node_dict)
for k in range(n):
    for x in range(n):
        for y in range(n):

            if lst[x][y] > lst[x][k] + lst[k][y]:
                print((x+1, y+1) , node_dict[(x+1, k+1)] , node_dict[(y+1, k+1)])
                lst[x][y] = lst[x][k] + lst[k][y]
                node_dict[(x+1, y+1)].extend(node_dict[(x+1, k+1)])
                node_dict[(x+1, y+1)].extend(node_dict[(y+1, k+1)])
                node_dict[(x+1, y+1)] = list(set(node_dict[(x+1, y+1)]))

print(node_dict)

