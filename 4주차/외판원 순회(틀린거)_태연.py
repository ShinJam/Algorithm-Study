N = int(input())
A, B, C, D = [], [], [], []
X = []
for _ in range(N):
    a, b, c, d = list(map(int, input().rstrip().split('.')))
    temp = d + (c << 8) + (b << 16) + (a << 24)
    X.append(temp)

x = X[0]
locate = -1
for i in range(1, N):
    x &= X[i]

for i in range(N):
    temp = x ^ X[i]
    for j in range(31, -1, -1):
        if locate >= j:
            break
        if (1 << j) & temp >= 1:
            locate = j
            break

k = ((1 << 32) - 1) - (1 << (locate + 1))
temp &= k

temp = bin(x)[2:].zfill(32)
print(int("0b" + temp[:8], 2), end='.')
print(int("0b" + temp[8:16], 2), end='.')
print(int("0b" + temp[16:24], 2), end='.')
print(int("0b" + temp[24:], 2))

a = (1 << 32) - 1
b = (1 << (locate + 1)) - 1
temp = bin(a - b)[2:].rjust(32, "1")
print(int("0b" + temp[:8], 2), end='.')
print(int("0b" + temp[8:16], 2), end='.')
print(int("0b" + temp[16:24], 2), end='.')
print(int("0b" + temp[24:], 2))