def findbit(numbers):
    max_ = max(numbers)
    min_ = min(numbers)
    ip = 0
    k = max_ ^ min_
    t = 7
    while True:
        if (k & (1 << t)) >= 1:
            break
        ip += (max_ & (1 << t))
        t -= 1

    bitmask = ((1 << 8) - 1) - ((1 << (t + 1)) - 1)
    return ip, bitmask

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    temp = list(map(int, input().rstrip().split('.')))
    A.append(temp[0])
    B.append(temp[1])
    C.append(temp[2])
    D.append(temp[3])

ip_address = []
network_mask = []

if len(set(A)) == 1:
    ip_address.append(str(A[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(A)
    ip_address.extend([str(ip), str(0), str(0), str(0)])
    network_mask.extend([str(bitmask), str(0), str(0), str(0)])
    print('.'.join(ip_address))
    print('.'.join(network_mask))
    exit(0)

if len(set(B)) == 1:
    ip_address.append(str(B[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(B)
    ip_address.extend([str(ip), str(0), str(0)])
    network_mask.extend([str(bitmask), str(0), str(0)])
    print('.'.join(ip_address))
    print('.'.join(network_mask))
    exit(0)

if len(set(C)) == 1:
    ip_address.append(str(C[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(C)
    ip_address.extend([str(ip), str(0)])
    network_mask.extend([str(bitmask), str(0)])
    print('.'.join(ip_address))
    print('.'.join(network_mask))
    exit(0)

if len(set(D)) == 1:
    ip_address.append(str(D[0]))
    network_mask.append(str(255))
else:
    ip, bitmask = findbit(D)
    ip_address.append(str(ip))
    network_mask.append(str(bitmask))

print('.'.join(ip_address))
print('.'.join(network_mask))


# N = int(input())
# A, B, C, D = [], [], [], []
# X = []
# for _ in range(N):
#     a, b, c, d = list(map(int, input().rstrip().split('.')))
#     temp = d + (c << 8) + (b << 16) + (a << 24)
#     X.append(temp)
#
# max_ = max(X)
# min_ = min(X)
# temp = bin(max_ & min_)[2:].zfill(32)
# print(int("0b" + temp[:8], 2), end='.')
# print(int("0b" + temp[8:16], 2), end='.')
# print(int("0b" + temp[16:24], 2), end='.')
# print(int("0b" + temp[24:], 2))
#
# temp = max_ ^ min_
# net = ''
# token = False
# for bit in range(31, -1, -1):
#     if temp & (1 << bit) >= 1 or token:
#         net += '0'
#         token = True
#     else:
#         net += '1'
# temp = net
# print(int("0b" + temp[:8], 2), end='.')
# print(int("0b" + temp[8:16], 2), end='.')
# print(int("0b" + temp[16:24], 2), end='.')
# print(int("0b" + temp[24:], 2))
# x = X[0]
# locate = set()
# for i in range(1, N):
#     x &= X[i]
#
# for i in range(N):
#     temp = x ^ X[i]
#     for j in range(31, -1, -1):
#         if (1 << j) & temp >= 1:
#             locate.add(j)
#
# temp = bin(x)[2:].zfill(32)
# print(int("0b" + temp[:8], 2), end='.')
# print(int("0b" + temp[8:16], 2), end='.')
# print(int("0b" + temp[16:24], 2), end='.')
# print(int("0b" + temp[24:], 2))
#
# temp = (1 << 32) - 1
# for bit in locate:
#     temp -= (1 << bit)
# temp = bin(temp)[2:].rjust(32, "1")
# print(int("0b" + temp[:8], 2), end='.')
# print(int("0b" + temp[8:16], 2), end='.')
# print(int("0b" + temp[16:24], 2), end='.')
# print(int("0b" + temp[24:], 2))
#
# a = (1 << 32) - 1
# b = (1 << (locate + 1)) - 1
#
#
#     for j in range(7, -1, -1):
#         1 << j

# print(aa, bb, cc, dd)
# tokenA, tokenB, tokenC, tokenD = False, False, False, False
# X, Y, Z, W = [], [], [], []
# for i in range(N):
#     aa ^= A[i]
#     bb ^= B[i]
#     cc ^= C[i]
#     dd ^= D[i]
#     for j in range(7, -1, -1):
#         if not tokenA and aa & (1 << j) == 1:
#             X.append(j)
#             tokenA = True
#         if not tokenB and bb & (1 << j) == 1:
#             Y.append(j)
#             tokenB = True
#         if not tokenC and cc & (1 << j) == 1:
#             Z.append(j)
#             tokenC = True
#         if not tokenD and dd & (1 << j) == 1:
#             W.append(j)
#             tokenD = True
