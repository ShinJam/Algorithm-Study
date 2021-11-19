import sys

n = int(input())
ip = [[], [], [], []]

for _ in range(n):
  ip_0, ip_1, ip_2, ip_3 = map(int, sys.stdin.readline().split('.'))
  ip[0].append(ip_0)
  ip[1].append(ip_1)
  ip[2].append(ip_2)
  ip[3].append(ip_3)

net_addr = [0, 0, 0, 0]
net_mask = [0, 0, 0, 0]

for i in range(4):
  if len(set(ip[i])) == 1:
    net_addr[i] = ip[i][0]
    net_mask[i] = 255

  else:
    min_ = min(ip[i])
    max_ = max(ip[i])

    m = len(bin(min_ ^ max_)) - 2
    subnet = int('1' * (8-m) + '0' * m, 2)

    net_addr[i] = subnet & min_
    net_mask[i] = subnet

    break

print(*net_addr, sep='.')
print(*net_mask, sep='.')


# f"{num:b}"
